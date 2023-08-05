

FINDCLUMPS
==========


Purpose
~~~~~~~
Identify clumps of emission within a 1, 2 or 3 dimensional NDF


Description
~~~~~~~~~~~
This application identifies clumps of emission within a 1, 2 or 3
dimensional NDF. It is assumed that any background has already been
removed from the data array (for instance, using CUPID:FINDBACK).
Information about the clumps is returned in several different ways:


+ A pixel mask identifying pixels as background, clump or edge pixels
is written to the Quality array of each output NDF (see parameters OUT
and QOUT). Three quality bits will be used; one is set if and only if
the pixel is contained within one or more clumps, another is set if
and only if the pixel is not contained within any clump, and the other
is set if and only if the pixel is in a clump but on the edge of the
clump (i.e. has one or more neighbouring pixels that are not inside a
clump). These three quality bits have names associated with them which
can be used with the KAPPA applications SETQUAL, QUALTOBAD, REMQUAL,
SHOWQUAL. The names used are "CLUMP", "BACKGROUND" and "EDGE". For
instance, to overlay the outline of a set of 2D clumps held in NDF
"fred" on a previously displayed 2D image, do "qualtobad fred fred2
background" followed by "contour noclear mode=good fred2".
+ Information about each clump, including a minimal cut-out image of
the clump and the clump parameters, is written to the CUPID extension
of the output NDF (see the section "Use of CUPID Extension" below).
+ An output catalogue containing clump parameters can be created (see
  parameter OUTCAT).

The algorithm used to identify the clumps (GaussCLumps, ClumpFind,
etc) can be specified (see parameter METHOD).


Usage
~~~~~


::

    
       findclumps in out outcat method
       



ADAM parameters
~~~~~~~~~~~~~~~



BACKOFF = _LOGICAL (Read)
`````````````````````````
If TRUE, the background level in each clump is removed from the clump
data values before calculating the reported clump sizes and centroid
position (the background level used is the minimum data value in the
clump). If FALSE, the full data values, including background, are used
when calculating the clump sizes and centroid position.
If BACKOFF is FALSE, a clump that sits on a high background level will
have a larger reported width than an identical clump sitting on a
lower background level. The position of the centroid may also be
affected by the background level. This is usually undesirable, and so
the default value for BACKOFF is usually TRUE. The main reason you may
want to set BACKOFF to FALSE is if you want to compare clump
properties found by FINDCLUMPS with those found by the IDL version of
CLUMPFIND (which includes the background in its calculations). For
this reason, the dynamic default value got BACKOFF is TRUE, unless
METHOD is "ClumpFind" and the ClumpFind.IDLAlg configuration parameter
is non-zero, in which case the dynamic default for BACKOFF is FALSE.
Note, the other reported clump properties such as total data value,
peak data value, etc, are always based on the full clump data values,
including background. []



CONFIG = GROUP (Read)
`````````````````````
Specifies values for the configuration parameters used by the clump
finding algorithms. If the string "def" (case-insensitive) or a null
(!) value is supplied, a set of default configuration parameter values
will be used.
The supplied value should be either a comma-separated list of strings
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated list of strings. Each string is
either a "keyword=value" setting, or the name of a text file preceded
by an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner (any blank lines or lines beginning with "#" are ignored).
Within a text file, newlines can be used as delimiters as well as
commas. Settings are applied in the order in which they occur within
the list, with later settings over-riding any earlier settings given
for the same keyword.
Each individual setting should be of the form:
<keyword>=<value>
where <keyword> has the form "algorithm.param"; that is, the name of
the algorithm, followed by a dot, followed by the name of the
parameter to be set. If the algorithm name is omitted, the current
algorithm given by parameter METHOD is assumed. The parameters
available for each algorithm are listed in the "Configuration
Parameters" sections below. Default values will be used for any
unspecified parameters. Assigning the value "<def>" (case insensitive)
to a keyword has the effect of reseting it to its default value.
Unrecognised options are ignored (that is, no error is reported).
[current value]



