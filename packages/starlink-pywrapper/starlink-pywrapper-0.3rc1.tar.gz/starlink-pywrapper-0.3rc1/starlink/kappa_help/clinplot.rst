

CLINPLOT
========


Purpose
~~~~~~~
Draws a spatial grid of line plots for an axis of a cube NDF


Description
~~~~~~~~~~~
This application displays a three-dimensional NDF as a series of line
plots of array value against position, arranged on a uniform spatial
grid and plotted on the current graphics device. The vertical axis of
each line plot represents array value, and the horizontal axis
represents position along a chosen axis (see Parameter USEAXIS). All
the line plots have the same axis limits.
This application will typically be used to display a grid of spectra
taken from a cube in which the current WCS Frame includes one spectral
axis (e.g. frequency) and two spatial axes (e.g. RA and Dec). For this
reason the following documentation refers to the "spectral axis" and
the "spatial axes". However, cubes containing other types of axes can
also be displayed, and references to "spectral" and "spatial" axes
should be interpreted appropriately.
A rectangular grid of NX by NY points (see Parameters NX and NY) is
defined over the spatial extent of the cube, and a spectrum is drawn
at each such point. If NX and NY equal the spatial dimensions of the
cube (which is the default for spatial axes of fewer than 31 pixels),
then one spectrum is drawn for every spatial pixel in the cube. For
speed, the spectrum will be binned up so that the number of elements
in the spectrum does not exceed the horizontal number of device pixels
available for the line plot.
Annotated axes for the spatial co-ordinates may be drawn around the
grid of line plots (see Parameter AXES). The appearance of these and
the space they occupy may be controlled in detail (see Parameters
STYLE and MARGIN).
The plot may take several different forms such as a "join-the-dots"
plot, a "staircase" plot, a "chain" plot (see Parameter MODE). The
plotting style (colour, founts, text size, etc.) may be specified in
detail using Parameter SPECSTYLE.
The data value at the top and bottom of each line plot can be
specified using Parameters YBOT and YTOP. The defaults can be selected
in several ways including percentiles (see Parameter LMODE).
The current picture is usually cleared before plotting the new
picture, but Parameter CLEAR can be used to prevent this, allowing the
plot (say) to be drawn over the top of a previously displayed grey
scale image.
The range and nature of the vertical and horizontal axes in each line
plot can be displayed in a key to the right of the main plot (see
Parameter KEY). Also, an option exists to add numerical labels to the
first (i.e. bottom left) line plot, see Parameter REFLABEL. However,
due to the nature of the plot, the text used may often be too small to
read.


Usage
~~~~~


::

    
       clinplot ndf [useaxis] [device] [nx] [ny]
       



ADAM parameters
~~~~~~~~~~~~~~~



ALIGN = _LOGICAL (Read)
```````````````````````
Controls whether or not the spectra should be aligned spatially with
an existing data plot. If ALIGN is TRUE, each spectrum will be drawn
in a rectangular cell that is centred on the corresponding point on
the sky. This may potentially cause the spectra to overlap, depending
on their spatial separation. If ALIGN is FALSE, then the spectra are
drawn in a regular grid of equal-sized cells that cover the entire
picture. This may cause them to be drawn at spatial positions that do
not correspond to their actual spatial positions within the supplied
cube. The dynamic default is TRUE if parameter CLEAR is TRUE and there
is an existing DATA picture on the graphics device. []



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes describing the spatial are to be
drawn around the outer edges of the plot. The appearance of the axes
can be controlled using the STYLE parameter. The dynamic default is to
draw axes only if the CLEAR parameter indicates that the graphics
device is not being cleared. []



BLANKEDGE = _LOGICAL (Read)
```````````````````````````
If TRUE then no tick marks or labels are placed on the edges of line
plots that touch the outer spatial axes (other edges that do not touch
the outer axes will still be annotated). This can avoid existing tick
marks being over-written when drawing a grid of spectra over the top
of a picture that includes annotated axes. The dynamic default is TRUE
if and only if the graphics device is not being cleared (i.e.
Parameter CLEAR is FALSE) and no spatial axes are being drawn (i.e.
Parameter AXES is FALSE). []



