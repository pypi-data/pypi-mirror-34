

MAKEMOS
=======


Purpose
~~~~~~~
Makes a mosaic by combining and normalising a set of NDFs


Description
~~~~~~~~~~~
This is a comprehensive application for combining a set of NDFs
(normally representing overlapping coverage of an object) into a
single mosaic. It addresses the problems of (a) combining a sequence
of separate data sets into a single NDF and (b) optionally normalising
each NDF so that they match each other in regions where they overlap.
Mutual alignment of the separate NDFs is not performed by this
application and must be addressed beforehand (although NDFs may be
aligned to the nearest pixel simply by shifting their pixel origin).
MAKEMOS registers the set of NDFs supplied by matching their pixel
indices and then forms a mosaic by combining the separate input pixel
values at each location using a nominated data-combination method (by
default, it takes the median). The resulting mosaic is of sufficient
extent to accommodate all the input data, with any output data pixels
which do not receive values from the input being set to the "bad"
pixel value. Account is taken of variance information associated with
the input NDFs, and all calculations are optimally weighted to
minimise the output noise. Output variance estimates for the final
mosaic may also be produced.
Forming a mosaic in this way will normally be successful only so long
as the input data are mutually consistent. Unfortunately, this is
often not the case, since data frequently have differing effective
exposure times and background levels which give discontinuities in the
final mosaic. Thus, MAKEMOS also addresses the problem of normalising
the input NDFs to make them mutually consistent. It does this by
optionally applying optimised multiplicative and/or additive
corrections (termed scale-factor and zero-point corrections) to each
NDF before forming the mosaic. These optimised corrections are
determined by inter-comparing the input NDFs in pairs, using the
regions where they overlap to determine the relative scale-factor
and/or zero-point difference between each pair. A self-consistent set
of corrections is then found which, when applied to each input NDF,
will best eliminate these observed differences and give a smooth
mosaic.


Usage
~~~~~


::

    
       makemos in out
       



ADAM parameters
~~~~~~~~~~~~~~~



ALPHA = _REAL (Read)
````````````````````
The fraction of extreme values to remove before combining input data
if the "trimmed mean" data combination method is selected for
producing the output mosaic (see the METHOD parameter). A fraction
alpha (approximately) of the available values is removed from each
extreme. This may take values in the range 0 to 0.5. [0.2]



CMPVAR = _LOGICAL (Read)
````````````````````````
This parameter controls the use of statistical error (variance)
information contained in the input NDFs when they are inter-compared
in pairs to derive scale-factor or zero-point corrections. It is only
used if either SCALE or ZERO is set to TRUE and if two or more of the
input NDFs contain variance information (a "reference NDF" also
counts, if supplied). In this case, if CMPVAR is set to TRUE, then
variance information is used to correctly weight the input data
whenever a pair of input NDFs are inter-compared and both have
variance information available.
The default behaviour is to use variance information during inter-
comparisons. This may be suppressed by setting CMPVAR to FALSE, which
sometimes gives faster execution without greatly affecting the result
(also see the "Algorithms Used" section). However, if input data with
similar values have widely differing variance values within the same
input NDF, then use of input variance information is recommended (this
could happen, for instance, if an input NDF is the result of a
previous mosaic-ing process). [TRUE]



CORRECT = LITERAL (Read)
````````````````````````
The name of the file used to output the scale and zero-point
corrections (see SCALE and ZERO parameters). This file can be read by
the DRIZZLE task. If the file already exists, it is overwritten. If a
null (!) value is supplied, or if SCALE and ZERO are both set to
FALSE, no file is written. [!]



GENVAR = _LOGICAL (Read)
````````````````````````
If GENVAR is set to TRUE and all the input NDFs supplied contain
statistical error (variance) information, then variance information
will also be calculated for the output mosaic NDF, provided that
USEVAR is also TRUE.
Otherwise if GENVAR is TRUE and either USEVAR is FALSE or some of the
input NDFs do not contain error information, then output variances
will be generated using the natural variations in the input data.
Obviously this method should only be used if there are many input
datasets, which also provide good coverage of the output area. If this
option is chosen any regions of the output image that have only one
input value will have their associated variances set bad.
The default for this parameter depends on the presence of error
information in the input NDFs. If all have error information then the
default is TRUE, otherwise it is FALSE.
[DYNAMIC]



