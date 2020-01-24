# Google Summer of Code 2020
The development team of the [C3G](http://computationalgenomics.ca/) Montreal node is aiming to participate as an organization in Google Summer of Code 2020. We are offering to mentor students who wish to spend their summer working on interesting and user-friendly software pipelines for the analysis of Next-Generation Sequencing data. This page hosts information for prospective GSoC students and our project ideas. We are looking for 4 to 6 excellent students to collaborate on some of our research and development projects.

[**See GSoC 2020 full time line**](timeline.md)

--------------
Table of content:

[TOC]

--------------
# The C3G montreal node 
The Montreal C3G nodes is hosted at the McGill University and Genome Quebec Innovation Center (MUGQIC). The Montreal node is strongly involved in the [GenAP](https://genap.ca/) developement team and had developed a robust genomic data analysis pipeline set. Since 2011, we have completed more than 400 bioinformatics analysis projects with over 290 distinct groups of researchers across Canada. Our teams have significant experience in personalized medicine applications. These have included genome analysis and interpretation of personal genomes, technology and services to record patient presentations, DNA-, RNA- and ChIP-seq data analysis, and analysis of complete human epigenomes in both germline disorders and cancers.

The current members of the team are:

 * Guillaume Bourque, _Ph.D_ - Director
 * Mathieu Bourgey, _Ph.D_ - R&D Bioinformatics manager
 * Francois Lefebvre, _MSc_ - Services Bioinformatics manager
 * David Bujold, _MSc_ - GenAP project manager  
 * Edouard Henrion, _MSc_ - Software developer
 * Emmanuel Gonzalez, _Ph.D_ - Bioinformatics specialist
 * Gary Leveque, _MSc_ - Bioinformatics specialist
 * Robert Eveleigh, _MSc_ - Bioinformatics specialist
 * Rola Dali, _Ph.D_ - Bioinformatics specialist
 * Pierre-Olivier Quirion, _Ph.D_ - HPC specialist   
 * José Héctor Gálvez López, _MSc_ - Bioinformatics specialist
 * Ulysse Fortier-Gauthier, _Ph.D_ - Bioinformatics software developer
 * Pascale Marquis, _MSc_ - Bioinformatics consultant
 * Alain Pacis, _Ph.D_ - Bioinformatics consultant
 * Robert Syme, _Ph.D_ - Bioinformatics consultant
 * Senthilkumar Kailasam, _Ph.D_ - Bioinformatics consultant
 * Paul Stretenowich, _MSc_ - Bioinformatics consultant
 * Ksenia Zaytseva, __ - Scientific Data Architect
 * Lindsay Dayton, _MSc_ - Research administrator
 * Ksenia Egorova, __ - Research administrator
 * Rachade Hmamouchi, __ - Program manager
 * David Anderson, _B.FA_ - Web designer
 * Romain Grégoire, Web Application Developer
 * David Lougheed, Web Application Developer
 * Patricia Goerner-Potvin, _MSc_ - PhD student
 * Maxime Caron, _MSc_ - PhD student
 * Jeffrey Hyacinthe, PhD student
 * Audrey Baguette, MSc student
 * Cristian Groza, Undergraduate student
 * Alexis Nolin Lapalme, Undergraduate student
 * David Lougheed, Undergraduate student


Collaborators:

 * Simon Gravel, _Ph.D_ - Assistant Professor at McGill University - [Simon's lab](simongravlabel.lab.mcgill.ca/Home.html)

# Mailing list

Students will be added to the mailing list once accepted into the program.

# Student application
Selected students will be automatically added to the mailing list

Selected students should follow the [student application guideline](Student_application.md)

# INSTRUCTIONS

Please read the list of available projects hosted for this year. If you are interested in a project, please complete the *Selection tests* for that project and contact the project mentors directly by email. If the project does not have Selection tests, contact the project mentors with your CV and ask about their requirements. Please **DO NOT post on the genpipes forum**, as not all mentors monitor the forum.


-----------------------------

# Proposed Projects 


## Creating a new pipeline for long-read RNA-seq using StringTie2

The majority of contemporary genomics and transcriptomics research is carried out using short-read technology such as the output of Illumina sequencers. However, newer long-read technologies such as PacBio and Oxford Nanopore (ONT) are becoming more prevalent due to the advantages they offer over short reads. The main advantage of long reads is that they span a much larger portion of the genome or transcriptome, making it easier to detect events such as structural variants or isoforms. As more researchers begin to take advantage of long reads, GenPipes needs to evolve and support long-read technology in its main pipelines. The objective of this project is to create a new RNA-seq pipeline (rnaseq_longreads), that supports long-read inputs. The new pipeline would be created based on the current versions of the RNA-seq pipeline, with the addition of the minimap2 aligner as well as StringTie2 and Ballgown for generating transcript counts. If time allows, in addition to implementing a long-read RNA-seq pipeline within the GenPipes framework, the student will help update the RNA-seq pipeline to also use StringTie2 as well as test both pipelines to ensure they are working properly. 


### Developer profile

Required skills: Python, R, bash, git
Nice to have: Experience with genomics data, especially long-reads

### Selection tests

1. Install the following software in your computing environment: 
        a. [StringTie2](https://github.com/mpertea/stringtie2)  (run test suite to ensure it is working). 
        b. The [Ballgown](http://bioconductor.org/packages/release/bioc/html/ballgown.html) R-Bioconductor library 
                i. If required, install R and any additional dependencies.
        c. [Tablemaker](https://github.com/leekgroup/tablemaker).   
        
2. Download the following nanopore mouse RNA-seq datasets from [this recent study](https://www.nature.com/articles/s41598-019-51470-9): 
        a. Brain C1: [genome BAM file](http://www.genoscope.cns.fr/externe/ONT_mouse_RNA/data/genome/RNA_nanopore.brain.C1R1_mapping_E94_minimap2_primary_no_read_less_than_80QC_genome_convert.sorted.bam)
        b. Liver C1: [genome BAM file](http://www.genoscope.cns.fr/externe/ONT_mouse_RNA/data/genome/RNA_nanopore.liver.C1R1_mapping_E94_minimap2_primary_no_read_less_than_80QC_genome_convert.sorted.bam)
        
3. Using StringTie2 long-read mode, generate a GTF file for each of these samples. 

4. Run Tablemaker on the two samples above (use the BAM and GTF files used above). 

5. Import the output of Tablemaker into R using Ballgown. 


Save your work in an external repository and send us a link to it. The repository must contain: 

    * A bash script with your StringTie2 and Tablemaker commands. 
    * An R script with your Ballgown commands. 
    * The first 1000 lines of both GTF files generated using StringTie2. 
    * The first 1000 lines of the FPKM matrix produced by Ballgown, saved as a csv. 
        * Hint: use the `texpr` function in Ballgown to obtain this matrix.


### Mentors
[Jose Hector Galvez](mailto:jose.hector.galvez@computationalgenomics.ca)

-----------------------------


## Large-scale modelling of genetic data

Genomic data poses formidable modelling challenges. At the simplest level, genetic information can be summarized as a matrix with rows corresponding to individuals and columns corresponding to genetic markers. Contemporary datasets have hundreds of thousands of rows and millions of columns. Even though we have pretty good mathematical models of how genetic data gets transmitted from generation to generation, fitting those on computers is VERY challenging.

Understanding genetic data requires careful modelling of historical events and efficient computing. Our group is involved in open-source efforts to build better simulations (https://github.com/tskit-dev/msprime), better encode genetic data (https://github.com/tskit-dev/tskit), and provide community curated quantitative models of human history (https://github.com/popsim-consortium/stdpopsim).

There are multiple related projects projects including:
* building more efficient simulation algorithms and data structures,
* implementing more biologically realistic simulations (including information about function , sex-specific recombination and mutation processes, biased gene conversion, inbreeding,etc).
and
* implementing existing historical models from the literature into model databases.


### Selection tests

Complete the notebooks fst_allel-hints.ipynb and wright-fisher-hints.ipnb found in the "data_test" folder by filling in the blanks and ellipses (…), run the code, and answer the interpretation questions.

### Mentors
[Dr. Simon Gravel](mailto:simon.gravel@mcgill.ca)

-----------------------------



