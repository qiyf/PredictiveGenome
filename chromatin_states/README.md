# This is to generate the chromatin states input file for the model

By using the script, simply execute the python script:
```
python genChromState.py [cell_type] [chromosome_id]
```
by default is calculating: Gm12878, chromosome 1 

[cell_type] can be selected from the following list:  
>Gm12878  
>H1hesc  
>Helas3  
>Hepg2  
>Huvec  
>K562  

[chromosome_id] can be selected from:  
>1 ~ 22

by default, the output of ChromHMM located in the folder './raw_data/', while the generated files located in the folder './model_input/' simultaneously