IN = LITERAL (Read and [optionally] Write)
``````````````````````````````````````````
A list of the names of the input NDFs which are to be combined into a
mosaic. The NDF names should be separated by commas and may include
wildcards.
The input NDFs are normally accessed only for reading. However, if the
MODIFY parameter is set to TRUE (and scale-factor or zero-point
corrections are being calculated) then each of the "input" NDFs will
be modified by applying the calculated corrections.



LISTIN = _LOGICAL (Read)
````````````````````````
If a TRUE value is given for this parameter (the default), then the
names of all the NDFs supplied as input will be listed (and will be
recorded in the logfile if this is enabled). Otherwise, this listing
will be omitted. [TRUE]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter, then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP, then the
value specified there will be used. Otherwise, the default is
"CCDPACK.LOG". [CCDPACK.LOG]



LOGTO = LITERAL (Read)
``````````````````````
Every CCDPACK application has the ability to log its output for future
reference as well as for display on the terminal. This parameter
controls this process, and may be set to any unique abbreviation of
the following:

+ TERMINAL -- Send output to the terminal only
+ LOGFILE -- Send output to the logfile only (see the LOGFILE
parameter)
+ BOTH -- Send output to both the terminal and the logfile
+ NEITHER -- Produce no output at all

If the logging system has been initialised using CCDSETUP, then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



MAX = _REAL (Read)
``````````````````
Upper limit for input data values which may contribute to the output
mosaic if the "threshold" data combination method is selected (see the
METHOD parameter). [Maximum real value]



MAXIT = _INTEGER (Read)
```````````````````````
This parameter specifies the maximum number of iterations to be used
when inter-comparing pairs of input NDF data arrays to determine their
relative scale-factor and/or zero-point. It is only used if (a) both
the SCALE and ZERO parameters have been set to TRUE, or (b) SCALE has
been set to TRUE and statistical error (variance) information obtained
from the input NDFs is being used to weight the data during the inter-
comparison. In other cases the inter-comparison operation is not
iterative.
If the specified number of iterations is exceeded without achieving
the accuracy required by the settings of the TOLS and TOLZ parameters,
then a warning message will be issued, but the results will still be
used. The value given for MAXIT must be at least one. [20]



METHOD = LITERAL (Read)
```````````````````````
The method to be used to combine the input NDFs' data values to form
the output mosaic. This may be set to any unique abbreviation of the
following:

+ MEAN -- Mean of the input data values
+ MEDIAN -- Weighted median of the input data values
+ TRIMMED -- An "alpha trimmed mean" in which a fraction alpha of the
values are removed from each extreme
+ MODE -- An iteratively "sigma clipped" mean which approximates to
the modal value
+ SIGMA -- A sigma clipped mean
+ THRESHOLD -- Mean with values above and below given limits removed
+ MINMAX -- Mean with the highest and lowest values removed
+ BROADENED -- A broadened median (the mean of a small number of
central values)
+ CLIPMED -- A sigma clipped median (like SIGMA except that the median
of the clipped values is used)
+ FASTMED -- Unweighted median of input data values [MEDIAN]





MIN = _REAL (Read)
``````````````````
Lower limit for input data values which may contribute to the output
mosaic if the "threshold" data combination method is selected (see the
METHOD parameter). [Minimum real value]



MODIFY = _LOGICAL (Read)
````````````````````````
By default, the NDFs supplied via the IN parameter are regarded as
"input" NDFs and will not be modified. However, if scale-factor or
zero-point corrections are being calculated (see the SCALE and ZERO
parameters), then giving a TRUE value for MODIFY indicates that these
NDFs are themselves to be modified by applying the calculated
corrections before the output mosaic is formed.
This facility provides a means of applying corrections to individual
NDFs (e.g. to mutually normalise them) without necessarily also
combining them into a mosaic. It may also be useful if several
invocations of MAKEMOS are to be made with different parameter
settings; by specifying MODIFY=TRUE for the first invocation, scale-
factor or zero-point corrections may be applied to normalise the input
data so that this need not be repeated on each invocation.
WARNING: Caution should be exercised if setting MODIFY to TRUE, as
information about the uncorrected data values of the "input" NDFs will
not be retained. [FALSE]



