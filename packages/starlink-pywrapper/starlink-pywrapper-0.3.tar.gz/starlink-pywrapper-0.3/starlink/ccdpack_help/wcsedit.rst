

WCSEDIT
=======


Purpose
~~~~~~~
Modifies or examines image coordinate system information


Description
~~~~~~~~~~~
This task performs one of a set of modifications to the WCS (World
Coordinate System) components of a list of NDFs. According to the
value of the MODE parameter it will:

+ Set the Current coordinate system
+ Add a new coordinate system
+ Remove a coordinate system
+ Set an attribute for a coordinate system
+ Show the coordinate system which currently exist

The routine does not fail if some of the requested edits cannot be
performed, but a file whose name is given by the NAMELIST parameter
records which NDFs were successfully accessed.


Usage
~~~~~


::

    
       WCSEDIT in mode frame
       



ADAM parameters
~~~~~~~~~~~~~~~



COEFFS( * ) = _DOUBLE (Read)
````````````````````````````
If MODE is ADD, this parameter is a list of the coefficients used for
the mapping from the target frame to the new frame. Its meaning and
the number of values required depend on the value of MAPTYPE:

+ UNIT -- No values are required X' = X Y' = Y
+ LINEAR -- Six values C1-C6 are required: X' = C1 + C2 * X + C3 * Y
Y' = C4 + C5 * X + C6 * Y
+ PINCUSHION -- Three values C1-C3 are required: X' = X + C1 * (X -
  C2) * ( (X - C2)**2 + (Y - C3)**2 ) ) Y' = Y + C1 * (Y - C3) * ( (X -
  C2)**2 + (Y - C3)**2 ) )





DOMAIN = LITERAL (Read)
```````````````````````
If MODE is ADD this gives the Domain (name) to be used for the new
frame. Spaces in the name are ignored and letters are folded to upper
case. If the new frame is successfully added and any frame with the
same domain name already exists, the old one will be removed, and a
message will be printed to that effect. [CCD_WCSEDIT]



EPOCH = _DOUBLE (Read)
``````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter BASEFRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



FOREXP * ( * ) = LITERAL (Read)
```````````````````````````````
If MODE=ADD and MAPTYPE=MATH, this gives the expressions to be used
for the forward transformation to be added. There must be at least two
expressions (for the two coordinates) but there may be more if
intermediate expressions are to be used. Expression syntax is fortran-
like; see the AST_MATHMAP documentation in SUN/210 for details.



FRAME = LITERAL (Read)
``````````````````````
This parameter specifies the 'target frame', which has the following
meaning according to the value of the MODE parameter:

+ MODE = CURRENT -- The frame to be made Current
+ MODE = REMOVE -- The frame to remove; if it is a domain name (see
below) then all frames with that domain will be removed.
+ MODE = ADD -- The new frame will be a copy of the target frame
(though Domain and Title will be changed), and will be mapped from it
using the mapping given.
+ MODE = SET -- The frame whose attributes are to be set
+ MODE = SHOW -- This parameter is ignored

The value of this parameter can be one of the following:

+ A domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
section "Sky Co-ordinate Systems" in SUN/95).
+ The Null (!) value; in this case the Current frame is used. A domain
  name, or !, is usually the most suitable choice. [!]





IN = LITERAL (Read)
```````````````````
A list specifying the names of the NDFs whose WCS components are to be
modified or examined. The NDF names should be separated by commas and
may include wildcards.



INVERT = _LOGICAL (Read)
````````````````````````
If set TRUE the mapping defined by COEFFS will be applied in the
reverse direction. [FALSE]



INVEXP * ( * ) = LITERAL (Read)
```````````````````````````````
If MODE=ADD and MAPTYPE=MATH, this gives the expressions to be used
for the inverse transformation to be added. There must be at least two
expressions (for the two coordinates) but there may be more if
intermediate expressions are to be used. Expression syntax is fortran-
like; see the AST_MATHMAP documentation in SUN/210 for details.



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



MAPTYPE = LITERAL (Read)
````````````````````````
This parameter is required when MODE is ADD, and specifies the type of
mapping which maps from the target frame to the new frame. It may take
one of the following values:

+ UNIT -- A Unit mapping
+ LINEAR -- A linear mapping
+ PINCUSHION -- A pincushion distortion
+ MATH -- A general algebraic mapping [UNIT]





MODE = LITERAL (Read)
`````````````````````
The action to be performed. It may take one of the following values:

+ ADD -- Add a new frame (which becomes Current)
+ CURRENT -- Set the Current frame
+ REMOVE -- Remove a frame (Current frame is not changed unless the
Current one is removed)
+ SET -- Set frame attributes (Current frame is not changed)
+ SHOW -- Display a list of the frames which exist [CURRENT]





NAMELIST = LITERAL (Read)
`````````````````````````
The name of an output file in which to write the names of all the NDFs
which were successfully accessed. In particular, if MODE is CURRENT,
this list will include all the NDFs which contained the specified
frame, but exclude any which did not. [WCSEDIT.LIS]



SET = LITERAL (Read)
````````````````````
If MODE is SET, then this gives a string of the form "attribute=value"
which is to be applied to the frame. The string is passed straight to
the AST_SET routine (see SUN/210).



SIMPFI = _LOGICAL (Read)
````````````````````````
If MODE=SET and MAPTYPE=MATH, this gives the value of the mapping's
SimpFI attribute (whether it is legitimate to simplify the forward
followed by the inverse transformation to a unit transformation).
[TRUE]



SIMPIF = _LOGICAL (Read)
````````````````````````
If MODE=SET and MAPTYPE=MATH, this gives the value of the mapping's
SimpIF attribute (whether it is legitimate to simplivy the inverse
followed by the forward transformation to a unit transformation).
[TRUE]



Examples
~~~~~~~~
wcsedit * current ccd_reg
This sets the Current coordinate system of all the NDFs in the current
directory to 'CCD_REG'. The names of all the NDFs which had this
coordinate system are written to the file WCSEDIT.LIS. Any which do
not appear in this file were not modified by the program.
wcsedit data* remove frame=4
The fourth coordinate frame in the WCS component of each NDF
'data*.sdf' is removed.
wcsedit "first,second" mode=add frame=GRID maptype=pincushion
coeffs=[-6.8e-8,0,0] domain=NEW A new coordinate system, called 'NEW',
is added to the NDFs first and second. It is connected to the
previously existing GRID domain by a pincushion distortion mapping
centred at the origin with a distortion coefficient of

+ 6.8e-8. If any frames with domain NEW already exist in those NDFs
  they are removed.


wcsedit ndf1 set ! set="domain=NEW,title=New frame"
This changes the value of the Domain attribute of the Current
coordinate frame in the WCS component of NDF1 to the name "NEW" and
sets the Title attribute of the frame to "New frame".
wcsedit image1 show
This displays all the coordinate frames in image1 with their Domains
and titles, and indicates which one is Current.
wcsedit frm mode=add frame=pixel maptype=math simpif simpfi
forexp=["r=sqrt(x*x+y*y)","theta=atan2(y,x)"]
invexp=[x=r*cos(theta),y=r*sin(theta)] Adds a frame giving a polar
coordinate view of the PIXEL frame.



Notes
~~~~~
This routine provides similar functionality to that provided by KAPPA
applications WCSADD, WCSREMOVE and WCSFRAME, but allows use of
CCDPACK-style NDF lists.


Copyright
~~~~~~~~~
Copyright (C) 1999 Central Laboratory of the Research Councils


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


