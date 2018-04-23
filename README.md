# DRAGON  

![DRAGON logo](https://github.com/qiyf/PredictiveGenome/blob/dragon/images/logo.png)

DRAGON is a software package to enable De novo, and RAtional prediction of Genome organizatiON. It provides an implementation of the model proposed in the [manuscript](https://www.biorxiv.org/content/early/2018/03/15/282095) to simulate chromatin structure and dynamics. With DRAGON, one can predict the structure of a 25Mb long chromatin region from a variety of cell types using genome-wide profiles of histone modifications and CTCF molecules. 

The package is mainly written in Python, and it streamlines all the necessary steps to process [epigenomics data](./processEpigenomicsData/), to perform [molecular dynamics simulations](./runMolecularDynamics/) and to analyze [predicted conformational ensmeble](./analyzeChromatinConformation/) for the chromatin. 

## Installation
To install DRAGON, one can download the source code by running the following command:
```
git clone https://github.com/ZhangGroup-MITChemistry/DRAGON.git
```
or download the zip file with the link:

[https://github.com/ZhangGroup-MITChemistry/DRAGON/archive/master.zip](https://github.com/ZhangGroup-MITChemistry/DRAGON/archive/master.zip)  

After the installation of DRAGON, one will need to install and compile [LAMMPS package](http://lammps.sandia.gov/) to enable molecular dynamics simulations. This can be done by executing the following command:

```
./LAMMPS.sh
```

Note that GCC compiler module need to be installed beforehand and an environment of OpenMPI is needed to compile the parallel version of LAMMPS. 

## Usage

We model the chromatin as beads on a string. Each bead is assigned with a chromatin state, and will be labeled as a CTCF binding site in a given orientation depending on the underlying Chip-Seq signal. 

The exact process is illustrated with the following flow chart. 

![Flow chart](https://github.com/qiyf/PredictiveGenome/blob/dragon/images/flow_chart.png)

Please follow the steps below to begin the simulation of chromatin structure of chr1 from GM12878. All the scripts are provided in the example folder. See main.py for more advanced simulation with multiple chrs. 

### Process Epigenomics Data
```
./1-processEpigenomics.sh
```

This scripts generates the chromatin states using six cell types. ChromHMM is used to process epigenomics data and define chromatin states. See `./processEpigenomicsData/README.md` for its installation and usage. ChIP-Seq signals for the CTCF-binding are used to define CTCF-binding sites. 

### Run Molecular Dynamics Simulation
We use LAMMPS to simulate chromatin structure and dynamics. See `./runMolecularDynamics/README.md` for its detailed usage. 

#### Select a 25Mb chromatin region
```
./2-selectChromatin.sh
```

The 25Mb long chromatin region is indicated in the file `./src/chr_region.txt`. The format is in the following:
>chromosome_id 	start_position(Mb) 	end_position
>1				20					45  
>2				20					45  
>3				20					45  
>4				20					45  

If a different 25Mb chromatin region for any individual chromosome is desired, simply change the start and end position.

#### Extract Epigenomics input

```
./3-ExtractEpigenomics.sh
```

#### Build LAMMPS input

```
./4-BuildLammps.sh
```

#### Run Simulation

```
./5-runMD.sh
```

### visualize 3D structure and contact map
A series of useful scripts are provided in the folder `./analyzeChromatinConformation/` to visualize chromatin structure with [VMD](http://www.ks.uiuc.edu/Research/vmd/) and to analyze contact maps using [MATLAB](https://www.mathworks.com/products/matlab.html). Installation of these two software packages are highly recommended. See `./analyzeChromatinConformation/contactMap/README.md`and `./analyzeChromatinConformation/visStructure/README.md` for detailed instructions of usage. 

### Start the first simulation
The `./example` folder outline the steps to simulation chromosome 1 from GM12878 cells. See `./example/README.md`for detailed instructions of usage. 
