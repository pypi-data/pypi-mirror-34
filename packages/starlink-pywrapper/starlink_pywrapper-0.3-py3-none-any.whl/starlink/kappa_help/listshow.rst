

LISTSHOW
========


Purpose
~~~~~~~
Reports the positions stored in a positions list


Description
~~~~~~~~~~~
This application reports positions contained in a catalogue. The
catalogue should have the form of a positions list as produced, for
instance, by applications LISTMAKE and CURSOR. By default all
positions in the catalogue are reported, but a subset may be reported
by specifying a range of "position identifiers" (see Parameters FIRST,
LAST and STEP).
Positions may be reported in a range of co-ordinate Frames dependent
on the information stored in the supplied positions list (see
Parameter FRAME). The selected positions are written to an output
parameter (Parameter POSNS), and may also be written to an output
positions list (see Parameter OUTCAT). The formatted screen output can
be saved in a logfile (see Parameter LOGFILE). The formats used to
report the axis values can be controlled using Parameter STYLE.
Graphics may also be drawn marking the selected positions (see
Parameters PLOT and LABEL). The supplied positions are aligned with
the picture specified by Parameter NAME. If possible, this alignment
occurs within the co-ordinate Frame specified using Parameter FRAME.
If this is not possible, alignment may occur in some other suitable
Frame. A message is displayed indicating the Frame in which alignment
occurred. If the supplied positions are aligned successfully with a
picture, then the range of Frames in which the positions may be
reported on the screen is extended to include all those associated
with the picture.


Usage
~~~~~


::

    
       listshow incat [frame] [first] [last] [plot] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



CATFRAME = LITERAL (Read)
`````````````````````````
A string determining the co-ordinate Frame in which positions are to
be stored in the output catalogue associated with Parameter OUTCAT.
See Parameter FRAME for a description of the allowed values for this
parameter. If a null (!) value is supplied, the positions will be
stored in the Frame used to specify positions within the input
catalogue. [!]



CATEPOCH = DOUBLE PRECISION (Read)
``````````````````````````````````
The epoch at which the sky positions stored in the output catalogue
were determined. It will only be accessed if an epoch value is needed
to qualify the co-ordinate Frame specified by COLFRAME. If required,
it should be given as a decimal years value, with or without decimal
places ("1996.8", for example). Such values are interpreted as a
Besselian epoch if less than 1984.0 and as a Julian epoch otherwise.



CLOSE = LOGICAL (Read)
``````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Poly". If TRUE, polgons will be closed by joining the first position
to the last position. [Current value]



DESCRIBE = LOGICAL (Read)
`````````````````````````
If TRUE, a detailed description of the co-ordinate Frame in which the
positions will be reported is displayed before the positions. [Current
value]



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation. Only accessed if Parameter PLOT indicates
that graphics are required. [The current graphics device]



DIM = _INTEGER (Write)
``````````````````````
The number of axes for each position written to output Parameter
POSNS.



EPOCH = DOUBLE PRECISION (Read)
```````````````````````````````
If an IRAS90 Sky Co-ordinate System specification is supplied (using
Parameter FRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



FIRST = INTEGER (Read)
``````````````````````
The identifier for the first position to be displayed. Positions are
only displayed which have identifiers in the range given by Parameters
FIRST and LAST. If a null (!) value is supplied, the value used is the
lowest identifier value in the positions list. [!]



FRAME = LITERAL (Read)
``````````````````````
A string determining the co-ordinate Frame in which positions are to
be reported. This application can report positions in any of the co-
ordinate Frames stored with the positions list. The string supplied
for FRAME can be one of the following.


+ A Domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame.
+ An IRAS90 Sky Co-ordinate System (SCS) values such as EQUAT(J2000)
  (see SUN/163).

If a null value (!) is supplied, positions are reported in the co-
ordinate Frame which was current when the positions list was created.
The user is re-prompted if the specified Frame is not available within
the positions list. The range of Frames available will include all
those read from the supplied positions list. In addition, if a
graphics device is opened (i.e. if Parameter PLOT is set to anything
other than NONE), then all the Frames associated with the picture
specified by Parameter NAME will also be available. [!]



GEODESIC = LOGICAL (Read)
`````````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Poly". It specifies whether the curves drawn between positions should
be stright lines, or should be geodesic curves. In many co-ordinate
Frames geodesic curves will be simple straight lines. However, in
others (such as the majority of celestial co-ordinate Frames) geodesic
curves will be more complex curves tracing the shortest path between
two positions in a non-linear projection. [FALSE]



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a positions list such as produced by
applications LISTMAKE, CURSOR, etc.



