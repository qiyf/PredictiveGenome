# This is a branch program to extract narrow peak binding location of ctcf and cohesin (rad21 subunit)

By using the script, simply execute the python script:
```
python processingNarrowPeak.py [-C Celltype] [-c chromosome_id_array]
```
by default is calculating: Gm12878, chromosome 1 

**[Celltype]** can be selected from the following list:  
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562  

**[chromosome_id_array]** can be selected from:  
>1 ~ 22

by default, the output of the binding narrow peak located in the folder `./[Celltype]/ctcf(rad21)/`.

The original narrowPeak data (located in the folder `./narrowPeak/`) is downloaded from the data sources indicated in the ExtendDataSheet. Raw NarrowPeak data can be downloaded by executing:
```
./narrowPeak/download.sh
```
and the downloaded files should be unzipped accordingly.