CLEAR = _LOGICAL (Read)
```````````````````````
If TRUE the current picture is cleared before the plot is drawn. IF
FALSE, then the display is left uncleared and an attempt is made to
align the spatial axes of the new plot with any spatial axes of the
existing plot. Thus, for instance, a while light image may be
displayed using DISPLAY, and then spectra drawn over the top of the
image using this application. [TRUE]



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be displayed. It may be "Data", "Quality",
"Variance", or "Error" (where "Error" is an alternative to "Variance"
and causes the square root of the variance values to be displayed). If
"Quality" is specified, then the quality values are treated as
numerical values (in the range 0 to 255). ["Data"]



DEVICE = DEVICE (Read)
``````````````````````
The name of the graphics device used to display the cube. [current
graphics device]



FILL = _LOGICAL (Read)
``````````````````````
If FILL is set to TRUE, then the display will be `stretched' to fill
the current picture in both directions. This can be useful to elongate
the spectra to reveal more detail by using more of the display surface
at the cost of different spatial scales, and when the spatial axes
have markedly different dimensions. The dynamic default is TRUE if
either of the spatial diensions is one. and FALSE otherwise. []



KEY = _LOGICAL (Read)
`````````````````````
If TRUE, then a "key" will be drawn to the right of the plot. The key
will include information about the vertical and horizontal axes of the
line plots, including the maximum and minimum value covered by the
axis and the quantity represented by the axis. The appearance of this
key can be controlled using Parameter KEYSTYLE, and its position can
be controlled using Parameter KEYPOS. [TRUE]



KEYPOS() = _REAL (Read)
```````````````````````
Two values giving the position of the key. The first value gives the
gap between the right-hand edge of the grid plot and the left-hand
edge of the key (0.0 for no gap, 1.0 for the largest gap). The second
value gives the vertical position of the top of the key (1.0 for the
highest position, 0.0 for the lowest). If the second value is not
given, the top of the key is placed level with the top of the grid
plot. Both values should be in the range 0.0 to 1.0. If a key is
produced, then the right-hand margin specified by Parameter MARGIN is
ignored. [current value]



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
The appearance of the text in the key can be changed by setting new
values for the attributes Colour(Strings), Font(Strings), etc.
[current value]



LMODE = LITERAL (Read)
``````````````````````
LMODE specifies how the defaults for Parameters YBOT and YTOP (the
lower and upper limit of the vertical axis of each line plot) should
be found. The supplied string should consist of up to three sub-
strings, separated by commas. The first sub-string must specify the
method to use. If supplied, the other two sub-strings should be
numerical values as described below (default values will be used if
these sub-strings are not provided). The following methods are
available.


+ "Range" -- The minimum and maximum data values in the supplied cube
are used as the defaults for YBOT and YTOP. No other sub-strings are
needed by this option.
+ "Extended" -- The minimum and maximum data values in the cube are
extended by percentages of the data range, specified by the second and
third sub-strings. For instance, if the value "Ex,10,5" is supplied,
then the default for YBOT is set to the minimum data value minus 10%
of the data range, and the default for YTOP is set to the maximum data
value plus 5% of the data range. If only one value is supplied, the
second value defaults to the supplied value. If no values are
supplied, both values default to "2.5".
+ "Percentile" -- The default values for YBOT and YTOP are set to the
specified percentiles of the data in the supplied cube. For instance,
if the value "Per,10,99" is supplied, then the default for YBOT is set
so that the lowest 10% of the plotted points are off the bottom of the
plot, and the default for YTOP is set so that the highest 1% of the
points are off the top of the plot. If only one value, p1, is
supplied, the second value, p2, defaults to (100 - p1). If no values
are supplied, the values default to "5,95".
+ "Sigma" -- The default values for YBOT and YTOP are set to the
  specified numbers of standard deviations below and above the mean of
  the data. For instance, if the value "sig,1.5,3.0" is supplied, then
  the default for YBOT is set to the mean of the data minus 1.5 standard
  deviations, and the default for YTOP is set to the mean plus 3
  standard deviations. If only one value is supplied, the second value
  defaults to the supplied value. If no values are provided both default
  to "3.0".

The method name can be abbreviated to a single character, and is case
insensitive. The initial value is "Range". [current value]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave around the outer spatial axes for
axis annotations, given as fractions of the corresponding dimension of
the current picture. The actual margins used may be increased to
preserve the aspect ratio of the data. Four values may be given, in
the order: bottom, right, top, left. If fewer than four values are
given, extra values are used equal to the first supplied value. If
these margins are too narrow any axis annotation may be clipped. If a
null (!) value is supplied, the value used is (for all edges); 0.15 if
annotated axes are being produced; and 0.0 otherwise. The initial
default is null. [current value]



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

The initial default is "Line". [current value]



NDF = NDF (Read)
````````````````
The input NDF structure containing the data to be displayed. It should
have three significant axes, i.e. whose dimensions are greater than 1.



NX = _INTEGER (Read)
````````````````````
The number of spectra to draw in each row. The spectra will be equally
spaced over the bounds of the x pixel axis. The dynamic default is the
number of pixels along the x axis of the NDF, so long as this value is
no more than 30. If the x axis spans more than 30 pixels, then the
dynamic default is 30 (meaning that some spatial pixels will be
ignored). []



