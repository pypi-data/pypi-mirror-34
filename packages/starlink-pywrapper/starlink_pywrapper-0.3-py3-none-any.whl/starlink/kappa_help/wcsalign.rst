

WCSALIGN
========


Purpose
~~~~~~~
Aligns a group of NDFs using World Co-ordinate System information


Description
~~~~~~~~~~~
This application resamples or rebins a group of input NDFs, producing
corresponding output NDFs which are aligned pixel-for-pixel with a
specified reference NDF, or POLPACK catalogue (see parameter REFCAT).
If an input NDF has more pixel axes than the reference NDF, then the
extra pixel axes are retained unchanged in the output NDF. Thus, for
instance, if an input RA/Dec/velocity cube is aligned with a reference
two-dimensional galactic-longitude/latitude image, the output NDF will
be a galactic-longitude/latitude/ velocity cube.
The transformations needed to produce alignment are derived from the
co-ordinate system information stored in the WCS components of the
supplied NDFs. For each input NDF, alignment is first attempted in the
current co-ordinate Frame of the reference NDF. If this fails,
alignment is attempted in the current co-ordinate Frame of the input
NDF. If this fails, alignment occurs in the pixel co-ordinate Frame. A
message indicating which Frame alignment was achieved in is displayed.
Two algorithms are available for determining the output pixel values:
resampling and rebinning (the method used is determined by the REBIN
parameter).
Two methods exist for determining the bounds of the output NDFs. First
you can give values for Parameters LBND and UBND which are then used
as the pixel index bounds for all output NDFs. Second, if a null value
is given for LBND or UBND, default values are generated separately for
each output NDF so that the output NDF just encloses the entire area
covered by the corresponding input NDF. Using the first method will
ensure that all output NDFs have the same pixel origin, and so the
resulting NDFs can be directly compared. However, this may result in
the output NDFs being larger than necessary. In general, the second
method results in smaller NDFs being produced, in less time. However,
the output NDFs will have differing pixel origins which need to be
taken into account when comparing the aligned NDFs.


Usage
~~~~~


::

    
       wcsalign in out lbnd ubnd ref
       



ADAM parameters
~~~~~~~~~~~~~~~



ABORT = _LOGICAL (Read)
```````````````````````
This controls what happens if an error occurs whilst processing one of
the input NDFs. If a FALSE value is supplied for ABORT, then the error
message will be displayed, but the application will attempt to process
any remaining input NDFs. If a TRUE value is supplied for ABORT, then
the error message will be displayed, and the application will abort.
[FALSE]



ACC = _REAL (Read)
``````````````````
The positional accuracy required, as a number of pixels. For highly
non-linear projections, a recursive algorithm is used in which
successively smaller regions of the projection are fitted with a
least-squares linear transformation. If such a transformation results
in a maximum positional error greater than the value supplied for ACC
(in pixels), then a smaller region is used. High accuracy is paid for
by larger run times. A value of zero prevents any linear
approximations being used - each pixel position is transformed
explicitly. [0.05]



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
As an example, if you are aligning two spectra which both use radio
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
As another example, consider aligning two maps which both have
(azimuth,elevation) axes. If ALIGNREF is TRUE, then any given (az,el)
values in one image will be mapped onto the exact same (az,el) values
in the other image, regardless of whether the two images were taken at
the same time. But if ALIGNREF is FALSE, then a given (az,el) value in
one image will be mapped onto pixel that has the same ICRS coordinates
in the other image (since AlignSystem default to ICRS for celestial
axes). Thus any different in the observation time of the two images
will result in an additional shift.
As yet another example, consider aligning two spectra which are both
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
panel. The dynamic default is TRUE if rebinning, and FALSE if
resampling (see Parameter REBIN). []



IN = NDF (Read)
```````````````
A group of input NDFs (of any dimensionality). This should be given as
a comma-separated list, in which each list element can be:


+ an NDF name, optionally containing wild-cards and/or regular
expressions ("*", "?", "[a-z]" etc.).
+ the name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  wild-cards, etc.), or another file specification (preceded by an up-
  arrow). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a minus sign "-",
