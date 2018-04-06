# This is to build up parallel simulations for calculation of contact maps

By using the script, simply execute the python script:
```
python parallel_cmap.py [cell_type] [runnum] [chromosome_id_array]
```
through indication of cell_type, the total number of parallel simulations and the array of chromosome id that contact maps are needed to be calculated
or
```
python parallel_cmap.py
```
is calculating by default: Gm12878, 8 parallel runs, chromosome 1

[cell_type] can be selected from the following list:  
>Gm12878  
>H1hesc  
>Helas3  
>Hepg2  
>Huvec  
>K562  

[chromosome_id_array] can be a subset selected from:  
>1 ~ 22