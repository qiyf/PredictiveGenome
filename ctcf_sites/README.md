# This is to generate the CTCF sites input file for the model

By using the script, simply execute the python script:
```
python processingCTCF.py
```
is calculating by default : Gm12878, chromosome 1
or:
```
python processingCTCF.py [cell_type] [chromosome_id]
```
to specify the cell type and chromosome id
or:
```
python processingCTCF.py [cell_type] [chromosome_id] [motif_buffer] [cap]
```
to further specify the buffer region (default 100bp) and nearest ctcf-cohesin center distance (default 50bp)

[cell_type] can be selected from the following list:  
>Gm12878  
>H1hesc  
>Helas3  
>Hepg2  
>Huvec  
>K562  

[chromosome_id] can be selected from:  
>1 ~ 22

by default, the direct output of CTCF index list located in the folder './processedCTCF/proc_data.50bp/[cell_type]/', while the output of CTCF list as input to the model located in the folder './processedCTCF/model_input/[cell_type]/' simultaneously
