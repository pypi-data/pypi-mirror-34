

CCDEDIT
=======


Purpose
~~~~~~~
Edits CCDPACK NDF extensions


Description
~~~~~~~~~~~
This routine provides the ability to edit the contents of the CCDPACK
extensions of a list of NDFs. The following modes of operation are
available:


+ associate position list(s)
+ erase extension items
+ add a transform structure
+ invert a transform structure.

The associate list facility allows the names of position lists to be
added to NDF extensions, these lists are then accessed when the NDF
names are given in response to an INLIST prompt (provided the
application NDFNAMES parameter is TRUE). This option also allows a
single position list to be associated with a range of NDFs.
Erase extension items is a safe way of deleting primitives and
structures from an NDF CCDPACK extension and removes the need to
remember the exact object name and path.
Add transform allows arbitrary transform structures to be added. The
transform may be generated from linear transform coefficients, copied
from a existing transform structure or may be specified as an
expression. Forward and inverse transformations are required.
Invert transform inverts the sense of the transformation.
Note that TRANSFORM structures are no longer (since version 3) widely
used in CCDPACK, so the TRANSFORM-structure manipulation options of
this command are unlikely to be very useful.


Usage
~~~~~


::

    
       ccdedit mode in
       



ADAM parameters
~~~~~~~~~~~~~~~



CLASS( ) = LITERAL (Read)
`````````````````````````
If CLASSIFY is TRUE then a list of classifications that describe the
properties of the transformation (parameters XFOR, YFOR, XINV and
YINV) should be given. This is optional, but the information can be
used to make other applications run more efficiently. Valid values
are:


+ LINEAR -- Linear and preserves straight lines.
+ INDEPENDENT -- Preserves the independence of the axes.
+ DIAGONAL -- Preserves the axes themselves.
+ ISOTROPIC -- Preserves angles and shapes.
+ POSITIVE_DET -- A component of reflection is absent.
+ NEGATIVE_DET -- A component of reflection is present.
+ CONSTANT_DET -- The scale factor is constant.
+ UNIT_DET -- Areas (or volumes etc.) are preserved.

See SUN/61 Appendix B for more details of transformation
classification and a table of the classifications of common mappings.



CLASSIFY = _LOGICAL (Read)
``````````````````````````
If TRTYPE="EXPRES" is chosen then this parameter decides whether or
not a classification of the transformation using parameters XFOR,
YFOR, XINV and YINV will be given. Classification is optional, but you
should note that the information can be used to make other
applications run more efficiently, and the lack of a classification
may stop certain types of operation. See SUN/61 appendix B for
details. Linear transformations are classified by this routine using
the FITTYPE parameter. [FALSE]



FA-FZ = LITERAL (Read)
``````````````````````
These parameters supply the values of "sub-expressions" used in the
expressions XFOR, YFOR, XINV and YINV. These parameters should be used
when repeated expressions are present in complex transformations. Sub-
expressions may contain references to other sub-expressions and
constants (PA-PZ). An example of using sub-expressions is: XFOR >
'XX=PA*ASIND(FA/PA)*X/FA' YFOR > 'YY=PA*ASIND(FA/PA)*Y/FA' XINV >
'X=PA*SIND(FB/PA)*XX/FB' YINV > 'Y=PA*SIND(FB/PA)*YY/FB' FA >
SQRT(X*X+Y*Y) PA > 100D0 FB > SQRT(XX*XX+YY*YY)



FITTYPE = _INTEGER (Read)
`````````````````````````
The type of fit specified by coefficients supplied via the TR
parameter. Appropriate values are.

+ 1 -- shift of origin
+ 2 -- shift of origin and rotation
+ 3 -- shift of origin and magnification
+ 4 -- shift of origin, rotation and magnification (solid body)
+ 5 -- a full six parameter fit

The value of this parameter is used to classify the transformation
(see the CLASS parameter). [5]



