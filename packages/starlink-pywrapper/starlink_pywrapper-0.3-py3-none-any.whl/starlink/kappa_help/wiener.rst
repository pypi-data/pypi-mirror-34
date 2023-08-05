

WIENER
======


Purpose
~~~~~~~
Applies a Wiener filter to a 1- or 2-dimensional array


Description
~~~~~~~~~~~
This application filters the supplied one- or two-dimensional array
using a Wiener filter. It takes an array holding observed data and
another holding a Point-Spread Function as input and produces an
output restored array with potentially higher resolution and lower
noise. Generally superior results can be obtained using applications
MEM2D or LUCY, but at the cost of much more processing time.
The Wiener filter attempts to minimise the mean squared difference
between the undegraded image and the restored image. To do this it
needs to know the power spectrum of the undegraded image (i.e. the
power at each spatial frequency before the instrumental blurring and
the addition of noise). Obviously, this is not usually available, and
instead the power spectrum of some other image must be used (the
`model' image). The idea is that a model image should be chosen for
which there is some a priori reason for believing it to have a power
spectrum similar to the undegraded image. Many different suggestions
have been made for the best way to make this choice and the literature
should be consulted for a detailed discussion (for instance, see the
paper "Wiener Restoration of HST Images: Signal Models and Photometric
Behavior" by I.C. Busko in the proceedings of the first Annual
Conference on Astronomical Data Analysis Software and Systems,
Tucson). By default, this application uses a `white' model image, i.e.
one in which there is equal power at all spatial frequencies. The
default value for this constant power is the mean power per pixel in
the input image. There is also an option to use the power spectrum of
a supplied model image.
The filter also depends on a model of the noise in the supplied image.
This application assumes that the noise is 'white' and is constant
across the image. You can specify the noise power to use. If a noise
power of zero is supplied, then the Wiener filter just becomes a
normal inverse filter which will tend to amplify noise in the supplied
image.
The filtering is done by multiplying the Fourier transform of the
supplied image by the Fourier transform of the filter function. The
output image is then created by taking the inverse Fourier transform
of the product. The Fourier transform of the filter function is given
by:
* H

+ ------------ 2 Pn |H| + ---- Pg

where H is the Fourier transform of the supplied Point-Spread
Function, Pn is the noise power, Pg is the power in the model image,
and the asterisk represents complex conjugation. If the supplied model
includes noise (as indicated by Parameter QUIET) then Pn is subtracted
from Pg before evaluating the above expression.


Usage
~~~~~


::

    
       wiener in psf out xcentre ycentre
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF containing the observed data. This image may contain bad
values, in which case the bad values will be replaced by zero before
applying the filter. The resulting filtered image is normalised by
dividing each pixel value by the corresponding weight of the good
input pixels. These weights are found by filtering a mask image which
holds the value one at every good input pixel, and zero at every bad
input pixel.



MODEL = NDF (Read)
``````````````````
An NDF containing an image to use as the model for the power spectrum
of the restored image. Any bad values in this image are replaced by
the mean of the good values. If a null value is supplied then the
model power spectrum is taken to be uniform with a value specified by
Parameter PMODEL. [!]



OUT = NDF (Write)
`````````````````
The restored output array. An extension named WIENER is added to the
output NDF to indicate that the image was created by this application
(see Parameter QUIET).



PMODEL = _REAL (Read)
`````````````````````
The mean power per pixel in the model image. This parameter is only
accessed if a null value is supplied for parameter MODEL. If a value
is obtained for PMODEL then the model image is assumed to have the
specified constant power at all spatial frequencies. If a null (!)
value is supplied, the value used is the mean power per pixel in the
input image. [!]



PNOISE = _REAL (Read)
`````````````````````
The mean noise power per pixel in the observed data. For Gaussian
noise this is equal to the variance. If a null (!) value is supplied,
the value used is an estimate of the noise variance based on the
difference between adjacent pixel values in the observed data. [!]



PSF = NDF (Read)
````````````````
An NDF holding an estimate of the Point-Spread Function (PSF) of the
input array. This could, for instance, be produced using the KAPPA
application "PSF". There should be no bad pixels in the PSF otherwise
an error will be reported. The PSF can be centred anywhere within the
array, but the location of the centre must be specified using
parameters XCENTRE and YCENTRE. The PSF is assumed to have the value
zero outside the supplied NDF.



QUIET = _LOGICAL (Read)
```````````````````````
This specifies whether or not the image given for parameter MODEL (or
the value given for Parameter PMODEL), includes noise. If the model
does not include any noise then a TRUE value should be supplied for
QUIET. If there is any noise in the model then QUIET should be
supplied FALSE. If a null (!) value is supplied, the value used is
FALSE, unless the image given for Parameter MODEL was created by a
previous run of WIENER (as indicated by the presence of a WIENER
extension in the NDF), in which case the run time default is TRUE
(i.e. the previous run of WIENER is assumed to have removed the
noise). [!]



THRESH = _REAL (Read)
`````````````````````
The fraction of the PSF peak amplitude at which the extents of the PSF
are determined. These extents are used to derive the size of the
margins that pad the supplied input array. Lower values of THRESH will
result in larger margins being used. THRESH must be positive and less
than 0.5. [0.0625]



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null (!) value means using the title of
the input NDF. [!]



WLIM = _REAL (Read)
```````````````````
If the input array contains bad values, then this parameter may be
used to determine the minimum weight of good input values required to
create a good output value. It can be used, for example, to prevent
output pixels from being generated in regions where there are
relatively few good input values to contribute to the restored result.
It can also be used to `fill in' small areas (i.e. smaller than the
PSF) of bad pixels.
The numerical value given for WLIM specifies the minimum total weight
associated with the good pixels in a smoothing box required to
generate a good output pixel (weights for each pixel are defined by
the normalised PSF). If this specified minimum weight is not present,
then a bad output pixel will result, otherwise a smoothed output value
will be calculated. The value of this parameter should lie between 0.0
and 1.0. WLIM=0 causes a good output value to be created even if there
is only one good input value, whereas WLIM=1 causes a good output
value to be created only if all input values are good. [0.001]



XCENTRE = _INTEGER (Read)
`````````````````````````
The x pixel index of the centre of the PSF within the supplied PSF
array. The suggested default is the middle pixel (rounded down if
there are an even number of pixels per line).



YCENTRE = _INTEGER (Read)
`````````````````````````
The y pixel index of the centre of the PSF within the supplied PSF
array. The suggested default is the middle line (rounded down if there
are an even number of lines).



Examples
~~~~~~~~
wiener cenA star cenA_hires 11 13
This example deconvolves the array in the NDF called cenA, putting the
resulting array in the NDF called cenA_hires. The PSF is defined by
the array in NDF star, and the centre of the PSF is at pixel (11,13).
wiener cenA star cenA_hires 11 13 pnoise=0
This example performs the same function as the previous example,
except that the noise power is given as zero. This causes the Wiener
filter to reduce to a standard inverse filter, which will result in
more high frequencies being present in the restored image.
wiener cenA star cenA_hires 11 13 model=theory quiet
This example performs the same function as the first example, except
that the power spectrum of the restored image is modelled on that of
NDF theory, which may for instance contain a theoretical model of the
object in NDF cenA, together with a simulated star field. The
Parameter QUIET is set to a TRUE value to indicate that the
theoretical model contains no noise.



Notes
~~~~~


+ The convolutions required by the Wiener filter are performed by the
  multiplication of Fourier transforms. The supplied input array is
  extended by a margin along each edge to avoid problems of wrap-around
  between opposite edges of the array. The width of this margin is about
  equal to the width of the significant part of the PSF (as determined
  by Parameter THRESH). The application displays the width of these
  margins. The margins are filled by replicating the edge pixels from
  the supplied input NDFs.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FOURIER, LUCY, MEM2D.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL,
TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point.




