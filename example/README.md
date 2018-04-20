
## Getting start to build the first simulation  

### Chromatin states derived from the underlying combinatorial patterns of key histone marks.  
To construct the chromatin states for GM12878, chromosome 1, run the following command:  
```
./example/genChromState.sh
```
The generated chromatin states file is located at `./chromatinStates/model_input/Gm12878/Gm12878_chr1_chromatin_states.txt`  

To process other chromosomes and cell types, go to folder `./chromatinStates/` and refer to `./chromatinStates/README.md` for details.  

### CTCF-binding sites derived from ChIP-Seq experiments.
To construct the CTCF-binding sites for GM12878, chromosome 1, run the following command:
```
./example/genCTCFbinding.sh
```
The generated chromatin states file is located at `./ctcfBindingSites/processedCTCF/model_input/`  

To process other chromosomes and cell types, go to folder `./ctcfBindingSites/` and refer to `./ctcfBindingSites/README.md` for details.  

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
