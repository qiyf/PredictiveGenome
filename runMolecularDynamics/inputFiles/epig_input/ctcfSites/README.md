# This is a branch program to generate the CTCF-binding sites input file for the model
This is the program to generate the CTCF-binding sites input file of the model for the specific [25Mb chromatin region](../../../../src/chr_region.txt) that is selected for an individual chromosome of a cell type. 

Usage:

```
python genCTCFbinding.py [-C Celltype] [-b motif_match_flexibility] [-a CTCF-cohesin_nearest_dist] [-c chromosome_id_array]
```
or default:
```
python genCTCFbinding.py
```
Note items in [] are optional. By default is calculating: Gm12878, chromosome 1.  

**[Celltype]** can be selected any one from the following list (case sensitive):
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562

**[motif_match_flexibility]** is the parameter that indicates the region for the motif matching. The default value is set to be 100bp, which means that if a motif is found within 100bp of the binding site, the orientation of the binding site was then assigned based on the DNA sequence of that motif.  

**[CTCF-cohesin nearest dist]** is the parameter that indicates the requirement for the nearest genomic distance of CTCF with Rad21. The default value is set to be 50bp.  

**[chromosome_id_array]** can be any non-repeated subset selected from:
>1 ~ 22

The CTCF-binding sites input to the model is processed based on the NarrowPeak binding profiles and motifs located in this [folder](../../../../processEpigenomicsData/ctcfBindingSites/). The generated files as the input of modeling are located in the folder: `./[Celltype]/`.

The manual would be available by executing:

```
python genCTCFbinding.py -h
```