DECONV = _LOGICAL (Read)
````````````````````````
Determines if the clump properties stored in the output catalogue and
NDF extension should be corrected to remove the effect of the
instrumental beam width specified by the FwhmBeam and VeloRes
configuration parameters. If TRUE, the clump sizes will be reduced and
the peak values increased to take account of the smoothing introduced
by the beam width. If FALSE, the undeconvolved values are stored in
the output catalogue and NDF. Note, the filter to remove clumps
smaller than the beam width is still applied, even if DECONV is FALSE.
[TRUE]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Controls the amount of diagnostic information reported. It uses the
standard message filtering system. It should be in the range 0 to 6
(NONE, QUIET, NORM, VERB, DEBUG, DEBUG1-3). A value of NONE (zero)
will suppress all screen output. Larger values give more information
(the precise information displayed depends on the algorithm being
used). Note, this screen output describes the progress of the specific
clump finding algorithm selected using the METHOD parameter, and
therefore clump parameters such as clump size, etc, will be displayed
using the definition most natural to the chosen algorithm. These
definitions may not be the same as those used to create the output
catalogue, since the output catalogue contains standardised columns
chosen to allow comparison between different algorithms. For instance,
the clump sizes displayed on the screen by the GaussClumps algorithm
will be FWHM in pixels, but the clump sizes stored in the output
catalogue are the RMS deviation of each pixel centre from the clump
centroid, weighted by the corresponding pixel data value. [NORM]



IN = NDF (Read)
```````````````
The 1, 2 or 3 dimensional NDF to be analysed.



JSACAT = NDF (Read)
```````````````````
An optional JSA-style output catalogue in which to store the clump
parameters (for KAPPA-style catalogues see parameter "OUTCAT"). No
catalogue will be produced if a null (!) value is supplied. The
created file will be a FITS file containing a binary table. The
columns in this catalogue will be the same as those created by the
"OUTCAT" parameter, but the table will in also hold the contents of
the FITS extension of the input NDF, and CADC-style provenance
headers. Note, an error will be reported if the current co-ordinate
system of the input NDF does not include a pair of celestial longitude
and latitude axes. The default for parameter SHAPE is changed to
"Polygon" if a JSA-style catalogue is being created. [!]



LOGFILE = LITERAL (Read)
````````````````````````
The name of a text log file to create. If a null (!) value is
supplied, no log file is created. [!]



METHOD = LITERAL (Read)
```````````````````````
The algorithm to use. Each algorithm is described in more detail in
the "Algorithms:" section below. Can be one of:


+ GaussClumps
+ ClumpFind
+ Reinhold
+ FellWalker

Each algorithm has a collection of extra tuning values which are set
via the CONFIG parameter. [current value]



NCLUMPS = _INTEGER (Write)
``````````````````````````
The total number of clumps descrriptions stored within the output NDF
(and catalogue).



OUT = NDF (Write)
`````````````````
The output NDF which has the same shape and size as the input NDF.
Information about the identified clumps and the configuration
parameters used will be stored in the CUPID extension of this NDF. See
"Use of CUPID Extension" below for further details about the
information stored in the CUPID extension. Other applications within
the CUPID package can be used to display this information in various
ways. The information written to the DATA array of this NDF depends on
the value of the METHOD parameter. If METHOD is GaussClumps, the
output NDF receives the sum of all the fitted Gaussian clump models
including a global background level chosen to make the mean output
value equal to the mean input value. If METHOD is ClumpFind,
FellWalker or Reinhold, each pixel in the output is the integer index
of the clump to which the pixel has been assigned. Bad values are
stored for pixels which are not part of any clump. The output NDF will
inherit the AXIS and WCS components (plus any extensions) from the
input NDF.



