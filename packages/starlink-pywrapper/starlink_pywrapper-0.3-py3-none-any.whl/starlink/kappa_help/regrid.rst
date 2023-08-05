

REGRID
======


Purpose
~~~~~~~
Applies a geometrical transformation to an NDF


Description
~~~~~~~~~~~
This application uses a specified Mapping to re-grid the pixel
positions in an NDF. The specified Mapping should transform pixel co-
ordinates in the input NDF into the corresponding pixel co-ordinates
in the output NDF.
By default, the bounds of the output pixel grid are chosen so that
they just encompass all the transformed input data, but they can be
set explicitly using parameters LBOUND and UBOUND.
Two algorithms are available for determining the output pixel values:
resampling and rebinning (the algorithm used is determined by the
REBIN parameter).
The Mapping to use can be supplied in several different ways (see
Parameter MAPPING).


Usage
~~~~~


::

    
       regrid in out [method]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES() = _INTEGER (Read)
````````````````````````
The indices of the pixel axes that are to be re-gridded. These should
be in the range 1 to NDIM (the number of pixel axes in the NDF). Each
value may appear at most once. The order of the supplied values is
insignificant. If a null (!) value is supplied, then all pixel axes
are re-gridded. Otherwise, only the specified pixel axes are
regridded. Note, it is not always possible to specify completely
arbitrary combinations of pixel axes to be regridded. For instance, if
the current WCS Frame contains RA and Dec. axes, then it is not
possible to regrid one of the corresponding pixel axes without the
other. An error will be reported in such cases. [!]



CONSERVE = _LOGICAL (Read)
``````````````````````````
If set TRUE, then the output pixel values will be scaled in such a way
as to preserve the total data value in a feature on the sky. The
scaling factor is the ratio of the output pixel size to the input
pixel size. This option can only be used if the Mapping is
successfully approximated by one or more linear transformations. Thus
an error will be reported if it used when the TOL parameter is set to
zero (which stops the use of linear approximations), or if the Mapping
is too non-linear to be approximated by a piece-wise linear
transformation. The ratio of output to input pixel size is evaluated
once for each panel of the piece-wise linear approximation to the
Mapping, and is assumed to be constant for all output pixels in the
panel. This parameter is ignored if the NORM parameter is set FALSE.
[TRUE]



IN = NDF (Read)
```````````````
The NDF to be transformed.



LBOUND( ) = _INTEGER (Read)
```````````````````````````
The lower pixel-index bounds of the output NDF. The number of values
must be equal to the number of dimensions in the output NDF. If a null
value is supplied, default bounds will be used which are just low
enough to fit in all the transformed pixels of the input NDF. [!]



MAPPING = FILENAME (Read)
`````````````````````````
The name of a file containing the Mapping to be used, or null (!) if
the input NDF is to be mapped into its own current Frame. If a file is
supplied, the forward direction of the Mapping should transform pixel
co-ordinates in the input NDF into the corresponding pixel co-
ordinates in the output NDF. If only a subset of pixel axes are being
re-gridded, then the inputs to the Mapping should correspond to the
pixel axes specified via parameter AXES. The file may be one of the
following.


+ A text file containing a textual representation of the AST Mapping
to use. Such files can be created by WCSADD.
+ A text file containing a textual representation of an AST FrameSet.
If the FrameSet contains a Frame with Domain PIXEL, then the Mapping
used is the Mapping from the PIXEL Frame to the current Frame. If
there is no PIXEL Frame in the FrameSet, then the Mapping used is the
Mapping from the base Frame to the Current Frame.
+ A FITS file. The Mapping used is the Mapping from the FITS pixel co-
ordinates in which the centre of the bottom left pixel is at co-
ordinates (1,1), to the co-ordinate system represented by the primary
WCS headers, CRVAL, CRPIX, etc.
+ An NDF. The Mapping used is the Mapping from the PIXEL Frame to the
  Current Frame of its WCS FrameSet.

If a null (!) value is supplied, the Mapping used is the Mapping from
pixel co-ordinates in the input NDF to the current Frame in the input
NDF. The output NDF will then have pixel co-ordinates which match the
co-ordinates of the current Frame of the input NDF (apart from
possible additional scalings as specified by the SCALE parameter).



METHOD = LITERAL (Read)
```````````````````````
The method to use when sampling the input pixel values (if
resampling), or dividing an input pixel value between a group of
neighbouring output pixels (if rebinning). For details of these
schemes, see the descriptions of routines AST_RESAMPLEx and
AST_REBINSEQx in SUN/210. METHOD can take the following values.


