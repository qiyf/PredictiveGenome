# Predictive Genome Model  
Predictive Genome Model is a predictive and transferable model to simulate the structure and dynamics of chromosomes.

## Dependencies  
The package for Predictive Genome Model is mainly written in Python. The modified LAMMPS package (LAMMPS-PreGenome) is written in C++. Environment of OpenMPI for compiling of the parallel version of LAMMPS is required. 

## Visualization of chromosome structures  
The information of trajectories stored in .dcd format can be visualized using VMD [http://www.ks.uiuc.edu/Research/vmd/](http://www.ks.uiuc.edu/Research/vmd/) or any other software that is capable of loading .dcd files and available online.

## Installation
Download the Predictive Genome Model source package by running the following comand:
```
git clone https://github.com/qiyf/PredictiveGenome.git
```
Download the modified LAMMPS source package by running the following comand:
```
https://github.com/qiyf/LAMMPS-PreGenome.git
```
or download the zip file from  
[https://github.com/qiyf/PredictiveGenome/archive/master.zip](https://github.com/qiyf/PredictiveGenome/archive/master.zip)  
[https://github.com/qiyf/LAMMPS-PreGenome/archive/master.zip](https://github.com/qiyf/LAMMPS-PreGenome/archive/master.zip)  
and extract both files under the same directory.

## Getting start to build the first simulation  
The 1D input of the model consists of two parts:  
### Chromatin states derived from the underlying combinatorial patterns of key histone marks.  
To construct the chromatin states for GM12878, chromosome 1, run the following command:  
```
./example/genChromState.sh
```
The generated chromatin states file is located at ./chromatinStates/model_input/Gm12878/Gm12878_chr1_chromatin_states.txt  
To process other chromosomes and cell types, go to folder ./chromatinStates/ and refer to ./chromatinStates/README.md for details.  
### CTCF-binding sites derived from ChIP-Seq experiments.
To construct the CTCF-binding sites for GM12878, chromosome 1, run the following command:
```
./example/genCTCFbinding.sh
```
The generated chromatin states file is located at ./ctcfBindingSites/processedCTCF/model_input/  
To process other chromosomes and cell types, go to folder ./ctcfBindingSites/ and refer to ./ctcfBindingSites/README.md for details.  
### Run the simulation
To initialize the simulation for GM12878, chromosome 1, run the following command:  
```
./example/runSimulation.sh [-p ncpu] [-i partition] [-t simulation_time] [-l Lammps_dir]
```
There would be an option for the availability of the computing cluster. If cluster resource is available, specify the number of cpu, the name of the partition available on the cluster, and the time limit of the node.  
To process other chromosomes and cell types, go to folder ./runSimulation/ and refer to ./runSimulation/README.md for details.  
### Contact map
To calculate the contact map for GM12878, chromosomes 1 after run the simulation, run the following command:
```
./example/calContactMap.sh [-u username] [-i partition]
```
There would be an option for the availability of the computing cluster. If cluster resource is available, specify the number of cpu, the name of the partition available on the cluster, and the time limit of the node.  
To process other chromosomes and cell types, go to folder ./contactMap/ and refer to ./contactMap/README.md for details.  
The experimental Hi-C data is available with GEO accession number GSE63525 [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525).