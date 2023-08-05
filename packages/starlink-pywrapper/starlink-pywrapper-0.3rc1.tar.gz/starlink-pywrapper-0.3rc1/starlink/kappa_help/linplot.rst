

LINPLOT
=======


Purpose
~~~~~~~
Draws a line plot of the data values in a one-dimensional NDF


Description
~~~~~~~~~~~
This application creates a plot of array value against position for a
one-dimensional NDF. The vertical axis of the plot represents array
value, and the horizontal axis represents position. These can be
mapped in various ways on to the graphics surface (e.g. linearly,
logarithmically); see Parameters XMAP and YMAP).
The plot may take several different forms such as a "join-the-dots"
plot, a "staircase" plot, a "chain" plot (see Parameter MODE). Errors
on both the data values and the data positions may be represented in
several different ways (see Parameters ERRBAR and SHAPE). The plotting
style (colour, founts, text size, etc.) may be specified in detail
using Parameter STYLE.
The bounds of the plot on both axes can be specified using Parameters
XLEFT, XRIGHT, YBOT and YTOP. If not specified they take default
values which encompass the entire supplied data set. The current
picture is usually cleared before plotting the new picture, but
Parameter CLEAR can be used to prevent this, allowing several plots to
be "stacked" together. If a new plot is drawn over an existing plot,
then there is an option to allow the new plot to be aligned with the
existing plot (see Parameter ALIGN).
The input NDF may, for instance, contain a spectrum of data values
against wavelength, or it may contain data values along a one-
dimensional profile through an NDF of higher dimensionality. In the
latter case, the current co-ordinate Frame of the NDF may have more
than one axis. Any of the axes in the current co-ordinate Frame of the
input NDF may be used to annotate the horizontal axis of the plot
produced by this application. Alternatively, the horizontal axis may
be annotated with offset from the first array element measured within
the current co-ordinate Frame of the NDF. For instance, a one-
dimensional slice through a two-dimensional image calibrated in RA/DEC
could be annotated with RA, or DEC, or offset from the first element
(in arc-minutes, degrees, etc.). This offset is measured along the
path of the profile. The choice of annotation for the horizontal axis
is controlled by Parameter USEAXIS.


Usage
~~~~~


::

    
       linplot ndf [comp] [mode] [xleft] [xright] [ybot] [ytop] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



ALIGN = _LOGICAL (Read)
```````````````````````
Controls whether or not the new data plot should be aligned with an
existing data plot. If ALIGN is TRUE, the X axis values of the new
plot will be mapped into the co-ordinate system of the X axis in the
existing plot before being used (if this is not possible an error is
reported). In this case, the XLEFT, XRIGHT, YBOT, and YTOP parameters
are ignored and the bounds of the existing plot are used instead. If
ALIGN is FALSE, the new X axis values are used without change. The
bounds of the new plot are specified using Parameters XLEFT, XRIGHT,
YBOT, and YTOP as usual, and these bounds are mapped to the edges of
the existing picture. The ALIGN parameter is only accessed if
Parameter CLEAR is FALSE, and if there is another line plot within the
current picture. If a null (!) value is supplied, a value of TRUE will
be used if and only if a mapping can be found between the existing and
the new plots. A value of FALSE will be used otherwise. [!]



ALIGNSYS = LITERAL (Read)
`````````````````````````
Only used if a TRUE value is supplied for Parameter ALIGN. It
specifies the co-ordinate system in which the new plot and the
existing plot are aligned (for further details see the description of
the AlignSystem attribute in SUN/211). The supplied name should be a
valid co-ordinate system name for the horizontal axis (see the
description of the "System" attribute in SUN/211 for a list of these
names). It may also take the special value "Data", in which case
alignment occurs in the co-ordinate system represented by the current
WCS Frame in the supplied NDF. If a null (!) value is supplied The
alignment system is determined by the current value of AlignSystem
attribute in the supplied NDF. ["Data"]



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the plot.
If a null (!) value is supplied, the value used is FALSE if the plot
is being aligned with an existing plot (see Parameter ALIGN), and TRUE
otherwise. Parameter USEAXIS determines the quantity used to annotated
the horizontal axis. The width of the margins left for the annotation
may be controlled using Parameter MARGIN. The appearance of the axes
(colours, founts, etc.) can be controlled using the Parameter STYLE.
[!]



