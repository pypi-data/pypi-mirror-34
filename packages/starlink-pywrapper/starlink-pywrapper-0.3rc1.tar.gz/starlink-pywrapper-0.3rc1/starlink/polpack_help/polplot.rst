

POLPLOT
=======


Purpose
~~~~~~~
Plots a 2-dimensional vector map


Description
~~~~~~~~~~~
This application plots vectors defined by the values contained within
four columns in a catalogue. These columns give the magnitude and
orientation of each vector, and the position of each vector (see
parameters COLMAG, COLANG, COLX and COLY). If the catalogue has a
third axis (spectral channel for instance), then only vectors with a
specified value on the third axis will be plotted (see parameter
ZAXVAL).
The plot is produced within the current graphics database picture, and
may be aligned with an existing DATA picture if the existing picture
contains suitable co-ordinate Frame information (see parameter CLEAR).
Annotated axes can be produced (see parameter AXES), and the
appearance of the axes can be controlled in detail (see parameter
STYLE). The axes show co-ordinates in the co-ordinate Frame specified
by parameter FRAME.
A key to the vector scale can be displayed to the right of the vector
map (see parameter KEY). The appearance and position of this key may
be controlled using parameters KEYSTYLE and KEYPOS.


Usage
~~~~~


::

    
       polplot cat colx coly colmag colang [vscale] [arrow] [just] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



ANGROT = _REAL (Read)
`````````````````````
A rotation angle in degrees to be added to each vector orientation
before plotting the vectors (see parameters COLANG and NEGATE). It
should be the range 0-360. Note, this parameter is named ANGROT for
historical reasons, and its use should not be confused with the ANGROT
extension item (see POLIMP) which gives the orientation of the
reference direction. [0.0]



ARROW = LITERAL (Read)
``````````````````````
Vectors are drawn as arrows, with the size of the arrow head specified
by this parameter. Simple lines can be drawn by setting the arrow head
size to zero. The value should be expressed as a fraction of the
largest dimension of the vector map. [0.0]



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the vector
map, showing the coordinate Frame specified by parameter FRAME. The
appearance of the axes can be controlled using the STYLE parameter.
[TRUE]



CAT = LITERAL (Read)
````````````````````
The name of the input catalogue. This may be in any format supported
by the CAT library (see SUN/181). A file type of .FIT is assumed if no
file type is supplied.



CLEAR = _LOGICAL (Read)
```````````````````````
TRUE if the graphics device is to be cleared before displaying the
vector map. If you want the vector map to be drawn over the top of an
existing DATA picture, then set CLEAR to FALSE. The vector map will
then be drawn in alignment with the displayed data. If possible,
alignment occurs within the co-ordinate Frame specified by parameter
FRAME. If this is not possible, (for instance if suitable WCS
information was not stored with the existing DATA picture), then
alignment is attempted in PIXEL co-ordinates. If this is not possible,
then alignment is attempted in GRID co-ordinates. If this is not
possible, then alignment is attempted in the first suitable Frame
found in the catalogue irrespective of its domain. A message is
displayed indicating the domain in which alignment occurred. If there
are no suitable Frames in the catalogue then an error is reported.
[TRUE]



COLANG = LITERAL (Read)
```````````````````````
The name of the catalogue column holding the orientation of each
vector. The values are considered to be in units of degrees unless the
UNITS attribute of the column has the value "Radians" (case
insensitive). The angles are assumed to be measured anti-clockwise
from the reference direction specified in the catalogue. A list of
available column names is displayed if a non-existent column name is
given. See also parameter NEGATE. [ANG]



COLMAG = LITERAL (Read)
```````````````````````
The name of the catalogue column holding the magnitude of each vector.
A list of available column names is displayed if a non-existent column
name is given. [P]



COLX = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the position of each
vector along the first axis. A list of available column names is
displayed if a non-existent column name is given. See the "Notes"
section below for further details of how these positions are
interpreted. [X]



COLY = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the position of each
vector along the second axis. A list of available column names is
displayed if a non-existent column name is given. See the "Notes"
section below for further details of how these positions are
interpreted. [Y]



COLZ = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the position of each
vector along a third axis. A list of available column names is
displayed if a non-existent column name is given. A null (!) value
should be supplied if no third axis is to be used. The dynamic default
is 'Z' if the catalogue contains a Z column, and null (!) otherwise.
See also parameter ZAXVAL. []



DEVICE = DEVICE (Read)
``````````````````````
The plotting device. [Current graphics device]



EPOCH = _DOUBLE (Read)
``````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



