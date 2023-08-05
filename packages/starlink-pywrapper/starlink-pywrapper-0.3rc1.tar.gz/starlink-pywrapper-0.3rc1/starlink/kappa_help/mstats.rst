

MSTATS
======


Purpose
~~~~~~~
Calculate statistics over a group of data arrays or points


Description
~~~~~~~~~~~
This application calculates cumulative statistics over a group of
NDFs. It can either generate the statistics of each corresponding
pixel in the input array components and output a new NDF with array
components containing the result, or calculate statistics at a single
point specified in the current co-ordinate Frame of the input NDFs.
In array mode (SINGLE=FALSE), statistics are calculated for each pixel
in one of the array components (DATA, VARIANCE or QUALITY) accumulated
over all the input NDFs and written to an output NDF; each pixel of
the output NDF is a result of combination of pixels with the same
Pixel co-ordinates in all the input NDFs. There is a selection of
statistics available to form the output values.
The input NDFs must all have the same number of dimensions, but need
not all be the same shape. The shape of the output NDF can be set to
either the intersection or the union of the shapes of the input NDFs
using the TRIM parameter.
In single pixel mode (SINGLE=TRUE) a position in the current co-
ordinate Frame of all the NDFs is given, and the value at the pixel
covering this point in each of the input NDFs is accumulated to form
the results that comprise the mean, variance, and median. These
statistics, and if environment variable MSG_FILTER is set to VERBOSE,
the value of each contributing pixel, is reported directly to you.


Usage
~~~~~


::

    
       mstats in out [estimator]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be analysed. It may be "Data", "Quality",
"Variance", or "Error" (where "Error" is an alternative to "Variance"
and causes the square root of the variance values to be used). If
"Quality" is specified, then the quality values are treated as
numerical values (in the range 0 to 255). In cases other than "Data",
which is always present, a missing component will be treated as having
all pixels set to the `bad' value. ["Data"]



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



ESTIMATOR = LITERAL (Read)
``````````````````````````
The method to use for estimating the output pixel values from the
multiple input pixels at each pixel index. It can be one of the
following options. "Mean" -- Mean value "WMean" -- Weighted mean in
which each data value is weighted by the reciprocal of the associated
variance. (2) "Mode" -- Modal value (4) "Median" -- Median value. Note
that this is extremely memory and CPU intensive for large datasets;
use with care! If strange things happen, use "Mean". (3) "Absdev" --
Mean absolute deviation from the unweighted mean. (2) "Cmean" --
Sigma-clipped mean. (4) "Csigma" -- Sigma-clipped standard deviation.
(4) "Comax" -- Co-ordinate of the maximum value. "Comin" -- Co-
ordinate of the minimum value. "FBad" -- Fraction of bad pixel values.
"FGood" -- Fraction of good pixel values. "Integ" -- Integrated value,
being the sum of the products of the value and pixel width in world
co-ordinates. "Iwc" -- Intensity-weighted co-ordinate, being the sum
of each value times its co-ordinate, all divided by the integrated
value (see the "Integ" option). "Iwd" -- Intensity-weighted dispersion
of the co-ordinate, normalised like "Iwc" by the integrated value. (4)
"Max" -- Maximum value. "Min" -- Minimum value. "NBad" -- Number of
bad pixel values. "NGood" -- Number of good pixel values. "Rms" --
Root-mean-square value. (4) "Sigma" -- Standard deviation about the
unweighted mean. (4) "Sum" -- The total value.
Where needed, the co-ordinates are the indices of the input NDFs in
the supplied order. Thus the calculations behave like the NDFs were
stacked one upon another to form an extra axis, and that axis had GRID
co-ordinates. Care using wildcards is necessary, to achieve a specific
order, say for a time series, and hence assign the desired co-ordinate
for a each NDF. Indirection through a text file is recommended.
The selection is restricted if there are only a few input NDFs. For
instance, measures of dispersion like "Sigma" and "Iwd" are
meaningless for combining only two NDFs. The minimum number of input
NDFs for each estimator is given in parentheses in the list above.
Where there is no number, there is no restriction. If you supply an
unavailable option, you will be informed, and presented with the
available options. ["Mean"]



IN = GROUP (Read)
`````````````````
A group of input NDFs. They may have different shapes, but must all
have the same number of dimensions. This should be given as a comma
separated list, in which each list element can be one of the
following.


+ An NDF name, optionally containing wild-cards and/or regular
expressions ("*", "?", "[a-z]" etc.).
+ The name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  wild-cards, etc.), or another file specification (preceded by an up-
  arrow). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a minus sign "-",
then the user is re-prompted for further input until a value is given
which does not end with a minus sign. All the images given in this way
are concatenated into a single group.



MEAN = _DOUBLE (Write)
``````````````````````
An output parameter to which is written the mean pixel value, if
SINGLE=TRUE.



MEDIAN = _DOUBLE (Write)
````````````````````````
An output parameter to which is written the median pixel value, if
SINGLE=TRUE.



OUT = NDF (Read)
````````````````
The name of an NDF to receive the results. Each pixel of the DATA (and
perhaps VARIANCE) component represents the statistics of the
corresponding pixels of the input NDFs. Only used if SINGLE=FALSE.