NY = _INTEGER (Read)
````````````````````
The number of spectra to draw in each column. The spectra will be
equally spaced over the bounds of the y pixel axis. The dynamic
default is the number of pixels along the y axis of the NDF, so long
as this value is no more than 30. If the y axis spans more than 30
pixels, then the dynamic default is 30 (meaning that some spatial
pixels will be ignored). []



REFLABEL = _LOGICAL (Read)
``````````````````````````
If TRUE then the first line plot (i.e. the lower left spectrum) will
be annotated with numerical and textual labels describing the two
axes. Note, due to the small size of the line plot, such text may be
too small to read on some graphics devices. [current value]



SPECAXES = _LOGICAL (Read)
``````````````````````````
TRUE if axes are to be drawn around each spectrum. The appearance of
the axes can be controlled using the SPECSTYLE parameter. [TRUE]



SPECSTYLE = LITERAL (Read)
``````````````````````````
A group of attribute settings describing the plotting style to use
when drawing the axes and data values in the spectrum line plots.
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
By default the axes have interior tick marks, and are without labels
and a title to avoid overprinting on adjacent plots.
The appearance of the data values is controlled by the attributes
Colour(Curves), Width(Curves), etc. (the synonym Lines may be used in
place of Curves). [current value]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the annotated outer spatial axes (see Parameter AXES).
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



USEAXIS = LITERAL (Read)
````````````````````````
The WCS axis that will appear along the horizontal axis of each line
plot (the other two axes will be used as the spatial axes). The axis
can be specified using one of the following options.


+ Its integer index within the current Frame of the NDF (in the range
1 to 3 in the current frame).
+ Its symbol string such as "RA", or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. The dynamic default is the index of any spectral axis found
in the current Frame of the NDF. []



YBOT = _REAL (Read)
```````````````````
The data value for the bottom edge of each line plot. The dynamic
default is chosen in a manner determined by Parameter LMODE. []



YTOP = _REAL (Read)
```````````````````
The data value for the top edge of each line plot. The dynamic default
is chosen in a manner determined by Parameter LMODE. []



Examples
~~~~~~~~
clinplot cube useaxis=3
Plots a set of line plots of data values versus position along the
third axis for the three-dimensional NDF called cube on the current
graphics device. Axes are drawn around the grid of plots indicating
the spatial positions in the current co-ordinate Frame. The third axis
may not be spectral and the other two axes need not be spatial.
clinplot cube margin=0.1
As above, but if a search locates a spectral axis in the world co-
ordinate system, this is plotted along the horizontal of the line
plots, and the other axes are deemed to be spatial. Also the margin
for the spatial axes is reduced to 0.1 to allow more room for the grid
of line plots.
clinplot map(~5,~5,) useaxis=3 noaxes
Plots data values versus position for the central 5-by-5 pixel region
of the three-dimensional NDF called map on the current graphics
device. No spatial axes are drawn.
clinplot map(~5,~5,) useaxis=3 noaxes device=ps_l mode=hist
As the previous example but now the output goes to a text file
(pgplot.ps) which can be printed on a PostScript printer and the data
are plotted in histogram form.
clinplot nearc v style="'title=Ne Arc variance'" useaxis=1
reflabel=f Plots variance values versus position along Axis 1, for
each spatial position in dimensions two and three, for the three
dimensional NDF called nearc on the current graphics device. The plot
has a title of "Ne Arc variance". No labels are drawn around the
lower-left line plot.
clinplot ndf=speccube noclear specstyle="colour(curves)=blue"
Plots data values versus pixel co-ordinate at each spatial position
for the three-dimensional NDF called speccube on the current graphics
device. The plot is drawn over any existing plot and inherits the
spatial bounds of the previous plot. The data are drawn in blue,
probably to distinguish it from the previous plot drawn in a different
colour.
Notes:


+ If no Title is specified via the STYLE parameter, then the Title
component in the NDF is used as the default title for the annotated
axes. If the NDF does not have a Title component, then the default
title is taken from current co-ordinate Frame in the NDF. If this has
not been set explicitly, then the name of the NDF is used as the
default title.
+ If all the data values at a spatial position are bad, no line plot
  is drawn at that location.





Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: DISPLAY, LINPLOT, MLINPLOT; Figaro: SPECGRID; SPLAT.


Copyright
~~~~~~~~~
Copyright (C) 2005-2006 Particle Physics & Astronomy Research Council.
(C) 2008-2010 Science & Technology Facilities Council. All Rights
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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, WCS and UNITS components of the input NDF.
+ Processing of bad pixels and automatic quality masking are
  supported.




