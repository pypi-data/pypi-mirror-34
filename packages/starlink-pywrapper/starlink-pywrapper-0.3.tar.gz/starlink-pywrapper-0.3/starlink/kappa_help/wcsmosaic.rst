

WCSMOSAIC
=========


Purpose
~~~~~~~
Tiles a group of NDFs using World Co-ordinate System information


Description
~~~~~~~~~~~
This application aligns and rebins a group of input NDFs into a single
output NDF. It differs from WCSALIGN in both the algorithm used, and
in the requirements placed on the input NDFs. WCSMOSAIC requires that
the transformation from pixel to WCS co-ordinates be defined in each
input NDF, but (unlike WCSALIGN) the inverse transformation from WCS
to pixel co-ordinates need not be defined. For instance, this means
that WCSMOSAIC can process data in which the WCS position of each
input pixel is defined via a look-up table rather than an analytical
expression. Note however, that the WCS information in the reference
NDF (see Parameter REF) must have a defined inverse transformation.
The WCSMOSAIC algorithm proceeds as follows. First, the output NDF is
filled with zeros. An associated array of weights (one weight for each
output pixel) is created and is also filled with zeros. Each input NDF
is then processed in turn. For each pixel in the current input NDF,
the corresponding transformed position in the output NDF is found
(based on the WCS information in both NDFs). The input pixel value is
then divided up between a small group of output pixels centred on this
central output position. The method used for choosing the fraction of
the input pixel value assigned to each output pixel is determined by
the METHOD and PARAMS parameters. Each of the affected output pixel
values is then incremented by its allocated fraction of the input
pixel value. The corresponding weight values are incremented by the
fractions used (that is, if 0.25 of an input pixel is assigned to an
output pixel, the weight for the output pixel is incremented by 0.25).
Once all pixels in the current input NDF have been rebinned into the
output NDF in this way, the algorithm proceeds to rebin the next input
NDF in the same way. Once all input NDFs have been processed, output
pixels which have a weight less than the value given by Parameter WLIM
are set bad. The output NDF may then optionally (see Parameter NORM)
be normalised by dividing it by the weights array. This normalisation
of the output NDF takes account of any difference in the number of
pixels contributing to each output pixel, and also removes artefacts
which may be produced by aliasing between the input and output pixel
grids. Thus each output pixel value is a weighted mean of the input
pixel values from which it receives contributions. This means that the
units of the output NDF are the same as the input NDF. In particular,
any difference between the input and output pixel sizes is ignored,
resulting in the total input data sum being preserved only if the
input and output NDFs have equal pixel\ sizes. However, an option
exists to scale the input values before use so that the total data sum
in each input NDF is preserved even if the input and output pixel
sizes differ (see Parameter CONSERVE).
If the input NDFs contain variances, then these are propagated to the
output. Alternatively, output variances can be generated from the
spread of input values contributing to each output pixel (see
Parameter GENVAR). Any input variances can also be used to weight the
input data (see Parameter VARIANCE). By default, all input data is
given equal weight. An additional weight for each NDF can be specified
using parameter WEIGHTS.
The transformations needed to produce alignment are derived from the
co-ordinate system information stored in the WCS components of the
supplied NDFs. For each input NDF, alignment is first attempted in the
current co-ordinate Frame of the reference NDF. If this fails,
alignment is attempted in the current co-ordinate Frame of the input
NDF. If this fails, alignment occurs in the pixel co-ordinate Frame. A
message indicating which Frame alignment was achieved in is displayed.


Usage
~~~~~


::

    
       wcsmosaic in out lbnd ubnd ref
       



ADAM parameters
~~~~~~~~~~~~~~~



ACC = _REAL (Read)
``````````````````
The positional accuracy required, as a number of pixels. For highly
non-linear projections, a recursive algorithm is used in which
successively smaller regions of the projection are fitted with a
least-squares linear transformation. If such a transformation results
in a maximum positional error greater than the value supplied for ACC
(in pixels), then a smaller region is used. High accuracy is paid for
by longer run times. [0.05]