FIXWCS = _LOGICAL (Read)
````````````````````````
If MODE="ERASE" and NAME="SET", then this parameter indicates whether
the CCD_SET coordinate frame should be removed from the World
Coordinate System etension of the NDF as well. Since CCD_SET
coordinates are usually a copy of another coordinate system, and
mainly intended for Set-related registration, it is usually sensible
to erase this coordinate frame when the rest of the Set header
information has been erased. [TRUE]



IN = NDF (Read)
```````````````
A list specifying the names of the NDFs whose CCDPACK extensions are
to be modified. The NDF names should be separated by commas and may
include wildcards.



INLIST = LITERAL (Read)
```````````````````````
A list specifying one or more position list names (only used if MODE =
"ALIST" ). If a single name is given then this position list will be
associated with all the input NDFs. If a list of names is given then
there should be as many names as input NDFs. The order of the input
NDF names is shown so that the correct correspondence may be achieved.
Position list names may NOT include wildcards. So a comma separated
list of explicit names should be used and/or the names should be read
from indirection files (the indirection indicator is "^").



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



MODE = LITERAL (Read)
`````````````````````
The mode of operation. Can be one of

+ ALIST
+ ERASE
+ TRANSFORM
+ INVERT

The "ALIST" option "associates" a position list(s) with NDFs (this
sets the "CURRENT_LIST" item). This is useful when importing position
lists generated externally to CCDPACK.
The "ERASE" option removes a named item from NDF extensions. Two
possible items are "CURRENT_LIST" and "SET".
The "TRANSFORM" option allows the generation or import of transforms
into NDF extensions. Transforms from other NDFs may be copied. Linear
transforms may be generated from the (6) coefficients. General
transforms may be specified by algebraic-like expressions containing
the functions allowed by the TRANSFORM package (SUN/61). If you intend
to do this, see the related parameters (XFOR, YFOR, XINV, YINV, FA-FZ,
PA-PZ, CLASSIFY and CLASS) and the examples section.
The "INVERT" option inverts the sense of transformations in the NDFs.
[ALIST]



NAME = LITERAL (Read)
`````````````````````
If MODE = "ERASE" is chosen then the value of this parameter names the
CCDPACK extension item of the input NDFs which is to be erased.
Typical items are "CURRENT_LIST", "TRANSFORM" and "SET". If "SET" is
used, then the FIXWCS parameter will be used to decide whether to
remove any CCD_SET-domain frames from the WCS component.



PA-PZ = _DOUBLE (Read)
``````````````````````
These parameters supply the values of constants used in the
expressions XFOR, YFOR, XINV and YINV. Using parameters allows the
substitution of repeated constants (with extended precisions?) using
one reference. It also allows easy modification of parameterised
expressions (expressions say with an adjustable centre) provided the
application has not been used in the interim. The parameter PI has a
default value of 3.14159265359D0. An example of using parameters is:
XFOR > 'XX=SQRT(FX*FX+FY*FY)' YFOR > 'YY=ATAN2D(-FY,FX)' XINV >
'X=XX*SIND(YY)+PA' YINV > 'Y=-YY*COSD(XX)+PB' FX > X-PA FY > Y-PB PA >
X-centre-value PB > Y-centre-value This maps (X,Y) to (R,THETA) about
a specified centre.



TRANSFORM = TRN (Read)
``````````````````````
If TRTYPE="STRUCT" is chosen then this parameter is used to access the
HDS object which contains a transform structure to copy into the input
NDFs. The standard place to store a transform structure (in CCDPACK)
is


+ NDF_NAME.MORE.CCDPACK.TRANSFORM





TR( 6 ) = _DOUBLE (Read)
````````````````````````
If TRTYPE="COEFF" is chosen then the values of this parameter are the
6 coefficients of a linear transformation of the type. X' = PA + PB*X
+ PC*Y Y' = PD + PE*X + PF*Y The default is the identity
transformation. [0,1,0,0,0,1] [PA,PB,PC,PD,PE,PF]



