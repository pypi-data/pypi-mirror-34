

FINDBACK
========


Purpose
~~~~~~~
Estimate the background in an NDF by removing small scale structure


Description
~~~~~~~~~~~
This application uses spatial filtering to remove structure with a
scale size less than a specified size from a 1, 2, or 3 dimensional
NDF, thus producing an estimate of the local background within the
NDF.
The algorithm proceeds as follows. A filtered form of the input data
is first produced by replacing every input pixel by the minimum of the
input values within a rectangular box centred on the pixel. This
filtered data is then filtered again, using a filter that replaces
every pixel value by the maximum value in a box centred on the pixel.
This produces an estimate of the lower envelope of the data, but
usually contains unacceptable sharp edges. In addition, this filtered
data has a tendency to hug the lower envelope of the noise, thus
under-estimating the true background of the noise-free data. The first
problem is minimised by smoothing the background estimate using a
filter that replaces every pixel value by the mean of the values in a
box centred on the pixel. The second problem is minimised by
estimating the difference between the input data and the background
estimate within regions well removed from any bright areas. This
difference is then extrapolated into the bright source regions and
used as a correction to the background estimate. Specifically, the
residuals between the input data and the initial background estimate
are first formed, and residuals which are more than three times the
RMS noise are set bad. The remaining residuals are smoothed with a
mean filter. This smoothing will replace a lot of the bad values
rejected above, but may not remove them all. Any remaining bad values
are estimated by linear interpolation between the nearest good values
along the first axis. The interpolated residuals are then smoothed
again using a mean filter, to get a surface representing the bias in
the initial background estimate. This surface is finally added onto
the initial background estimate to obtain the output NDF.


Usage
~~~~~


::

    
       findback in out box
       



ADAM parameters
~~~~~~~~~~~~~~~



BOX() = _INTEGER (Read)
```````````````````````
The dimensions of each of the filters, in pixels. Each value should be
odd (if an even value is supplied, the next higher odd value will be
used). The number of values supplied should not exceed the number of
significant (i.e. more than one element) pixel axes in the input
array. If any trailing values of 1 are supplied, then each pixel value
on the corresponding axes will be fitted independently of its
neighbours. For instance, if the data array is 3-dimensional, and the
third BOX value is 1, then each x-y plane will be fitted independently
of the neighbouring planes. If the NDF has more than 1 pixel axis but
only 1 value is supplied, then the same value will be used for the
both the first and second pixel axes (a value of 1 will be assumed for
the third axis if the input array is 3-dimensional).



MSG_FILTER = _CHAR (Read)
`````````````````````````
Controls the amount of diagnostic information reported. This is the
standard messaging level. The default messaging level is NORM (2). A
value of NONE or 0 will suppress all screen output. VERB (3) will
indicate progress through the various stages of the algorithm. [NORM]



IN = NDF (Read)
```````````````
The input NDF.



RMS = _DOUBLE (Read)
````````````````````
Specifies a value to use as the global RMS noise level in the supplied
data array. The suggested default value is the square root of the mean
of the values in the input NDF's Variance component. If the NDF has no
Variance component, the suggested default is based on the differences
between neighbouring pixel values, measured over the entire input NDF.
If multiple slices within the NDF are to be processed independently
(see parameter BOX), it may be more appropriate for a separate default
RMS to be calculated for each slice. This will normally be the case if
the noise could be different in each of the slices. In such cases a
null (!) can be supplied for the RMS parameter, which forces a
separate default RMS value to be found and used for each slice. Any
pixel-to-pixel correlation in the noise can result in these defaults
being too low.



SUB = _LOGICAL (Read)
`````````````````````
If a TRUE value is supplied, the output NDF will contain the
difference between the supplied input data and the estimated
background. If a FALSE value is supplied, the output NDF will contain
the estimated background itself. [FALSE]



OUT = NDF (Write)
`````````````````
The output NDF containing either the estimated background, or the
background-subtracted input data, as specified by parameter SUB.



WLIM = _REAL (Read)
```````````````````
If the input NDF contains bad pixels, then this parameter may be used
to determine the number of good pixels which must be present within
the filter box before a valid output pixel is generated. It can be
used, for example, to prevent output pixels from being generated in
regions where there are relatively few good pixels to contribute to
the filtered result.
If a null (!) value is used for WLIM, the pattern of bad pixels is
propagated from the input NDF to the output NDF unchanged. In this
case, filtered output values are only calculated for those pixels
which are not bad in the input NDF.
If a numerical value is given for WLIM, then it specifies the minimum
fraction of good pixels which must be present in the filter box in
order to generate a good output pixel. If this specified minimum
fraction of good input pixels is not present, then a bad output pixel
will result, otherwise a filtered output value will be calculated. The
value of this parameter should lie between 0.0 and 1.0 (the actual
number used will be rounded up if necessary to correspond to at least
1 pixel). [0.3]



Notes
~~~~~


+ Smoothing cubes in 3 dimensions can be very slow.




Synopsis
~~~~~~~~
void findback( int *status );


Copyright
~~~~~~~~~
Copyright (C) 2009,2013 Science and Technology Facilities Council.
Copyright (C) 2006, 2007 Particle Physics & Astronomy Research
Council. All Rights Reserved.


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


