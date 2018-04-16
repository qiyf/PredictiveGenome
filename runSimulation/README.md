# This is the main program to run the simulation  
Usage:
```
python main.py [-C Celltype] [-n runnumber] [-N number_of_Node] [-p number_of_cpu] [-i partition] [-t simulation_time] [-l Lammps_dir] [-d near_CTCF_threshold] [-r simulation_steps] [-c chromosome_id_array]
```
or default:
```
python main.py
```
Note items in [] are optional. By default is calculating: Gm12878, chromosome 1, 8 parallel running.  

**[Celltype]** can be selected from the following list (case sensitive):
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562

**[runnumber]** specifies the number of parallel running. By default the value is 8. 

**[number_of_Node]** **[number_of_cpu]** **[partition]** **[simulation_time]** should be specified based on the computational capability. By defaul, the values are set to be 1 Node, 14 cpus, 48hrs at maximum.  

**[Lammps_dir]** should be specified as `/path-to-LAMMPS-folder/src/`.  

**[near_CTCF_threshold]** is the parameter that indicates the number of convergent CTCF pairs that are separated by no more than a finite number of CTCF-binding sites in both orientations to mimic the finte processivity of cohesin molecules. The default value is set to be 4.  

**[simulation_steps]** indicates the number of MD steps. The default value is set to be 40 million steps.  

**[chromosome_id_array]** can be any non-repeated subset selected from:
>1 ~ 22

The manual would be available by executing:
```
python main.py -h
```