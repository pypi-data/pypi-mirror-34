

ALIGN2D
=======


Purpose
~~~~~~~
Aligns a pair of two-dimensional NDFs by minimising the residuals
between them


Description
~~~~~~~~~~~
This application attempts to align a two-dimensional input NDF with a
two-dimensional reference NDF in pixel co-ordinates, using an affine
transformation of the form:
Xin = C1 + C2*Xref + C3*Yref
Yin = C4 + C5*Xref + C6*Yref
where (Xin,Yin) are pixel co-ordinates in the input NDF, and
(Xref,Yref) are pixel co-ordinates in the reference NDF. The
coefficient values (C1--C6) are determined by doing a least-squares
fit that minimises the sum of the squared residuals between the
reference NDF and the transformed input NDF. If variance information
is present in either NDF, it is used to determine the SNR of each
pixel which is used to weight the residuals within the fit, so that
noisy data values have less effect on the fit. The best fit
coefficients are displayed on the screen and written to an output
parameter. Optionally, the transformation may be applied to the input
NDF to create an output NDF (see Parameter OUT). It is possible to
restrict the transformation in order to prevent shear, rotation,
scaling, etc. (see Parameter FORM).
It is possible to exclude from the fitting process areas of the input
NDF that are poorly correlated with the corresponding areas in the
reference NDF (e.g. flat background areas that contain only noise).
See parameter CORLIMIT.


Usage
~~~~~


::

    
       align2d in ref out
       



ADAM parameters
~~~~~~~~~~~~~~~



BOX = _INTEGER (Read)
`````````````````````
The box size, in pixels, over which to calculate the correlation
coefficient between the input and reference images. This should be set
to an estimate of the maximum expected shift between the two images,
but should not be less than typical size of features within the two
images. See also parameter CORLIMIT. [5]



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



CORLIMIT = _REAL (Read)
```````````````````````
If CORLIMIT is not null (!), each pixel in the input image is checked
to see if the pixel values in its locality are well correlated with
the corresponding locality in the reference image. The input pixel is
excluded from the fitting process if the local correlation is below
CORLIMIT. The supplied value should be between zero and 1.0. The size
of the locality used around each input pixel is given by Parameter
BOX.
In addition, if a value is supplied for CORLIMIT, the input and
reference pixel values that pass the above check are scaled so that
they have a mean value of zero and a standard deviation of unity
before being used in the fitting process. [!]



FITVALS = _LOGICAL (Read)
`````````````````````````
If TRUE, the fitting process will adjust the scale and offset of the
input data values, in addition to the geometric position of the the
input values, in order to minimise the sum of the squared residuals.
[FALSE]



FORM = _INTEGER (Read)
``````````````````````
The form of the affine transformation to use:


+ 0 -- full unrestricted 6 coefficient fit;
+ 1 -- shift, rotation and a common X/Y scale but no shear;
+ 2 -- shift and rotation but no scale or shear; or
+ 3 -- shift but not rotation, scale or shear. [0]





IN = NDF (Read)
```````````````
NDF to be transformed.



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



OUT = NDF (Writed)
``````````````````
An optional output NDF to contain a copy of IN aligned with OUT. No
output is created if null (!) is supplied. If FITVALS is TRUE, the
output data values will be scaled so that they have the same
normalisation as the reference values.



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



REF = NDF (Read)
````````````````
NDF to be used as a refernece.



RMS = _DOUBLE (Write)
`````````````````````
An output parameter to which is written the RMS residual between the
aligned data and the reference data.



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



TR( 6 or 8 ) = _DOUBLE (Write)
``````````````````````````````
An output parameter to which are written the coefficients of the fit.
If FITVALS is TRUE, then this will include the scale and offset
(written to the seventh and eighth entries).



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
align2d my_data orionA my_corrected form=2
Aligns the two-dimensional NDF called my_data with the two-dimensional
NDF called orionA, putting the aligned image in a new NDF called
my_corrected. The transformation is restricted to a shift of origin
and a rotation.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSALIGN.


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
  transformation (controlled by Parameter TOL) can produce artefacts at
  the joints between the panels of the approximation. They are caused by
  the discontinuities between the adjacent panels of the approximation,
  and can be minimised by reducing the value assigned to the TOL
  parameter.




Copyright
~~~~~~~~~
Copyright (C) 2016 East Asian Observatory. All Rights Reserved.


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


+ This routine correctly processes the DATA, VARIANCE, WCS, LABEL,
TITLE, and UNITS components of the NDF.
+ All non-complex numeric data types can be handled.




