# ![DRAGON logo](https://github.com/qiyf/images/blob/master/logo2.png)

DRAGON is a software package to enable De novo, and RAtional prediction of Genome organizatiON. It provides an implementation of the model proposed in the [manuscript](https://www.biorxiv.org/content/early/2018/03/15/282095) to simulate chromatin structure and dynamics. With DRAGON, one can predict the structure of a 25Mb long chromatin region from a variety of cell types using genome-wide profiles of histone modifications and CTCF molecules. 

The package is mainly written in Python, and it streamlines all the necessary steps to process [epigenomics data](./processEpigenomicsData/), to perform [molecular dynamics simulations](./runMolecularDynamics/) and to analyze [predicted conformational ensemble](./analyzeChromatinConformation/) for the chromatin. 

## Installation
DRAGON can be installed by running the following command:
```
git clone https://github.com/ZhangGroup-MITChemistry/DRAGON.git
```
or by downloading the zip file with the link:

[https://github.com/ZhangGroup-MITChemistry/DRAGON/archive/master.zip](https://github.com/ZhangGroup-MITChemistry/DRAGON/archive/master.zip)  

DRAGON uses [LAMMPS](http://lammps.sandia.gov/), a molecular dynamics software package, for simulating chromatin structures. LAMMPS, together with our custom modifications, can be compiled and installed with the following command:

```
./src/LAMMPS.sh
```

Note that the [GCC](https://gcc.gnu.org/) compiler needs to be installed beforehand and an environment of [OpenMPI](https://www.open-mpi.org/) is needed to compile the parallel version of LAMMPS. 

## Usage

DRAGON models the chromatin as a coarse-grained bead-spring polymer, with each bead correponding to a five kb genomic segment.  This coarse-grained polymer is made cell type and chromosome specific by assigning each bead with a chromatin state. The polymer bead will also be labeled as a orientation dependent CTCF binding site if there is a strong binding signal in the corresponding region. With its underlying biochemistry specified, the structure of the chromatin can be predicted by simulating the sequence-specific potential energy function parameterized in our [manuscript](https://www.biorxiv.org/content/early/2018/03/15/282095) using LAMMPS. See the flow chart below for an illustration of the different steps for chromatin structure prediction.

![Flow chart](https://github.com/qiyf/images/blob/master/flow_chart.png)

We further provide step-by-step instructions below to simulate the structure of chromosome 1 from GM12878 cells. All the executable scripts are provided in the [`./example/`](./example/) folder. 

### I) Process Epigenomics Data

Before starting any structure predictions, we need to learn the chromatin states from genome-wide histone modification profiles, and identify the genomic location and orientation of CTCF binding sites. 

```
./example/1-processEpigenomicsData.sh
```

This script provide detailed instructions on how to process epigenomics data using [ChromHMM](http://compbio.mit.edu/ChromHMM/) and custom python scripts. 

### II) Run Molecular Dynamics Simulation

To start simulating chromatin structures, the following steps are necessary in order to incorporate the processed epigenomics input into data formats recognized by LAMMPS.


#### Select a 25Mb chromatin region

First, one needs to select a 25Mb long chromatin region of interest (the default is chr1:20-45Mb from GM12878 cells) by running the following script 

```
./example/2-selectChromatinRegion.sh
```

DRAGON currently can only simulate chromatin regions with a fixed length of 25Mb, but generalization to whole chromosomes is straightforward. 

This script produces a [txt file](./src/chr_region.txt) that lists the region of interested for each chromosome in the following format:
```
chromosome_id     start_position(Mb)      end_position(Mb)  
1                 20                      45  
2                 20                      45  
3                 20                      45  
4                 20                      45   
```

If a different chromatin region is desired, one can either modify the [chromtin region file](./src/chr_region.txt) or original script [`./example/2-selectChromatinRegion.sh`](./example/2-selectChromatinRegion.sh).

#### Extract epigenomics input

Second, one needs to extract chromatin states and CTCF binding sites for the selected chromatin region from results produced in step I).

```
./example/3-extractEpigenomicsInput.sh
```

Three txt files are generated to provide [`the chromatin state of each polymer bead`](./runMolecularDynamics/inputFiles/epig_input/chromStates/Gm12878/Gm12878_chr1_chromatin_states_From20MbTo45Mb.txt), [`the CTCF binding potency of each polymer bead`](./runMolecularDynamics/inputFiles/epig_input/ctcfSites/Gm12878/Gm12878_chr1_ctcf_position_From20MbTo45Mb.txt), and [`the location of nearest CTCF binding sites for each polymer bead`] (./runMolecularDynamics/inputFiles/epig_input/ctcfSites/Gm12878/Gm12878_chr1_ctcf_index_From20MbTo45Mb.txt). 
See [Chromatin States README](./runMolecularDynamics/inputFiles/epig_input/chromStates/README.md) and [CTCF-binding Sites README](./runMolecularDynamics/inputFiles/epig_input/ctcfSites/README.md) for details on file formats and data extraction.

#### Build LAMMPS input

Third, one needs to incorporate the epigenomic inputs produced from the last step into a topology file and an input file recognized by LAMMPS.

```
./example/4-buildLammpsInput.sh
```

The files produced by this script are located at [`./runMolecularDynamics/inputFiles/lmps_input/`](./runMolecularDynamics/inputFiles/lmps_input/) and in the simulation folder [`./runMolecularDynamics/run_folder/Gm12878/chr1/run00/`](./runMolecularDynamics/run_folder/Gm12878/chr1/run00/). 

#### Run simulation

```
./example/5-runMD.sh
```

A single simulation for chromosome 1, GM12878 is started by executing this script. The trajectory files are dumped as .dcd file located in the simulation folder [`./runMolecularDynamics/run_folder/Gm12878/chr1/run00/`](./runMolecularDynamics/run_folder/Gm12878/chr1/run00/). Note that this is to run the simulation in serial, which might be relatively slow but simple enough to be represented as part of the instruction. 


For the steps in this section, a [main python program](./runMolecularDynamics/main.py) is provided to incorporate all necessary steps and initialize simulations with different cell types and multiple chromosomes. See [README](./runMolecularDynamics/README.md) for detailed usage of that program.

### III) Analyze Chromatin Conformation

We use [MATLAB](https://www.mathworks.com/products/matlab.html) to analyze contact maps and [VMD](http://www.ks.uiuc.edu/Research/vmd/) to visualize chromatin structure. Installation of these two software packages is highly recommended. See [contact map README](./analyzeChromatinConformation/contactMap/README.md) and [structure visualization README](./analyzeChromatinConformation/visStructure/README.md) for detailed instructions on usage. 

#### Calculate and visualize contact map

```
./example/6-calcCMAP.sh
```

The simulated contact map for chromosome 1, GM12878 is calculated by executing this script. The core program to calculate the contact map from trajectory files is a FORTRAN code and has been compiled located at [`./src/cmap/FORTRAN/`](./src/cmap/FORTRAN/) with ifort compiler. It can also be compiled with gfortran, but have either of these compilers installed beforehand is necessary. 

The calculated contact map is located at [`./analyzeChromatinConformation/contactMap/cmap/`](./analyzeChromatinConformation/contactMap/cmap/). To visualize the contact map, use the provided [MATLAB script](./analyzeChromatinConformation/contactMap/visContactMap.m). See [README](./analyzeChromatinConformation/contactMap/README.md) for more detailed instructions. 

#### Visualize the 3D structure

```
./example/7-geneVMDScript.sh
```

The VMD script for the visualization of 3D structure for chromosome 1, GM12878 is generated by executing this script. The generated script is located at [`./analyzeChromatinConformation/visStructure/`](./analyzeChromatinConformation/visStructure/).  See [README](./analyzeChromatinConformation/visStructure/README.md) for detailed instruction of visualization steps with VMD.
