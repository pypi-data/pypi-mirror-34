

MFITTREND
=========


Purpose
~~~~~~~
Fits independent trends to data lines that are parallel to an axis


Description
~~~~~~~~~~~
This routine fits trends to all lines of data in an NDF that lie
parallel to a chosen axis. The trends are characterised by polynomials
of order up to 15, or by cubic splines. The fits can be restricted to
use data that only lies within a series of co-ordinate ranges along
the selected axis.
The ranges may be determined automatically. There is a choice of
tunable approaches to mask regions to be excluded from the fitting to
cater for a variety of data sets. The actual ranges used are reported
in the current co-ordinate Frame and pixels, provided they apply to
all lines being fitted.
Once the trends have been determined they can either be stored
directly or subtracted from the input data. If stored directly they
can be subtracted later. The advantage of that approach is the
subtraction can be undone, but at some cost in efficiency.
Fits may be rejected if their root-mean squared (rms) residuals are
more than a specified number of standard deviations from the the mean
rms residuals of the fits. Rejected fits appear as bad pixels in the
output data.
Fitting independent trends can be useful when you need to remove the
continuum from a spectral cube, where each spectrum is independent of
the others (that is you need an independent continuum determination
for each position on the sky). It can also be used to de-trend
individual spectra and perform functions like debiassing a CCD which
has bias strips.


Usage
~~~~~


