

VECPLOT
=======


Purpose
~~~~~~~
Plots a two-dimensional vector map


Description
~~~~~~~~~~~
This application plots vectors defined by the values contained within
a pair of two-dimensional NDFs, the first holding the magnitude of the
vector quantity at each pixel, and the second holding the
corresponding vector orientations. It is assumed that the two NDFs are
aligned in pixel co-ordinates. The number of vectors in the plot is
kept to a manageable value by only plotting vectors for pixels on a
sparse regular matrix. The increment (in pixels) between plotted
vectors is given by Parameter STEP. Zero orientation may be fixed at
any position angle within the plot by specifying an appropriate value
for Parameter ANGROT. Each vector may be represented either by an
arrow or by a simple line, as selected by Parameter ARROW.
The plot is produced within the current graphics database picture, and
may be aligned with an existing DATA picture if the existing picture
contains suitable co-ordinate Frame information (see Parameter CLEAR).
Annotated axes can be produced (see Parameter AXES), and the
appearance of these can be controlled in detail using Parameter STYLE.
The axes show co-ordinates in the current co-ordinate Frame of NDF1.
A key to the vector scale can be displayed to the right of the vector
map (see Parameter KEY). The appearance and position of this key may
be controlled using Parameters KEYSTYLE and KEYPOS.


Usage
~~~~~


::

    
       vecplot ndf1 ndf2 [comp] [step] [vscale] [arrow] [just] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



ANGROT = _REAL (Read)
`````````````````````
A rotation angle in degrees to be added to each vector orientation
before plotting the vectors (see Parameter NDF2). It should be in the
range 0--360. [0.0]



ARROW = LITERAL (Read)
``````````````````````
Vectors are drawn as arrows, with the size of the arrow head specified
by this parameter. Simple lines can be drawn by setting the arrow head
size to zero. The value should be expressed as a fraction of the
largest dimension of the vector map. [current value]



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the vector
map. These display co-ordinates in the current co-ordinate Frame NDF1,
which may be changed using application WCSFRAME (see also Parameter
USEAXIS). The width of the margins left for the annotation may be
controlled using Parameter MARGIN. The appearance of the axes
(colours, founts, etc.) can be controlled using the STYLE parameter.
[TRUE]



CLEAR = _LOGICAL (Read)
```````````````````````
TRUE if the graphics device is to be cleared before displaying the
vector map. If you want the vector map to be drawn over the top of an
existing DATA picture, then set CLEAR to FALSE. The vector map will
then be drawn in alignment with the displayed data. If possible,
alignment occurs within the current co-ordinate Frame of the NDF. If
this is not possible (for instance, if suitable WCS information was
not stored with the existing DATA picture), then alignment is
attempted in PIXEL co-ordinates. If this is not possible, then
alignment is attempted in GRID co-ordinates. If this is not possible,
then alignment is attempted in the first suitable Frame found in the
NDF irrespective of its domain. A message is displayed indicating the
domain in which alignment occurred. If there are no suitable Frames in
the NDF then an error is reported. [TRUE]



COMP = LITERAL (Read)
`````````````````````
The component of NDF1 which is to be used to define the vector
magnitudes. It may be "Data", "Error" or "Variance". The last two are
not available if NDF1 does not contain a VARIANCE component. The
vector orientations are always defined by the "Data" component of
NDF2. ["Data"]



DEVICE = DEVICE (Read)
``````````````````````
The plotting device. [Current graphics device]



FILL = _LOGICAL (Read)
``````````````````````
The DATA picture containing the vector map is usually produced with
the same shape as the data. However, for maps with markedly different
dimensions this default behaviour may not give the clearest result.
When FILL is TRUE, the smaller dimension of the picture is expanded to
produce the largest possible picture within the current picture.
[FALSE]



JUST = LITERAL (Read)
`````````````````````
The justification for each vector; it can take any of the following
values:


+ "Centre" -- the vectors are drawn centred on the corresponding
pixel,
+ "Start" -- the vectors are drawn starting at the corresponding
pixel, and
+ "End" -- the vectors are drawn ending at the corresponding pixel.

["Centre"]



