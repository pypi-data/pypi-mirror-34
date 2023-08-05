

BLOCK
=====


Purpose
~~~~~~~
Smooths an NDF using an n-dimensional rectangular box filter


Description
~~~~~~~~~~~
This application smooths an n-dimensional NDF using a rectangular box
filter, whose dimensionality is the same as that of the NDF being
smoothed. Each output pixel is either the mean or the median of the
input pixels within the filter box. The mean estimator provides one of
the fastest methods of smoothing an image and is often useful as a
general-purpose smoothing algorithm when the exact form of the
smoothing point-spread function is not important.
It is possible to smooth in selected dimensions by setting the boxsize
to 1 for the dimensions not requiring smoothing. For example you can
apply two-dimensional smoothing to the planes of a three-dimensional
NDF (see Parameter BOX). If it has three dimensions, then the filter
is applied in turn to each plane in the cube and the result written to
the corresponding plane in the output cube.


Usage
~~~~~


::

    
       block in out box [estimator]
       



ADAM parameters
~~~~~~~~~~~~~~~



BOX() = _INTEGER (Read)
```````````````````````
The sizes (in pixels) of the rectangular box to be applied to smooth
the data. These should be given in axis order. A value set to 1
indicates no smoothing along that axis. Thus, for example, BOX=[3,3,1]
for a three-dimensional NDF would apply a 3x3-pixel filter to all its
planes independently.
If fewer values are supplied than the number of dimensions of the NDF,
then the final value will be duplicated for the missing dimensions.
The values given will be rounded up to positive odd integers, if
necessary, to retain symmetry.



ESTIMATOR = LITERAL (Read)
``````````````````````````
The method to use for estimating the output pixel values. It can be
either "Mean" or "Median". ["Mean"]



IN = NDF (Read)
```````````````
The input NDF to which box smoothing is to be applied.



OUT = NDF (Write)
`````````````````
The output NDF which is to contain the smoothed data.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the input NDF to be used. [!]



WLIM = _REAL (Read)
```````````````````
If the input image contains bad pixels, then this parameter may be
used to determine the number of good pixels which must be present
within the smoothing box before a valid output pixel is generated. It
can be used, for example, to prevent output pixels from being
generated in regions where there are relatively few good pixels to
contribute to the smoothed result.
By default, a null (!) value is used for WLIM, which causes the
pattern of bad pixels to be propagated from the input image to the
output image unchanged. In this case, smoothed output values are only
calculated for those pixels which are not bad in the input image.
If a numerical value is given for WLIM, then it specifies the minimum
fraction of good pixels which must be present in the smoothing box in
order to generate a good output pixel. If this specified minimum
fraction of good input pixels is not present, then a bad output pixel
will result, otherwise a smoothed output value will be calculated. The
value of this parameter should lie between 0.0 and 1.0 (the actual
number used will be rounded up if necessary to correspond to at least
1 pixel). [!]



Examples
~~~~~~~~
block aa bb 9
Smooths the two-dimensional image held in the NDF structure aa,
writing the result into the structure bb. The smoothing box is 9
pixels square. If any pixels in the input image are bad, then the
corresponding pixels in the output image will also be bad. Each output
pixel is the mean of the corresponding input pixels.
block spectrum spectrums 5 median title="Smoothed spectrum"
Smooths the one-dimensional data in the NDF called spectrum using a
box size of 5 pixels, and stores the result in the NDF structure
spectrums. Each output pixel is the median of the corresponding input
pixels. If any pixels in the input image are bad, then the
corresponding pixels in the output image will also be bad. The output
NDF has the title "Smoothed spectrum".
block ccdin(123,) ccdcol [1,9]
Smooths the 123rd column in the two-dimensional NDF called ccdin using
a box size of 9 pixels, and stores the result in the NDF structure
ccdcol. The first value of the smoothing box is ignored as the first
dimension has only one element. Each output pixel is the mean of the
corresponding input pixels.
block in=image1 out=image2 box=[5,7] estimator=median
Smooths the two-dimensional image held in the NDF structure image1
using a rectangular box of size 5x7 pixels. The smoothed image is
written to the structure image2. Each output pixel is the median of
the corresponding input pixels.
block etacar etacars box=[7,1] wlim=0.6
Smooths the specified image data using a rectangular box 7x1 pixels in
size. Smoothed output values are generated only if at least 60% of the
pixels in the smoothing box are good, otherwise the affected output
pixel is bad.
block in=cubein out=cubeout box=[3,3,7]
Smooths the three-dimensional NDF called cubein using a box that has
three elements along the first two axes and seven along the third. The
smoothed cube is written to NDF cubeout.
block in=cubein out=cubeout box=[3,1,7]
As the previous example, except that planes comprising the first and
third axes are smoothed independently for all lines.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CONVOLVE, FFCLEAN, GAUSMOOTH, MEDIAN; Figaro: ICONV3, ISMOOTH,
IXSMOOTH, MEDFILT.


Timing
~~~~~~
When using the mean estimator, the execution time is approximately
proportional to the number of pixels in the image to be smoothed and
is largely independent of the smoothing box size. This makes the
routine particularly suitable for applying heavy smoothing to an
image. Execution time will be approximately doubled if a variance
array is present in the input NDF.
The median estimator is much slower than the mean estimator, and is
heavily dependent on the smoothing box size.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992, 1994 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2005 Particle Physics & Astronomy Research
Council. .Copyright (C) 2009 Science & Facilities Research Council.
All Rights Reserved.


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
propagates all extensions. In addition, if the mean estimator is used,
the VARIANCE component is also processed. If the median estimator is
used, then the output NDF will have no VARIANCE component, even if
there is a VARIANCE component in the input NDF.
+ Processing of bad pixels and automatic quality masking are
supported. The bad-pixel flag is also written for the data and
variance arrays.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point, or double precision,
  if appropriate.




