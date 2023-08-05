

PICTRANS
========


Purpose
~~~~~~~
Transforms a graphics position from one picture co-ordinate Frame to
another


Description
~~~~~~~~~~~
This application transforms a position on a graphics device from one
co-ordinate Frame to another. The input and output Frames may be
chosen freely from the Frames available in the WCS information stored
with the current picture in the AGI graphics database. The transformed
position is formatted for display and written to the screen and also
to an output parameter.


Usage
~~~~~


::

    
       pictrans posin framein [frameout] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



BOUND = _LOGICAL (Write)
````````````````````````
BOUND is TRUE when the supplied point lies within the bounds of the
current picture.



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation. [The current graphics device]



EPOCHIN = _DOUBLE (Read)
````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAMEIN) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky position was determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



EPOCHOUT = _DOUBLE (Read)
`````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAMEOUT) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the
transformed sky position is required. It should be given as a decimal
years value, with or without decimal places ("1996.8" for example).
Such values are interpreted as a Besselian epoch if less than 1984.0
and as a Julian epoch otherwise.



FRAMEIN = LITERAL (Read)
````````````````````````
A string specifying the co-ordinate Frame in which the input position
is supplied (see parameter POSIN). The string can be one of the
following:


+ A domain name such as SKY, AXIS, PIXEL, GRAPHICS, NDC, CURPIC,
BASEPIC, CURNDC, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).

If a null parameter value is supplied, then the current Frame in the
current picture is used. [!]



FRAMEOUT = LITERAL (Read)
`````````````````````````
A string specifying the co-ordinate Frame in which the transformed
position is required. If a null parameter value is supplied, then the
current Frame in the picture is used. The string can be one of the
following options.


+ A domain name such as SKY, AXIS, PIXEL, GRAPHICS, NDC, CURPIC,
BASEPIC, CURNDC, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).

If a null parameter value is supplied, then the BASEPIC Frame is used.
["BASEPIC"]



POSIN = LITERAL (Read)
``````````````````````
The co-ordinates of the position to be transformed, in the co-ordinate
Frame specified by parameter FRAMEIN (supplying a colon ":" will
display details of the required co-ordinate Frame). The position
should be supplied as a list of formatted axis values separated by
spaces or commas.



POSOUT = LITERAL (Write)
````````````````````````
The formatted co-ordinates of the transformed position, in the co-
ordinate Frame specified by parameter FRAMEOUT. The position will be
stored as a list of formatted axis values separated by spaces.



Examples
~~~~~~~~
pictrans "100.3,-20.1" framein=pixel
This converts the position (100.3,-20.1), in pixel co-ordinates within
the current picture of the current graphics device, to the BASEPIC co-
ordinates of that point in the BASE picture.
pictrans "100.3,-20.1" framein=pixel frameout=graphics
This converts the position (100.3,-20.1), in pixel co-ordinates within
the current picture of the current graphics device, to the GRAPHICS
co-ordinates of that point (i.e. millimetres from the bottom-left
corner of the graphics device).
pictrans "10 10" framein=graphics frameout=basepic
This converts the position (10 10), in graphics co-ordinates (i.e. the
point which is 10mm above and to the right of the lower-left corner of
the graphics device), into BASEPIC co-ordinates.



Notes
~~~~~


+ BASEPIC co-ordinates locate a position within the entire graphics
device. The bottom-left corner of the device screen has BASEPIC co-
ordinates of (0,0). The shorter dimension of the screen has length
1.0, and the other axis has a length greater than 1.0.
+ NDC co-ordinates also locate a position within the entire graphics
device. The bottom-left corner of the device screen has NDC co-
ordinates of (0,0), and the top-right corner has NDC co-ordinates
(1,1).
+ GRAPHICS co-ordinates also span the entire graphics device but are
measured in millimetres from the bottom left corner.
+ CURPIC co-ordinates locate a point within the current picture. The
bottom-left corner of the current picture has CURPIC co-ordinates of
(0,0). The shorter dimension of the current picture has length 1.0,
and the other axis has a length greater than 1.0.
+ CURNDC co-ordinates also locate a position within the current
picture. The bottom left corner of the current picture has CURNDC co-
ordinates of (0,0), and the top right corner has CURNDC co-ordinates
(1,1).
+ The transformed position is not written to the screen when the
  message filter environment variable MSG_FILTER is set to QUIET. The
  creation of the output Parameter POSOUT is unaffected by MSG_FILTER.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: GDSTATE, PICIN, PICXY.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 2001-2002, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2009 Science and Technology Facilities Council. All
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