FILL = _LOGICAL (Read)
``````````````````````
The DATA picture containing the vector map is usually produced with
the same shape as the data. However, for maps with markedly different
dimensions this default behaviour may not give the clearest result.
When FILL is TRUE, the smaller dimension of the picture is expanded to
produce the largest possible picture within the current picture.
[FALSE]



FRAME = LITERAL (Read)
``````````````````````
This gives the co-ordinate Frame to be displayed along the annotated
axes (see parameter AXES). If a null parameter value is supplied, then
the current Frame in the supplied catalogue is used. The string can be
one of the following:

+ A domain name such as SKY, AXIS, PIXEL, etc. The two "pseudo-
domains" WORLD and DATA may be supplied and will be translated into
PIXEL and AXIS respectively, so long as the WCS FrameSet in the
catalogue does not contain Frames with these domains.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95). [!]





JUST = LITERAL (Read)
`````````````````````
The justification for each vector; it can take any of the following
values:

+ CENTRE -- the vectors are drawn centred on the corresponding pixel
coordinates.
+ START -- the vectors are drawn starting at the corresponding pixel
coordinates.
+ END -- the vectors are drawn ending at the corresponding pixel
  coordinates. ["Centre"]





KEY = _LOGICAL (Read)
`````````````````````
TRUE if a key indicating the vector scale is to be produced. [TRUE]



KEYPOS() = _REAL (Read)
```````````````````````
Two values giving the position of the key. The first value gives the
gap between the right hand edge of the vector map and the left hand
edge of the key (0.0 for no gap, 1.0 for the largest gap). A positive
value will place the key to the right of (i.e. outside) the vector
map, and a negative value will place the key inside the vector map.
The second value gives the vertical position of the top of the key
(1.0 for the highest position, 0.0 for the lowest). If the second
value is not given, the top of the key is placed level with the top of
the vector map. Both values should be in the range 0.0 to 1.0. If a
key is produced, then the right hand margin specified by parameter
MARGIN is ignored. [current value]



KEYSTYLE = GROUP (Read)
```````````````````````
A group of attribute settings describing the plotting style to use for
the key (see parameter KEY).
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings over-riding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a plotting attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!) is supplied. See section "Plotting Attributes" in SUN/95 for
a description of the available attributes. Any unrecognised attributes
are ignored (no error is reported).
By default the key starts with two lines of text, the first being
"Vector scale:" and the second giving a numerical value for the scale
in units per centimetre. These two lines may be replaced by assigning
alternative text to the Title attribute using this parameter. If no
text is required, either assign a blank value for Title, or set the
DrawTitle attribute to zero.
The appearance of the text in the key is controlled using "String"
attributes (e.g. COLOUR(STRINGS), FONT(STRINGS), etc - the synonym
TEXT can be used in place of STRINGS). Note, the Size attribute
specifies the size of key text relative to the size of the numerical
labels on the vector map axes. Thus a value of 2.0 for Size will
result in text which is twice the size of the numerical axis labels.
The appearance of the example vector is controlled using "Curve"
attributes (e.g. COLOUR(CURVES), etc - the synonym VECTOR can be used
in place of CURVES). The numerical scale value is formatted as an axis
1 value (using attributes FORMAT(1), DIGITS(1), etc - the synonym
SCALE can be used in place of the value 1). The length of the example
vector is formatted as an axis 2 value (using attribute FORMAT(2), etc
- the synonym VECTOR can be used in place of the value 2). The
vertical space between lines in the key can be controlled using
attribute TextLabGap. A value of 1.0 is used if no value is set for
this attribute, and produces default vertical spacing. Values larger
than 1.0 increase the vertical space, and values less than 1.0
decrease the vertical space. If the key is drawn over the top of the
vector map, the key will ne opaque by default. The key can be made
transparent by including the setting "Colour(Back)=clear". [current
value]



