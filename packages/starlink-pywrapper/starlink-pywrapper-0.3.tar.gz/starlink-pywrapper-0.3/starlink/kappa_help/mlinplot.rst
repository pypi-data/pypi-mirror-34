

MLINPLOT
========


Purpose
~~~~~~~
Draws a multi-line plot of the data values in a two-dimensional NDF


Description
~~~~~~~~~~~
This application plots a set of curves giving array value against
position in a two-dimensional NDF. All the curves are drawn within a
single set of annotated axes. Each curve is displaced vertically by a
specified offset to minimise overlap between the curves. These offsets
may be chosen automatically or specified by the user (see Parameter
SPACE). The curves may be drawn in several different ways such as a
"join-the-dots" plot, a "staircase" plot, a "chain" plot, etc., (see
Parameter MODE).
The data represented by each curve can be either a row or column
(chosen using Parameter ABSAXS) of any array component within the
supplied NDF (see Parameter COMP). Vertical error bars may be drawn if
the NDF contains a VARIANCE component (see Parameter ERRBAR). The
vertical axis of the plot represents array value (or the logarithm of
the array value---see Parameter YLOG). The horizontal axis represents
position, and may be annotated using an axis selected from the Current
Frame of the NDF (see Parameter USEAXIS).
Each curve may be labelled using its pixel index or a label specified
by the user (see Parameters LINLAB and LABELS). The appearance of
these labels (size, colour, fount, horizontal position, etc.) can be
controlled using Parameter STYLE. A key may be produced to the left of
the main plot listing the vertical offsets of the curves (see
Parameter KEY). The appearance of the key may be controlled using
Parameter KEYSTYLE. Its position may be controlled using Parameter
KEYOFF. Markers indicating the zero point for each curve may also be
drawn within the main plot (see Parameter ZMARK).
The bounds of the plot on both axes can be specified using parameters
XLEFT, XRIGHT, YBOT and YTOP. If not specified they take default
values which encompass the entire supplied data set. The current
picture is usually cleared before plotting the new picture, but
Parameter CLEAR can be used to prevent this, allowing several plots to
be "stacked" together. If a new plot is drawn over an existing plot,
then the bounds of the new plot are set automatically to the bounds of
the existing plot (XLEFT, XRIGHT, YBOT, and YTOP are then ignored).


Usage
~~~~~


