

NORMALIZE
=========


Purpose
~~~~~~~
Normalises one NDF to a similar NDF by calculating a scale factor and
zero-point difference


Description
~~~~~~~~~~~
This application compares the data values in one NDF against the
corresponding values in the other NDF. A least-squares straight-line
is then fitted to the relationship between the two sets of data values
in order to determine the relative scale factor and any zero-level
offset between the NDFs (the offset may optionally be fixed at zero -
see parameter ZEROFF). To reduce computation time, the data points are
binned according to the data value in the second NDF. The mean data
value within each bin is used to find the fit and weights are applied
according to the number of pixels which contribute to each bin.
To guard against erroneous data values, which can corrupt the fit
obtained, the application then performs a number of iterations. It
calculates a noise estimate for each bin according to the rms
deviation of data values in the bin from the straight-line fit
obtained previously. It then re-bins the data, omitting values which
lie more than a specified number of standard deviations from the
expected value in each bin. The straight-line fit is then re-
calculated. You can specify the number of standard deviations and the
number of iterations used.
A plot is produced after the final iteration showing the bin centres,
with error bars representing the spread of values in each bin. The
best fitting straight line is overlayed on this plot.
Optionally, an output NDF can be created containing a normalised
version of the data array from the first input NDF.
For the special case of two-dimensional images, if IN2 (or IN1) spans
only a single row or column, it can be used to normalize each row or
column of IN1 (or IN2) in turn. See Parameter LOOP.


Usage
~~~~~


::

    
       normalize in1 in2 out
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the plot.
The width of the margins left for the annotation may be controlled
using Parameter MARGIN. The appearance of the axes (colours, founts,
etc,) can be controlled using the Parameter STYLE. The dynamic default
is TRUE if CLEAR is TRUE, and FALSE otherwise. []



CLEAR = _LOGICAL (Read)
```````````````````````
If TRUE the current picture is cleared before the plot is drawn. If
CLEAR is FALSE not only is the existing plot retained, but also an
attempt is made to align the new picture with the existing picture.
Thus you can generate a composite plot within a single set of axes,
say using different colours or modes to distinguish data from
different datasets. [TRUE]



CORR = _REAL (Write)
````````````````````
An output parameter giving Pearson's coefficient of linear correlation
for the data included in the last fit.



DATARANGE( 2 ) = _REAL (Read)
`````````````````````````````
This parameter may be used to override the auto-scaling feature. If
given, two real numbers should be supplied specifying the lower and
upper data values in IN2, between which data will be used. If a null
(!) value is supplied, the values used are the auto-scaled values,
calculated according to the value of PCRANGE. Note, this parameter
controls the range of data used in the fitting algorithm. The range of
data displayed in the plot can be specified separately using
Parameters XLEFT, XRIGHT, YBOT, and YTOP. [!]



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation on which to produce the plot. If a null value
(!) is supplied no plot will be made. [Current graphics device]



DRAWMARK = _LOGICAL (Read)
``````````````````````````
The central markers for each bin are not included in the plot if this
parameter is set to FALSE. [TRUE]



DRAWWIDTH = _LOGICAL (Read)
```````````````````````````
The "error bars" marking the width of each bin are not included in the
plot if this parameter is set to FALSE. [TRUE]



IN1 = NDF (Read)
````````````````
The NDF to be normalised.



IN2 = NDF (Read)
````````````````
The NDF to which IN1 will be normalised.



LOOP = _LOGICAL (Read)
``````````````````````
If both IN1 and IN2 are two-dimensional, but one of them spans only a
single row or column, then setting LOOP to TRUE will cause every row
or column in to be normalised independently of each other.
Specifically, if IN2 spans only a single row or column, then it will
be used to normalise each row or column of IN1 in turn. Any output NDF
(see parameter OUT) will have the shape and size of IN1. If IN1 spans
only a single row or column, then it will be normalised in turn by
each row or column of IN2. Any output NDF (see parameter OUT) will
then have the shape and size of IN2. In either case, the details of
the fit for each row or column will be displayed separately. Also see
Parameters OUTSLOPE, OUTOFFSET and OUTCORR. [FALSE]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave for axis annotation, given as
fractions of the corresponding dimension of the current picture. Four
values may be given, in the order: bottom, right, top, left. If less
than four values are given, extra values are used equal to the first
supplied value. If these margins are too narrow any axis annotation
may be clipped. If a null (!) value is supplied, the value used is
0.15 (for all edges) if annotated axes are produced, and zero
otherwise. [current value]



MARKER = _INTEGER (Read)
````````````````````````
Specifies the symbol with which each position should be marked in the
plot. It should be given as an integer PGPLOT-marker type. For
instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3 gives an
asterisk, 7 gives a triangle. The value must be larger than or equal
to -31. [current value]



MINPIX = _INTEGER (Read)
````````````````````````
The minimum number of good pixels required in a bin before it
contributes to the fitted line. It must be in the range 1 to the
number of pixels per bin. [2]



NBIN = _INTEGER (Read)
``````````````````````
The number of bins to use when binning the scatter plot prior to
fitting a straight line, in the range 2 to 10000. [50]



NITER = _INTEGER (Read)
```````````````````````
The number of iterations performed to reject bad data values in the
range 0 to 100. [2]



