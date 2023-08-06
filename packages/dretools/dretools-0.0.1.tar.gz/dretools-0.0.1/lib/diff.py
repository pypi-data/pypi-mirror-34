from lib.parsers import generate_snvs
from collections import namedtuple
from random import randint, random
from lib.io import shared_params
from lib.shared import passes_min_coverage, passes_min_editing, get_strand, base_transition_tuples_and_titles, passes_max_percent_editing
from pysam import AlignmentFile, Fastafile
from statistics import mean, stdev
from lib.parsers import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
from lib.parsers import SampleGroup
from scipy.stats import ttest_ind, combine_pvalues, norm
from math import floor

FILE_DELIMITER = ","

import warnings
warnings.filterwarnings("ignore")

r_script = """

dataFrame1 <- data.frame(
    siteEPK=c(100,105,110,114,56,73,0,110),
    repAvgEPK=c(50,51,52,53,27,26,25,38),
    size=c(100,101,102,103,104,105,106,107),
    depth=c(5,5.1,5.2,5.3,5.4,5.5,5.6,5.7),
    group=c(rep("A",4),rep("B",4))
)

minVal<-min(dataFrame1$siteEPK[dataFrame1$siteEPK>0])/2
dataFrame1$siteEPK[dataFrame1$siteEPK<=0] <- minVal
dataFrame1$logSiteEPK                     <- log(dataFrame1$siteEPK)
dataFrame1$logRepAvgEPK                   <- log(dataFrame1$repAvgEPK)

lm1 <- lm(logSiteEPK~logRepAvgEPK+size+depth+group,data=dataFrame1)

pValue <- summary(lm1)$coefficients['groupB','Pr(>|t|)']

"""


def make_groups(dict_of_groups, labels=None):
    """
    { "bam": ["bam1,bam2", "bam3,bam4"]
    {
        "group_1": {"vcf":[vcf_1, vcf_2], "bam":[bam_1, bam_2]}
        "group_2": {"vcf":[vcf_3, vcf_4], "bam":[bam_3, bam_4]}
    }

    :param dict_of_groups:
    :return:
    """

    sorted_keys = sorted(dict_of_groups)

    if labels:
        labels = ",".split(FILE_DELIMITER)
    else:
        first_label_groups = len(dict_of_groups[sorted_keys[0]])
        labels = []
        for i in range(1, first_label_groups+1):
            labels.append("Group_%s" % i)

    group_names = []
    for dict_key in sorted(dict_of_groups):
        group_names.append(dict_key)

    print(group_names)

    GroupObj = namedtuple('GroupObj', group_names)

    g = GroupObj(["1", "3"], ["2", "4"])
    print(g)
    print(GroupObj)

    groups = []
    for i in range(len(labels)):
        tmp_list = []
        for sorted_key in sorted_keys:
            tmp_list.append(dict_of_groups[sorted_key][i].split(","))

        print(tmp_list)

        groups.append(GroupObj(*tmp_list))
    return groups


def build_grouped_sample_data_structure(list_of_grouped_samples, delimiter=","):
    """ Build an ordered nested data structure of groups with samples files contained within.

    :param list_of_grouped_samples:
    :param delimiter:
    :return:
    """
    return [group.split(delimiter) for group in list_of_grouped_samples]


def site_level_differential_editing_decision_function(group_1, group_2, coverage_1, coverage_2):

    choices = ["YES", "NO", "NO_TEST"]

    return choices[randint(0, 2)], random()


def find_total_area_covered(n, file_name):
    total_area = 0
    for line in open(file_name):
        sl = line.split()
        if sl[0] == "genome" and int(sl[1]) >= n:
            total_area += int(sl[2])
    return total_area


def find_coverage(info):
    return int(info.split("DP=")[-1].split(";")[0])


def normalized_editing(sites, total_area_covered):
    return round((sites * 1.0e6) / total_area_covered, 5)


