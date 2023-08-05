

CONTOUR
=======


Purpose
~~~~~~~
Contours a 2-d NDF


Description
~~~~~~~~~~~
This application produces a contour map of a two-dimensional NDF on
the current graphics device, with single-pixel resolution. Contour
levels can be chosen automatically in various ways, or specified
explicitly (see Parameter MODE). In addition, this application can
also draw an outline around either the whole data array, or around the
good pixels in the data array (set MODE to "Bounds" or "Good").
The plot is produced within the current graphics database picture, and
may be aligned with an existing DATA picture if the existing picture
contains suitable co-ordinate Frame information (see Parameter CLEAR).
The appearance of each contour can be controlled in several ways. The
pens used can be rotated automatically (see Parameter PENROT).
Contours below a given threshold value can be drawn dashed (see
Parameter DASHED). Alternatively, the appearance of each contour can
be set explicitly (see Parameter PENS).
Annotated axes can be produced (see Parameter AXES), and the
appearance of the axes can be controlled in detail (see Parameter
STYLE). The axes show co-ordinates in the current co-ordinate Frame of
the supplied NDF.
A list of the contour levels can be displayed to the right of the
contour map (see Parameter KEY). The appearance and position of this
key may be controlled using Parameters KEYSTYLE and KEYPOS.


Usage
~~~~~


