

SURFIT
======


Purpose
~~~~~~~
Fits a polynomial or bi-cubic spline surface to two-dimensional data
array


Description
~~~~~~~~~~~
The background of a two-dimensional data array in the supplied NDF
structure is estimated by condensing the array into equally sized
rectangular bins, fitting a spline or polynomial surface to the bin
values, and finally evaluating the surface for each pixel in the data
array.
There is a selection of estimators by which representative values for
each bin are determined. There are several options to make the fit
more accurate. Values beyond upper and lower thresholds may be
excluded from the binning. Bad pixels are also excluded, so prior
masking may help to find the background more rapidly. Kappa-sigma
clipping of the fitted bins is available so that the fit is not biased
by anomalous bins, such as those entirely within an extended object.
If a given bin contains more than a prescribed fraction of bad pixels,
it is excluded from the fit.
The data array representing the background is evaluated at each pixel
by one of two methods. It is written to the output NDF structure.
The raw binned data, the weights, the fitted binned data and the
residuals to the fit may be written to a logfile. This also keeps a
record of the input parameters and the rms error of the fit.


Usage
~~~~~


::

    
       surfit in out [fittype] [estimator] [bindim] [evaluate]
       



ADAM parameters
~~~~~~~~~~~~~~~



BINDIM() = _INTEGER (Read)
``````````````````````````
The x-y dimensions of a bin used to estimate the local background. If
you supply only one value, it is used for both dimensions. The minimum
value is 2. The maximum may be constrained by the number of polynomial
terms, such that in each direction there are at least as many bins as
terms. If a null (!) value is supplied, the value used is such that 32
bins are created along each axis. [!]



CLIP() = _REAL (Read)
`````````````````````
Array of limits for progressive clipping of pixel values during the
binning process in units of standard deviation. A null value means
only unclipped statistics are computed and presented. Between one and
five values may be supplied. [2,3]



ESTIMATOR = LITERAL (Read)
``````````````````````````
The estimator for the bin. It must be one of the following values:
"Mean" for the mean value, "Ksigma" for the mean with kappa-sigma
clipping; "Mode" for the mode, and "Median" for the median. "Mode" is
only available when there are at least twelve pixels in a bin. If a
null (!) value is supplied, "Median" is used if there are fewer than 6
values in a bin, and "Mode" is used otherwise. [!]



EVALUATE = LITERAL (Read)
`````````````````````````
The method by which the resulting data array is to be evaluated from
the surface-fit. It must be either "Interpolate" where the values at
the corners of the bins are derived first, and then the pixel values
are found by linear interpolation within those bins; or "All" where
the surface-fit is evaluated for every pixel. The latter is slower,
but can produce more-accurate results, unless the surface is well
behaved. The default is the current value, which is initially set to
"Interpolate". []



FITCLIP() = _REAL (Read)
````````````````````````
Array of limits for progressive clipping of the binned array in units
of the rms deviation of the fit. A null value (!) means no clipping of
the binned array will take place. Between 1 and 5 values may be
supplied. The default is the current value, which is ! initially. []



FITTYPE = LITERAL (Read)
````````````````````````
The type of fit. It must be either "Polynomial" for a Chebyshev
polynomial or "Spline" for a bi-cubic spline. The default is the
current value, which initially is "Spline". []



GENVAR = _LOGICAL (Read)
````````````````````````
If TRUE, a constant variance array is created in the output NDF
assigned to the mean square surface-fit error. [FALSE]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the file to log the binned array and errors before and after
fitting. If null, there will be no logging. [!]



