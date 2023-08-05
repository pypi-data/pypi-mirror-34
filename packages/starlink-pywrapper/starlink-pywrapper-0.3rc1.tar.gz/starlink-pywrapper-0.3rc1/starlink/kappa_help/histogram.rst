

HISTOGRAM
=========


Purpose
~~~~~~~
Computes an histogram of an NDF's values


Description
~~~~~~~~~~~
This application derives histogram information for an NDF array
between specified limits, using either a set number of bins (Parameter
NUMBIN) or a chosen bin width (Parameter WIDTH). The histogram is
reported, and may optionally be written to a text log file, and/or
plotted graphically.
By default, each data value contributes a value of one to the
corresponding histogram bin, but alternative weights may be supplied
via Parameter WEIGHTS.


Usage
~~~~~


::

    
       histogram in numbin range [comp] [logfile]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the plot.
The width of the margins left for the annotation may be controlled
using Parameter MARGIN. The appearance of the axes (colours, fonts,
etc.) can be controlled using the Parameter STYLE. The dynamic default
is TRUE if CLEAR is TRUE, and FALSE otherwise. []



CLEAR = _LOGICAL (Read)
```````````````````````
If TRUE the current picture is cleared before the plot is drawn. If
CLEAR is FALSE not only is the existing plot retained, but also an
attempt is made to align the new picture with the existing picture.
Thus you can generate a composite plot within a single set of axes,
say using different colours or modes to distinguish data from
different datasets. [TRUE]



COMP = LITERAL (Read)
`````````````````````
The name of the NDF array component to have its histogram computed:
"Data", "Error", "Quality" or "Variance" (where "Error" is the
alternative to "Variance" and causes the square root of the variance
values to be taken before computing the statistics). If "Quality" is
specified, then the quality values are treated as numerical values (in
the range 0 to 255). ["Data"]



CUMUL = _LOGICAL (Read)
```````````````````````
Should a cumulative histogram be reported? [FALSE]



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation on which to produce the plot. If it is null
(!), no plot will be made. [Current graphics device]



IN = NDF (Read)
```````````````
The NDF data structure to be analysed.



LOGFILE = FILENAME (Write)
``````````````````````````
A text file into which the results should be logged. If a null value
is supplied (the default), then no logging of results will take place.
[!]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave for axis annotation, given as
fractions of the corresponding dimension of the current picture. Four
values may be given, in the order bottom, right, top, left. If fewer
than four values are given, extra values are used equal to the first
supplied value. If these margins are too narrow any axis annotation
may be clipped. If a null (!) value is supplied, the value used is
0.15 (for all edges) if either annotated axes or a key are produced,
and zero otherwise. [current value]



NUMBIN = _INTEGER (Read)
````````````````````````
The number of histogram bins to be used. This must lie in the range 2
to 10000. The suggested default is the current value. It is ignored if
WIDTH is not null.



OUT = NDF (Read)
````````````````
Name of the NDF structure to save the histogram in its data array. If
null (!) is entered the histogram NDF is not created. [!]



RANGE = LITERAL (Read)
``````````````````````
RANGE specifies the range of values for which the histogram is to be
computed. The supplied string should consist of up to three sub-
strings, separated by commas. For all but the option where you give
explicit numerical limits, the first sub-string must specify the
method to use. If supplied, the other two sub-strings should be
numerical values as described below (default values will be used if
these sub-strings are not provided). The following options are
available.


+ lower,upper -- You can supply explicit lower and upper limiting
values. For example, "10,200" would set the histogram lower limit to
10 and its upper limit to 200. No method name prefixes the two values.
If only one value is supplied, the "Range" method is adopted. The
limits must be within the dynamic range for the data type of the NDF
array component.
+ "Percentiles" -- The default values for the histogram data range are
set to the specified percentiles of the data. For instance, if the
value "Per,10,99" is supplied, then the lowest 10% and highest 1% of
the data values are excluded from the histogram. If only one value,
p1, is supplied, the second value, p2, defaults to (100 - p1). If no
values are supplied, the values default to "5,95". Values must be in
the range 0 to 100.
+ "Range" -- The minimum and maximum array values are used. No other
sub-strings are needed by this option. Null (!) is a synonym for the
"Range" method.
+ "Sigmas" -- The histogram limiting values are set to the specified
  numbers of standard deviations below and above the mean of the data.
  For instance, if the supplied value is "sig,1.5,3.0", then the
  histogram extends from the mean of the data minus 1.5 standard
  deviations to the mean plus 3 standard deviations. If only one value
  is supplied, the second value defaults to the supplied value. If no
  values are supplied, both default to "3.0".

The "Percentiles" and "Sigmas" methods are useful to generate a first
pass at the histogram. They reduce the likelihood that all but a small
number of values lie within a few histogram bins.
The extreme values are reported unless Parameter RANGE is specified on
the command line. In this case extreme values are only calculated
where necessary for the chosen method.
The method name can be abbreviated to a single character, and is case
insensitive. The initial value is "Range". The suggested defaults are
the current values, or ! if these do not exist. [current value]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the annotated axes and data values.
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
The appearance of the histogram curve is controlled by the attributes
Colour(Curves), Width(Curves), etc. (The synonym Line may be used in
place of Curves.) [current value]



