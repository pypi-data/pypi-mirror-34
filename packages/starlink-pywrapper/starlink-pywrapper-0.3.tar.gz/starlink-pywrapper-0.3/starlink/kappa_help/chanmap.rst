

CHANMAP
=======


Purpose
~~~~~~~
Creates a channel map from a cube NDF by compressing slices along a
nominated axis


Description
~~~~~~~~~~~
This application creates a two-dimensional channel-map image from a
three-dimensional NDF. It collapses along a nominated pixel axis in
each of a series of slices. The collapsed slices are tiled with no
margins to form the output image. This grid of channel maps is filled
from left to right, and bottom to top. A specified range of axis
values can be used instead of the whole axis (see parameters LOW and
HIGH). The number of channels and their arrangement into an image is
controlled through parameters NCHAN and SHAPE.
For each output pixel, all corresponding input pixel values between
the channel bounds of the nominated axis to be collapsed are combined
together using one of a selection of estimators, including a mean,
mode, or median, to produce the output pixel value.


Usage
~~~~~


::

    
       chanmap in out axis nchan shape [low] [high] [estimator] [wlim]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = LITERAL (Read)
`````````````````````
The axis along which to collapse the NDF. This can be specified using
one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If the axes of the current Frame are not parallel to the NDF
pixel axes, then the pixel axis which is most nearly parallel to the
specified current Frame axis will be used.



CLIP = _REAL (Read)
```````````````````
The number of standard deviations about the mean at which to clip
outliers for the "Mode", "Cmean" and "Csigma" statistics (see
Parameter ESTIMATOR). The application first computes statistics using
all the available pixels. It then rejects all those pixels whose
values lie beyond CLIP standard deviations from the mean and will then
re-evaluate the statistics. For "Cmean" and "Csigma" there is
currently only one iteration, but up to seven for "Mode".
The value must be positive. [3.0]



ESTIMATOR = LITERAL (Read)
``````````````````````````
The method to use for estimating the output pixel values. It can be
one of the following options. "Mean" -- Mean value "WMean" -- Weighted
mean in which each data value is weighted by the reciprocal of the
associated variance. (2) "Mode" -- Modal value (4) "Median" -- Median
value. Note that this is extremely memory and CPU intensive for large
datasets; use with care! If strange things happen, use "Mean". (3)
"Absdev" -- Mean absolute deviation from the unweighted mean. (2)
"Cmean" -- Sigma-clipped mean. (4) "Csigma" -- Sigma-clipped standard
deviation. (4) "Comax" -- Co-ordinate of the maximum value. "Comin" --
Co-ordinate of the minimum value. "FBad" -- Fraction of bad pixel
values. "FGood" -- Fraction of good pixel values. "Integ" --
Integrated value, being the sum of the products of the value and pixel
width in world co-ordinates. "Iwc" -- Intensity-weighted co-ordinate,
being the sum of each value times its co-ordinate, all divided by the
integrated value (see the "Integ" option). "Iwd" -- Intensity-weighted
dispersion of the co-ordinate, normalised like "Iwc" by the integrated
value. (4) "Max" -- Maximum value. "Min" -- Minimum value. "NBad" --
Number of bad pixel values. "NGood" -- Number of good pixel values.
"Rms" -- Root-mean-square value. (4) "Sigma" -- Standard deviation
about the unweighted mean. (4) "Sum" -- The total value.
The selection is restricted if each channel contains three or fewer
pixels. For instance, measures of dispersion like "Sigma" and "Iwd"
are meaningless for single-pixel channels. The minimum number of
pixels per channel for each estimator is given in parentheses in the
list above. Where there is no number, there is no restriction. If you
supply an unavailable option, you will be informed, and presented with
the available options. ["Mean"]



HIGH = LITERAL (Read)
`````````````````````
Together with Parameter LOW, this parameter defines the range of
values for the axis specified by Parameter AXIS to be divided into
channels. For example, if AXIS is 3 and the current Frame of the input
NDF has axes RA/DEC/Wavelength, then a wavelength value should be
supplied. If, on the other hand, the current Frame in the NDF was the
PIXEL Frame, then a pixel co-ordinate value would be required for the
third axis (note, the pixel with index I covers a range of pixel co-
ordinates from (I-1) to I).
Note, HIGH and LOW should not be equal. If a null value (!) is
supplied for either HIGH or LOW, the entire range of the axis
fragmented into channels. [!]



IN = NDF (Read)
```````````````
The input NDF. This must have three dimensions.



LOW = LITERAL (Read)
````````````````````
Together with Parameter HIGH this parameter defines the range of
values for the axis specified by Parameter AXIS to be divided into
channels. For example, if AXIS is 3 and the current Frame of the input
NDF has axes RA/DEC/Frequency, then a frequency value should be
supplied. If, on the other hand, the current Frame in the NDF was the
PIXEL Frame, then a pixel co-ordinate value would be required for the
third axis (note, the pixel with index I covers a range of pixel co-
ordinates from (I-1) to I).
Note, HIGH and LOW should not be equal. If a null value (!) is
supplied for either HIGH or LOW, the entire range of the axis
fragmented into channels. [!]



