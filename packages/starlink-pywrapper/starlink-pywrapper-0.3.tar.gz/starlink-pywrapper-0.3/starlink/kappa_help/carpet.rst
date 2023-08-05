

CARPET
======


Purpose
~~~~~~~
Creates a cube representing a carpet plot of an image


Description
~~~~~~~~~~~
This application creates a new three-dimensional NDF from an existing
two-dimensional NDF. The resulting NDF can, for instance, be viewed
with the three-dimensional iso-surface facilities of the GAIA image
viewer, in order to create a display similar to a "carpet plot" of the
image (the iso-surface at value zero represents the input image data
values).
The first two pixel axes (X and Y) in the output cube correspond to
the pixel axes in the input image. The third pixel axis (Z) in the
output cube is proportional to data value in the input image. The
value of a pixel in the output cube measures the difference between
the data value implied by its Z-axis position, and the data value of
the corresponding pixel in the input image. Two schemes are available
(see Parameter MODE): the output pixel values can be either simply the
difference between these two data values, or the difference divided by
the standard deviation at the corresponding pixel in the input image
(as determined either from the VARIANCE component in the input NDF or
by Parameter SIGMA).


Usage
~~~~~


::

    
       carpet in out [ndatapix] [range] [mode] [sigma]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input two-dimensional NDF.



MODE = LITERAL (Read)
`````````````````````
Determines how the pixel values in the output cube are calculated.


+ "Data" -- the value of each output pixel is equal to the difference
between the data value implied by its position along the data value
axis, and the value of the corresponding pixel in the input image.
+ "Sigma" -- this is the same as "Data" except that the output pixel
  values are divided by the standard deviation implied either by the
  VARIANCE component of the input image, or by the SIGMA parameter.

["Data"]



NDATAPIX = _INTEGER (Read)
``````````````````````````
The number of pixels to use for the data value axis in the output
cube. The pixel origin of this axis will be 1. The dynamic default is
the square root of the number of pixels in the input image. This gives
a fairly "cubic" output cube. []



OUT = NDF (Write)
`````````````````
The output three-dimensional NDF.



RANGE = LITERAL (Read)
``````````````````````
RANGE specifies the range covered by the data value axis (i.e. the
third pixel axis) in the output cube. The supplied string should
consist of up to three sub-strings, separated by commas. For all but
the option where you give explicit numerical limits, the first sub-
string must specify the method to use. If supplied, the other two sub-
strings should be numerical values as described below (default values
will be used if these sub-strings are not provided). The following
options are available.


+ lower,upper -- You can supply explicit lower and upper limiting
values. For example, "10,200" would set the lower limit on the output
data axis to 10 and its upper limit to 200. No method name prefixes
the two values. If only one value is supplied, the "Range" method is
adopted. The limits must be within the dynamic range for the data type
of the input NDF array component.
+ "Percentiles" -- The default values for the output data axis range
are set to the specified percentiles of the input data. For instance,
if the value "Per,10,99" is supplied, then the lowest 10% and highest
1% of the data values are beyond the bounds of the output data value
axis. If only one value, p1, is supplied, the second value, p2,
defaults to (100 - p1). If no values are supplied, the values default
to "5,95". Values must be in the range 0 to 100.
+ "Range" -- The minimum and maximum input data values are used. No
other sub-strings are needed by this option. Null (!) is a synonym for
the "Range" method.
+ "Sigmas" -- The limits on the output data value axis are set to the
  specified numbers of standard deviations below and above the mean of
  the input data. For instance, if the supplied value is "sig,1.5,3.0",
  then the data value axis extends from the mean of the input data minus
  1.5 standard deviations to the mean plus 3 standard deviations. If
  only one value is supplied, the second value defaults to the supplied
  value. If no values are supplied, both default to "3.0".

The limits adopted for the data value axis are reported unless
parameter RANGE is specified on the command line. In this case values
are only calculated where necessary for the chosen method.
The method name can be abbreviated to a single character, and is case
insensitive. The initial default value is "Range". The suggested
defaults are the current values, or ! if these do not exist. [current
value]



SIGMA = _REAL (Read)
````````````````````
The standard deviation to use if Parameter MODE is set to "Sigma". If
a null (!) value is supplied, the standard deviations implied by the
VARIANCE component in the input image are used (an error will be
reported if the input image does not have a VARIANCE component). If a
SIGMA value is supplied, the same value is used to scale all output
pixels. [!]



Examples
~~~~~~~~
carpet m31 m31-cube mode=sigma
Asssuming the two-dimensional NDF in file m31.sdf contains a VARIANCE
component, this will create a three-dimensional NDF called m31-cube in
which the third pixel axis corresponds to data value in NDF m31, and
each output pixel value is the number of standard deviations of the
pixel away from the corresponding input data value. If you then use
GAIA to view the cube, an iso-surface at value zero will be a carpet
plot of the data values in m31, an iso-surface at value -1.0 will be a
carpet plot showing data values one standard deviation below the m31
data values, and an iso-surface at value +1.0 will be a carpet plot
showing data values one sigma above the m31 data values. This can help
to visualise the errors in an image.



Copyright
~~~~~~~~~
Copyright (C) 2009, 2011 Science & Technology Facilities Council. All
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


+ Any VARIANCE and QUALITY components in the input image are not
  propagated to the output cube.




