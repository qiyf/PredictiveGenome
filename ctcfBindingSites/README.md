# This is to generate the CTCF sites input file for the model

By using the script, simply execute the python script:
```
python processingCTCF.py
```
is calculating by default : Gm12878, chromosome 1. With motif matching buffer region +/-100bp, requirement for CTCF-cohesin nearest distance 50bp. 
or:
```
python processingCTCF.py [-C Celltype] [-c chromosome_id] [-b binding_flexibility] [-p CTCF-cohesin_nearest_dist]
```
to specify the cell type, chromosome id, and the corresponding two parameters.
or:
```
python processingCTCF.py [-Cell Celltype] [-chrom chromosome_id] [-bindflex binding_flexibility] [-cap CTCF-cohesin_nearest_dist]
```
e.g.
```
python processingCTCF.py -C K562 -c 1 10 19 21 -b 100 -p 50
```
is to calculate K562, chromosome 1, 10, 19, 21 with the corresponding two parameters as 100bp and 50bp (default values).

[Celltype] can be selected any one from the following list (case sensitive):  
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562  

[chromosome_id] can be selected any ones from:  
>1 ~ 22

by default, the direct output of CTCF index list located in the folder './processedCTCF/proc_data.50bp/[cell_type]/', while the output of CTCF list as input to the model located in the folder './processedCTCF/model_input/[cell_type]/' simultaneously.
