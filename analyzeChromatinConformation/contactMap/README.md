# This is a branch program to calculate the contact maps based on the trajectories of MD simulations

## Calculate contact maps

The simulated contact maps based on the result trajectories of MD simulation can be calculated by using the code [`calContactMap.py`](./calContactMap.py) that is provided.  

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

The processed output of the individual contact maps are located in the folder `./[Celltype]/[chrId]/[runId]/`, the combined maps are located in the folder [`./cmap/`](./cmap/).  

The manual would be available by executing:  
```
python calContactMap.py -h
```

The core program to calculate the contact map from trajectory files is a FORTRAN code located [here](../../src/cmap/FORTRAN/). It has been compiled with ifort compiler. It can also be compiled with gfortran, but be aware that having either of these compilers installed beforehand is necessary. 

## Visualize contact maps with MATLAB

To visualize the contact maps, a MATLAB script [`visContactMap.m`](./visContactMap.m) is provided. Note that the corresponding raw Hi-C maps with consistent resolution need to be downloaded beforehand by executing the following command:

```
cd ./hic/rawMap/; ./download.sh
```

A pack file for the contact map of GM12878 would be downloaded and then unpacked, which may take a little while for the whole process. The raw Hi-C maps are downloaded from:  

> Rao, Suhas S.P. et al. *Cell* **159**, 1665-1680 (2014).

Then open [MATLAB](https://www.mathworks.com/products/matlab.html) and execute the script [`visContactMap.m`](./visContactMap.m) to plot the contact map. Type in the parameters such as the cell type and chromosome id accordingly. Leave the option empty if the default is satisfied. Note that the path for the Hi-C maps will be directed to the location where the Hi-C maps are downloaded by default when executing the MATLAB script. 

