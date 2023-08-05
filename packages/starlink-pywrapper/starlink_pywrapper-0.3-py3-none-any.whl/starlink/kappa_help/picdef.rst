

PICDEF
======


Purpose
~~~~~~~
Defines a new graphics-database FRAME picture or an array of FRAME
pictures


Description
~~~~~~~~~~~
This application creates either one new graphics-database FRAME
picture or a grid of new FRAME pictures. It offers a variety of ways
by which you can define a new picture's location and extent. You may
constrain a new picture to lie within either the current or the BASE
picture, and the new picture adopts the world co-ordinate system of
that reference picture.
You may specify a single new picture using one of three methods: 1.
moving a cursor to define the lower and upper bounds via pressing
choice number 1 (the application will instruct what to do for the
specific graphics device), provided a cursor is available on the
chosen graphics workstation; 2. obtaining the bounds from the
environment (in world co-ordinates of the reference picture); 3. or by
giving a position and size for the new picture. The position is
specified by a two-character code. The first controls the vertical
location, and may be "T", "B", or "C" to create the new picture at the
top, bottom, or in the centre respectively. The second defines the
horizontal situation, and may be "L", "R", or "C" to define a new
picture to the left, right, or in the centre respectively. Thus a code
of "BR" will make a new picture in the bottom-right corner. The size
of the new picture along each axis may be specified either in
centimetres, or as a fraction of the corresponding axis of the
reference picture. The picture may also be forced to have a specified
aspect ratio.
The picture created becomes the current picture on exit.
Alternatively, you can create an array of n-by-m equal-sized pictures
by giving the number of pictures in the horizontal and vertical
directions. These may or may not be abutted. For easy reference in
later processing the pictures may be labelled automatically. The label
consists of a prefix you define, followed by the number of the
picture. The numbering starts at a defined value, usually one, and
increments by one for each new picture starting from the bottom-left
corner and moving from left to right to the end of the line. This is
repeated in each line until the top-right picture. Thus if the prefix
were "GALAXY", the start number is one and the array comprises three
pictures horizontally and two vertically, the top-left picture would
have the label "GALAXY4". On completion the bottom-left picture in the
array becomes the current picture.


Usage
~~~~~