ALIGNREF = _LOGICAL (Read)
``````````````````````````
Determines the coordinate system in which each input NDF is aligned
with the reference NDF. If TRUE, alignment is performed in the
coordinate system described by the current Frame of the WCS FrameSet
in the reference NDF. If FALSE, alignment is performed in the
coordinate system specified by the following set of WCS attributes in
the reference NDF: AlignSystem AlignStdOfRest, AlignOffset,
AlignSpecOffset, AlignSideBand, AlignTimeScale. The AST library
provides fixed defaults for all these. So for instance, AlignSystem
defaults to ICRS for celestial axes and Wavelength for spectral axes,
meaning that celestial axes will be aligned in ICRS and spectral axes
in wavelength, by default. Similarly, AlignStdOfRest defaults to
Heliocentric, meaning that by default spectral axes will be aligned in
the Heliocentric rest frame.
As an example, if you are mosaicing two spectra which both use radio
velocity as the current WCS, but which have different rest
frequencies, then setting ALIGNREF to TRUE will cause alignment to be
performed in radio velocity, meaning that the differences in rest
frequency are ignored. That is, a channel with 10 Km/s in the input is
mapping onto the channel with 10 km/s in the output. If ALIGNREF is
FALSE (and no value has been set for the AlignSystem attribute in the
reference WCS), then alignment will be performed in wavelength,
meaning that the different rest frequencies cause an additional shift.
That is, a channel with 10 Km/s in the input will be mapping onto
which ever output channel has the same wavelength, taking into account
the different rest frequencies.
As another example, consider mosaicing two maps which both have
(azimuth,elevation) axes. If ALIGNREF is TRUE, then any given (az,el)
values in one image will be mapped onto the exact same (az,el) values
in the other image, regardless of whether the two images were taken at
the same time. But if ALIGNREF is FALSE, then a given (az,el) value in
one image will be mapped onto pixel that has the same ICRS coordinates
in the other image (since AlignSystem default to ICRS for celestial
axes). Thus any different in the observation time of the two images
will result in an additional shift.
As yet another example, consider mosaicing two spectra which are both
in frequency with respect to the LSRK, but which refer to different
points on the sky. If ALIGNREF is TRUE, then a given LSRK frequency in
one spectra will be mapped onto the exact same LSRK frequency in the
other image, regardless of the different sky positions. But if
ALIGNREF is FALSE, then a given input frequency will first be
converted to Heliocentric frequency (the default value for
AlignStdOfRest is "Heliocentric"), and will be mapped onto the output
channel that has the same Heliocentric frequency. Thus the differecen
in sky positions will result in an additional shift. [FALSE]



CONSERVE = _LOGICAL (Read)
``````````````````````````
If set TRUE, then the output pixel values will be scaled in such a way
as to preserve the total data value in a feature on the sky. The
scaling factor is the ratio of the output pixel size to the input
pixel size. This option can only be used if the Mapping is
successfully approximated by one or more linear transformations. Thus
an error will be reported if it used when the ACC parameter is set to
zero (which stops the use of linear approximations), or if the Mapping
is too non-linear to be approximated by a piece-wise linear
transformation. The ratio of output to input pixel size is evaluated
once for each panel of the piece-wise linear approximation to the
Mapping, and is assumed to be constant for all output pixels in the
panel. This parameter is ignored if the NORM parameter is set FALSE.
[TRUE]



FLBND( ) = _DOUBLE (Write)
``````````````````````````
The lower bounds of the bounding box enclosing the output NDF in the
current WCS Frame. The number of elements in this parameter is equal
to the number of axes in the current WCS Frame. Celestial axis values
will be in units of radians.



FUBND( ) = _DOUBLE (Write)
``````````````````````````
The upper bounds of the bounding box enclosing the output NDF in the
current WCS Frame. The number of elements in this parameter is equal
to the number of axes in the current WCS Frame. Celestial axis values
will be in units of radians.



GENVAR = _LOGICAL (Read)
````````````````````````
If TRUE, output variances are generated based on the spread of input
pixel values contributing to each output pixel. Any input variances
then have no effect on the output variances (although input variances
will still be used to weight the input data if the VARIANCE parameter
is set TRUE). If GENVAR is set FALSE, the output variances are based
on the variances in the input NDFs, so long as all input NDFs contain
variances (otherwise the output NDF will not contain any Variances).
If a null (!) value is supplied, then a value of FALSE is adopted if
and only if all the input NDFs have variance components (TRUE is used
otherwise). [FALSE]



