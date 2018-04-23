# This is a branch program to calculate the contact maps based on the trajectories of MD simulations

## Calculate contact maps

The simulated contact maps based on the result trajectories of MD simulation can be calculated by using the code `calContactMap.py` that is provided.  

Usage:
```
python calContactMap.py [-C Celltype] [-n runnumber] [-j jobname] [-u username] [-i partition] [-c chromosome_id_array]
```
or default:
```
python calContactMap.py
```
Note items in [] are optional. By default is calculating: Gm12878, chromosome 1, 8 parallel running. 

**[Celltype]** can be selected from the following list (case sensitive):
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562

**[runnumber]** specifies the number of parallel running. By default, the value is 8. 

**[jobname]** specifies the name of the job on the cluster.  

**[number_of_cpu]** **[partition]** should be specified based on the cluster account and available cluster partition.  

**chromosome id array]** can be any non-repeated subset selected from:
>1 ~ 22

The processed output of the individual contact maps are located in the folder `./[Celltype]/[chrId]/[runId]/`, the combined maps are located in the folder `./cmap/`.  

The manual would be available by executing:  
```
python calContactMap.py -h
```

The core program to calculate the contact map from trajectory files is a FORTRAN code located at `/Dragon/src/FORTRAN/cmap.f90`. It has been compiled as './src/FORTRAN/cmap' with ifort compiler. It can also be compiled with gfortran, but have either of these compilers installed beforehand is necessary. 

## Visualize contact maps with MATLAB

To visualize the contact maps, a MATLAB script `visContactMap.m` is provided. Note that the corresponding raw Hi-C maps with consistent resolution need to be downloaded beforehand, and the path for the Hi-C maps needs to be indicated when executing the MATLAB script. The raw Hi-C maps can be downloaded from:  
>Rao, Suhas S.P. et al. *Cell* **159**, 1665-1680 (2014).

