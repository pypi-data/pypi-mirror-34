

COLLAPSE
========


Purpose
~~~~~~~
Reduce the number of axes in an N-dimensional NDF by compressing it
along a nominated axis


Description
~~~~~~~~~~~
This application collapses a nominated pixel axis of an N-dimensional
NDF, producing an output NDF with one fewer pixel axes than the input
NDF. A specified range of axis values can be used instead of the whole
axis (see Parameters LOW and HIGH).
For each output pixel, all corresponding input pixel values between
the specified bounds of the nominated axis to be collapsed are
combined together using one of a selection of estimators, including a
mean, mode, or median, to produce the output pixel value.
Possible uses include such things as collapsing a range of wavelength
planes in a three-dimensional RA/DEC/Wavelength cube to produce a
single two-dimensional RA/DEC image, or collapsing a range of slit
positions in a two-dimensional slit position/wavelength image to
produce a one-dimensional wavelength array.


Usage
~~~~~


::

    
       collapse in out axis [low] [high] [estimator] [wlim]
       



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
currently only one iteration , but up to seven for "Mode".
The value must be positive. [3.0]



COMP = LITERAL (Read)
`````````````````````
The name of the NDF array component for which statistics are required:
"Data", "Error", "Quality" or "Variance" (where "Error" is the
alternative to "Variance" and causes the square root of the variance
values to be taken before computing the statistics). If "Quality" is
specified, then the quality values are treated as numerical values (in
the range 0 to 255). ["Data"]



ESTIMATOR = LITERAL (Read)
``````````````````````````
The method to use for estimating the output pixel values. It can be
one of the following options. The first five are more for general
collapsing, and the remainder are for cube analysis. "Mean" -- Mean
value "WMean" -- Weighted mean in which each data value is weighted by
the reciprocal of the associated variance (not available for
COMP="Variance" or "Error"). "Mode" -- Modal value "Median" -- Median
value. Note that this is extremely memory and CPU intensive for large
datasets; use with care! If strange things happen, use "Mean" or try
"FastMed". "FastMed"-- Faster median using Wirth's algorithm for
selecting the kth value, rather than a full sort. Weighting is not
supported, thus this option is unavailable if both Parameter VARIANCE
is TRUE and the input NDF contains a VARIANCE component.
"Absdev" -- Mean absolute deviation from the unweighted mean. "Cmean"
-- Sigma-clipped mean. "Csigma" -- Sigma-clipped standard deviation.
"Comax" -- Co-ordinate of the maximum value. "Comin" -- Co-ordinate of
the minimum value. "FBad" -- Fraction of bad pixel values. "FGood" --
Fraction of good pixel values. "Integ" -- Integrated value, being the
sum of the products of the value and pixel width in world co-
ordinates. "Iwc" -- Intensity-weighted co-ordinate, being the sum of
each value times its co-ordinate, all divided by the integrated value
(see the "Integ" option). "Iwd" -- Intensity-weighted dispersion of
the co-ordinate, normalised like "Iwc" by the integrated value. "Max"
-- Maximum value. "Min" -- Minimum value. "NBad" -- Number of bad
pixel values. "NGood" -- Number of good pixel values. "Rms" -- Root-
mean-square value. "Sigma" -- Standard deviation about the unweighted
mean. "Sum" -- The total value. ["Mean"]



HIGH = LITERAL (Read)
`````````````````````
A formatted value for the axis specified by Parameter AXIS. For
example, if AXIS is 3 and the current Frame of the input NDF has axes
RA/DEC/Wavelength, then a wavelength value should be supplied. If, on
the other hand, the current Frame in the NDF was the PIXEL Frame, then
a pixel co-ordinate value would be required for the third axis (note,
the pixel with index I covers a range of pixel co-ordinates from (I-1)
to I). Together with Parameter LOW, this parameter gives the range of
axis values to be compressed. Note, HIGH and LOW should not be equal.
If a null value (!) is supplied for either HIGH or LOW, the entire
range of the axis is collapsed. [!]



IN = NDF (Read)
```````````````
The input NDF.



LOW = LITERAL (Read)
````````````````````
A formatted value for the axis specified by Parameter AXIS. For
example, if AXIS is 3 and the current Frame of the input NDF has axes
RA/DEC/Wavelength, then a wavelength value should be supplied. If, on
the other hand, the current Frame in the NDF was the PIXEL Frame, then
a pixel co-ordinate value would be required for the third axis (note,
the pixel with index I covers a range of pixel co-ordinates from (I-1)
to I). Together with Parameter HIGH, this parameter gives the range of
axis values to be compressed. Note, LOW and HIGH should not be equal.
If a null value (!) is supplied for either LOW or HIGH, the entire
range of the axis is collapsed. [!]



OUT = NDF (Write)
`````````````````
The output NDF.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



