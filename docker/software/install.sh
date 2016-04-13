#!/bin/bash

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -p /software/conda -b

/software/conda/bin/conda config --add channels r
/software/conda/bin/conda config --add channels bioconda

/software/conda/bin/conda install -y conda-build

/software/conda/bin/conda install -y bwa htslib samtools vcftools bowtie2
/software/conda/bin/conda install -y blast fastqc fastx_toolkit seqtk rainbow
/software/conda/bin/conda install -y trimmomatic picard genepop bcftools bayescan
/software/conda/bin/conda install -y bedtools vcflib freebayes stacks pear qualimap
/software/conda/bin/conda install -y cutadapt mafft kraken mothur mummer cd-hit
/software/conda/bin/conda install -y muscle novoalign picard raxml snpeff spades trinity
/software/conda/bin/conda install -y ddocent eigensoft

/software/conda/bin/conda install -y bioconductor-biocinstaller

/software/conda/bin/conda install -y jupyter scipy scikit-learn matplotlib
/software/conda/bin/conda install -y biopython seaborn pandas

/software/conda/bin/conda create -n dDocent python=3
source /software/conda/bin/conda/activate dDocent
/software/conda/bin/conda install -c bioconda ddocent
source /software/conda/bin/conda/deactivate

/software/conda/bin/conda create -n python2 python=2
source /software/conda/bin/conda/activate python2
/software/conda/bin/conda install -c bioconda pyrad 
/software/conda/bin/conda install -y jupyter scipy scikit-learn matplotlib
/software/conda/bin/conda install -y biopython seaborn pandas
/software/conda/bin/conda install -c http://conda.binstar.org/bpeng simuPOP

source /software/conda/bin/conda/deactivate
