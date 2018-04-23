# Getting started the first simulation  

## Generate epigenomics data as model input
To construct the chromatin states and CTCF-binding sites for GM12878, chromosome 1, run the following command:  
```
./example/genEpigData.sh
```
The generated epigenomics input files are located at `./runMolecularDynamics/inputFiles/epig_input/`

To process other chromosomes and cell types, refer to `./runMolecularDynamics/inputFiles/epig_input/chromStates/README.md` and `./runMolecularDynamics/inputFiles/epig_input/ctcfSites/README.md` for detail.  

## Run the simulation
To initialize the simulation for GM12878, chromosome 1, run the following command:  
```
./example/runSimulation.sh [-p ncpu] [-i partition] [-t simulation_time] [-l Lammps_dir]
```
There would be an option for the availability of the computing cluster. If cluster resource is available, specify the number of cpu, the name of the partition available on the cluster, and the time limit of the node.  

To process other chromosomes and cell types, refer to `././runMolecularDynamics/README.md` for details.  

## Analyze the simulated chromatin conformations
### Simulated contact maps
To calculate the contact map for GM12878, chromosomes 1 after running the simulation, run the following command:
```
./example/calContactMap.sh [-n runnumber] [-u username] [-i partition]
```
There would be an option for the availability of the computing cluster. If cluster resource is available, specify the number of parallel running be included to calculate the contact map, the username on the cluster, and the name of the partition available on the cluster.  

To process other chromosomes and cell types, refer to `./analyzeChromatinConformation/contactMap/README.md` for details.  

The experimental Hi-C data is available with GEO accession number GSE63525 [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525).  

### Chromosome conformation visualization
A series of useful scripts are provided to enable the visualization of the simulated chromosome structure ensemble through the VMD software. The VMD software can be download [here](http://www.ks.uiuc.edu/Research/vmd/). Refer to `./analyzeChromatinConformation/visStructure/README.md` for details about the steps on visualizing the structures.  
