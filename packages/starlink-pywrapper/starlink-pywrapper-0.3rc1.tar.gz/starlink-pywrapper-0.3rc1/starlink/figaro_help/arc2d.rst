

ARC2D
=====


Purpose
~~~~~~~
Wavelength calibration


Description
~~~~~~~~~~~
This program controls both 1D and 2D wavlength calibration and can
operate either in BATCH or INTERACTIVE modes. The philosophy behind it
is somewhat different to those presented in the existing SPICA/SDRSYS
and FIGARO software in many respects. In particular its exclusive use
of gausian fitting of arclines, its demand for "intellegent" users,
who can decide which lines they want to use initially and then allow
them to make objective assesments of which,if any are erroneous.
Typical diagnostic information given are plots of residuals from the
fit versus line width,flux and position. This is all made possible by
the use of the Gaussian fitting. The least squares polynomial fitting
allows weights to be included for each line(again derived from the
formal Gaussian fits).Thus it is possible to constrain the polynomial
in difficult regions eg "the 5100 gap" without distorting the global
fit.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) Name of image for input This should be a file
containing an arc spectrum. ARC_OPTS = CHARACTER (Read) Enter arc fit
option NEW : set up a new wavelength calibration REPEAT : Itterate on
previous calibration CLONE : CLone a previous calibration YSTART =
INTEGER (Read) analysis lower limit The data between the limits ystart
and yend is extracted and the resultant spectrum is used to locate the
lines. YEND = INTEGER (Read) analysis upper limit The data between the
limits ystart and yend is extracted and the resultant spectrum is used
to locate the lines. YBLOCK = INTEGER (Read) Enter analysis x-sect
width Each window is of this width (except perhaphs the final one).
ITERATION = INTEGER*2 (Read) New value of iteration ORDER = INTEGER
(Read) order for polynomial fitting This is for the continuity
correction of the data. Idealy the arc should have been pre-processed
with ARCSDI, so a low order e.g. 2 should be used. MAXLINES = INTEGER
(Read) Maximum number of lines to allow room for This must be greater
than or equal to the number of lines fitted, so room should be allowed
in case any more are to be added later. CLFILE = FILE (Read) Name of
image for cloning from This should be a file containing an arc
spectrum. TOLS = CHARACTER (Read) For use in batch only KEEP_ITT =
LOGICAL (Read) keep itteration files' PRFITS = LOGICAL (Read) Print
out details of fitting


Files
~~~~~
NAME PURPOSE (image).IAR Stores polynomial coefficients, for use by
ISCRUNCH. IMAGE The arc data. This should be a FIGARO data file with a
data array. If there is a data array for the first axis the
information it contains will be used during the program.


Subroutines/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
APPLY_TOLS : Apply tolerances ARCFIT : this does the actual fitting of
polynomials in the channel direction (wavelength as a function of
channel number). Either the line positions or the positions
interpolated by control_cpoly_w may be used. ARC_WINDOW : Find line
centres by fitting Gaussians CLGRAP : Close graphics CNF_PVAL : Full
pointer to dynamically allocated memory CONTIN_CORR : this fits
polynomials in the x-sect direction (i.e. along the lines), so as to
remove discontinuities due to noise. It then set the results from this
into the .RES.DATA structure for use by arcfit. GET_LINE_IDS : This
obtains the line ids etc., if in new or clone mode. Otherwise it
simply maps the data file with some checking. TWO_OPEN : Open input
file and get its dimensions etc. DSA_GET_WORK_ARRAY : Get virtual
memory IROUTP : this outputs the results of the fitting by arcfit to a
file for use by ISCRUNCH, and also a summary to the terminal. This was
copied from the FIGARO IARC program. LOOK : Output values of main
results array UNMAP_RES : Unmap results structure
DSA_FREE_WORKSPACE : Free workspace DSA_CLOSE : Close DSA system
PAR_QUEST : Obtain YES/NO response from user PAR_WRUSER : Write
character string to user


