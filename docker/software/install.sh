#!/bin/bash

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -p /software/conda -b
CONDA=/software/conda/bin/conda

$CONDA config --add channels r
$CONDA config --add channels bioconda
$CONDA config --add channels conda-forge

$CONDA install -y conda-build
$CONDA install -y pytables blosc dask pyqt ipyparallel
$CONDA install -y r-irkernel pcre
$CONDA install -y r-ggplot2 r-plyr r-stringi r-igraph r-cpp r-quadprog

$CONDA install -y bwa htslib samtools vcftools bowtie2
$CONDA install -y blast fastqc fastx_toolkit seqtk rainbow
$CONDA install -y plink2
$CONDA install -y trimmomatic picard genepop bcftools bayescan
$CONDA install -y bedtools vcflib freebayes stacks pear qualimap
$CONDA install -y cutadapt mafft kraken mothur mummer cd-hit
$CONDA install -y muscle novoalign picard raxml snpeff spades trinity
$CONDA install -y fastq-join pear
$CONDA install -y eigensoft pyvcf pysam

$CONDA install -y bioconductor-biocinstaller
$CONDA install -y bioconductor-edger

$CONDA install -y jupyter jupyterhub scipy scikit-learn matplotlib
$CONDA install -y seaborn pandas rpy2
$CONDA install -y biopython

$CONDA create -n python2 python=2
source $CONDA/activate python2
$CONDA install -y pyrad 
$CONDA install -y fastq-join pear

$CONDA install -c http://conda.binstar.org/bpeng simuPOP
$CONDA install -y biopython qiime qiime-default-reference

source $CONDA/deactivate