NSIGMA = _REAL (Read)
`````````````````````
The number of standard deviations at which bad data is rejected. It
must lie in the range 0.1 to 1.0E6. [3.0]



OFFSET = _REAL (Write)
``````````````````````
An output parameter giving the offset in the linear normalisation
expression: IN1 = SLOPE * IN2 + OFFSET.



OUT = NDF (Write)
`````````````````
An optional output NDF to hold a version of IN1 which is normalised to
IN2. A null (!) value indicates that an output NDF is not required.
See also parameter LOOP.



OUTCORR = NDF (Write)
`````````````````````
An optional 1-dimensonal output NDF to hold the correlation
coefficient for each row or column when LOOP=YES. See parameter CORR.
Ignored if LOOP=NO.



OUTOFFSET = NDF (Write)
```````````````````````
An optional 1-dimensonal output NDF to hold the offset used for each
row or column when LOOP=YES. See parameter OFFSET. Ignored if LOOP=NO.



OUTSLOPE = NDF (Write)
``````````````````````
An optional 1-dimensonal output NDF to hold the slope used for each
row or column when LOOP=YES. See parameter SLOPE. Ignored if LOOP=NO.



PCRANGE( 2 ) = _REAL (Read)
```````````````````````````
This parameter takes two real values in the range 0 to 100 and is used
to modify the action of the auto-scaling algorithm which selects the
data to use in the fitting algorithm. The two values correspond to the
percentage points in the histogram of IN2 at which the lower and upper
cuts on data value are placed. With the default value, the plots will
omit those pixels that lie in the lower and upper two-percent
intensity range of IN2. Note, this parameter controls the range of
data used in the fitting algorithm. The range of data displayed in the
plot can be specified separately using Parameters XLEFT, XRIGHT, YBOT,
and YTOP. [2,98]



SLOPE = _REAL (Write)
`````````````````````
An output parameter giving the slope of the linear normalisation
expression: IN1 = SLOPE * IN2 + OFFSET.



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the annotated axes, data values, error bars, and best-
fitting line.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings overriding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a plotting attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!)---the initial default---is supplied. To apply changes of
style to only the current invocation, begin these attributes with a
plus sign. A mixture of persistent and temporary style changes is
achieved by listing all the persistent attributes followed by a plus
sign then the list of temporary attributes.
See section "Plotting Attributes" in SUN/95 for a description of the
available attributes. Any unrecognised attributes are ignored (no
error is reported).
The appearance of the best-fitting straight line is controlled by the
attributes Colour(Curves), Width(Curves), etc. (the synonym Linemay be
used in place of Curves). The appearance of markers is controlled by
Colour(Markers), Width(Markers), etc. (the synonym Symbols may be used
in place of Markers). The appearance of the error bars is controlled
using Colour(ErrBars), Width(ErrBars), etc. Note, Size(ErrBars)
controls the length of the serifs (i.e. the cross pieces at each end
of the error bar), and defaults to 1.0. [current value]



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for Parameter IN1 to be used instead. [!]



XLEFT = _DOUBLE (Read)
``````````````````````
The axis value to place at the left hand end of the horizontal axis of
the plot. If a null (!) value is supplied, the value used is the
minimum data value used by the fitting algorithm from IN2 (with a
small margin). The value supplied may be greater than or less than the
value supplied for XRIGHT. [!]



