import argparse

def parse_args():
     # create the top-level parser
     parser = argparse.ArgumentParser()
     subparsers = parser.add_subparsers(dest="command")
     
     add_build_ref_subparser(subparsers)
     add_DMRfind_subparser(subparsers)
     add_se_pipeline_subparser(subparsers)
     add_pe_pipeline_subparser(subparsers)
     add_bam_filter_subparser(subparsers)
     add_call_mc_subparser(subparsers)

     args = parser.parse_args()
     if args.command == "build-reference":
          from methylpy.call_mc_se import build_ref
          build_ref(input_files=args.input_files,
                    output=args.output_prefix,
                    bowtie2=args.bowtie2,
                    path_to_aligner=args.path_to_aligner,
                    buffsize=args.buffsize,
                    parallel=args.parallel,
                    offrate=args.offrate)
               
     elif args.command == "DMRfind":
          from methylpy.DMRfind import DMRfind
          DMRfind(allc_files = args.allc_files,
                  samples=args.samples,
                  mc_type=args.mc_type,
                  chroms=args.chroms,
                  num_procs=args.num_procs,
                  output_prefix=args.output_prefix,
                  min_cov=args.min_cov,
                  dmr_max_dist=args.dmr_max_dist,
                  sig_cutoff=args.sig_cutoff,
                  num_sims=args.num_sims,
                  num_sig_tests=args.min_tests,
                  min_num_dms=args.min_num_dms,
                  sample_category=args.sample_category,
                  mc_max_dist=args.mc_max_dist,
                  resid_cutoff=args.resid_cutoff,
                  collapse_samples=args.collapse_samples,
                  keep_temp_files=args.keep_temp_files,
                  min_cluster=args.min_cluster,
                  seed=args.seed)

     elif args.command == "single-end-pipeline":
          from methylpy.call_mc_se import run_methylation_pipeline
          run_methylation_pipeline(read_files=args.read_files,
                                   sample=args.sample,
                                   forward_reference=args.forward_ref,
                                   reverse_reference=args.reverse_ref,
                                   reference_fasta=args.ref_fasta,
                                   libraries=args.libraries,                                   
                                   path_to_output=args.path_to_output,
                                   pbat=args.pbat,
                                   num_procs=args.num_procs,
                                   sort_mem=args.sort_mem,
                                   num_upstr_bases=args.num_upstream_bases,
                                   num_downstr_bases=args.num_downstream_bases,
                                   generate_allc_file=args.generate_allc_file,
                                   generate_mpileup_file=args.generate_mpileup_file,
                                   compress_output=args.compress_output,
                                   trim_reads=args.trim_reads,
                                   path_to_cutadapt=args.path_to_cutadapt,
                                   bowtie2=args.bowtie2,
                                   path_to_aligner=args.path_to_aligner,
                                   aligner_options=args.aligner_options,
                                   remove_clonal=args.remove_clonal,
                                   path_to_picard=args.path_to_picard,
                                   keep_clonal_stats=args.keep_clonal_stats,
                                   java_options=args.java_options,
                                   path_to_samtools=args.path_to_samtools,
                                   adapter_seq=args.adapter_seq,
                                   unmethylated_control=args.unmethylated_control,
                                   binom_test=args.binom_test,
                                   sig_cutoff=args.sig_cutoff,
                                   min_cov=args.min_cov,
                                   max_adapter_removal=args.max_adapter_removal,
                                   overlap_length=args.overlap_length,
                                   zero_cap=args.zero_cap,
                                   error_rate=args.error_rate,
                                   min_qual_score=args.min_qual_score,
                                   min_read_len=args.min_read_len,
                                   min_base_quality=args.min_base_quality,
                                   keep_temp_files=args.keep_temp_files)
     
     elif args.command == "paired-end-pipeline":
          from methylpy.call_mc_pe import run_methylation_pipeline_pe
          run_methylation_pipeline_pe(read1_files=args.read1_files,
                                      read2_files=args.read2_files,
                                      sample=args.sample,
                                      forward_reference=args.forward_ref,
                                      reverse_reference=args.reverse_ref,
                                      reference_fasta=args.ref_fasta,
                                      libraries=args.libraries,
                                      path_to_output=args.path_to_output,
                                      pbat=args.pbat,
                                      num_procs=args.num_procs,
                                      sort_mem=args.sort_mem,
                                      num_upstr_bases=args.num_upstream_bases,
                                      num_downstr_bases=args.num_downstream_bases,
                                      generate_allc_file=args.generate_allc_file,
                                      generate_mpileup_file=args.generate_mpileup_file,
                                      compress_output=args.compress_output,
                                      trim_reads=args.trim_reads,
                                      path_to_cutadapt=args.path_to_cutadapt,
                                      bowtie2=args.bowtie2,
                                      path_to_aligner=args.path_to_aligner,
                                      aligner_options=args.aligner_options,
                                      remove_clonal=args.remove_clonal,
                                      path_to_picard=args.path_to_picard,
                                      keep_clonal_stats=args.keep_clonal_stats,
                                      java_options=args.java_options,
                                      path_to_samtools=args.path_to_samtools,
                                      adapter_seq_read1=args.adapter_seq_read1,
                                      adapter_seq_read2=args.adapter_seq_read2,
                                      unmethylated_control=args.unmethylated_control,                                   
                                      binom_test=args.binom_test,
                                      sig_cutoff=args.sig_cutoff,
                                      min_cov=args.min_cov,
                                      max_adapter_removal=args.max_adapter_removal,
                                      overlap_length=args.overlap_length,
                                      zero_cap=args.zero_cap,
                                      error_rate=args.error_rate,
                                      min_qual_score=args.min_qual_score,
                                      min_read_len=args.min_read_len,
                                      min_base_quality=args.min_base_quality,
                                      keep_temp_files=args.keep_temp_files)

     elif args.command == "bam-quality-filter":          
          from methylpy.call_mc_se import bam_quality_mch_filter
          bam_quality_mch_filter(inputf=args.input_file,
                                 outputf=args.output_file,
                                 reference_fasta=args.ref_fasta,
                                 quality_cutoff=args.quality_cutoff,
                                 min_ch=args.min_num_ch,
                                 max_mch_level=args.max_mch_level,
                                 buffer_line_number=args.buffer_line_number,
                                 path_to_samtools=args.path_to_samtools)
     elif args.command == "call-methylation-state":
          if args.paired_end:
               from call_mc_pe import call_methylated_sites_pe
               call_methylated_sites_pe(inputf=args.input_file,
                                        sample=args.sample,
                                        reference_fasta=args.ref_fasta,
                                        unmethylated_control=args.unmethylated_control,
                                        sig_cutoff=args.sig_cutoff,
                                        num_procs=args.num_procs,                                     
                                        num_upstr_bases=args.num_upstream_bases,
                                        num_downstr_bases=args.num_downstream_bases,
                                        generate_mpileup_file=args.generate_mpileup_file,
                                        compress_output=args.compress_output,
                                        min_cov=args.min_cov,
                                        binom_test=args.binom_test,
                                        min_mc=args.min_mc,
                                        path_to_samtools=args.path_to_samtools,
                                        path_to_files=args.path_to_output,
                                        min_base_quality=args.min_base_quality)
          else:
               from call_mc_se import call_methylated_sites
               call_methylated_sites(inputf=args.input_file,
                                     sample=args.sample,
                                     reference_fasta=args.ref_fasta,
                                     unmethylated_control=args.unmethylated_control,
                                     sig_cutoff=args.sig_cutoff,
                                     num_procs=args.num_procs,                                     
                                     num_upstr_bases=args.num_upstream_bases,
                                     num_downstr_bases=args.num_downstream_bases,
                                     generate_mpileup_file=args.generate_mpileup_file,
                                     compress_output=args.compress_output,
                                     min_cov=args.min_cov,
                                     binom_test=args.binom_test,
                                     min_mc=args.min_mc,
                                     path_to_samtools=args.path_to_samtools,
                                     path_to_files=args.path_to_output,
                                     min_base_quality=args.min_base_quality)

