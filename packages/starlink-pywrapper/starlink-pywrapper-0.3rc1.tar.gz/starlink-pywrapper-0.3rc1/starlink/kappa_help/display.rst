

DISPLAY
=======


Purpose
~~~~~~~
Displays a one- or two-dimensional NDF


Description
~~~~~~~~~~~
This application displays a one- or two-dimensional NDF as an image on
the current image-display device. The minimum and maximum data values
to be displayed can be selected in several ways (see Parameter MODE).
Data values outside these limits are displayed with the colour of the
nearest limit. A key showing the relationship between colour and data
value can be displayed (see Parameter KEY).
Annotated axes or a simple border can be drawn around the image (see
Parameters AXES and BORDER). The appearance of these may be controlled
in detail (see Parameters STYLE and BORSTYLE).
A specified colour lookup table may optionally be loaded prior to
displaying the image (see Parameter LUT). For devices which reset the
colour table when opened (such as postscript files), this may be the
only way of controlling the colour table.
The image is produced within the current graphics database picture.
The co-ordinates at the centre of the image, and the scale of the
image can be controlled using Parameters CENTRE, XMAGN and YMAGN. Only
the parts of the image that lie within the current picture are
visible; the rest is clipped. The image is padded with bad pixels if
necessary.


Usage
~~~~~


