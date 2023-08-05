

FITCONT
=======


Purpose
~~~~~~~
To fit a Chebyshev polynomial to the continuum for 2D data


Description
~~~~~~~~~~~
As with VIG, lines can be excluded from the polynomial fitting.
FITCONT stores the polynomial fitting coefficients in the actual data
file, for use by LONGSLIT (the program is specifically for use with
LONGSLIT, and of no use otherwise).


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) Input file XSECT = INTEGER (Read) Cross-section to
take first cut from


Subroutines called
~~~~~~~~~~~~~~~~~~
CLGRAP : Close graphics CNF_PVAL : Full pointer to dynamically
allocated memory CONTRL_CPOLY2 : Fit polynomials to points, finding
order if required COPR2D : Copy real to double precision FITCONT_ST :
Create .fitcont structure by a number of elements GR_SOFT : Open
softcopy device PGPAGE : Clear graphics screen PLOT_DATA : Plot data
REJECT_DATA : Reject data from polynomial fitting WEIGHT_FIT : Set
weight array
CNV_FMTCNV : Format conversion routine DSA_CLOSE : Close DSA
DSA_DATA_SIZE : Get data size DSA_FREE_WORKSPACE : Free workspace
DSA_GET_WORK_ARRAY : Get workspace DSA_INPUT : Open input file
DSA_MAP_AXIS_DATA : Map axis data DSA_MAP_DATA : Map data DSA_OPEN :
Open DSA DYN_INCAD : Address offset PAR_RDVAL : Read value from user
PAR_WRUSER : Write string to user


