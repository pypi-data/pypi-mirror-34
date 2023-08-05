

ISCAN
=====


Purpose
~~~~~~~
To display cuts through an IMAGE


Description
~~~~~~~~~~~
Either the user can go into a loop in which (s)he is prompted for the
start and end x-sects to extract, or the program will go through the
data, displaying successive cuts.


Parameter
~~~~~~~~~
IMAGE = FILE (Read) Image to take cuts from XSTART = REAL (Read)
Starting wavelength (or pixel number if not calibrated) XEND = REAL
(Read) End wavelength etc. YSTART = INTEGER (Read) Starting cross-
section YEND = INTEGER (Read) End cross-section YBLOCK = INTEGER
(Read) Width to extract from data in cross-sections (if scanning) SCAN
= LOGICAL (Read) If to scan through data HARDCOPY = LOGICAL (Read) If
to plot in hard-copy


Subroutine/functions called
~~~~~~~~~~~~~~~~~~~~~~~~~~~
CANAXLIM : Reset parameters for axis limits CNF_PVAL : Full pointer to
dynamically allocated memory GRCLOSE : Close graphics GR_INIT :
Initialise graphics common blocks GR_SELCT : Open graphics, selecting
a device PLOT_SPECT : Plot a 1-d spectrum
DSA_CLOSE : Close DSA DSA_DATA_SIZE : Get data size DSA_FREE_WORKSPACE
: Free workspace DSA_GET_AXIS_INFO : Get axis units/label
DSA_GET_WORK_ARRAY : Get workspace DSA_INPUT : Open input file
DSA_MAP_AXIS_DATA : Map axis array DSA_MAP_DATA : Map data array
DSA_OPEN : Open DSA DYN_INCAD : Address offset FIG_XTRACT : Take slice
thru' data in X direction ICH_TIDY = INTEGER (Read) Remove control
characters from string PAR_QUEST : Get YES/NO response from user
PAR_RDKEY : Read key parameter PAR_RDVAL : Read value parameter
PAR_WRUSER : Write character string to user