OUTCAT = FILENAME (Write)
`````````````````````````
An optional KAPPA-style output catalogue in which to store the clump
parameters (for JSA-style catalogues see parameter "JSACAT"). No
catalogue will be produced if a null (!) value is supplied. The
following columns are included in the output catalogue:


+ Peak1: The position of the clump peak value on axis 1.
+ Peak2: The position of the clump peak value on axis 2.
+ Peak3: The position of the clump peak value on axis 3.
+ Cen1: The position of the clump centroid on axis 1.
+ Cen2: The position of the clump centroid on axis 2.
+ Cen3: The position of the clump centroid on axis 3.
+ Size1: The size of the clump along pixel axis 1.
+ Size2: The size of the clump along pixel axis 2.
+ Size3: The size of the clump along pixel axis 3.
+ Sum: The total data sum in the clump.
+ Peak: The peak value in the clump.
+ Volume: The total number of pixels falling within the clump.

There is also an optional column called "Shape" containing an STC-S
description of the spatial coverage of each clump. See parameter
SHAPE.
The coordinate system used to describe the peak and centroid positions
is determined by the value supplied for parameter WCSPAR. If WCSPAR is
FALSE, then positions are specified in the pixel coordinate system of
the input NDF. In addition, the clump sizes are specified in units of
pixels, and the clump volume is specified in units of cubic pixels
(square pixels for 2D data). If WCSPAR is TRUE, then positions are
specified in the current coordinate system of the input NDF. In
addition, the clump sizes and volumes are specified in WCS units.
Note, the sizes are still measured parallel to the pixel axes, but are
recorded in WCS units rather than pixel units. Celestial coordinate
positions are units of degrees, sizes are in units are arc-seconds,
and areas in square arc-seconds. Spectral coordinates are in the units
displayed by the KAPPA command "ndftrace".
If the data has less than 3 pixel axes, then the columns describing
the missing axes will not be present in the catalogue.
The catalogue inherits any WCS information from the input NDF.
The "size" of the clump on an axis is the RMS deviation of each pixel
centre from the clump centroid, where each pixel is weighted by the
corresponding pixel data value. For a Gaussian profile, this "size"
value is equal to the standard deviation of the Gaussian. Optionally,
the weights can be be based on the pixel data value after removal of
the background - see parameter BACKOFF). If parameter DECONV is set
TRUE, the values stored for "Size..." and "Peak" are corrected to take
account of the smoothing introduced by the instrumental beam. These
corrections reduced the "size..." values and increase the peak value.
Beam sizes are specified by configuration parameters FWHMBeam and
VeloRes.
For the GaussClump algorithm, the Sum and Volume values refer to the
part of the Gaussian within the level defined by the
GaussClump.ModelLim configuration parameter.
The values used for configuration parameters and ADAM parameters are
written to the history information of the output catalogue.
The KAPPA command "listshow" can be used to draw markers at the
central positions of the clumps described in a catalogue. For
instance, the command "listshow fred plot=mark" will draw markers
identifying the positions of the clumps described in file fred.FIT,
overlaying the markers on top of the currently displayed image.
Specifying "plot=STCS" instead of "plot=mark" will cause the spatial
outline of the clump to be drawn if it is present in the catalogue
(see parameter SHAPE). [!]



PERSPECTRUM = _LOGICAL (Read)
`````````````````````````````
This parameter is ignored unless the supplied input NDF is
3-dimensional and includes a spectral axis. If so, then a TRUE value
for PERSPECTRUM will cause all spectra within the supplied cube to be
processed independenly of the neighbouring spectra. That is, each
identified clump will contain pixels from only a single input
spectrum. If a clump extends across multiple spectra, then it will be
split up into multiple clumps, one for each spectrum. Currently, this
parameter can only be used with the FellWalker and ClumpFind methods.
A value of FALSE is always used for other methods. [FALSE]



QOUT = NDF (Write)
``````````````````
An optional output NDF that is a copy of the input NDF, except that
any Quality component in the input NDF is discarded and a new one
created. The new Quality component defines 3 flags that indicate if
each pixel is inside a clump, on the edge of a clump or outside all
clumps. If a null (!) value is supplied, no NDF is created. [!]



