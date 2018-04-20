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


### Run the simulation
To initialize the simulation for GM12878, chromosome 1, run the following command:  
```
./example/runSimulation.sh [-p ncpu] [-i partition] [-t simulation_time] [-l Lammps_dir]
```
There would be an option for the availability of the computing cluster. If cluster resource is available, specify the number of cpu, the name of the partition available on the cluster, and the time limit of the node.  

To process other chromosomes and cell types, go to folder `./runSimulation/` and refer to `./runSimulation/README.md` for details.  

### Contact map
To calculate the contact map for GM12878, chromosomes 1 after running the simulation, run the following command:
```
./example/calContactMap.sh [-n runnumber] [-u username] [-i partition]
```
There would be an option for the availability of the computing cluster. If cluster resource is available, specify the number of parallel running be included to calculate the contact map, the username on the cluster, and the name of the partition available on the cluster.  

To process other chromosomes and cell types, go to folder `./contactMap/` and refer to `./contactMap/README.md` for details.  

The experimental Hi-C data is available with GEO accession number GSE63525 [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525).  

The visualization of the simulated chromosome structure ensemble is also available. Please refer to the **Visualization of chromosome structures** section on where to download the VMD software, and `./contactMap/README.md` for details about the steps on visualizing the structures.  


## Visualization of chromosome structures  
The information of trajectories stored in .dcd format can be visualized using VMD [http://www.ks.uiuc.edu/Research/vmd/](http://www.ks.uiuc.edu/Research/vmd/) or any other software that is capable of loading .dcd files and available online. Refer to `./PredictiveGenome/contactMap/README.md` for more details on visualization of the simulated chromosome structure.
