

LONGSLIT
========


Purpose
~~~~~~~
Longslit rotation curve and line profile analysis


Description
~~~~~~~~~~~
LONGSLIT can fit Gaussians, skew Gaussians, Lorentzians and Cauchy
functions to line profiles, and can carry out line profile analysis to
produce the Whittle and Heckman asymmetry parameters. Much of this can
be carried out in batch mode. This program generates rotation curves
from 2D data, for a number of emission/absorption lines. Options are
available to automatically fit each line in the spectrum or to do it
in an interactive manner allowing unsatisfactory fits to be rejected.
Unsatisfactory fits may then be refitted on a second pass. For each
line a table is created containing all the fit parameters as a
function of crossection.If the data has been block averaged in an
range of XSECTS the average XSECT value and the XSECT range are
computed and stored. In manual mode the user can sweep through the
XSECTS choosing different BLOCKINGS and line types repeatedly until he
either accepts the fit or issues an instruction not to fit a given
range of XSECTS. Continuum Fitting is provided in two ways. Firstly a
GLOBAL continuum may be defined for each block of data. This is a
continuum which is fitted to all regions of the spectrum which do NOT
contain lines. A variety of models are available. Chebyshev
Polynomials, Splines, (Power Law, Black Body, Black Body with optical
depth cuttoff, Empirical, and Balmer Continuum). Secondly, A local
continuum may be applied to each INDIVIDUAL line. This continuum is
applied in addition to that created by GLOBAL but is confined to the
regions of the spectra containing a particular line. Because most of
the allowed line options also fit a FLAT base the combination of these
fits can be made to match even the most complex continua The types of
allowed continuum models for INDIVIDUAL is restricted to Spline, Flat
or Chebyshev. It is possible to Edit the results cube created by
LONGSLIT and to create new Synthetic spectra by doing model -data
manipulations or from the models themselves. During this process
several usefull things can be done to the output spectra, notably
changing their Redshift, applying or removing Reddening. A similar
approach creating Sky subracted data and using sky lines for
correcting for instrumental vignetting is also possible. Rotation
curves in individual lines are produced as requested in the PLOT mode.
In addition it is possible to calculate a mean rotation curve. In the
current release the user now has complete control over the plotting
parameters and the lines being plotted.


Subroutines/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ACCRES : Access results structure APPLY_TOLS : Apply tolerances
CHECK_CONTROL : Check whether to perform "normal" and/or "transfer"
fits CLGRAP : Close graphics CNF_PVAL : Full pointer to dynamically
allocated memory DATA_WINDOW : controls the fitting process -
automatic FLAVOURS : Produce output plots, tables etc. GET_LINE_IDS :
This opens the file, obtains the line ids etc., if in new or clone
mode. Otherwise it simply maps the data file with some checking.
LONG_OPTS : This selects the option required by the user (interactive
use only) MANUAL_MODE : controls the fitting process - manual NEW_ANAL
: Set up a new analysis-define fits REDO_ALL_FITS : Refit a data cube
using previous results SETUP_ARC : Locate and identify lines LOOK :
Output values of main results array TRANSFER : Perform fitting using
previous results from different lines UNMAP_RES : Unmap results
structure
DSA_CLOSE : Close DSA system PAR_RDKEY : Read key parameter PAR_RDVAL
: Read numeric parameter from user PAR_WRUSER : Write character string
to user


Parameters:
~~~~~~~~~~~
IMAGE = FILE (Read) Name of image for input This is the data. This
should be a .dst file with a .Z.DATA component. This should also have
a .X.DATA array which contains the wavelengths of the lines. For the
identification files supplied with the program the units should be
Angstroms, but if the user supplies his/her own files, this need not
apply, although some plots may have the wrong labels. ARC_OPTS =
CHARACTER (Read) Enter fit option NEW : set up a new analysis REPEAT :
iterate on previous analysis CLONE : Clone an analysis from another
file (line locations etc.) YSTART = INTEGER (Read) analysis lower
limit YEND = INTEGER (Read) analysis upper limit YBLOCK = INTEGER
(Read) Enter analysis x-sect width ITERATION = INTEGER*2 (Read) New
value of iteration MAXLINES = INTEGER (Read) Maximum number of lines
to allow room for CLFILE = FILE (Read) Name of image for cloning from
OUTABLE = FILE (Write) Name for extactic file VCORR = REAL (Read)
correction to apply to radial velocities TOLS = CHARACTER (Read) For
use in batch only INHERIT = INTEGER (Read) Number to control
inheritance of previous fits If zero no inheritance of fits If one
then inherited from next block If minus one then inherited from
previous block DEVICE = CHARACTER (Read) Device to use for greyscale
plots FITRAT = REAL (Read) Ratio for double fitting (of widths/heights
or separation) CALRAT = INTEGER (Read) Ratio to multiply default
number of iterations in Nag optimisation WHITE = REAL (Read) White
level for greyscale plots BLACK = REAL (Read) Black level for
greyscale plots MAXGAUSS = INTEGER (Read) Maximum number of Gaussians
to allow room for LONGSLIT can fit up to 9 component fits, but the
results array for such is quite large. This allows the user to set the
maximum number of components he/she is likely to fit, since very
little data requires 9 components! TSTART = REAL (Read) analysis lower
limit TEND = REAL (Read) analysis upper limit TBLOCK = REAL (Read)
Analysis blocking width in T direction FIT_MODEL = CHARACTER (Read)
Model of fit to perform PLOTLIM(4) = REAL ARRAY (Read) Limits for
velocity plots OUTPUT = FILE (Write) Name of output file HARDCOPY =
LOGICAL (Read) produce hardcopy plots of fits from cube TABLE =
LOGICAL (Read) produce table of fits from cube PLOT = LOGICAL (Read)
produce plots of rotation curves PRINT = LOGICAL (Read) produce print
out of rotation curves SHAPE = LOGICAL (Read) carry out shape analysis
KEEP_ITT = LOGICAL (Read) keep iteration files FIT = LOGICAL (Read)
perform fitting COPY = LOGICAL (Read) copy previous fits This will
repeat all the fits previously made, which is likely to be of use if
data is co-added after one file has been analysed. Also, when used
with CLONE the entire .RES structure is copied without any change. For
the new fits the previous fits (suitably scaled) are used as first
guesses. ABSORPTION = LOGICAL (Read) Allow fitting of absorption lines
BOUNDS = LOGICAL (Read) Perform bounded fits to lines (in batch) LABEL
= LOGICAL (Read) Put labels on plots CONTOUR = LOGICAL (Read) Create
contour plots GREY = LOGICAL (Read) Create greyscale plots LOG =
LOGICAL (Read) Use logarithmic scale for CONTOUR and GREY WEIGHTS =
LOGICAL (Read) Use weights for fitting PRFITS = LOGICAL (Read) Print
out details of fitting FULL = LOGICAL (Read) Print out full details of
fits in table CHECK = LOGICAL (Read) Plot array of line profiles