TRIM = _LOGICAL (Read)
``````````````````````
This parameter controls whether the collapsed axis should be removed
from the co-ordinate syatems describing the output NDF. If a TRUE
value is supplied, the collapsed WCS axis will be removed from the WCS
FrameSet of the output NDF, and the collapsed pixel axis will also be
removed from the NDF, resulting in the output NDF having one fewer
pixel axes than the input NDF. If a FALSE value is supplied, the
collapsed WCS and pixel axes are retained in the output NDF, resulting
in the input and output NDFs having the same number of pixel axes. In
this case, the pixel-index bounds of the collapse axis will be set to
(1:1) in the output NDF (that is, the output NDF will span only a
single pixel on the collapse axis). Thus, setting TRIM to FALSE allows
information to be retained about the range of values over which the
collapse occurred. [TRUE]



VARIANCE = _LOGICAL (Read)
``````````````````````````
A flag indicating whether a variance array present in the NDF is used
to weight data values while forming the estimator's statistic, and to
derive output variance. If VARIANCE is TRUE and the NDF contains a
variance array, this array will be used to define the weights,
otherwise all the weights will be set equal. By definition this
parameter is set to FALSE when COMP is "Variance" or "Error".
The VARIANCE parameter is ignored and set to FALSE when there are more
than 300 pixels along the collapse axis and ESTIMATOR is "Median",
"Mode", "Cmean", or "Csigma". This prevents the covariance matrix from
being huge. For "Median" estimates of variance come from mean variance
instead. The other affected estimators switch to use equal weighting.
[TRUE]



WCSATTS = GROUP (Read)
``````````````````````
A group of attribute settings which will be used to make temporary
changes to the properties of the current co-ordinate Frame in the WCS
FrameSet before it is used. Supplying a list of attribute values for
this parameter is equivalent to invoking WCSATTRIB on the input NDF
prior to running this command, except that no permanent change is made
to the NDF (however the changes are propagated through to the output
NDF).
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings overriding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a Frame attribute, and <value> is the
value to assign to the attribute. Any unspecified attributes will
retain the value they have in the supplied NDF. No attribute values
will be changed if a null value (!) is supplied. Any unrecognised
attributes are ignored (no error is reported). [!]



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
collapse m31 profile axis=RA low="0:36:01" high="0:48:00"
Collapses the two-dimensional NDF called m31 along the right-ascension
axis, from "0:36:01" to "0:48:00", and puts the result in an output
NDF called profile.
collapse cube slab lambda 4500 4550
The current Frame in the input three-dimensional NDF called cube has
axes with labels "RA", "DEC" and "Lambda", with the lambda axis being
parallel to the third pixel axis. The above command extracts a slab of
the input cube between wavelengths 4500 and 4550 Angstroms, and
collapses this slab into a single two-dimensional output NDF called
slab with RA and DEC axes. Each pixel in the output NDF is the mean of
the corresponding input pixels with wavelengths between 4500 and 4550
Angstroms.
collapse cube slab 3 4500 4550
The same as the previous example except the axis to collapse along is
specified by index (3) rather than label (lambda).
collapse cube slab 3 101.0 134.0
This is the same as the second example, except that the current Frame
in the input NDF has been set to the PIXEL Frame (using WCSFRAME), and
so the high and low axis values are specified in pixel co-ordinates
instead of Angstroms. Note the difference between floating-point pixel
co-ordinates, and integer pixel indices (for instance the pixel with
index 10 extends from pixel co-ordinate 9.0 to pixel co-ordinate
10.0).
collapse cube slab 3 low=99.0 high=100.0
This is the same as the second example, except that a single pixel
plane in the cube (pixel 100) is used to create the output NDF.
Following the usual definition of pixel co-ordinates, pixel 100
extends from pixel co-ordinate 99.0 to pixel co-ordinate 100.0. So the
given HIGH and LOW values encompass the single pixel plane at pixel
100.



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

+ A warning is issued (at the normal reporting level) whenever any
  output values are set bad because there are too few contributing data
  values. This reports the fraction of flagged output data generated by
  the WLIM parameter's threshold.

No warning is given when Parameter WLIM=0. Input data containing only
bad values are not counted in the flagged fraction, since no potential
good output value has been lost.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSFRAME, COMPAVE, COMPICK, COMPADD.


Copyright
~~~~~~~~~
Copyright (C) 2000-2001, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2005-2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2007-2009, 2013, 2018 Science and
Technology Facilities Council. All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, VARIANCE, LABEL,
TITLE, UNITS, WCS, and HISTORY components of the input NDF and
propagates all extensions. QUALITY is not propagated.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




