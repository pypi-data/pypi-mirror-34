

ZAPLIN
======


Purpose
~~~~~~~
Replaces regions in a two-dimensional NDF by bad values or by linear
interpolation


Description
~~~~~~~~~~~
This routine replaces selected areas within a two-dimensional input
NDF (specified by Parameter IN), either by filling the areas with bad
values, or by linear interpolation between neighbouring data values
(see Parameter ZAPTYPE). Each area to be replaced can be either a
range of pixel columns extending the full height of the image, a range
of pixel lines extending the full width of the image, or a rectangular
region with edges parallel to the pixel axes (see Parameter LINCOL).
The bounds of the area to be replaced can be specified either by using
a graphics cursor, or directly in response to parameter prompts, or by
supplying a text file containing the bounds (see Parameter MODE). In
the first two modes the application loops asking for new areas to zap,
until told to quit or an error is encountered. In the last mode
processing stops when the end of file is found. An output text file
may be produced containing a description of the areas replaced (see
Parameter COLOUT). This file may be used to specify the regions to be
replaced in a subsequent invocation of ZAPLIN.


Usage
~~~~~


::

    
       zaplin in out [title] { lincol=?
                             { columns=? lines=?
                             { colin=?
                             mode
       



ADAM parameters
~~~~~~~~~~~~~~~



COLIN = FILENAME (Read)
```````````````````````
The name of a text file containing the bounds of the areas to be
replaced. This parameter is only accessed if Parameter MODE is set to
"File". Each record in the file must be either a blank line, a comment
(indicated by a "!" or "#" in column 1 ), or a definition of an area
to be replaced, consisting of three or four space-separated fields. If
a range of columns is to be replaced, each of the first two fields
should be a formatted value for the first axis of the current co-
ordinate Frame of the input NDF, and the third field should be the
single character "C". If a range of lines is to be replaced, each of
the first two fields should be a formatted value for the second axis
of the current co-ordinate Frame, and the third field should be the
single character "L". If a rectangular region is to be replaced, the
first two fields should give the formatted values on axes 1 and 2 at
one corner of the box, and the second two fields should give the
formatted values on axes 1 and 2 at the opposite corner of the box.



COLOUT = FILENAME (Read)
````````````````````````
The name of an output text file in which to store descriptions of the
areas replaced by the current invocation of this application. It has
the same format as the input file accessed using Parameter COLIN, and
so may be used as input on a subsequent invocation. This parameter is
not accessed if Parameter MODE is set to "File". If COLOUT is null
(!), no file will be created. [!]



COLUMNS = LITERAL (Read)
````````````````````````
A pair of X values indicating the range of columns to be replaced. All
columns between the supplied values will be replaced. This parameter
is only accessed if Parameter LINCOL is set to "Columns" or "Region",
and Parameter MODE is set to "Interface". Each X value should be given
as a formatted value for axis 1 of the current co-ordinate Frame of
the input NDF. The two values should be separated by a comma, or by
one or more spaces.



DEVICE = DEVICE (Read)
``````````````````````
The graphics device to use if Parameter MODE is set to "Cursor".
[Current graphics device]



IN = NDF (Read)
```````````````
The input image.



LINCOL = LITERAL (Read)
```````````````````````
The type of area is to be replaced. This Parameter is only accessed if
Parameter MODE is set to "Cursor" or "Interface". The options are as
follows.


+ "Lines" -- Replaces lines of pixels between the Y values specified
by Parameter LINES. Each replaced line extends the full width of the
image.
+ "Columns" -- Replaces columns of pixels between the X values
specified by Parameter COLUMNS. Each replaced column extends the full
height of the image.
+ "Region" -- Replaces the rectangular region of pixels within the X
  and Y bounds specified by Parameters COLUMNS and LINES. The edges of
  the box are parallel to the pixel axes.

If this parameter is specified on the command line, and Parameter MODE
is set to "Interface", only one area will be replaced; otherwise a
series of areas will be replaced until a null (!) value is supplied
for this parameter.



LINES = LITERAL (Read)
``````````````````````
A pair of Y values indicating the range of lines to be replaced. All
lines between the supplied values will be replaced. This parameter is
only accessed if Parameter LINCOL is set to "Lines" or "Region", and
Parameter MODE is set to "Interface". Each Y value should be given as
a formatted value for axis 2 of the current co-ordinate Frame of the
input NDF. The two values should be separated by a comma, or by one or
more spaces.



MARKER = INTEGER (Read)
```````````````````````
This parameter is only accessed if Parameter PLOT is set to "Mark". It
specifies the type of marker with which each cursor position should be
marked, and should be given as an integer PGPLOT marker type. For
instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3 gives an
asterisk, 7 gives a triangle. The value must be larger than or equal
to -31. [current value]



MODE = LITERAL (Read)
`````````````````````
The method used to obtain the bounds of the areas to be replaced. The
supplied string can be one of the following options.


+ "Interface" -- bounds are obtained using Parameters COLUMNS, and
LINES. The type of area to be replaced is specified using Parameter
LINCOL.
+ "Cursor" -- bounds are obtained using the graphics cursor of the
device specified by Parameter DEVICE. The type of area to be replaced
is specified using Parameter LINCOL. The WCS information stored with
the picture in the graphics database is used to map the supplied
cursor positions into the pixel co-ordinate Frame of the input NDF. A
message is displayed indicating the co-ordinate Frame in which the
picture and the output NDF were aligned. Graphics may be drawn over
the image indicating the region to be replaced (see Parameter PLOT).
+ "File" -- the bounds and type of each area to be replaced are
  supplied in the text file specified by Parameter COLIN.

[current value]



NOISE = _LOGICAL (Read)
```````````````````````
This parameter is only accessed if Parameter ZAPTYPE is set to
"Linear". If a TRUE value is supplied, gaussian noise is added to each
interpolated pixel value. The variance of the noise is equal to the
variance of the data value being replaced. If the data variance is
bad, no noise is added. If the input NDF has no VARIANCE component,
variances equal to the absolute data value are used. This facility is
provided for cosmetic use. [FALSE]



OUT = NDF (Write)
`````````````````
The output image.



PLOT = LITERAL (Read)
`````````````````````
The type of graphics to be used to mark each cursor position. The
appearance of these graphics (colour, size, etc ) is controlled by the
STYLE parameter. PLOT can take any of the following values.


+ "Adapt" -- Causes "Box" to be used if a region is being replaced,
"Vline" is a range of columns is being replaced, and "Hline" if a
range of lines is being replaced.
+ "Box" -- A rectangular box with edges parallel to the edges of the
graphics device is drawn with the two specified positions at opposite
corners.
+ "Mark" -- Each position is marked by the symbol specified by
Parameter MARKER.
+ "None" -- No graphics are produced.
+ "Vline" -- A vertial line is drawn through each specified position,
extending the entire height of the selected picture.
+ "Hline" -- A horizontal line is drawn through each specified
  position, extending the entire width of the selected picture.

[current value]



STYLE = LITERAL (Read)
``````````````````````
A group of attribute settings describing the style to use when drawing
the graphics specified by Parameter PLOT.
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
The appearance of vertical and horizontal lines is controlled by the
attributes Colour(Curves), Width(Curves), etc. (the synonym Lines may
be used in place of Curves). The appearance of boxes is controlled by
the attributes Colour(Border), Size(Border), etc. (the synonym Box may
be used in place of Border). The appearance of markers is controlled
by attributes Colour(Markers), Size(Markers), etc. [current value]



TITLE = LITERAL (Read)
``````````````````````
Title for the output image. A null value (!) propagates the title from
the input image to the output image. [!]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the input
NDF has more than two axes. A group of two strings should be supplied
specifying the two axes spanning the plane containing the areas to be
replaced. Each axis can be specified using one of the following
options.


+ Its integer index within the current Frame of the output NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the first two significant NDF pixel axes are used. [!]



ZAPTYPE = LITERAL (Read)
````````````````````````
The method used to choose the replacement pixel values. It should be
one of the options below.


+ "Bad" -- Replace the selected pixels by bad values.
+ "Linear" -- Replace the selected pixels using linear interpolation.
  If a range of lines is replaced, then the interpolation is performed
  vertically between the first non-bad pixels above and below the
  selected lines. If a range of columns is replaced, then the
  interpolation is performed horizontally between the first non-bad
  pixels to the left and right of the selected columns. If a rectangular
  region is replaced, then the interpolation is bi-linear between the
  nearest non-bad pixels on all four edges of the selected region. If
  interpolation is not possible (for instance, if the selected pixels
  are at the edge of the array) then the pixels are replaced with bad
  values. ["Linear"]





Examples
~~~~~~~~
zaplin out=cleaned colout=fudge.dat
Assuming the current value of Parameter MODE is "Cursor", this will
copy the NDF associated with the last DATA picture to an NDF called
"cleaned", interactively replacing areas using the current graphics
device. Linear interpolation is used to obtain the replacement values.
A record of the areas replaced will be stored in a text file named
"fudge.dat".
zaplin grubby cleaned i lincol=r columns="188,190" lines="15,16"
This replaces a region from pixel (188,15) to (190,16) within the NDF
called "grubby" and stores the result in the NDF called "cleaned". The
current co-ordinate Frame in the input NDF should be set to PIXEL
first (using WCSFRAME). The replacement is performed using linear
interpolation.
zaplin grubby(6,,) cleaned i lincol=r columns="188,190"
This replaces columns 188 to 190 in the 6th y-z plane region within
the NDF called "grubby" and stores the result in the NDF called
"cleaned". The current co-ordinate Frame in the input NDF should be
set to PIXEL first (using WCSFRAME). The replacement is performed
using linear interpolation.
zaplin m42 m42c f colin=aaoccd1.dat zaptype=b
This flags with bad values the regions in the NDF called "m42" defined
in the text file called "aaoccd1.dat", and stores the result in an NDF
called "m42c".
zaplin m42 m42c f colin=aaoccd1.dat noise
As above except that linear interpolation plus cosmetic noise are used
to replace the areas to be cleaned rather than bad pixels.



Notes
~~~~~


+ Bounds supplied in Interface and File mode are transformed into the
PIXEL Frame of the input NDF before being used.
+ Complicated results arise if the axes of the current Frame of the
input NDF are not parallel to the pixel axes. In these cases it is
usually better to switch to the PIXEL Frame (using WCSFRAME) prior to
using ZAPLIN. Roughly speaking, the range of pixel lines and/or
columns which are replaced will include any which intersect the
specified range on the current Frame axis.
+ When using input files care should be taken to ensure that the co-
ordinate system used in the file matches the current co-ordinate Frame
of the input NDF.
+ If the input NDF is a section of an NDF with a higher
  dimensionality, the "lines" and "columns" are with respect to the two-
  dimensional section, and do not necessarily refer to the first and
  second dimensions of the NDF as a whole. See the "Examples".




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDMASK, CHPIX, FILLBAD, GLITCH, NOMAGIC, REGIONMASK, SEGMENT,
SETMAGIC; Figaro: CSET, ICSET, NCSET, TIPPEX.


Copyright
~~~~~~~~~
Copyright (C) 1985-1993 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2000, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2010, 2012 Science & Facilities
Research Council. All Rights Reserved.


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
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