::

    
       mlinplot ndf [comp] lnindx [mode] [xleft] [xright] [ybot] [ytop]
                [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



ABSAXS = _INTEGER (Read)
````````````````````````
This selects whether to plot rows or columns within the NDF. If ABSAXS
is 1, each curve will represent the array values within a single row
of pixels within the NDF. If it is 2, each curve will represent the
array values within a single column of pixels within the NDF. [1]



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the plot.
If a null (!) value is supplied, FALSE is used if the plot is being
aligned with an existing plot (see Parameter CLEAR), and TRUE is used
otherwise. Parameters USEAXIS and YLOG determine the quantities used
to annotated the horizontal and vertical axes respectively. The width
of the margins left for the annotation may be controlled using
Parameter MARGIN. The appearance of the axes (colours, founts, etc.)
can be controlled using the Parameter STYLE. [!]



CLEAR = _LOGICAL (Read)
```````````````````````
If TRUE the current picture is cleared before the plot is drawn. If
CLEAR is FALSE not only is the existing plot retained, but also the
previous plot is used to specify the axis limits. [TRUE]



COMP = LITERAL (Read)
`````````````````````
The NDF component to be plotted. It may be "Data", "Quality",
"Variance", or "Error" (where "Error" is an alternative to "Variance"
and causes the square root of the variance values to be displayed). If
"Quality" is specified, then the quality values are treated as
numerical values (in the range 0 to 255). ["Data"]



DEVICE = DEVICE (Read)
``````````````````````
The plotting device. [current graphics device]



ERRBAR = _LOGICAL (Read)
````````````````````````
TRUE if vertical error bars are to be drawn. This is only possible if
the NDF contains a VARIANCE component, and Parameter COMP is set to
"Data". The length of the error bars (in terms of standard deviations)
is set by Parameter SIGMA. The appearance of the error bars (width,
colour, etc.) can be controlled using Parameter STYLE. See also
Parameter FREQ. [FALSE]



FREQ = _INTEGER (Read)
``````````````````````
The frequency at which error bars are to be plotted. For instance, a
value of 2 would mean that alternate points have error bars plotted.
This lets some plots be less cluttered. FREQ must lie in the range 1
to half of the number of points to be plotted. FREQ is only accessed
when Parameter ERRBAR is TRUE. [1]



KEY = _LOGICAL (Read)
`````````````````````
TRUE if a key giving the offset of each curve is to be produced. The
appearance of this key can be controlled using Parameter KEYSTYLE, and
its position can be controlled using Parameter KEYPOS. [TRUE]



KEYPOS() = _REAL (Read)
```````````````````````
Two values giving the position of the key. The first value gives the
gap between the right-hand edge of the multiple-line plot and the
left-hand edge of the key (0.0 for no gap, 1.0 for the largest gap).
The second value gives the vertical position of the top of the key
(1.0 for the highest position, 0.0 for the lowest). If the second
value is not given, the top of the key is placed level with the top of
the multiple-line plot. Both values should be in the range 0.0 to 1.0.
If a key is produced, then the right-hand margin specified by
parameter MARGIN is ignored. [current value]



KEYSTYLE = GROUP (Read)
```````````````````````
A group of attribute settings describing the plotting style to use for
the key (see Parameter KEY).
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
The heading in the key can be changed by setting a value for the Title
attribute (the supplied heading is split into lines of no more than 17
characters). The appearance of the heading is controlled by attributes
Colour(Title), Font(Title), etc. The appearance of the curve labels is
controlled by attributes Colour(TextLab), Font(TextLab), etc. (the
synonym Labels can be used in place of TextLab). The appearance of the
offset values is controlled by attributes Colour(NumLab),
Font(NumLab), etc. (the synonym Offset can be used in place of
NumLab). Offset values are formatted using attributes Format(2), etc.
(the synonym Offset can be used in place of the value 2). [current
value]



LABELS = LITERAL (Read)
```````````````````````
A group of strings with which to label the plotted curves. A comma-
separated list of strings should be given, or the name of a text file
preceded by an up-arrow character "^". Such text files should contain
further comma-separated lists which will be read and interpreted in
the same manner. The first string obtained is used as the label for
the first curve requested using Parameter LNINDX, the second string is
used as the label for the second curve, etc. If the number of supplied
strings is fewer than the number of curves requested using LNINDX,
then extra default labels are used. These are equal to the NDF pixel
index of the row or column, preceded by a hash character ("#"). If a
null (!) value is supplied for LABELS, then default labels are used
for all curves. [!]



LINLAB = _LOGICAL (Read)
````````````````````````
If TRUE, the curves in the plot will be labelled using the labels
specified by Parameter LABELS. A single label is placed in-line with
the curve. The horizontal position and appearance of these labels can
be controlled using Parameter STYLE. [TRUE]



LNINDX = LITERAL (Read)
```````````````````````
Specifies the NDF pixel indices of the rows or columns to be displayed
(see Parameter ABSAXS). A maximum of 100 lines may be selected. It can
take any of the following values.


+ "ALL" or "*" -- All lines (rows or columns).
+ "xx,yy,zz" -- A list of line indices.
+ "xx:yy" -- Line indices between xx and yy inclusively. When xx is
omitted the range begins from the lower bound of the line dimension;
when yy is omitted the range ends with the maximum value it can take,
that is the upper bound of the line dimension or the maximum number of
lines this routine can plot.
+ Any reasonable combination of above values separated by commas.





MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave around the multiple-line plot for
axis annotation. The widths should be given as fractions of the
corresponding dimension of the current picture. Four values may be
given, in the order; bottom, right, top, left. If fewer than four
values are given, extra values are used equal to the first supplied
value. If these margins are too narrow any axis annotation may be
clipped. See also Parameter KEYPOS. [current value]



MARKER = _INTEGER (Read)
````````````````````````
This parameter is only accessed if Parameter MODE is set to "Chain" or
"Mark". It specifies the symbol with which each position should be
marked, and should be given as an integer PGPLOT marker type. For
instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3 gives an
asterisk, 7 gives a triangle. The value must be larger than or equal
to -31. [current value]



MODE = LITERAL (Read)
`````````````````````
Specifies the way in which each curve is drawn. MODE can take the
following values.


+ "Histogram" -- An histogram of the points is plotted in the style of
a "staircase" (with vertical lines only joining the y values and not
extending to the base of the plot). The vertical lines are placed
midway between adjacent x positions.
+ "Line" -- The points are joined by straight lines.
+ "Point" -- A dot is plotted at each point.
+ "Mark" -- Each point is marker with a symbol specified by Parameter
MARKER.
+ "Chain" -- A combination of "Line" and "Mark".

[current value]



NDF = NDF (Read)
````````````````
NDF structure containing the array to be plotted.



OFFSET() = _DOUBLE (Read)
`````````````````````````
This parameter is used to obtain the vertical offsets for the data
curve when Parameter SPACE is given the value "Free". The number of
values supplied should equal the number of curves being drawn.



PENS = GROUP (Read)
```````````````````
A group of strings, separated by semicolons, each of which specifies
the appearance of a pen to be used to draw a curve. The first string
in the group describes the pen to use for the first curve, the second
string describes the pen for the second curve, etc. If there are fewer
strings than curves, then the supplied pens are cycled through again,
starting at the beginning. Each string should be a comma-separated
list of plotting attributes to be used when drawing the curve. For
instance, the string "width=0.02,colour=red,style=2" produces a thick,
red, dashed curve. Attributes which are unspecified in a string
default to the values implied by Parameter STYLE. If a null value (!)
is given for PENS, then the pen attributes implied by Parameter STYLE
are used. [!]



SIGMA = LITERAL (Read)
``````````````````````
If vertical error bars are produced (see Parameter ERRBAR), then SIGMA
gives the number of standard deviations that the error bars are to
represent. [current value]



SPACE = LITERAL (Read)
``````````````````````
The value of this parameter specifies how the vertical offset for each
data curve is determined. It should be given one of the following
values:


+ "Average" -- The offsets are chosen automatically so that the
average data values of the curves are evenly spaced between the upper
and lower limits of the plotting area. Any line- to-line striping is
thus hidden and the amount of overlap of adjacent traces is minimised.
+ "Constant" -- The offsets are chosen automatically so that the zero
points of the curves are evenly spaced between the upper and lower
limits of the plotting area. The width of any line-to-line strip is
constant, which could result in the curves becoming confused if the
bias of a curve from its zero point is so large that it overlaps
another curve.
+ "Free" -- The offsets to use are obtained explicitly using Parameter
OFFSET.
+ "None" -- No vertical offsets are used. All curves are displayed
  with the same zero point.

The input can be abbreviated to an unambiguous length and is case
insensitive. ["Average"]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the annotated axes, data curves, error bars, zero
markers, and curve labels.
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
The appearance of the data curves is controlled by the attributes
Colour(Curves), Width(Curves), etc. (the synonym Lines may be used in
place of Curves). The appearance of markers used if Parameter MODE is
set to "Point", "Mark" or "Chain" is controlled by Colour(Markers),
Width(Markers), etc. (the synonym Symbols may be used in place of
Markers). The appearance of the error bars is controlled using
Colour(ErrBars), Width(ErrBars), etc. (see Parameter ERRBAR). The
appearance of the zero-point markers is controlled using
Colour(ZeroMark), Size(ZeroMark), etc. The appearance of the curve
labels is controlled using Colour(Labels), Size(Labels), etc.
LabPos(Left) controls the horizontal position of the in-line curve
label (see Parameter LINLAB), and LabPos(Right) controls the
horizontal position of the curve label associated with the right-hand
zero-point marker (see Parameter ZMARK). LabPos without any qualifier
is equivalent to LabPos(Left). LabPos values are floating point, with
0.0 meaning the left edge of the plotting area, and 1.0 the right
edge. Values outside the range 0 to 1 may be used. [current value]



USEAXIS = LITERAL (Read)
````````````````````````
The quantity to be used to annotate the horizontal axis of the plot
specified by using one of the following options.


+ An integer index of an axis within the current Frame of the input
NDF (in the range 1 to the number of axes in the current Frame).
+ An axis symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

The quantity used to annotate the horizontal axis must have a defined
value at all points in the array, and must increase or decrease
monotonically along the array. For instance, if RA is used to annotate
the horizontal axis, then an error will be reported if the profile
passes through RA=0 because it will introduce a non-monotonic jump in
axis value (from 0h to 24h, or 24h to 0h). If a null (!) value is
supplied, the value of Parameter ABSAXS is used. [!]



XLEFT = LITERAL (Read)
``````````````````````
The axis value to place at the left-hand end of the horizontal axis.
If a null (!) value is supplied, the value used is the first element
in the data being displayed. The value supplied may be greater than or
less than the value supplied for XRIGHT. A formatted value for the
quantity specified by parameter USEAXIS should be supplied. [!]



XRIGHT = LITERAL (Read)
```````````````````````
The axis value to place at the right-hand end of the horizontal axis.
If a null (!) value is supplied, the value used is the last element in
the data being displayed. The value supplied may be greater than or
less than the value supplied for XLEFT. A formatted value for the
quantity specified by parameter USEAXIS should be supplied. [!]



YBOT = _DOUBLE (Read)
`````````````````````
The data value to place at the bottom end of the vertical axis. If a
null (!) value is supplied, the value used is the lowest data value to
be displayed, after addition of the vertical offsets. The value
supplied may be greater than or less than the value supplied for YTOP.
[!]



YLOG = _LOGICAL (Read)
``````````````````````
TRUE if the value displayed on the vertical axis is to be the
logarithm of the supplied data values. If TRUE, then the values
supplied for parameters YTOP and YBOT should be values for the
logarithm of the data value, not the data value itself. [FALSE]



YTOP = _DOUBLE (Read)
`````````````````````
The data value to place at the top end of the vertical axis. If a null
(!) value is supplied, the value used is the highest data value to be
displayed, after addition of the vertical offsets. The value supplied
may be greater than or less than the value supplied for YBOT. [!]



ZMARK = _LOGICAL (Read)
```````````````````````
If TRUE, then a pair of short horizontal lines are drawn at the left
and right edges of the main plot for each curve. The vertical position
of these lines corresponds to the zero point for the corresponding
curve. The right-hand marker is annotated with the curve label (see
Parameter LABELS). The appearance of these markers can be controlled
using the Parameter STYLE. [TRUE]



Examples
~~~~~~~~
mlinplot rcw3_b1 reset \
Plot the first five rows of the two-dimensional NDF file, rcw3_b1 on
the current graphics device. The lines are offset such that the
averages of the rows are evenly separated in the direction of the
vertical axis.
mlinplot rcw3_b1 lnindx="1,3,5,7:10" \
Plot the rows 1, 3, 5, 7, 8, 9 and 10 of the two-dimensional NDF file,
rcw3_b1, on the current graphics device.
mlinplot rcw3_b1 lnindx=* \
Plot all rows of the two-dimensional NDF file, rcw3_b1, on the current
graphics device.
mlinplot rcw3_b1 lnindx=* style="colour(curve)=red+width(curve)=4" \
As the previous example, but the rows are drawn in red at four times
normal thickness. The change of line coluor persists to the next
invocation, but not the temporary widening of the lines.
mlinplot rcw3_b1 lnindx=* style="+width(curve)=4" \
As the previous example, but now the rows are drawn in the current
line colour.
mlinplot rcw3_b1 absaxs=2 lnindx="20:25,30,31" \
Plot columns 20, 21, 22, 23, 24, 25, 30 and 31 of the two-dimensional
NDF file, rcw3_b1, on the current graphics device.
mlinplot rcw3_b1 style="Title=CRDD rcw3_b1" \
Plot the currently selected rows of the two-dimensional NDF file,
rcw3_b1, on the current graphics device. The plot has a title of "CRDD
rcw3_b1".
mlinplot rcw3_b1(100:500,) ybot=0.0 ytop=1.0E-3 \
Plot the currently selected rows of the two-dimensional NDF, rcw3_b1,
between column 100 and column 500. The vertical display range is from
0.0 to 1.0E-3.
mlinplot rcw3_b1 space=constant device=ps_p \
Plot the currently selected rows of the two-dimensional NDF file,
rcw3_b1, on the ps_p device. The base lines are evenly distributed
over the range of the vertical axis.
mlinplot rcw3_b1 space=free offset=[0.,2.0E-4,4.0E-4,6.0E-4,0.1] \
Plot the currently selected rows of the two-dimensional NDF file,
rcw3_b1. The base lines are set at 0.0 for the first row, 2.0E-4 for
the second, 4.0E-4 for the third, 6.0E-4 for the fourthm and 0.1 for
the fifth.



Notes
~~~~~


+ If no Title is specified via the STYLE parameter, then the TITLE
component in the NDF is used as the default title for the annotated
axes. If the NDF does not have a TITLE component, then the default
title is taken from current co-ordinate Frame in the NDF. If this has
not been set explicitly, then the name of the NDF is used as the
default title.
+ The application stores a number of pictures in the graphics database
  in the following order: a FRAME picture containing the annotated axes,
  data plot, and optional key; a KEY picture to store the key if
  present; and a DATA picture containing just the data plot. Note, the
  FRAME picture is only created if annotated axes or a key has been
  drawn, or if non-zero margins were specified using Parameter MARGIN.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LINPLOT; Figaro: ESPLOT, IPLOTS, MSPLOT, SPLOT, SPECGRID;
SPLAT.


Copyright
~~~~~~~~~
Copyright (C) 1999, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2010 Science & Technology Facilities Council. All Rights
Reserved.


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
LABEL, TITLE, WCS and UNITS components of the NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Only double-
  precision floating-point data can be processed directly. Other non-
  complex data types will undergo a type conversion before the plot is
  drawn.