def add_DMRfind_subparser(subparsers):
     # create the parser for the "DMRfind" command
     parser_dmrfind = subparsers.add_parser(
          "DMRfind",
          formatter_class=argparse.ArgumentDefaultsHelpFormatter,
          help="Finding differentially methylated regions")
     
     # add options
     parser_dmrfind_req = parser_dmrfind.add_argument_group("required inputs")
     parser_dmrfind_req.add_argument("--allc-files",
                                     type=str,
                                     nargs="+",
                                     required=True,
                                     help="List of allc files.")

     parser_dmrfind_req.add_argument("--chroms",
                                     type=str,
                                     nargs="+",
                                     required=True,
                                     help="Space separated listing of chromosomes where DMRs will "
                                     + "be called.")

     parser_dmrfind_req.add_argument("--samples",
                                     type=str,
                                     nargs="+",
                                     required=True,
                                     help="List of space separated samples")
     
     parser_dmrfind_req.add_argument("--output-prefix",
                                     type=str,
                                     required=True,
                                     help="String indicating the prefix for output files")
     
     parser_dmrfind_opt = parser_dmrfind.add_argument_group("optional inputs")

     parser_dmrfind_opt.add_argument("--mc-type",
                                     type=str,
                                     nargs="+",
                                     default=["CGN"],
                                     help="List of space separated mc nucleotide contexts for "
                                     + "which you want to look for DMRs. These classifications "
                                     + "may use the wildcards H (indicating anything but a G) and "
                                     + "N (indicating any nucleotide).")
     
     parser_dmrfind_opt.add_argument("--num-procs",
                                     type=int,
                                     default=1,
                                     help="Number of processors you wish to use to parallelize this function")
     
     parser_dmrfind_opt.add_argument("--min-cov",
                                     type=int,
                                     default=0,
                                     help="Minimum number of reads that must cover a site for it to be "
                                     + "considered.")

     parser_dmrfind_opt.add_argument("--dmr-max-dist",
                                     type=int,
                                     default=250,
                                     help="Maximum distance two significant sites can be to be included "
                                     + "in the same block.")
     
     parser_dmrfind_opt.add_argument("--sig-cutoff",
                                     type=float,
                                     default=.01,
                                     help="Float indicating at what FDR you want to consider a result "
                                     + "significant.")

     parser_dmrfind_opt.add_argument("--num-sims",
                                     type=int,
                                     default=3000,
                                     help="Number of permutation tests you would like to run to estimate "
                                     + "the p-values of the differential methylation tests")
     
     parser_dmrfind_opt.add_argument("--min-tests",
                                     type=int,
                                     default=100,
                                     help="Minimum number of permuation tests you\ would d like to run "
                                     + "for each mC")     
     
     parser_dmrfind_opt.add_argument("--min-num-dms",
                                     type=int,
                                     default=0,
                                     help="The minimum number of differentially methylated sites "
                                     + "that a differentially methylated region needs to contain to be "
                                     + "reported")
     
     parser_dmrfind_opt.add_argument("--sample-category",
                                     type=int,
                                     nargs="+",
                                     default=False,
                                     help="A list of categories that each respective sample belongs "
                                     + "to; the categories must begin at 0 and increase by 1 for "
                                     + "each category added. ex: samples [A,B,C] categories [0,1,2] "
                                     + "or categories [0, 1, 0] ")
     
     parser_dmrfind_opt.add_argument("--mc-max-dist",
                                     type=int,
                                     default=0,
                                     help="Integer indicating the maximum distance two sites can be "
                                     + "from one another for their methylation counts to be combined. "
                                     + "This option helps with low coverage experiments where you may "
                                     + "want to leverage the correlation of methylation between sites "
                                     + "to get more statistical power.")
     
     parser_dmrfind_opt.add_argument("--resid-cutoff",
                                     type=int,
                                     default=0.01,
                                     help="Results will have to show deviations in the contingency "
                                     + "table in the same direction as the rest of the window")
     
     parser_dmrfind_opt.add_argument("--collapse-samples",
                                     type=str,
                                     nargs="+",
                                     default=False,
                                     help="A list of samples for collapsing blocks")
     
     parser_dmrfind_opt.add_argument("--keep-temp-files",
                                     type=str2bool,
                                     default=False,
                                     help="Boolean; keep intermediate files?")
     
     parser_dmrfind_opt.add_argument("--min-cluster",
                                     type=int,
                                     default=0,
                                     help="The minimum number of each sample category that must be "
                                     + "present in every block that is output.")
     
     parser_dmrfind_opt.add_argument("--seed",
                                     type=int,
                                     default=-1,
                                     help="A seed to provide to the random number generator for "
                                     + "permutation testing. Only change this if you are debugging "
                                     + "and want to make sure the permutation output is consistent")
     
