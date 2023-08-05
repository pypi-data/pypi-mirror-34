

MAKEMAP
=======


Purpose
~~~~~~~
Make a map from SCUBA-2 data


Description
~~~~~~~~~~~
This command is used to create a map from SCUBA-2 data. Two techniques
are provided and can be selected using the METHOD parameter.
The "REBIN" method can be used to make a map by coadding all the
samples in the correct location using a number of different
convolution techniques. This is useful when the time series has been
processed independently of the map-maker and the map should be made
"as-is". Raw data will be flatfielded but this method will not apply
any extinction correction, sky removal or filtering. It is assumed
that this has been handled by other tasks prior to making the map.
The default "ITERATE" method takes a more holistic approach to map
making using an iterative technique to fit for a number of models for
noise and instrumental behaviour, one of which is the underlying
astronomical image. Details of the map making process can be
controlled using the CONFIG parameter.


ADAM parameters
~~~~~~~~~~~~~~~



ABORTEDAT = _INTEGER (Write)
````````````````````````````
Set to a non-zero value on exit if the iterative process was aborted
because of the ABORTSOON parameter being set TRUE. The specific non-
zero value returned is the number of iterations that had been
completed when the iterative process was aborted. Always set to zero
if ABORTSOON is FALSE.



ABORTSOON = _LOGICAL (Read)
```````````````````````````
If TRUE, then the iterative process will exit as soon as it becomes
likely that the convergence criterion (specified by configuration
parameter MAPTOL) will not be reached within the number of iterations
allowed by configuration parameter NUMITER. [FALSE]



ALIGNSYS = _LOGICAL (Read)
``````````````````````````
If TRUE, then the spatial positions of the input data are aligned in
the co-ordinate system specified by parameter SYSTEM. Otherwise, they
are aligned in the ICRS co-ordinate system. For instance, if the
output co-ordinate system is AZEL, then setting ALIGNSYS to TRUE will
result in the AZEL values of the input data positions being compared
directly, disregarding the fact that a given AZEL will correspond to
different positions on the sky at different times. [FALSE]



BBM = NDF (Read)
````````````````
Group of files to be used as bad bolometer masks. Each data file
specified with the IN parameter will be masked. The corresponding
previous mask for a subarray will be used. If there is no previous
mask the closest following will be used. It is not an error for no
mask to match. A NULL parameter indicates no mask files to be
supplied. [!]



CHUNKCHANGE( ) = _DOUBLE (Write)
````````````````````````````````
An output array holding the final normalised map change value for each
chunk.



CONFIG = GROUP (Read)
`````````````````````
Specifies values for the configuration parameters used by the
iterative map maker (METHOD=ITERATE). If the string "def" (case-
insensitive) or a null (!) value is supplied, a set of default
configuration parameter values will be used. A full list of the
available configuration parameters is available in the appendix of
SUN/258. A smaller list of the more commonly used configuration
parameters is available in SC/21.
The supplied value should be either a comma-separated list of strings
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated lists of strings. Each string
is either a "keyword=value" setting, or the name of a text file
preceded by an up-arrow character "^". Such text files should contain
further comma-separated lists which will be read and interpreted in
the same manner (any blank lines or lines beginning with "#" are
ignored). Within a text file, newlines can be used as delimiters, as
well as commas. Settings are applied in the order in which they occur
within the list, with later settings over-riding any earlier settings
given for the same keyword.
Each individual setting should be of the form:
<keyword>=<value>
The parameters available are listed in the "Configuration Parameters"
appendix of SUN/258. Default values will be used for any unspecified
parameters. Assigning the value "<def>" (case insensitive) to a
keyword has the effect of reseting it to its default value.
Unrecognised options will result in an error condition. This is done
to help find spelling mistakes. [current value]



CROTA = _REAL (Read)
````````````````````
The angle, in degrees, from north through east (in the coordinate
system specified by the SYSTEM parameter) to the second pixel axis in
the output cube. Only accessed if a null value is supplied for
parameter REF.