KEYVEC = _REAL (Read)
`````````````````````
Length of the vector to be displayed in the key, in data units. A
default value is generated based on the spread of vector lengths in
the plot. []



LBND(2) = _REAL (Read)
``````````````````````
The coordinates to put at the lower left corner of the plotting area,
in the coordinates system specified by parameters COLX and COLY. If a
null value is supplied then an area is used which just encloses all
the data in the supplied catalogue. [!]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave around the vector map for axis
annotation. The widths should be given as fractions of the
corresponding dimension of the current picture. The actual margins
used may be increased to preserve the aspect ratio of the DATA
picture. Four values may be given, in the order; bottom, right, top,
left. If fewer than four values are given, extra values are used equal
to the first supplied value. If these margins are too narrow any axis
annotation may be clipped. The dynamic default is 0.15 (for all edges)
if annotated axes are being produced, and zero otherwise. See also
parameter KEYPOS. []



NEGATE = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, then the angles giving the orientation of
the polarization (i.e. the values in the column specified by parameter
COLANG) are negated before adding on any value specified by parameter
ANGROT. [FALSE]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the contours and annotated axes.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings over-riding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a plotting attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!) is supplied. See section "Plotting Attributes" in SUN/95 for
a description of the available attributes. Any unrecognised attributes
are ignored (no error is reported).
The appearance of the vectors is controlled by the attributes
Colour(Curves), Width(Curves), etc (the synonym Vectors may be used in
place of Curves). [current value]



UBND(2) = _REAL (Read)
``````````````````````
The coordinates to put at the top right corner of the plotting area,
in the coordinates system specified by parameters COLX and COLY. If a
null value is supplied then an area is used which just encloses all
the data in the supplied catalogue. [!]



VSCALE = _REAL (Read)
`````````````````````
The scale to be used for the vectors. The supplied value should give
the data value corresponding to a vector length of one centimetre. []



ZAXVAL = LITERAL (Read)
```````````````````````
Specifies the Z axis value for the vectors to be displayed. The given
value should be in the current coordinate Frame of the supplied
catalogue (see parameter COLZ). For instance, if the current
coordinate Frame contains a calibrated wavelength axis, the value
should be given in the units specified in that frame (Angstroms,
nanometres, etc.). If the wavelength axis has not been calibrated, the
value will probably need to be supplied in units of pixels. Entering a
colon (":") for the parameter will result in a description of the
current coordinate Frame being shown. This may help to determine the
units in which a value is expected. The value actually used is the
closest available value within the catalogue. This value is displayed
on the screen and included in the default plot title. The ZAXVAL
parameter is only accessed if a null (!) value is supplied for
parameter ZCOLVAL. See also parameter COLZ.



ZCOLVAL = _REAL (Read)
``````````````````````
Specifies the Z column value for the vectors to be displayed. The
given value should be in the same coordinate system as the values
stored in the Z column of the catalogue (usually pixels). This
parameter provides an alternative to the ZAXVAL parameter. Use the
ZCOLVAL parameter to specify the Z value in pixels, and the ZAXVAL
parameter to specify the Z value in Hertz, angstroms, nanometres, etc
(if the Z axis has been calibrated). If a null value is supplied for
ZCOLVAL, then ZAXVAL is used to determine the Z value to display. [!]



Examples
~~~~~~~~
polplot poltab
Produces a vector map on the current graphics device with vectors
defined in the FITS binary table "poltab". The magnitudes are taken
from column P, the orientations from column ANG and the coordinates of
each vector from columns X and Y.
polplot poltab style=^mystyle.dat
As above, but the annotated axes and vectors are drawn according to
the description given in text file mystyle.dat. If this files contains
the following lines:
title = My favorite colours grid = 1 minticklen = 0 colour(border) =
green colour(grid) = blue colour(vec) = red width(border) = 0.05
then the title is set to "My favourite colours"; a grid is drawn
across the plot instead of tick marks around the edge; the border,
grid and vectors are drawn in green, blue and red respectively, and
slightly thicker lines are used to draw the border.
polplot poltab ra dec noclear angrot=90 frame=eq(B1950)
Produces a vector map in which each vector is rotated by 90



Notes
~~~~~


+ The TITLE parameter in the supplied catalogue is used as the default
title for the annotated axes. If the catalogue does not have a TITLE
parameter (of it is blank), then the default title is taken from
current co-ordinate Frame stored in the WCS component of the
catalogue. This default may be over-ridden by specifying a value for
the Title attribute using the STYLE parameter.
+ The columns specified by parameters COLX and COLY should hold
  coordinates in the "Base Frame" of the WCS information stored as an
  AST FrameSet (see SUN/210) in the supplied catalogue. If the catalogue
  has been produced by one of the POLPACK application polvec or polbin,
  then the Base Frame will be pixel co-ordinates within the aligned
  intensity images, and these will be stored in columns with names "X"
  and "Y". If the catalogue was not created by POLPACK, it may have no
  usable WCS information, in which case the supplied positions are
  mapped linearly onto the screen. There is one exception to this; if
  the columns have names RA and DEC then they are assumed to be
  equatorial sky coordinates with epoch and equinox specified by the
  optional catalogue parameters EPOCH and EQUINOX (defaults are used for
  these parameters if they are not present in the catalogue). If the
  vector map is displayed over an existing DATA picture (i.e. if
  CLEAR=NO) then these RA/DEC positions will be aligned with the
  existing DATA picture if possible (i.e. if the existing picture has
  sky coordinate information stored with it).