+ "Linear" -- When resampling, the output pixel values are calculated
by bi-linear interpolation among the four nearest pixels values in the
input NDF. When rebinning, the input pixel value is divided bi-
linearly between the four nearest output pixels. Produces smoother
output NDFs than the nearest-neighbour scheme, but is marginally
slower.
+ "Nearest" -- When resampling, the output pixel values are assigned
the value of the single nearest input pixel. When rebinning, the input
pixel value is assigned completely to the single nearest output pixel.
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
+ "BlockAve" -- Block averaging over all pixels in the surrounding
  N-dimensional cube. This option is only available when resampling
  (i.e. if REBIN is set to FALSE).

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
in the sample positions and in the pixel-centre positions. For these
reasons, if you want to use the output variances, you are generally
safer using nearest-neighbour interpolation. The initial default is
"Nearest". [current value]



NORM = _LOGICAL (Read)
``````````````````````
In general, each output pixel contains contributions from multiple
input pixel values, and the number of input pixels contributing to
each output pixel will vary from pixel to pixel. If NORM is set TRUE
(the default), then each output value is normalised by dividing it by
the number of contributing input pixels, resulting in each output
value being the weighted mean of the contributing input values.
However, if NORM is set FALSE, this normalisation is not applied. See
also Parameter CONSERVE. [TRUE]



OUT = NDF (Write)
`````````````````
The transformed NDF.



PARAMS( 2 ) = _DOUBLE (Read)
````````````````````````````
An optional array which consists of additional parameters required by
the Sinc, SincSinc, SincCos, SincGauss, Somb, SombCos, and Gauss
methods.
PARAMS( 1 ) is required by all the above schemes. It is used to
specify how many pixels are to contribute to the interpolated result
on either side of the interpolation or binning point in each
dimension. Typically, a value of 2 is appropriate and the minimum
allowed value is 1 (i.e. one pixel on each side). A value of zero or
fewer indicates that a suitable number of pixels should be calculated
automatically. [0]
PARAMS( 2 ) is required only by the SombCos, Gauss, SincSinc, SincCos,
and SincGauss schemes. For the SombCos, SincSinc, and SincCos schemes,
it specifies the number of pixels at which the envelope of the
function goes to zero. The minimum value is 1.0, and the run-time
default value is 2.0. For the Gauss and SincGauss scheme, it specifies
the full-width at half-maximum (FWHM) of the Gaussian envelope
measured in output pixels. The minimum value is 0.1, and the run-time
default is 1.0. On astronomical images and spectra, good results are
often obtained by approximately matching the FWHM of the envelope
function, given by PARAMS(2), to the point-spread function of the
input data. []



REBIN = _LOGICAL (Read)
```````````````````````
Determines the algorithm used to calculate the output pixel values. If
a TRUE value is given, a rebinning algorithm is used. Otherwise, a
resampling algorithm is used. See the "Choice of Algorithm" below.
[current value]



