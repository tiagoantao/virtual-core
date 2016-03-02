#!/bin/bash

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -p /software/conda -b
/software/conda/bin/conda config --add channels r
/software/conda/bin/conda config --add channels bioconda
/software/conda/bin/conda install -y bwa htslib samtools vcftools bowtie2
/software/conda/bin/conda install -y blast fastqc fastx_toolkit 
/software/conda/bin/conda install -y trimmomatic picard genepop bcftools 
/software/conda/bin/conda install -y bedtools vcflib freebayes

/software/conda/bin/conda install -y bioconductor-biocinstaller

/software/conda/bin/conda install -y jupyter scipy scikit-learn matplotlib
/software/conda/bin/conda install -y biopython


