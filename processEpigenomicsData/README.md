## Epigenomics Input 

We model the chromatin as beads on a string. Each bead is assigned with a chromatin state, and will be labeled as a CTCF binding site in a given orientation or depending on the underlying Chip-Seq signal. Checkout the folder [chromatinStates](./chromatinStates) and [ctcfBindingSites](./ctcfBindingSites) to see how to get chromatin states and CTCF binding sites from genome wide Chip-Seq data. 

ChromHMM is used to process the epigenomics data, and must be installed to run all the scripts provided here. Detailed installation instructions for ChromHMM can be found [here](http://compbio.mit.edu/ChromHMM/). 