::

    
       picdef [mode] [fraction]
          { xpic ypic prefix=?
          { lbound ubound
         mode
       



ADAM parameters
~~~~~~~~~~~~~~~



ASPECT = _REAL (Read)
`````````````````````
The aspect ratio (x/y) of the picture to be created in modes other
than Cursor, Array, and XY. The new picture is the largest possible
with the chosen aspect ratio that will fit within the part of the
reference picture defined by the fractional sizes (see parameter
FRACTION). The justification comes from the value of MODE. Thus to
obtain the largest picture parameter set FRACTION=1.0. A null value
(!) does not apply an aspect-ratio constraint, and therefore the new
picture fills the part of the reference picture defined by the
fractional sizes. [!]



CURRENT = _LOGICAL (Read)
`````````````````````````
TRUE if the new picture is to lie within the current picture,
otherwise the new picture can lie anywhere within the BASE picture. In
other words, when it is TRUE the current picture is the reference
picture, and when FALSE the base is the reference picture. [FALSE]



DEVICE = DEVICE (Read)
``````````````````````
The graphics device. [Current graphics device]



FILL = _REAL (Read)
```````````````````
The linear filling factor for the Array mode. In other words the
fractional size (applied to both co-ordinates) of the new picture
within each of the XPIC * YPIC abutted sections of the picture being
sub-divided. Each new picture is located centrally within the section.
A filling factor of 1.0 means that the pictures in the array abut.
Smaller factors permit a gap between the pictures. For example, FILL =
0.9 would give a gap between the created pictures of 10 per cent of
the height and width of each picture, with exterior borders of 5 per
cent. FILL must lie between 0.1 and 1.0. [1.0]



FRACTION( ) = _REAL (Read)
``````````````````````````
The fractional size of the new picture along each axis, applicable for
modes other than Array, Cursor, and XY. Thus FRACTION controls the
relative shape as well as the size of the new picture. If only a
single value is given then it is applied to both x and y axes,
whereupon the new picture has the shape of the reference picture. So a
value of 0.5 would create a picture 0.25 the area of the current or
BASE picture. The default is 0.5, unless parameter ASPECT is not null,
when the default is 1.0. This parameter is not used if the picture
size is specified in centimetres using parameter SIZE. []



LABELNO = _INTEGER (Read)
`````````````````````````
The number used to form the label for the first (bottom-left) picture
in Array mode. It cannot be negative. [1]



LBOUND( 2 ) = _REAL (Read)
``````````````````````````
BASEPIC co-ordinates of the lower bounds that defines the new picture.
The BASEPIC co-ordinates of the bottom-left corner of the BASE picture
are (0,0). The shorter dimension of the BASE picture has length 1.0,
and the other axis has a length greater than 1.0. The suggested
default is the top-right of the current picture. (XY mode)



MODE = LITERAL (Read)
`````````````````````
Method for selecting the new picture. The options are "Cursor" for
cursor mode (provided the graphics device has one), "XY" to select x-y
limits, and "Array" to create a grid of equal-sized FRAME pictures.
The remainder are locations specified by two characters, the first
corresponding to the vertical position and the second the horizontal.
For the vertical, valid positions are T(op), B(ottom), or C(entre);
and for the horizontal the options are L(eft), R(ight), or C(entre).
["Cursor"]



OUTLINE = _LOGICAL (Read)
`````````````````````````
If TRUE, a box that delimits the new picture is drawn. [TRUE]



PREFIX = LITERAL (Read)
```````````````````````
The prefix to be given to the labels of picture created in Array mode.
It should contain no more than twelve characters. If the empty string
"" is given, the pictures will have enumerated labels. Note that the
database can contain only one picture with a given label, and so
merely numbering labels increases the chance of losing existing
labels. A ! response means no labelling is required. The suggested
default is the last-used prefix.



SIZE( 2 ) = _REAL (Read)
````````````````````````
The size of the new picture along both axes, in centimetres,
applicable for modes other than Array, Cursor, and XY. If a single
value is given, it is used for both axes. If a null value (!) is
given, then the size of the picture is determined by parameter
FRACTION. [!]



UBOUND( 2 ) = _REAL (Read)
``````````````````````````
BASEPIC co-ordinates of the upper bound that defines the new picture.
The BASEPIC co-ordinates of the bottom-left corner of the BASE picture
are (0,0). The shorter dimension of the BASE picture has length 1.0,
and the other axis has a length greater than 1.0. The suggested
default is the top-right of the current picture. (XY mode)



XPIC = _INTEGER (Read)
``````````````````````
The number of new pictures to be formed horizontally in the BASE or
current picture in Array mode. The total number of new pictures is
XPIC * YPIC. The value must lie in the range 1--20. The suggested
default is 2.



YPIC = _INTEGER (Read)
``````````````````````
The number of new pictures to be formed vertically in the BASE or
current picture in Array mode. The value must lie in the range 1--20.
The suggested default is the value of parameter XPIC.



Examples
~~~~~~~~
picdef tr
Creates a new FRAME picture in the top-right quarter of the full
display area on the current graphics device, and an outline is drawn
around the new picture. This picture becomes the current picture.
picdef bl aspect=1.0
Creates a new FRAME picture within the full display area on the
current graphics device, and an outline is drawn around the new
picture. This picture is the largest square possible, and it is
justified to the bottom-left corner. It becomes the current picture.
picdef bl size=[15,10]
Creates a new FRAME picture within the full display area on the
current graphics device, and an outline is drawn around the new
picture. This picture is 15 by 10 centimetres in size and it is
justified to the bottom-left corner. It becomes the current picture.
picdef cc 0.7 current nooutline
Creates a new FRAME picture situated in the centre of the current
picture on the current graphics device. The new picture has the same
shape as the current one, but it is linearly reduced by a factor of
0.7. No outline is drawn around it. The new picture becomes the
current picture.
picdef cc [0.8,0.5] current nooutline
As above except that its height is half that of the current picture,
and its width is 0.8 of the current picture.
picdef cu device=graphon
Creates a new FRAME picture within the full display area of the
Graphon device. The bounds of the new picture are defined by cursor
interaction. An outline is drawn around the new picture which becomes
the current picture.
picdef mode=a prefix=M xpic=3 ypic=2
Creates six new equally sized and abutting FRAME pictures within the
full display area of the current graphics device. All are outlined.
They have labels M1, M2, M3, M4, M5, and M6. The bottom-left picture
(M1) becomes the current picture.
picdef mode=a prefix="" xpic=3 ypic=2 fill=0.8
As above except that the pictures do not abut since each is 0.8 times
smaller in both dimensions, and the labels are 1, 2, 3, 4, 5, and 6.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PICBASE, PICCUR, PICDATA, PICFRAME, PICGRID, PICLABEL, PICLIST,
PICSEL, PICXY.


Copyright
~~~~~~~~~
Copyright (C) 1989-1994 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2000, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. All Rights Reserved.


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