JUST = LITERAL (Read)
`````````````````````
A string specifying the justification to be used when displaying text
strings at the supplied positions. This parameter is only accessed if
Parameter PLOT is set to "Text". The supplied string should contain
two characters; the first should be "B", "C", or "T", meaning bottom,
centre, or top respectively. The second should be "L", "C", or "R",
meaning left, centre, or right respectively. The text is displayed so
that the supplied position is at the specified point within the
displayed text string. ["CC"]



LABEL = LOGICAL (Read)
``````````````````````
If TRUE the positions are labelled on the graphics device specified by
Parameter DEVICE. The offset of the centre of each label from the
corresponding position is controlled using the "NumLabGap(1)" and
"NumLabGap(2)" plotting attributes, and the appearance of the labels
is controlled using attributes "Colour(NumLab)", "Size(NumLab)", etc.
These attributes may be specified using Parameter STYLE. The content
of the label is determined by Parameter LABTYPE. [FALSE]



LABTYPE = LITERAL (Read)
````````````````````````
Determines what sort of labels are drawn if the LABEL parameter is set
TRUE. It can be either of the following.


+ "ID" -- causes the integer identifier associated with each row to be
used as the label for the row.
+ "LABEL" -- causes the textual label associated with each row to be
  used as the label for the row. These strings are read from the "LABEL"
  column of the supplied catalogue.

If a null (!) value is supplied, a default of "LABEL" will be used if
the input catalogue contains a "LABEL" column. Otherwise, a default of
"ID" will be used. [!]



LAST = INTEGER (Read)
`````````````````````
The identifier for the last position to be displayed. Positions are
only displayed which have identifiers in the range given by Parameters
FIRST and LAST. If a null (!) value is supplied, the value used is the
highest identifier value in the positions list. [!]



LOGFILE = FILENAME (Write)
``````````````````````````
The name of the text file in which the formatted co-ordinates of the
selected positions may be stored. This is intended primarily for
recording the screen output, and not for communicating positions to
subsequent applications. A null string (!) means that no file is
created. [!]



MARKER = INTEGER (Read)
```````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Mark". It specifies the type of marker with which each position
should be marked, and should be given as an integer PGPLOT marker
type. For instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3
gives an asterisk, 7 gives a triangle. The value must be larger than
or equal to -31. [current value]



NAME = LITERAL (Read)
`````````````````````
Determines the graphics database picture with which the supplied
positions are to be aligned. Only accessed if Parameter PLOT indicates
that some graphics are to be produced. A search is made for the most
recent picture with the specified name (e.g. DATA, FRAME or KEY)
within the current picture. If no such picture can be found, or if a
null value is supplied, the current picture itself is used. The name
BASE can also be supplied as a special case, which causes the BASE
picture to be used even though it will not in general fall within the
current picture. ["DATA"]



NUMBER = _INTEGER (Write)
`````````````````````````
The number of positions selected.



OUTCAT = FILENAME (Write)
`````````````````````````
The output catalogue in which to store the selected positions. If a
null value is supplied, no output catalogue is produced. See Parameter
COLFRAME. [!]



PLOT = LITERAL (Read)
`````````````````````
The type of graphics to be used to mark the positions on the graphics
device specified by Parameter DEVICE. The appearance of these graphics
(colour, size, etc.) is controlled by the STYLE parameter. PLOT can
take any of the following values.


+ "None" -- No graphics are produced.
+ "Mark" -- Each position is marked with a marker of type specified by
Parameter MARKER.
+ "Poly" -- Causes each position to be joined by a line to the
previous position. These lines may be simple straight lines or
geodesic curves (see Parameter GEODESIC). The polygons may optionally
be closed by joining the last position to the first (see Parameter
CLOSE).
+ "Chain" -- This is a combination of "Mark" and "Poly". Each position
is marked by a marker and joined by a line to the previous position.
Parameters MARKER, GEODESIC and CLOSE are used to specify the markers
and lines to use.
+ "Box" -- A rectangular box with edges parallel to the edges of the
graphics device is drawn between each pair of positions.
+ "Vline" -- A vertical line is drawn through each position, extending
the entire height of the selected picture.
+ "Hline" -- A horizontal line is drawn through each position,
extending the entire width of the selected picture.
+ "Cross" -- A combination of "Vline" and "Hline".
+ "STCS" -- Indicates that each position should be marked using the
two-dimensional STC-S shape read from the catalogue column specified
by Parameter STCSCOL.
+ "Text" -- A text string is used to mark each position. The string is
drawn horizontally with the justification specified by Parameter JUST.
The strings to use for each position are specified using Parameter
STRINGS.
+ "Blank" -- The graphics device is opened and the picture specified
  by Parameter NAME is found, but no actual graphics are drawn to mark
  the positions. This can be useful if you just want to transform the
  supplied positions into one of the co-ordinate Frames associated with
  the picture, without drawing anything (see Parameter FRAME).

Each position may also be separately labelled with its integer
identifier value by giving a TRUE value for Parameter LABEL. ["None"]



POSNS() = _DOUBLE (Write)
`````````````````````````
The unformatted co-ordinates of the positions selected by Parameters
FIRST and LAST, in the co-ordinate Frame selected by FRAME. The axis
values are stored as a 1-dimensional vector. All the axis-1 values for
the selected positions are stored first, followed by the axis-2
values, etc. The number of positions in the vector is written to the
output Parameter NUMBER, and the number of axes per position is
written to the output Parameter DIM. The axis values may not be in the
same units as the formatted values shown on the screen. For instance,
unformatted celestial co-ordinate values are stored in units of
radians.