FBL( ) = _DOUBLE (Write)
````````````````````````
Sky coordinates (radians) of the bottom left corner of the output map
(the corner with the smallest PIXEL dimension for axis 1 and the
smallest PIXEL dimension for axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel.



FBR( ) = _DOUBLE (Write)
````````````````````````
Sky coordinates (radians) of the bottom right corner of the output map
(the corner with the largest PIXEL dimension for axis 1 and the
smallest PIXEL dimension for axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel.



FLBND( ) = _DOUBLE (Write)
``````````````````````````
The lower bounds of the bounding box enclosing the output map in the
selected output WCS Frame. The values are calculated even if no output
cube is created. Celestial axis values will be in units of radians.
The parameter is named to be consistent with KAPPA:NDFTRACE output.



FLATMETH = _CHAR (Read)
```````````````````````
Method to use to calculate the flatfield solution. Options are
POLYNOMIAL and TABLE. Polynomial fits a polynomial to the measured
signal. Table uses an interpolation scheme between the measurements to
determine the power. [POLYNOMIAL]



FLATORDER = _INTEGER (Read)
```````````````````````````
The order of polynomial to use when choosing POLYNOMIAL method. [1]



FLATSNR = _DOUBLE (Read)
````````````````````````
Signal-to-noise ratio threshold to use when filtering the responsivity
data to determine valid bolometers for the flatfield. [3.0]



FLATUSENEXT = _LOGICAL (Read)
`````````````````````````````
If true the previous and following flatfield will be used to determine
the overall flatfield to apply to a sequence. If false only the
previous flatfield will be used. A null default will use both
flatfields for data when we did not heater track at the end, and will
use a single flatfield when we did heater track. The parameter value
is not sticky and will revert to the default unless explicitly over-
ridden. [!]



FTL( ) = _DOUBLE (Write)
````````````````````````
Sky coordinates (radians) of the top left corner of the output map
(the corner with the smallest PIXEL dimension for axis 1 and the
largest PIXEL dimension for axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel.



FTR( ) = _DOUBLE (Write)
````````````````````````
Sky coordinates (radians) of the top right corner of the output map
(the corner with the largest PIXEL dimension for axis 1 and the
largest PIXEL dimension for axis 2). No check is made that the pixel
corresponds to valid data. Note that the position is reported for the
centre of the pixel.



FUBND( ) = _DOUBLE (Write)
``````````````````````````
The upper bounds of the bounding box enclosing the output map in the
selected output WCS Frame. The values are calculated even if no output
cube is created. Celestial axis values will be in units of radians.
The parameter is named to be consistent with KAPPA:NDFTRACE output.



FTSPORT = _CHAR (Read)
``````````````````````
The FTS-2 port to use in calculating the mapping to sky coordinates,
or null if FTS-2 was not in the beam. If set, this parameter should be
"tracking" or "image". [!]



IN = NDF (Read)
```````````````
Input file(s).



IPREF = NDF (Read)
``````````````````
An existing NDF that is to be used to define the correction to be made
for instrumental polarisation (IP). It is only accessed if the input
data contains POL2 Q or U time-series values, as created by
SMURF:CALCQU. No IP correction is made if a null (!) value is
supplied. If a non-null value is supplied, it should be an NDF that
holds the total intensity (in pW) within the area of sky covered by
the output map. The supplied NDF need not be pre-aligned with the
output map - the WCS information in the NDF will be used to aligned
them. For each Q or U value in the input time-streams, the
corresponding total intensity (I) value is found by sampling the
supplied IPREF map at the sky position of the Q/U value. This I value
is multipled by a factor that depends on elevation and focal plane
position, to get the IP correction. These Q and U corrections are
rotated so that they use the same reference direction as the input Q/U
data, corrected for extinction, and are then subtracted from the input
Q or U value before going on to make a map from the corrected values.
[!]



ITERMAPS = LITERAL (Read)
`````````````````````````
Specifies the name of a file in which to place a copy of the current
map at the end of each iteration. If a null (!) value is supplied,
they are placed in the MORE.SMURF.ITERMAPS component of the main
output NDF (see parameter OUT). See configuration parameter "Itermap".
[!]



JSATILES = _LOGICAL (Read)
``````````````````````````
If TRUE, the output map is created on the JSA all-sky pixel grid, and
is split up into individual JSA tiles. Thus multiple output NDFs may
be created, one for each JSA tile that touches the map. Each of these
output NDFs will have the tile index number appended to the end of the
path specified by parameter "OUT". If "JSATILES" is TRUE, the "REF"
parameter is ignored. [FALSE]



JSATILELIST() = _INTEGER (Write)
````````````````````````````````
If parameter "JSATILES" is set TRUE, the zero-based indicies of the
created JSA tiles will be written to this output parameter. The number
of such indices is given the "NTILE" parameter



LBND( 2 ) = _INTEGER (Read)
```````````````````````````
An array of values giving the lower pixel index bound on each spatial
axis of the output NDF. The suggested default values encompass all the
input spatial information. The supplied values may be modified if TRIM
is set TRUE. []



LBOUND( 2 ) = _INTEGER (Write)
``````````````````````````````
The lower pixel bounds of the output NDF. Note, values will be written
to this output parameter even if a null value is supplied for
parameter OUT.



MASK2 = NDF (Read)
``````````````````
An existing NDF that can be used to specify a second external mask for
use with either the AST, FLT or COM model. See configuration
parameters AST.ZERO_MASK, FLT.ZERO_MASK and COM.ZERO_MASK. Note, it is
assumed that this image is aligned in pixel coordinate with the output
map. [!]



MASK3 = NDF (Read)
``````````````````
An existing NDF that can be used to specify a third external mask for
use with either the AST, FLT or COM model. See configuration
parameters AST.ZERO_MASK, FLT.ZERO_MASK and COM.ZERO_MASK. Note, it is
assumed that this image is aligned in pixel coordinate with the output
map. [!]



MAXMEM = _INTEGER (Read)
````````````````````````
Maximum memory available for map-making in MiB (mebibytes). For
machines with more than 20 GB or memory, the default is to leave 4 GB
free for other processes. For machines with less than than 20 GB or
memory, the default is to leave 20% of the total memory free for other
processes. []



METHOD = LITERAL (Read)
```````````````````````
Specify which map-maker should be used to construct the map. The
parameter can take the following values:

+ "REBIN" -- Use a single pass rebinning algorithm. This technique
assumes that the data have previously had atmosphere and instrument
signatures removed. It makes use of the standard AST library rebinning
algorithms (see also KAPPA:WCSMOSAIC). It is an excellent choice for
obtaining an image quickly, especially of a bright source.
+ "ITERATE" -- Use the iterative map maker. This map maker is much
  slower than the REBIN algorithm because it continually makes a map,
  constructs models for different data components (common-mode, spikes
  etc.). See CONFIG for parameters controlling the iterative map maker.
  [ITERATE]





MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NBOLOEFF = _DOUBLE (Write)
``````````````````````````
Effective number of bolometers in the output map when METHOD=iterate.
[!]



NCONTCHUNK = _INTEGER (Write)
`````````````````````````````
Total number of continuous data chunks processed by makemap when
METHOD=iterate. [!]



NMCNVG = _INTEGER (Write)
`````````````````````````
Total number of continuous data chunks processed by makemap when
METHOD=iterate that failed to converge. [!]



NMINSMP = _INTEGER (Write)
``````````````````````````
Total number of continuous data chunks processed by makemap when
METHOD=iterate that failed due to insufficient samples. [!]



NTILE = _INTEGER (Write)
````````````````````````
The number of output tiles used to hold the entire output array (see
parameters JSATILES and TILEDIMS). If no input data fall within a
specified tile, then no output NDF will be created for the tile, but
(if JSATILES is FALSE) the tile will still be included in the tile
numbering.



OUT = NDF (Write)
`````````````````
Output file.



OUTFILES = LITERAL (Write)
``````````````````````````
The name of a text file to create, in which to put the names of all
the output NDFs created by this application via parameter OUT (one per
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
point-spread function of the input data.



PIXSIZE( 2 ) = _REAL (Read)
```````````````````````````
Pixel dimensions in the output image, in arcsec. If only one value is
supplied, the same value will be used for both axes. The default
depends on the wavelength of the input data.



POINTING = LITERAL (Read)
`````````````````````````
The name of a text file containing corrections to the pointing read
from the input data files. If null (!) is supplied, no corrections are
used. If a file is supplied, it should start with one or more lines
containing "#" in column one. These are comment lines, but if any
comment line has the form "# SYSTEM=AZEL" or "# SYSTEM=TRACKING" then
it determines the system in which the pointing correction are
specified (SYSTEM defaults to AZEL). The last comment line should be a
space-separated list of column names, including "TAI", "DLON" and
"DLAT". Each remaining line should contain numerical values for each
column, separated by white space. The TAI column should contain the
TAI time given as an MJD. The DLON and DLAT columns should give arc-
distance offsets parallel to the longitude and latitude axes, in arc-
seconds. The TAI values should be monotonic increasing with row
number. The longitude and latitude axes are either AZEL or TRACKING as
determined by the SYSTEM value in the header comments. Blank lines are
ignored. The DLON and DLAT values are added onto the SMU jiggle
positions stored in the JCMTSTATE extension of the input NDFs. DLON
and DLAT values for non-tabulated times are determined by
interpolation.
If you need to apply two sets of pointing corrections, one in TRACKING
and one in AZEL, you can include two tables (one for each system) in a
single text file. Both tables should use the format described above.
The two tables must be separated by a line containing two or more
minus signs with no leading spaces. [!]



RATE_LIMITED = _LOGICAL (Write)
```````````````````````````````
Set TRUE on exit if the iterative loop was terminated because the mean
normalised change in the map does not seem to be falling (see config
parameter "MAPTOL_RATE").



REF = NDF (Read)
````````````````
An existing NDF that is to be used to define the output grid, or the
string "JSA". If an NDF is supplied, the output grid will be aligned
with the supplied reference NDF. The reference can be either 2D or 3D
and the spatial frame will be extracted. If "JSA" is supplied, the JSA
all-sky pixel grid will be used (note, the map will still be created
as a single NDF - if multiple NDFs, one for each JSA tile, are
required, the "JSATILES" parameter should beset TRUE instead of using
the "REF" parameter). If a null (!) value is supplied then the output
grid is determined by parameters REFLON, REFLAT, etc. In addition,
this NDF can be used to mask the AST, FLT or COM model. See
configuration parameters AST.ZERO_MASK, FLT.ZERO_MASK and
COM.ZERO_MASK. [!]



REFLAT = LITERAL (Read)
```````````````````````
The formatted celestial latitude value at the tangent point of the
spatial projection in the output cube. This should be provided in the
coordinate system specified by parameter SYSTEM.



REFLON = LITERAL (Read)
```````````````````````
The formatted celestial longitude value at the tangent point of the
spatial projection in the output cube. This should be provided in the
system specified by parameter SYSTEM.



RESIST = GROUP (Read)
`````````````````````
A group expression containing the resistor settings for each
bolometer. Usually specified as a text file using "^" syntax. An
example can be found in $STARLINK_DIR/share/smurf/resist.cfg
[$STARLINK_DIR/share/smurf/resist.cfg]



RESPMASK = _LOGICAL (Read)
``````````````````````````
If true, responsivity data will be used to mask bolometer data when
calculating the flatfield. [TRUE]



SPREAD = LITERAL (Read)
```````````````````````
The method to use when spreading each input pixel value out between a
group of neighbouring output pixels if using METHOD=REBIN (for
METHOD=ITERATE nearest-neighbour resampling is always used). If SPARSE
is set TRUE, then SPREAD is not accessed and a value of "Nearest" is
always assumed. SPREAD can take the following values:


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
The celestial coordinate system for the output cube. One of ICRS,
GAPPT, FK5, FK4, FK4-NO-E, AZEL, GALACTIC, ECLIPTIC. It can also be
given the value "TRACKING", in which case the system used will be
which ever system was used as the tracking system during the
observation. The supplied value is ignored if a value is supplied for
parameter "REF".
The choice of system also determines if the telescope is considered to
be tracking a moving object such as a planet or asteroid. If the
system is GAPPT or AZEL, then each time slice in the input data will
be shifted in order to put the base telescope position (given by
TCS_AZ_BC1/2 in the JCMTSTATE extension of the input NDF) at the same
pixel position that it had for the first time slice. For any other
system, no such shifts are applied, even if the base telescope
position is changing through the observation. [TRACKING]



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
The number of tiles used to cover the entire output array is written
to output parameter NTILES. The tiles all share the same projection
and so can be simply pasted together in pixel coordinates to
reconstruct the full size output array. The tiles are centred so that
the reference position (given by REFLON and REFLAT) falls at the
centre of a tile. If a tile receives no input data, then no
corresponding output NDF is created, but the tile is still included in
the tile numbering scheme. If a null (!) value is supplied for
TILEDIMS, then the entire output array is created as a single tile and
stored in a single output NDF with the name given by parameter OUT
(without any "_<N>" appendix). [!]



TRIM = _LOGICAL (Read)
``````````````````````
If TRUE, then the output image is trimmed to remove any border of bad
pixels. [FALSE]



TRIMTILES = _LOGICAL (Read)
```````````````````````````
Only accessed if the output is being split up into more than one
spatial tile (see parameter TILEDIMS and JSATILES). If TRUE, then the
tiles around the border will be trimmed to exclude areas that fall
outside the bounds of the full sized output array. This will result in
the border tiles being smaller than the central tiles. [FALSE]



UBND( 2 ) = _INTEGER (Read)
```````````````````````````
An array of values giving the upper pixel index bound on each spatial
axis of the output NDF. The suggested default values encompass all the
input spatial information. The supplied values may be modified if TRIM
is set TRUE. []



UBOUND( 2 ) = _INTEGER (Write)
``````````````````````````````
The upper pixel bounds of the output NDF. Note, values will be written
to this output parameter even if a null value is supplied for
parameter OUT.



Notes
~~~~~


+ If multiple masks are specified for a single model component, then
the source areas of the individual masks are combined together to form
the total mask. For instance, if values are supplied for both
AST.ZERO_MASK and AST.ZERO_LOWHITS, then a pixel in the total mask
will be considered to be a "source" pixel if it is a source pixel in
either the external mask specified by AST.ZERO_MASK, or in the "low
hits" mask.
+ The iterative algorithm can be terminated prematurely by pressing
control-C at any time. If this is done, the current iteration will
complete and the user will then be asked how to continue. Options
include: 1) abort immediately without an output map, 2) close
retaining the current unfinalised output map, and 3) perform one more
iteration to finalise the map and then close. Note, if control-C is
pressed a second time, the application will abort immediately,
potentially leaving files in an unclean state.
+ A FITS extension is added to the output NDF containing any keywords
that are common to all input NDFs. To be included in the output FITS
extension, a FITS keyword must be present in the NDF extension of
every input NDF, and it must have the same value in all input NDFs. In
addition, certain headers that relate to start and end events are
propogated from the oldest and newest files respectively.
+ The output NDF will contain an extension named "SMURF" containing an
NDF named "EXP_TIME", which contains the exposure time associated with
each pixel.
+ The FITS keyword EXP_TIME is added to the output FITS extension.
This header contains the median value of the EXP_TIME array (stored in
the SMURF extension of the output NDF).If this value cannot be
calculated for any reason, the corresponding FITS keyword is assigned
a blank value.
+ If parameter TILEDIMS is assigned a value, FITS keywords NUMTILES
and TILENUM are added to the output FITS header. These are the number
of tiles used to hold the output data, and the index of the NDF
containing the header, in the range 1 to NUMTILES, but if JSATILES is
TRUE then FITS keyword TILENUM is also added but is instead used for
the JSA tile number in the range 0 to 12 * Nside ^ 2 - 1.
+ The model configuration parameters can be sub-instrument dependent.
For example, 850.flt.edgelow will copy the edgelow value into the flt
section only for 850 micron data. Similarly for 450.flt.edgelow.
+ Default values can be read from the $SMURF_DIR/smurf_makemap.def
  file.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: QLMAKEMAP


Copyright
~~~~~~~~~
Copyright (C) 2005-2007 Particle Physics and Astronomy Research
Council. Copyright (C) 2005-2010,2013 University of British Columbia.
Copyright (C) 2007-2012 Science and Technology Facilities Council.
Copyright (C) 2017 East Asian Observatory. All Rights Reserved.


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