def resolve_names(names, default_groups):
    """

    :param names:
    :param default_groups:
    :return:
    """
    if names:
        group_names = names[0].split(",")
    else:
        group_names = [str(group_int) for group_int in range(len(default_groups))]
    return group_names


def sample(parser):
    """ Normalize the editing rates among samples based on the entire sample.

    chromosome  depth   bps_covered_by  percent
    1   0   218256120  248956422    0.876684
    1   1   9532255    248956422    0.0382889
    1   2   4797353    248956422    0.0192699
    1   3   2582708    248956422    0.0103741

    hekase sanorm --names    SRR2087305,SRR1998058,SRR2087291                          \\
                  --vcf      SRR2087305.vcf SRR1998058.vcf SRR2087291.vcf              \\
                  --coverage SRR2087305.cov.tsv SRR1998058.cov.tsv SRR2087291.cov.tsv  \\

    """

    r_script = """

    library(lme4)
    library(lmerTest)
    library(stringr)

    df1 <- list()

    df1$Counts      <- Counts
    df1$Area        <- Area
    df1$Coverage    <- Coverage

    df1$id        <- id
    df1$group     <- group_id

    df1$Area             <-log(df1$Area)
    df1$area_squared     <-df1$Area**2
    df1$coverage_squared <-df1$Coverage**2
    df1$area_cubed       <-df1$Area**3

    lm3me <- lmer(Counts ~ Area + areaSq + areaCub + Coverage + Coverage:Area + Area*type+(1|id), data=df1)

    #lm3me <- lmer(Counts ~ Area + area_squared + area_cubed + Coverage + Coverage:Area + (1|id), data=df1)

    coef1 <- as.matrix(coef(lm3me)$id[1,])

    df1$pred <- mean(coef(lm3me)$id[,1]) +
                coef1[,'Area'] * df1$Area +
                coef1[,'area_squared'] * df1$area_squared +
                coef1[,'area_cubed'] * df1$area_cubed +
                coef1[,'Coverage'] * df1$Coverage +
                coef1[,'Area:Coverage'] * df1$Area * df1$Coverage

    preds <- df1$pred

    ############# Statistical test #############   lmer anova

    df1$norm <- df1$pred - df1$Counts
    norm <- df1$norm

    lm4me <- update(lm3me,.~.+group)

    # print(lm4me)
    # lm4me_summary <- summary(lm4me)

    lm4me_anova <- anova(lm4me)

    p_value <- lm4me_anova["Pr(>F)"][[1]][[5]]

    """

    import rpy2.robjects as robjects
    import numpy as np
    from rpy2.robjects import Formula
    from rpy2.robjects import Environment
    from rpy2.robjects import StrVector, IntVector, FloatVector
    # from rpy2 import robjects
    # from rpy2.robjects import lme4
    # import rpy2's package module
    import rpy2.robjects.packages as rpackages
    # lme4 = rpackages.importr('lme4')
    lme = rpackages.importr('lmerTest')
    from lib.shared import determine_aggregation_depth

    shared_params(parser, gtf=False, bed=True)

    args = parser.parse_args()

    assert len(args.coverage) == len(args.vcf)

    vcf_groups = args.vcf
    coverage_groups = args.coverage
    vcf_groups = build_grouped_sample_data_structure(vcf_groups)
    coverage_groups = build_grouped_sample_data_structure(coverage_groups)

    # =============================================================================================
    # Determine depth to begin aggregation.
    # After a certain depth more reads will negligibly increase the change of detecting editing.
    # =============================================================================================
    min_coverage = int(args.min_coverage)
    min_editing = int(args.min_editing)
    max_cov = float(args.max_editing)
    max_depth = determine_aggregation_depth(min_editing)

    max_cl = 30

    # Decide what the group names should be.
    group_names = resolve_names(args.names, vcf_groups)

    tmp_list = [group_int for group_int in range(len(vcf_groups))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    sample_groups_obj = SampleGroup(min_editing=min_editing, min_coverage=min_coverage, max_percent_coverage=max_cov)

    for group_name_i in range(len(group_names)):

        sample_groups_obj.add_group(
            group_name=group_names[group_name_i],
            vcf_file_list=vcf_groups[group_name_i],
            coverage_file_list=coverage_groups[group_name_i],
            alignment_file_list=None
        )

    # =============================================================================================
    # Compare Groups
    # =============================================================================================
    p_value = ""
    max_val = 50
    coverage_bins_all = list(sorted(sample_groups_obj.get_coverage_bins()))
    coverage_bins = []
    for cba in coverage_bins_all:
        if cba < max_val:
            coverage_bins.append(cba)

    titles = [
        "group_1_name",
        "group_2_name",
        "ECPM_1",
        "ECPM_2",
        "p-val"
    ]
    print("\t".join(titles))
    # remove largest values
    for group_1_name, group_2_name in sample_groups_obj.get_group_comparison_tuples():

        tmp_id_list = []
        tmp_group_names = []
        tmp_exp_type_list = []
        tmp_es_cnt = []
        tmp_area_covered = []
        tmp_coverage_level = []

        avg_group_ecpm = {}
        for group_name in [group_1_name, group_2_name]:

            # Get group vals group_name
            group_average_vals = []

            for sample_name in sample_groups_obj.get_samples_in_group(group_name):
                sample_id = sample_name.get_file_name()

                tmp_avg_ecpm = []
                tmp_avg_cov = []
                for coverage_level in coverage_bins:
                    area_covered_at_level = sample_name.get_area_covered_by_n_reads(coverage_level)
                    editing_sites_at_level = sample_name.get_editing_sites_covered_by_n_reads(coverage_level)

                    if coverage_level < max_cl:
                        tmp_avg_ecpm.append( (editing_sites_at_level*1e6)/area_covered_at_level  )
                        tmp_avg_cov.append(area_covered_at_level)

                    tmp_id_list.append(sample_id)
                    tmp_group_names.append(group_name)
                    tmp_exp_type_list.append(group_name)

                    tmp_es_cnt.append(editing_sites_at_level)
                    tmp_area_covered.append(area_covered_at_level)
                    tmp_coverage_level.append(coverage_level)
                try:
                    group_average_vals.append(np.average(tmp_avg_ecpm, weights=tmp_avg_cov))
                except:
                    group_average_vals.append(-1.0)
            avg_group_ecpm[group_name] = np.average(group_average_vals)

        # ====================================================================
        #                     Add data to R environment.
        # ====================================================================

        robjects.globalenv['id'] = StrVector(tmp_id_list)
        robjects.globalenv['group_id'] = StrVector(tmp_group_names)
        robjects.globalenv['exp_type_list'] = StrVector(tmp_exp_type_list)
        robjects.globalenv['Counts'] = FloatVector(tmp_es_cnt)
        robjects.globalenv['Area'] = FloatVector(tmp_area_covered)
        robjects.globalenv['Coverage'] = FloatVector(tmp_coverage_level)

        # ====================================================================
        #                     Evaluate statistical test
        # ====================================================================
        robjects.r(r_script)

        p_value = robjects.globalenv["p_value"][-1]

        out_list = [
            group_1_name,
            group_2_name,
            str(round(avg_group_ecpm[group_1_name], 5)),
            str(round(avg_group_ecpm[group_2_name], 5)),
            str(round(p_value, 5))
        ]

        print("\t".join(out_list))


def filter_bases(bases, min_coverage=5):
    """

    :param bases:
    :param min_coverage:
    :param alt_cnt:
    :return:
    """
    group_over_cutoff = []
    group_over_cutoff_alt = []
    total_coverage = 0
    for tmp_sample_name in bases:
        ref_cnt = float(bases[tmp_sample_name][0])
        alt_cnt = float(bases[tmp_sample_name][1])
        total = ref_cnt + alt_cnt
        if total >= min_coverage:  # and alt_cnt >= min_editing
            total_coverage += total
            group_over_cutoff.append(alt_cnt / total)
            group_over_cutoff_alt.append(alt_cnt)

    return group_over_cutoff, total_coverage


def decide_outcome(p_value_1, group_1, p_value_2, group_2, cutoff=0.05):

    if p_value_1 <= 0.05:
        return p_value_1, group_1
    elif p_value_2 <= 0.05:
        return p_value_2, group_2
    else:
        return sorted([p_value_1, p_value_2])[0], "NONS"


def generate_group_pairs(group_list):
    # Make Comparison Groups
    group_pair_list = []

    tmp_list = list(sorted(group_list))
    while tmp_list:
        name_1 = tmp_list.pop(0)
        for name_2 in tmp_list:
            group_pair_list.append((name_1, name_2))

    return group_pair_list


def region_diff(parser):
    """ Check for significant differences in editing within genomic regions among samples.

    :param parser:
    :return:
    """

    from lib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    import rpy2.robjects.packages as rpackages

    from lib.parsers import EditingInSample
    # from import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
    r_script = """

    df1<-data.frame(
       group=group_ids,
       sampleEPK=sample_epk,
       regionEPK=region_epk,
       regionSize=region_size,
       regionDepth=region_depth
    )

    minVal <- min( df1$regionEPK[df1$regionEPK>0] ) / 2
    df1$regionEPK[df1$regionEPK<=0] <- minVal
    df1$logRegionEPK <-log(df1$regionEPK)
    df1$logSampleEPK <-log(df1$sampleEPK)

    lm1<-lm(logRegionEPK ~ logSampleEPK + regionSize + regionDepth + group, data=df1)
    #lm1<-lm(logRegionEPK ~ logSampleEPK + group, data=df1)

    p_value <- summary(lm1)$coefficients

    """
    parser.add_argument(
        "--regions",
        type=str,
        help="")

    parser.add_argument(
        "--stat-file",
        type=str,
        default=None,
        help="")

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--max-depth-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--min-area",
        type=float,
        default=20,
        help="")

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help="")

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--region-epk",
        nargs='+',
        type=str,
        help="")

    args = parser.parse_args()

    bed_path = args.regions

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    region_epk = build_grouped_sample_data_structure(args.region_epk)

    # max_cl = 30
    # Decide what the group names should be.
    # Returns a list of group names.
    # Will be a list of comma separated names provided to the names parameter or a list of integers.
    group_names = resolve_names(args.names, sample_epk)

    tmp_list = [group_int for group_int in range(len(sample_epk))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    groups_dict = {}
    min_samples_in_group = len(group_names[0])

    for group_i in range(len(group_names)):

        number_of_samples = len(sample_epk[group_i])

        if number_of_samples < min_samples_in_group:
            min_samples_in_group = number_of_samples

        for sample_i in range(number_of_samples):
            epk_in_sample = sample_epk[group_i][sample_i]
            epk_in_region = region_epk[group_i][sample_i]

            editing_obj = EditingInSample(epk_in_sample, epk_in_region)

            tmp_group_name = group_names[group_i]
            try:
                groups_dict[tmp_group_name].append(editing_obj)
            except KeyError:
                groups_dict[tmp_group_name] = [editing_obj]

    # Get a a tuple of all possible sets of two groups.
    group_comparisons = generate_group_pairs(group_names)

    bed_obj = BED(bed_path)
    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    min_average_depth = args.min_depth
    min_editing_area = args.min_area
    max_coverage_cov = args.max_coverage_cov
    max_depth_cov = args.max_depth_cov

    for record in bed_obj.yield_lines():

        for group_1_name, group_2_name in group_comparisons:

            region_epks, sample_epks, region_size, region_avg_depth, group_ids = [], [], [], [], []
            val_dict = {}

            for tmp_group_name in (group_1_name, group_2_name):
                if tmp_group_name not in val_dict:
                    val_dict[tmp_group_name] = []

                for tmp_sample in groups_dict[tmp_group_name]:

                    tmp_region_depth = tmp_sample.get_region_depth(record.name)

                    if tmp_region_depth > min_average_depth:
                        region_avg_depth.append(tmp_region_depth)
                        group_ids.append(tmp_group_name)
                        sample_epks.append(tmp_sample.get_sample_epk())
                        # Region-wise data.
                        tmp_region_epk = tmp_sample.get_region_epk(record.name)
                        region_epks.append(tmp_sample.get_region_epk(record.name))
                        region_size.append(tmp_sample.get_region_size(record.name))

                        val_dict[tmp_group_name].append(tmp_region_epk)

            # When zero editing is detectable in regions this will cause errors when calculating stddev.
            at_least_one_region_has_editing = sum(region_epks) > 0

            # Make sure we can test at least almost half of the samples.
            min_samples_for_testability = floor(min_samples_in_group/2)
            min_samples_for_testability = 2 if  min_samples_for_testability <= 1 else min_samples_for_testability
            group_1_is_testable = len(val_dict[group_1_name]) > min_samples_for_testability
            group_2_is_testable = len(val_dict[group_2_name]) > min_samples_for_testability

            if at_least_one_region_has_editing and group_1_is_testable and group_2_is_testable:

                area_cov = stdev(region_size)/mean(region_size)
                depth_cov = stdev(region_avg_depth)/mean(region_avg_depth)
                region_max_editing_area = sorted(region_size)[-1]

                if area_cov < max_coverage_cov and min_editing_area < region_max_editing_area and depth_cov < max_depth_cov:

                    testable += 1
                    #print(record.name)
                    #print("group_ids", group_ids)
                    #print("sample_epks", sample_epks)
                    #print("region_epks", region_epks)
                    #print("region_size", region_size)
                    #print("region_avg_depth", region_avg_depth)
                    robjects.globalenv['group_ids'] = StrVector(group_ids)
                    robjects.globalenv['region_depth'] = FloatVector(region_avg_depth)
                    robjects.globalenv['sample_epk'] = FloatVector(sample_epks)
                    robjects.globalenv['region_epk'] = FloatVector(region_epks)
                    robjects.globalenv['region_size'] = FloatVector(region_size)

                    robjects.r(r_script)

                    p_value = robjects.globalenv["p_value"][-1]

                    if p_value < 0.05:
                        rpvalcnt += 1

                    g1_mean = mean(val_dict[group_1_name])
                    g2_mean = mean(val_dict[group_2_name])

                    ttest_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                    if ttest_results[1] < 0.05:
                        tpvalcnt += 1

                    print(
                        "\t".join(
                         [
                             group_1_name,
                             group_2_name,
                             record.name,
                             record.chromosome+":"+str(record.start)+"-"+str(record.end),
                             str(round(g1_mean, 2)),
                             str(round(g2_mean, 2)),
                             str(round(p_value, 7)),
                             str(round(ttest_results[1], 7))
                          ]
                        )
                    )

    # print("# rpvalcnt", rpvalcnt)
    # print("# tpvalcnt", tpvalcnt)
    # print("# testable", testable)
    # print("# COV Cutoff:", cov_cutoff)
    # print("# lm",    rpvalcnt/float(testable))
    # print("# ttest", tpvalcnt/float(testable))



def editing_site_diff(parser):
    """ Check for significant differences in editing of individual sites among samples.

    Sample_A1,Sample_A2  Sample_B1,Sample_B2  Sample_C1,Sample_C2

    """

    from lib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    # import rpy2.robjects.packages as rpackages
    from lib.parsers import EditingInSample

    # from import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
    r_script = """

    df1<-data.frame(
       group=group_ids,
       sampleEPK=sample_epk,
       regionEPK=region_epk,
       regionSize=region_size,
       regionDepth=region_depth
    )

    minVal <- min( df1$regionEPK[df1$regionEPK>0] ) / 2
    df1$regionEPK[df1$regionEPK<=0] <- minVal
    df1$logRegionEPK <-log(df1$regionEPK)
    df1$logSampleEPK <-log(df1$sampleEPK)

    lm1<-lm(logRegionEPK ~ logSampleEPK + regionSize + regionDepth + group, data=df1)

    p_value <- summary(lm1)$coefficients

    """

    # shared_params(parser, gtf=False, editing_islands=False, bed=True, genome=True)

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help="")

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--vcf",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.50,
        help="")

    args = parser.parse_args()

    # alignment_groups = args.alignment
    # vcf_groups = args.vcf
    # coverage_groups = args.coverage

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    vcf_edited = build_grouped_sample_data_structure(args.vcf)

    # vcf_groups = build_grouped_sample_data_structure(vcf_groups)
    # coverage_groups = build_grouped_sample_data_structure(coverage_groups)
    # alignment_groups = build_grouped_sample_data_structure(alignment_groups)

    # min_coverage = int(args.min_coverage)
    # min_editing = int(args.min_editing)
    # max_cov = float(args.max_editing)
    # max_depth = determine_aggregation_depth(min_editing)
    # reference_genome = Fastafile(args.genome)

    # max_cl = 30

    # Decide what the group names should be.
    # Returns a list of group names.
    # Will be a list of comma separated names provided to the names parameter or a list of integers.
    group_names = resolve_names(args.names, sample_epk)

    tmp_list = [group_int for group_int in range(len(sample_epk))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    groups_dict = {}
    min_samples_in_group = len(group_names[0])

    for group_i in range(len(group_names)):

        number_of_samples = len(sample_epk[group_i])

        if number_of_samples < min_samples_in_group:
            min_samples_in_group = number_of_samples

        for sample_i in range(number_of_samples):

            epk_in_sample = sample_epk[group_i][sample_i]
            epk_in_site = vcf_edited[group_i][sample_i]

            editing_obj = EditingInSample(epk_in_sample, region_epk_file=None, vcf_file=epk_in_site)

            tmp_group_name = group_names[group_i]
            try:
                groups_dict[tmp_group_name].append(editing_obj)
            except KeyError:
                groups_dict[tmp_group_name] = [editing_obj]

    group_comparisons = generate_group_pairs(group_names)

    # bed_obj = BED(bed_path)

    name_list = {}
    for tmp_group_name in group_names: # group_comparisons:
        for tmp_sample in groups_dict[tmp_group_name]:
            for tmp_record_name, tmp_record in tmp_sample.yield_editing_sites():
                try:
                    name_list[tmp_record_name] += 1
                except KeyError:
                    name_list[tmp_record_name] = 1

    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    for record in name_list:

        for group_1_name, group_2_name in group_comparisons:
            region_epks = []
            sample_epks = []
            region_size = []
            region_avg_depth = []
            group_ids = []
            val_dict = {}

            for tmp_group_name in (group_1_name, group_2_name):

                if tmp_group_name not in val_dict:
                    val_dict[tmp_group_name] = []

                for tmp_sample in groups_dict[tmp_group_name]:

                    tmp_avg_depth = tmp_sample.get_site_depth(record)
                    if tmp_avg_depth > args.min_depth:
                        region_avg_depth.append(tmp_avg_depth)

                        group_ids.append(tmp_group_name)
                        sample_epks.append(tmp_sample.get_sample_epk())
                        region_size.append(1.0)

                        # Region-wise data.
                        tmp_region_epk = tmp_sample.get_site_epk(record)
                        region_epks.append(tmp_region_epk)
                        val_dict[tmp_group_name].append(tmp_region_epk)

            min_s = floor(min_samples_in_group/2)
            if len(val_dict[group_1_name]) > min_s and len(val_dict[group_2_name]) > min_s:

                cov_cutoff = args.max_coverage_cov
                max_depth_cov = args.max_coverage_cov

                if sum(region_epks) > 0:
                    area_cov = stdev(region_size) / mean(region_size)
                    depth_cov = stdev(region_avg_depth) / mean(region_avg_depth)

                    if area_cov < cov_cutoff and depth_cov < max_depth_cov:
                        testable += 1

                        robjects.globalenv['group_ids'] = StrVector(group_ids)
                        robjects.globalenv['sample_epk'] = FloatVector(sample_epks)

                        robjects.globalenv['region_epk'] = FloatVector(region_epks)
                        robjects.globalenv['region_size'] = FloatVector(region_size)
                        robjects.globalenv['region_depth'] = FloatVector(region_avg_depth)

                        robjects.r(r_script)

                        p_value = robjects.globalenv["p_value"][-1]
                        if p_value < 0.05:
                            rpvalcnt += 1

                        t_test_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                        if t_test_results[1] < 0.05:
                            tpvalcnt += 1

                        g1_mean = mean(val_dict[group_1_name])
                        g2_mean = mean(val_dict[group_2_name])

                        print(
                            "\t".join(
                                [
                                    group_1_name,
                                    group_2_name,
                                    record,
                                    record,
                                    str(round(g1_mean, 2)),
                                    str(round(g2_mean, 2)),
                                    str(round(p_value, 7)),
                                    str(round(t_test_results[1], 7))
                                ]
                            )
                        )
    # if stat-file
    #print("#", rpvalcnt)
    #print("#", tpvalcnt)
    #print("#", testable)
    # print("#COV Cutoff:", cov_cutoff)
    #print("#lm", rpvalcnt / float(testable))
    #print("#ttest", tpvalcnt / float(testable))


def es_diff_diff(parser):
    """ Check for significant differences in editing within genomic regions among samples.

    :param parser:
    :return:
    """

    from lib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    import rpy2.robjects.packages as rpackages

    from lib.parsers import EditingInSample
    # from import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
    r_script = """

    df1<-data.frame(
       group=group_ids,
       sampleEPK=sample_epk,
       regionEPK=region_epk,
       regionSize=region_size,
       regionDepth=region_depth
    )

    minVal <- min( df1$regionEPK[df1$regionEPK>0] ) / 2
    df1$regionEPK[df1$regionEPK<=0] <- minVal
    df1$logRegionEPK <-log(df1$regionEPK)
    df1$logSampleEPK <-log(df1$sampleEPK)

    lm1<-lm(logRegionEPK ~ logSampleEPK + regionSize + regionDepth + group, data=df1)
    #lm1<-lm(logRegionEPK ~ logSampleEPK + group, data=df1)

    p_value <- summary(lm1)$coefficients

    """
    parser.add_argument(
        "--sites",
        type=str,
        help="")

    parser.add_argument(
        "--stat-file",
        type=str,
        default=None,
        help="")

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--max-depth-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--min-area",
        type=float,
        default=20,
        help="")

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help="")

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--site-epk",
        nargs='+',
        type=str,
        help="")

    args = parser.parse_args()

    bed_path = args.sites

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    region_epk = build_grouped_sample_data_structure(args.site_epk)

    # max_cl = 30
    # Decide what the group names should be.
    # Returns a list of group names.
    # Will be a list of comma separated names provided to the names parameter or a list of integers.
    group_names = resolve_names(args.names, sample_epk)

    tmp_list = [group_int for group_int in range(len(sample_epk))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    groups_dict = {}
    min_samples_in_group = len(group_names[0])

    for group_i in range(len(group_names)):

        number_of_samples = len(sample_epk[group_i])

        if number_of_samples < min_samples_in_group:
            min_samples_in_group = number_of_samples

        for sample_i in range(number_of_samples):
            epk_in_sample = sample_epk[group_i][sample_i]
            epk_in_region = region_epk[group_i][sample_i]

            editing_obj = EditingInSample(epk_in_sample, epk_in_region)

            tmp_group_name = group_names[group_i]
            try:
                groups_dict[tmp_group_name].append(editing_obj)
            except KeyError:
                groups_dict[tmp_group_name] = [editing_obj]

    # Get a a tuple of all possible sets of two groups.
    group_comparisons = generate_group_pairs(group_names)

    bed_obj = BED(bed_path)


    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    min_average_depth = args.min_depth
    min_editing_area = args.min_area
    max_coverage_cov = args.max_coverage_cov
    max_depth_cov = args.max_depth_cov

    for record in generate_snvs(bed_path, min_coverage=None, min_editing=None, max_editing=None):

        record_name = record.chromosome+":"+record.position

        for group_1_name, group_2_name in group_comparisons:

            region_epks, sample_epks, region_size, region_avg_depth, group_ids = [], [], [], [], []
            val_dict = {}

            for tmp_group_name in (group_1_name, group_2_name):

                if tmp_group_name not in val_dict:
                    val_dict[tmp_group_name] = []

                for tmp_sample in groups_dict[tmp_group_name]:

                    tmp_region_depth = tmp_sample.get_region_depth(record_name)

                    if tmp_region_depth > min_average_depth:

                        region_avg_depth.append(tmp_region_depth)
                        group_ids.append(tmp_group_name)
                        sample_epks.append(tmp_sample.get_sample_epk())

                        # Region-wise data.
                        tmp_region_epk = tmp_sample.get_region_epk(record_name)
                        region_epks.append(tmp_sample.get_region_epk(record_name))
                        region_size.append(tmp_sample.get_region_size(record_name))

                        val_dict[tmp_group_name].append(tmp_region_epk)

            # When zero editing is detectable in regions this will cause errors when calculating stddev.
            at_least_one_region_has_editing = sum(region_epks) > 0

            # Make sure we can test at least almost half of the samples.
            min_samples_for_testability = floor(min_samples_in_group/2)
            min_samples_for_testability = 2 if min_samples_for_testability <= 1 else min_samples_for_testability
            group_1_is_testable = len(val_dict[group_1_name]) > min_samples_for_testability
            group_2_is_testable = len(val_dict[group_2_name]) > min_samples_for_testability

            if at_least_one_region_has_editing and group_1_is_testable and group_2_is_testable:

                area_cov = stdev(region_size)/mean(region_size)
                depth_cov = stdev(region_avg_depth)/mean(region_avg_depth)
                region_max_editing_area = sorted(region_size)[-1]

                if area_cov < max_coverage_cov and depth_cov < max_depth_cov:

                    testable += 1
                    #print(record.name)
                    #print("group_ids", group_ids)
                    #print("sample_epks", sample_epks)
                    #print("region_epks", region_epks)
                    #print("region_size", region_size)
                    #print("region_avg_depth", region_avg_depth)
                    robjects.globalenv['group_ids'] = StrVector(group_ids)
                    robjects.globalenv['region_depth'] = FloatVector(region_avg_depth)
                    robjects.globalenv['sample_epk'] = FloatVector(sample_epks)
                    robjects.globalenv['region_epk'] = FloatVector(region_epks)
                    robjects.globalenv['region_size'] = FloatVector(region_size)

                    robjects.r(r_script)

                    p_value = robjects.globalenv["p_value"][-1]

                    if p_value < 0.05:
                        rpvalcnt += 1

                    g1_mean = mean(val_dict[group_1_name])
                    g2_mean = mean(val_dict[group_2_name])

                    ttest_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                    if ttest_results[1] < 0.05:
                        tpvalcnt += 1

                    print(
                        "\t".join(
                         [
                             group_1_name,
                             group_2_name,
                             record_name,
                             record_name,
                             str(round(g1_mean, 2)),
                             str(round(g2_mean, 2)),
                             str(round(p_value, 7)),
                             str(round(ttest_results[1], 7))
                          ]
                        )
                    )

    # print("# rpvalcnt", rpvalcnt)
    # print("# tpvalcnt", tpvalcnt)
    # print("# testable", testable)
    # print("# COV Cutoff:", cov_cutoff)
    # print("# lm",    rpvalcnt/float(testable))
    # print("# ttest", tpvalcnt/float(testable))