SCALE( ) = _DOUBLE (Read)
`````````````````````````
Axis scaling factors which are used to modify the supplied Mapping. If
the number of supplied values is less than the number of output axes
associated with the Mapping, the final supplied value is duplicated
for the missing axes. In effect, transformed input co-ordinate axis
values would be multiplied by these factors to obtain the
corresponding output pixel co-ordinates. If a null (!) value is
supplied for SCALE, then default values are used which depends on the
value of Parameter MAPPING. If a null value is supplied for MAPPING
then the default scaling factors are chosen so that pixels retain
their original size (very roughly) after transformation. If as non-
null value is supplied for MAPPING then the default scaling factor
used is 1.0 for each axis (i.e. no scaling). [!]



TITLE = LITERAL (Read)
``````````````````````
A Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



TOL = _DOUBLE (Read)
````````````````````
The maximum tolerable geometrical distortion that may be introduced as
a result of approximating non-linear Mappings by a set of piece-wise
linear transforms. Both algorithms approximate non-linear co-ordinate
transformations in order to improve performance, and this parameter
controls how inaccurate the resulting approximation is allowed to be,
as a displacement in pixels of the input NDF. A value of zero will
ensure that no such approximation is done, at the expense of
increasing execution time. [0.05]



UBOUND( ) = _INTEGER (Read)
```````````````````````````
The upper pixel-index bounds of the output NDF. The number of values
must be equal to the number of dimensions of the output NDF. If a null
value is supplied, default bounds will be used which are just high
enough to fit in all the transformed pixels of the input NDF. [!]



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
regrid sg28948 sg28948r mapping=rotate.ast
Here sg28948 is resampled into a new co-ordinate system using the AST
Mapping stored in a text file called rotate.ast (which may have been
created using WCSADD for instance).
regrid flat distorted mapping=!
This transforms the NDF called flat into its current co-ordinate
Frame, writing the result to an NDF called distorted. It uses nearest-
neighbour resampling. If the units of the PIXEL and current co-
ordinate Frames of flat are of similar size, then the pixel co-
ordinates of distorted will be the same as the current co-ordinates of
flat, but if there is a large scale discrepancy a scaling factor will
be applied to give the output NDF a similar size to the input one. The
output NDF will be just large enough to hold the transformed copies of
all the pixels from NDF flat.
regrid flat distorted mapping=! scale=1 method=sinccos
params=[0,3] As the previous example, but the additional scaling
factor will not be applied even in the case of large size discrepancy,
and a sinc*cos one-dimensional resampling kernel is used which rolls
off at a distance of 3 pixels from the central one.
regrid flat distorted mapping=! scale=0.2 method=blockave params=2
In this case, an additional shrinking factor of 0.2 is being applied
to the output NDF (i.e. performed following the Mapping from pixel to
current co-ordinates), and the resampling is being done using a block
averaging scheme in which a cube extending two pixels either side of
the central pixel is averaged over to produce the output value. If the
PIXEL-domain and current Frame pixels have (about) the same size, this
will result in every pixel from the input NDF adding a contribution to
one pixel of the output NDF.
regrid a119 a119s mapping=! lbound=[1,-20] ubound=[256,172]
This transforms the NDF called a119 into an NDF called a119s. It uses
nearest-neighbour resampling. The shape of a119s is forced to be
(1:256,-20:172) regardless of the location of the transformed pixels
of a119.



Notes
~~~~~


+ If the input NDF contains a VARIANCE component, a VARIANCE component
will be written to the output NDF. It will be calculated on the
assumption that errors on the input data values are statistically
independent and that their variance estimates may simply be summed
(with appropriate weighting factors) when several input pixels
contribute to an output data value. If this assumption is not valid,
then the output error estimates may be biased. In addition, note that
the statistical errors on neighbouring output data values (as well as
the estimates of those errors) may often be correlated, even if the
above assumption about the input data is correct, because of the sub-
pixel interpolation schemes employed.
+ This task is based on the AST_RESAMPLE<X> and AST_REBINSEQ<X>
  routines described in SUN/210.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FLIP, ROTATE, SLIDE, WCSADD, WCSALIGN. CCDPACK: TRANLIST,
TRANNDF, WCSEDIT.


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
weighted mean of the nearby input values, and so do not alter the mean
pixel values associated with a source, even if the pixel size changes.
Thus the total data sum in a source will change if the input and
output pixel sizes differ. However, if the CONSERVE parameter is set
TRUE, the output values are scaled by the ratio of the output to input
pixel size, so that the total data sum in a source is preserved.
A difference between resampling and rebinning is that resampling
guarantees to fill the output image with good pixel values (assuming
the input image is filled with good input pixel values), whereas holes
can be left by the rebinning algorithm if the output image has smaller
pixels than the input image. Such holes occur at output pixels that
receive no contributions from any input pixels, and will be filled
with the value zero in the output image. If this problem occurs, the
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
  transformation (controlled by Parameter TOL) can produce artefacts at
  the joints between the panels of the approximation. They are caused by
  the discontinuities between the adjacent panels of the approximation,
  and can be minimised by reducing the value assigned to the TOL
  parameter.




Copyright
~~~~~~~~~
Copyright (C) 2001-2004 Central Laboratory of the Research Councils.
Copyright (C) 2005-2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2012 Science & Technology Facilities Council. All Rights
Reserved.


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


+ The LABEL, UNITS, and HISTORY components, and all extensions are
propagated. TITLE is controlled by the TITLE parameter. DATA,
VARIANCE, and WCS are propagated after appropriate modification. The
QUALITY component is also propagated if Nearest-Neighbour
interpolation is being used. The AXIS component is not propagated.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. If REBIN is TRUE,
the data type will be converted to one of _INTEGER, _DOUBLE or _REAL
for processing.
+ There can be an arbitrary number of NDF dimensions.




