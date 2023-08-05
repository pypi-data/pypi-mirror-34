

FIBDISP
=======


Purpose
~~~~~~~
To analyse a fibre cube


Description
~~~~~~~~~~~
This cube should have been created using FIB2CUBE. Options available
include displaying planes of the cube and profiles and fitting
Gaussians etc. to these profiles.


Parameters
~~~~~~~~~~
CUBE = FILE (Read) Cube for display This should be a file produced by
FIB2CUBE, containing a .FIBRE structure. YSTART = REAL (Read) analysis
lower limit The data between the limits ystart and yend is extracted
and the resultant spectrum is used to locate the lines. YEND = REAL
(Read) analysis upper limit The data between the limits ystart and
yend is extracted and the resultant spectrum is used to locate the
lines. YBLOCK = REAL (Read) Enter analysis x-sect width Each window is
of this width (except perhaps the final one). TSTART = REAL (Read)
analysis lower limit The data between the limits tstart and tend is
extracted and the resultant spectrum is used to locate the lines. TEND
= REAL (Read) analysis upper limit The data between the limits tstart
and tend is extracted and the resultant spectrum is used to locate the
lines. TBLOCK = REAL (Read) Enter analysis blocking width in 3rd
dimension Each window is of this width (except perhaps the final one).
DEVICE = CHARACTER (Read) Device for display ITERATION = INTEGER*2
(Read) New value of itteration OUTABLE = FILE (Write) Name for EXTATIC
file VCORR = REAL (Read) correction to apply to radial velocities TOLS
= CHARACTER (Read) For use in batch only FITRAT = REAL (Read) Ratio of
widths, heights, or separation, for double fits CALRAT = INTEGER
(Read) Ratio of number of iteration to default OUTPUT = FILE (Write)
Name for output file FIT_MODEL = CHARACTER (Read) Model of fit to
perform LOW = REAL (Read) Minimum value for display HIGH = REAL (Read)
Maximum value for display ABSORPTION = LOGICAL (Read) Allow fitting of
absorption lines BOUNDS = LOGICAL (Read) Perform bounded fits to lines
(in batch) HARDCOPY = LOGICAL (Read) produce hardcopy plots of fits
from cube TABLE = LOGICAL (Read) produce table of fits from cube PRINT
= LOGICAL (Read) Produce print out of rotation curves SHAPE = LOGICAL
(Read) Carry out shape analysis KEEP_ITT = LOGICAL (Read) Keep
itteration files' FIT = LOGICAL (Read) perform fitting AIC = LOGICAL
(Read) Use Akiakes information criterion for fitting WEIGHTS = LOGICAL
(Read) Use weights for fitting PRFITS = LOGICAL (Read) Print out
details of fitting FULL = LOGICAL (Read) Print out full details of
fits in table


Subroutine/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ACCRES : Access results structure DATA_WINDOW : Automatic fitting of
Gaussians etc. FIBMEN : Main menu FIBOUT : Create various output
FIBSLFIL : Take a slice through the cube and write it to a file
FIBSLICE : Take slice through cube and plot it APPLY_TOLS : Set/apply
tolerances GTPROF : Analyse line profile HEXDISPS : Display plane of
sorted "cube" (hexagonal array) HEXPRARR : Display array of profiles
(hexagonal array) MAPCUBE : Map data arrays RECTDISPS : Display plane
of sorted "cube" (rectangular array) RECTPRARR : Display array of
profiles (rectangular array)
CNF_PVAL : Full pointer to dynamically allocated memory GR_INIT :
Initialise graphics common blocks
DSA_AXIS_RANGE : Get axis limits DSA_FREE_WORKSPACE (DSA): Free
workspace DSA_GET_WORK_ARRAY : Get workspace DSA_GET_RANGE : Get
min/max of main data array PAR_GIVEN (PAR)(l): Find out parameter
given on command line PAR_QNUM (PAR)(l): Get number from user
PAR_RDCHAR (PAR): Get character string from user PAR_RDKEY (PAR): Get
key parameter response from user PAR_WRUSER (PAR): Write character
string to user