IN = NDF (Read)
```````````````
A group of input NDFs (of any dimensionality). This should be given as
a comma-separated list, in which each list element can be one of the
following options.


+ An NDF name, optionally containing wild-cards and/or regular
expressions ("*", "?", "[a-z]" etc.).
+ The name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  wild-cards, etc.), or another file specification (preceded by an up-
  arrow). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a hyphen, then you
are re-prompted for further input until a value is given which does
not end with a hyphen. All the NDFs given in this way are concatenated
into a single group.



LBND() = _INTEGER (Read)
````````````````````````
An array of values giving the lower pixel-index bound on each axis for
the output NDF. The suggested default values just encompass all the
input data. A null value (!) also results in these same defaults being
used. [!]



LBOUND() = _INTEGER (Write)
```````````````````````````
The lower pixel bounds of the output NDF. Note, values will be written
to this output parameter even if a null value is supplied for
Parameter OUT.



MAXPIX = _INTEGER (Read)
````````````````````````
A value which specifies an initial scale size in pixels for the
adaptive algorithm which approximates non-linear Mappings with piece-
wise linear transformations. If MAXPIX is larger than any dimension of
the region of the output grid being used, a first attempt will be made
to approximate the Mapping by a linear transformation over the entire
output region. If a smaller value is used, the output region will
first be divided into subregions whose size does not exceed MAXPIX
pixels in any dimension, and then attempts will be made at
approximation. [1000]



METHOD = LITERAL (Read)
```````````````````````
The method to use when dividing an input pixel value between a group
of neighbouring output pixels. For details on these schemes, see the
description of AST_REBINx in SUN/210. METHOD can take the following
values.


+ "Bilinear" -- The input pixel value is divided bi-linearly between
the four nearest output pixels. This produces smoother output NDFs
than the nearest-neighbour scheme, but is marginally slower.
+ "Nearest" -- The input pixel value is assigned completely to the
single nearest output pixel.
+ "Sinc" -- Uses the sinc(pi*x) kernel, where x is the pixel offset
from the transformed input pixel centre, and sinc(z)=sin(z)/z. Use of
this scheme is not recommended.
+ "SincSinc" -- Uses the sinc(pi*x)sinc(k*pi*x) kernel. This is a
valuable general-purpose scheme, intermediate in its visual effect on
NDFs between the bilinear and nearest-neighbour schemes.
+ "SincCos" -- Uses the sinc(pi*x)cos(k*pi*x) kernel. It gives similar
results to the "Sincsinc" scheme.
+ "SincGauss" -- Uses the sinc(pi*x)exp(-k*x*x) kernel. Good results
can be obtained by matching the FWHM of the envelope function to the
point-spread function of the input data (see Parameter PARAMS).
+ "Somb" -- Uses the somb(pi*x) kernel, where somb(z)=2*J1(z)/z (J1 is
the first-order Bessel function of the first kind). This scheme is
similar to the "Sinc" scheme.
+ "SombCos" -- Uses the somb(pi*x)cos(k*pi*x) kernel. This scheme is
similar to the "SincCos" scheme.
+ "Gauss" -- Uses the exp(-k*x*x) kernel. The FWHM of the Gaussian is
  given by Parameter PARAMS(2), and the point at which to truncate the
  Gaussian to zero is given by Parameter PARAMS(1).

All methods propagate variances from input to output, but the variance
estimates produced by schemes other than nearest neighbour need to be
treated with care since the spatial smoothing produced by these
methods introduces correlations in the variance estimates. Also, the
degree of smoothing produced varies across the NDF. This is because a
sample taken at a pixel centre will have no contributions from the
neighbouring pixels, whereas a sample taken at the corner of a pixel
will have equal contributions from all four neighbouring pixels,
resulting in greater smoothing and lower noise. This effect can
produce complex Moire patterns in the output variance estimates,
resulting from the interference of the spatial frequencies in the
sample positions and in the pixel-centre positions. For these reasons,
if you want to use the output variances, you are generally safer using
nearest-neighbour interpolation. The initial default is "SincSinc".
[current value]



NORM = _LOGICAL (Read)
``````````````````````
In general, each output pixel contains contributions from multiple
input pixel values, and the number of input pixels contributing to
each output pixel will vary from pixel to pixel. If NORM is set TRUE
(the default), then each output value is normalised by dividing it by
the number of contributing input pixels, resulting in each output
value being the weighted mean of the contibuting input values.
However, if NORM is set FALSE, this normalisation is not applied. See
also Parameter CONSERVE. Setting NORM to FALSE and VARIANCE to TRUE
results in an error being reported. [TRUE]



OUT = NDF (Write)
`````````````````
The output NDF. If a null (!) value is supplied, WCSMOSAIC will
terminate early without creating an output cube, but without reporting
an error. Note, the pixel bounds which the output cube would have had
will still be written to output Parameters LBOUND and UBOUND, even if
a null value is supplied for OUT.



