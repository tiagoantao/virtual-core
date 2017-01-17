#!/bin/bash

if [ ! -d /vcore/software/conda/bin ]; then
  wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

  bash Miniconda3-latest-Linux-x86_64.sh -p /vcore/software/conda -b
fi

CONDA=/vcore/software/conda/bin/conda

#$CONDA config --add channels r
#$CONDA config --add channels bioconda
#$CONDA config --add channels conda-forge

$CONDA install -y conda-build gcc
$CONDA install -y pytables blosc dask pyqt ipyparallel
$CONDA install -y r-irkernel pcre
$CONDA install -y r-ggplot2 r-plyr r-stringi r-igraph r-rcpp r-quadprog
$CONDA install -y r-sp pydotplus
$CONDA install -y tensorflow

$CONDA install -y bwa htslib samtools vcftools bowtie2
$CONDA install -y blast fastqc fastx_toolkit seqtk rainbow
$CONDA install -y plink2 hmmer
$CONDA install -y trimmomatic picard genepop bcftools bayescan
$CONDA install -y bedtools vcflib freebayes stacks pear qualimap
$CONDA install -y cutadapt mafft kraken mothur mummer cd-hit
$CONDA install -y muscle novoalign picard raxml snpeff spades trinity
$CONDA install -y fastq-join pear gffutils
$CONDA install -y eigensoft pyvcf pysam

$CONDA install -y bioconductor-biocinstaller
$CONDA install -y bioconductor-edger

$CONDA install -y jupyter jupyterhub scipy scikit-learn matplotlib
$CONDA install -y seaborn pandas rpy2
$CONDA install -y biopython kallisto
$CONDA install -y bioblend blat
$CONDA install -y stacks transdecoder

$CONDA create -y -n python2 python=2
source $CONDA/activate python2
$CONDA install -y pyrad 
$CONDA install -y fastq-join pear

$CONDA install -y -c http://conda.binstar.org/bpeng simuPOP
$CONDA install -y biopython qiime qiime-default-reference bioblend

source $CONDA/deactivate

#$CONDA create -y -n trinity trinity
