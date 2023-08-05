

CURSOR
======


Purpose
~~~~~~~
Reports the co-ordinates of positions selected using the cursor


Description
~~~~~~~~~~~
This application reads co-ordinates from the chosen graphics device
using a cursor and displays them on your terminal. The selected
positions may be marked in various ways on the device (see parameter
PLOT), and can be written to an output positions list so that
subsequent applications can make use of them (see Parameter OUTCAT).
The format of the displayed positions may be controlled using
Parameter STYLE. The pixel data value in any associated NDF can also
be displayed (see Parameter SHOWDATA).
Positions may be reported in several different co-ordinate Frames (see
Parameter FRAME). Optionally, the corresponding pixel co-ordinates at
each position may also be reported (see Parameter SHOWPIXEL).
The picture or pictures within which positions are required can be
selected in several ways (see Parameters MODE and NAME).
Restrictions can be made on the number of positions to be given (see
Parameters MAXPOS and MINPOS), and screen output can be suppressed
(see the Notes).


Usage
~~~~~


::

    
       cursor [mode] [name] [outcat] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



CATFRAME = LITERAL (Read)
`````````````````````````
A string determining the co-ordinate Frame in which positions are to
be stored in the output catalogue associated with parameter OUTCAT.
The string supplied for CATFRAME can be one of the following:


+ A Domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame.
+ An IRAS90 Sky Co-ordinate System (SCS) values such as EQUAT(J2000)
  (see SUN/163).

If a null (!) value is supplied, the positions will be stored in the
current Frame. [!]



CATEPOCH = DOUBLE PRECISION (Read)
``````````````````````````````````
The epoch at which the sky positions stored in the output catalogue
were determined. It will only be accessed if an epoch value is needed
to qualify the co-ordinate Frame specified by COLFRAME. If required,
it should be given as a decimal years value, with or without decimal
places ("1996.8" for example). Such values are interpreted as a
Besselian epoch if less than 1984.0 and as a Julian epoch otherwise.



CLOSE = _LOGICAL (Read)
```````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Poly". If TRUE, polygons will be closed by joining the first position
to the last position. [current value]



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be displayed if Parameter SHOWDATA is set
TRUE.. It may be "Data", "Quality", "Variance", or "Error" (where
"Error" is an alternative to "Variance" and causes the square root of
the variance values to be displayed). If "Quality" is specified, then
the quality values are treated as numerical values (in the range 0 to
255). ["Data"]



DESCRIBE = _LOGICAL (Read)
``````````````````````````
If TRUE, a detailed description of the co-ordinate Frame in which
subsequent positions will be reported is produced each time a position
is reported within a new picture. [current value]



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation. This device must support cursor interaction.
[current graphics device]



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
A string determining the co-ordinate Frame in which positions are to
be reported. When a data array is displayed by an application such as
DISPLAY, CONTOUR, etc, WCS information describing the co-ordinate
systems known to the data array are stored with the DATA picture in
the graphics database. This application can report positions in any of
the co-ordinate Frames stored with each picture. The string supplied
for FRAME can be one of the following:


+ A domain name such as SKY, AXIS, PIXEL, etc. The special domains
AGI_WORLD and AGI_DATA are used to refer to the world and data co-
ordinate system stored in the AGI graphics database. They can be
useful if no WCS information was store with the picture when it was
created.
+ An integer value giving the index of the required Frame.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).

If a null value (!) is supplied, positions are reported in the co-
ordinate Frame which was current when the picture was created. [!]



GEODESIC = _LOGICAL (Read)
``````````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Poly". It specifies whether the curves drawn between positions should
be straight lines, or should be geodesic curves. In many co-ordinate
Frames geodesic curves will be simple straight lines. However, in
others (such as the majority of celestial co-ordinates Frames)
geodesic curves will be more complex curves tracing the shortest path
between two positions in a non-linear projection. [FALSE]



INFO = _LOGICAL (Read)
``````````````````````
If TRUE then messages are displayed describing the use of the mouse
prior to obtaining the first position. Note, these informational
messages are not suppressed by setting MSG_FILTER environment variable
to QUIET. [TRUE]



JUST = LITERAL (Read)
`````````````````````
A string specifying the justification to be used when displaying text
strings at the supplied cursor positions. This parameter is only
accessed if Parameter PLOT is set to "Text". The supplied string
should contain two characters; the first should be "B", "C" or "T",
meaning bottom, centre or top. The second should be "L", "C" or "R",
meaning left, centre or right. The text is displayed so that the
supplied position is at the specified point within the displayed text
string. [CC]



LASTDIM = _INTEGER (Write)
``````````````````````````
The number of axis values written to Parameter LASTPOS.



LASTPOS() = _DOUBLE (Write)
```````````````````````````
The unformatted co-ordinates of the last valid position selected with
the cursor, in the co-ordinate Frame which was used to report the
position. The number of axis values is written to output Parameter
LASTDIM.



