

COMB
====


Purpose
~~~~~~~
Allow correction of 2-d spectra for S-distortion using a comb


Description
~~~~~~~~~~~
This is a program to correct data for s-distortion by moving data in
the cross-section direction to line it up for a comb of continua
spectra.This correction is then applied to the data itself. A comb
dekker is used to produce about ten continuum spectra across an image
(this is done at the telescope). This image is then used by the
program:- The program requests two adjacent "teeth" to be marked, it
locates the remaining teeth and follows them along the image (in the
channel direction), finding the line centres by fitting gaussians. The
points so obtained are fitted with Chebyshev polynomials (for each
tooth), The intermediate positions are interpolated from these, which
are then used to evaluate the required movement for each data point.
The coefficients are written to a file which may then be read by the
program to apply correction to the actual data. Alternatively if QUICK
is specified, centroids are used rather than Gaussians.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) Name of image for input This should be a file
containing continua spectra. ARC_OPTS = CHARACTER (Read) Enter arc fit
option NEW : set up a new wavelength calibration REPEAT : Itterate on
previous calibration. CLONE : CLone a previous calibration. OLD :
Correct using previous results OUTPUT = FILE (Write) Name of output
file File to contain corrected data. XSTART = INTEGER (Read) analysis
lower limit The data between the limits xstart and xend is extracted
and the resultant spectrum is used to locate the lines. XEND = INTEGER
(Read) analysis upper limit The data between the limits xstart and
xend is extracted and the resultant spectrum is used to locate the
lines. XBLOCK = INTEGER (Read) Enter averaging width in channels Each
window is of this width (except perhaphs the final one). ITERATION =
INTEGER*2 (Read) New value of iteration LEVEL = REAL (Read) Level of
edge of tooth ORDER = INTEGER (Read) order for polynomial fitting This
is for the continuity correction of the data. Idealy the arc should
have been pre-processed with ARCSDI, so a low order e.g. 2 should be
used. MAXLINES = INTEGER (Read) Maximum number of lines to allow room
for This must be greater than or equal to the number of lines fitted,
so room should be allowed in case any more are to be added later.
CLFILE = FILE (Read) Name of image for cloning from This should be a
file containing an arc spectrum. TOLS = CHARACTER (Read) For use in
batch only KEEP_ITT = LOGICAL (Read) keep itteration files? QUICK =
LOGICAL (Read) Centriod rather than fit gaussians? PRFITS = LOGICAL
(Read) Print out details of fitting PLOTCORR = LOGICAL (Read) Plot
correction?


Subroutines/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
APPLY : Apply correction APPLY_TOLS : Apply tolerances AUTO : Fit
Gaussian to (or find centroids of) continua CLGRAP : Close graphics
CLONE_MODE : CLONE continuum locations etc. from another file CNF_PVAL
: Full pointer to dynamically allocated memory COMB_MENU : Main menu
COMB_CONTIN : Fit polynomials to continua centres found by AUTO
GR_SELCT : Open graphics device ARCSDI_INIT : Open input file etc.
INIT_RES : Initialise results structure MAP_DATA : Map data MAP_RES :
Map results structure NEW_ARC : Create results structure NEW_COMB :
Locate continua QMENU : Get menu response from user REFINE_RES : Check
results structure exists, and get size SETUP_ARC2 : Locate continua
LOOK : Output values of main results array UNMAP_RES : Unmap results
structure
DSA_AXIS_RANGE : Get axis limits DSA_FREE_WORKSPACE : Free workspace
DSA_GET_WORK_ARRAY : Get workspace DSA_OPEN_TEXT_FILE : Open text file
DSA_OUTPUT : Create output file DSA_MAP_DATA : Map main data array
DSA_CLOSE : Close DSA system FIG_YTRACT : Take slice thru' data in Y
direction PAR_RDKEY : Read key parameter PAR_RDCHAR : Read character
parameter PAR_WRUSER : Write character string to user
CHR_FILL : Fill character variable with one character


