

MAKECUBE
========


Purpose
~~~~~~~
Regrid ACSIS spectra into a data cube


Description
~~~~~~~~~~~
This routine converts one or more raw data cubes, spanned by
(frequency, detector number, time) axes, into an output cube spanned
by (celestial longitude, celestial latitude, frequency) axes.
Optionally, the output cube can be split up into several separate
NDFs, each containing a spatial tile extracted from the full cube (see
parameter JSATILES and TILEDIMS). These tiles abut exactly in pixel
co-ordinates and can be combined (for example) using KAPPA:PASTE.
In addition, there is an option to divide the output up into separate
polarisation angle bins (see parameter POLBINSIZE). If this option is
selected, each tile is split up into several output NDFs (all within
the same container file), each one containing the input data relating
to a particular range of polarisation angle.
The full output cube can be either a regularly gridded tangent-plane
projection of the sky, or a sparse array (see parameter SPARSE). If a
tangent plane projection is selected, the parameters of the projection
from sky to pixel grid co-ordinates can be specified using parameters
CROTA, PIXSIZE, REFLAT, REFLON. Alternatively, parameter AUTOGRID can
be set true, in which case projection parameters are determined
automatically in a manner that favours projections that place samples
centrally within pixels. Alternatively, a reference NDF can be
supplied (see parameter REF), in which case the same pixel grid will
be used for the output cube.
Variance values in the output can be calculated either on the basis of
the spread of input dat avalues contributing to each output pixel, or
on the basis of the system-noise temperature values supplied in the
input NDFs (see parameter GENVAR).


ADAM parameters
~~~~~~~~~~~~~~~



ALIGNSYS = _LOGICAL (Read)
``````````````````````````
If TRUE, then the spatial positions of the input data are aligned in
the co-ordinate system specified by parameter SYSTEM. Otherwise, they
are aligned in the ICRS co-ordinate system. For instance, if the
output co-ordinate system is AZEL, then setting ALIGNSYS to TRUE will
result in the AZEL values of the input data positions being compared
directly, disregarding the fact that a given AZEL will correspond to
different positions on the sky at different times. [FALSE]



AUTOGRID = _LOGICAL (Read)
``````````````````````````
Only accessed if a null value is supplied for parameter REF.
Determines how the dynamic default values should be determined for the
projection parameters CROTA, PIXSIZE, REFLAT, REFLON, REFPIX1 and
REFPIX2. If TRUE, then default projection parameters are determined by
adjusting the grid until as many data samples as possible fall close
to the centre of pixels in the output cube. If FALSE, REFLON/REFLAT
are set to the first pointing BASE position, CROTA is set to the
MAP_PA value in the FITS header (converted to the requested sky co-
ordinate system), PIXSIZE is set to 6 arcseconds, and REFPIX1/REFPIX2
are both set to zero. [FALSE]



REFPIX1 = _DOUBLE (Read)
````````````````````````
Controls the precise placement of the spatial tangent point on the
first pixel axis of the output cube. The position of the tangent point
on the sky is specified by REFLON/REFLAT, and this sky position is
placed at grid coordinates specified by REFPIX1/REFPIX2. Note, these
grid coordinates refer to an interim grid coordinate system that does
not depend on the values supplied for LBND, rather than the final grid
coordinate system of the output cube. Therefore, if values are
supplied for REFPIX1/REFPIX2, they should be copies of the values
written to output parameter PIXREF by a previous run of MAKECUBE. The
REFPIX and PIXREF parameters allow an initial run of MAKECUBE with
AUTOGRID=YES to generate projection parameters that can then be re-
used in subsequent runs of MAKECUBE with AUTOGRID=NO in order to force
MAKECUBE to use the same pixel grid. If a null (!) value is supplied,
default values will be used for REFPIX1/2 - either the autogrid values
(if AUTOGRID=YES) or (0,0) (if AUTOGRID=NO). [!]



REFPIX2 = _DOUBLE (Read)
````````````````````````
Controls the precise placement of the spatial tangent point on the
second pixel axis of the output cube. See REFPIX1. [!]