NITER = _REAL (Read)
````````````````````
Maximum number of refining iterations used if the "mode" data
combination method is selected (see the METHOD parameter). [7]



OPTOV = _INTEGER (Read)
```````````````````````
This parameter specifies the "optimum number of overlaps" which an NDF
should have with its neighbours and controls the number of inter-
comparisons made between pairs of overlapping NDFs when determining
scale-factor or zero-point corrections (see the SCALE and ZERO
parameters).
The need for this parameter arises because when multiple input NDFs
are supplied there may be a large number of potential pair-wise
overlaps between them. To prevent them all being used, which may take
far longer than is justified, this set of potential overlaps is
reduced by elimination, starting with the smallest ones (as measured
by the number of overlapping pixels) and continuing until no more
overlaps can be removed without reducing the number of overlaps of any
NDF below the value given for OPTOV. In practice, this means that each
NDF will end up with about (although not exactly) OPTOV overlaps with
its neighbours, with the largest overlaps being preferred.
Note that although this algorithm is effective in reducing the number
of overlaps, it is not guaranteed always to result in a set of
overlaps which allow the optimum set of corrections to be calculated.
In practice, problems from this cause are unlikely unless unusual
patterns of NDF overlap are involved, but they may be solved by
increasing the value of OVOPT and/or constructing the required mosaic
in pieces by running MAKEMOS several times on different sets of input
NDFs.
In some cases, reducing the value of OVOPT may reduce the number of
inter-comparisons made, and hence reduce the execution time, but if
too few inter-comparisons are made, there is a risk that the
corrections obtained may not be the best possible.
This parameter is only used if SCALE or ZERO is set to TRUE. [3]



OUT = NDF (Write)
`````````````````
Name of the NDF to contain the output mosaic. This is normally
mandatory. However, if the "input" NDFs are being modified (by setting
the MODIFY parameter to TRUE), then it may optionally be omitted by
supplying a null value (!). In this case, no output mosaic will be
formed.



PRESERVE = _LOGICAL (Read)
``````````````````````````
If a TRUE value is given for this parameter (the default), then the
data type of the output mosaic NDF will be derived from that of the
input NDF with the highest precision, so that the input data type will
be "preserved" in the output NDF. Alternatively, if a FALSE value is
given, then the output NDF will be given an appropriate floating point
data type.
When using integer input data, the former option is useful for
minimising the storage space required for large mosaics, while the
latter typically permits a wider output dynamic range when necessary.
A wide dynamic range is particularly important if a large range of
scale factor corrections are being applied (as when combining images
with a wide range of exposure times).
If a global value has been set up for this parameter using CCDSETUP,
then that value will be used. [TRUE]



REF = NDF (Read)
````````````````
If scale-factor and/or zero-point corrections are being applied (see
the SCALE and ZERO parameters) then, by default, these are normalised
so that the median corrections are unity and zero respectively.
However, if an NDF is given via the REF parameter (so as to over-ride
its default null value), then scale-factor and zero-point corrections
will instead be adjusted so that the corrected data are normalised to
the "reference NDF" supplied.
This provides a means of retaining the calibration of a set of data,
even when corrections are being applied, by nominating a reference NDF
which is to remain unchanged. It also allows the output mosaic to be
normalised to any externally-calibrated NDF with which it overlaps,
and hence allows a calibration to be transferred from one set of data
to another.
If the NDF supplied via the REF parameter is one of those supplied as
input via the IN parameter, then this serves to identify which of the
input NDFs should be used as a reference, to which the others will be
adjusted. In this case, the scale-factor and/or zero-point corrections
applied to the nominated input NDF will be set to one and zero, and
the corrections for the others will be adjusted accordingly.
Alternatively, if the reference NDF does not appear as one of the
input NDFs, then it will be included as an additional set of data in
the inter-comparisons made between overlapping NDFs and will be used
to normalise the corrections obtained (so that the output mosaic is
normalised to it). However, it will not itself contribute to the
output mosaic in this case. [!]