PARAMS( 2 ) = _DOUBLE (Read)
````````````````````````````
An optional array which consists of additional parameters required by
the Sinc, SincSinc, SincCos, SincGauss, Somb, SombCos and Gauss
methods.
PARAMS( 1 ) is required by all the above schemes. It is used to
specify how many output pixels on either side of the central output
pixel are to receive contribution from the corresponding input pixel.
Typically, a value of 2 is appropriate and the minimum allowed value
is 1 (i.e. one pixel on each side). A value of zero or fewer indicates
that a suitable number of pixels should be calculated automatically.
[0]
PARAMS( 2 ) is required only by the Gauss, SombCos, SincSinc, SincCos,
and SincGauss schemes. For the SombCos, SincSinc and SincCos schemes,
it specifies the number of output pixels at which the envelope of the
function goes to zero. The minimum value is 1.0, and the run-time
default value is 2.0. For the Gauss and SincGauss scheme, it specifies
the full-width at half-maximum (FWHM) of the Gaussian envelope
measured in output pixels. The minimum value is 0.1, and the run-time
default is 1.0. []



REF = NDF (Read)
````````````````
The NDF to which all the input NDFs are to be aligned. If a null value
is supplied for this parameter, the first NDF supplied for Parameter
IN is used. The WCS information in this NDF must have a defined
inverse transformation (from WCS co-ordinates to pixel co-ordinates).
[!]



UBND() = _INTEGER (Read)
````````````````````````
An array of values giving the upper pixel-index bound on each axis for
the output NDF. The suggested default values just encompass all the
input data. A null value (!) also results in these same defaults being
used. [!]



UBOUND() = _INTEGER (Write)
```````````````````````````
The upper pixel bounds of the output NDF. Note, values will be written
to this output parameter even if a null value is supplied for
Parameter OUT.



VARIANCE = _LOGICAL (Read)
``````````````````````````
If TRUE, then any input VARIANCE components in the input NDFs are used
to weight the input data (the weight used for each data value is the
reciprocal of the variance). If FALSE, all input data is given equal
weight. Note, some applications (such as CCDPACK:MAKEMOS) use a
parameter named USEVAR to determine both whether input variances are
used to weights input data values, and also how to calculate output
variances. However, WCSMOSAIC uses the VARIANCE parameter only for the
first of these purposes (determining whether to weight the input
data). The second purpose (determining how to create output variances)
is fulfilled by the GENVAR parameter. [FALSE]



WEIGHTS = LITERAL (Read)
````````````````````````
An optional group of numerical weights, one for each of the input NDFs
specified by parameter IN. If VARIANCE is TRUE, the weight assigned to
each input pixel is the value supplied in this group correspoinding to
the appropriate input NDF, divided by the variance of the pixel value.
An error is reported if the number of supplied weights does not equal
the number of supplied input NDFs. [!]



WLIM = _REAL (Read)
```````````````````
This parameter specifies the minimum number of good pixels that must
contribute to an output pixel for the output pixel to be valid. Note,
fractional values are allowed. If a value less than 1.0E-10 is
supplied, a value of 1.0E-10 is used. [1.0E-10]



Examples
~~~~~~~~
wcsmosaic m51* mosaic lbnd=! accept
This example rebins all the NDFs with names starting with the string
"m51" in the current directory so that they are aligned with the first
input NDF, and combines them all into a single output NDF called
mosaic. The output NDF is just big enough to contain all the pixels in
all the input NDFs.



Notes
~~~~~


+ WCS information (including the current co-ordinate Frame) is
propagated from the reference NDF to the output NDF. All other
information is propagated form the first input NDF.
+ The QUALITY and AXIS components are not propagated from input to
output.
+ There are different facts reported, their verbosity depending on the
  current message-reporting level set by environment variable
  MSG_FILTER. If this is set to QUIET, no information will be displayed
  while the command is executing. When the filtering level is at least
  as verbose as NORMAL, the interpolation method being used will be
  displayed. If set to VERBOSE, the name of each input NDF will also be
  displayed as it is processed.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSFRAME, WCSALIGN, REGRID; CCDPACK: TRANNDF.


Copyright
~~~~~~~~~
Copyright (C) 2005-2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2007-2009 Science & Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA, VARIANCE, LABEL, TITLE,
UNITS, WCS, and HISTORY components of the input NDFs (see the METHOD
parameter for notes on the interpretation of output variances).
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled, but the data type
  will be converted to one of _INTEGER, _DOUBLE or _REAL for processing.




