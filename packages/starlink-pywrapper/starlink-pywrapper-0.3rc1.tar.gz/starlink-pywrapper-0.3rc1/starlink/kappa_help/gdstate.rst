

GDSTATE
=======


Purpose
~~~~~~~
Shows the current status of a graphics device


Description
~~~~~~~~~~~
This application displays information about the current graphics
database picture on a graphics device, including the extreme axis
values in any requested co-ordinate Frame (see Parameter FRAME).
Information is written to various output parameters for use by other
applications, and is also written to the screen by default (see
Parameter REPORT). An outline may be drawn around the current picture
if required (see Parameter OUTLINE).
A list of the colours in the current palette is also produced.


Usage
~~~~~


::

    
       gdstate [device] [frame]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMMENT = LITERAL (Write)
`````````````````````````
The comment of the current picture. Up to 132 characters will be
written.



DESCRIBE = _LOGICAL (Read)
``````````````````````````
If TRUE, a detailed description is displayed of the co-ordinate Frame
in which the picture bounds are reported (see Parameter FRAME).
[current value]



DEVICE = DEVICE (Read)
``````````````````````
Name of the graphics device about which information is required.
[Current graphics device]



DOMAIN = LITERAL (Write)
````````````````````````
The Domain name of the current co-ordinate Frame for the current
picture.



EPOCH = _DOUBLE (Read)
``````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
Parameter FRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the
displayed sky co-ordinates were determined. It should be given as a
decimal years value, with or without decimal places ("1996.8" for
example). Such values are interpreted as a Besselian epoch if less
than 1984.0 and as a Julian epoch otherwise.



FRAME = LITERAL (Read)
``````````````````````
A string determining the co-ordinate Frame in which the bounds of the
current picture are to be reported. When a picture is created by an
application such as PICDEF, DISPLAY, etc, WCS information describing
the available co-ordinate systems are stored with the picture in the
graphics database. This application can report bounds in any of the
co-ordinate Frames stored with the current picture. The string
supplied for FRAME can be one of the following:


+ A domain name such as SKY, AXIS, PIXEL, NDC, BASEPIC, CURPIC, etc.
The special domain AGI_WORLD is used to refer to the world co-ordinate
system stored in the AGI graphics database. This can be useful if no
WCS information was store with the picture when it was created.
+ An integer value giving the index of the required Frame.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).

If a null value (!) is supplied, bounds are reported in the co-
ordinate Frame which was current when the picture was created. [!]



LABEL = LITERAL (Write)
```````````````````````
The label of the current picture. It is blank if there is no label.



NAME = LITERAL (Write)
``````````````````````
The name of the current picture.



OUTLINE = _LOGICAL (Read)
`````````````````````````
If OUTLINE is TRUE, then an outline will be drawn around the current
picture to indicate its position. [FALSE]



REFNAM = LITERAL (Write)
````````````````````````
The reference object associated with the current picture. It is blank
if there is no reference object. Up to 132 characters will be written.



REPORT = _LOGICAL (Read)
````````````````````````
If this is FALSE the state of the graphics device is not reported,
merely the results are written to the output parameters. It is
intended for use within procedures. [TRUE]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the outline (see Parameter OUTLINE). The format of the
axis values reported on the screen may also be controlled.
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
The appearance of the outline is controlled by the attributes
Colour(Border), Width(Border), etc (the synonym "Outline" may be used
in place of "Border"). In addition, the following attributes may be
set in order to control the appearance of the formatted axis values
reported on the screen: Format, Digits, Symbol, Unit. These may be
suffixed with an axis number (e.g. "Digits(2)") to refer to the values
displayed for a specific axis. [current value]



X1 = LITERAL (Write)
````````````````````
The lowest value found within the current picture for axis 1 of the
requested co-ordinate Frame (see Parameter FRAME).



X2 = LITERAL (Write)
````````````````````
The highest value found within the current picture for axis 1 of the
requested co-ordinate Frame (see Parameter FRAME).



Y1 = LITERAL (Write)
````````````````````
The lowest value found within the current picture for axis 2 of the
requested co-ordinate Frame (see Parameter FRAME).



Y2 = LITERAL (Write)
````````````````````
The highest value found within the current picture for axis 2 of the
requested co-ordinate Frame (see Parameter FRAME).



Examples
~~~~~~~~
gdstate
Shows the status of the current graphics device. The bounds of the
picture are displayed in the current co-ordinate Frame of the picture.
gdstate ps_l basepic
Shows the status of the ps_l device. The bounds of the picture are
displayed in the BASEPIC Frame (normalised device co-ordinates in
which the short of the two dimensions of the display surface has
length 1.0).
gdstate outline frame=pixel style="'colour=red,width=3'"
Shows the status of the current graphics device and draws a thick, red
outline around the current database picture. The bounds of the picture
are displayed in the PIXEL co-ordinate Frame (if available).
gdstate refnam=(ndfname)
Shows the status of the current graphics device. If there is a
reference data object, its name is written to the ICL variable
NDFNAME.
gdstate x1=(x1) x2=(x2) y1=(y1) y2=(y2) frame=basepic
Shows the status of the current graphics device. The bounds of the
current picture in normalised device co-ordinates are written to the
ICL variables: X1, X2, Y1, Y2.



Notes
~~~~~


+ The displayed bounds are the extreme axis values found anywhere
within the current picture. In some situations these extreme values
may not occur on the edges of the picture. For instance, if the
current picture represents a region including the north celestial
pole, then displaying the picture bounds in celestial co-ordinates
will give a declination upper limit of +90 degrees, whilst the RA
limits will be 0 hours and (close to) 24 hours.
+ Previous versions of this application reported bounds in "Normalised
Device Co-ordinates". Similar functionality is now provided by setting
Parameter FRAME to "BASEPIC". Be aware though, that "Normalised Device
Co-ordinates" were normalised so that the longer of the two axes had a
length of 1.0, but BASEPIC co-ordinates are normalised so that the
shorter of the two axes has length 1.0.
+ The Domain "NDC" now refers to a Frame in which the bottom left
  corner of the device has co-ordinates (0,0) and the top right corner
  has co-ordinates (1,1).




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: GDSET, GDCLEAR.


Copyright
~~~~~~~~~
Copyright (C) 1989-1991 Science & Engineering Research Council.
Copyright (C) 2000, 2002, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2010-2011 Science & Technology Facilities
Council. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