TRTYPE = LITERAL (Read)
```````````````````````
If MODE = "TRANSFORM" is selected then this parameter specifies the
type of transform which will be supplied. Valid returns are

+ COEFF
+ EXPRES
+ STRUCT

If "COEFF" is chosen then the transform will be generated from the 6
coefficients of the equations. X' = PA + PB*X + PC*Y Y' = PD + PE*X +
PF*Y supplied in the order PA,PB,PC,PD,PE,PF.
If "STRUCT" is chosen then an existing transformation structure will
be copied into the extensions of the NDFs. Note that no checking of
the transform's validity will be made.
If "EXPRES" is chosen then the transformation will be specified using
algebraic-like statements of the type. XFOR > 'XX=PA+PC*X' YFOR >
'YY=PD+PE*Y' XINV > 'X=(XX-PA)/PC' YINV > 'Y=(YY-PD)/PE'
The values of PA-PZ are accessed through the PA-PZ parameters. The PA-
PZ's are reserved for constants (FA-FZ are also reserved for repeated
expressions). This example allows independent offsets and scales in X
and Y. The inverse transformation must be supplied. [COEFF]



XFOR = LITERAL (Read)
`````````````````````
If TRTYPE="EXPRES" is chosen then this parameter's value is the
transformation that maps to the new X coordinate. The expression can
contain constants, arithmetic operators (+,-,/,*,**) and the functions
described in SUN/61 (SIN,COS,TAN, etc.).
Constants may be specified using the special tokens PA-PZ. Prompts for
the values for these tokens will then be made (this provides a
mechanism for parameterising functions allowing trivial value
changes). Sub-expressions which occur in many places may also be
specified using the special tokens FA-FZ. These are prompted for and
placed into the main expression. Sub-expressions may contain
references to constants and other sub-expressions. An example
expression is: XFOR > 'XX=PA*ASIND(FA/PA)*X/FA' Note the single
quotes. They are necessary to protect the equals sign.



XINV = LITERAL (Read)
`````````````````````
If TRTYPE="EXPRES" is chosen then this parameter's value is the
transformation that maps to the old X coordinate - the inverse
transformation of XFOR. The expression can contain constants,
arithmetic operators (+,-,/,*,**) and the functions described in
SUN/61 (SIN,COS,TAN, etc.).
Constants may be specified using the special tokens PA-PZ prompts for
values for these tokens will then be made (this provides a mechanism
for parameterising functions allowing trivial values changes). Sub-
expressions which occur in many places may also be specified using the
special tokens FA-FZ. These are prompted for and placed into the main
expression. Sub-expressions may contain references to constants and
other sub-expressions. An example expression is: XINV >
'X=PA*SIND(FB/PA)*XX/FB' Note the single quotes. They are necessary to
protect the equals sign.



YFOR = LITERAL (Read)
`````````````````````
If TRTYPE="EXPRES" is chosen then this parameter's value is the
transformation that maps to the new Y coordinate. The expression can
contain constants, arithmetic operators (+,-,/,*,**) and the functions
described in SUN/61 (SIN,COS,TAN, etc.).
Constants may be specified using the special tokens PA-PZ. Prompts for
the values of these tokens will then be made (this provides a
mechanism for parameterising functions allowing trivial value
changes). Sub-expressions which occur in many places may also be
specified using the special tokens FA-FZ. These are prompted for and
placed into the main expression. Sub-expressions may contain
references to constants and other sub-expressions. An example
expression is: YFOR > 'YY=PA*ASIND(FA/PA)*Y/FA' Note the single
quotes. They are necessary to protect the equals sign.



