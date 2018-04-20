# DRAGON  
DRAGON is a software package to enable De novo, and RAtional prediction of Genome organizatiON. It provides an implementation of the model proposed in the [manuscript](https://www.biorxiv.org/content/early/2018/03/15/282095) to simulate chromatin structure and dynamics. With DRAGON, one can predict the structure of a 25Mb long chromatin region from a variety of cell types using genome-wide profiles of histone modifications and CTCF molecules. 

The package is mainly written in Python, and it streamlines all the necessary steps to process [epigenomics data](./chromatinStates), to perform molecular dynamics simulations and to analyze predicted conformational ensmeble for the chromatin. 


## Installation
To install DRAGON, one can download the source code by running the following command:
```
git clone https://github.com/qiyf/PredictiveGenome.git
```
or download the zip file with the link:  

[https://github.com/qiyf/PredictiveGenome/archive/master.zip](https://github.com/qiyf/PredictiveGenome/archive/master.zip)  

We use ChromHMM to process epigenomics data. See the README file in the Epigenomics folder for its installation and usage. 

We use LAMMPS to simulate chromatin structure and dynamics. See the README file in the Molecular Dynamics folder for its installation and usage. 

A series of useful scripts are provided in the tools folder to visualize chromatin structure with VMD and to analyze contact maps using Matlab. Installation of these two software packages are highly recommended. 

## Usage

We model the chromatin as beads on a string. Each bead is assigned with a chromatin state, and will be labeled as a CTCF binding site in a given orientation or depending on the underlying Chip-Seq signal. 

The exact process is illustrated with the following flow chart. 
