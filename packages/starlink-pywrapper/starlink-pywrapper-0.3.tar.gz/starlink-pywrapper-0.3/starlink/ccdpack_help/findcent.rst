

FINDCENT
========


Purpose
~~~~~~~
Centroids image features


Description
~~~~~~~~~~~
This routine determines the centroids of image features located in the
data components of a list of NDFs. It is useful for locating accurate
values for the positions of stars given hand selected positions. It
can also be used for centroiding any sufficiently peaked image
features.
The initial positions associated with each NDF are given in formatted
files whose names are determined either using the CCDPACK NDF
extension item CURRENT_LIST (which is maintained by list processing
CCDPACK applications) or from an explicit list of names.


Usage
~~~~~


::

    
       findcent in outlist
       



ADAM parameters
~~~~~~~~~~~~~~~



AUTOSCALE = _LOGICAL (Read)
```````````````````````````
Whether to "automatically" adjust the centroid location parameters to
reflect the fact that picking good initial positions is less likely
when dealing with very large images (these tend to be displayed using
one display pixel to represent many image pixels).
If TRUE then the values of the parameters ISIZE, TOLER and MAXSHIFT
are scaled by an amount that maps the largest dimension of each input
image to an image of size 1024 square (so an image of size 2048 square
will have these parameters increased by a factor of two). [FALSE]



IN = LITERAL (Read)
```````````````````
The names of the NDFs whose data components contain image features
which are to be centroided. The NDF names should be separated by
commas and may include wildcards.



INLIST = LITERAL (Read)
```````````````````````
If NDFNAMES is FALSE then this parameter will be used to access the
names of the lists which contain the initial positions. The format of
the data in the files is described in the notes section.
The names of the input lists may use modifications of the input NDF
names, so for instance if the position lists are stored in files with
the same name as the input NDFs but with a file type of ".dat" instead
of ".sdf" then use
INLIST > *.dat
(.sdf is always removed from NDF names). If the input list names are a
modification of the NDF names say with a trailing type of
"_initial.positions". Then a response of
INLIST > *_initial.positions
will access the correct files. Names may also use substitution
elements, say the NDF names are *_data and the position lists are
*_pos.dat, then a response like
INLIST > *|data|pos.dat|
may be used. If a naming scheme has not been used then an explicit
list of names should be returned (wildcards cannot be used to specify
list names). These names should be given in the same order as the
input NDF names and may use indirection elements as well as names
separated by commas. A listing of the input NDF name order (after any
wildcard expansions etc. have been made) is shown to make sure that
the order is correct.



ISIZE = _INTEGER (Read)
```````````````````````
The size of a box side (in pixels) centered on current position which
will be used to form the marginal profiles used to estimate the
centroid. [9]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter, then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP, then the
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

If the logging system has been initialised using CCDSETUP, then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



MAXITER = _INTEGER (Read)
`````````````````````````
The maximum number of iterations which may be used in estimating the
centroid. Only used if the tolerance criterion is not met in this
number of iterations. [3]



MAXSHIFT = _DOUBLE (Read)
`````````````````````````
The maximum shift (in pixels) allowed from an initial position. [5.5]



NAMELIST = LITERAL (Read)
`````````````````````````
Only used if NDFNAMES is FALSE. If this is the case then this
specifies the name of a file to contain a listing of the names of the
output lists. This file may then be used to pass the names onto
another CCDPACK application using indirection. [FINDCENT.LIS]



NDFNAMES = _LOGICAL (Read)
``````````````````````````
If TRUE then the routine will assume that the names of the input
position lists are stored in the CCDPACK extension item "CURRENT_LIST"
of the input NDFs. The names will be present in the extension if the
positions were located using a CCDPACK application (such as IDICURS).
Using this facility allows the transparent propagation of position
lists through processing chains.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [TRUE]



POSITIVE = _LOGICAL (Read)
``````````````````````````
If TRUE then the image features have increasing values otherwise they
are negative. [TRUE]



OUTLIST = FILENAME (Write)
``````````````````````````
A list of names specifying the centroid result files. The names of the
lists may use modifications of the input NDF names. So if you want to
call the output lists the same name as the input NDFs except to add a
type use.
OUTLIST > *.cent
Or alternatively you can use an explicit list of names. These may use
indirection elements as well as names separated by commas. [*.cent]



TOLER = _DOUBLE (Read)
``````````````````````
The required tolerance in the positional accuracy of the centroid. On
each iteration the box of data from which the centroid is estimated is
updated. If the new centroid does not differ from the previous value
by more than this amount (in X and Y) then iteration stops. Failure to
meet this level of accuracy does not result in the centroid being
rejected, the centroiding process just stops after the permitted
number of iterations (MAXITER). [0.05]



Examples
~~~~~~~~
findcent in='*' outlist='*.cent'
In this example all the NDFs in the current directory are processed.
It is assumed that the NDFs are associated with positions lists of
inaccurate positions (via the item CURRENT_LIST in the NDF CCDPACK
extensions). These position lists are accessed and centroided with the
appropriate NDFs. On exit the new lists are named *.cent and are
associated with the NDFs (instead of the original "input" lists).
findcent ndfnames=false in='"ndf1,ndf2,ndf3"'
inlist='"ndf1.pos,ndf2.pos,ndf3.pos"' outlist='*.acc'
namelist=new_position_lists In this example the position list names
are not previously associated with the NDFs and must have their names
given explicitly (and in the same order as the NDF names). The output
lists are called the same names as the input NDFs except with the
extension .acc. The names of the output lists are written into the
file new_position_lists which can be used to pass these names onto
another application using indirection (in which invoke the next
application with ndfnames=false inlist=^new_position_lists).



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
Data following the third column is copied without modification into
the results files
In all cases, the coordinates in position lists are pixel coordinates.


+ NDF extension items.

If NDFNAMES is TRUE then the item "CURRENT_LIST" of the .MORE.CCDPACK
structure of the input NDFs will be located and assumed to contain the
names of the lists whose positions are to be centroided. On exit this
item will be updated to reference the name of the centroided list of
positions.


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new datasets or
after a break of sometime. The intrinsic default behaviour of the
application may be restored by using the RESET keyword on the command
line.
Certain parameters (LOGTO, LOGFILE and NDFNAMES) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1992-1993 Science & Engineering Research Council.
Copyright (C) 1995, 1997, 1999-2001 Central Laboratory of the Research
Councils. All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA and QUALITY components of
  an NDF data structure. Bad pixels and all non-complex numeric data
  types can be handled.