NCHAN = _INTEGER (Read)
```````````````````````
The number of channels to appear in the channel map. It must be a
positive integer up to the lesser of 100 or the number of pixels along
the collapsed axis.



OUT = NDF (Write)
`````````````````
The output NDF.



SHAPE = _INTEGER (Read)
```````````````````````
The number of channels along the x axis of the output NDF. The number
along the y axis will be 1+(NCHAN-1)/SHAPE. A null value (!) asks the
application to select a shape. It will generate one that gives the
most square output NDF possible. The value must be positive and no
more than the value of Parameter NCHAN.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the input
NDF has more than three axes. A group of three strings should be
supplied specifying the three axes which are to be retained in a
collapsed slab. Each axis can be specified using one of the following
options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the three used pixel axes within the NDF are used. [!]



WLIM = _REAL (Read)
```````````````````
If the input NDF contains bad pixels, then this parameter may be used
to determine the number of good pixels which must be present within
the range of collapsed input pixels before a valid output pixel is
generated. It can be used, for example, to prevent output pixels from
being generated in regions where there are relatively few good pixels
to contribute to the collapsed result.
WLIM specifies the minimum fraction of good pixels which must be
present in order to generate a good output pixel. If this specified
minimum fraction of good input pixels is not present, then a bad
output pixel will result, otherwise a good output value will be
calculated. The value of this parameter should lie between 0.0 and 1.0
(the actual number used will be rounded up if necessary to correspond
to at least one pixel). [0.3]



Examples
~~~~~~~~
chanmap cube chan4 lambda 4 2 4500 4550
The current Frame in the input three-dimensional NDF called cube has
axes with labels "RA", "DEC" and "Lambda", with the lambda axis being
parallel to the third pixel axis. The above command extracts four
slabs of the input cube between wavelengths 4500 and 4550 Angstroms,
and collapses each slab, into a single two-dimensional array with RA
and DEC axes forming a channel image. Each channel image is pasted
into a 2x2 grid within the output NDF called chan4. Each pixel in the
output NDF is the mean of the corresponding input pixels with
wavelengths in 12.5-Angstrom bins.
chanmap in=cube out=chan4 axis=3 low=4500 high=4550 nchan=4
shape=2 The same as above except the axis to collapse along is
specified by index (3) rather than label (lambda), and it uses
keywords rather than positional parameters.
chanmap cube chan4 3 4 2 9.0 45.0
This is the same as the above examples, except that the current Frame
in the input NDF has been set to the PIXEL Frame (using WCSFRAME), and
so the high and low axis values are specified in pixel co-ordinates
instead of Angstroms, and each channel covers nine pixels. Note the
difference between floating-point pixel co-ordinates, and integer
pixel indices (for instance the pixel with index 10 extends from pixel
co-ordinate 9.0 to pixel co-ordinate 10.0).
chanmap in=zcube out=vel7 axis=1 low=-30 high=40 nchan=7 shape=!
estimator=max This command assumes that the zcube NDF has a current
co-ordinate system where the first axis is radial velocity (perhaps
selected using WCSFRAME and WCSATTRIB), and the second and third axes
are "RA", and "DEC". It extracts seven velocity slabs of the input
cube between -30 and +40 km/s, and collapses each slab, into a single
two-dimensional array with RA and DEC axes forming a channel image.
Each channel image is pasted into a default grid (likely 4x2) within
the output NDF called vel7. Each pixel in the output NDF is the
maximum of the corresponding input pixels with velocities in 10-km/s
bins.



Notes
~~~~~


+ The collapse is always performed along one of the pixel axes, even
  if the current Frame in the input NDF is not the PIXEL Frame. Special
  care should be taken if the current-Frame axes are not parallel to the
  pixel axes. The algorithm used to choose the pixel axis and the range
  of values to collapse along this pixel axis proceeds as follows.

The current-Frame co-ordinates of the central pixel in the input NDF
are determined (or some other point if the co-ordinates of the central
pixel are undefined). Two current-Frame positions are then generated
by substituting in turn into this central position each of the HIGH
and LOW values for the current-Frame axis specified by Parameter AXIS.
These two current-Frame positions are transformed into pixel co-
ordinates, and the projections of the vector joining these two pixel
positions on to the pixel axes are found. The pixel axis with the
largest projection is selected as the collapse axis, and the two end
points of the projection define the range of axis values to collapse.

+ The WCS of the output NDF retains the three-dimensional co-ordinate
system of the input cube for every tile, except that each tile has a
single representative mean co-ordinate for the collapsed axis.
+ The slices may have slightly different pixel depths depending where
  the boundaries of the channels lie in pixel co-ordinates. Excise care
  interpreting estimators like "Sum" or ensure equal numbers of pixels
  in each channel.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: COLLAPSE, CLINPLOT.


Copyright
~~~~~~~~~
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2007 Science & Technology Facilities Council. Copyright
(C) 2008, 2009, 2012 Science and Technology Faciities Council. All
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
UNITS, WCS, and HISTORY components of the input NDF; and propagates
all extensions. AXIS and QUALITY are not propagated.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ The origin of the output NDF is at (1,1).