POS = LITERAL (Read)
````````````````````
In Single pixel mode (SINGLE=TRUE), this parameter gives the position
in the current co-ordinate Frame at which the statistics should be
calculated (supplying a colon ":" will display details of the required
co-ordinate Frame). The position should be supplied as a list of
formatted axis values separated by spaces or commas. The pixel
covering this point in each input array, if any, will be used.



SINGLE = _LOGICAL (Read)
````````````````````````
Whether the statistics should be calculated in Single pixel mode or
Array mode. If SINGLE=TRUE, then the POS parameter will be used to get
the point to which the statistics refer, but if SINGLE=FALSE an output
NDF will be generated containing the results for all the pixels.
[FALSE]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. ["KAPPA - Mstats"]



TRIM = _LOGICAL (Read)
``````````````````````
This parameter controls the shape of the output NDF. If TRIM=TRUE,
then the output NDF is the shape of the intersection of all the input
NDFs, i.e. only pixels which appear in all the input arrays will be
represented in the output. If TRIM=FALSE, the output is the shape of
the union of the inputs, i.e. every pixel which appears in the input
arrays will be represented in the output. [TRUE]



VAR = _DOUBLE (Write)
`````````````````````
An output parameter to which is written the variance of the pixel
values, if SINGLE=TRUE.



VARIANCE = _LOGICAL (Read)
``````````````````````````
A flag indicating whether a variance array present in the NDF is used
to weight the array values while forming the estimator's statistic,
and to derive output variance. If VARIANCE is TRUE and all the input
NDFs contain a variance array, this array will be used to define the
weights, otherwise all the weights will be set equal. [TRUE]



WLIM = _REAL (Read)
```````````````````
If the input NDFs contain bad pixels, then this parameter may be used
to determine at a given pixel location the number of good pixels which
must be present within the input NDFs before a valid output pixel is
generated. It can be used, for example, to prevent output pixels from
being generated in regions where there are relatively few good pixels
to contribute to the result of combining the input NDFs.
WLIM specifies the minimum fraction of good pixels which must be
present in order to generate a good output pixel. If this specified
minimum fraction of good input pixels is not present, then a bad
output pixel will result, otherwise a good output value will be
calculated. The value of this parameter should lie between 0.0 and 1.0
(the actual number used will be rounded up if necessary to correspond
to at least one pixel). [0.3]



Examples
~~~~~~~~
mstats idat* ostats
This calculates the mean of each pixel in the Data arrays of all the
NDFs in the current directory with names that start "idat", and writes
the result in a new NDF called "ostats". The shape of ostats will be
the intersection of the volumes of all the indat* NDFs.
mstats idat* ostats trim=false
This does the same as the previous example, except that the output NDF
will be the `union' of the volumes of the input NDFs, that is a cuboid
with lower bounds as low as the lowest pixel bound of the input NDFs
in each dimension and with upper bounds as high as the highest pixel
bound in each dimension.
mstats idat* ostats variance
This is like the first example except variance information present is
used to weight the data values.
mstats idat* ostats comp=variance variance
This does the same as the first example except that statistics are
calculated on the VARIANCE components of all the input NDFs. Thus the
pixels of the VARIANCE component of "ostats" will be the variances of
the variances of the input data.
mstats m31* single=true pos="0:42:38,40:52:20"
This example is analysing the pixel brightness at the indicated sky
position in a number of NDFs whose name start with "m31", which all
have SKY as their current co-ordinate Frame. The mean and variance of
the pixels at that position in all the NDFs are printed to the screen.
If the reporting level is verbose, the command also prints the value
of the sampled pixel in each of the NDFs. For those in which the pixel
at the selected position is bad or falls outside the NDF, this is also
indicated.
mstats in="arr1,arr2,arr3" out=middle estimator=median wlim=1.0
This example calculates the medians of the DATA components of the
three named NDFs and writes them into a new NDF called "middle". All
input values must be good to form a non-bad output value.



Notes
~~~~~


+ A warning is issued (at the normal reporting level) whenever any
  output values are set bad because there are too few contributing data
  values. This reports the fraction of flagged output data generated by
  the WLIM parameter's threshold.

No warning is given when parameter WLIM=0. Input data containing only
bad values are not counted in the flagged fraction, since no potential
good output value has been lost.


+ For SINGLE=TRUE the value of the MSG_FILTER environment variable is
  used to output messages. If it is QUIET, nothing is reported on the
  screen. If it is undefined, NORMAL or VERBOSE, the statistics are
  reported. If it is VERBOSE, the individual pixel values are also
  reported.




Related Applications
~~~~~~~~~~~~~~~~~~~~
CCDPACK: MAKEMOS, MAKECAL, MAKEFLAT.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2008, 2009, 2012, 2014, Science & Technology Facilities
Council. All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, VARIANCE, QUALITY,
LABEL, TITLE, UNITS, WCS, and HISTORY components of the first input
NDF and propagates all its extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Calculations are
performed using the more appropriate of the data types real or double
precision. If the input NDFs' structures contain values with other
data types, then conversion will be performed as necessary.
+ Up to six NDF dimensions are supported.