LOGFILE = FILENAME (Write)
``````````````````````````
The name of the text file in which the formatted co-ordinates of
positions selected with the cursor may be stored. This is intended
primarily for recording the screen output, and not for communicating
positions to subsequent applications (use Parameter OUTCAT for this
purpose). A null string (!) means that no file is created. [!]



MARKER = _INTEGER (Read)
````````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Mark". It specifies the symbol with which each position should be
marked, and should be given as an integer PGPLOT marker type. For
instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3 gives an
asterisk, 7 gives a triangle. The value must be larger than or equal
to -31. [current value]



MAXPOS = _INTEGER (Read)
````````````````````````
The maximum number of positions which may be supplied before the
application terminates. The number must be in the range 1 to 200.
[200]



MINPOS = _INTEGER (Read)
````````````````````````
The minimum number of positions which may be supplied. The user is
asked to supply more if necessary. The number must be in the range 0
to the value of Parameter MAXPOS. [0]



MODE = LITERAL (Read)
`````````````````````
The method used to select the pictures in which cursor positions are
to be reported. There are three options:


+ "Current" -- reports positions within the current picture in the AGI
database. If a position does not lie within the current picture, an
extrapolated position is reported, if possible.
+ "Dynamic" -- reports positions within the top-most picture under the
cursor in the AGI database. Thus the second and subsequent cursor hits
may result in the selection of a new picture.
+ "Anchor" -- lets the first cursor hit select the picture in which
  all positions are to be reported. If a subsequent cursor hit falls
  outside this picture, an extrapolated position is reported if
  possible.

["Dynamic"]



NAME = LITERAL (Read)
`````````````````````
Only pictures of this name are to be selected. For instance, if you
want positions in a DATA picture which is covered by a transparent
FRAME picture, then you could specify NAME=DATA. A null (!) or blank
string means that pictures of all names may be selected. NAME is
ignored when MODE = "Current". [!]



NUMBER = _INTEGER (Write)
`````````````````````````
The number of positions selected with the cursor (excluding invalid
positions).



OUTCAT = FILENAME (Write)
`````````````````````````
An output catalogue in which to store the valid selected positions.
The catalogue has the form of a positions list such as created by
application LISTMAKE. Only positions in the first selected picture are
recorded. This application uses the conventions of the CURSA package
(SUN/190) for determining the format of the catalogue. If a file type
of .fit is given, then the catalogue is stored as a FITS binary table.
If a file type of .txt is given, then the catalogue is stored in a
text file in "Small Text List" (STL) format. If no file type is given,
then ".fit" is assumed. If a null value is supplied, no output
positions list is produced. See also Parameter CATFRAME. [!]



PLOT = LITERAL (Read)
`````````````````````
The type of graphics to be used to mark the selected positions which
have valid co-ordinates. The appearance of these graphics (colour,
size, etc ) is controlled by the STYLE parameter. PLOT can take any of
the following values:


+ "None" -- No graphics are produced.
+ "Mark" -- Each position is marked by the symbol specified by
Parameter MARKER.
+ "Poly" -- Causes each position to be joined by a line to the
previous position. These lines may be simple straight lines or
geodesic curves (see Parameter GEODESIC). The polygons may optionally
be closed by joining the last position to the first (see Parameter
CLOSE).
+ "Chain" -- This is a combination of "Mark" and "Poly". Each position
is marked by a symbol and joined by a line to the previous position.
Parameters MARKER, GEODESIC and CLOSE are used to specify the symbols
and lines to use.
+ "Box" -- A rectangular box with edges parallel to the edges of the
graphics device is drawn with the specified position at one corner,
and the previously specified position at the diagonally opposite
corner.
+ "Vline" -- A vertial line is drawn through each specified position,
extending the entire height of the selected picture.
+ "Hline" -- A horizontal line is drawn through each specified
position, extending the entire width of the selected picture.
+ "Cross" -- A combination of "Vline" and "Hline".
+ "Text" -- A text string is used to mark each position. The string is
  drawn horizontally with the justification specified by Parameter JUST.
  The strings to use for each position are specified using Parameter
  STRINGS.

[current value]



SHOWDATA = _LOGICAL (Read)
``````````````````````````
If TRUE, the pixel value within the displayed NDF is reported for each
selected position. This is only possible if the picture within which
position are being selected contains a reference to an existing NDF.
The NDF array component to be displayed is selected via Parameter
COMP. [FALSE]



SHOWPIXEL = _LOGICAL (Read)
```````````````````````````
If TRUE, the pixel co-ordinates of each selected position are shown on
a separate line, following the co-ordinates requested using Parameter
FRAME. If pixel co-ordinates are being displayed anyway (see Parameter
FRAME) then a value of FALSE is used for. SHOWPIXEL. [current value]