SCALE = _LOGICAL (Read)
```````````````````````
This parameter specifies whether MAKEMOS should attempt to adjust the
input data values by applying scale-factor (i.e. multiplicative)
corrections before combining them into a mosaic. This would be
appropriate, for instance, if a series of images had been obtained
with differing exposure times; to combine them without correction
would yield a mosaic with discontinuities at the image edges where the
data values differ.
If SCALE is set to TRUE, then MAKEMOS will inter-compare the NDFs
supplied as input and will estimate the relative scale-factor between
selected pairs of input data arrays where they overlap. From this
information, a global set of multiplicative corrections will be
derived which make the input data as mutually consistent as possible.
These corrections will be applied to the input data before combining
them into a mosaic.
Calculation of scale-factor corrections may also be combined with the
use of zero-point corrections (see the ZERO parameter). By default, no
scale-factor corrections are applied. [FALSE]



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations at which to reject values if the "mode",
"sigma" or "clipmed" data combination methods are selected (see the
METHOD parameter). This value must be positive. [4.0]



SKYSUP = _REAL (Read)
`````````````````````
A positive "sky noise suppression factor" used to control the effects
of sky noise when pairs of input NDFs are inter-compared to determine
their relative scale-factor. It is intended to prevent the resulting
scale-factor estimate being biased by the many similar values present
in the "sky background" of typical astronomical data. SKYSUP controls
an algorithm which reduces the weight given to data where there is a
high density of points with the same value, in order to suppress this
effect. It is only used if a scale factor is being estimated (i.e. if
SCALE is TRUE).
A SKYSUP value of unity can often be effective, but a value set by the
approximate ratio of sky pixels to useful object pixels (i.e. those
containing non-sky signal) in a "typical" NDF overlap region will
usually be better. The precise value is not critical. A value of zero
disables the sky noise suppression algorithm completely. The default
value for SKYSUP is 10**(n/2.0), where n is the number of significant
dimensions in the output mosaic. Hence, for a 2-dimensional image, it
will default to 10 which is normally reasonable for CCD frames of
extended objects such as galaxies (a larger value, say 100, may give
slightly better results for star fields). [10**(n/2.0)]



TITLE = LITERAL (Read)
``````````````````````
Title for the output mosaic NDF. [Output from MAKEMOS]



TOLS = _REAL (Read)
```````````````````
This parameter defines the accuracy tolerance to be achieved when
inter-comparing pairs of input NDF data arrays to determine their
relative scale-factor. It is only used if the inter-comparison is to
be performed iteratively, which will be the case if (a) both the SCALE
and ZERO parameters have been set to TRUE, or (b) SCALE has been set
to TRUE and statistical error (variance) information obtained from the
input NDFs is being used to weight the data during the inter-
comparison.
The value given for TOLS specifies the tolerable fractional error in
the estimation of the relative scale-factor between any pair of input
NDFs. This value must be positive. [0.001]



TOLZ = _REAL (Read)
```````````````````
This parameter defines the accuracy tolerance to be achieved when
inter-comparing pairs of input NDF data arrays to determine their
relative zero-points. It is only used if the inter-comparison is to be
performed iteratively, which will be the case if both the SCALE and
ZERO parameters have been set to TRUE.
The value given for TOLZ specifies the tolerable absolute error in the
estimation of the relative zero-point between any pair of input NDFs
whose relative scale-factor is unity. If the relative scale-factor is
also being estimated, then the value used is multiplied by this
relative scale-factor estimate (which reflects the fact that an NDF
with a larger data range can tolerate a larger error in estimating its
zero-point). The TOLS value supplied must be positive. [0.05]



USEVAR = _LOGICAL (Read)
````````````````````````
The value of this parameter specifies whether statistical error
(variance) information contained in the input NDFs should be used to
weight the input data when they are combined to produce the output
mosaic. This parameter is only used if all the input NDFs contain
variance information, in which case the default behaviour is to use
this information to correctly weight the data values being combined.
If output variances are to be generated (specified by the GENVAR
parameter) then this parameter (and GENVAR) should be set TRUE.
If insufficient input variance information is available, or if USEVAR
is set to FALSE, then weights are instead derived from the scale-
factor corrections applied to each NDF (see the WEIGHTS parameter for
details); unit weight is used if no scale-factor corrections are being
applied. Alternatively, explicit weights may be given for each input
NDF via the WEIGHTS parameter.
If you want to add estimated variances to the output image (based on
the natural variations of the input images) and all your input images
contain variances then you will need to set this parameter FALSE (see
GENVAR).
[TRUE]