then you are re-prompted for further input until a value is given
which does not end with a hyphen. All the NDFs given in this way are
concatenated into a single group.



INSITU = _LOGICAL (Read)
````````````````````````
If INSITU is set to TRUE, then no output NDFs are created. Instead,
the pixel origin of each input NDF is modified in order to align the
input NDFs with the reference NDF (which is a much faster operation
than a full resampling). This can only be done if the mapping from
input pixel co-ordinates to reference pixel co-ordinates is a simple
integer pixel shift of origin. If this is not the case an error will
be reported when the input is processed (what happens then is
controlled by the ABORT parameter). Also, in-situ alignment is only
possible if null values are supplied for LBND and UBND. [FALSE]



LBND() = _INTEGER (Read)
````````````````````````
An array of values giving the lower pixel index bound on each axis for
the output NDFs. The number of values supplied should equal the number
of axes in the reference NDF. The given values are used for all output
NDFs. If a null value (!) is given for this parameter or for Parameter
UBND, then separate default values are calculated for each output NDF
which result in the output NDF just encompassing the corresponding
input NDF. The suggested defaults are the lower pixel-index bounds
from the reference NDF, if supplied (see Parameter REF).



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
The method to use when sampling the input pixel values (if
resampling), or dividing an input pixel value between a group of
neighbouring output pixels (if rebinning). For details on these
schemes, see the descriptions of routines AST_RESAMPLEx and AST_REBINx
in SUN/210. METHOD can take the following values.


