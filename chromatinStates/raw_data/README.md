# chromatin states defined by ChromHMM

Please be aware to compile the ChromHMM from the following link before using:  
[http://compbio.mit.edu/ChromHMM/](http://compbio.mit.edu/ChromHMM/)

15 chromatin states are defined based the epigenetic information of the following 6 cell types:
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562  

The links for downloading the files for 12 histone marks of each cell type are provided in the Extend Data Sheet.
ChromHMM script `../src/run_chromHMM_5kb_6celltypes_15states.sh` is used to calculate the chromatin states.
 
If new cell type(s) are added, please be aware of corresponding the new chromatin states with the present-defined ones. 
