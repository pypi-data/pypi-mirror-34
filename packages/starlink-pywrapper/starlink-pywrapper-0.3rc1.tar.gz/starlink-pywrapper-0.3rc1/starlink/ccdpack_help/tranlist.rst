

TRANLIST
========


Purpose
~~~~~~~
Transforms lists of positions


Description
~~~~~~~~~~~
This routine transforms positions stored in position lists.
Transformations are defined either by a set of 6 coefficients for the
linear transform, by an algebraic expression given by you, by using a
forward or inverse mapping from a TRANSFORM structure, or by a mapping
between two coordinate sytems in the WCS component of the NDF.


Usage
~~~~~


::

    
       tranlist inlist outlist trtype
       



ADAM parameters
~~~~~~~~~~~~~~~



EPOCHIN = _DOUBLE (Read)
````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAMEIN) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise. [Dynamic]



EPOCHOUT = _DOUBLE (Read)
`````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAMEOUT) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise. [Dynamic]



FA-FZ = LITERAL (Read)
``````````````````````
These parameters supply the values of "sub-expressions" used in the
expressions XFOR and YFOR. These parameters should be used when
repeated expressions are present in complex transformations. Sub-
expressions may contain references to other sub-expressions and
constants (PA-PZ). An example of using sub-expressions is: XFOR >
PA*ASIND(FA/PA)*X/FA YFOR > PA*ASIND(FA/PA)*Y/FA FA > SQRT(X*X+Y*Y) PA
> 100D0



FORWARD = _LOGICAL (Read)
`````````````````````````
If TRTYPE="STRUCT" then this parameter's value controls whether the
forward or inverse mapping in the transform structure is used. [TRUE]



FRAMEIN = LITERAL (Read)
````````````````````````
If TRTYPE="WCS" then the transformation is a mapping from the frame
specified by this parameter to that specified by the FRAMEOUT
parameter. The value of this parameter can be one of the following:

+ A domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95). [PIXEL]





FRAMEOUT = LITERAL (Read)
`````````````````````````
If TRTYPE="WCS" then the transformation is a mapping from the
coordinate frame specified by the FRAMEIN parameter to that specified
by this parameter. The value of this parameter can be one of the
following:

+ A domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
section "Sky Co-ordinate Systems" in SUN/95).
+ Null (!), indicating the Current frame. [!]





INEXT = _LOGICAL (Read)
```````````````````````
If NDFNAMES is TRUE and the transformation is to be specified using a
WCS component (TRTYPE="WCS"), then this parameter controls whether or
not the WCS component should be located in each of the NDFs. If set
FALSE, the WCSFILE parameter will be used.
If NDFNAMES is TRUE and the transformation is to be specified using a
TRANSFORM structure (TRTYPE="STRUCT") then this parameter controls
whether or not the structure should be located in the CCDPACK
extension of each of the NDFs. If set FALSE, the TRANSFORM parameter
will be used.
If this option is chosen then the WCS component or transform structure
in EACH NDF will be applied to the associated position list. So for
instance if you have a set of registered NDFs and positions these may
be transformed all at once to and from the reference coordinate
system. [TRUE]



