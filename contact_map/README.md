# This is to build up parallel simulations for calculation of contact maps

By using the script, simply execute the python script:
```
python parallel_cmap.py [cell_type] [runnum] [chromosome_id_array]
```
or
```
python parallel_cmap.py
```
is calculating by default: Gm12878, chromosome 1
the runnum is the total number of parallel simulations, default is 8

[cell_type] can be selected from the following list:  
>Gm12878  
>H1hesc  
>Helas3  
>Hepg2  
>Huvec  
>K562  

[chromosome_id_array] can be a subset selected from:  
>1 ~ 22