BADMASK = LITERAL (Read)
````````````````````````
A string determining the way in which bad pixels are propagated from
input to output. The "AND" scheme uses all input data (thus reducing
the noise in the output) and also minimises the number of bad pixels
in the output. However, the memory requirements of the "AND" scheme
can be excessive. For this reason, two other schemes, "FIRST" and
"OR", are provided which greatly reduce the memory requirements, at
the expense either of introducing more bad pixels into the output
("OR") or producing higher output noise levels ("FIRST"). The value
supplied for this parameter is used only if SPREAD is set to "Nearest"
(otherwise "AND" is always used):


+ "FIRST" -- The bad-pixel mask in each output spectrum is inherited
from the first input spectrum that contributes to the output spectrum.
Any subsequent input spectra that contribute to the same output
spectrum but which have a different bad-pixel mask are ignored. So an
output pixel will be bad if and only if the corresponding pixel in the
first input NDF that contributes to it is bad. Since this scheme
ignores entire input spectra if they do not conform to the expected
bad-pixel mask, the noise in the output can be higher than using the
other schemes. However, this scheme has the benefit of using much less
memory than the "AND" scheme, and will in general produce fewer bad
pixels in the output than the "OR" scheme.
+ "OR" -- The bad pixel mask in each output spectrum is the union
(logical OR) of the bad pixel masks for all input spectra that
contribute to the output spectrum. So an output pixel will be bad if
any of the input pixels that contribute to it are bad. This scheme
will in general produce more bad output pixels than the "FIRST"
scheme, but the non-bad output pixels will have a lower noise because,
unlike "FIRST", all the contributing input data are coadded to produce
the good output pixels. Like "FIRST", this scheme uses much less
memory than "AND".
+ "AND" -- The bad pixel mask for each output spectrum is the
  intersection (logical AND) of the bad pixel masks for all input
  spectra that contribute to the output spectrum. So an output pixel
  will be bad only if all the input pixels that contribute to it are
  bad. This scheme will produce fewer bad output pixels and will also
  give lower output noise levels than "FIRST" or "OR", but at the
  expense of much greater memory requirements.

["OR"]



CATFRAME = LITERAL (Read)
`````````````````````````
A string determining the co-ordinate Frame in which positions are to
be stored in the output catalogue associated with parameter OUTCAT.
The string supplied for CATFRAME can be one of the following:


+ A Domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame.
+ An IRAS90 Sky Co-ordinate System (SCS) values such as EQUAT(J2000)
  (see SUN/163).

If a null (!) value is supplied, the positions will be stored in the
current Frame of the output NDF. [!]



CATEPOCH = _DOUBLE (Read)
`````````````````````````
The epoch at which the sky positions stored in the output catalogue
were determined. It will only be accessed if an epoch value is needed
to qualify the co-ordinate Frame specified by COLFRAME. If required,
it should be given as a decimal years value, with or without decimal
places ("1996.8" for example). Such values are interpreted as a
Besselian epoch if less than 1984.0 and as a Julian epoch otherwise.



CROTA = _REAL (Read)
````````````````````
Only accessed if a null value is supplied for parameter REF. The
angle, in degrees, from north through east (in the co-ordinate system
specified by the SYSTEM parameter) to the second pixel axis in the
output cube. The dynamic default value is determined by the AUTOGRID
parameter. []



DETECTORS = LITERAL (Read)
``````````````````````````
A group of detector names to include in, or exclude from, the output
cube. If the first name starts with a minus sign, then the specified
detectors are excluded from the output cube (all other detectors are
included). Otherwise, the specified detectors are included in the
output cube (all other detectors are excluded). If a null (!) value is
supplied, data from all detectors will be used. [!]



EXTRACOLS = LITERAL (Read)
``````````````````````````
A group of names specifying extra columns to be added to the catalogue
specified by parameter OUTCAT. Each name should be the name of a
component in the JCMTState extension structure. For each name in the
group, an extra column is added to the output catalogue containing the
value of the named extension item for every table row (i.e. for each
data sample). These extra columns can be viewed and manipulated with
general-purpose FITS table tools such as TOPCAT, but will not be
displayed by the KAPPA:LISTSHOW command. One use for these extra
columns is to allow the catalogue to be filtered (e.g. by TOPCAT) to
remove samples that meet (or do not meet) some specified requirement
specified by the JCMTState contents. No extra columns are added if a
null (!) value is supplied. [!]