TITLE = LITERAL (Read)
``````````````````````
Title for the histogram NDF. ["KAPPA - Histogram"]



WEIGHTS = NDF (Read)
````````````````````
An optional NDF holding weights associated with each input pixel value
(supplied via parameter IN). Together with parameter WEIGHTSTEP, these
determine the count added to the corresponding histogram bin for each
input pixel value. For instance, weights could be related to the
variance of the data values, or to the position of the data values
within the input NDF. If a null value (!) is supplied for WEIGHTS, all
input values contribute a count of one to the corresponding histogram
bin. If an NDF is supplied, the histogram count for a particular input
pixel is formed by dividing its weight value (supplied in the WEIGHTS
NDF) by the value of parameter WEIGHTSTEP, and then taking the nearest
integer. Input pixels with bad or zero weights are excluded from the
histogram. [!]



WEIGHTSTEP = _DOUBLE (Read)
```````````````````````````
Only accessed if a value is supplied for parameter WEIGHTS. WEIGHTSTEP
is the increment in weight value that corresponds to a unit increment
in histogram count.



WIDTH = _DOUBLE (Read)
``````````````````````
The bin width. This is the alternative to setting the number of bins.
The bins of the chosen width start from the minimum value and do not
exceed the maximum value. Values are constrained to give between 2 and
10000 bins. If this parameter is set to null (!), the data range and
Parameter NUMBIN are used to specify the bin width. [!]



XLEFT = _DOUBLE (Read)
``````````````````````
The axis value to place at the left hand end of the horizontal axis of
the plot. If a null (!) value is supplied, the minimum data value in
the histogram is used. The value supplied may be greater than or less
than the value supplied for XRIGHT. [!]



XLOG = _LOGICAL (Read)
``````````````````````
TRUE if the plot X axis is to be logarithmic. Any histogram bins which
have negative or zero central data values are omitted from the plot.
[FALSE]



XRIGHT = _DOUBLE (Read)
```````````````````````
The axis value to place at the right hand end of the horizontal axis
of the plot. If a null (!) value is supplied, the maximum data value
in the histogram is used. The value supplied may be greater than or
less than the value supplied for XLEFT. [!]



YBOT = _DOUBLE (Read)
`````````````````````
The axis value to place at the bottom end of the vertical axis of the
plot. If a null (!) value is supplied, the lowest count the histogram
is used. The value supplied may be greater than or less than the value
supplied for YTOP. [!]



YLOG = _LOGICAL (Read)
``````````````````````
TRUE if the plot Y axis is to be logarithmic. Empty bins are removed
from the plot if the Y axis is logarithmic. [FALSE]



YTOP = _DOUBLE (Read)
`````````````````````
The axis value to place at the top end of the vertical axis of the
plot. If a null (!) value is supplied, the largest count in the
histogram is used. The value supplied may be greater than or less than
the value supplied for YBOT. [!]



Examples
~~~~~~~~
histogram image 100 ! device=!
Computes and reports the histogram for the data array in the NDF
called image. The histogram has 100 bins and spans the full range of
data values.
histogram ndf=spectrum comp=variance range="100,200" numbin=20
Computes and reports the histogram for the variance array in the NDF
called spectrum. The histogram has 20 bins and spans the values
between 100 and 200. A plot is made to the current graphics device.
histogram ndf=spectrum comp=variance range="100,204" width=5
This behaves the same as the previous example, even though it
specifies a larger maximum, as the same number of width=5 bins are
used.
histogram cube(3,4,) 10 si out=c3_4_hist device=!
Computes and reports the histogram for the z-vector at (x,y) element
(3,4) of the data array in the 3-dimensional NDF called cube. The
histogram has 10 bins and spans a range three standard deviations
either side of the mean of the data values. The histogram is written
to a one-dimensional NDF called c3_4_hist.
histogram cube numbin=32 ! device=xwindows style="title=cube"
Computes and reports the histogram for the data array in the NDF
called cube. The histogram has 32 bins and spans the full range of
data values. A plot of the histogram is made to the XWINDOWS device,
and is titled "cube".
histogram cube numbin=32 ! device=xwindows ylog style=^style.dat
As in the previous example except the logarithm of the number in each
histogram bin is plotted, and the contents of the text file style.dat
control the style of the resulting graph. The plotting style specified
in file style.dat becomes the default plotting style for future
invocations of HISTOGRAM.
histogram cube numbin=32 ! device=xw ylog tempstyle=^style.dat
This is the same as the previous example, except that the style
specified in file style.dat does not become the default style for
future invocations of HISTOGRAM.
histogram halley(~200,~300) "pe,10,90" logfile=hist.dat \
Computes the histogram for the central 200 by 300 elements of the data
array in the NDF called halley, and writes the results to a logfile
called hist.dat. The histogram uses the current number of bins, and
includes data values between the 10 and 90 percentiles. A plot appears
on the current graphics device.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISTAT, MSTATS, NUMB, STATS; Figaro: HIST, ISTAT.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995, 1998-2000, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2005-2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2008-2012, 2014 Science and Technology Facilities
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
LABEL, TITLE, UNITS, and HISTORY components of the input NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