INLIST = LITERAL (Read)
```````````````````````
This parameter is used to access the names of the lists which contain
the positions and, if NDFNAMES is TRUE, the names of the associated
NDFs. If NDFNAMES is TRUE the names of the position lists are assumed
to be stored in the extension of the NDFs (in the CCDPACK extension
item CURRENT_LIST) and the names of the NDFs themselves should be
given in response (and may include wildcards).
If NDFNAMES is FALSE then the actual names of the position lists
should be given. These may not use wildcards but may be specified
using indirection (other CCDPACK position list processing routines
will write the names of their results files into a file suitable for
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



NAMELIST = _FILENAME
````````````````````
Only used if NDFNAMES is FALSE. This specifies the name of a file to
contain a listing of the names of the output lists. This file may then
be used to pass the names onto another CCDPACK application using
indirection. [TRANLIST.LIS]



NDFNAMES = _LOGICAL (Read)
``````````````````````````
If TRUE then the routine will assume that the names of the position
lists are stored in the NDF CCDPACK extensions under the item
"CURRENT_LIST". The names will be present in the extension if the
positions were located using a CCDPACK application (such as FINDOBJ).
Using this facility allows the transparent propagation of position
lists through processing chains.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [TRUE]



OUTLIST = FILENAME (Write)
``````````````````````````
A list of names specifying the result files. The names of the lists
may use modifications of the input names (NDF names if available
otherwise the names of the position lists). So if you want to call the
output lists the same name as the input NDFs except to add a type use.
OUTLIST > *.FIND
If no NDF names are given (NDFNAMES is FALSE) then if you want to
change the extension of the files (from ".CENT" to ".TRAN" in this
case) use
OUTLIST > *|CENT|TRAN|
Or alternatively you can use an explicit list of names. These may use
indirection elements as well as names separated by commas.



PA-PZ = _DOUBLE (Read)
``````````````````````
These parameters supply the values of constants used in the
expressions XFOR and YFOR. Using parameters allows the substitution of
repeated constants (with extended precisions?) using one reference. It
allows easy modification of parameterised expressions (expressions say
with an adjustable centre) provided the application has not been used
to apply a new transform using expressions. The parameter PI has a
default value of 3.14159265359D0. An example of using parameters is:
XFOR > SQRT(FX*FX+FY*FY) YFOR > ATAN2D(-FY,FX) FX > X-PA FY > Y-PB PA
> X-centre-value PB > Y-centre-value This maps (X,Y) to (R,THETA)
about a specified centre.



TRTYPE = LITERAL (Read)
```````````````````````
The form of the transformation which is to be applied to the positions
in the input lists. This can take the values


+ COEFF
+ EXPRES
+ WCS
+ STRUCT

or unique abbreviations of.
COEFF means that a linear transformation of the form X' = A + B*X +
C*Y Y' = D + E*X + F*Y is to be applied to the data. In this case a
prompt for the values of the coefficients A-F is made.
EXPRES indicates that you want to supply algebraic-like expressions to
transform the data. In this case the parameters XFOR and YFOR are used
to obtain the expressions. Things like XFOR > 2.5*COS(X)+LOG10(Y) YFOR
> 2.5*SIN(X)+EXP(Y) are allowed. The expression functions must be in
terms of X and Y. For a full set of possible functions see SUN/61
(TRANSFORM).
WCS means that the transformation will be taken from the WCS component
of an NDF. In this case the name of the NDF containing the WCS
component should be supplied (this will be picked up automatically
through the association of an NDF and a position list if NDFNAMES and
INEXT are both TRUE). The transformation will be that between the
coordinate systems defined by the FRAMEIN and FRAMEOUT parameters.
STRUCT signifies that a transform structure (probably created by
REGISTER or CCDEDIT) is to be applied to the data. In this case the
name of the object containing the structure should be supplied (this
will be picked up automatically through the association of an NDF and
a position list if NDFNAMES and INEXT are both TRUE) and whether to
use the forward or inverse mappings (the FORWARD parameter). [COEFF]



TR( 6 ) = _DOUBLE (Read)
````````````````````````
If TRTYPE="COEFF" is chosen then the values of this parameter are the
6 coefficients of a linear transformation of the type. X' = PA + PB*X
+ PC*Y Y' = PD + PE*X + PF*Y The default is the identity
transformation. [0,1,0,0,0,1] [PA,PB,PC,PD,PE,PF]



TRANSFORM = TRN (Read)
``````````````````````
If TYPE="STRUCT" and INEXT=FALSE then this parameter is used to access
the HDS object which contains the transform structure. The standard
place to store a transform structure (in CCDPACK) is


+ NDF_NAME.MORE.CCDPACK.TRANSFORM

Only one structure can be used at a time.



WCSFILE = NDF (Read)
````````````````````
If TRTYPE="WCS" and INEXT is false, then this parameter gives the name
of the NDF containing the WCS component containing coordinate systems
to be used for the transformation.