IN = NDF (Read)
```````````````
NDF containing the two-dimensional data array to be fitted.



KNOTS( 2 ) = _INTEGER (Read)
````````````````````````````
The number of interior knots used for the bi-cubic-spline fit along
the x and y axes. These knots are equally spaced within the image.
Both values must be in the range 0 to 11. If you supply a single
value, it applies to both axes. Thus 1 creates one interior knot,
[5,4] gives 5 along the x axis and 4 along the y direction. Increasing
this parameter values increases the flexibility of the surface.
Normally, 4 is a reasonable value. The upper limit of acceptable
values will be reduced along each axis when its binned array dimension
is fewer than 29. KNOTS is only accessed when FITTYPE="Spline". The
default is the current value, which is 4 initially. []



ORDER( 2 ) = _INTEGER (Read)
````````````````````````````
The orders of the fits along the x and y directions. Both values must
be in the range 0 to 14. If you supply a single single value, it
applies to both axes. Thus 0 gives a constant, [3,1] gives a cubic
along the x direction and a linear fit along the y. Increasing this
parameter values increases the flexibility of the surface. The upper
limit of acceptable values will be reduced along each axis when its
binned array dimension is fewer than 29. ORDER is only accessed when
FITTYPE="Polynomial". The default is the current value, which is 4
initially. []



OUT = NDF (Write)
`````````````````
NDF to contain the fitted two-dimensional data array.



RMS = _REAL (Write)
```````````````````
An output parameter in which is stored the RMS deviation of the fit
from the original data (per pixel).



THRHI = _REAL (Read)
````````````````````
Upper threshold above which values will be excluded from the analysis
to derive representative values for the bins. If it is null (!) there
will be no upper threshold. [!]



THRLO = _REAL (Read)
````````````````````
Lower threshold below which values will be excluded from the analysis
to derive representative values for the bins. If it is null (!) there
will be no lower threshold. [!]



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



WLIM = _REAL (Read)
```````````````````
The minimum fraction of good pixels in a bin that permits the bin to
be included in the fit. Here good pixels are ones that participated in
the calculation of the bin's representative value. So they exclude
both bad pixels and ones rejected during estimation (e.g. ones beyond
the thresholds or were clipped). [!]



Examples
~~~~~~~~
surfit comaB comaB_bg
This calculates the surface fit to the two-dimensional NDF called
comaB using the current defaults. The evaluated fit is stored in the
NDF called comaB_bg.
surfit comaB comaB_bg poly median order=5 bindim=[24,30]
As above except that 5th-order polynomial fit is chosen, the median is
used to derive the representative value for each bin, and the binning
size is 24 pixels along the first axis, and 32 pixels along the
second.
surfit comaB comaB_bg fitclip=[2,3] logfile=comaB_fit.lis
As the first example except that the binned array is clipped at 2 then
3 standard deviations to remove outliers before the final fit is
computed. The text file comaB_fit.lis records a log of the surface
fit.
surfit comaB comaB_bg estimator=ksigma clip=[2,2,3]
As the first example except that the representative value of each bin
is the mean after clipping twice at 2 then once at 3 standard
deviations.
surfit in=irasorion out=sback evaluate=all fittype=s knots=7
This calculates the surface fit to the two-dimensional NDF called
irasorion. The fit is evaluated at every pixel and the resulting array
stored in the NDF called sback. A spline with seven knots along each
axis is used to fit the surface.



Notes
~~~~~
A polynomial surface fit is stored in a SURFACEFIT extension,
component FIT of type POLYNOMIAL, variant CHEBYSHEV or BSPLINE.
For further details of the CHEBYSHEV variant see SGP/38. The CHEBYSHEV
variant includes the fitting variance for each coefficient.
The BSPLINE variant structure is provisional. It contain the spline
coefficients in the two-dimensional DATA_ARRAY component, the knots in
XKNOTS and YKNOTS arrays, and a scaling factor to restore the original
values after spline evaluation recorded in component SCALE. All of
these components have type _REAL.
Also stored in the SURFACEFIT extension is the r.m.s. deviation of
data values compared with the fit (component RMS); and the co-ordinate
system component COSYS, set to "GRID".


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDMASK, FITSURFACE, MAKESURFACE, REGIONMASK.


Copyright
~~~~~~~~~
Copyright (C) 1996, 1998, 2000, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2007-2010 Science & Technology
Facilities Council. All Rights Reserved.


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
TITLE, UNITS, WCS and HISTORY components of the input NDF. Any input
VARIANCE is ignored.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single- or double-precision floating point for FITTYPE
  = "Spline" or "Polynomial" respectively. The output NDF's DATA and
  VARIANCE components have type _REAL (single-precision).




