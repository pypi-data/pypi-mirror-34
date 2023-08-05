

CONVOLVE
========


Purpose
~~~~~~~
Convolves a pair of NDFs where the smoothing NDF is one- or two-
dimensional


Description
~~~~~~~~~~~
This application smooths an NDF using a Point-Spread Function given by
a second NDF. The output NDF is normalised to the same mean data value
as the input NDF (if parameter NORM is set to TRUE), and is the same
size as the input NDF.
The NDF being smoothed may have up to three dimensions. If it has
three significant dimensions, then the filter must be two-dimensional,
and it is applied in turn to each plane in the cube and the result
written to the corresponding plane in the output cube. The orientation
of the smoothing plane can be specified using the AXES parameter.


Usage
~~~~~


::

    
       convolve in psf out xcentre ycentre
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES(2) = _INTEGER (Read)
`````````````````````````
This parameter is only accessed if the NDF has exactly three
significant pixel axes. It should be set to the indices of the NDF
pixel axes which span the plane in which smoothing is to be applied.
All pixel planes parallel to the specified plane will be smoothed
independently of each other. The dynamic default is the indices of the
first two significant axes in the NDF. []



IN = NDF (Read)
```````````````
The input NDF containing the array to be smoothed.



NORM = _LOGICAL (Read)
``````````````````````
Determines how the output NDF is normalised to take account of the
total data sum in the PSF, and of the presence of bad pixels in the
input NDF. If TRUE, bad pixels are excluded from the data sum for each
output pixel, and the associated weight for the output pixel is
reduced appropriately. The supplied PSF is normalised to a total data
sum of unity so that the output NDF has same normalisation as the
input NDF. If NORM is FALSE, bad pixels are replaced by the mean value
and then included in the convolution as normal. The normalisation of
the supplied PSF is left unchanged, and so determines the
normalisation of the output NDF. [TRUE]



OUT = NDF (Write)
`````````````````
The output NDF which is to contain the smoothed array.



PSF = NDF (Read)
````````````````
An NDF holding the Point-Spread Function (PSF) with which the input
array is to be smoothed. An error is reported if the PSF contains any
bad pixels. The PSF can be centred anywhere within the array (see
parameters XCENTRE and YCENTRE). A constant background is removed from
the PSF before use. This background level is equal to the minimum of
the absolute value in the four corner pixel values. The PSF is assumed
to be zero beyond the bounds of the supplied NDF. It should have the
same number of dimensions as the NDF being smoothed, unless the input
NDF has three significant dimensions, whereupon the PSF must be two-
dimensional. It will be normalised to a total data sum of unity if
NORM is TRUE.



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null (!) value means using the title of
the input NDF. [!]



WLIM = _REAL (Read)
```````````````````
If the input array contains bad pixels, and NORM is TRUE, then this
parameter may be used to determine the number of good pixels that must
be present within the smoothing box before a valid output pixel is
generated. It can be used, for example, to prevent output pixels from
being generated in regions where there are relatively few good pixels
to contribute to the smoothed result.
By default, a null (!) value is used for WLIM, which causes the
pattern of bad pixels to be propagated from the input array to the
output array unchanged. In this case, smoothed output values are only
calculated for those pixels which are not bad in the input array.
If a numerical value is given for WLIM, then it specifies the minimum
total weight associated with the good pixels in the smoothing box
required to generate a good output pixel (weights for each pixel are
defined by the normalised PSF). If this specified minimum weight is
not present, then a bad output pixel will result, otherwise a smoothed
output value will be calculated. The value of this parameter should
lie between 0.0 and 1.0. A value of 0.0 will result in a good output
pixel being created even if only one good input pixel contributes to
it. A value of 1.0 will result in a good output pixel being created
only if all the input pixels which contribute to it are good. See also
NORM. [!]



XCENTRE = _INTEGER (Read)
`````````````````````````
The x pixel index (column number) of the centre of the PSF within the
supplied PSF array. The suggested default is the centre of the PSF
array. (This is how the PSF command would generate the array.)



YCENTRE = _INTEGER (Read)
`````````````````````````
The y pixel index (line number) of the centre of the PSF within the
supplied PSF array. The suggested default is the centre of the PSF
array. (This is how the PSF command would generate the array.)



Examples
~~~~~~~~
convolve ccdframe iraspsf ccdlores 50 50
The image in the NDF called ccdframe is convolved using the PSF in NDF
iraspsf to create the smoothed image ccdlores. The centre of the PSF
image in iraspsf is at pixel indices (50,50). Any bad pixels in the
input image are propagated to the output.
convolve ccdframe iraspsf ccdlores 50 50 wlim=1.0
As above, but good output values are only created for pixels which
have no contributions from bad input pixels.
convolve ccdframe iraspsf ccdlores \
As in the first example except the centre of the PSF is located at the
centre of the PSF array.



Notes
~~~~~


+ The algorithm used is based on the multiplication of the Fourier
transforms of the input array and PSF array.
+ A PSF can be created using the PSF command or MATHS if the PSF is an
  analytic function.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: BLOCK, FFCLEAN, GAUSMOOTH, MATHS, MEDIAN, PSF; Figaro: ICONV3,
ISMOOTH, IXSMOOTH, MEDFILT.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2004 Central Laboratory of the Research Councils. All
Rights Reserved. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2009-2010 Science & Technology
Facilities Council. All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using double-precision floating point.




