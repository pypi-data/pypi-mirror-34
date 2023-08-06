from lib.parsers import generate_snvs
from lib.io import shared_params
from lib.io import island_params


def get_dict_of_merged_positions(file_list, store_variants=False):
    """

    :param file_list:
    :param store_variants:
    :return:
    """
    merged_dict = {}
    for vcf_file in file_list:
        for chrom, pos, id, ref, alt, qual, fil, info in generate_snvs(vcf_file):

            site_key = (chrom, pos, ref, alt)

            if store_variants:
                try:
                    merged_dict[site_key].append(vcf_file)
                except KeyError:
                    merged_dict[site_key] = [vcf_file]
            else:
                try:
                    merged_dict[site_key] += 1
                except KeyError:
                    merged_dict[site_key] = 1

    return merged_dict


def merge_editing_sites(parser):
    """ Merge two or more VCF files containing editing sites.
    """

    shared_params(parser, coverage=False, editing_islands=False, names=False, genome=False, gtf=False, alignment=False)

    parser.add_argument(
        "--min-samples",
        type=int,
        default=2,
        help="Site should be found in greater than or equal to n samples.  "
    )

    args = parser.parse_args()

    min_cov = args.min_coverage
    min_ed = args.min_editing
    max_ed = args.max_editing
    # name_list = args.names
    vcf_list = args.vcf
    store_variants = False
    merged_dict = {}

    for vcf_file_name in vcf_list:
        for site in generate_snvs(vcf_file_name, min_coverage=min_cov, min_editing=min_ed, max_editing=max_ed):

            site_key = (site.chromosome, site.position, site.reference, site.alteration)

            if store_variants:
                try:
                    merged_dict[site_key].append(vcf_file_name)
                except KeyError:
                    merged_dict[site_key] = [vcf_file_name]
            else:
                try:
                    merged_dict[site_key] += 1
                except KeyError:
                    merged_dict[site_key] = 1

    for dict_key in merged_dict:
        chrom, pos, ref, alt = dict_key
        if merged_dict[dict_key] >= args.min_samples:

            id, qual, fil, info = ".", ".", ".", str(merged_dict[dict_key])
            print("\t".join([chrom, pos, id, ref, alt, qual, fil, info]))


def find_islands(parser):
    """ Search for editing islands within VCF files containing editing sites.

    :return:
    """

    from sklearn.cluster import DBSCAN
    from base64 import urlsafe_b64encode
    from hashlib import md5
    island_params(parser)

    args = parser.parse_args()

    # Sort by chromosome, what about strand?
    chromosome_dict = {"+": {}, "-": {}}

    min_cov = args.min_coverage
    min_ed = args.min_editing
    max_ed = args.max_editing

    pad_len = int(args.pad_length)

    for vcf_name in args.vcf:

        for site in generate_snvs(vcf_name, min_coverage=min_cov, min_editing=min_ed, max_editing=max_ed):

            strand = "+" if site.reference == "A" else "-"
            position = int(site.position)

            try:
                try:
                    chromosome_dict[strand][site.chromosome][position] += 1
                except KeyError:
                    chromosome_dict[strand][site.chromosome][position] = 1
            except KeyError:
                chromosome_dict[strand].update({site.chromosome: dict()})

    print("\t".join(["chromosome", "start", "end", "strand", "length", "number_of_sites", "density"]))

    for strand in chromosome_dict:
        for chromosome in chromosome_dict[strand]:

            pos_dict = set(chromosome_dict[strand][chromosome])
            l = len(pos_dict)
            pos_list = [[p] for p in pos_dict]

            if l > args.min_samples:
                db = DBSCAN(eps=args.epsilon, min_samples=args.min_samples).fit(pos_list)
                island_dict = {}  # Make lists of bounds
                for i in range(l):
                    try:
                        island_dict[db.labels_[i]].append(pos_list[i])
                    except KeyError:
                        island_dict[db.labels_[i]] = [pos_list[i]]

                for label in range(len(island_dict) - 1):

                    sites_in_island = sorted(island_dict[label])

                    island_start = sites_in_island[0][0] - pad_len
                    island_end = sites_in_island[-1][0]+1 + pad_len
                    island_length = island_end - island_start
                    number_of_sites_in_island = len(sites_in_island)

                    if island_length >= args.min_length:                    
                        hstr = chromosome + strand + str(island_start) + str(island_end)
                        md5_digest = md5(hstr.encode('utf-8')).digest()

                        print("\t".join([
                            chromosome,
                            str(island_start),
                            str(island_end),
                            urlsafe_b64encode(md5_digest)[:-2].decode('utf-8'),
                            ".",                                                           # score
                            strand,
                            str(island_length),                                            # length of island
                            str(number_of_sites_in_island),                                # number of sites in island
                            str(round(number_of_sites_in_island/float(island_length), 5))  # density
                        ]))


def merge_editing_islands(parser):
    """ Merge two or more BED files containing editing islands.

    """
    pass


def split(parser):
    """ Split a VCF file containing editing sites into Adar1 and Adar2 sites.

    """
    pass