FBL( ) = _DOUBLE (Write)
````````````````````````
Sky co-ordinates (radians) of the bottom-left corner of the output
cube (the corner with the smallest PIXEL dimension for Axis 1 and the
smallest pixel dimension for Axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel. If SPARSE mode is enabled the positions reported
will not be reliable.



FBR( ) = _DOUBLE (Write)
````````````````````````
Sky co-ordinates (radians) of the bottom right corner of the output
cube (the corner with the largest PIXEL dimension for Axis 1 and the
smallest pixel dimension for Axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel. If SPARSE mode is enabled the positions reported
will not be reliable.



FLBND( ) = _DOUBLE (Write)
``````````````````````````
The lower bounds of the bounding box enclosing the output cube in the
selected output WCS Frame. The values are calculated even if no output
cube is created. Celestial axis values will be in units of radians,
spectral-axis units will be in the same units as the input frameset
(matching those used in the SPECBOUNDS parameter). The parameter is
named to be consistent with KAPPA:NDFTRACE output. Note, the stored
values correspond to the outer edges of the first pixel, not to the
pixel centre.



FUBND( ) = _DOUBLE (Write)
``````````````````````````
The upper bounds of the bounding box enclosing the output cube in the
selected output WCS Frame. The values are calculated even if no output
cube is created. Celestial axis values will be in units of radians,
spectral-axis units will be in the same units of the input frameset
(matching those used in the SPECBOUNDS parameter). The parameter is
named to be consistent with KAPPA:NDFTRACE output. Note, the stored
values correspond to the outer edges of the first pixel, not to the
pixel centre.



FTL( ) = _DOUBLE (Write)
````````````````````````
Sky co-ordinates (radians) of the top left corner of the output cube
(the corner with the smallest PIXEL dimension for Axis 1 and the
largest pixel dimension for Axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel. If SPARSE mode is enabled the positions reported
will not be reliable.



FTR( ) = _DOUBLE (Write)
````````````````````````
Sky co-ordinates (radians) of the top right corner of the output cube
(the corner with the largest PIXEL dimension for Axis 1 and the
largest pixel dimension for Axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel. If SPARSE mode is enabled the positions reported
will not be reliable.



GENVAR = LITERAL (Read)
```````````````````````
Indicates how the Variance values in the output NDF are to be
calculated. It can take any of the following values:


+ "Spread" -- the output Variance values are based on the spread of
input data values contributing to each output pixel. This option is
not available if parameter SPARSE is set TRUE. If the BADMASK value is
"OR" or "FIRST", then a single variance value will be produced for
each output spectrum (i.e. all channels in an output spectrum will
have the same variance value). If BADMASK is "AND", then an
independent variance value will be calculated for each channel in each
output spectrum.
+ "Tsys" -- the output Variance values are based on the system noise
temperature values supplied in the input NDFs. Since each input
spectrum is characterised by a single Tsys value, each output spectrum
will have a constant Variance value (i.e. all channels in an output
spectrum will have the same variance value).
+ "None" -- no output Variance values are created.

["Tsys"]



IN = NDF (Read)
```````````````
Input raw data file(s)



INWEIGHT = _LOGICAL (Read)
``````````````````````````
Indicates if the input spectra should be weighted when combining two
or more input spectra together to form an output spectrum. If TRUE,
the weights used are the reciprocal of the variances associated with
the input spectra, as determined from the Tsys values in the input.
[TRUE]



JSATILES = _LOGICAL (Read)
``````````````````````````
If TRUE, the output cube is created on the JSA all-sky pixel grid, and
is split up into individual JSA tiles. Thus multiple output NDFs may
be created, one for each JSA tile that touches the cube. Each of these
output NDFs will have the tile index number appended to the end of the
path specified by parameter "OUT". If "JSATILES" is TRUE, the "REF"
parameter is ignored. [FALSE]



JSATILELIST() = _INTEGER (Write)
````````````````````````````````
If parameter "JSATILES" is set TRUE, the zero-based indices of the
created JSA tiles will be written to this output parameter. The number
of such indices is given the "NTILE" parameter



LBND( 2 ) = _INTEGER (Read)
```````````````````````````
An array of values giving the lower pixel-index bound on each spatial
axis of the output NDF. The suggested default values encompass all the
input spatial information. The supplied bounds may be modified if the
parameter TRIM takes its default value of TRUE. []



LBOUND( 3 ) = _INTEGER (Write)
``````````````````````````````
The lower pixel bounds of the output NDF. Note, values will be written
to this output parameter even if a null value is supplied for
parameter OUT.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NTILE = _INTEGER (Write)
````````````````````````
The number of output tiles used to hold the entire output array (see
parameter JSATILES and TILEDIMS). If no input data falls within a
specified tile, then no output NDF will be created for the tile, but
(if JSATILES is FALSE) the tile will still be included in the tile
numbering scheme.



NPOLBIN = _INTEGER (Write)
``````````````````````````
The number of polarisation angle bins used to hold the entire output
data (see parameter POLBINSIZE).



OUT = NDF (Write)
`````````````````
Output file. If a null (!) value is supplied, the application will
terminate early without creating an output cube, but without reporting
an error. Note, the pixel bounds which the output cube would have had
will still be written to output parameters LBOUND and UBOUND, even if
a null value is supplied for OUT. If the output cube is split up into
multiple output NDFs (e.g. an NDF for each tile -- see parameter
TILEDIMS -- or for each polarisation angle bin -- see parameter
POLBINSIZE), then the value supplied for "OUT" will be used as the
root name to which other strings are appended to create the name of
each output NDF.



OUTCAT = FILENAME (Write)
`````````````````````````
An output catalogue in which to store all the spatial detector
positions used to make the output cube (i.e. those selected using the
DETECTORS parameter). By default, the stored positions are in the same
sky co-ordinate system as the current Frame in the output NDF (but see
parameter CATFRAME). The label associated with each row in the
catalogue is the detector name. The detector positions in the
catalogue are ordered as follows: all the positions for the first
input NDF come first, followed by those for the second input NDF, etc.
Within the group of positions associated with a single input NDF, the
positions for the first time slice come first, followed by the
positions for the second time slice, etc. If a null value (!) is
supplied, no output catalogue is produced. See also parameter
CATFRAME. [!]



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application via parameter OUT (one per
line). If a null (!) value is supplied no file is created. [!]



PARAMS( 2 ) = _DOUBLE (Read)
````````````````````````````
An optional array which consists of additional parameters required by
the Sinc, SincSinc, SincCos, SincGauss, Somb, SombCos, and Gauss
spreading methods (see parameter SPREAD).
PARAMS( 1 ) is required by all the above schemes. It is used to
specify how many pixels on either side of the output position (that
is, the output position corresponding to the centre of the input
pixel) are to receive contributions from the input pixel. Typically, a
value of 2 is appropriate and the minimum allowed value is 1 (i.e. one
pixel on each side). A value of zero or fewer indicates that a
suitable number of pixels should be calculated automatically. [0]
PARAMS( 2 ) is required only by the SombCos, Gauss, SincSinc, SincCos,
and SincGauss schemes. For the SombCos, SincSinc, and SincCos schemes,
it specifies the number of pixels at which the envelope of the
function goes to zero. The minimum value is 1.0, and the run-time
default value is 2.0. For the Gauss and SincGauss scheme, it specifies
the full-width at half-maximum (FWHM) of the Gaussian envelope. The
minimum value is 0.1, and the run-time default is 1.0. On astronomical
images and spectra, good results are often obtained by approximately
matching the FWHM of the envelope function, given by PARAMS(2), to the
point-spread function of the input data. []



PIXREF( 2 ) = _DOUBLE (Write)
`````````````````````````````
The grid coordinates used for the reference pixel, within the interim
grid coordinate system. See REFPIX1.



PIXSIZE( 2 ) = _REAL (Read)
```````````````````````````
Only accessed if a null value is supplied for parameter REF. Pixel
dimensions in the output image, in arcseconds. If only one value is
supplied, the same value will be used for both axes. The dynamic
default value is determined by the AUTOGRID parameter. []



POLBINSIZE = _REAL (Read)
`````````````````````````
This parameter is only prompted for if the input files contain
polarisation data. The supplied value is used as the bin size (in
degrees) for grouping polarisation analyser angles. The first bin is
centred at the angle given by parameter POLBINZERO. The "analyser
angle" is the anti-clockwise angle from celestial north (in the system
chosen by parameter SYSTEM) to the axis of the "effective analyser" -
a rotating analyser that would have the same effect as the combination
of fixed analyser and half-wave plate actually present in the
polarimeter. The supplied value for POLBINSIZE will be modified if
required to ensure that a whole number of bins is used to cover the
complete range of analyser angles (0 to 360 degrees). A separate
output cube will be created for each bin that is not empty, and each
output NDF will contain a POLPACK extension suitable for use with the
POLPACK:POLCAL command. These NDFs are all stored in a single HDS
container file (one per tile) with the name specified by parameter
OUT. Within this container file, each cube will be held in a component
with name of the form "P<N>" appended to the end, where "<N>" is an
integer bin index. The largest value of N is written to output
parameter NPOLBIN. If a null value (!) is supplied, then a single
output NDF (without POLPACK extension) is created for each tile,
containing all input data.



POLBINZERO = _REAL (Read)
`````````````````````````
This parameter is only prompted for if the input files contain
polarisation data. It is the analyser angle (in degrees) at the centre
of the first analyser angle bin. A value of zero corresponds to north
in the celestial co-ordinate system specified by parameter SYSTEM. [0]



POSERRFATAL = _LOGICAL (Read)
`````````````````````````````
If a true value is supplied, then an error is reported and the
application terminates if a significant difference is found between
the detector positions array (RECEPPOS) and positions implied by the
FPLANEX/Y arrays. If a false value is supplied, a warning is issued
but the application proceeds. See also parameters POSERRMAX and
USEDETPOS. [FALSE]



POSERRMAX = _REAL (Read)
````````````````````````
Defines the maximum insignificant discrepancy between the detector
positions array (RECEPPOS) and positions implied by the FPLANEX/Y
arrays, in units of arc-seconds. See parameter POSERRFATAL. [3.0]



REF = NDF (Read)
````````````````
An existing NDF that is to be used to define the output grid, or the
string "JSA". If an NDF is supplied, the output grid will be aligned
with the supplied reference NDF. The NDF need not be three-
dimensional. For instance, a two-dimensional image can be supplied in
which case the spatial axes of the output cube will be aligned with
the reference image and the spectral axis will be inherited form the
first input NDF. If "JSA" is supplied, the JSA all-sky pixel grid will
be used (note, the cube will still be created as a single NDF - if
multiple NDFs, one for each JSA tile, are required, the "JSATILES"
parameter should beset TRUE instead of using the "REF" parameter). If
a null (!) value is supplied then the output grid is determined by
parameters AUTOGRID, REFLON, REFLAT, etc. [!]



REFLAT = LITERAL (Read)
```````````````````````
Only accessed if a null value is supplied for parameter REF. The
formatted celestial-latitude value at the tangent point of the spatial
projection in the output cube. This should be provided in the system
specified by parameter SYSTEM. The dynamic-default value is determined
by the AUTOGRID parameter. []



REFLON = LITERAL (Read)
```````````````````````
Only accessed if a null value is supplied for parameter REF. The
formatted celestial-longitude value at the tangent point of the
spatial projection in the output cube. This should be provided in the
system specified by parameter SYSTEM. The dynamic-default value is
determined by the AUTOGRID parameter. []



SPARSE = _LOGICAL (Read)
````````````````````````
Indicates if the spectra in the output cube should be stored as a
sparse array, or as a regularly gridded array. If FALSE, pixel Axes 1
and 2 of the output cube represent a regularly gridded tangent plane
projection of the sky, with parameters determined by CROTA, PIXSIZE,
REFLON and REFLAT. Each input spectrum is placed at the appropriate
pixel position in this three-dimensional projection, as given by the
celestial co-ordinates associated with the spectrum. If SPARSE is
TRUE, then each input spectrum is given an associated index, starting
from 1, and the spectrum with index "I" is stored at pixel position
(I,1) in the output cube (pixel Axis 2 will always have the value 1 --
that is, Axis 2 is a degenerate axis that spans only a single pixel).
In both cases, the third pixel axis in the output cube corresponds to
spectral position (frequency, velocity, etc).
Whatever the setting of SPARSE, the output NDF's WCS component can be
used to transform pixel position into the corresponding (celestial
longitude, celestial latitude, spectral position) values. However, if
SPARSE is TRUE, then the inverse transformation (i.e. from
(long,lat,spec) to pixel co-ordinates) will not be defined. This
means, for instance, that if a sparse array is displayed as a two-
dimensional image, then it will not be possible to annotate the axes
with WCS values. Also, whilst KAPPA:WCSMOSAIC will succesfully align
the data in a sparse array with a regularly gridded cube,
KAPPA:WCSALIGN will not, since WCSALIGN needs the inverse
transformation to be defined.
The dynamic default value for SPARSE depends on the value supplied for
parameter AUTOGRID. If AUTOGRID is set FALSE, then SPARSE defaults to
FALSE. If AUTOGRID is set TRUE, then the default for SPARSE will be
TRUE if the algorithm described under the AUTOGRID parameter fails to
find useful default grid parameters. If the AUTOGRID algorithm
succeeds, the default for SPARSE will be FALSE. []



SPECBOUNDS = LITERAL (Read)
```````````````````````````
The bounds of the output cube on the spectral axis. Input data that
falls outside the supplied range will not be included in the output
cube. The supplied parameter value should be a string containing a
pair of axis values separated by white space or commas. The first
should be the spectral value corresponding to the lower edge of the
first spectral channel in the output cube, and the second should be
the spectral value corresponding to the upper edge of the last
spectral channel. The supplied values should refer to the spectral
system described by the WCS FrameSet of the first input NDF. To see
what this is, supply a single colon (":") for the parameter value.
This will display a description of the required spectral co-ordinate
system, and then re-prompt for a new parameter value. The dynamic
default is determined by the SPECUNION parameter. []



SPECUNION = _LOGICAL (Read)
```````````````````````````
Determines how the default spectral bounds for the output are chosen.
If a TRUE value is supplied, then the defaults for the SPECBOUNDS
parameter represent the union of the spectral ranges in the input
data. Otherwise, they represent the intersection of the spectral
ranges in the input data. This option is only available if parameter
BADMASK is set to AND. For any other value of BADMASK, a value of
FALSE is always used for SPECUNION. [FALSE]



SPREAD = LITERAL (Read)
```````````````````````
The method to use when spreading each input pixel value out between a
group of neighbouring output pixels. If SPARSE is set TRUE, then
SPREAD is not accessed and a value of "Nearest" is always assumed.
SPREAD can take the following values:


+ "Linear" -- The input pixel value is divided bi-linearly between the
four nearest output pixels. Produces smoother output NDFs than the
nearest-neighbour scheme.
+ "Nearest" -- The input pixel value is assigned completely to the
single nearest output pixel. This scheme is much faster than any of
the others.
+ "Sinc" -- Uses the sinc(pi*x) kernel, where x is the pixel offset
from the interpolation point (resampling) or transformed input pixel
centre (rebinning), and sinc(z)=sin(z)/z. Use of this scheme is not
recommended.
+ "SincSinc" -- Uses the sinc(pi*x)sinc(k*pi*x) kernel. A valuable
general-purpose scheme, intermediate in its visual effect on NDFs
between the bi-linear and nearest-neighbour schemes.
+ "SincCos" -- Uses the sinc(pi*x)cos(k*pi*x) kernel. Gives similar
results to the "Sincsinc" scheme.
+ "SincGauss" -- Uses the sinc(pi*x)exp(-k*x*x) kernel. Good results
can be obtained by matching the FWHM of the envelope function to the
point-spread function of the input data (see parameter PARAMS).
+ "Somb" -- Uses the somb(pi*x) kernel, where x is the pixel offset
from the transformed input pixel centre, and somb(z)=2*J1(z)/z (J1 is
the first-order Bessel function of the first kind). This scheme is
similar to the "Sinc" scheme.
+ "SombCos" -- Uses the somb(pi*x)cos(k*pi*x) kernel. This scheme is
similar to the "SincCos" scheme.
+ "Gauss" -- Uses the exp(-k*x*x) kernel. The FWHM of the Gaussian is
  given by parameter PARAMS(2), and the point at which to truncate the
  Gaussian to zero is given by parameter PARAMS(1).

For further details of these schemes, see the descriptions of routine
AST_REBINx in SUN/211. ["Nearest"]



SYSTEM = LITERAL (Read)
```````````````````````
The celestial co-ordinate system for the output cube. One of ICRS,
GAPPT, FK5, FK4, FK4-NO-E, AZEL, GALACTIC, ECLIPTIC. It can also be
given the value "TRACKING", in which case the system used will be
which ever system was used as the tracking system during in the
observation. The value supplied for the CROTA parameter should refer
to the co-ordinate system specified by this parameter.
The choice of system also determines if the telescope is considered to
be tracking a moving object such as a planet or asteroid. If system is
GAPPT or AZEL, then each time slice in the input data will be shifted
in order to put the base telescope position (given by TCS_AZ_BC1/2 in
the JCMTSTATE extension of the input NDF) at the same pixel position
that it had for the first time slice. For any other system, no such
shifts are applied, even if the base telescope position is changing
through the observation. [TRACKING]



TILEBORDER = _INTEGER (Read)
````````````````````````````
Only accessed if a non-null value is supplied for parameter TILEDIMS.
It gives the width, in pixels, of a border to add to each output tile.
These borders contain data from the adjacent tile. This results in an
overlap between adjacent tiles equal to twice the supplied border
width. If the default value of zero is accepted, then output tiles
will abut each other in pixel space without any overlap. If a non-zero
value is supplied, then each pair of adjacent tiles will overlap by
twice the given number of pixels. Pixels within the overlap border
will be given a quality name of "BORDER" (see KAPPA:SHOWQUAL). [0]



TILEDIMS( 2 ) = _INTEGER (Read)
```````````````````````````````
This parameter is ignored if parameter "JSATILES" is set TRUE.
For large data sets, it may sometimes be beneficial to break the
output array up into a number of smaller rectangular tiles, each
created separately and stored in a separate output NDF. This can be
accomplished by supplying non-null values for the TILEDIMS parameter.
If supplied, these values give the nominal spatial size of each output
tile, in pixels. Edge tiles may be thinner if the TRIMTILES parameter
is set TRUE. In order to avoid creating very thin tiles around the
edges, the actual tile size used for the edge tiles may be up to 10 %
larger than the supplied value. This creation of "fat" edge tiles may
be prevented by supplying a negative value for the tile size, in which
case edge tiles will never be wider than the supplied absolute value.
If only one value is supplied, the supplied value is duplicated to
create square tiles. Tiles are created in a raster fashion, from
bottom left to top right of the spatial extent. The NDF file name
specified by "out" is modified for each tile by appending "_<N>" to
the end of it, where <N> is the integer tile index (starting at 1).
The number of tiles used to cover the entire output cube is written to
output parameter NTILES. The tiles all share the same projection and
so can be simply pasted together in pixel co-ordinates to reconstruct
the full size output array. The tiles are centred so that the
reference position (given by REFLON and REFLAT) falls at the centre of
a tile. If a tile receives no input data, then no corresponding output
NDF is created, but the tile is still included in the tile numbering
scheme. If a null (!) value is supplied for TILEDIMS, then the entire
output array is created as a single tile and stored in a single output
NDF with the name given by parameter OUT (without any "_<N>"
appendage). [!]



TRIM = _LOGICAL (Read)
``````````````````````
If TRUE, then the output cube will be trimmed to exclude any borders
filled with bad values. Such borders can be caused, for instance, by
one or more detectors having been excluded (see parameter DETECTORS),
or by the supplied LBND and/or UBND parameter values extending beyond
the available data. [TRUE]



TRIMTILES = _LOGICAL (Read)
```````````````````````````
Only accessed if the output is being split up into more than one
spatial tile (see parameter TILEDIMS and JSATILES). If TRUE, then the
tiles around the border will be trimmed to exclude areas that fall
outside the bounds of the full sized output array. This will result in
the border tiles being smaller than the central tiles. [FALSE]



UBND( 2 ) = _INTEGER (Read)
```````````````````````````
An array of values giving the upper pixel-index bound on each spatial
axis of the output NDF. The suggested default values encompass all the
input spatial information. The supplied bounds may be modified if the
parameter TRIM takes its default value of TRUE. []



UBOUND( 3 ) = _INTEGER (Write)
``````````````````````````````
The upper pixel bounds of the output NDF. Note, values will be written
to this output parameter even if a null value is supplied for
parameter OUT.



USEDETPOS = _LOGICAL (Read)
```````````````````````````
If a true value is supplied, then the detector positions are read from
the detector position arrays in each input NDF. Otherwise, the
detector positions are calculated on the basis of the FPLANEX/Y
arrays. Both methods should (in the absence of bugs) result in
identical cubes. See also parameter POSERRFATAL. [TRUE]



WEIGHTS = _LOGICAL (Read)
`````````````````````````
If TRUE, then the weights associated with the array of output pixels
are stored in an extension named ACSISRED, within the output NDF. If
FALSE the weights are discarded once they have been used. These
weights record the relative weight of the input data associated with
each output pixel. If SPARSE is set TRUE, then WEIGHTS is not accessed
and a FALSE value is assumed. [FALSE]



Notes
~~~~~


+ A FITS extension is added to the output NDF containing any keywords
that are common to all input NDFs. To be included in the output FITS
extension, a FITS keyword must be present in the NDF extension of
every input NDF, and it must have the same value in all input NDFs. In
addition, certain headers that relate to start and end events are
propagated from the oldest and newest files respectively.
+ The output NDF will contain an extension named "SMURF" containing
two NDFs named "EXP_TIME" and "EFF_TIME". In addition, if parameter
SPREAD is set to "Nearest", a third NDF called "TSYS" will be created.
Each of these NDFs is 2-dimensional, with the same pixel bounds as the
spatial axes of the main output NDF, so that a pixel in one of these
NDFs corresponds to a spectrum in the main output NDF. EXP_TIME holds
the sum of the total exposure times (Ton + Toff) for the input spectra
that contributed to each output spectrum. EFF_TIME holds the sum of
the effective integration times (Teff) for the input spectra that
contributed to each output spectrum, scaled up by a factor of 4 in
order to normalise it to the reported exposure times in EXP_TIME. TSYS
holds the effective system temperature for each output spectrum. The
TSYS array is not created if GENVAR is "None" or if SPREAD is not
"Nearest".
+ FITS keywords EXP_TIME, EFF_TIME and MEDTSYS are added to the output
FITS extension. The EXP_TIME and EFF_TIME keywords hold the median
values of the EXP_TIME and EFF_TIME arrays (stored in the SMURF
extension of the output NDF). The MEDTSYS keyword holds the median
value of the TSYS array (also stored in the SMURF extension of the
output NDF). If any of these values cannot be calculated for any
reason, the corresponding FITS keyword is assigned a blank value.
+ FITS keywords NUMTILES and TILENUM are added to the output FITS
  header. These are the number of tiles used to hold the output data,
  and the index of the NDF containing the header, in the range 1 to
  NUMTILES. See parameter TILEDIMS.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: TIMESORT


Copyright
~~~~~~~~~
Copyright (C) 2017 East Asian Observatory. Copyright (C) 2007-2014
Science and Technology Facilities Council. Copyright (C) 2006-2007
Particle Physics and Astronomy Research Council. Copyright (C)
2006-2008,2013 University of British Columbia. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


