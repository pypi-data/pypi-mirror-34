

STATS
=====


Purpose
~~~~~~~
Computes simple statistics for an NDF's pixels


Description
~~~~~~~~~~~
This application computes and displays simple statistics for the
pixels in an NDF's data, quality or variance array. The statistics
available are:

+ the pixel sum,
+ the pixel mean,
+ the pixel population standard deviation,
+ the pixel population skewness and excess kurtosis,
+ the value and position of the minimum- and maximum-valued pixels,
+ the total number of pixels in the NDF,
+ the number of pixels used in the statistics, and
+ the number of pixels omitted.

Iterative K-sigma clipping may also be applied as an option (see
Parameter CLIP).
Order statistics (median and percentiles) may optionally be derived
and displayed (see Parameters ORDER and PERCENTILES). Although this
can be a relatively slow operation on large arrays, unlike application
HISTAT the reported order statistics are accurate, not approximations,
irrespective of the distribution of values being analysed.


Usage
~~~~~


::

    
       stats ndf [comp] [clip] [logfile]
       



ADAM parameters
~~~~~~~~~~~~~~~



CLIP( ) = _REAL (Read)
``````````````````````
An optional one-dimensional array of clipping levels to be applied,
expressed as standard deviations. If a null value is supplied for this
parameter (the default), then no iterative clipping will take place
and the statistics computed will include all the valid NDF pixels.
If an array of clipping levels is given, then the routine will first
compute statistics using all the available pixels. It will then reject
all those pixels whose values lie outside K standard deviations of the
mean (where K is the first value supplied) and will then re-evaluate
the statistics. This rejection iteration is repeated in turn for each
value in the CLIP array. A maximum of five values may be supplied, all
of which must be positive. [!]



COMP = LITERAL (Read)
`````````````````````
The name of the NDF array component for which statistics are required:
"Data", "Error", "Quality" or "Variance" (where "Error" is the
alternative to "Variance" and causes the square root of the variance
values to be taken before computing the statistics). If "Quality" is
specified, then the quality values are treated as numerical values (in
the range 0 to 255). ["Data"]



KURTOSIS = _DOUBLE (Write)
``````````````````````````
The population excess kurtosis of all the valid pixels in the NDF
array. This is the normal kurtosis minus 3, such that a Gaussian
distribution of values would generate an excess kurtosis of 0.



LOGFILE = FILENAME (Write)
``````````````````````````
A text file into which the results should be logged. If a null value
is supplied (the default), then no logging of results will take place.
[!]



MAXCOORD( ) = _DOUBLE (Write)
`````````````````````````````
A one-dimensional array of values giving the WCS co-ordinates of the
centre of the (first) maximum-valued pixel found in the NDF array. The
number of co-ordinates is equal to the number of NDF dimensions.



MAXIMUM = _DOUBLE (Write)
`````````````````````````
The maximum pixel value found in the NDF array.



MAXPOS( ) = _INTEGER (Write)
````````````````````````````
A one-dimensional array of pixel indices identifying the (first)
maximum-valued pixel found in the NDF array. The number of indices is
equal to the number of NDF dimensions.



MAXWCS = LITERAL (Write)
````````````````````````
The formatted WCS co-ordinates at the maximum pixel value. The
individual axis values are comma separated.



MEAN = _DOUBLE (Write)
``````````````````````
The mean value of all the valid pixels in the NDF array.



MEDIAN = _DOUBLE (Write)
````````````````````````
The median value of all the valid pixels in the NDF array when ORDER
is TRUE.



MINCOORD( ) = _DOUBLE (Write)
`````````````````````````````
A one-dimensional array of values giving the WCS co-ordinates of the
centre of the (first) minimum-valued pixel found in the NDF array. The
number of co-ordinates is equal to the number of NDF dimensions.



MINIMUM = _DOUBLE (Write)
`````````````````````````
The minimum pixel value found in the NDF array.



MINPOS( ) = _INTEGER (Write)
````````````````````````````
A one-dimensional array of pixel indices identifying the (first)
minimum-valued pixel found in the NDF array. The number of indices is
equal to the number of NDF dimensions.



MINWCS = LITERAL (Write)
````````````````````````
The formatted WCS co-ordinates at the minimum pixel value. The
individual axis values are comma separated.



NDF = NDF (Read)
````````````````
The NDF data structure to be analysed.



NUMBAD = _INTEGER (Write)
`````````````````````````
The number of pixels which were either not valid or were rejected from
the statistics during iterative K-sigma clipping.



NUMGOOD = _INTEGER (Write)
``````````````````````````
The number of NDF pixels which actually contributed to the computed
statistics.



NUMPIX = _INTEGER (Write)
`````````````````````````
The total number of pixels in the NDF (both good and bad).



ORDER = _LOGICAL (Read)
```````````````````````
Whether or not to calculate order statistics. If set TRUE the median
and optionally percentiles are determined and reported. [FALSE]



PERCENTILES( 100 ) = _REAL (Read)
`````````````````````````````````
A list of percentiles to be found. None are computed if this parameter
is null (!). The percentiles must be in the range 0.0 to 100.0 This
parameter is ignored unless ORDER is TRUE. [!]



PERVAL() = _DOUBLE (Write)
``````````````````````````
The values of the percentiles of the good pixels in the NDF array.
This parameter is only written when one or more percentiles have been
requested.



SIGMA = _DOUBLE (Write)
```````````````````````
The population standard deviation of the pixel values in the NDF
array.



SKEWNESS = _DOUBLE (Write)
``````````````````````````
The population skewness of all the valid pixels in the NDF array.



TOTAL = _DOUBLE (Write)
```````````````````````
The sum of the pixel values in the NDF array.



Examples
~~~~~~~~
stats image
Computes and displays simple statistics for the data array in the NDF
called image.
stats image order percentiles=[25,75]
As the previous example but it also reports the median, 25 and 75
percentiles.
stats ndf=spectrum variance
Computes and displays simple statistics for the variance array in the
NDF called spectrum.
stats spectrum error
Computes and displays statistics for the variance array in the NDF
called spectrum, but takes the square root of the variance values
before doing so.
stats halley logfile=stats.dat
Computes statistics for the data array in the NDF called halley, and
writes the results to a logfile called stats.dat.
stats ngc1333 clip=[3.0,2.8,2.5]
Computes statistics for the data array in the NDF called NGC1333,
applying three iterations of K-sigma clipping. The statistics are
first calculated for all the valid pixels in the data array. Those
pixels with values lying more than 3.0 standard deviations from the
mean are then rejected, and the statistics are re-computed. This
process is then repeated twice more, rejecting pixel values lying more
than 2.8 and 2.5 standard deviations from the mean. The final
statistics are displayed.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISTAT, NDFTRACE; Figaro: ISTAT.


Copyright
~~~~~~~~~
Copyright (C) 1991-1992 Science & Engineering Research Council.
Copyright (C) 2004 Central Laboratory of the Research Councils.
Copyright (C) 2007, 2009, 2010. 2013 Science & Technology Facilities
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
TITLE, and HISTORY components of the NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
performed using double-precision floating point.
+ Any number of NDF dimensions is supported.




