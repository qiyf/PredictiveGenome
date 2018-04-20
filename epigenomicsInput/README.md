## Epigenomics Input 

We model the chromatin as beads on a string. Each bead is assigned with a chromatin state, and will be labeled as a CTCF binding site in a given orientation or depending on the underlying Chip-Seq signal. 

ChromHMM is used to process the epigenomics data, and must be installed to run all the scripts provided here. Detailed installation instructions for ChromHMM can be found [here](http://compbio.mit.edu/ChromHMM/). 

The 1D input of the model consists of two parts: chromatin states and CTCF-binding sites, which will be illrustrated in the following: 

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
