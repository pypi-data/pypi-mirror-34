

PICIN
=====


Purpose
~~~~~~~
Finds the attributes of a picture interior to the current picture


Description
~~~~~~~~~~~
This application finds the attributes of a picture, selected by name,
that was created since the current picture and lies within the bounds
of the current picture. The search starts from the most-recent
picture, unless the current picture is included, whereupon the current
picture is tested first.
The attributes reported are the name, comment, label, name of the
reference data object, the bounds in the co-ordinate Frame selected by
parameter FRAME.


Usage
~~~~~


::

    
       picin [name] [device] [frame]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMMENT = LITERAL (Write)
`````````````````````````
The comment of the picture. Up to 132 characters will be written.



CURRENT = _LOGICAL (Read)
`````````````````````````
If this is {\tt TRUE}, the current picture is compared against the
chosen name before searching from the most-recent picture within the
current picture. [FALSE]



DESCRIBE = _LOGICAL (Read)
``````````````````````````
This controls whether or not the report (when REPORT=TRUE) should
contain a description of the Frame being used. [FALSE]



DEVICE = DEVICE (Read)
``````````````````````
Name of the graphics device about which information is required.
[Current graphics device]



DOMAIN = LITERAL (Write)
````````````````````````
The Domain name of the current co-ordinate Frame for the picture.



EPOCH = _DOUBLE (Read)
``````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the
displayed sky co-ordinates were determined. It should be given as a
decimal years value, with or without decimal places ("1996.8" for
example). Such values are interpreted as a Besselian epoch if less
than 1984.0 and as a Julian epoch otherwise.



FRAME = LITERAL (Read)
``````````````````````
A string determining the co-ordinate Frame in which the bounds of the
picture are to be reported. When a picture is created by an
application such as PICDEF, DISPLAY, etc, WCS information describing
the available co-ordinate systems are stored with the picture in the
graphics database. This application can report bounds in any of the
co-ordinate Frames stored with the current picture. The string
supplied for FRAME can be one of the following:


+ A domain name such as SKY, AXIS, PIXEL, BASEPIC, NDC, CURPIC, etc.
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
The label of the picture. It is blank if there is no label.



NAME = LITERAL (Read)
`````````````````````
The name of the picture to be found within the current picture. If it
is null (!), the first interior picture is selected. ["DATA"]



PNAME = LITERAL (Write)
```````````````````````
The name of the picture.



REFNAM = LITERAL (Write)
````````````````````````
The reference object associated with the picture. It is blank if there
is no reference object. Up to 132 characters will be written.



REPORT = _LOGICAL (Read)
````````````````````````
If this is FALSE details of the picture are not reported, merely the
results are written to the output parameters. It is intended for use
within procedures. [TRUE]



X1 = LITERAL (Write)
````````````````````
The lowest value found within the picture for axis 1 of the requested
co-ordinate Frame (see parameter FRAME).



X2 = LITERAL (Write)
````````````````````
The highest value found within the picture for axis 1 of the requested
co-ordinate Frame (see parameter FRAME).



Y1 = LITERAL (Write)
````````````````````
The lowest value found within the picture for axis 2 of the requested
co-ordinate Frame (see parameter FRAME).



Y2 = LITERAL (Write)
````````````````````
The highest value found within the picture for axis 2 of the requested
co-ordinate Frame (see parameter FRAME).



Examples
~~~~~~~~
picin
This reports the attributes of the last DATA picture within the
current picture for the current graphics device. The bounds of the
picture in its current co-ordinate Frame are reported.
picin frame=pixel
As above but the bounds of the picture in the PIXEL Frame are
reported.
picin refnam=(object) current
This reports the attributes of the last data picture within the
current picture for the current graphics device. If there is a
reference data object, its name is written to the ICL variable OBJECT.
The search includes the current picture.
picin x1=(x1) x2=(x2) y1=(y1) y2=(y2)
This reports the attributes of the last DATA picture within the
current picture for the current graphics device. The bounds of the
current picture are written to the ICL variables: X1, X2, Y1, Y2.



Notes
~~~~~
This application is intended for use within procedures. Also if a DATA
picture is selected and the current picture is included in the search,
this application informs about the same picture that an application
that works in a cursor interaction mode would select, and so acts as a
check that the correct picture will be accessed.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: GDSTATE, PICDEF, PICLIST, PICTRANS, PICXY.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1993 Science & Engineering Research Council.
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2011 Science & Technology Facilities Council. All Rights
Reserved.


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


