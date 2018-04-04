# This is a extraction for narrow peak binding location of ctcf and cohesin (rad21 subunit)

By using the script, simply execute the python script:
```
python processingNarrowPeak.py [cell_type] [chromosome_id]
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

The original narrowPeak data (located in the folder './narrowPeak/') is downloaded from the data sources indicated in the ExtendDataSheet.

by default, the output of the binding narrow peak located in the folder './[cell_type]/ctcf(rad21)/'.
