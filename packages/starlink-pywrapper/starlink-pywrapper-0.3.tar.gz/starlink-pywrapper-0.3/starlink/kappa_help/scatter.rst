

SCATTER
=======


Purpose
~~~~~~~
Displays a scatter plot between data in two NDFs


Description
~~~~~~~~~~~
This application displays a two-dimensional plot in which the
horizontal axis corresponds to the data value in the NDF given by
Parameter IN1, and the vertical axis corresponds to the data value in
the NDF given by Parameter IN2. Optionally, the variance, standard
deviation or quality may be used instead of the data value for either
axis (see Parameters COMP1 and COMP2). A symbol is displayed at an
appropriate position in the plot for each pixel which has a good value
in both NDFs, and falls within the bounds specified by Parameter
XLEFT, XRIGHT, YBOT and YTOP. The type of symbol may be specified
using Parameter MARKER.
The supplied arrays may be compressed prior to display (see Parameter
COMPRESS). This reduces the number of points in the scatter plot, and
also reduces the noise in the data.
The Pearson correlation coefficient of the displayed scatter plot is
also calculated and displayed, and written to output parameter CORR.


Usage
~~~~~


::

    
       scatter in1 in2 comp1 comp2 device
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the plot.
The width of the margins left for the annotation may be controlled
using Parameter MARGIN. The appearance of the axes (colours, founts,
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



COMP1 = LITERAL (Read)
``````````````````````
The NDF array component to be displayed on the horizontal axis. It may
be "Data", "Quality", "Variance", or "Error" (where "Error" is an
alternative to "Variance" and causes the square root of the variance
values to be displayed). If "Quality" is specified, then the quality
values are treated as numerical values (in the range 0 to 255).
["Data"]



COMP2 = LITERAL (Read)
``````````````````````
The NDF array component to be displayed on the vertical axis. It may
be "Data", "Quality", "Variance", or "Error" (where "Error" is an
alternative to "Variance" and causes the square root of the variance
values to be displayed). If "Quality" is specified, then the quality
values are treated as numerical values (in the range 0 to 255).
["Data"]



COMPRESS() = _INTEGER (Read)
````````````````````````````
The compression factors to be used when compressing the supplied
arrays prior to display. If any of the supplied values are greater
than 1, then the supplied arrays are compressed prior to display by
replacing each box of input pixels by a single pixel equal to the mean
of the pixels in the box. The size of each box in pixels is given by
the compression factors. No compression occurs if all values supplied
for this parameter are 1. If the number of values supplied is smaller
than the number of axes, the final value supplied is duplicated for
the remaining axes. [1]



CORR = _DOUBLE (Write)
``````````````````````
The Pearson correlation coefficient of the points in the scatter plot.
A value of zero is stored if the correlation coefficient cannot be
calculated.



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation on which to produce the plot. If a null value
(!) is supplied no plot will be made. [Current graphics device]



IN1 = NDF (Read)
````````````````
The NDF to be displayed on the horizontal axis.



IN2 = NDF (Read)
````````````````
The NDF to be displayed on the vertical axis.



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave for axis annotation, given as
fractions of the corresponding dimension of the current picture. Four
values may be given, in the order - bottom, right, top, left. If less
than four values are given, extra values are used equal to the first
supplied value. If these margins are too narrow any axis annotation
may be clipped. If a null (!) value is supplied, the used value is
0.15 (for all edges) if annotated axes are produced, and zero
otherwise. [current value]



MARKER = _INTEGER (Read)
````````````````````````
Specifies the symbol with which each position should be marked in the
plot. It should be given as an integer PGPLOT marker type. For
instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3 gives an
asterisk, 7 gives a triangle. The value must be larger than or equal
to -31. [current value]



NPIX = _INTEGER (Write)
```````````````````````
The number of points used to form the correlation coefficient.



PERC1( 2 ) = _REAL (Read)
`````````````````````````
The percentiles that define the default values for XLEFT and XRIGHT.
For example, [5,95] would result in the lowest and highest 5% of the
data value in IN1 being excluded from the plot if the default values
are accepted for XLEFT and XRIGHT. [current value]



PERC2( 2 ) = _REAL (Read)
`````````````````````````
The percentiles that define the default values for YBOT and YTOP. For
example, [5,95] would result in the lowest and highest 5% of the data
value in IN2 being excluded from the plot if the default values are
accepted for YBOT and YTOP. [current value]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the annotated axes, and markers.
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
The appearance of markers is controlled by Colour(Markers),
Width(Markers), etc. (the synonym Symbols may be used in place of
Markers). [current value]



XLEFT = _DOUBLE (Read)
``````````````````````
The axis value to place at the left hand end of the horizontal axis.
If a null (!) value is suplied, the value used is determined by
Parameter PERC1. The value supplied may be greater than or less than
the value supplied for XRIGHT. [!]



XRIGHT = _DOUBLE (Read)
```````````````````````
The axis value to place at the right hand end of the horizontal axis.
If a null (!) value is suplied, the value used is determined by
Parameter PERC1. The value supplied may be greater than or less than
the value supplied for XLEFT. [!]



YBOT = _DOUBLE (Read)
`````````````````````
The axis value to place at the bottom end of the vertical axis. If a
null (!) value is suplied, the value used is determined by Parameter
PERC2. The value supplied may be greater than or less than the value
supplied for YTOP. [!]



YTOP = _DOUBLE (Read)
`````````````````````
The axis value to place at the top end of the vertical axis. If a null
(!) value is suplied, the value used is determined by Parameter PERC2.
The value supplied may be greater than or less than the value supplied
for YBOT. [!]



Examples
~~~~~~~~
scatter cl123a cl123b
This displays a scatter plot of the data value in NDF cl123b against
the data value in NDF cl123a, on the current graphics device.
scatter cl123a cl123a pscol_l comp2=error compress=3
This displays a scatter plot of the error in NDF cl123a against the
data value in the same NDF. The graphics device used is "pscol_l". The
data is compressed by a factor of 3 on each axis before forming the
plot.



Notes
~~~~~


+ Any pixels that are bad (after any compression) in either array are
excluded from the plot, and from the calculation of the default axis
limits
+ The application stores two pictures in the graphics database in the
  following order: a FRAME picture containing the annotated axes and
  data plot, and a DATA picture containing just the data plot. Note, the
  FRAME picture is only created if annotated axes have been drawn, or if
  non-zero margins were specified using Parameter MARGIN. The world co-
  ordinates in the DATA picture will correspond to data value in the two
  NDFs.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA:NORMALIZE.


Copyright
~~~~~~~~~
Copyright (C) 1999, 2001, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. Copyright (C) 2010-2011 Science and Technology Facilities
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


+ Processing of bad pixels and automatic quality masking are
supported.
+ Only _REAL data can be processed directly. Other non-complex numeric
  data types will undergo a type conversion before processing occurs.