REPCONF = _LOGICAL (Read)
`````````````````````````
If a TRUE value is supplied, then the configuration parameters
supplied by the CONFIG parameter will be listed to standard output.
[current value]



RMS = _DOUBLE (Read)
````````````````````
Specifies a value to use as the global RMS noise level in the supplied
data array. The suggested default value is the square root of the mean
of the values in the input NDF's Variance component. If the NDF has no
Variance component, the suggested default is based on the differences
between neighbouring pixel values. Any pixel-to-pixel correlation in
the noise can result in this estimate being too low. The value
supplied for this parameter will be ignored if the RMS noise level is
also given in the configuration file specified by parameter CONFIG.



SHAPE = LITERAL (Read)
``````````````````````
Specifies the shape that should be used to describe the spatial
coverage of each clump in the output catalogue. It can be set to
"None", "Polygon" or "Ellipse". If it is set to "None", the spatial
shape of each clump is not recorded in the output catalogue.
Otherwise, the catalogue will have an extra column named "Shape"
holding an STC-S description of the spatial coverage of each clump.
"STC-S" is a textual format developed by the IVOA for describing
regions within a WCS - see
http://www.ivoa.net/Documents/latest/STC-S.html for details. These
STC-S desriptions can be displayed by the KAPPA:LISTSHOW command, or
using GAIA. Since STC-S cannot describe regions within a pixel array,
it is necessary to set parameter WCSPAR to TRUE if using this option.
An error will be reported if WCSPAR is FALSE. An error will also be
reported if the WCS in the input data does not contain a pair of
scelestial sky axes.


+ Polygon: Each polygon will have, at most, 15 vertices. If the data
is 2-dimensional, the polygon is a fit to the clump's outer boundary
(the region containing all godo data values). If the data is
3-dimensional, the spatial footprint of each clump is determined by
rejecting the least significant 10% of spatial pixels, where
"significance" is measured by the number of spectral channels that
contribute to the spatial pixel. The polygon is then a fit to the
outer boundary of the remaining spatial pixels.
+ Ellipse: All data values in the clump are projected onto the spatial
plane and "size" of the collapsed clump at four different position
angles - all separated by 45 degrees - is found (see the OUTCAT
parameter for a description of clump "size"). The ellipse that
generates the closest sizes at the four position angles is then found
and used as the clump shape.
+ Ellipse2: The above method for determining ellipses works well for
  clumps that are in fact elliptical, but can generate extremely long
  thin ellipses for clumps are far from being ellitical. The "Ellipse2"
  option uses a different method for determining the best ellipse based
  on finding many marginal profiles at one degree intervals of azimuth,
  and using the longest marginal profile as the major axis.

In general, ellipses will outline the brighter, inner regions of each
clump, and polygons will include the fainter outer regions. The
dynamic default is "Polygon" if a JSA-style catalogue (see parameters
JSACAT) is being created, and "None" otherwise. Note, if a JSA-style
catalogue is being created an error will be reported if "Ellipse",
"Ellipse2" or "None" is selected. []



WCSPAR = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, then the clump parameters stored in the
output catalogue and in the CUPID extension of the output NDF, are
stored in WCS units, as defined by the current coordinate frame in the
WCS component of the input NDF (this can be inspected using the
KAPPA:WCSFRAME command). For instance, if the current coordinate
system in the 3D input NDF is (RA,Dec,freq), then the catalogue
columns that hold the clump peak and centroid positions will use this
same coordinate system. The spatial clump sizes will be stored in arc-
seconds, and the spectral clump size will be stored in the unit of
frequency used by the NDF (Hz, GHz, etc). If a FALSE value is supplied
for this parameter, the clump parameters are stored in units of pixels
within the pixel coordinate system of the input NDF. The dynamic
default for this parameter is TRUE if the current coordinate system in
the input NDF represents celestial longitude and latitude in some
system, plus a recogonised spectral axis (if the input NDF is 3D).
Otherwise, the dynamic default is FALSE. Note, an error will be
reported if a JSA-style catalogue is being created (see parameter
JSACAT) and WCSPAR is set to FALSE. []



Synopsis
~~~~~~~~
void findclumps( int *status );


Use of CUPID Extension
~~~~~~~~~~~~~~~~~~~~~~
This application will create an NDF extension called "CUPID" in the
output NDF and will add the following components to it:


+ CLUMPS: This a an array of CLUMP structures, one for each clump
  identified by the selected algorithm. Each such structure contains the
  same clump parameters that are written to the catalogue via parameter
  OUTCAT. It also contains a component called MODEL which is an NDF
  containing a section of the main input NDF which is just large enough
  to encompass the clump. Any pixels within this section which are not
  contained within the clump are set bad. So for instance, if the input
  array "fred.sdf" is 2-dimensional, and an image of it has been
  displayed using KAPPA:DISPLAY, then the outline of clump number 9
  (say) in the output image "fred2.sdf" can be overlayed on the image by
  doing:

contour noclear "fred2.more.cupid.clumps(9).model" mode=good labpos=\!


+ CONFIG: Lists the algorithm configuration parameters used to
identify the clumps (see parameter CONFIG).
+ QUALITY_NAMES: Defines the textual names used to identify background
  and clump pixels within the Quality mask.




Algorithms
~~~~~~~~~~


+ GaussClumps: Based on the algorithm described by Stutski & Gusten
(1990, ApJ 356, 513). This algorithm proceeds by fitting a Gaussian
profile to the brightest peak in the data. It then subtracts the fit
from the data and iterates, fitting a new ellipse to the brightest
peak in the residuals. This continues until the integrated data sum in
the fitted Gaussians reaches the integrated data sum in the input
array, or a series of consecutive fits are made which have peak values
below a given multiple of the noise level. Each fitted ellipse is
taken to be a single clump and is added to the output catalogue. In
this algorithm, clumps may overlap. Any input variance component is
used to scale the weight associated with each pixel value when
performing the Gaussian fit. The most significant configuration
parameters for this algorithm are: GaussClumps.FwhmBeam and
GaussClumps.VeloRes which determine the minimum clump size.
+ ClumpFind: Described by Williams et al (1994, ApJ 428, 693). This
algorithm works by first contouring the data at a multiple of the
noise, then searches for peaks of emission which locate the clumps,
and then follows them down to lower intensities. No a priori clump
profile is assumed. In this algorithm, clumps never overlap. Clumps
which touch an edge of the data array are not included in the final
list of clumps.
+ Reinhold: Based on an algorithm developed by Kim Reinhold at JAC.
See SUN/255 for more information on this algorithm. The edges of the
clumps are first found by searching for peaks within a set of 1D
profiles running through the data, and then following the wings of
each peak down to the noise level or to a local minimum. A mask is
thus produced in which the edges of the clumps are marked. These edges
however tend to be quite noisy, and so need to be cleaned up before
further use. This is done using a pair of cellular automata which
first dilate the edge regions and then erode them. The volume between
the edges are then filled with an index value associated with the peak
position. Another cellular automata is used to removed noise from the
filled clumps.
+ FellWalker: Based on an algorithm which walks up hill along the line
  of greatest gradient until a significant peak is reached. It then
  assigns all pixels visited along the route to the clump associated
  with the peak. Such a walk is performed for every pixel in the data
  array which is above a specified background level. See SUN/255 for
  more information on this algorithm.




GaussClumps Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GaussClumps.ExtraCols: If set to a positive integer, then extra
method-specific columns are added to the output catalogue. If set to
1, then the catalogue will include columns with names GCFWHM<i> (where
<i> is 1, 2, or 3), holding the FWHM of the fitted Gaussian in units
of pixels (these FWHM values have NOT been reduced to excluded the
effect of the beam width), and "GCANGLE" - the spatial orientation
angle (in degrees, positive from +ve GRID1 axis to +ve GRID2 axis). If
set greater than 1, then additional columns will be included holding
the initial estimates for the peak and background values, the number
of fitting iterations used and the final ch-squared value for the fit.
GaussClumps.FwhmBeam: The FWHM of the instrument beam, in pixels. The
fitted Gaussians are not allowed to be smaller than the instrument
beam. This prevents noise spikes being fitted. In addition, if
application paremeter DECONV is set TRUE, the clump widths written to
the output catalogue are reduced (in quadrature) by this amount. [2.0]
GaussClumps.FwhmStart: An initial guess at the ratio of the typical
observed clump size to the instrument beam width. This is used to
determine the starting point for the algorithm which finds the best
fitting Gaussian for each clump. If no value is supplied (or if
FwhmBeam is zero), the initial guess at the clump size is based on the
local profile around the pixel with peak value. [] GaussClumps.MaxBad:
The maximum fraction of bad pixels which may be included in a clump.
Clumps will be excluded if they contain more bad pixels than this
value [0.05] GaussClumps.MaxClumps: Specifies a termination criterion
for the GaussClumps algorithm. The algorithm will terminate when
"MaxClumps" clumps have been identified, or when one of the other
termination criteria is met. [unlimited] GaussClumps.MaxNF: The
maximum number of evaluations of the objective function allowed when
fitting an individual clump. Here, the objective function evaluates
the chi-squared between the current gaussian model and the data being
fitted. [100] GaussClumps.MaxSkip: The maximum number of consecutive
failures which are allowed when fitting Guassians. If more than
"MaxSkip" consecutive clumps cannot be fitted, the iterative fitting
process is terminated. [10] GaussClumps.ModelLim: Determines the value
at which each Gaussian model is truncated to zero. Model values below
ModelLim times the RMS noise are treated as zero. [0.5]
GaussClumps.NPad: Specifies a termination criterion for the
GaussClumps algorithm. The algorithm will terminate when "Npad"
consecutive clumps have been fitted all of which have peak values less
than the threshold value specified by the "Thresh" parameter, or when
one of the other termination criteria is met. [10] GaussClumps.RMS:
The global RMS noise level in the data. The default value is the value
supplied for parameter RMS. [] GaussClumps.S0: The Chi-square
stiffness parameter "S0" which encourages the fitted gaussian value to
be below the corresponding value in the observed data at every point
(see the Stutski & Gusten paper). [1.0] GaussClumps.Sa: The Chi-square
stiffness parameter "Sa" which encourages the peak amplitude of each
fitted gaussian to be close to the corresponding maximum value in the
observed data (see the Stutski & Gusten paper). [1.0] GaussClumps.Sb:
An additional Chi-square stiffness parameter which encourages the
background value to stay close to its initial value. This stiffness is
not present in the Stutzki & Gusten paper but is added because the
background value is usually determined by data points which have very
low weight and is thus poorly constrained. It would thus be possibly
to get erroneous background values without this extra stiffness. [0.1]
GaussClumps.Sc: The Chi-square stiffness parameter "Sc" which
encourages the peak position of each fitted gaussian to be close to
the corresponding peak position in the observed data (see the Stutski
& Gusten paper). [1.0] GaussClumps.Thresh: Gives the minimum peak
amplitude of clumps to be fitted by the GaussClumps algorithm (see
also GaussClumps.NPad). The supplied value is multipled by the RMS
noise level before being used. [2.0] GaussClumps.VeloRes: The velocity
resolution of the instrument, in channels. The velocity FWHM of each
clump is not allowed to be smaller than this value. Only used for 3D
data. In addition, the velocity width of each clump written to the
output catalogue is reduced (in quadrature) by this amount. [2.0]
GaussClumps.VeloStart: An initial guess at the ratio of the typical
observed clump velocity width to the velocity resolution. This is used
to determine the starting point for the algorithm which finds the best
fitting Gaussian for each clump. If no value is supplied (or if
VeloRes is zero), the initial guess at the clump velocity width is
based on the local profile around the pixel with peak value. Only used
for 3D data. [] GaussClumps.Wmin: This parameter, together with
GaussClumps.Wwidth, determines which input data values are used when
fitting a Gaussian to a given peak in the data array. It specifies the
minimum normalised weight which is to be used. Pixels with normalised
weight smaller than this value are not included in the fitting
process. The absolute weight values are normalised by dividing them by
a value equal to the mean of the absolute weights plus four standard
deviations. An iterative sigma clipping algorithm is used when
calculating this value in order to eliminate the effects of any pixel
that have unusually low variance values, and thus unusually high
absolute weights. [0.05] GaussClumps.Wwidth: This parameter, together
with GaussClumps.Wmin, determines which input data values are used
when fitting a Gaussian to a given peak in the data array. It is the
ratio of the width of the Gaussian weighting function (used to weight
the data around each clump during the fitting process), to the width
of the initial guess Guassian used as the starting point for the
Gaussian fitting process. The Gaussian weighting function has the same
centre as the initial guess Gaussian. [2.0]


ClumpFind Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ClumpFind.AllowEdge: If set to a zero value, then clumps are rejected
if they touch any edge of the data array. If non-zero, then such
clumps are retained. Note, other implementations of ClumpFind often
include such clumps but flag them in some way. [0] ClumpFind.DeltaT:
The gap between the contour levels. Only accessed if no value is
supplied for "Level1", in which case the contour levels are linearly
spaced, starting at a lowest level given by "Tlow" and spaced by
"DeltaT". Note, small values of DeltaT can result in noise spikes
being interpreted as real peaks, whilst large values can result in
some real peaks being missed and merged in with neighbouring peaks.
The default value of two times the RMS noise level is usually
considered to be optimal, although this obviously depends on the RMS
noise level being correct. The value can be supplied either as an
absolute data value, or as a multiple of the RMS noise using the
syntax "[x]*RMS", where "[x]" is a numerical value (e.g. "3.2*RMS").
[2*RMS] ClumpFind.FwhmBeam: The FWHM of the instrument beam, in
pixels. If application paremeter DECONV is set TRUE, the clump widths
written to the output catalogue are reduced (in quadrature) by this
amount. If a direct comparison with other implementations of the
ClumpFind algorithm is required, DECONV should be set to FALSE. [2.0]
ClumpFind.IDLAlg: If a non-zero value is supplied, then FINDCLUMPS
emulates the ClumpFind algorithm as implemented by the IDL package
available from Jonathan Williams WWW site on 28th April 2006. The
default value of zero causes FINDCLUMPS to use the algorithm described
in the Williams et al ApJ paper of 1994. These two algorithms differ
in the way that pixels within merged clumps are allocated to
individual clumps. Also the ApJ algorithm rejects clumps that do not
not extend above the second contour level, whereas the IDL algorithm
accepts such clumps. See also parameter BACKOFF. [0]
ClumpFind.Level<n>: The n'th data value at which to contour the data
array (where <n> is an integer). Values should be given for "Level1",
"Level2", "Level3", etc. Any number of contours can be supplied, but
there must be no gaps in the progression of values for <n>. The values
will be sorted into descending order before being used. If "Level1" is
not supplied (the default), then contour levels are instead determined
automatically using parameters "Tlow" and "DeltaT". Note clumps found
at higher contour levels are traced down to the lowest supplied
contour level, but any new clumps which are initially found at the
lowest contour level are ignored. That is, clumps must have peaks
which exceed the second lowest contour level to be included in the
returned catalogue. The values can be supplied either as absolute data
values, or as mutliples of the RMS noise using the syntax "[x]*RMS",
where "[x]" is a numerical value (e.g. "3.2*RMS").[] ClumpFind.MaxBad:
The maximum fraction of pixels in a clump that are allowed to be
adjacent to a bad pixel. If the fraction of clump pixels adjacent to a
bad pixel exceeds this value, the clump is excluded. If a direct
comparison with other implementations of the ClumpFind algorithm is
required, a value of 1.0 should be used. [0.05] ClumpFind.MinPix: The
lowest number of pixel which a clump can contain. If a candidate clump
has fewer than this number of pixels, it will be ignored. This
prevents noise spikes from being interpreted as real clumps. The
default value is based on the supplied values for the other parameters
that specify the minimum peak height, the background level and the
instrumental beam widths, limited to be at least 16 pixels (for 3D
data), 7 pixels (for 2D data) or 3 pixels (for 1D data, or if
"PERSPECTRUM" is set TRUE). If a direct comparison with other
implementations of the ClumpFind algorithm is required, a value of 5
should be used (for 3D data) or 20 (for 2D data). [] ClumpFind.Naxis:
Controls the way in which contiguous areas of pixels are located when
contouring the data. When a pixel is found to be at or above a contour
level, the adjacent pixels are also checked. "Naxis" defines what is
meant by an "adjacent" pixel in this sense. The supplied value must be
at least 1 and must not exceed the number of pixel axes in the data.
The default value equals the number of pixel axes in the data. If the
data is 3-dimensional, any given pixel can be considered to be at the
centre of a cube of neighbouring pixels. If "Naxis" is 1 only those
pixels which are at the centres of the cube faces are considered to be
adjacent to the central pixel. If "Naxis" is 2, pixels which are at
the centre of any edge of the cube are also considered to be adjacent
to the central pixel. If "Naxis" is 3, pixels which are at the corners
of the cube are also considered to be adjacent to the central pixel.
If the data is 2-dimensional, any given pixel can be considered to be
at the centre of a square of neighbouring pixels. If "Naxis" is 1 only
those pixels which are at the centres of the square edges are
considered to be adjacent to the central pixel. If "Naxis" is 2,
pixels which are at square corners are also considered to be adjacent
to the central pixel. For one dimensional data, a value of 1 is always
used for "Naxis", and each pixel simply has 2 adjacent pixels, one on
either side. Note, the supplied "naxis" value is ignored if the ADAM
parameter "PERSPECTRUM" is set TRUE. [] ClumpFind.RMS: The global RMS
noise level in the data. The default value is the value supplied for
parameter RMS. [] ClumpFind.Tlow: The lowest level at which to contour
the data array. Only accessed if no value is supplied for "Level1".
See also "DeltaT". The value can be supplied either as an absolute
data value, or as a mutliple of the RMS noise using the syntax
"[x]*RMS", where "[x]" is a numerical value (e.g. "3.2*RMS"). [2*RMS]
ClumpFind.VeloRes: The velocity resolution of the instrument, in
channels. The velocity width of each clump written to the output
catalogue is reduced (in quadrature) by this amount. If a direct
comparison with other implementations of the ClumpFind algorithm is
required, a value of zero should be used. [2.0]


Reinhold Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Reinhold.FwhmBeam: The FWHM of the instrument beam, in pixels. If
application paremeter DECONV is set TRUE, the clump widths written to
the output catalogue are reduced (in quadrature) by this amount. [2.0]
ReinholdClumps.MaxBad: The maximum fraction of pixels in a clump that
are allowed to be adjacent to a bad pixel. If the fraction of clump
pixels adjacent to a bad pixel exceeds this value, the clump is
excluded. [0.05] Reinhold.MinLen: The minimum number of pixels spanned
by a peak along any one dimension in order for the peak to be
considered significant. If a peak is spanned by fewer than this number
of pixels on any axis, then it is ignored. [4] Reinhold.MinPix: The
lowest number of pixel which a clump can contain. If a candidate clump
has fewer than this number of pixels, it will be ignored. This
prevents noise spikes from being interpreted as real clumps. The
default value is based on the supplied values for the other parameters
that specify the minimum peak height, the background level and the
instrumental beam widths, limited to be at least 16 pixels(for 3D
data), 7 pixels (for 2D data) or 3 pixels (for 1D data). []
Reinhold.Noise: Defines the data value below which pixels are
considered to be in the noise. A peak is considered to end when the
peak value dips below the "noise" value. The value can be supplied
either as an absolute data value, or as a mutliple of the RMS noise
using the syntax "[x]*RMS", where "[x]" is a numerical value (e.g.
"3.2*RMS"). [2*RMS] Reinhold.Thresh: The smallest significant peak
height. Peaks which have a maximum data value less than this value are
ignored. The value can be supplied either as an absolute data value,
or as a mutliple of the RMS noise using the syntax "[x]*RMS", where
"[x]" is a numerical value (e.g. "3.2*RMS"). [Noise+2*RMS]
Reinhold.FlatSlope: A peak is considered to end when the slope of a
profile through the peak drops below this value. The value should be
given as a change in data value between adjacent pixels. The value can
be supplied either as an absolute data value, or as a mutliple of the
RMS noise using the syntax "[x]*RMS", where "[x]" is a numerical value
(e.g. "3.2*RMS"). [1.0*RMS] Reinhold.CAThresh: Controls the operation
of the cellular automata which is used to erode the (previously
dilated) edges regions prior to filling them with clump indices. If
the number of edge pixels in the 3x3x3 pixel cube (or 2x2 pixel square
for 2D data) surrounding any pixel is greater than CAThresh, then the
central pixel is considered to be an edge pixel. Otherwise it is not
considered to be an edge pixel. The default value is one less than the
total number of pixels in the square or cube (i.e. 8 for 2D data and
26 for 3D data). [] Reinhold.CAIterations: This gives the number of
times to apply the cellular automata which is used to erode the edges
regions prior to filling them with clump indices. [1]
Reinhold.FixClumpsIterations: This gives the number of times to apply
the cellular automata which cleans up the filled clumps. This cellular
automata replaces each output pixel by the most commonly occuring
value within a 3x3x3 cube (or 2x2 square for 2D data) of input pixels
centred on the output pixel. [1] Reinhold.RMS: The global RMS noise
level in the data. The default value is the value supplied for
parameter RMS. [] Reinhold.VeloRes: The velocity resolution of the
instrument, in channels. The velocity width of each clump written to
the output catalogue is reduced (in quadrature) by this amount. [2.0]


FellWalker Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FellWalker.AllowEdge: If set to a zero value, then clumps are rejected
if they touch any edge of the data array. If non-zero, then such
clumps are retained. [1] FellWalker.CleanIter: This gives the number
of times to apply the cellular automata which cleans up the filled
clumps. This cellular automata replaces each clump index by the most
commonly occuring value within a 3x3x3 cube (or 2x2 square for 2D
data) of neighbours. The supplied value is ignored and a value of zero
is assumed if "PERSPECTRUM" is set TRUE. [1] FellWalker.FlatSlope: Any
initial section to a walk which has an average gradient (measured over
4 steps) less than this value, and for which the data value is less
than "NOISE + 2*RMS", will not be included in the clump. The value of
this parameter is the data increment between pixels, and can be
supplied either as an absolute data value, or as a mutliple of the RMS
noise using the syntax "[x]*RMS", where "[x]" is a numerical value
(e.g. "3.2*RMS"). [1.0*RMS] FellWalker.FwhmBeam: The FWHM of the
instrument beam, in pixels. If application paremeter DECONV is set
TRUE, the clump widths written to the output catalogue are reduced (in
quadrature) by this amount. [2.0] FellWalker.MaxBad: The maximum
fraction of pixels in a clump that are allowed to be adjacent to a bad
pixel. If the fraction of clump pixels adjacent to a bad pixel exceeds
this value, the clump is excluded. [0.05] FellWalker.MinDip: If the
dip between two adjacent peaks is less than this value, then the peaks
are considered to be part of the same clump. The value can be supplied
either as an absolute data value, or as a mutliple of the RMS noise
using the syntax "[x]*RMS", where "[x]" is a numerical value (e.g.
"3.2*RMS"). [2.0*RMS] FellWalker.MinHeight: If the peak value in a
clump is less than this value then the clump is not included in the
returned list of clumps. The value can be supplied either as an
absolute data value, or as a mutliple of the RMS noise using the
syntax "[x]*RMS", where "[x]" is a numerical value (e.g. "3.2*RMS").
[Noise] FellWalker.MinPix: The lowest number of pixel which a clump
can contain. If a candidate clump has fewer than this number of
pixels, it will be ignored. This prevents noise spikes from being
interpreted as real clumps. The default value is based on the supplied
values for the other parameters that specify the minimum peak height,
the background level and the instrumental beam widths, limited to be
at least 16 pixels (for 3D data), 7 pixels (for 2D data) or 3 pixels
(for 1D data). [] FellWalker.MaxJump: Defines the extent of the
neighbourhood about a local maximum which is checked for higher pixel
values. The neighbourhood checked is square or cube with side equal to
twice the supplied value, in pixels. [4] FellWalker.Noise: Defines the
data value below which pixels are considered to be in the noise. No
walk will start from a pixel with data value less than this value. The
value can be supplied either as an absolute data value, or as a
mutliple of the RMS noise using the syntax "[x]*RMS", where "[x]" is a
numerical value (e.g. "3.2*RMS"). [2*RMS] FellWalker.RMS: The global
RMS noise level in the data. The default value is the value supplied
for parameter RMS. [] FellWalker.VeloRes: The velocity resolution of
the instrument, in channels. The velocity width of each clump written
to the output catalogue is reduced (in quadrature) by this amount.
[2.0]


Copyright
~~~~~~~~~
Copyright (C) 2005-2007 Particle Physics & Astronomy Research Council.
Copyright (C) 2007-2009 Science & Technology Facilities Council.
Copyright (C) 2009 University of British Columbia. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