::

    
       contour ndf [comp] mode ncont [key] [device]
         { firstcnt=? stepcnt=?
         { heights=?
         { percentiles=?
         mode
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the contour
map, showing the current co-ordinate Frame of the supplied NDF. The
appearance of the axes can be controlled using the STYLE parameter. If
a null (!) value is supplied, then axes will be drawn unless the CLEAR
parameter indicates that the graphics device is not being cleared. [!]



CLEAR = _LOGICAL (Read)
```````````````````````
TRUE if the graphics device is to be cleared before displaying the
contour map. If you want the contour map to be drawn over the top of
an existing DATA picture, then set CLEAR to FALSE. The contour map
will then be drawn in alignment with the displayed data. If possible,
alignment occurs within the current co-ordinate Frame of the NDF. If
this is not possible, (for instance if suitable WCS information was
not stored with the existing DATA picture), then alignment is
attempted in PIXEL co-ordinates. If this is not possible, then
alignment is attempted in GRID co-ordinates. If this is not possible,
then alignment is attempted in the first suitable Frame found in the
NDF irrespective of its domain. A message is displayed indicating the
domain in which alignment occurred. If there are no suitable Frames in
the NDF then an error is reported. [TRUE]



COMP = LITERAL (Read)
`````````````````````
The NDF component to be contoured. It may be "Data", "Quality",
"Variance", or "Error" (where "Error" is an alternative to "Variance"
and causes the square root of the variance values to be displayed). If
"Quality" is specified, then the quality values are treated as
numerical values (in the range 0 to 255). ["Data"]



DASHED = _REAL (Read)
`````````````````````
The height below which the contours will be drawn with dashed lines
(if possible). A null value (!) results in contours being drawn with
the styles specified by Parameters PENS, PENROT, and STYLE. [!]



DEVICE = DEVICE (Read)
``````````````````````
The plotting device. [current image-display device]



FAST = _LOGICAL (Read)
``````````````````````
If TRUE, then a faster, but in certain cases less-accurate, method is
used to draw the contours. In fast mode, contours may be incorrectly
placed on the display if the mapping between graphics co-ordinates and
the current co-ordinate Frame of the supplied NDF has any
discontinuities, or is strongly non-linear. This may be the case, for
instance, when displaying all-sky maps on top of each other. [TRUE]



FILL = _LOGICAL (Read)
``````````````````````
The contour plot normally has square pixels, in other words a
specified length along each axis corresponds to the same number of
pixels. However, for images with markedly different dimensions this
default behaviour may not be suitable or give the clearest plot. When
FILL is TRUE, the square-pixel constraint is relaxed and the contour
plot is the largest possible within the current picture. When FILL is
FALSE, the pixels are square. [FALSE]



FIRSTCNT = _REAL (Read)
```````````````````````
Height of the first contour (Linear and Magnitude modes).



HEIGHTS() = _REAL (Read)
````````````````````````
The required contour levels (Free mode).



KEY = _LOGICAL (Read)
`````````````````````
TRUE if a key of the contour level versus pixel value is to be
produced. The appearance of this key can be controlled using Parameter
KEYSTYLE, and its position can be controlled using Parameter KEYPOS.
[TRUE]



KEYPOS() = _REAL (Read)
```````````````````````
Two values giving the position of the key. The first value gives the
gap between the right-hand edge of the contour map and the left-hand
edge of the key (0.0 for no gap, 1.0 for the largest gap). The second
value gives the vertical position of the top of the key (1.0 for the
highest position, 0.0 for the lowest). If the second value is not
given, the top of the key is placed level with the top of the contour
map. Both values should be in the range 0.0 to 1.0. If a key is
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
The heading in the key can be changed by setting a value for the Title
attribute (the supplied heading is split into lines of no more than 17
characters). The appearance of the heading is controlled by attributes
Colour(Title), Font(Title), etc. The appearance of the contour indices
is controlled by attributes Colour(TextLab), Font(TextLab), etc. (the
synonym Index can be used in place of TextLab). The appearance of the
contour values is controlled by attributes Colour(NumLab),
Font(NumLab), etc (the synonym Value can be used in place of NumLab).
Contour indices are formatted using attributes Format(1), Digits(1),
etc. (the synonym Index can be used in place of value 1). Contour
values are formatted using attributes Format(2), etc. (the synonym
Value can be used in place of the value 2). [current value]



LABPOS() = _REAL (Read)
```````````````````````
Only used if Parameter MODE is set to "Good" or "Bounds". It specifies
the position at which to place a label identifying the input NDF
within the plot. The label is drawn parallel to the first pixel axis.
Two values should be supplied for LABPOS. The first value specifies
the distance in millimetres along the first pixel axis from the centre
of the bottom-left pixel to the left edge of the label. The second
value specifies the distance in millimetres along the second pixel
axis from the centre of the bottom-left pixel to the baseline of the
label. If a null (!) value is given, no label is produced. The
appearance of the label can be set by using the STYLE parameter (for
instance "Size(strings)=2"). [!]



LASTCNT = _REAL (Read)
``````````````````````
Height of the last contour (Linear and Magnitude modes).



LENGTH() = _REAL (Write)
````````````````````````
On exit this holds the total length in pixels of the contours at each
selected height. These values are only computed when Parameter STATS
is TRUE.



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave around the contour map for axis
annotation. The widths should be given as fractions of the
corresponding dimension of the current picture. The actual margins
used may be increased to preserve the aspect ratio of the DATA
picture. Four values may be given, in the order: bottom, right, top,
left. If fewer than four values are given, extra values are used equal
to the first supplied value. If these margins are too narrow any axis
annotation may be clipped. If a null (!) value is supplied, the value
used is 0.15 (for all edges) if annotated axes are being produced, and
zero otherwise. See also Parameter KEYPOS. [current value]



MODE = LITERAL (Read)
`````````````````````
The method used to select the contour levels. The options are:


+ "Area" -- The contours enclose areas of the array for which the
equivalent radius increases by equal increments. You specify the
number of levels.
+ "Automatic" -- The contour levels are equally spaced between the
maximum and minimum pixel values in the array. You supply the number
of contour levels.
+ "Bounds" -- A single "contour" is drawn representing the bounds of
the input array. A label may also be added (see Parameter LABPOS).
+ "Equalised" -- You define the number of equally spaced percentiles.
+ "Free" -- You specify a series of contour values explicitly.
+ "Good" -- A single "contour" is drawn outlining the good pixel
values. A label may also be added (see Parameter LABPOS).
+ "Linear" -- You define the number of contours, the start contour
level and linear step between contours.
+ "Magnitude" -- You define the number of contours, the start contour
level and step between contours. The step size is in magnitudes so the
nth contour is dex(-0.4*(n-1)*step) times the start contour level.
+ "Percentiles" -- You specify a series of percentiles.
+ "Scale" -- The contour levels are equally spaced between two pixel
  values that you specify. You also supply the number of contour levels,
  which must be at least two.

If the contour map is aligned with an existing DATA picture (see
Parameter CLEAR), then only part of the supplied NDF may be displayed.
In this case, the choice of contour levels is based on the data within
a rectangular section of the input NDF enclosing the existing DATA
picture. Data values outside this section are ignored.



NCONT = _INTEGER (Read)
```````````````````````
The number of contours to draw (only required in certain modes). It
must be between 1 and 50. If the number is large, the plot may be
cluttered and take longer to produce. The initial suggested default of
6 gives reasonable results.



NDF = NDF (Read)
````````````````
NDF structure containing the 2-dimensional image to be contoured.



NUMBER() = _INTEGER (Write)
```````````````````````````
On exit this holds the number of closed contours at each selected
height. Contours are not closed if they intersect a bad pixel or the
edge of the image. These values are only computed when Parameter STATS
is TRUE.



PENROT = _LOGICAL (Read)
````````````````````````
If TRUE, the plotting pens are cycled through the contours to aid
identification of the contour heights. Only accessed if pen
definitions are not supplied using Parameter PENS. [FALSE]



PENS = GROUP (Read)
```````````````````
A group of strings, separated by semicolons, each of which specifies
the appearance of a pen to be used to draw a contour. The first string
in the group describes the pen to use for the first contour, the
second string describes the pen for the second contour, etc. If there
are fewer strings than contours, then the supplied pens are cycled
through again, starting at the beginning. Each string should be a
comma-separated list of plotting attributes to be used when drawing
the contour. For instance, the string "width=10.0,colour=red,style=2"
produces a thick, red, dashed contour. Attributes that are unspecified
in a string default to the values implied by Parameter STYLE. If a
null value (!) is given for PENS, then the pens implied by Parameters
PENROT, DASHED and STYLE are used. [!]



PERCENTILES() = _REAL (Read)
````````````````````````````
Contour levels given as percentiles. The values must lie between 0.0
and 100.0. (Percentiles mode).



STATS = _LOGICAL (Read)
```````````````````````
If TRUE, the LENGTH and NUMBER statistics are computed. [FALSE]



STEPCNT = _REAL (Read)
``````````````````````
Separation between contour levels, linear for Linear mode and in
magnitudes for Magnitude mode.



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the contours and annotated axes.
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
The appearance of the contours is controlled by the attributes
Colour(Curves), Width(Curves), etc (the synonym Contours may be used
in place of Curves). The contour appearance established in this way
may be modified using Parameters PENS, PENROT and DASHED. [current
value]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of two strings should be supplied
specifying the two axes which are to be used when annotating and
aligning the contour map. Each axis can be specified using one of the
following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the two significant NDF pixel axes are used. [!]



Examples
~~~~~~~~
contour myfile
Contours the data array in the NDF called myfile on the current
graphics device. All other settings are defaulted, so for example the
current mode for determining heights is used, and a key is plotted.
contour taurus1(100:199,150:269,4)
Contours a 2-dimensional section of the three-dimensional NDF called
taurus1 on the current graphics device. The section extends from pixel
(100,150,4) to pixel (199,269,4).
contour ngc6872 mode=au ncont=5 device=ps_l pens="style=1;style=2"
Contours the data array in the NDF called ngc6872 on the ps_l graphics
device. Five equally spaced contours between the maximum and minimum
data values are drawn, alternating between line styles 1 and 2 (solid
and dashed).
contour ndf=ngc6872 mode=au ncont=5 penrot style="^mysty,grid=1"
As above except that the current graphics device is used, pens are
cycled automatically, and the appearance of the axes is read from text
file mysty. The plotting attribute Grid is set explicitly to 1 to
ensure that a co-ordinate grid is drawn over the plot. The text file
mysty could, for instance, contain the two lines "Title=NGC6872 at 25
microns" and "grid=0". The Title setting gives the title to display at
the top of the axes. The Grid setting would normally prevent a co-
ordinate grid being drawn, but is overridden in this example by the
explicit setting for Grid which follows the file name.
contour m51 mode=li firstcnt=10 stepcnt=2 ncont=4 keystyle=^keysty
Contours the data array in the NDF called m51 on the current graphics
device. Four contours at heights 10, 12, 14, and 16 are drawn. A key
is plotted using the style specified in the text file keysty. This
file could, for instance, contain the two lines "font=3" and
"digits(2)=4" to cause all text in the key to be drawn using PGPLOT
font 3 (an italic font), and 4 digits to be used when formatting the
contour values.
contour ss443 mode=pe percentiles=[80,90,95] stats keypos=0.02
Contours the data array in the NDF called ss443 on the current
graphics device. Contours at heights corresponding to the 80, 90 and
95 percentiles are drawn. The key is placed closer to the contour map
than usual. Contour statistics are computed.
contour skyflux mode=eq ncont=5 dashed=0 pens='colour=red' noclear
Contours the data array in the NDF called skyflux on the current
graphics device. The contour map is automatically aligned with any
existing DATA picture, if possible. Contours at heights corresponding
to the 10, 30, 50, 70 and 90 percentiles (of the data within the
picture) are drawn in red. Those contours whose values are negative
will appear as dashed lines.
contour comp=d nokey penrot style="grid=1,title=My data" \
Contours the data array in the current NDF on the current graphics
device using the current method for height selection. No key is drawn.
The appearance of the contours cycles every third contour. A co-
ordinate grid is drawn over the plot, and a title of "My data" is
displayed at the top.
contour comp=v mode=fr heights=[10,20,40,80] \
Contours the variance array in the current NDF on the current graphics
device. Contours at 10, 20, 40 and 80 are drawn.



Notes
~~~~~


+ If no Title is specified via the STYLE parameter, then the Title
component in the NDF is used as the default title for the annotated
axes. If the NDF does not have a Title component, then the default
title is taken from current co-ordinate Frame in the NDF. If this has
not been set explicitly, then the name of the NDF is used as the
default title.
+ The application stores a number of pictures in the graphics database
  in the following order: a FRAME picture containing the annotated axes,
  contours, and key; a KEY picture to store the key if present; and a
  DATA picture containing just the contours. Note, the FRAME picture is
  only created if annotated axes or a key has been drawn, or if non-zero
  margins were specified using Parameter MARGIN. The world co-ordinates
  in the DATA picture will be pixel co-ordinates. A reference to the
  supplied NDF, together with a copy of the WCS information in the NDF
  are stored in the DATA picture. On exit the current database picture
  for the chosen device reverts to the input picture.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSFRAME, PICDEF; Figaro: ICONT; SPECDRE: SPECCONT.


Copyright
~~~~~~~~~
Copyright (C) 1988-1993 Science & Engineering Research Council.
Copyright (C) 1995, 1997-1999, 2001, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2010 Science & Technology Facilities
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


+ Only real data can be processed directly. Other non-complex numeric
data types will undergo a type conversion before the contour plot is
drawn.
+ Bad pixels and automatic quality masking are supported.