XRIGHT = _DOUBLE (Read)
```````````````````````
The axis value to place at the right hand end of the horizontal axis
of the plot. If a null (!) value is supplied, the value used is the
maximum data value used by the fitting algorithm from IN2 (with a
small margin). The value supplied may be greater than or less than the
value supplied for XLEFT. [!]



YBOT = _DOUBLE (Read)
`````````````````````
The axis value to place at the bottom end of the vertical axis of the
plot. If a null (!) value is supplied, the value used is the minimum
data value used by the fitting algorithm from IN1 (with a small
margin). The value supplied may be greater than or less than the value
supplied for YTOP. []



YTOP = _DOUBLE (Read)
`````````````````````
The axis value to place at the top end of the vertical axis of the
plot. If a null (!) value is supplied, the value used is the maximum
data value used by the fitting algorithm from IN1 (with a small
margin). The value supplied may be greater than or less than the value
supplied for YBOT. [!]



ZEROFF = _LOGICAL (Read)
````````````````````````
If TRUE, the offset of the linear fit is constrained to be zero.
[FALSE]



Examples
~~~~~~~~
normalize cl123a cl123b cl123c
This normalises NDF cl123a to the NDF cl123b. A plot of the fit is
made on the current graphics device, and the resulting normalisation
scale and offset are written only to the normalize.sdf parameter file
(as in the all the examples below except where noted). The NDF cl123c
is the normalised version of the input cl123a.
normalize cl123a cl123b
style="'size(errba)=0,title=Gain calibration'" This normalises NDF
cl123a to the NDF cl123b. A plot of the fit is made on the current
graphics device with the title "Gain calibration". The error bars are
drawn with no serifs.
normalize cl123a cl123b cl123c offset=(shift) slope=(scale)
This normalises NDF cl123a to the NDF cl123b. A plot of the fit is
made on the current graphics device. The resulting normalisation scale
and offset are written to the ICL variables SCALE and SHIFT
respectively, where they could be passed to another application via an
ICL procedure. The NDF cl123c is the normalised version of the input
cl123a.
normalize in2=old in1=new out=! device=xwindows style=^normstyle
This normalises NDF new to the NDF old. A plot of the fit is made on
the xwindows device, using the plotting style defined in text file
normstyle. No output NDF is produced.
normalize in1=new in2=old out=young niter=5 pcrange=[3,98.5]
This normalises NDF new to the NDF old. It has five iterations to
reject outliers from the linear regression, and forms the regression
using pixels in old whose data values lie between the 3 and 98.5
percentiles, comparing with the corresponding pixels in new. A plot of
the fit is made on the current graphics device. The NDF young is the
normalised version of the input new.



Notes
~~~~~


+ The application stores two pictures in the graphics database in the
  following order: a FRAME picture containing the annotated axes and
  data plot, and a DATA picture containing just the data plot. Note, the
  FRAME picture is only created if annotated axes have been drawn, or if
  non-zero margins were specified using Parameter MARGIN. The world co-
  ordinates in the DATA picture will correspond to data values in the
  two NDFs.




Related Applications
~~~~~~~~~~~~~~~~~~~~
CCDPACK: MAKEMOS.


Copyright
~~~~~~~~~
Copyright (C) 1990-1992 Science & Engineering Research Council.
Copyright (C) 1995, 1998-1999, 2001, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2007, 2010, 2011, 2013 Science &
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


+ The routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS, and HISTORY components of an NDF, and
propagates all extensions to the output NDF. All propagated components
come from the NDF to be normalised.
+ At the moment, variance values are not used in the fitting algorithm
but are modified in the output NDF to take account of the scaling
introduced by the normalisation. (A later version may take account of
variances in the fitting algorithm.)
+ Processing of bad pixels and automatic quality masking are
supported.
+ Only _REAL data can be processed directly. Other non-complex numeric
data types will undergo a type conversion before processing occurs.
_DOUBLE data cannot be processed due to a loss of precision.
+ The pixel bounds of the two input NDFs are matched by trimming
  before calculating the normalisation constants, and are mapped as
  vectors to allow processing of NDFs of any dimensionality. An output
  NDF may optionally be produced which is based on the first input NDF
  (IN1) by applying the calculated normalisation constants to IN1.