WEIGHTS( ) = _REAL (Read)
`````````````````````````
A set of positive weighting factors to be used to weight the input
NDFs when they are combined. If this parameter is used, then one value
should be given for each input NDF and the values should be supplied
in the same order as the input NDFs. If a null (!) value is given (the
default) then a set of weights will be generated internally - these
will normally all be unity unless scale-factor corrections are being
applied (see the SCALE parameter), in which case the reciprocal of the
scale factor correction for each input NDF is used as its weight. This
corresponds to the assumption that variance is proportional to data
value in each input NDF.
This parameter is only used if the USEVAR parameter is set to FALSE or
if one or more of the input NDFs does not contain variance
information. Otherwise, the input variance values are used to weight
the input data when they are combined. [!]



ZERO = _LOGICAL (Read)
``````````````````````
This parameter specifies whether MAKEMOS should attempt to adjust the
input data values by applying zero-point (i.e. additive) corrections
before combining them into a mosaic. This would be appropriate, for
instance, if a series of images had been obtained with differing
background (sky) values; to combine them without correction would
yield a mosaic with discontinuities at the image edges where the data
values differ.
If ZERO is set to TRUE, then MAKEMOS will inter-compare the NDFs
supplied as input and will estimate the relative zero-point difference
between selected pairs of input data arrays where they overlap. From
this information, a global set of additive corrections will be derived
which make the input data as mutually consistent as possible. These
corrections will be applied to the input data before they are combined
into a mosaic.
Calculation of zero-point corrections may also be combined with the
use of scale-factor corrections (see the SCALE parameter). By default,
no zero-point corrections are applied. [FALSE]



Examples
~~~~~~~~
makemos '*' mymos
Combines the set of NDFs matching the wild-card "*" into a single
mosaic called mymos. By default, no normalisation corrections are
applied to the input data, which are combined by taking the median in
regions where several input NDFs overlap.
makemos in='"a,b,c,d"' out=combined zero
Combines the four overlapping input NDFs a, b, c and d into a single
mosaic called combined. Optimised zero-point corrections are derived
and applied to the data before combining them so as to make them as
mutually consistent as possible. This helps to eliminate unwanted
discontinuities in the output mosaic.
makemos '"a,b,c,d"' out=combined scale
Combines the four NDFs a, b, c and d as above, but makes optimised
corrections to the scale factor of each (i.e. multiplies each by an
appropriate constant) before they are combined. This would be
appropriate if, for instance, the input data were CCD frames acquired
using different exposure times and had subsequently had their sky
background removed.
makemos in='frame*' out=result scale zero
Combines the set of input NDFs matching the wild-card "frame*" into a
single mosaic called result. Optimised scale factor and zero point
corrections are applied before combining the data. This would be
appropriate if, for instance, the input data had been acquired using
different exposure times and also had different levels of sky
background.
makemos in='frame*' out=result scale zero modify
This is identical to the previous example, except that in addition to
forming the output result, the MODIFY parameter causes all the input
NDFs to be modified using the same optimised corrections as are
applied when forming the mosaic, thus mutually normalising all the
separate NDFs. Note that this feature should be used with care, as
information about the original normalisation of the input data will be
lost. When MODIFY is specified, a null value "!" may be given for the
OUT parameter if an output mosaic is not actually required.
makemos '"a,b,c,d"' result scale zero ref=b
This example merges the four input NDFs a, b, c and d into a mosaic
called result. In calculating the optimised scale factor and zero
point corrections to apply, b is regarded as a "reference NDF" and the
other NDFs are normalised to it. This means that if b has previously
been calibrated, then the output mosaic will inherit this calibration.
makemos '"a,b,c,d"' result scale zero ref=e
This example is identical to that above, except that the "reference
NDF" e is not one of the input NDFs and will not form part of the
output mosaic. Nevertheless, the scale factor and zero point
corrections applied will be such that all the input NDFs are
normalised to it (the reference NDF must overlap with at least one of
the input NDFs). Thus, if e has been calibrated, this calibration will
be transferred to the output mosaic (note that if MODIFY is specified,
then the calibration could also be transferred to each of the input
NDFs).
makemos 'frame*' mosaic nopreserve nogenvar method=minmax skysup=0
This example illustrates some of the less commonly used MAKEMOS
options. nopreserve causes the output data type to be a floating point
type rather than preserving the input data type, nogenvar prevents
generation of an output variance array (possibly to save space with a
large mosaic), method=minmax indicates that output pixels are to be
calculated by taking the mean of input pixels after discarding the
lowest and highest values, and skysup=0 is used to disable the sky
noise suppression algorithm (perhaps for data which contain few sky
pixels).



Algorithms Used
~~~~~~~~~~~~~~~
Some of the algorithms used by MAKEMOS require a little explanation.
The first of these is used to inter-compare overlapping regions of the
input NDFs to determine their relative scale-factor and zero-point
difference (in the most general case). In effect, this algorithm has
to fit a straight line to a scatter plot representing the pixel values
in the two overlapping NDFs.
Rather than use a conventional least-squares fit for this purpose,
which would be sensitive to spurious data, a fit based on minimisation
of the sum of the absolute values of the residuals is used instead.
This is considerably more robust. It also allows the residuals to be
defined by the perpendicular distance of each point from the fitted
line, rather than the vertical distance used in conventional least
squares. In turn, this removes the distinction between dependent and
independent variables and allows the statistical uncertainty on both
axes (described by an error ellipse) to be properly taken into account
along with other weighting factors used to implement sky noise
suppression.
In general, this fitting algorithm is iterative and is controlled via
the MAXIT, TOLS and TOLZ parameters which specify the convergence
criteria. However, in some important cases the fit can be obtained in
a single pass, with consequent savings in execution time. This occurs
if:

+ Only zero-point corrections are being determined, or
+ Only scale-factor corrections are being determined and no input
  variance information is being used to weight the inter-comparison
  process (see the CMPVAR parameter).

The second stage of normalisation involves a global optimisation
process which seeks to determine the best corrections to be applied to
each input NDF. The algorithm which performs this task makes a guess
at the best corrections to apply and then calculates the scale-factor
and/or zero-point differences which would remain between each pair of
overlapping NDFs if they were corrected in this way. These corrections
are then adjusted until the weighted sum of squares of the remaining
differences is minimised. The weights used in this process are derived
from error estimates produced by the earlier (inter-comparison)
algorithm. This allows information about the required corrections to
be optimally combined from many overlaps, even in cases where
individual overlaps may be small and contain inadequate information on
their own.
The algorithm used for combining the separate input NDFs into a mosaic
requires no special explanation, except to note that it is designed to
operate on large mosaics without making excessive demands on system
resources such as memory. It does this by partitioning the mosaic into
small regions for processing.


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ SKYSUP -- dynamically defaulted
+ GENVAR -- dynamically defaulted
+ SCALE -- always FALSE
+ ZERO -- always FALSE
+ MODIFY -- always FALSE
+ TITLE -- always "Output from MAKEMOS"

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new
datasets/different devices, or after a break of sometime. The
intrinsic default behaviour of the application may be restored by
using the RESET keyword on the command line.
Certain parameters (LOGTO, LOGFILE and PRESERVE) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council Copyright
(C) 1998-1999 Central Laboratory of the Research Councils


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


+ MAKEMOS supports "bad" pixel values and all non-complex data types,
  with arithmetic being performed using the appropriate floating point
  type. It can process NDFs with any number of dimensions. The DATA,
  TITLE and VARIANCE components of an NDF are directly supported, with
  the AXIS, HISTORY, LABEL and UNITS components and all extensions being
  propagated from the first input NDF supplied (note that AXIS values,
  if present, will normally be extrapolated as a result of propagation
  to the output mosaic, which will typically have a larger extent than
  any of the input NDFs).




