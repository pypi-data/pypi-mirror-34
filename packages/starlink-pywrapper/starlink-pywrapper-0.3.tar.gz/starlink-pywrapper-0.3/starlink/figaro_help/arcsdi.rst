

ARCSDI
======


Purpose
~~~~~~~
Correct for line curvature


Description
~~~~~~~~~~~
Program to allow correction of 2-d spectra for S-distortion using an
arc - as a preliminary stage prior to wavelength calibration and
scrunching. The lines are located by fitting gaussians to them. These
positions are then used to fit a chebyshev polynomial to - one for
each line. The intermediate positions are interpolated from these.
Once this is done the data are shifted and interpolated in the
x-section direction to align them all.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) Name of image for input This should be a file
containing an arc spectrum. ARC_OPTS = CHARACTER (Read) Enter arc fit
option NEW : set up a new wavelength calibration REPEAT : Itterate on
previous calibration. CLONE : CLone a previous calibration. OLD :
Correct using previous results OUTPUT = FILE (Write) Name of output
file File to contain corrected data. YSTART = INTEGER (Read) analysis
lower limit The data between the limits ystart and yend is extracted
and the resultant spectrum is used to locate the lines. YEND = INTEGER
(Read) analysis upper limit The data between the limits ystart and
yend is extracted and the resultant spectrum is used to locate the
lines. YBLOCK = INTEGER (Read) Enter analysis x-sect width Each window
is of this width (except perhaphs the final one). ITERATION =
INTEGER*2 (Read) New value of iteration ORDER = INTEGER (Read) order
for polynomial fitting This is for the continuity correction of the
data. Idealy the arc should have been pre-processed with ARCSDI, so a
low order e.g. 2 should be used. MAXLINES = INTEGER (Read) Maximum
number of lines to allow room for This must be greater than or equal
to the number of lines fitted, so room should be allowed in case any
more are to be added later. CLFILE = FILE (Read) Name of image for
cloning from This should be a file containing an arc spectrum. TOLS =
CHARACTER (Read) For use in batch only KEEP_ITT = LOGICAL (Read) keep
itteration files' PRFITS = LOGICAL (Read) Print out details of fitting
PLOTCORR = LOGICAL (Read) Plot correction?


Subroutines/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
APPLY : Apply correction APPLY_TOLS : Apply tolerances ARCSDI_CONTIN :
Fit polynomials to centres found by ARC_WINDOW ARCSDI_INIT : Open
input file ARC_WINDOW : Find line centres by fitting Gaussians
ARC_INIT : Initialise common arrays CLGRAP : Close graphics CLONE_MODE
: CLONE continuum locations etc. from another file GR_SELCT : Open
graphics device CNF_PVAL : Full pointer to dynamically allocated
memory INIT_RES : Initialise results structure MAP_DATA : Map data
MAP_RES : Map results structure NEW_ARC : Create results structure
QMENU : Get menu response from user REFINE_RES : Check results
structure exists, and get size SETUP_ARC2 : Locate continua LOOK :
Output values of main results array UNMAP_RES : Unmap results
structure
DSA_CLOSE : Close DSA system DSA_AXIS_RANGE : Get axis limits
DSA_FREE_WORKSPACE : Free workspace DSA_GET_WORK_ARRAY : Get workspace
DSA_OUTPUT : Create output file DSA_MAP_DATA : Map main data array
FIG_XTRACT : Take slice thru' data in X direction PAR_RDKEY : Read key
parameter PAR_RDVAL : Read value parameter PAR_WRUSER : Write
character string to user CHR_FILL : Fill character variable with one
character


