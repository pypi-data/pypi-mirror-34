

DRAWNORTH
=========


Purpose
~~~~~~~
Draws arrows parallel to the axes


Description
~~~~~~~~~~~
This application draws a pair of arrows on top of a previously
displayed DATA picture which indicate the directions of the labelled
axes in the underlying picture, at the position specified by Parameter
ORIGIN. For instance, if the underlying picture has axes labelled with
celestial co-ordinates, then the arrows will by default indicate the
directions of north and east. The appearance of the arrows, including
the labels attached to each arrow, may be controlled using the STYLE
parameter. The picture area behind the arrows may optionally be
cleared before drawing the arrows (see Parameter BLANK).


Usage
~~~~~


::

    
       drawnorth [device] [length] [origin]
       



ADAM parameters
~~~~~~~~~~~~~~~



ARROW = _REAL (Read)
````````````````````
The size of the arrow heads are specified by this parameter. Simple
lines can be drawn by setting the arrow head size to zero. The value
should be expressed as a fraction of the largest dimension of the
underlying DATA picture. [current value]



BLANK = _LOGICAL (Read)
```````````````````````
If TRUE, then the area behind the arrows is blanked before the arrows
are drawn. This is done by drawing a rectangle filled with the current
background colour of the selected graphics device. The size of the
blanked area can be controlled using Parameter BLANKSIZE. [FALSE]



BLANKSIZE = _REAL (Read)
````````````````````````
Specifies the size of the blanked area (see Parameter BLANK). A value
of 1.0 results in the blanked area being just large enough to contain
the drawn arrows and labels. Values larger than 1.0 introduce a blank
margin around the drawn arrows and labels. This parameter also
specifies the size of the picture stored in the graphics database.
[1.05]



DEVICE = DEVICE (Read)
``````````````````````
The plotting device. [Current graphics device]



EPOCH = _DOUBLE (Read)
``````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
Parameter FRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



FRAME = LITERAL (Read)
``````````````````````
Specifies the co-ordinate Frame to which the drawn arrows refer. If a
null (!) value is supplied, the arrows are drawn parallel to the two
axes which were used to annotate the previously displayed picture. If
the arrows are required to be parallel to the axes of some other
Frame, the required Frame should be specified using this parameter.
The string supplied for FRAME can be one of the following options.


+ A domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).

An error will be reported if a co-ordinate Frame is requested which is
not available in the previously displayed picture. If the selected
Frame has more than two axes, the Parameter USEAXIS will determine the
two axes which are to be used. [!]



LENGTH( 2 ) = _REAL (Read)
``````````````````````````
The lengths of the arrows, expressed as fractions of the largest
dimension of the underlying DATA picture. If only one value is
supplied, both arrows will be drawn with the given length. One of the
supplied values can be set to zero if only a single arrow is required.
[current value]



OFRAME = LITERAL (Read)
```````````````````````
Specifies the co-ordinate Frame in which the position of the arrows
will be supplied (see Parameter ORIGIN). The following Frames will
always be available.


+ "GRAPHICS" -- gives positions in millimetres from the bottom-left
corner of the plotting surface.
+ "BASEPIC" -- gives positions in a normalised system in which the
bottom-left corner of the plotting surface is (0,0) and the shortest
dimension of the plotting surface has length 1.0. The scales on the
two axes are equal.
+ "CURPIC" -- gives positions in a normalised system in which the
bottom-left corner of the underlying DATA picture is (0,0) and the
shortest dimension of the picture has length 1.0. The scales on the
two axes are equal.
+ "NDC" -- gives positions in a normalised system in which the bottom-
left corner of the plotting surface is (0,0) and the top-right corner
is (1,1).
+ "CURNDC" -- gives positions in a normalised system in which the
  bottom-left corner of the underlying DATA picture is (0,0) and the
  top-right corner is (1,1).

Additional Frames will be available, describing the co-ordinates
systems known to the data displayed within the underlying picture.
These could include PIXEL, AXIS, SKY, for instance, but the exact list
will depend on the displayed data. If a null value is supplied, the
ORIGIN position should be supplied in the Frame used to annotate the
underlying picture (supplying a colon ":" will display details of this
co-ordinate Frame). ["CURNDC"]



ORIGIN = LITERAL (Read)
```````````````````````
The co-ordinates at which to place the origin of the arrows, in the
Frame specified by Parameter OFRAME. If a null (!) value is supplied,
OFRAME is ignored and the arrows are situated at a default position
near one of the corners, or at the centre. The supplied position can
be anywhere within the current picture. An error is reported if the
arrows and labels cannot be drawn at any of these positions. [!]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the vectors and annotated axes.
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
The appearance of the arrows is controlled by the attributes
Colour(Axes), Width(Axes), etc. (the synonym Arrows may be used in
place of Axes).
The text of the label to draw against each arrow is specified by the
Symbol(1) and Symbol(2) attributes. These default to that
corresponding attributes of the underlying picture. The appearance of
these labels can be controlled using the attributes Font(TextLab),
Size(TextLab), etc. The gap between the end of the arrow and the
corresponding label can be controlled using attribute TextLabGap. The
drawing of labels can be suppressed using attribute TextLab. [current
value]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the co-ordinate Frame selected using
Parameter FRAME has more than two axes. A group of two strings should
be supplied specifying the two axes to which the two drawn arrows
should refer. Each axis can be specified using one of the following
options.


+ An integer index of an axis within the current Frame of the input
NDF (in the range 1 to the number of axes in the current Frame).
+ An axis symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the first two axes of the
Frame are used. [!]



Examples
~~~~~~~~
drawnorth
Draws a pair of arrows indicating the directions of the axes of the
previously displayed image, contour map, etc. The arrows are drawn at
the top left of the picture. The current values for all other
parameters are used.
drawnorth blank origin="0.5,0.5" style='TextBackColour=clear'
As above, but blanks out the picture area behind the arrows, and
positions them in the middle of the underlying DATA picture. In
addition, the text labels are drawn with a clear background so that
the underlying image can seen around the text.
drawnorth blank blanksize=1.2 oframe=pixel origin="150,250"
As above, but positions the arrows at pixel co-ordinates (150,250),
and blanks out a larger area around the arrows.
drawnorth blank oframe=! origin="10:12:34,-12:23:37"
As above, but positions the arrows at RA=10:12:34 and DEC=-12:23:37
(this assumes the underlying picture was annotated with RA and DEC
axes).
drawnorth length=[0.1,0] style='colour(arrows)=red'
Draws the axis-1 arrow with length equal to 0.1 of the longest
dimension of the underlying picture, but does not draw the axis-2
arrow. Both arrows are drawn red.
drawnorth style='textlab=0'
Draws both arrows but does not draw any text labels.
drawnorth style="'Size(TextLab1)=2,Symbol(1)=A,Symbol(2)=B'"
Draws arrows with labels "A" and "B", using characters of twice the
default size for the label for the first axis.



Notes
~~~~~


+ An error is reported if there is no existing DATA picture within the
current picture on the selected graphics device.
+ The application stores a picture in the graphics database with name
  KEY which contains the two arrows. On exit the current database
  picture for the chosen device reverts to the input picture.




Copyright
~~~~~~~~~
Copyright (C) 2002, 2004 Central Laboratory of the Research Councils.
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