CLEAR = _LOGICAL (Read)
```````````````````````
If TRUE the current picture is cleared before the plot is drawn. If
CLEAR is FALSE not only is the existing plot retained, but also the
previous plot can be used to specify the axis limits (see Parameter
ALIGN). Thus you can generate a composite plot within a single set of
axes, say using different colours or modes to distinguish data from
different datasets. Note, alignment between the two plots is
controlled by the AlignSystem attribute of the data being displayed.
For instance, if you have an existing plot showing a spectrum plotted
against radio velocity and you overlay another spectrum, also in radio
velocity but with a different rest frequency, the appearance of the
final plot will depend on the value of the AlignSystem attribute of
the second spectrum. If AlignSystem is "Wavelen" (this is the default)
then the two spectra will be aligned in wavelength, but if AlignSystem
is "vrad" they will be aligned in radio velocity. There will be no
difference in effect between these two forms of alignment unless the
rest frequency is different in the two spectra. Likewise, the
AlignStdOfRest attribute of the second spectrum controls the standard
of rest in which alignment occurs. These attributes (like all other
attributes) may be examined and modified using WCSATTRIB.



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
TRUE if error bars are to be drawn. The error bars can comprise either
or both of the data and axis-centre errors, depending on what is
available in the supplied dataset. The Parameter SHAPE controls the
appearance of the error bars, and XSIGMA and YSIGMA control their
lengths. The ERRBAR parameter is ignored unless the Parameter COMP is
set to "Data". [FALSE]



FREQ = _INTEGER (Read)
``````````````````````
The frequency at which error bars are to be plotted. For instance, a
value of 2 would mean that alternate points have error bars plotted.
This lets some plots be less cluttered. FREQ must lie in the range 1
to half of the number of points to be plotted. FREQ is only accessed
when Parameter ERRBAR is TRUE. [1]



KEY = _LOGICAL (Read)
`````````````````````
TRUE if a key is to be plotted below the horizontal axis giving the
positions at the start and end of the plot, within the current co-
ordinate Frame of the NDF. If Parameter USEAXIS is zero (i.e. if the
horizontal axis is annotated with offset from the first array
element), then the positions refer to the centres of the first and
last elements in the supplied NDF, whether or not these elements are
actually visible in the plot. If USEAXIS is not zero (i.e. if the
horizontal axis is annotated with the value on one of the axes of the
NDF's current co-ordinate Frame), then the displayed positions
correspond to the two ends of the visible section of the horizontal
axis. The appearance of the key can be controlled using Parameter
KEYSTYLE. If a null (!) value is supplied, a key is produced if the
current co-ordinate Frame of the supplied NDF has two or more axes,
but no key is produced if it only has one axis. [!]



KEYSTYLE = LITERAL (Read)
`````````````````````````
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
error is reported). [current value]



LMODE = LITERAL (Read)
``````````````````````
LMODE specifies how the defaults for Parameters YBOT and YTOP (the
lower and upper limit of the vertical axis of the plot) should be
found. The supplied string should consist of up to three sub-strings,
separated by commas. The first sub-string must specify the method to
use. If supplied, the other two sub-strings should be numerical values
as described below (default values will be used if these sub-strings
are not provided). The following methods are available.


+ "Range" -- The minimum and maximum data values (including any error
bars) are used as the defaults for YBOT and YTOP. No other sub-strings
are needed by this option.
+ "Extended" -- The minimum and maximum data values (including error
bars) are extended by percentages of the data range, specified by the
second and third sub-strings. For instance, if the value "Ex,10,5" is
supplied, then the default for YBOT is set to the minimum data value
minus 10% of the data range, and the default for YTOP is set to the
maximum data value plus 5% of the data range. If only one value is
supplied, the second value defaults to the supplied value. If no
values are supplied, both values default to "2.5". Care should be
taken with this mode if YMAP is set to "Log" since the extension to
the data range caused by this mode may result in the axis encompassing
the value zero.
+ "Percentile" -- The default values for YBOT and YTOP are set to the
specified percentiles of the data (excluding error bars). For
instance, if the value "Per,10,99" is supplied, then the default for
YBOT is set so that the lowest 10% of the plotted points are off the
bottom of the plot, and the default for YTOP is set so that the
highest 1% of the points are off the top of the plot. If only one
value, p1, is supplied, the second value, p2, defaults to (100 - p1).
If no values are supplied, the values default to "5,95".
+ "Sigma" -- The default values for YBOT and YTOP are set to the
  specified numbers of standard deviations below and above the mean of
  the data. For instance, if the value "sig,1.5,3.0" is supplied, then
  the default for YBOT is set to the mean of the data minus 1.5 standard
  deviations, and the default for YTOP is set to the mean plus 3
  standard deviations. If only one value is supplied, the second value
  defaults to the supplied value. If no values are provided both default
  to "3.0".

The method name can be abbreviated to a single character, and is case
insensitive. The initial value is "Extended". [current value]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave for axis annotation, given as
fractions of the corresponding dimension of the current picture. Four
values may be given, in the order: bottom, right, top, left. If fewer
than four values are given, extra values are used equal to the first
supplied value. If these margins are too narrow any axis annotation
may be clipped. If a null (!) value is supplied, the value used is
0.15 (for all edges) if either annotated axes or a key are produced,
and zero otherwise. [current value]



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
Specifies the way in which data values are represented. MODE can take
the following values.


+ "Histogram" -- An histogram of the points is plotted in the style of
a "staircase" (with vertical lines only joining the y-axis values and
not extending to the base of the plot). The vertical lines are placed
midway between adjacent x-axis positions. Bad values are flanked by
vertical lines to the lower edge of the plot.
+ "GapHistogram" -- The same as the "Histogram" option except bad
values are not flanked by vertical lines to the lower edge of the
plot, leaving a gap.
+ "Line" -- The points are joined by straight lines.
+ "Point" -- A dot is plotted at each point.
+ "Mark" -- Each point is marker with a symbol specified by Parameter
MARKER.
+ "Chain" -- A combination of "Line" and "Mark".
+ "Step" -- Each point is displayed as a horizontal line, whose length
  is specified by the axis width of the pixel.

[current value]



NDF = NDF (Read)
````````````````
NDF structure containing the array to be plotted.



SHAPE = LITERAL (Read)
``````````````````````
Specifies the way in which errors are represented. SHAPE can take the
following values.


+ "Bars" -- Bars with serifs (i.e. cross pieces at each end) are drawn
joining the x-error limits and the y-error limits. The plotting
attribute "Size(ErrBars)" (see Parameter STYLE) can be used to control
the size of these serifs (the attribute value should be a
magnification factor; 1.0 gives default serifs).
+ "Cross" -- San-serif bars are drawn joining the x-error limits and
the y-error limits.
+ "Diamond" -- Adjacent error limits are joined to form an error
  diamond.

The length of the error bars can be controlled using Parameters XSIGMA
and YSIGMA. The colour, line width and line style used to draw them
can be controlled using the plotting attributes "Colour(ErrBars)",
"Width(ErrBars)" and "Style(ErrBars)" (see Parameter STYLE). SHAPE is
only accessed when Parameter ERRBAR is TRUE. [current value]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the annotated axes, data values, and error markers.
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
The appearance of the data values is controlled by the attributes
Colour(Curves), Width(Curves), etc. (the synonym Lines may be used in
place of Curves). The appearance of markers used if Parameter MODE is
set to "Point", "Mark" or "Chain" is controlled by Colour(Markers),
Width(Markers), etc. (the synonym Symbols may be used in place of
Markers). The appearance of the error symbols is controlled using
Colour(ErrBars), Width(ErrBars), etc. (see Parameter SHAPE). [current
value]



USEAXIS = LITERAL (Read)
````````````````````````
Specifies the quantity to be used to annotate the horizontal axis of
the plot using one of the following options.


+ An integer index of an axis within the current Frame of the input
NDF (in the range 1 to the number of axes in the current Frame).
+ An axis symbol string such as "RA", or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
and latitude axes respectively. Only those axis domains present are
available as options.
+ The special value 0 (zero), asks for the distance along the profile
  from the centre of the first element in the supplied NDF to be used to
  annotate the axis. This will be measured in the current co-ordinate
  Frame of the NDF.

The quantity used to annotate the horizontal axis must have a defined
value at all points in the array, and must increase or decrease
monotonically along the array. For instance, if RA is used to annotate
the horizontal axis, then an error will be reported if the profile
passes through RA=0 because it will introduce a non-monotonic jump in
axis value (from 0h to 24h, or 24h to 0h). If a null (!) value is
supplied, the value used is 1 if the current co-ordinate Frame in the
NDF is one-dimensional and 0 otherwise. [!]



XLEFT = LITERAL (Read)
``````````````````````
The axis value to place at the left hand end of the horizontal axis.
If a null (!) value is supplied, the value used is the value for the
first element in the supplied NDF (with a margin to include any
horizontal error bar). The value supplied may be greater than or less
than the value supplied for XRIGHT. A formatted value for the quantity
specified by Parameter USEAXIS should be supplied. See also Parameter
ALIGN. [!]



XMAP = LITERAL (Read)
`````````````````````
Specifies how the quantity represented by the X axis is mapped on to
the plot. The options are as follows


+ "Pixel" -- The mapping is such that pixel index within the input NDF
increases linearly across the plot.
+ "Distance" -- The mapping is such that distance along the curve
within the current WCS Frame of the input NDF increases linearly
across the plot.
+ "Log" -- The mapping is such that the logarithm (base 10) of the
value used to annotate the axis increases linearly across the plot. An
error will be reported if the dynamic range of the axis is less than
100, or if the range specified by XLEFT and XRIGHT encompasses the
value zero.
+ "Linear" -- The mapping is such that the value used to annotate the
axis increases linearly across the plot.
+ "Default" -- One of "Linear" or "log" is chosen automatically,
  depending on which one produces a more-even spread of values on the
  plot. ["Default"]





XRIGHT = LITERAL (Read)
```````````````````````
The axis value to place at the right hand end of the horizontal axis.
If a null (!) value is supplied, the value used is the value for the
last element in the supplied NDF (with a margin to include any
horizontal error bar). The value supplied may be greater than or less
than the value supplied for XLEFT. A formatted value for the quantity
specified by Parameter USEAXIS should be supplied. See also Parameter
ALIGN. [!]



XSIGMA = LITERAL (Read)
```````````````````````
If horizontal error bars are produced (see Parameter ERRBAR), then
XSIGMA gives the number of standard deviations that the error bars are
to represent. [current value]



YBOT = LITERAL (Read)
`````````````````````
The axis value to place at the bottom end of the vertical axis. If a
null (!) value is supplied, the value used is determined by Parameter
LMODE. The value of YBOT may be greater than or less than the value
supplied for YTOP. If Parameter YMAP is set to "ValueLog", then the
supplied value should be the logarithm (base 10) of the bottom data
value. See also Parameter ALIGN. [!]



YMAP = LITERAL (Read)
`````````````````````
Specifies how the quantity represented by the Y axis is mapped on to
the screen. The options are as follows.


+ "Linear" -- The data values are mapped linearly on to the screen.
+ "Log" -- The data values are logged logarithmically on to the
screen. An error will be reported if the dynamic range of the axis is
less than 100, or if the range specified by YTOP and YBOT encompasses
the value zero. For this reason, care should be taken over the choice
of value for Parameter LMODE, since some choices could result in the Y
range being extended so far that it encompasses zero.
+ "ValueLog" -- This is similar to "Log" except that, instead of
  mapping the data values logarithmically on to the screen, this option
  maps the log (base 10) of the data values linearly on to the screen.
  If this option is selected, the values supplied for Parameters YTOP
  and YBOT should be values for the logarithm of the data value, not the
  data value itself. ["Linear"]





YSIGMA = LITERAL (Read)
```````````````````````
If vertical error bars are produced (see Parameter ERRBAR), then
YSIGMA gives the number of standard deviations that the error bars are
to represent. [current value]



YTOP = LITERAL (Read)
`````````````````````
The axis value to place at the top end of the vertical axis. If a null
(!) value is supplied, the value used is determined by Parameter
LMODE. The value of LTOP may be greater than or less than the value
supplied for YBOT. If Parameter YMAP is set to "ValueLog", then the
supplied value should be the logarithm (base 10) of the bottom data
value. See also Parameter ALIGN. [!]



Examples
~~~~~~~~
linplot spectrum
Plots data values versus position for the whole of the one-dimensional
NDF called spectrum on the current graphics device. If the current co-
ordinate Frame of the NDF is also one-dimensional, then the horizontal
axis will be labelled with values on axis 1 of the current co-ordinate
Frame. Otherwise, it will be labelled with offset from the first
element.
linplot map(,100)
Plots data values versus position for row 100 in the two-dimensional
NDF called map on the current graphics device.
linplot spectrum(1:500) device=ps_l
Plots data values versus position for the first 500 elements of the
one-dimensional NDF called spectrum. The output goes to a text file
which can be printed on a PostScript printer.
linplot ironarc v style="'title=Fe Arc variance,drawdsb=0'"
Plots variance values versus position for the whole of the one-
dimensional NDF called ironarc on the current graphics device. The
plot has a title of "Fe Arc variance". If the data is from a dual
sideband instrument, the image sideband would normally be annotated
along the top edge of the plot, but the inclusion of "drawdsb=0" in
the style value prevents this.
linplot prof useaxis=dec xleft="23:30:22" xright="23:30:45"
This plots data values versus declination for those elements of the
one-dimensional NDF called prof with declination value between 23d 30m
22s, and 23d 30m 45s. This assumes that the current co-ordinate Frame
in the NDF has an axis with symbol "dec".
linplot prof useaxis=2 ybot=10 ytop=1000.0 ymap=log xmap=log
This plots the data values in the entire one-dimensional NDF called
prof, against the value described by the second axis in the current
co-ordinate Frame of the NDF. The values represented by both axes are
mapped logarithmically on to the screen. The bottom of the vertical
axis corresponds to a data value of 10.0 and the top corresponds to a
data value of 1000.0.
linplot xspec mode=p errbar xsigma=3 ysigma=3 shape=d
style=^my_sty This plots the data values versus position for the
dataset called xspec. Each pixel is plotted as a point surrounded by
diamond-shaped error bars. The error bars are 3-sigma error bars. The
plotting style is read from text file my_sty. This could, for
instance, contain strings such as: colour(err)=pink, colour(sym)=red,
tickall=0, edge(2)=right. These cause the error bars to be drawn in
pink, the points to be drawn in red, tick marks to be restricted to
the labelled edges of the plot, and the vertical axis (axis 2) to be
annotated on the right-hand edge of the plot. The plotting style
specified in file my_sty becomes the default plotting style for future
invocations of LINPLOT.
linplot xspec mode=p errbar xsigma=3 ysigma=3 shape=d
style=+^my_sty This is the same as the previous example, except that
the style specified in file my_sty does not become the default style
for future invocations of LINPLOT.
linplot ndf=spectrum noclear align
Plots data values versus pixel co-ordinate for the whole of the one-
dimensional NDF called spectrum on the current graphics device. The
plot is drawn over any existing plot and inherits the bounds of the
previous plot on both axes. A warning will be reported if the labels
for the horizontal axes of the two plots are different.
linplot spectrum system="'system(1)=freq,unit(1)=GHz'"
This example assumes that the current co-ordinate Frame of NDF
spectrum is a SpecFrame. The horizontal axis (Axis "1") is labelled
with frequency values, in units of GHz. If the SpecFrame represents
some other system (such as wavelength, velocity, energy), or has some
other units, then the conversion is done automatically. Note, a
SpecFrame is a specialised class of Frame which knows how to do these
conversions; the above command will fail if the current co-ordinate
Frame in the NDF is a simple Frame (such as the AXIS Frame). A
SpecFrame can be created from an AXIS Frame using application WCSADD.



Notes
~~~~~


+ If the horizontal axis is described by a DSBSpecFrame (a description
of the co-ordinates attached to a dual-sideband spectrum) in the NDF's
WCS FrameSet, then the unselected sideband will be annotated along the
top edge of the plot.
+ If no Title is specified via the STYLE parameter, then the Title
component in the NDF is used as the default title for the annotated
axes. If the NDF does not have a Title component, then the default
title is taken from current co-ordinate Frame in the NDF. If this has
not been set explicitly, then the name of the NDF is used as the
default title.
+ Default axis errors and widths are used, if none are present in the
NDF. The defaults are the constants 0 and 1 respectively.
+ The application stores a number of pictures in the graphics database
  in the following order: a FRAME picture containing the annotated axes,
  data plot, and optional key; a KEY picture to store the key if
  present; and a DATA picture containing just the data plot. Note, the
  FRAME picture is only created if annotated axes or a key has been
  drawn, or if non-zero margins were specified using Parameter MARGIN.
  The world co-ordinates in the DATA picture will correspond to offset
  along the profile on the horizontal axis, and data value (or logarithm
  of data value) on the vertical axis. On exit the current database
  picture for the chosen device reverts to the input picture.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PROFILE, MLINPLOT; Figaro: ESPLOT, IPLOTS, MSPLOT, SPECGRID,
SPLOT; SPLAT.


Copyright
~~~~~~~~~
Copyright (C) 1998-2000, 2003-2004 Central Laboratory of the Research
Councils. Copyright (C) 2006-2007 Particle Physics & Astronomy
Research Council. Copyright (C) 2008, 2010, 2011, 2016 Science &
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


+ This routine correctly processes the AXIS, DATA, VARIANCE, QUALITY,
LABEL, TITLE, WCS and UNITS components of the NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Only double-
  precision floating-point data can be processed directly. Other non-
  complex data types will undergo a type conversion before the plot is
  drawn.




