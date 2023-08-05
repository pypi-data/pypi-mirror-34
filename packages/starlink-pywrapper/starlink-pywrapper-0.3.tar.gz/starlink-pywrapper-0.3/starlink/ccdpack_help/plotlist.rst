

PLOTLIST
========


Purpose
~~~~~~~
Draws position markers on a graphics display


Description
~~~~~~~~~~~
This routine draws a variety of markers (crosses, circles, squares
etc.) on a graphics device at positions specified in a series of
position lists. Before this application can be run an image (or other
graphical output such as a contour image) must have been displayed
using a suitable routine such as KAPPA's DISPLAY (SUN/95) or CCDPACK's
DRAWNDF.
For a more interactive display of markers on an Xwindows display, you
can use the IDICURS program instead.


Usage
~~~~~


::

    
       plotlist inlist [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



CLEAR = _LOGICAL (Read)
```````````````````````
This parameter controls whether or not the display device is cleared
before plotting the markers. Setting this TRUE could be useful if
plotting in a device overlay. [FALSE]



DEVICE = DEVICE (Write)
```````````````````````
The name of the device on which to plot the markers. [Current display
device]



INLIST = LITERAL (Read)
```````````````````````
This parameter is used to access the names of the lists which contain
the positions and, if NDFNAMES is TRUE, the names of the associated
NDFs. If NDFNAMES is TRUE the names of the position lists are assumed
to be stored in the extension of the NDFs (in the CCDPACK extension
item CURRENT_LIST) and the names of the NDFs themselves should be
given (and may include wildcards).
If NDFNAMES is FALSE then the actual names of the position lists
should be given. These may not use wildcards but may be specified
using indirection (other CCDPACK position list processing routines
will write the names of their results files into files suitable for
use in this manner) the indirection character is "^".



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is
"CCDPACK.LOG". [CCDPACK.LOG]



LOGTO = LITERAL (Read)
``````````````````````
Every CCDPACK application has the ability to log its output for future
reference as well as for display on the terminal. This parameter
controls this process, and may be set to any unique abbreviation of
the following:

+ TERMINAL -- Send output to the terminal only
+ LOGFILE -- Send output to the logfile only (see the LOGFILE
parameter)
+ BOTH -- Send output to both the terminal and the logfile
+ NEITHER -- Produce no output at all

If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



MSIZE = _REAL (Read)
````````````````````
The size of the marker which will be drawn as a multiple of the
default value. So for instance doubling the value of this parameter
will increase the size of the markers by a factor of two. The default
marker size is around 1/40 of the lesser of the width or height of the
plot. [2.5]



MTYPE = _INTEGER (Read)
```````````````````````
The type of marker to plot at the positions given in the input files.
PGPLOT Graph Markers are drawn if the value lies in the range 0-31 (a
value of 2 gives a cross, 7 a triangle, 24-27 various circles etc. see
the PGPLOT manual). If the value of this parameter is less than zero
then the identifier values, which are in column one of the input file,
will be written over the objects. [2]



NDFNAMES = _LOGICAL (Read)
``````````````````````````
If TRUE then the routine will assume that the names of the position
lists are stored in the NDF CCDPACK extensions under the item
"CURRENT_LIST".
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [TRUE]



PALNUM = _INTEGER (Read)
````````````````````````
The pen number to use when drawing the markers. The colours associated
with these pens are the default PGPLOT pens (see the PGPLOT manual for
a complete description). These are:

+ 0 -- background colour
+ 1 -- foreground colour
+ 2 -- red
+ 3 -- green
+ 4 -- blue
+ 5 -- cyan
+ 6 -- magenta
+ 7 -- yellow
+ 8 -- orange

and so on up to pen 16 (or up to the number available on the current
graphics device). After PLOTLIST has been run these colours can be
superseded by using the KAPPA palette facilities PALDEF and PALENTRY,
but note that any subsequent runs of PLOTLIST will reinstate the
PGPLOT default colours. The KAPPA palette pen numbers correspond to
PALNUM values (hence the parameter name). [3]



THICK = _INTEGER (Read)
```````````````````````
The thickness of the lines used to draw the markers. This may take any
value in the range 1-21. [1]



Examples
~~~~~~~~
plotlist inlist='*'
In this example all the NDFs in the current directory are accessed and
their associated lists of positions are plotted onto the current
display device.
plotlist ndfnames=false inlist=one_list.dat
In this example the position list one_list.dat is opened and its
position are plotted on the current display device.
plotlist in='aligned_*' mtype=-1 palnum=4 msize=1 thick=3
In this example the NDFs aligned_* have their associated position
lists accessed and the positions are plotted on the current display
device. The pen colour used is blue. The text is drawn at a relative
size of 1 (the normal default is 2.5) with a line thickness of 3.



Notes
~~~~~


+ Position list formats.

CCDPACK supports data in two formats.
CCDPACK format - the first three columns are interpreted as the
following.


+ Column 1: an integer identifier
+ Column 2: the X position
+ Column 3: the Y position

The column one value must be an integer and is used to identify
positions which are the same but which have different locations on
different images. Values in any other (trailing) columns are usually
ignored.
EXTERNAL format - positions are specified using just an X and a Y
entry and no other entries.


+ Column 1: the X position
+ Column 2: the Y position

This format is used by KAPPA applications such as CURSOR.
Comments may be included in a file using the characters "#" and "!".
Columns may be separated by the use of commas or spaces.


+ NDF extension items.

If NDFNAMES is TRUE then the item "CURRENT_LIST" of the .MORE.CCDPACK
structure of the input NDFs will be located and assumed to contain the
names of the lists whose positions are to be plotted.


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application. The intrinsic default
behaviour of the application may be restored by using the RESET
keyword on the command line.
Certain parameters (LOGTO, LOGFILE and NDFNAMES) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.
The DEVICE parameter also has a global association. This is not
controlled by the usual CCDPACK mechanisms, instead it works in co-
operation with KAPPA (SUN/95) image display/control routines.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2000-2001 Central Laboratory of the Research Councils.
All Rights Reserved.


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


