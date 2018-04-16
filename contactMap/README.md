# This is a branch program to calculate the contact maps based on the trajectories of the MD simulation
Usage:
```
python calContactMap.py [-C Celltype] [-n runnumber] [-j jobname] [-u username] [-i partition] [-c chromosome_id_array]
```
or default:
```
python calContactMap.py
```
Note items in [] are optional. By default is calculating: Gm12878, chromosome 1, 8 parallel running.  
[Celltype] can be selected from the following list (case sensitive):
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562  
[runnumber] specifies the number of parallel running. By default the value is 8.  
[jobname] specifies the name of the job on the cluster.  
[number_of_cpu] [partition] should be specified based on the cluster account and available cluster partition.
[chromosome id array] can be any non-repeated subset selected from:
>1 ~ 22  
The processed output of the individual contact maps are located in the folder './Celltype/chrId/runId/', the combined maps are located in the folder './cmap/'.  
The manual would be available by executing:  
```
python calContactMap.py -h
```