XFOR = LITERAL (Read)
`````````````````````
If TRTYPE="EXPRES" is chosen then this parameter specifies the
transformation that maps to the new X coordinate. The expression can
contain constants, arithmetic operators (+,-,/,*,**) and the functions
described in SUN/61 (SIN,COS,TAN, etc.).
As an inverse mapping is not required in this application there is no
need to use the X'=func(X,Y) form only func(X,Y) is required, however,
the variables must be given as "X" and "Y".



YFOR = LITERAL (Read)
`````````````````````
If TRTYPE="EXPRES" is chosen then this parameter specifies the
transformation that maps to the new Y coordinate. The expression can
contain constants, arithmetic operators (+,-,/,*,**) and the functions
described in SUN/61 (SIN,COS,TAN, etc.).
As an inverse mapping is not required in this application there is no
need to use the Y'=func(X,Y) form only func(X,Y) is required, however,
the variables must be given as "X" and "Y".



Examples
~~~~~~~~
tranlist inlist='*' outlist='*.reg' trtype=wcs framein=pixel
In this example all the NDFs in the current directory are accessed and
their associated position lists are opened. The WCS component of each
NDF is used to transform the coordinates in the position lists from
pixel coordinates to coordinates in the Current coordinate system. The
output lists are called ndf-name.reg and are associated with the NDFs.
tranlist inlist='*' outlist='*.tran' trtype=struct forward=false
In this example transform structures in each of the NDFs in the
current directory are used to transform their associated position
lists. The inverse mappings are used.
tranlist inlist='*_reduced' outlist='*.off' trtype=coeff
tr='[10,1,0,20,0,1]' In this example the position lists associated
with the NDFs *_reduced are transformed using the linear fit
coefficients [10,1,0,20,0,1] resulting in a shift of all the positions
in these lists of +10 in X and +20 in Y. The output lists are called
ndf_name.off and are now associated with the NDFs.
tranlist inlist='*_resam' outlist='*.rot' trtype=coeff
tr='[0,0.707,-0.707,0,0.707,0.707]' In this example a linear
transformation is used to rotate the positions by 45 degrees about
[0,0]. The linear coefficients for a rotation are specified as [0,
cos, -sin, 0, sin, cos].
tranlist inlist=here outlist=reflected.dat trtype=express
xfor=-x yfor=-y In this example a transformation expression is used to
reflect the positions stored in the list associated with NDF here
about the X and Y axes. A similar effect could be achieved with
trtype=coeff and tr=[0,-1,0,0,0,-1].
tranlist inlist=ndf_with_list outlist='*.tran' trtype=express
xfor='(fx*(1d0+pa*(fx*fx+fy*fy)))*ps+px'
yfor='(fy*(1d0+pa*(fx*fx+fy*fy)))*ps+py' fx='(x-px)/ps' fy='(y-py)/ps'
pa=pincushion_distortion_factor px=X-centre-value py=Y-centre-value
ps=scale_factor In this example a general transformation (which is of
the type used when applying pin cushion distortions) is applied to the
position list associated with the NDF ndf_with_list. The
transformation is parameterised with an offset and scale (converts
pixel coordinates to one projection radius units) applied to the input
coordinates and a pincushion distortion parameter pa.
tranlist ndfnames=false inlist='"list1,list2,list3"'
outlist='"outlist1,outlist2,outlist3"' namelist=newfiles In this
example the input position lists are not associated with NDFs
(ndfnames=false) And have to be specified by name (no wildcards
allowed). The output lists are also specified in this fashion, but,
the same effect could have been achieved with outlist=out* as the
input list names are now used as as modifiers for the output list
names (the NDF names are always used when they are available -- see
previous examples). The names of the output lists are written to the
file newfiles, this could be used to specify the names of these files
to another application using indirection (e.g inlist=^newfiles, with
ndfnames=false again). The transformation type is not specified in
this example and will be obtained by prompting.



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
names of the lists whose positions are to be transformed. On exit this
item will be updated to reference the name of the transformed list of
positions.
This application may also access the item "TRANSFORM" from the NDF
extensions if NDFNAMES and INEXT are TRUE and TRTYPE="STRUCT".


+ In this application data following the third column are copied
  without modification into the results files.




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
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995, 1997, 1999-2001 Central Laboratory of the Research Councils.
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