::

    
       mfittrend in axis ranges out { order
                                    { knots=?
                                    fittype
       



ADAM parameters
~~~~~~~~~~~~~~~



ARANGES() = _INTEGER (Write)
````````````````````````````
This parameter is only written when AUTO=TRUE, recording the trend-
axis fitting regions determined automatically. They comprise pairs of
pixel co-ordinates.



AUTO = _LOGICAL (Read)
``````````````````````
If TRUE, the ranges that define the trends are determined
automatically, and parameter RANGES is ignored. [FALSE]



AXIS = LITERAL (Read)
`````````````````````
The axis of the current co-ordinate system that defines the direction
of the trends. This is specified using one of the following options.


+ An integer index of an axis within the current Frame of the input
NDF (in the range 1 to the number of axes in the current Frame).
+ An axis symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If the axes of the current Frame are not parallel to the NDF
pixel axes, then the pixel axis which is most nearly parallel to the
specified current Frame axis will be used. AXIS defaults to the last
axis. [!]



CLIP() = _REAL (Read)
`````````````````````
Array of standard-deviation limits for progressive clipping of
outlying binned (see NUMBIN) pixel values while determining the
fitting ranges automatically. It is therefore only applicable when
AUTO=TRUE. Its purpose is to exclude features that are not part of the
trends.
Pixels are rejected at the ith clipping cycle if they lie beyond plus
or minus CLIP(i) times the dispersion about the median of the
remaining good pixels. Thus lower values of CLIP will reject more
pixels. The normal approach is to start low and progressivley increase
the clipping factors, as the dispersion decreases after the exclusion
of features. The source of the dispersion depends on the value the
METHOD parameter. Between one and five values may be supplied.
Supplying the null value (!), results in 2, 2.5, and 3 clipping
factors. [2,2,2.5,3]



FITTYPE = LITERAL (Read)
````````````````````````
The type of fit. It must be either "Polynomial" for a polynomial or
"Spline" for a bi-cubic B-spline. ["Polynomial"]



FOREST = _LOGICAL (Read)
````````````````````````
Set this TRUE if the data may contain spectral data with many lines---
a line forest---when using the automatic range mode (AUTO=TRUE). A
different approach using the histogram determines the baseline mode
and noise better in the presence of multiple lines. This leads to
improved masking of the spectral lines and affords a better
determination of the baseline. In a lineforest the ratio of baseline
to line regions is much reduced and hence normal sigma clipping, when
FOREST=FALSE, is biased. [FALSE]



KNOTS = _INTEGER (Read)
```````````````````````
The number of interior knots used for the cubic-spline fit along the
trend axis. Increasing this parameter value increases the flexibility
of the surface. KNOTS is only accessed when FITTYPE="Spline". See
INTERPOL for how the knots are arranged. The default is the current
value.
For INTERPOL=TRUE, the value must be in the range 1 to 11, and 4 is a
reasonable value for flatish trends. The initial default is 4.
For INTERPOL=FALSE the allowed range is 1 to 60 with an initial
default of 8. In this mode, KNOTS is the maximum number of interior
knots.
The upper limit of acceptable values for a trend axis is no more than
half of the axis dimension. []



IN = NDF (Read & Write)
```````````````````````
The input NDF. On successful completion this may have the trends
subtracted, but only if SUBTRACT and MODIFYIN are both set TRUE.



INTERPOL = _LOGICAL (Read)
``````````````````````````
The type of spline fit to use when FITTYPE="Spline".
If set TRUE, an interpolating spline is fitted by least squares that
ensures the fit is exact at the knots. Therefore the knot locations
may be set by the POSKNOT parameter.
If set FALSE, a smoothing spline is fitted. A smoothing factor
controls the degree of smoothing. The factor is determined iteratively
between limits, hence it is the slower option of the two, but
generally gives better fits, especially for curvy trends. The location
of of the knots is decided automatically by Dierckx's algorithm,
governed where they are most needed. Knots are added when the weighted
sum of the squared residuals exceeds the smoothing factor. A final fit
is made with the chosen smoothing, but finding the knots afresh.
The few iterations commence from the upper limit and progress more
slowly at each iteration towards the lower limit. The iterations
continue until the residuals stabilise or the maximum number of
interior knots is reached or the lower limit is reached. The upper
limit is the weighted sum of the squares of the residuals of the
least-squares cubic polynomial fit. The lower limit is the estimation
of the overall noise obtained from a clipped mean the standard
deviation in short segments that diminish bias arising from the shape
of the trend. The lower limit prevents too many knots being created
and fitting to the noise or fine features.
The iteration to a smooth fit makes a smoothing spline somewhat
slower. [FALSE]



MASK = NDF (Write)
``````````````````
The name of the NDF to contain the feature mask. It is only accessed
for automatic mode and METHOD="Single" or "Global". It has the same
bounds as the input NDF and the data array is type _BYTE. No mask NDF
is created if null (!) is supplied. [!]



METHOD = LITERAL (Given)
````````````````````````
The method used to define the masked regions in automatic mode.
Allowed values are as follows.


+ "Region" -- This averages trend lines from a selected representative
  region given by parameter SECTION and bins neighbouring elements
  within this average line. Then it performs a linear fit upon the
  binned line, and rejects the outliers, iteratively with standard-
  deviation clipping (parameter CLIP). The standard deviation is that of
  the average line within the region. The ranges are the intervals
  between the rejected points, rescaled to the original pixels. They are
  returned in parameter ARANGES.

This is best suited to a low dispersion along the trend axis and a
single concentrated region containing the bulk of the signal to be
excluded from the trend fitting.


+ "Single" -- This is like "Region" except there is neither averaging
  of lines nor a single set of ranges. Each line is masked
  independently. The dispersion for the clipping of outliers within a
  line is the standard deviation within that line.

This is more appropriate when the features being masked vary widely
across the image, and significantly between adjacent lines. Some prior
smoothing or background tracing (CUPID:FINDBACK) will usually prove
beneficial.


+ "Global" -- This is a variant of "Single". The only difference is
  that the dispersion used to reject features using the standard
  deviation of the whole data array. This is more robust than "Single",
  however it does not perform rejections well for lines with anomalous
  noise.

["Single"]



MODIFYIN = _LOGICAL (Read)
``````````````````````````
Whether or not to modify the input NDF. It is only used when SUBTRACT
is TRUE. If MODIFYIN is FALSE, then an NDF name must be supplied by
the OUT parameter. [FALSE]



NUMBIN = _INTEGER (Read)
````````````````````````
The number of bins in which to compress the trend line for the
automatic range-determination mode. A single line or even the average
over a region will often be noisy; this compression creates a better
signal-to-noise ratio from which to detect features to be excluded
from the trend fitting. If NUMBIN is made too large, weaker features
will be lost or stronger features will be enlarged and background
elements excluded from the fitting. The minimum value is 16, and the
maximum is such that there will be a factor of two compression. NUMBIN
is ignored when there are fewer than 32 elements in each line to be
de-trended. [32]



ORDER = _INTEGER (Read)
```````````````````````
The order of the polynomials to be used when trend fitting. A
polynomial of order 0 is a constant and 1 a line, 2 a quadratic etc.
The maximum value is 15. ORDER is only accessed when
FITTYPE="Polynomial". [3]



OUT = NDF (Read)
````````````````
The output NDF containing either the difference between the input NDF
and the various trends, or the values of the trends themselves. This
will not be used if SUBTRACT and MODIFYIN are TRUE (in that case the
input NDF will be modified).



POSKNOT( ) = LITERAL (Read)
```````````````````````````
The co-ordinates of the interior knots for all trends. KNOTS values
should be supplied, or just the null (!) value to request equally
spaced knots. The units of these co-ordinates is determined by the
axis of the current world co-ordinate system of the input NDF that
corresponds to the trend axis. Supplying a colon ":" will display
details of the current co-ordinate Frame. [!]



PROPBAD = _LOGICAL (Read)
`````````````````````````
Only used if SUBTRACT is FALSE. If PROPBAD is TRUE, the returned
fitted values are set bad if the corresponding input value is bad. If
PROPBAD is FALSE, the fitted values are retained. [TRUE]



RANGES() = LITERAL (Read)
`````````````````````````
These are the pairs of co-ordinates that define ranges along the trend
axis. When given these ranges are used to select the values that are
used in the fits. The null value (!) causes all the values along each
data line to be used. The units of these ranges is determined by the
axis of the current world co-ordinate system that corresponds to the
trend axis. Supplying a colon ":" will display details of the current
co-ordinate Frame. Up to ten pairs of values are allowed. This
parameter is not accessed when AUTO=TRUE. [!]



RMSCLIP = _REAL (Read)
``````````````````````
The number of standard deviations exceeding the mean of the root-mean-
squared residuals of the fits at which a fit is rejected. A null value
(!) means perform no rejections. Allowed values are between 2 and 15.
[!]



SECTION = LITERAL (Read)
````````````````````````
The region from which representative lines are averaged in automatic
mode to determine the regions to fit trends. It is therefore only
accessed when AUTO=TRUE, METHOD="Region", and the dimensionality of
the input NDF is more than 1. The value is defined as an NDF section,
so that ranges can be defined along any axis, and be given as pixel
indices or axis (data) co-ordinates. The pixel axis corresponding to
parameter AXIS is ignored. So for example, if the pixel axis were 3 in
a cube, the value "3:5,4," would average all the lines in elements in
columns 3 to 5 and row 4. See "NDF sections" in SUN/95, or the online
documentation for details.
A null value (!) requests that a representative region around the
centre be used. [!]



SUBTRACT = _LOGICAL (Read)
``````````````````````````
Whether not to subtract the trends from the input NDF or not. If not,
then the trends will be evaluated and written to a new NDF (see also
Parameter PROPBAD). [FALSE]



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
If TRUE and the input NDF contains variances, then the polynomial or
spline fits will be weighted by the variances.



Examples
~~~~~~~~
mfittrend in=cube axis=3 ranges="1000,2000,3000,4000" order=4
out=detrend This example fits cubic polynomials to the spectral axis
of a data cube. The fits only use the data lying within the ranges
1000 to 2000 and 3000 to 4000 Angstroms (assuming the spectral axis is
calibrated in Angstroms and that is the current co-ordinate system).
The fit is evaluated and written to the data cube called detrend.
mfittrend in=cube axis=3 auto clip=[2,3] order=4 out=detrend
As above except the fitting ranges are determined automatically with
2- then 3-sigma clipping using a representative central region.
mfittrend in=cube axis=3 auto clip=[2,3] fittype=spline out=detrend
interpol As the previous example except that interpolation cubic-
spline fits with four equally spaced interior knots are used to
characterise the trends.
mfittrend m51 3 out=m51_bsl mask=m51_msk auto fittype=spl
This example fits to trends along the third axis of NDF m51 and writes
the evaluated fits to NDF m51_bsl. The fits use a smoothing cubic
spline with the placement and number of interior knots determined
automatically. Features are determined automatically, and a mask of
excluded features is written to NDF m51_msk.
mfittrend cube axis=3 auto method=single order=1 subtract
out=cube_dt mask=cube_mask This fits linear trends to the spectral
axis of a data cube called cube, masking spectral features along each
line independently. The mask pixels are recorded in NDF cube_mask. The
fitted trend are subtracted and stored in NDF cube_dt.



Notes
~~~~~


+ This application attempts to solve the problem of fitting numerous
  polynomials in a least-squares sense and that do not follow the
  natural ordering of the NDF data, in the most CPU-time-efficient way
  possible.

To do this requires the use of additional memory (of order one less
than the dimensionality of the NDF itself, times the polynomial order
squared). To minimise the use of memory and get the fastest possible
determinations you should not use weighting and assert that the input
data do not have any BAD values (use the application SETBAD to set the
appropriate flag).

+ If you choose to use the automatic range determination. You may need
to determine empirically what are the best clipping limits, binning
factor, and for METHOD="Region" the region to average.
+ You are advised to inspect the fits, especially the spline fits or
  high-order polynomials. A given set of trends may require more than
  one pass through this task, if they exhibit varied morphologies. Use
  masking or NDF sections to select different regions that are fit with
  different parameters. The various trend maps are then integrated with
  PASTE to form the final composite set of trends that you can subtract.




Related Applications
~~~~~~~~~~~~~~~~~~~~
FIGARO: FITCONT, FITPOLY; CCDPACK: DEBIAS; KAPPA: SETBAD.


Copyright
~~~~~~~~~
Copyright (C) 2005-2006 Particle Physics and Astronomy Research
Council. Copyright (C) 2007-2008, 2012, 2016 Science and Technology
Facilities Council. All Rights reserved.


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
UNITS, TITLE, HISTORY, WCS and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Handles data of up to 7 dimensions.