STEP = _INTEGER (Read)
``````````````````````
The increment between position identifiers to be displayed. Specifying
a value larger than 1 causes a subset of the position identifiers
between FIRST and LAST to be displayed. [1]



STCSCOL = LITERAL (Read)
````````````````````````
The name of a catalogue column containing an STC-S description of a
two-dimensional spatial shape associated with each position. The STC-S
format is an IVOA proposal for describing regions of space, time and
spectral position. For further details, see the STC-S document on the
IVOA web site (http://www.ivoa.net/Documents/). An STC-S description
of a shape includes the co-ordinate system in which the shape is
defined. This application assumes that all the STC-S shapes read from
the specified column will be defined within the same co-ordinate
system. The transformation from the STC-S co-ordinate system to the
co-ordinate system of the displayed image is determined once from the
first shape plotted, and then re-used for all later shapes. ["Shape"]



STRINGS = LITERAL (Read)
````````````````````````
A group of text strings which are used to mark the supplied positions
if Parameter PLOT is set to "TEXT". The first string in the group is
used to mark the first position, the second string is used to mark the
second position, etc. If more positions are given than there are
strings in the group, then the extra positions will be marked with an
integer value indicating the index within the list of supplied
positions. (Note, these integers may be different from the position
identifiers in the supplied positions list). If a null value (!) is
given for the parameter, then all positions will be marked with the
integer indices, starting at 1.
A comma-separated list should be given in which each element is either
a marker string, or the name of a text file preceded by an up-arrow
character "^". Such text files should contain further comma-separated
lists which will be read and interpreted in the same manner. Note,
strings within text files can be separated by new lines as well as
commas.



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the style to use when
formatting the co-ordinate values displayed on the screen, and when
drawing the graphics specified by Parameter PLOT.
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
In addition to the attributes which control the appearance of the
graphics (Colour, Fount, etc.), the following attributes may be set in
order to control the appearance of the formatted axis values reported
on the screen: Format, Digits, Symbol, Unit. These may be suffixed
with an axis number (e.g. "Digits(2)") to refer to the values
displayed for a specific axis. [current value]



Examples
~~~~~~~~
listshow stars pixel
This displays the pixel co-ordinates of all the positions stored in
the FITS binary catalogue stars.fit. They are all written to the
output Parameter POSNS.
listshow star outcat=star-gal catframe=gal quiet
This copies a position list from catalogue "star" to a new catalogue
called "star-gal". The positions are stored in galactic co-ordinates
in the output catalogue.
listshow stars.fit equat(J2010) first=3 last=3
This extracts Position 3 from the catalogue stars.fit transforming it
into FK5 equatorial RA/DEC co-ordinates (referenced to the J2010
equinox), if possible. The RA/DEC values (in radians) are written to
the output Parameter POSNS.
listshow stars_2.txt style="digits(1)=5,digits(2)=7"
This lists the positions in the STL format catalogue contained in text
file stars_2.txt in their original co-ordinate Frame. By default, five
digits are used to format Axis-1 values, and 7 to format Axis-2
values. These defaults are overridden if the attributes Format(1)
and/or Format(2) are assigned values in the description of the current
Frame stored in the positions list.
listshow s.txt plot=marker marker=3
style="colour(marker)=red,size=2" This marks the positions in s.txt on
the currently selected graphics device using PGPLOT Marker 3 (an
asterisk). The positions are aligned with the most recent DATA picture
in the current picture. The markers are red and are twice the default
size. The positions are likely not to be reported on the screen.



Notes
~~~~~


+ This application uses the conventions of the CURSA package (SUN/190)
for determining the formats of input and output catalogues. If a file
type of .fits is given, then the catalogue is assumed to be a FITS
binary table. If a file type of .txt is given, then the catalogue is
assumed to be stored in a text file in "Small Text List" (STL) format.
If no file type is given, then ".fit" is assumed.
+ The positions are not displayed on the screen when either the
  message filter environment variable MSG_FILTER is set to NORMAL and
  any graphics or labels are being plotted (see Parameters PLOT and
  LABEL); or when MSG_FILTER is set to QUIET and no graphics are
  produced. The creation of output parameters and files is unaffected by
  MSG_FILTER.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CURSOR, LISTMAKE; CURSA: XCATVIEW, CATSELECT.


Copyright
~~~~~~~~~
Copyright (C) 1998-1999, 2001, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. Copyright (C) 2009-2010 Science and Technology Facilities
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