KEY = _LOGICAL (Read)
`````````````````````
TRUE if a key indicating the vector scale is to be produced. [TRUE]



KEYPOS() = _REAL (Read)
```````````````````````
Two values giving the position of the key. The first value gives the
gap between the right-hand edge of the vector map and the left-hand
edge of the key (0.0 for no gap, 1.0 for the largest gap). The second
value gives the vertical position of the top of the key (1.0 for the
highest position, 0.0 for the lowest). If the second value is not
given, the top of the key is placed level with the top of the vector
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
The appearance of the text in the key is controlled using "String"
attributes (e.g. Colour(Strings), Font(Strings), etc.; the synonym
TEXT can be used in place of Strings). Note, the Size attribute
specifies the size of key text relative to the size of the numerical
labels on the vector map axes. Thus a value of 2.0 for Size will
result in text which is twice the size of the numerical axis labels.
The appearance of the example vector is controlled using "Curve"
attributes (e.g. Colour(Curves), etc.; the synonym Vector can be used
in place of Curves). The numerical scale value is formatted as as
axis-1 value (using attributes Format(1), Digits(1), etc.; the synonym
Scale can be used in place of the value 1). The length of the example
vector is formatted as an axis-2 value (using attribute Format(2),
etc.; the synonym Vector can be used in place of the value 2). The
vertical space between lines in the key can be controlled using
attribute TextLabGap. A value of 1.0 is used if no value is set for
this attribute, and produces default vertical spacing. Values larger
than 1.0 increase the vertical space, and values less than 1.0
decrease the vertical space. [current value]



KEYVEC = _REAL (Read)
`````````````````````
Length of the vector to be displayed in the key, in data units. If a
null (!) value is supplied, the value used is generated on the basis
of the spread of vector lengths in the plot. [!]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave around the vector map for axis
annotation. The widths should be given as fractions of the
corresponding dimension of the current picture. The actual margins
used may be increased to preserve the aspect ratio of the DATA
picture. Four values may be given, in the order; bottom, right, top,
left. If fewer than four values are given, extra values are used equal
to the first supplied value. If these margins are too narrow any axis
annotation may be clipped. If a null (!) value is supplied, the value
used is 0.15 (for all edges) if annotated axes are being produced, and
zero otherwise. See also Parameter KEYPOS. [current value]



NDF1 = NDF (Read)
`````````````````
NDF structure containing the two-dimensional image giving the vector
magnitudes.



NDF2 = NDF (Read)
`````````````````
NDF structure containing the two-dimensional image giving the vector
orientations. The values are considered to be in units of degrees
unless the UNITS component of the NDF has the value "Radians" (case
insensitive). The positive y pixel axis defines zero orientation, and
rotation from the x pixel axis to the y pixel is considered positive.



STEP = _INTEGER (Read)
``````````````````````
The number of pixels between adjacent displayed vectors (along both
axes). Increasing this value reduces the number of displayed vectors.
If a null (!) value is supplied, the value used gives about thirty
vectors along the longest axis of the plot. [!]



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
The appearance of the vectors is controlled by the attributes
Colour(Curves), Width(Curves), etc. (the synonym Vectors may be used
in place of Curves). [current value]



VSCALE = _REAL (Read)
`````````````````````
The scale to be used for the vectors. The supplied value should give
the data value corresponding to a vector length of one centimetre. If
a null (!) value is supplied, a default value is used. [!]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of two strings should be supplied
specifying the two axes which are to be used when annotating and
aligning the vector map. Each axis can be specified using one of the
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
vecplot polint polang
Produces a vector map on the current graphics device with vector
magnitude taken from the NDF called polint and vector orientation
taken from NDF polang. All other settings are defaulted, so for
example about 20 vectors are displayed along the longest axis, and a
key is plotted.
vecplot polint polang angrot=23.4 clear=no
Produces a vector map in which the primary axis of the vectors (as
defined by the value zero in the NDF polang) is at the position angle
23.4 degrees (measured anti-clockwise from the positive y axis) in the
displayed map. The map is drawn over the top of the previously drawn
DATA picture, aligned in a suitable co-ordinate Frame.
vecplot stack(,,2) stack(,,1) arrow=0.1 just=start nokey
Produces a vector map in which the vectors are defined by two planes
in the 3-dimensional NDF called stack. There is no need to copy the
two planes into two separate NDFs before running VECPLOT. Each vector
is represented by an arrow, starting at the position of the
corresponding pixel. No key to the vector scale and justification is
produced.



Notes
~~~~~


+ If no Title is specified via the STYLE parameter, then the Title
component in NDF1 is used as the default title for the annotated axes.
If the NDF does not have a Title component, then the default title is
taken from current co-ordinate Frame in NDF1. If this has not been set
explicitly, then the name of NDF1 is used as the default title.
+ The application stores a number of pictures in the graphics database
  in the following order: a FRAME picture containing the annotated axes,
  vectors, and key; a KEY picture to store the key if present; and a
  DATA picture containing just the vectors. Note, the FRAME picture is
  only created if annotated axes or a key has been drawn, or if non-zero
  margins were specified using Parameter MARGIN. The world co-ordinates
  in the DATA picture will be pixel co-ordinates. A reference to NDF1,
  together with a copy of the WCS information in the NDF are stored in
  the DATA picture. On exit the current database picture for the chosen
  device reverts to the input picture.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CALPOL.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995, 1999, 2004 Central Laboratory of the Research Councils.
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


+ Only real data can be processed directly. Other non-complex numeric
data types will undergo a type conversion before the vector plot is
drawn.
+ Bad pixels and automatic quality masking are supported.




