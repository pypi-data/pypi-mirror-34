

HISTAT
======


Purpose
~~~~~~~
Computes ordered statistics for an NDF's pixels using an histogram


Description
~~~~~~~~~~~
This application computes and displays simple ordered statistics for
the pixels in an NDF's data, quality, error, or variance array. The
statistics available are:

+ the pixel sum,
+ the pixel mean,
+ the pixel median,
+ the pixel mode,
+ the pixel value at selected percentiles,
+ the value and position of the minimum- and maximum-valued pixels,
+ the total number of pixels in the NDF,
+ the number of pixels used in the statistics, and
+ the number of pixels omitted.

The mode may be obtained in different ways (see Parameter METHOD).


Usage
~~~~~


::

    
       histat ndf [comp] [percentiles] [logfile]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The name of the NDF array component for which statistics are required.
The options are limited to the arrays within the supplied NDF. In
general the value may "Data", "Error", "Quality" or "Variance" (note
that "Error" is the alternative to "Variance" and causes the square
root of the variance values to be taken before computing the
statistics). If "Quality" is specified, then the quality values are
treated as numerical values (in the range 0 to 255). ["Data"]



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
The median value of all the valid pixels in the NDF array.



METHOD = LITERAL (Read)
```````````````````````
The method used to evaluate the mode. The choices are as follows.


+ "Histogram" -- This finds the peak of an optimally binned histogram,
the mode being the central value of that bin. The number of bins may
be altered given through Parameter NUMBIN, however it is recommended
to use the optimal binsize derived from the prescription of Freedman &
Diatonis.
+ "Moments" -- As "Histogram" but the mode is the weighted centroid
from the moments of the peak bin and its neighbours. The neighbours
are those bins either side of the peak in a continuous sequence whose
membership exceeds the peak value less three times the Poisson error
of the peak bin. Thus it gives an interpolated mode and does reduce
the effect of noise.
+ "Pearson" -- This uses the 3 * median $-$ 2 * mean formula devised
  by Pearson. See the first two References. This assumes that the median
  is bracketed by the mode and mean and only a mildly skew unimodal
  distribution. This often applies to an image of the sky.

["Moments"]



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



MODE = _DOUBLE (Write)
``````````````````````
The modal value of all the valid pixels in the NDF array. The method
used to obtain the mode is governed by Parameter METHOD.



NDF = NDF (Read)
````````````````
The NDF data structure to be analysed.



NUMBAD = _INTEGER (Write)
`````````````````````````
The number of pixels which were either not valid or were rejected from
the statistics during iterative K-sigma clipping.



NUMBIN = _INTEGER (Read)
````````````````````````
The number of histogram bins to be used for the coarse histogram to
evaluate the mode. It is only accessed when METHOD="Histogram" or
"Moments". This must lie in the range 10 to 10000. The suggested
default is calculated dynamically depending on the data spread and
number of values (using the prescription of Freedman & Diaconis). For
integer data it is advisble to use the dynamic default or an integer
multiple thereof to avoid creating non-integer wide bins. []



NUMGOOD = _INTEGER (Write)
``````````````````````````
The number of NDF pixels which actually contributed to the computed
statistics.



NUMPIX = _INTEGER (Write)
`````````````````````````
The total number of pixels in the NDF (both good and bad).



PERCENTILES( 100 ) = _REAL (Read)
`````````````````````````````````
A list of percentiles to be found. None are computed if this parameter
is null (!). The percentiles must be in the range 0.0 to 100.0 [!]



PERVAL() = _DOUBLE (Write)
``````````````````````````
The values of the percentiles of the good pixels in the NDF array.
This parameter is only written when one or more percentiles have been
requested.



TOTAL = _DOUBLE (Write)
```````````````````````
The sum of the pixel values in the NDF array.



Examples
~~~~~~~~
histat image
Computes and displays simple ordered statistics for the data array in
the NDF called image.
histat image method=his
As above but the mode is the centre of peak bin in the optimally
distributed histogram rather than sub-bin interpolated using
neighbouring bins.
histat ndf=spectrum variance
Computes and displays simple ordered statistics for the variance array
in the NDF called spectrum.
histat spectrum error
Computes and displays ordered statistics for the variance array in the
NDF called spectrum, but takes the square root of the variance values
before doing so.
histat halley logfile=stats.dat method=pearson
Computes ordered statistics for the data array in the NDF called
halley, and writes the results to a logfile called stats.dat. The mode
is derived using the Pearson formula.
histat ngc1333 percentiles=[0.25,0.75]
Computes ordered statistics for the data array in the NDF called
ngc1333, including the quartile values.



Notes
~~~~~


+ Where the histogram contains a few extreme outliers, the histogram
limits are adjusted to reduce greatly the bias upon the statistics,
even if a chosen percentile corresponds to an extreme outlier. The
outliers are still accounted in the median and percentiles. The
histogram normally uses 10000 bins. For small arrays the number of
bins is at most a half of the number of array elements. Integer arrays
have a minimum bin width of one; this can also reduce the number of
bins. The goal is to avoid most histogram bins being empty
artificially, since the sparseness of the histogram is the main
criterion for detecting outliers. Outliers can also be removed
(flagged) via application THRESH prior to using this application.
+ There is quantisation bias in the statistics, but for non-
  pathological distributions this should be insignificant. Accuracy to
  better than 0.01 of a percentile is normal. Linear interpolation
  within a bin is used, so the largest errors arise near the median.




References
~~~~~~~~~~
Moroney, M.J., 1957, "Facts from Figures" (Pelican) Goad, L.E. 1980,
"Statistical Filtering of Cosmic-Ray Events from Astronomical CCD
Images in "Applications of Digital Image Processing to Astronomy",
SPIE 264, 136. Freedman, D. & Diaconis, P. 1981, "On the histogram as
a density estimator: L2 theory", Zeitschrift fur
Wahrscheinlichkeitstheorie und verwandte Gebiete 57, 453.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISTOGRAM, MSTATS, NDFTRACE, NUMB, STATS; ESP: HISTPEAK;
Figaro: ISTAT.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1994 Science & Engineering Research Council.
Copyright (C) 2000, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2007, 2009, 2010, 2012 Science & Technology Facilities
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


+ This routine correctly processes the AXIS, WCS, DATA, VARIANCE,
QUALITY, TITLE, and HISTORY components of the NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
performed using single- or double-precision floating point, as
appropriate.
+ Any number of NDF dimensions is supported.




