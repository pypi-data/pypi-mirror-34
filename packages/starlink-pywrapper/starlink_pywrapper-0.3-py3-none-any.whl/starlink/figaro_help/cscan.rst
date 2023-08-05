

CSCAN
=====


Purpose
~~~~~~~
To display cuts through an CUBE


Description
~~~~~~~~~~~
This displays line profiles from a sorted data cube (i.e. the first
dimension is that of wavelength).


Parameters
~~~~~~~~~~
CUBE = FILE (Read) Name of CUBE for input YSTART = REAL (Read) display
lower limit YEND = REAL (Read) display upper limit TSTART = INTEGER
(Read) display lower limit TEND = INTEGER (Read) display upper limit
HARDCOPY = LOGICAL (Read) use hard graphics device for display


Subroutines/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CANAXLIM : Reset parameters for axis limits CLGRAP : Close graphics
CNF_PVAL : Full pointer to dynamically allocated memory DRAWPOLY :
Draw a polyline GR_SELCT : Select/open a graphics device
DSA_AXIS_RANGE : Get range to use in a given axis direction DSA_CLOSE
: Close DSA DSA_INPUT : Open file for input DSA_DATA_SIZE : Get size
of data DSA_GET_RANGE : Get range of values of main data array
DSA_MAP_DATA : Map main data array DSA_MAP_AXIS_DATA : Map axis data
array DSA_OPEN : Open DSA GEN_RANGEF : Get range of array PAR_BATCH =
LOGICAL Find out if running in batch mode PAR_RDKEY : Get value of
keyword PAR_WRUSER : Write character string to user


