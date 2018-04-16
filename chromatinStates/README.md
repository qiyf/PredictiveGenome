# This is a branch program to generate the chromatin states input file for the model
Usage:
```
python genChromState.py [-C Celltype] [-c chromosome_id_array]
```
or default:
```
python genChromState.py
```
Note items in [] are optional. By default is calculating: Gm12878, chromosome 1.

**[Celltype]** can be selected from the following list (case sensitive):
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562

**[chromosome_id_array]** can be any non-repeated subset selected from:
>1 ~ 22

The processed output of the 15 states defined based on 12 histone marks with ChromHMM is located in the folder: `./raw_data/OUTPUTSAMPLE_5kb_6celltype_15states/`. The generated files as the input of modeling are located in the folder: `./model_input/`.

The manual would be available by executing:
```
python genChromState.py -h
```