::

    
       display in [comp] clear [device] mode [centre] [xmagn] [ymagn]
          [out] { low=? high=?
                { percentiles=?
                { sigmas=?
                mode
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the image.
These display co-ordinates in the current co-ordinate Frame of the
supplied NDF, and may be changed using application WCSFRAME (see also
Parameter USEAXIS). The width of the margins left for the annotation
may be controlled using Parameter MARGIN. The appearance of the axes
(colours, founts, etc.) can be controlled using the STYLE parameter.
[current value]



BADCOL = LITERAL (Read)
```````````````````````
The colour with which to mark any bad (i.e. missing) pixels in the
display. There are a number of options described below.


+ "MAX" -- The maximum colour index used for the display of the image.
+ "MIN" -- The minimum colour index used for the display of the image.
+ An integer -- The actual colour index. It is constrained between 0
and the maximum colour index available on the device.
+ A named colour -- Uses the named colour from the palette, and if it
is not present, the nearest colour from the palette is selected.
+ An HTML colour code such as \#ff002d.

If the colour is to remain unaltered as the lookup table is
manipulated choose an integer between 0 and 15, or a named colour. The
suggested default is the current value. [current value]



BORDER = _LOGICAL (Read)
````````````````````````
TRUE if a border is to be drawn around the regions of the displayed
image containing valid co-ordinates in the current co-ordinate Frame
of the NDF. For instance, if the NDF contains an Aitoff all-sky map,
then an elliptical border will be drawn if the current co-ordinate
Frame is galactic longitude and latitude. This is because pixels
outside this ellipse have undefined positions in galactic co-
ordinates. If, instead, the current co-ordinate Frame had been pixel
co-ordinates, then a simple box would have been drawn containing the
whole image. This is because every pixel has a defined position in
pixel co-ordinates. The appearance of the border (colour, width, etc.)
can be controlled using Parameter BORSTYLE. [current value]



BORSTYLE = GROUP (Read)
```````````````````````
A group of attribute settings describing the plotting style to use for
the border (see Parameter BORDER).
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



CENTRE = LITERAL (Read)
```````````````````````
The co-ordinates of the data pixel to be placed at the centre of the
image, in the current co-ordinate Frame of the NDF (supplying a colon
":" will display details of the current co-ordinate Frame). The
position should be supplied as a list of formatted axis values
separated by spaces or commas. See also Parameter USEAXIS. A null (!)
value causes the centre of the image to be used. [!]



CLEAR = _LOGICAL (Read)
```````````````````````
TRUE if the current picture is to be cleared before the image is
displayed. [current value]



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be displayed. It may be "Data", "Quality",
"Variance", or "Error" (where "Error" is an alternative to "Variance"
and causes the square root of the variance values to be displayed). If
"Quality" is specified, then the quality values are treated as
numerical values (in the range 0 to 255). ["Data"]



DEVICE = DEVICE (Read)
``````````````````````
The name of the graphics device used to display the image. The device
must have at least 24 colour indices or greyscale intensities.
[current graphics device]



FILL = _LOGICAL (Read)
``````````````````````
If FILL is set to TRUE, then the image will be "stretched" to fill the
current picture in both directions. This can be useful when displaying
images with markedly different dimensions, such as two-dimensional
spectra. The dynamic default is TRUE if the array being displayed is
one-dimensional, and FALSE otherwise. []



HIGH = _DOUBLE (Read)
`````````````````````
The data value corresponding to the highest pen in the colour table.
All larger data values are set to the highest colour index when HIGH
is greater than LOW, otherwise all data values greater than HIGH are
set to the lowest colour index. The dynamic default is the maximum
data value. There is an efficiency gain when both LOW and HIGH are
given on the command line, because the extreme values need not be
computed. (Scale mode)



IN = NDF (Read)
```````````````
The input NDF structure containing the data to be displayed.



KEY = _LOGICAL (Read)
`````````````````````
TRUE if a key to the colour table is to be produced to the right of
the display. This can take the form of a colour ramp, a coloured
histogram of pen indices, or graphs of RGB intensities, all annotated
with data value. The form and appearance of this key can be controlled
using Parameter KEYSTYLE, and its horizontal position can be
controlled using Parameter KEYPOS. If the key is required in a
different location, set KEY=NO and use application LUTVIEW after
displaying the image. [TRUE]



KEYPOS( 2 ) = _REAL (Read)
``````````````````````````
The first element gives the gap between the right-hand edge of the
display and the left-hand edge of the key, as a fraction of the width
of the current picture. If a key is produced, then the right-hand
margin specified by Parameter MARGIN is ignored, and the value
supplied for KEYPOS is used instead. The second element gives the
vertical position of the key as a fractional value in the range zero
to one: zero puts the key as low as possible, one puts it as high as
possible. [current value]



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
Axis 1 is always the "data value" axis. So for instance, to set the
label for the data-value axis, assign a value to "Label(1)" in the
supplied style.
To get a ramp key (the default), specify "form=ramp". To get a
histogram key (a coloured histogram of pen indices), specify
"form=histogram". To get a graph key (three curves of RGB
intensities), specify "form=graph". If a histogram key is produced,
the population axis can be either logarithmic or linear. To get a
logarithmic population axis, specify "logpop=1". To get a linear
population axis, specify "logpop=0" (the default). To annotate the
long axis with pen numbers instead of pixel value, specify "pennums=1"
(the default, "pennums=0", shows pixel values). [current value]



LOW = _DOUBLE (Read)
````````````````````
The data value corresponding to the lowest pen in the colour table.
All smaller data values are set to the lowest colour index when LOW is
less than HIGH, otherwise all data values smaller than LOW are set to
the highest colour index. The dynamic default is the minimum data
value. There is an efficiency gain when both LOW and HIGH are given on
the command line, because the extreme values need not be computed.
(Scale mode)



LUT = NDF (Read)
````````````````
Name of the NDF containing a colour lookup table in its Data array;
the lookup table is written to the image-display's colour table. The
purpose of this parameter is to provide a means of controlling the
appearance of the image on certain devices, such as colour printers,
that do not have a dynamic colour table (i.e. the colour table is
reset when the device is opened). If used with dynamic devices (such
as X-windows), the new colour table remains after this application has
completed. A null value (! ) causes the existing colour table to be
used.
The LUT must be two-dimensional, the dimension of the first axis being
3, and the second being arbitrary. The method used to compress or
expand the colour table if the second dimension is different from the
number of unreserved colour indices is controlled by Parameter NN.
Also the LUT's values must lie in the range 0.0--1.0. [!]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave around the image for axis
annotations, given as fractions of the corresponding dimension of the
current picture. The actual margins used may be increased to preserve
the aspect ratio of the data. Four values may be given, in the order:
bottom, right, top, left. If fewer than four values are given, extra
values are used equal to the first supplied value. If these margins
are too narrow any axis annotation may be clipped. If a null (!) value
is supplied, the value used is (for all edges); 0.15 if annotated axes
are being produced; 0.04, if a simple border is being produced; and
0.0 if neither border nor axes are being produced. [current value]



MODE = LITERAL (Read)
`````````````````````
The method by which the maximum and minimum data values to be
displayed are chosen. The options are as follows.


+ "Current" -- The image is scaled between the upper and lower limits
that were used by the previous invocation of DISPLAY. If the previous
scaling limits cannot be determined, the MODE value reverts to
"Scale".
+ "Faint" -- The image is scaled between the mean data value minus one
standard deviation and the mean data value plus seven standard
deviations. The scaling values are reported so that the faster Scale
mode may be utilised later.
+ "Flash" -- The image is flashed onto the screen without any scaling
at all. This is the fastest option.
+ "Percentiles" -- The image is scaled between the data values
corresponding to two percentiles. The scaling values are reported so
that the faster Scale mode may be used later.
+ "Range" -- The image is scaled between the minimum and maximum data
values.
+ "Scale" -- You define the upper and lower limits between which the
image is to be scaled. The application reports the maximum and the
minimum data values for reference and makes these the suggested
defaults.
+ "Sigmas" -- The image is scaled between two standard-deviation
  limits. The scaling values used are reported so that the faster Scale
  mode may be utilised later.





NN = _LOGICAL (Read)
````````````````````
If TRUE the input lookup table is mapped to the colour table by using
the nearest-neighbour method. This preserves sharp edges and is better
for lookup tables with blocks of colour. If NN is FALSE linear
interpolation is used, and this is suitable for smoothly varying
colour tables. NN is ignored unless LUT is not null. [FALSE]



NUMBIN = _INTEGER (Read)
````````````````````````
The number of histogram bins used to compute percentiles for scaling.
(Percentiles mode) [2048]



OUT = NDF (Write)
`````````````````
A scaled copy of the displayed section of the image. Values in this
output image are integer colour indices shifted to exclude the indices
reserved for the palette (i.e. the value zero refers to the first
colour index following the palette). The output NDF is intended to be
used as the input data in conjunction with SCALE=FALSE. If a null
value (!) is supplied, no output NDF will be created. This parameter
is not accessed when SCALE=FALSE. [!]



PENRANGE( 2 ) = _REAL (Read)
````````````````````````````
The range of colour indices ("pens") to use. The supplied values are
fractional values where zero corresponds to the lowest available
colour index and 1.0 corresponds to the highest available colour
index. The default value of [0.0,1.0] thus causes the full range of
colour indicies to be used. Note, if parameter LUT is null (!) or
parameter SCALE is FALSE then this parameter is ignored and the fill
range of pens is used. [0.0,1.0]



PERCENTILES( 2 ) = _REAL (Read)
```````````````````````````````
The percentiles that define the scaling limits. For example, [25,75]
would scale between the quartile values. (Percentile mode)



SCAHIGH = _DOUBLE (Write)
`````````````````````````
On exit, this holds the data value which corresponds to the maximum
colour index in the displayed image. In Flash mode or when there is no
scaling the highest colour index is returned.



SCALE = _LOGICAL (Read)
```````````````````````
If TRUE the input data are to be scaled according to the value of
Parameter MODE. If it is FALSE, MODE is ignored, and the input data
are displayed as is (i.e. the data values are simply converted to
integer type and used as indices into the colour table). A value of
zero refers to the first pen following the palette. A FALSE value is
intended to be used with data previously scaled by this or similar
applications which have already performed the required scaling (see
Parameter OUT). It provides the quickest method of image display
within this application. [TRUE]



SCALOW = _DOUBLE (Write)
````````````````````````
The data value scaled to the minimum colour index for display. In
Flash mode or when there is no scaling the lowest colour index is
used. The current display linear-scaling minimum is set to this value.



SIGMAS( 2 ) = _REAL (Read)
``````````````````````````
The standard-deviation bounds that define the scaling limits. To
obtain values either side of the mean both a negative and a positive
value are required. Thus [-2,3] would scale between the mean minus two
and the mean plus three standard deviations. [3,-2] would give the
negative of that.



SQRPIX = _LOGICAL (Read)
````````````````````````
If TRUE then the default value for YMAGN equals the value supplied for
XMAGN, resulting in all pixels being displayed as squares on the
display surface. If a FALSE value is supplied for SQRPIX, then the
default value for YMAGN is chosen to retain the pixels original aspect
ratio at the centre of the image. [current value]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the annotated axes (see Parameter AXES).
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



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of two strings should be supplied
specifying the two axes which are to be used when annotating the
image, and when supplying a value for Parameter CENTRE. Each axis can
be specified using one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the two used pixel axes within the NDF are used. [!]



XMAGN = _REAL (Read)
````````````````````
The horizontal magnification for the image. The default value of 1.0
corresponds to 'normal' magnification in which the the image fills the
available space in at least one dimension. A value larger than 1.0
makes each data pixel wider. If this results in the image being wider
than the available space then the image will be clipped to display
fewer pixels. See also Parameters YMAGN, CENTRE, SQRPIX, and FILL.
[1.0]



YMAGN = _REAL (Read)
````````````````````
The vertical magnification for the image. A value of 1.0 corresponds
to 'normal' magnification in which the image fills the available space
in at least one dimension. A value larger than 1.0 makes each data
pixel taller. If this results in the image being taller than the
available space then the image will be clipped to display fewer
pixels. See also Parameters XMAGN, CENTRE, and FILL. If a null (!)
value is supplied, the default value used depends on Parameter SQRPIX.
If SQRPIX is TRUE, the default YMAGN value used is the value supplied
for XMAGN. This will result in each pixel occupying a square area on
the screen. If SQRPIX is FALSE, then the default value for YMAGN is
chosen so that each pixel occupies a rectangular area on the screen
matching the pixel aspect ratio at the centre of the image, determined
within the current WCS Frame. [!]



Examples
~~~~~~~~
display ngc6872 mode=p percentiles=[10,90] noaxes
Displays the NDF called ngc6872 on the current graphics device. The
scaling is between the 10 and 90 per cent percentiles of the image. No
annotated axes are produced.
display vv256 mode=flash noaxes border
borstyle="colour=blue,style=2" Displays the NDF called vv256 on the
current graphics device. There is no scaling of the data; instead the
modulus of each pixel with respect to the number of colour-table
indices is shown. No annotated axes are drawn, but a blue border is
drawn around the image using PGPLOT line style number 2 (i.e. dashed
lines).
display mode=fa axes style="^sty,grid=1" margin=0.2 clear
out=video \ Displays the current NDF DATA component with annotated
axes after clearing the current picture on the current graphics
device. The appearance of the axes is specified in the text file sty,
but this is modified by setting the Grid attribute to 1 so that a co-
ordinate grid is drawn across the plot. The margins around the image
containing the axes are made slightly wider than normal. The scaling
is between the -1 and +7 standard deviations of the image around its
mean. The scaled data are stored in an NDF called video.
display video noscale \
Displays the DATA component of the NDF called video (created in the
previous example) without scaling within the current picture on the
current graphics device.
display in=cgs4a comp=v mode=sc low=1 high=5.2 device=xwindows
Displays the VARIANCE component of NDF cgs4a on the xwindows device,
scaling between 1 and 5.2.
display mydata centre="12:23:34 -22:12:23" xmagn=2 badcol="red" \
Displays the NDF called mydata centred on the position RA=12:23:34,
DEC=-22:12:23. This assumes that the current co-ordinate Frame in the
NDF is an equatorial (RA/DEC) Frame. The image is displayed with a
magnification of 2 so that each data pixel appears twice as large (on
each axis) as normal. Fewer data pixels may be displayed to ensure the
image fits within the available space in the current picture. The
current scaling is used, and bad pixels are shown in red.
display ngc6872 mode=ra device=lj250 lut=pizza
Displays the NDF called ngc6872 on the LJ250 device. The lookup table
in the NDF called pizza is mapped on the LJ250's colour table. The
scaling is between the minimum and maximum of the image.



Notes
~~~~~


+ For large images the resolution of the graphics device may allow
only a fraction of the detail in the data to be plotted. Therefore,
large images will be compressed by block averaging when this can be
done without loss of resolution in the displayed image. This saves
time scaling the data and transmitting them to the image display. Note
that the default values for Parameters LOW and HIGH are the minimum
and maximum values in the compressed floating-point data.
+ If no Title is specified via the STYLE parameter, then the TITLE
component in the NDF is used as the default title for the annotated
axes. If the NDF does not have a TITLE component, then the default
title is taken from current co-ordinate Frame in the NDF. If this has
not been set explicitly, then the name of the NDF is used as the
default title.
+ The application stores a number of pictures in the graphics database
in the following order: a FRAME picture containing the annotated axes,
the image area, and the border; a DATA picture containing just the
image area. Note, the FRAME picture is only created if annotated axes
or a border have been drawn, or if non-zero margins were specified
using Parameter MARGIN. The world co-ordinates in the DATA picture
will be pixel co-ordinates. A reference to the supplied NDF, together
with a copy of the WCS information in the NDF are stored in the DATA
picture. On exit the current database picture for the chosen device
reverts to the input picture.
+ The data type of the output NDF depends on the number of colour
  indices: _UBYTE for no more than 256, _UWORD for 257 to 65535, and
  _INTEGER otherwise. The output NDF will not contain any extensions,
  UNITS, QUALITY, and VARIANCE; but LABEL, TITLE, WCS and AXIS
  information are propagated from the input NDF. The output NDF does not
  become the new current data array. It is a Simple NDF (because the
  bad-pixel flag is set to false in order to access the maximum colour
  index, and to handle sections), therefore only NDF-compliant
  applications can process it.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSFRAME, PICDEF; Figaro: IGREY, IMAGE; SPECDRE: MOVIE.


Copyright
~~~~~~~~~
Copyright (C) 1990-1992 Science & Engineering Research Council.
Copyright (C) 1995, 1997-1999, 2001, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2007, 2009, 2010, 2012 Science &
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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, WCS and UNITS components of the input NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ This application will handle data in all numeric types, though type
  conversion to integer will occur for unsigned byte and word images.
  However, when there is no scaling only integer data will not be type
  converted, but this is not expensive for the expected byte-type data.




