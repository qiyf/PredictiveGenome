#########################################################################
# Author: Charlse.Zhang
# Created Time: Sun 27 Jul 2014 03:20:38 PM CDT
# File Name: compile.sh
# Description: 
#########################################################################
#!/bin/bash

module load engaging/intel/2013.1.046
ifort -o cmap          contact_map.f90

#ifort -o eavg_blas_msg      ensemble_average_ms.f90
#ifort -o eavg_blas_msg_ideal      ensemble_average_ms_ideal.f90
#ifort -o eavg_blas_msg_nov      ensemble_average_ms_no_overlap.f90
#ifort -o eavg_blas_msg_fi      ensemble_average_ms_full_ideal.f90
#ifort -o eavg_blas_msg_log      ensemble_average_ms_log.f90
#ifort -o eavg_blas_msg_log_multi      ensemble_average_ms_log_multi.f90
#ifort -o eavg_blas_msg_nov      ensemble_average_ms_no_overlap.f90
#ifort -o eavg_nov_mgrid      ensemble_average_no_overlap_more_grid.f90
#
#ifort -o gyration     gyration.f90 
#
#ifort -o eavg     ensemble_average.f90 
#ifort -o eavg_q     ensemble_average_quies.f90 
#ifort -o eavg_m     ensemble_average_match.f90 
ifort -o eavg_mc     ensemble_average_match_counter.f90 