STRINGS = LITERAL (Read)
````````````````````````
A group of text strings which are used to mark the supplied positions
if Parameter PLOT is set to "TEXT". The first string in the group is
used to mark the first position, the second string is used to mark the
second position, etc. If more positions are given than there are
strings in the group, then the extra positions will be marked with an
integer value indicating the index within the list of supplied
positions. If a null value (!) is given for the parameter, then all
positions will be marked with integer indices, starting at 1.
A comma-separated list should be given in which each element is either
a marker string, or the name of a text file preceded by an up-arrow
character "^". Such text files should contain further comma-separated
lists which will be read and interpreted in the same manner. Note,
strings within text files can be separated by new lines as well as
commas.



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the graphics specified by Parameter PLOT. The format of
the positions reported on the screen may also be controlled.
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
In addition to the attributes which control the appearance of the
graphics (Colour, Fount, etc), the following attributes may be set in
order to control the appearance of the formatted axis values reported
on the screen: Format, Digits, Symbol, Unit. These may be suffixed
with an axis number (e.g. "Digits(2)") to refer to the values
displayed for a specific axis. [current value]



Examples
~~~~~~~~
cursor frame=pixel
This obtains co-ordinates within any visible picture for the current
graphics device by use of the cursor. Positions are reported in pixel
co-ordinates if available, and in the current co-ordinate Frame of the
picture otherwise.
cursor frame=pixel outcat=a catframe=gal
Like the previous example, except that, in addition to being displayed
on the screen, the positions are transformed into galactic co-
ordinates and stored in FITS binary table called "a.FIT", together
with any associated WCS information.
cursor frame=equat(J2010)
This obtains co-ordinates within any visible picture for the current
graphics device by use of the cursor. Positions are reported in
equatorial RA/DEC co-ordinates (referenced to the J2010 equinox) if
available, and in the current co-ordinate Frame of the picture
otherwise.
cursor describe plot=mark marker=3 style="colour=red,size=2"
As above except, positions are always reported in the current co-
ordinate Frame of each picture. The details of these co-ordinate
Frames are described as they are used. Each selected point is marked
with PGPLOT marker 3 (an asterisk). The markers are red and are twice
the default size.
cursor current maxpos=2 minpos=2 plot=poly outcat=slice
Exactly two positions are obtained within the current picture, and are
joined with a straight line. The positions are written to a FITS
binary catalogue called slice.FIT. The catalogue may be used to
communicate the positions to later applications (LISTSHOW, PROFILE,
etc).
cursor name=data style="^mystyle,digits(1)=5,digits(2)=7"
This obtains co-ordinates within any visible DATA picture on the
current graphics device. The style to use is read from text file
mystyle, but is then modified so that 5 digits are used to format
Axis-1 values, and 7 to format Axis-2 values.
cursor plot=box style="width=3,colour=red" maxpos=2 minpos=2
Exactly two positions must be given using the cursor, and a red box is
drawn joining the two positions. The lines making up the box are three
times the default width.
cursor plot=text style="size=2,textbackcolour=clear"
Positions are marked using integer values, starting at 1 for the first
position. The text drawn is twice as large as normal, and the
background is not cleared before drawing the text.



Notes
~~~~~


+ The unformatted values stored in the output Parameter LASTPOS, may
not be in the same units as the formatted values shown on the screen
and logged to the log file. For instance, unformatted celestial co-
ordinate values are stored in radians.
+ The current picture is unchanged by this application.
+ In DYNAMIC and ANCHOR modes, if the cursor is situated at a position
where there are no pictures of the selected name, the co-ordinates in
the BASE picture are reported.
+ Pixel co-ordinates are formatted with 1 decimal place unless a
format has already been specified by setting the Format attributes for
the axes of the PIXEL co-ordinate Frame (eg using application
WCSATTRIB).
+ Positions can be removed (the instructions state how), starting from
the most-recent one. Such positions are excluded from the output
positions list and log file (if applicable). If graphics are being
used to mark the positions, then removed positions will be highlighted
by drawing a marker of type 8 (a circle containing a cross) over the
removed positions in a different colour.
+ The positions are not displayed on the screen when the message
  filter environment variable MSG_FILTER is set to QUIET. The creation
  of output parameters and files is unaffected by MSG_FILTER. The
  display of informational messages describing the use of the cursor is
  controlled by the Parameter INFO.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LISTSHOW, LISTMAKE, PICCUR; Figaro: ICUR, IGCUR.


Copyright
~~~~~~~~~
Copyright (C) 1989-1993 Science & Engineering Research Council.
Copyright (C) 1995-2001 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2009-2010 Science and Technology Facilities Council. All
Rights Reserved.


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


