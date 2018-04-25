# Process Epigenomics Data 

We model the chromatin as beads on a string. Each bead is assigned with a chromatin state, and will be labeled as a CTCF-binding site in a given orientation depending on the underlying Chip-Seq signal. Checkout the folder [`./chromatinStates`](./chromatinStates) and [`./ctcfBindingSites`](./ctcfBindingSites) to see how to obtain the chromatin states and CTCF-binding sites from genome-wide Chip-Seq data. 

## Chromatin states defined by ChromHMM

We built the chromatin states for the following six cell types using 12 key histone modifications from ENCODE that are indicated in the [Extend Data Sheet](https://www.biorxiv.org/highwire/filestream/86852/field_highwire_adjunct_files/1/282095-2.xlsx) of the [manuscript](https://www.biorxiv.org/content/early/2018/03/15/282095):
>Gm12878  
>H1hesc  
>Hela  
>Hepg2  
>Huvec  
>K562 

Once the epigenomics data are downloaded, ChromHMM is used to learn chromatin states from these genome-wide data. ChromHMM must be installed to run the [script]( ./chromatinStates/run_chromHMM_5kb_6celltypes_15states.sh). Detailed installation instructions for ChromHMM can be found [here](http://compbio.mit.edu/ChromHMM/). 

Note that if new cell type(s) are added, be aware of corresponding the new chromatin states with the present-defined ones through the generated emission pattern. 

## NarrowPeak and motif files for CTCF-binding

We defined the location of CTCF-binding sites using the ChIP-Seq NarrowPeak binding profiles of CTCF together with Rad21 (Cohesin subunit). A near binding peak of Cohesin to the binding peak of CTCF is required to define a CTCF-binding site. And we further determine the orientation of the CTCF-binding site using the CTCF-binding motifs.

The NarrowPeak files are downloaded from the source provided in the [Extend Data Sheet](https://www.biorxiv.org/highwire/filestream/86852/field_highwire_adjunct_files/1/282095-2.xlsx) of the [manuscript](https://www.biorxiv.org/content/early/2018/03/15/282095), and the motif files that are used to determine the orientation of CTCF-binding sites are from the following references:

>Rao, Suhas S.P. et al. *Cell* **159**, 1665-1680 (2014).
>Kheradpour, P. & Kellis, M. *Nucleic Acids Res.* **42**, 2976-2987 (2014).

### NarrowPeak files

Raw NarrowPeak data can be downloaded by executing:
```
cd ./ctcfBindingSites/raw.narrowPeak/narrowPeak/; ./download.sh
```
and the downloaded files should be unzipped accordingly.

The python program to process the downloaded NarrowPeak files is located at `ctcfBindingSites/raw.narrowPeak/prepareNarrowPeak.py`.

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