YINV = LITERAL (Read)
`````````````````````
If TRTYPE="EXPRES" is chosen then this parameter's value is the
transformation that maps to the old Y coordinate - the inverse
transformation of YFOR. The expression can contain constants,
arithmetic operators (+,-,/,*,**) and the functions described in
SUN/61 (SIN,COS,TAN, etc.).
Constants may be specified using the special tokens PA-PZ. Prompts for
the values of these tokens will then be made (this provides a
mechanism for parameterising functions allowing trivial value
changes). Sub-expressions which occur in many places may also be
specified using the special tokens FA-FZ. These are prompted for and
placed into the main expression. Sub-expressions may contain
references to constants and other sub-expressions. An example
expression is: YINV > 'Y=PA*SIND(FB/PA)*YY/FB' Note the single quotes.
They are necessary to protect the equals sign.



Examples
~~~~~~~~
ccdedit mode=alist in='*' inlist=reference_set
This example shows how to "associate" a single position list called
reference_set with all the NDFs in the current directory.
ccdedit mode=alist in='"ndf1,ndf2,ndf3"'
inlist='"pos1.dat,pos2.dat,pos3.dat"' In this example the NDF ndf1 is
associated with pos1.dat, the NDF ndf2 with pos2.dat and the NDF ndf3
with pos3.dat.
ccdedit mode=erase in=ndf_with_bad_transform name=transform
In this example the TRANSFORM structure in the CCDPACK extension of
the NDF ndf_with_bad_transform is removed.
ccdedit mode=erase name=set fixwcs=yes in='*'
All Set header information, and any CCD_SET coordinate frames which
are associated with it, will be removed from the NDFs in the current
directory.
ccdedit mode=invert in='*'
In this example all the NDFs in the current directory have their
transforms inverted.
ccdedit mode=transform trtype=coeff in=shift_this_ndf
tr='[10.25,1,0,-101.1,0,1]' fittype=1 In this example the NDF
shift_this_ndf has a transform structure written into its CCDPACK
extension which specifies a shift of 10.25 in X and a negative shift
of 101.1 in Y. The shift is specified using the appropriate linear
transformation coefficients [XSHIFT,1,0,YSHIFT,0,1] and is correctly
classified as a fittype of 1.
ccdedit mode=transform trtype=coeff in=rotate_this_ndf
tr='[0,0.965926,-0.258819,0,0.258819,0.965926]' fittype=2 In this
example the NDF rotate_this_ndf has a transform structure written into
its CCDPACK extension which specifies a rotation by 15 degrees about
the [0,0] position. The rotation is specified using the appropriate
linear transformation coefficients [0,cos,-sin,0,sin,cos].
ccdedit mode=transform trtype=struct in=need_transform
transform=trn.more.ccdpack.transform In this example the
transformation structure trn.more.ccdpack.transform is copied to the
NDF need_transform.
ccdedit mode=transform trtype=expres in=map2gls
xfor='"xx=x*cosd(y)"' yfor='"yy=y"' xinv='"x=xx/cosd(yy)"'
yinv='"y=yy"' In this example the transform structure to be added to
NDF map2gls is defined as an algebraic expression. The mapping used is
a Sanson-Flamstead sinusoidal with X and Y in degrees.
ccdedit mode=transform trtype=express in=map2merc
xfor='"x=xx"'
yfor='"y=180/pi*log(tand((90d0+min(pa,max(-pa,yy))/2d0)))"'
xinv='"xx=x"' yinv='"2d0*(atand(exp(y*pi/180d0)))-90d0"' pa=89.9999d0
In this example a Mercator-like transform structure is added to the
NDF map2merc. The arguments to TAND are limited to the range +/-
89.9999D) to stop blow-up. The parameter PI is defaulted to
3.14159265359D0.



Notes
~~~~~


+ NDF extension items. All NDF extension items dealt with by this
routine are in the structure .MORE.CCDPACK.
+ When using the MODE=ALIST option the item CURRENT_LIST in the
CCDPACK extension of the input NDFs is set to the name of the input
list(s). Such NDF items may be used by other CCDPACK position list
processing routines to automatically access these lists.
+ When using the MODE=ERASE option the name of the item to be erase is
the name of the structure or primitive after the XXX.MORE.CCDPACK has
been removed.
+ Transforms are stored in the item .MORE.CCDPACK.TRANSFORM .
+ If MODE=ERASE, NAME=SET and FIXWCS=TRUE, the WCS component of the
  NDF may also be modified.




Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application after a break of
sometime. The intrinsic default behaviour of the application may be
restored by using the RESET keyword on the command line.
Certain parameters (LOGTO and LOGFILE) have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set and reset using
the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995, 1997, 2000-2001 Central Laboratory of the Research Councils.
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