def add_se_pipeline_subparser(subparsers):
     parser_se = subparsers.add_parser("single-end-pipeline",
                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                       help="Methylation pipeline for single-end data")

     parser_se_req = parser_se.add_argument_group("required inputs")
          
     parser_se_req.add_argument("--read-files",
                                  type=str,
                                  nargs="+",
                                  required=True,
                                  help="list of all the fastq files you would like to run through "
                                  + "the pipeline. Note that globbing is supported here (i.e., you "
                                  + "can use * in your paths)")
     
     parser_se_req.add_argument("--sample",
                                  type=str,
                                  required=True,
                                  help="String indicating the name of the sample you are processing. "
                                  + "It will be included in the output files.")
     
     parser_se_req.add_argument("--forward-ref",
                                  type=str, required=True, help="string indicating the path to the "
                                  + "forward strand reference created by build_ref")
     
     parser_se_req.add_argument("--reverse-ref",
                                  type=str,
                                  required=True,
                                  help="string indicating the path to the reverse strand reference "
                                  + "created by build_ref")
     
     parser_se_req.add_argument("--ref-fasta",
                                  type=str,
                                  required=True,
                                  help="string indicating the path to a fasta file containing the "
                                  + "sequences you used for mapping")
     
     parser_se_opt = parser_se.add_argument_group("optional inputs")

     parser_se_opt.add_argument("--libraries",
                                type=str,
                                nargs="+",
                                default=["libA"],
                                help="list of library IDs (in the same order as the files list) "
                                + "indiciating which libraries each set of fastq files belong to. "
                                + "If you use a glob, you only need to indicate the library ID for "
                                + "those fastqs once (i.e., the length of files and libraries should "
                                + "be the same)")
     
     parser_se_opt.add_argument("--path-to-output",
                                type=str,
                                default="",
                                help="Path to a directory where you would like the output to be stored. "
                                + "The default is the same directory as the input fastqs.")

     parser_se_opt.add_argument("--pbat",
                                type=str2bool,
                                default=False,
                                help="Boolean indicating whether to process data in PBAT (Post-Bisulfite "
                                +"Adaptor Tagging) mode, in which reads will be mapped to opposite strand "
                                +"of C-T converted genome and the forward strand of G-A converted genome.")

     parser_se_opt.add_argument("--num-procs",
                                type=int,
                                default=1,
                                help="Number of processors you wish to use to parallelize this function")     

     parser_se_opt.add_argument("--sort-mem",
                                type=str,
                                default="500M",
                                help="Parameter to pass to unix sort with -S/--buffer-size command")

     parser_se_opt.add_argument("--num-upstream-bases",
                                type=int,
                                default=0,
                                help="Number of base(s) upstream of each cytosine that you wish to include "
                                + "in output file. Recommend value 1 for NOMe-seq processing since the "
                                + "upstream base is required to tell apart cytosine at GC context.")

     parser_se_opt.add_argument("--num-downstream-bases",
                                type=int,
                                default=2,
                                help="Number of base(s) downstream of each cytosine that you wish to include "
                                + "in output file. Recommend value to be at least 1 to separate cytosines at "
                                + "different sequence contexts.")

     parser_se_opt.add_argument("--generate-allc-file",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to generate the final output file that "
                                +" contains the methylation state of each cytosine. If set to be false, "
                                +"only alignment file (in BAM format) will be generated.")

     parser_se_opt.add_argument("--generate-mpileup-file",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to generate intermediate mpileup file to save "
                                +"space. However, skipping mpileup step may cause problem due to the nature of "
                                +"python. Not skipping this step is recommended.")
     
     parser_se_opt.add_argument("--compress-output",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to compress (by gzip) the final output "
                                + "(allc file(s)).")     

     parser_se_opt.add_argument("--trim-reads",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to trim reads using cutadapt.")
     
     parser_se_opt.add_argument("--path-to-cutadapt",
                                type=str,
                                default="",
                                help="Path to cutadapt installation (default is current dir)")
     
     parser_se_opt.add_argument("--bowtie2",
                                type=str2bool,
                                default=True,
                                help="Specifies whether to use the bowtie2 aligner instead of bowtie")

     parser_se_opt.add_argument("--path-to-aligner",
                                type=str,
                                default="",
                                help="Path to bowtie/bowtie2 installation (default is current dir)")
     
     parser_se_opt.add_argument("--aligner-options",
                                type=str,
                                nargs="+",
                                help="list of strings indicating options you would like passed "
                                + "to bowtie (e.g., [\"-k 1\",\"-l 2\"])")
          
     parser_se_opt.add_argument("--remove-clonal",
                                type=str2bool,
                                default=True,
                                help="Boolean indicates whether to remove clonal reads or not")
     
     parser_se_opt.add_argument("--path-to-picard",
                                type=str,
                                default="",
                                help="The path to the picard.jar in picard tools. The jar file can "
                                + "be downloaded from https://broadinstitute.github.io/picard/index.html "
                                + "(default is current dir)")
          
     parser_se_opt.add_argument("--keep-clonal-stats",
                                type=str2bool,
                                default=False,
                                help="Boolean indicates whether to store the metric file from picard.")
     
     parser_se_opt.add_argument("--java-options",
                                type=str,
                                default="-Xmx20g",
                                help="String indicating the option pass the java when running picard.")

     parser_se_opt.add_argument("--path-to-samtools",
                                type=str,
                                default="",
                                help="Path to samtools installation (default is current dir)")
     
     parser_se_opt.add_argument("--adapter-seq",
                                type=str,
                                default="AGATCGGAAGAGCACACGTCTG",
                                help="sequence of an adapter that was ligated to the 3\' end. The "
                                +"adapter itself and anything that follows is trimmed.")

     parser_se_opt.add_argument("--unmethylated-control",
                                type=str,
                                default=None,
                                help="name of the chromosome/region that you want to use to estimate "
                                + "the non-conversion rate of your sample, or the non-conversion rate "
                                + "you would like to use. Consequently, control is either a string, or "
                                + "a decimal. If control is a string then it should be in the following "
                                + "format: \"chrom:start-end\". If you would like to specify an entire "
                                + "chromosome simply use \"chrom:\"")
     
     parser_se_opt.add_argument("--binom-test",
                                type=str2bool,
                                default=False,
                                help="Indicates that you would like to perform a binomial test on each cytosine "
                                +"to delineate cytosines that are significantly methylated than noise due to "
                                +"the failure of bisulfite conversion.")
     
     parser_se_opt.add_argument("--sig-cutoff",
                                type=float,
                                default=.01,
                                help="float indicating the adjusted p-value cutoff you wish to use for "
                                + "determining whether or not a site is methylated")

     parser_se_opt.add_argument("--min_cov",
                                type=int,
                                default=0,
                                help="Integer indicating the minimum number of reads for a site to be tested.")
     
     parser_se_opt.add_argument("--max_adapter_removal",
                                type=int,
                                help="Indicates the maximum number of times to try to remove adapters. Useful "
                                +"when an adapter gets appended multiple times.")
     
     parser_se_opt.add_argument("--overlap_length",
                                type=int,
                                help="Minimum overlap length. If the overlap between the read and the adapter "
                                +"is shorter than LENGTH, the read is not modified. This reduces the no. of "
                                +"bases trimmed purely due to short random adapter matches.")
     
     parser_se_opt.add_argument("--zero_cap",
                                type=str2bool,
                                help="Flag that causes negative quality values to be set to zero (workaround "
                                +"to avoid segmentation faults in BWA)")
     
     parser_se_opt.add_argument("--error_rate",
                                type=float,
                                help="maximum allowed error rate (no. of errors divided by the length of "
                                +"the matching region)")
     
     parser_se_opt.add_argument("--min_qual_score",
                                type=int,
                                default=10,
                                help="allows you to trim low-quality ends from reads before adapter removal. "
                                +"The algorithm is the same as the one used by BWA (Subtract CUTOFF from all "
                                +"qualities; compute partial sums from all indices to the end of the sequence; "
                                +" cut sequence at the index at which the sum is minimal).")
     
     parser_se_opt.add_argument("--min_read_len",
                                type=int,
                                default=30,
                                help="indicates the minimum length a read must be to be kept. Reads that "
                                +"are too short even before adapter removal are also discarded. In colorspace, "
                                "an initial primer is not counted.")

     parser_se_opt.add_argument("--min-base-quality",
                                type=int,
                                default=1,
                                help="Integer indicating the minimum PHRED quality score for a base to be "
                                +"included in the mpileup file (and subsequently to be considered for "
                                +"methylation calling).")
     
     parser_se_opt.add_argument("--keep_temp_files",
                                type=str2bool,
                                default=False,
                                help="Boolean indicating that you would like to keep the intermediate files "
                                +"generated by this function. This can be useful for debugging, but in general "
                                +"should be left False.")

def add_pe_pipeline_subparser(subparsers):
     parser_pe = subparsers.add_parser("paired-end-pipeline",
                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                       help="Methylation pipeline for paired-end data")

     parser_pe_req = parser_pe.add_argument_group("required inputs")
          
     parser_pe_req.add_argument("--read1-files",
                                  type=str,
                                  nargs="+",
                                  required=True,
                                  help="list of all the read 1 fastq files you would like to run through "
                                  + "the pipeline. Note that globbing is supported here (i.e., you "
                                  + "can use * in your paths)")
     
     parser_pe_req.add_argument("--read2-files",
                                  type=str,
                                  nargs="+",
                                  required=True,
                                  help="list of all the read 2 fastq files you would like to run through "
                                  + "the pipeline. Note that globbing is supported here (i.e., you "
                                  + "can use * in your paths)")
     
     parser_pe_req.add_argument("--sample",
                                  type=str,
                                  required=True,
                                  help="String indicating the name of the sample you are processing. "
                                  + "It will be included in the output files.")
     
     parser_pe_req.add_argument("--forward-ref",
                                  type=str, required=True, help="string indicating the path to the "
                                  + "forward strand reference created by build_ref")
     
     parser_pe_req.add_argument("--reverse-ref",
                                  type=str,
                                  required=True,
                                  help="string indicating the path to the reverse strand reference "
                                  + "created by build_ref")
     
     parser_pe_req.add_argument("--ref-fasta",
                                  type=str,
                                  required=True,
                                  help="string indicating the path to a fasta file containing the "
                                  + "sequences you used for mapping")
     
     parser_pe_opt = parser_pe.add_argument_group("optional inputs")

     parser_pe_opt.add_argument("--libraries",
                                type=str,
                                nargs="+",
                                default=["libA"],
                                help="list of library IDs (in the same order as the files list) "
                                + "indiciating which libraries each set of fastq files belong to. "
                                + "If you use a glob, you only need to indicate the library ID for "
                                + "those fastqs once (i.e., the length of files and libraries should "
                                + "be the same)")
     
     parser_pe_opt.add_argument("--path-to-output",
                                type=str,
                                default="",
                                help="Path to a directory where you would like the output to be stored. "
                                + "The default is the same directory as the input fastqs.")

     parser_pe_opt.add_argument("--pbat",
                                type=str2bool,
                                default=False,
                                help="Boolean indicating whether to process data in PBAT (Post-Bisulfite "
                                +"Adaptor Tagging) mode, in which reads will be mapped to opposite strand "
                                +"of C-T converted genome and the forward strand of G-A converted genome.")

     parser_pe_opt.add_argument("--num-procs",
                                type=int,
                                default=1,
                                help="Number of processors you wish to use to parallelize this function")     

     parser_pe_opt.add_argument("--sort-mem",
                                type=str,
                                default="500M",
                                help="Parameter to pass to unix sort with -S/--buffer-size command")

     parser_pe_opt.add_argument("--num-upstream-bases",
                                type=int,
                                default=0,
                                help="Number of base(s) upstream of each cytosine that you wish to include "
                                + "in output file. Recommend value 1 for NOMe-seq processing since the "
                                + "upstream base is required to tell apart cytosine at GC context.")

     parser_pe_opt.add_argument("--num-downstream-bases",
                                type=int,
                                default=2,
                                help="Number of base(s) downstream of each cytosine that you wish to include "
                                + "in output file. Recommend value to be at least 1 to separate cytosines at "
                                + "different sequence contexts.")

     parser_pe_opt.add_argument("--generate-allc-file",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to generate the final output file that "
                                +" contains the methylation state of each cytosine. If set to be false, "
                                +"only alignment file (in BAM format) will be generated.")

     parser_pe_opt.add_argument("--generate-mpileup-file",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to generate intermediate mpileup file to save "
                                +"space. However, skipping mpileup step may cause problem due to the nature of "
                                +"python. Not skipping this step is recommended.")
     
     parser_pe_opt.add_argument("--compress-output",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to compress (by gzip) the final output "
                                + "(allc file(s)).")     

     parser_pe_opt.add_argument("--trim-reads",
                                type=str2bool,
                                default=True,
                                help="Boolean indicating whether to trim reads using cutadapt.")
     
     parser_pe_opt.add_argument("--path-to-cutadapt",
                                type=str,
                                default="",
                                help="Path to cutadapt installation (default is current dir)")
     
     parser_pe_opt.add_argument("--bowtie2",
                                type=str2bool,
                                default=True,
                                help="Specifies whether to use the bowtie2 aligner instead of bowtie")

     parser_pe_opt.add_argument("--path-to-aligner",
                                type=str,
                                default="",
                                help="Path to bowtie/bowtie2 installation (default is current dir)")
     
     parser_pe_opt.add_argument("--aligner-options",
                                type=str,
                                nargs="+",
                                help="list of strings indicating options you would like passed "
                                + "to bowtie (e.g., [\"-k 1\",\"-l 2\"])")
          
     parser_pe_opt.add_argument("--remove-clonal",
                                type=str2bool,
                                default=True,
                                help="Boolean indicates whether to remove clonal reads or not")
     
     parser_pe_opt.add_argument("--path-to-picard",
                                type=str,
                                default="",
                                help="The path to the picard.jar in picard tools. The jar file can "
                                + "be downloaded from https://broadinstitute.github.io/picard/index.html "
                                + "(default is current dir)")
          
     parser_pe_opt.add_argument("--keep-clonal-stats",
                                type=str2bool,
                                default=False,
                                help="Boolean indicates whether to store the metric file from picard.")
     
     parser_pe_opt.add_argument("--java-options",
                                type=str,
                                default="-Xmx20g",
                                help="String indicating the option pass the java when running picard.")

     parser_pe_opt.add_argument("--path-to-samtools",
                                type=str,
                                default="",
                                help="Path to samtools installation (default is current dir)")
     
     parser_pe_opt.add_argument("--adapter-seq-read1",
                                type=str,
                                default="AGATCGGAAGAGCACACGTCTGAAC",
                                help="sequence of an adapter that was ligated to the 3\' end of read 1. The "
                                +"adapter itself and anything that follows is trimmed.")
     
     parser_pe_opt.add_argument("--adapter-seq-read2",
                                type=str,
                                default="AGATCGGAAGAGCGTCGTGTAGGGA",
                                help="sequence of an adapter that was ligated to the 3\' end of read 2. The "
                                +"adapter itself and anything that follows is trimmed.")

     parser_pe_opt.add_argument("--unmethylated-control",
                                type=str,
                                default=None,
                                help="name of the chromosome/region that you want to use to estimate "
                                + "the non-conversion rate of your sample, or the non-conversion rate "
                                + "you would like to use. Consequently, control is either a string, or "
                                + "a decimal. If control is a string then it should be in the following "
                                + "format: \"chrom:start-end\". If you would like to specify an entire "
                                + "chromosome simply use \"chrom:\"")
     
     parser_pe_opt.add_argument("--binom-test",
                                type=str2bool,
                                default=False,
                                help="Indicates that you would like to perform a binomial test on each cytosine "
                                +"to delineate cytosines that are significantly methylated than noise due to "
                                +"the failure of bisulfite conversion.")
     
     parser_pe_opt.add_argument("--sig-cutoff",
                                type=float,
                                default=.01,
                                help="float indicating the adjusted p-value cutoff you wish to use for "
                                + "determining whether or not a site is methylated")

     parser_pe_opt.add_argument("--min_cov",
                                type=int,
                                default=0,
                                help="Integer indicating the minimum number of reads for a site to be tested.")
     
     parser_pe_opt.add_argument("--max_adapter_removal",
                                type=int,
                                help="Indicates the maximum number of times to try to remove adapters. Useful "
                                +"when an adapter gets appended multiple times.")
     
     parser_pe_opt.add_argument("--overlap_length",
                                type=int,
                                help="Minimum overlap length. If the overlap between the read and the adapter "
                                +"is shorter than LENGTH, the read is not modified. This reduces the no. of "
                                +"bases trimmed purely due to short random adapter matches.")
     
     parser_pe_opt.add_argument("--zero_cap",
                                type=str2bool,
                                help="Flag that causes negative quality values to be set to zero (workaround "
                                +"to avoid segmentation faults in BWA)")
     
     parser_pe_opt.add_argument("--error_rate",
                                type=float,
                                help="maximum allowed error rate (no. of errors divided by the length of "
                                +"the matching region)")
     
     parser_pe_opt.add_argument("--min_qual_score",
                                type=int,
                                default=10,
                                help="allows you to trim low-quality ends from reads before adapter removal. "
                                +"The algorithm is the same as the one used by BWA (Subtract CUTOFF from all "
                                +"qualities; compute partial sums from all indices to the end of the sequence; "
                                +" cut sequence at the index at which the sum is minimal).")
     
     parser_pe_opt.add_argument("--min_read_len",
                                type=int,
                                default=30,
                                help="indicates the minimum length a read must be to be kept. Reads that "
                                +"are too short even before adapter removal are also discarded. In colorspace, "
                                "an initial primer is not counted.")

     parser_pe_opt.add_argument("--min-base-quality",
                                type=int,
                                default=1,
                                help="Integer indicating the minimum PHRED quality score for a base to be "
                                +"included in the mpileup file (and subsequently to be considered for "
                                +"methylation calling).")
     
     parser_pe_opt.add_argument("--keep_temp_files",
                                type=str2bool,
                                default=False,
                                help="Boolean indicating that you would like to keep the intermediate files "
                                +"generated by this function. This can be useful for debugging, but in general "
                                +"should be left False.")

def add_build_ref_subparser(subparsers):
     # create the parser for the "DMRfind" command
     parser_build = subparsers.add_parser(
          "build-reference",
          formatter_class=argparse.ArgumentDefaultsHelpFormatter,
          help="Building reference for bisulfite sequencing data")
     
     # add options
     parser_build_req = parser_build.add_argument_group("required inputs")
     parser_build_req.add_argument("--input-files",
                                   type=str,
                                   nargs="+",
                                   required=True,
                                   help="List of genome fasta files to build a reference from.")

     parser_build_req.add_argument("--output-prefix",
                                   type=str,
                                   required=True,
                                   help="the prefix of the two output reference files that will be created.")
     
     parser_build_opt = parser_build.add_argument_group("optional inputs")
     parser_build_opt.add_argument("--bowtie2",
                                   type=str2bool,
                                   default=True,
                                   help="Boolean indicating whether to create reference for bowtie2 instead "
                                   +"of for bowtie.")

     parser_build_opt.add_argument("--path-to-aligner",
                                   type=str,
                                   default="",
                                   help="Path to bowtie/bowtie2 installation (default is current dir)")

     parser_build_opt.add_argument("--buffsize",
                                   type=int,
                                   default=100,
                                   help="The number of bytes that will be read in from the reference at once.")

     parser_build_opt.add_argument("--parallel",
                                   type=str2bool,
                                   default=False,
                                   help="Boolean indicating whether to use 2 cores for processing.")

     parser_build_opt.add_argument("--offrate",
                                   type=str2bool,
                                   default=False,
                                   help="offrate refers to the Bowtie parameter, reference the bowtie "
                                   +"manual to see more detail.")

def add_bam_filter_subparser(subparsers):
     parser_filter = subparsers.add_parser(
          "bam-quality-filter",
          formatter_class=argparse.ArgumentDefaultsHelpFormatter,
          help="Filter out single-end reads by mapping quality and mCH level")
     
     # add options
     parser_filter_req = parser_filter.add_argument_group("required inputs")
     parser_filter_req.add_argument("--input-file",
                                    type=str,
                                    required=True,
                                    help="BAM file to filter.")
     
     parser_filter_req.add_argument("--output-file",
                                    type=str,
                                    required=True,
                                    help="Name of output file")

     parser_filter_req.add_argument("--ref-fasta",
                                    type=str,
                                    required=True,
                                    help="string indicating the path to a fasta file containing the "
                                    +"sequences you used for mapping")
     
     parser_filter_opt = parser_filter.add_argument_group("optional inputs")
     parser_filter_opt.add_argument("--quality-cutoff",
                                    type=int,
                                    default=30,
                                    help="Minimum MAPQ for reads to be included.")

     parser_filter_opt.add_argument("--min-num-ch",
                                    type=int,
                                    default=30,
                                    help="Minimum number of CH sites for mCH level filter to be applied.")

     parser_filter_opt.add_argument("--max-mch-level",
                                    type=float,
                                    default=0.7,
                                    help="Maximum mCH level for reads to be included.")

     parser_filter_opt.add_argument("--path-to-samtools",
                                type=str,
                                default="",
                                help="Path to samtools installation (default is current dir)")
     
     parser_filter_opt.add_argument("--buffer-line-number",
                                type=int,
                                default=100000,
                                help="size of buffer for reads to be written on hard drive.")

def add_call_mc_subparser(subparsers):
     call_mc = subparsers.add_parser("call-methylation-state",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     help="Call cytosine methylation state from BAM file")

     call_mc_req = call_mc.add_argument_group("required inputs")     
     call_mc_req.add_argument("--input-file",
                              type=str,
                              help="bam file that contains mapped bisulfite sequencing reads.")
     
     call_mc_req.add_argument("--sample",
                              type=str,
                              required=True,
                              help="String indicating the name of the sample you are processing. "
                              + "It will be included in the output files.")

     call_mc_req.add_argument("--ref-fasta",
                              type=str,
                              required=True,
                              help="string indicating the path to a fasta file containing the "
                              + "sequences you used for mapping")

     call_mc_req.add_argument("--paired-end",
                              type=str2bool,
                              required=True,
                              default=False,
                              help="Boolean indicating whether the input BAM file is from paired-end "
                              +"data.")
     
     call_mc_opt = call_mc.add_argument_group("optional inputs")

     call_mc_opt.add_argument("--path-to-output",
                              type=str,
                              default="",
                              help="Path to a directory where you would like the output to be stored. "
                              + "The default is the same directory as the input fastqs.")

     call_mc_opt.add_argument("--num-procs",
                              type=int,
                              default=1,
                              help="Number of processors you wish to use to parallelize this function")     

     call_mc_opt.add_argument("--num-upstream-bases",
                              type=int,
                              default=0,
                              help="Number of base(s) upstream of each cytosine that you wish to include "
                              + "in output file. Recommend value 1 for NOMe-seq processing since the "
                              + "upstream base is required to tell apart cytosine at GC context.")

     call_mc_opt.add_argument("--num-downstream-bases",
                              type=int,
                              default=2,
                              help="Number of base(s) downstream of each cytosine that you wish to include "
                              + "in output file. Recommend value to be at least 1 to separate cytosines at "
                              + "different sequence contexts.")

     call_mc_opt.add_argument("--generate-allc-file",
                              type=str2bool,
                              default=True,
                              help="Boolean indicating whether to generate the final output file that "
                              +" contains the methylation state of each cytosine. If set to be false, "
                              +"only alignment file (in BAM format) will be generated.")

     call_mc_opt.add_argument("--generate-mpileup-file",
                              type=str2bool,
                              default=True,
                              help="Boolean indicating whether to generate intermediate mpileup file to save "
                              +"space. However, skipping mpileup step may cause problem due to the nature of "
                              +"python. Not skipping this step is recommended.")
     
     call_mc_opt.add_argument("--compress-output",
                              type=str2bool,
                              default=True,
                              help="Boolean indicating whether to compress (by gzip) the final output "
                              + "(allc file(s)).")     

     call_mc_opt.add_argument("--path-to-samtools",
                              type=str,
                              default="",
                              help="Path to samtools installation (default is current dir)")

     call_mc_opt.add_argument("--unmethylated-control",
                              type=str,
                              default=None,
                              help="name of the chromosome/region that you want to use to estimate "
                              + "the non-conversion rate of your sample, or the non-conversion rate "
                              + "you would like to use. Consequently, control is either a string, or "
                              + "a decimal. If control is a string then it should be in the following "
                              + "format: \"chrom:start-end\". If you would like to specify an entire "
                              + "chromosome simply use \"chrom:\"")
     
     call_mc_opt.add_argument("--binom-test",
                              type=str2bool,
                              default=False,
                              help="Indicates that you would like to perform a binomial test on each cytosine "
                              +"to delineate cytosines that are significantly methylated than noise due to "
                              +"the failure of bisulfite conversion.")
     
     call_mc_opt.add_argument("--sig-cutoff",
                              type=float,
                              default=.01,
                              help="float indicating the adjusted p-value cutoff you wish to use for "
                              + "determining whether or not a site is methylated")

     call_mc_opt.add_argument("--min_cov",
                              type=int,
                              default=0,
                              help="Integer indicating the minimum number of reads for a site to be tested.")
     
     call_mc_opt.add_argument("--min_mc",
                              type=int,
                              default=0,
                              help="Minimum number of mCs that must be observed for cytosine to be called as "
                              +"methylated.")
     
     call_mc_opt.add_argument("--min-base-quality",
                              type=int,
                              default=1,
                              help="Integer indicating the minimum PHRED quality score for a base to be "
                              +"included in the mpileup file (and subsequently to be considered for "
                              +"methylation calling).")

def str2bool(v):
     ## adapted from the answer by Maxim at
     ## https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
     if v.lower() in ('yes', 'true', 't', 'y', '1'):
          return(True)
     elif v.lower() in ('no', 'false', 'f', 'n', '0'):
          return(False)
     else:
          raise argparse.ArgumentTypeError('Boolean value expected.')

              
if __name__ == "__main__":
     parse_args()
