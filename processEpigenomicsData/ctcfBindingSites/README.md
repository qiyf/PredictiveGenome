## Build orientation specific CTCF-binding sites

We defined the location of CTCF-binding sites using the ChIP-Seq narrow-peak binding profiles of CTCF together with Rad21 (Cohesin subunit). A near binding peak of Cohesin to the binding peak of CTCF is required to define a CTCF-binding site. And we further determine the orientation of the CTCF-binding site using the CTCF-binding motifs.


### NarrowPeak files

CTCF and Rad21 narrow-peak files can be downloaded by running the following command:
```
cd ./ctcfBindingSites/raw.narrowPeak/narrowPeak/; ./download.sh
```
The downloaded files should be unzipped accordingly.

These narrow-peak files are further processed by the python program [`processingNarrowPeak.py`](./ctcfBindingSites/processingNarrowPeak.py) into txt files that contains only the genomic positions of individual binding sites for a given chromosome.

Usage:
```
python processingNarrowPeak.py [-C Celltype] [-c chromosome_id_array]
```
by default is calculating: Gm12878, chromosome 1.

**[Celltype]** can be selected from the following list:  
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562  

**[chromosome_id_array]** can be any non-repeated subset selected from:  
>1 ~ 22

by default, the output of the binding narrow peak located in the folder `ctcfBindingSites/raw.narrowPeak/[Celltype]/ctcf(rad21)/`.

### Motif files

The motif files that are used to determine the orientation of CTCF-binding sites are from the following references:

>Rao, Suhas S.P. et al. *Cell* **159**, 1665-1680 (2014).  
>Kheradpour, P. & Kellis, M. *Nucleic Acids Res.* **42**, 2976-2987 (2014).

The python program to process the downloaded NarrowPeak files is located at `ctcfBindingSites/motif_file/prepareMotif.py`.

Usage: 
```
python prepareMotif.py [-m motif_file] [-p motif_folder_name_option] [-c chromosome_id_array]
```
**[motif_file]** is the name of the downloaded motif file.

**[motif_folder_name_option]** is the name of the processed folder.

**[chromosome_id_array]** can be any non-repeated subset selected from:  

> 1 ~ 22

by default is calculating: motif file from the first reference abovementioned and chromosome 1 (with the folder name as 'lbm'). The other two motif folders are calculated based on the motif files from the second reference abovementioned.