+ "Bilinear" -- When resampling, the output pixel values are
calculated by bi-linear interpolation among the four nearest pixels
values in the input NDF. When rebinning, the input pixel value is
divided bi-linearly between the four nearest output pixels. Produces
smoother output NDFs than the nearest-neighbour scheme, but is
marginally slower.
+ "Nearest" -- When resampling, the output pixel values are assigned
the value of the single nearest input pixel. When rebinning, the input
pixel value is assigned completely to the single nearest output pixel.
+ "Sinc" -- Uses the sinc(pi*x) kernel, where x is the pixel offset
from the interpolation point (resampling) or transformed input pixel
centre (rebinning), and sinc(z)=sin(z)/z. Use of this scheme is not
recommended.
+ "SincSinc" -- Uses the sinc(pi*x)sinc(k*pi*x) kernel. A valuable
general-purpose scheme, intermediate in its visual effect on NDFs
between the bilinear and nearest-neighbour schemes.
+ "SincCos" -- Uses the sinc(pi*x)cos(k*pi*x) kernel. Gives similar
results to the "Sincsinc" scheme.
+ "SincGauss" -- Uses the sinc(pi*x)exp(-k*x*x) kernel. Good results
can be obtained by matching the FWHM of the envelope function to the
point-spread function of the input data (see Parameter PARAMS).
+ "Somb" -- Uses the somb(pi*x) kernel, where x is the pixel offset
from the interpolation point (resampling) or transformed input pixel
centre (rebinning), and somb(z)=2*J1(z)/z (J1 is the first-order
Bessel function of the first kind. This scheme is similar to the
"Sinc" scheme.
+ "SombCos" -- Uses the somb(pi*x)cos(k*pi*x) kernel. This scheme is
similar to the "SincCos" scheme.
+ "Gauss" -- Uses the exp(-k*x*x) kernel. The FWHM of the Gaussian is
  given by Parameter PARAMS(2), and the point at which to truncate the
  Gaussian to zero is given by Parameter PARAMS(1).

All methods propagate variances from input to output, but the variance
estimates produced by interpolation schemes other than nearest
neighbour need to be treated with care since the spatial smoothing
produced by these methods introduces correlations in the variance
estimates. Also, the degree of smoothing produced varies across the
NDF. This is because a sample taken at a pixel centre will have no
contributions from the neighbouring pixels, whereas a sample taken at
the corner of a pixel will have equal contributions from all four
neighbouring pixels, resulting in greater smoothing and lower noise.
This effect can produce complex Moire patterns in the output variance
estimates, resulting from the interference of the spatial frequencies
in the sample positions and in the pixel centre positions. For these
reasons, if you want to use the output variances, you are generally
safer using nearest-neighbour interpolation. The initial default is
"SincSinc". [current value]



OUT = NDF (Write)
`````````````````
A group of output NDFs corresponding one-for-one with the list of
input NDFs given for Parameter IN. This should be given as a comma-
separated list, in which each list element can be:


+ an NDF name. If the name contains an asterisk character "*", the
name of the corresponding input NDF (without directory or file suffix)
is substituted for the asterisk (for instance, "*_al" causes the
output NDF name to be formed by appending the string "_al" to the
corresponding input NDF name). Input NDF names can also be edited by
including original and replacement strings between vertical bars after
the NDF name (for instance, *_al|b4|B1| causes any occurrence of the
string "B4" in the input NDF name to be replaced by the string "B1"
before appending the string "_al" to the result).
+ the name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  editing, etc), or another file specification (preceded by an up-
  arrow). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a hyphen "-", then
you are re-prompted for further input until a value is given which
does not end with a hyphen. All the NDFs given in this way are
concatenated into a single group.
This parameter is only accessed if the INSITU parameter is FALSE.



PARAMS( 2 ) = _DOUBLE (Read)
````````````````````````````
An optional array which consists of additional parameters required by
the Sinc, SincSinc, SincCos, SincGauss, Somb, SombCos and Gauss
methods.
PARAMS( 1 ) is required by all the above schemes. It is used to
specify how many pixels are to contribute to the interpolated result
on either side of the interpolation or binning point in each
dimension. Typically, a value of 2 is appropriate and the minimum
allowed value is 1 (i.e. one pixel on each side). A value of zero or
fewer indicates that a suitable number of pixels should be calculated
automatically. [0]
PARAMS( 2 ) is required only by the Gauss, SombCos, SincSinc, SincCos,
and SincGauss schemes. For the SombCos, SincSinc and SincCos schemes,
it specifies the number of pixels at which the envelope of the
function goes to zero. The minimum value is 1.0, and the run-time
default value is 2.0. For the Gauss and SincGauss scheme, it specifies
the full-width at half-maximum (FWHM) of the Gaussian envelope
measured in output pixels. The minimum value is 0.1, and the run-time
default is 1.0. On astronomical NDFs and spectra, good results are
often obtained by approximately matching the FWHM of the envelope
function, given by PARAMS(2), to the point-spread function of the
input data. []



REBIN = _LOGICAL (Read)
```````````````````````
Determines the algorithm used to calculate the output pixel values. If
a TRUE value is given, a rebinning algorithm is used. Otherwise, a
resampling algorithm is used. See the "Choice of Algorithm" topic
below. The initial default is FALSE. [current value]



REF = NDF (Read)
````````````````
The NDF to which all the input NDFs are to be aligned. If a null value
is supplied for this parameter, the first NDF supplied for Parameter
IN is used. This parameter is only used if no catalogue is supplied
for parameter REFCAT.



REFCAT = NDF (Read)
```````````````````
A POLPACK catalogue defining the WCS to which all the input NDFs are
to be aligned. If a null value is supplied for this parameter, the WCS
will be obtained from an NDF using parameter REF. [!]



UBND() = _INTEGER (Read)
````````````````````````
An array of values giving the upper pixel-index bound on each axis for
the output NDFs. The number of values supplied should equal the number
of axes in the reference NDF. The given values are used for all output
NDFs. If a null value (!) is given for this parameter or for Parameter
LBND, then separate default values are calculated for each output NDF
which result in the output NDF just encompassing the corresponding
input NDF. The suggested defaults are the upper pixel-index bounds
from the reference NDF, if supplied (see Parameter REF).



WLIM = _REAL (Read)
```````````````````
This parameter is only used if REBIN is set TRUE. It specifies the
minimum number of good pixels which must contribute to an output pixel
for the output pixel to be valid. Note, fractional values are allowed.
A null (!) value causes a very small positive value to be used
resulting in output pixels being set bad only if they receive no
significant contribution from any input pixel. [!]



Examples
~~~~~~~~
wcsalign image1 image1_al ref=image2 accept
This example resamples the NDF called image1 so that it is aligned
with the NDF call image2, putting the output in image1_al. The output
image has the same pixel-index bounds as image2 and inherits WCS
information from image2.
wcsalign m51* *_al lbnd=! accept
This example resamples all the NDFs with names starting with the
string "m51" in the current directory so that they are aligned with
the first input NDF. The output NDFs have the same names as the input
NDFs, but extended with the string "_al". Each output NDF is just big
enough to contain all the pixels in the corresponding input NDF.
wcsalign ^in.lis ^out.lis lbnd=! accept
This example is like the previous example, except that the names of
the input NDFs are read from the text file in.lis, and the names of
the corresponding output NDFs are read from text file out.lis.



Notes
~~~~~


+ WCS information (including the current co-ordinate Frame) is
propagated from the reference NDF to all output NDFs.
+ QUALITY is propagated from input to output only if Parameter METHOD
  is set to "Nearest" and REBIN is set to FALSE.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSFRAME, REGRID; CCDPACK: TRANNDF.


Choice of Algorithm
~~~~~~~~~~~~~~~~~~~
The algorithm used to produce the output images is determined by the
REBIN parameter, and is based either on resampling the output image or
rebinning the corresponding input image.
The resampling algorithm steps through every pixel in the output
image, sampling the input image at the corresponding position and
storing the sampled input value in the output pixel. The method used
for sampling the input image is determined by the METHOD parameter.
The rebinning algorithm steps through every pixel in the input image,
dividing the input pixel value between a group of neighbouring output
pixels, incrementing these output pixel values by their allocated
share of the input pixel value, and finally normalising each output
value by the total number of contributing input values. The way in
which the input sample is divided between the output pixels is
determined by the METHOD parameter.
Both algorithms produce an output in which the each pixel value is the
weighted mean of the near-by input values, and so do not alter the
mean pixel values associated with a source, even if the pixel size
changes. Thus the total data sum in a source will change if the input
and output pixel sizes differ. However, if the CONSERVE parameter is
set TRUE, the output values are scaled by the ratio of the output to
input pixel size, so that the total data sum in a source is preserved.
A difference between resampling and rebinning is that resampling
guarantees to fill the output image with good pixel values (assuming
the input image is filled with good input pixel values), whereas holes
can be left by the rebinning algorithm if the output image has smaller
pixels than the input image. Such holes occur at output pixels which
receive no contributions from any input pixels, and will be filled
with the value zero in the output image. If this problem occurs the
solution is probably to change the width of the pixel spreading
function by assigning a larger value to PARAMS(1) and/or PARAMS(2)
(depending on the specific METHOD value being used).
Both algorithms have the capability to introduce artefacts into the
output image. These have various causes described below.


+ Particularly sharp features in the input can cause rings around the
corresponding features in the output image. This can be minimised by
suitable settings for the METHOD and PARAMS parameters. In general
such rings can be minimised by using a wider interpolation kernel (if
resampling) or spreading function (if rebinning), at the cost of
degraded resolution.
+ The approximation of the Mapping using a piece-wise linear
  transformation (controlled by paremeter ACC) can produce artefacts at
  the joints between the panels of the approximation. They are caused by
  the discontinuities between the adjacent panels of the approximation,
  and can be minimised by reducing the value assigned to the ACC
  parameter.




Copyright
~~~~~~~~~
Copyright (C) 1998-1999, 2001-2002, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2005 Particle Physics & Astronomy
Research Council. Copyright (C) 2011-2012 Science & Technology
Facilities Council. All Rights Reserved.


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
+ All non-complex numeric data types can be handled. If REBIN is TRUE,
  the data type will be converted to one of _INTEGER, _DOUBLE or _REAL
  for processing.




