

GAUSMOOTH
=========


Purpose
~~~~~~~
Smooths a one- to three-dimensional NDF using a Gaussian filter


Description
~~~~~~~~~~~
This application smooths an NDF using a one- or two-dimensional
symmetrical Gaussian point spread function (PSF) of specified width,
or widths and orientation. Each output pixel is the PSF-weighted mean
of the input pixels within the filter box.
The NDF may have up to three dimensions. If it has three dimensions,
then the filter is applied in turn to each plane in the cube and the
result written to the corresponding plane in the output cube. The
orientation of the smoothing plane can be specified using the AXES
parameter.


Usage
~~~~~


::

    
       gausmooth in out fwhm
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES(2) = _INTEGER (Read)
`````````````````````````
This parameter is only accessed if the NDF has exactly three
significant pixel axes. It should be set to the indices of the NDF
pixel axes which span the plane in which smoothing is to be applied.
All pixel planes parallel to the specified plane will be smoothed
independently of each other. The dynamic default comprises the indices
of the first two significant axes in the NDF. []



BOX() = _INTEGER (Read)
```````````````````````
The x and y sizes (in pixels) of the rectangular region over which the
Gaussian PSF should be applied at each point. The smoothing PSF will
be set to zero outside this rectangle, which should therefore be
sufficiently large not to truncate the PSF too early. A square region
is defined should only one size be given. For a one-dimensional or
circular Gaussian a second size is ignored. Two values are expected
when an elliptical PSF is requested (see the description of parameter
FWHM).
The values given will be rounded up to positive odd integers if
necessary. If a null (!) value is supplied, the value used is just
sufficient to accommodate the Gaussian PSF out to a radius of 3
standard deviations. Note that the time taken to perform the smoothing
increases in approximate proportion to the value of this parameter for
a circular Gaussian, and in proportion to the product of the two box
sizes for an elliptical Gaussian. [!]



FWHM() = _REAL (Read)
`````````````````````
This specifies whether a circular or elliptical Gaussian point-spread
function is used in smoothing a two-dimensional image. If one value is
given it is the full-width at half-maximum of a one-dimensional or
circular Gaussian PSF. (Indeed only one value is permitted for a one-
dimensional array.) If two values are supplied, this parameter becomes
the full-width at half-maximum of the major and minor axes of an
elliptical Gaussian PSF. Values between 0.1 and 10000.0 pixels should
be given. Note that unless a non-default value is specified for the
BOX parameter, the time taken to perform the smoothing will increase
in approximate proportion to the value(s) of FWHM. The suggested
default is the current value.



IN = NDF (Read)
```````````````
The input NDF containing the one-, two-, or three-dimensional image to
which Gaussian smoothing is to be applied.



ORIENT = _REAL (Read)
`````````````````````
The orientation of the major axis of the elliptical Gaussian PSF,
measured in degrees in an anti-clockwise direction from the x axis of
the NDF. ORIENT is not obtained if FWHM has one value, i.e. a circular
Gaussian PSF will be used to smooth the image, or the input NDF is
one-dimensional. The suggested default is the current value.



OUT = NDF (Write)
`````````````````
The output NDF which is to contain the smoothed image.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the input NDF to be used. [!]



WLIM = _DOUBLE (Read)
`````````````````````
If the input image contains bad pixels, then this parameter may be
used to determine the number of good pixels which must be present
within the PSF area before a valid output pixel is generated. It can
be used, for example, to prevent output pixels from being generated in
regions where good pixels are only present in the wings of the PSF.
By default, a null (!) value is used for WLIM, which causes the
pattern of bad pixels to be propagated from the input image to the
output image unchanged. In this case, smoothed output values are only
calculated for those pixels which are not bad in the input image.
If a numerical value is given for WLIM, then it specifies the minimum
PSF-weighted fraction of good pixels which must be present in the PSF
area (i.e. box) in order to generate a good output pixel. The maximum
value, in the absence of bad pixels, is unity. If the specified
minimum fraction of good input pixels is not present, then a bad
output pixel will result, otherwise a smoothed output value will be
calculated. The value of this parameter should lie between 1E-6 and
1.0. [!]



Examples
~~~~~~~~
gausmooth image1 image2 5.0
Smooths the two-dimensional image held in the NDF structure image1
using a symmetrical Gaussian PSF with a full-width at half-maximum of
5 pixels. The smoothed image is written to image2. If any pixels in
the input image are bad, then the corresponding pixels in the output
image will also be bad.
gausmooth spectrum1 spectrum2 5.0 box=9
Smooths the one-dimensional image held in the NDF structure spectrum1
using a symmetrical Gaussian PSF with a full-width at half-maximum of
5, and is evaluated over a length of 9 pixels. The smoothed image is
written to spectrum2. If any pixels in the input image are bad, then
the corresponding pixels in the output image will also be bad.
gausmooth in=a out=b fwhm=3.5 box=31
Smooths the two-dimensional image held in the NDF structure a, writing
the result into the structure b. The Gaussian smoothing PSF has a
full-width at half-maximum of 3.5 pixels and is evaluated over a large
square of size 31x31 pixels.
gausmooth in=a out=b fwhm=[4,3] orient=52.7 box=[29,33]
Smooths the two-dimensional image held in the NDF structure a, writing
the result into the structure b. The elliptical Gaussian smoothing PSF
has full-width at half-maximum of 4 pixels along its major axis and
three pixels along its minor axis, and is evaluated over a large
rectangle of size 29x33 pixels. The major axis of the PSF is oriented
52.7 degrees anti-clockwise from the x axis of the data array.
gausmooth ngc1097 ngc1097s fwhm=7.2 wlim=0.1
Smooths the specified image data using a Gaussian PSF with a full-
width at half-maximum of 7.2. An output value is calculated for any
pixel for which the PSF-weighted fraction of good input pixels is at
least 0.1. This will cause the smoothing operation to fill in
moderately sized regions of bad pixels.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: BLOCK, CONVOLVE, FFCLEAN, MATHS, MEDIAN, PSF; Figaro: ICONV3,
ISMOOTH, IXSMOOTH, MEDFILT.


Timing
~~~~~~
For a circular PSF, the execution time is approximately proportional
to the number of pixels in the image to be smoothed and to the value
given for the BOX parameter. By default, this latter value is
proportional to the value given for FWHM. For an elliptical PSF, the
execution time is approximately proportional to the number of pixels
in the image to be smoothed and to the product of the values given for
the BOX parameter. By default, these latter values are approximately
proportional to the values given for FWHM. Execution time will be
approximately doubled if a variance array is present in the input NDF.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2000, 2004 Central Laboratory of the
Research Councils. All Rights Reserved. Copyright (C) 2006 Particle
Physics & Astronomy Research Council. All Rights Reserved.


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
supported. The bad-pixel flag is also written for the data and
variance arrays.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point, or double precision,
  if appropriate.




