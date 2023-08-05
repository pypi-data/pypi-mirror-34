

REGISTER
========


Purpose
~~~~~~~
Determines transformations between lists of positions


Description
~~~~~~~~~~~
This routine determines the transformations between (labelled)
position lists. Six different types of transformation are available.
The first 5 are based on the linear transformation, the sixth being a
function defined by you. The linear transformations are based on the
mappings
X' = A + B*X + C*Y Y' = D + E*X + F*Y
and allow:

+ shift of origin
+ shift of origin and rotation
+ shift of origin and magnification
+ shift of origin, rotation and magnification (solid body)
+ or a full six parameter fit

The self defined transform can be any mapping given as an algebraic
expression (including functions) using the methods allowed by
TRANSFORM (SUN/61).
When determining linear transformations REGISTER allows many lists to
be processed at once performing a simultaneous registration of all the
lists. When using a self defined transform only two lists may be
registered at any time.
The results from REGISTER are reported via the logging system and then
coded as new coordinate systems attached to NDFs. Normally, the new
coordinate systems will be attached to the NDFs with which the lists
are associated, but if the lists are not associated with NDFs then
they can be attached to a named list of NDFs, or a single named one.
The new coordinate system is a copy of the Pixel coordinate system of
the refernce image, and so is guaranteed to be a sensible one in which
to resample. The resampling can be done by TRANNDF.


Usage
~~~~~


::

    
       register inlist fittype refpos
       



ADAM parameters
~~~~~~~~~~~~~~~



FA-FZ = LITERAL (Read)
``````````````````````
These parameters supply the values of "sub-expressions" used in the
expressions XFOR, YFOR, XINV and YINV. These parameters should be used
when repeated expressions are present in complex transformations. Sub-
expressions may contain references to other sub-expressions and the
variables (PA-PZ). An example of using sub-expressions is: XFOR >
PA*ASIND(FA/PA)*X/FA YFOR > PA*ASIND(FA/PA)*Y/FA XINV >
PA*SIND(FB/PA)*XX/FB YINV > PA*SIND(FB/PA)*YY/FB FA > SQRT(X*X+Y*Y) FB
> SQRT(XX*XX+YY*YY)
This parameter is only used when IFIT=6.



FITTYPE = _INTEGER (Read)
`````````````````````````
The type of fit which should be used when determining the
transformation between the input positions lists. This may take the
values

+ 1 -- shift of origin
+ 2 -- shift of origin and rotation
+ 3 -- shift of origin and magnification
+ 4 -- shift of origin, rotation and magnification (solid body)
+ 5 -- a full six parameter fit
+ 6 -- self defined function

If more than two position lists are provided, then only the values 1-5
may be used. [5]



FULL = _LOGICAL (Read)
``````````````````````
If FITTYPE=6 is chosen then this parameter value determines if a full
transformation is to be performed or not. If FALSE then you will only
be prompted for expressions for XFOR and YFOR and the inverse
transformation will remain undefined.
If TRUE then you will also be prompted for XINV and YINV in response
to which the inverse mappings for X' and Y' are required. Not
performing a full fit will affect the later uses of the
transformation. At present not providing an inverse mapping means that
image resampling (TRANNDF) may not be performed. [FALSE]



IN = LITERAL (Read)
```````````````````
If NDFNAMES is FALSE and PLACEIN is "EACH" then a list of NDF names in
which to store the WCS frames is required. This list of names must
correspond exactly to the order of the associated input lists. A
listing of the order of inputs is shown before this parameter is
accessed.
The NDF names may (although this is probably not advisable) be
specified using wildcards, or may be specified using an indirection
file (the indirection character is "^").



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



NDFNAMES = _LOGICAL (Read)
``````````````````````````
This parameter specifies whether the names of the input positions
lists are stored in the CCDPACK extensions of NDFs. If TRUE then the
INLIST parameter accesses a list of NDFs which are used to get the
associated positions lists. If FALSE then INLIST just accesses the
position list names directly.
If the names of the lists are stored in the CCDPACK NDF extension then
the new coordinate system is attached to the associated NDF.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [TRUE]



OUTDOMAIN = LITERAL (Read)
``````````````````````````
The transformation information is written as a new coordinate system
attached to the NDF. This parameter gives the label (domain) of the
new coordinate system. When the new coordinate system is added, any
previously existing one with the same Domain will be removed.
If PLACEIN is "SINGLE", then the new coordinate systems are all
attached to a single NDF. In this case the domains are OUTDOMAIN_1,
OUTDOMAIN_2, ....
The name is converted to upper case, and whitespace is removed.
[CCD_REG]



PA-PZ = LITERAL (Read)
``````````````````````
When FITTYPE is 6 these parameters are used for supplying initial
guesses at the values of the fit parameters. Normally the values of
these parameters are not critical, but occasionally the minimization
routine fails due to numeric problems (these are usually caused by
trig functions etc. which are given invalid values (outside +/-1
etc.)). [1.0D0]



PLACEIN = LITERAL (Read)
````````````````````````
If NDFNAMES is FALSE then this parameter specifies where you would
like to store the final transformation structures. The options are:

+ EACH -- attach them one per NDF in a set of NDFs
+ SINGLE -- attach them all to a single NDF

If the EACH option is chosen then you will have the option of
supplying the NDF names via the parameter IN. If the SINGLE option is
chosen then the name of an NDF should be given in response to the
WCSFILE parameter; if no NDF by this name exists, a new dummy one will
be created. [EACH]



REFPOS = _INTEGER (Read)
````````````````````````
The position within the list of inputs which corresponds to the list
to be used as the reference set. [1]



SIMPFI = _LOGICAL (Read)
````````````````````````
If FITTYPE=6 and FULL=TRUE, this gives the value of the mapping's
SimpFI attribute (whether it is legitimate to simplify the forward
followed by the inverse transformation to a unit transformation).
[TRUE]



SIMPIF = _LOGICAL (Read)
````````````````````````
If FITTYPE=6 and FULL=TRUE this gives the value of the mapping's
SimpIF attribute (whether it is legitimate to simplify the inverse
followed by the forward transformation to a unit transformation).
[TRUE]



TOLER = _DOUBLE (Read)
``````````````````````
The RMS tolerance in positions which is used to determine the best
fit. Adjust this value only if the input positions are specified in
coordinates with a higher accuracy or smaller units. [0.001]



USESET = _LOGICAL (Read)
````````````````````````
This parameter determines whether Set header information should be
used in the registration. If USESET is true, then REGISTER will try to
group position lists according to the Set Name attribute of the NDFs
to which they are attached. All lists coming from NDFs which share the
same (non-blank) Set Name attribute, and which have a CCD_SET
coordinate frame in their WCS component, will be grouped together and
treated by the program as a single position list. Images which have no
associated position list but are in the same Set as ones which are
successfully registered will have a suitable registration frame added
too, based on their Set alignment relation to the registered Set
member. Thus the assumption is made that the relative alignment of
images within a Set is already known and has been fixed.
If USESET is false, all Set header information is ignored. If NDFNAMES
is false, USESET will be ignored. If the input NDFs have no Set
headers, or if they have no CCD_SET frame in their WCS components, the
setting of USESET will make no difference.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



USEWCS = _LOGICAL (Read)
````````````````````````
This parameter specifies whether the coordinates in the position lists
should be transformed from Pixel coordinates into the Current
coordinate system of the associated NDF before use. It should normally
be set TRUE, in which case the transformation type set by the FITTYPE
parameter is the type which will be fit between the Current coordinate
systems of the NDFs. Otherwise the fit will be between the positions
in pixel coordinates.
This parameter is ignored if NDFNAMES is not TRUE. [TRUE]



WCSFILE = NDF (Read)
````````````````````
If PLACEIN is "SINGLE" then the value of this parameter gives the the
name of an NDF which will have the new coordinate systems attached to
it. They will be added with domains given by the OUTDOMAIN parameter
with '_1', '_2', ... appended. If the NDF named by this parameter does
not exist, a dummy one will be created.



XFOR = LITERAL (Read)
`````````````````````
If FITTYPE=6 then this parameter specifies the parameterised algebraic
expression to be used as the forward X transformation. The expression
may use all the functions specified in SUN/61 (TRANSFORM) as well as
the usual mathematical operators (+,-,*,/,**). Functions are
parameterised by the strings PA,PB,PC...PZ which are the values which
will be determined. The string must contain at least one reference to
either X or Y. So a possible return is PA+PB*X
which is the same as the linear X transformation which just applies an
offset and a scale factor.



XINV = LITERAL (Read)
`````````````````````
If FITTYPE=6 and FULL=TRUE then this parameter specifies the inverse X
transformation. The expression may use all the functions specified in
SUN/61 (TRANSFORM) as well as the usual mathematical operations
(+,-,*,/,**). Functions are parameterised by the strings PA,PB,PC...PZ
which are the values which will be determined. This expression must
contain a reference to either XX or YY. So a possible return is (XX-
PA)/PB
which is the same as the inverse linear X transformation for an offset
and scale.



YFOR = LITERAL (Read)
`````````````````````
If FITTYPE=6 then this parameter specifies the parameterised algebraic
expression to be used as the forward Y transformation. The expression
may use all the functions specified in SUN/61 (TRANSFORM) as well as
the usual mathematical operators (+,-,*,/,**). Functions are
parameterised by the strings PA,PB,PC...PZ which are the values which
will be determined. The string must contain at least one reference to
either X or Y. So a possible return is PC+PD*Y
which is the same as the linear Y transformation which just applies an
offset and a scale factor.



YINV = LITERAL (Read)
`````````````````````
If FITTYPE=6 and FULL=TRUE then this parameter specifies the inverse Y
transformation. The expression may use all the functions specified in
SUN/61 (TRANSFORM) as well as the usual mathematical operations
(+,-,*,/,**). Functions are parameterised by the strings PA,PB,PC...PZ
which are the values which will be determined. This expression must
contain a reference to either XX or YY. So a possible return is (YY-
PC)/PD
which is the same as the inverse linear Y transformation for an offset
and scale.



Examples
~~~~~~~~
register inlist='*' fittype=1
In this example all the NDFs in the current directory are accessed and
their associated position lists are opened. A global fit between all
the datasets is then performed which results in estimates for the
offsets from the first input NDF's position. These offsets are between
the Current coordinate systems of the NDFs. The results are then
attached as new coordinate systems, labelled 'CCD_REG', in the WCS
component of the NDFs. Actual registration of the images can then be
achieved by aligning all the NDFs in the CCD_REG domain using TRANNDF.
register inlist='*' fittype=5 outdomain=result-set1
This example works as above but this time the global transformations
are derived for a full 6-parameter linear fit (which allows offset,
rotation, magnification and shear). The results are coded as attached
coordinate systems labelled 'RESULT-SET1'.
register inlist='"myimage1,myimage2"' fittype=4 refpos=2
In this example a solid body fit is performed between the position
lists associated with the NDFs myimage1 and myimage2. The reference
positions are chosen to be those associated with myimage2, so that the
CCD_REG coordinates will be the same as the pixel coordinates of NDF
myimage2.
register inlist='"one,two"' fittype=6 xfor='pa+pb*x' yfor='pa+pb*y'
In this example the position lists associated with the NDFs one and
two are said to be related by the algebraic expressions "pa+pb*x" and
"pa+pb*y", which indicates that a single offset applies in both
directions and a single scale factor. A solution for the values PA and
PB is found using a general least-squares minimization technique.
Starting values for PA and PB can be given using the parameters PA and
PB. Since the fittype is 6, only two position lists may be registered
in the same run.
register inlist='"ndf1,ndf2"' fittype=6 xfor='pa+pb*x+pc*y+pd*x*y'
yfor='pe+pf*x+pg*y+ph*x*y' In this example a non-linear transformation
is fit between the positions associated with the NDFs ndf1 and ndf2.
This analysis may help in determining whether a 6-parameter fit is
good enough, or if you just want to transform positions. A problem
with proceeding with this transformation in a general fashion is
deriving the inverse as this is required if you want to perform image
resampling using TRANNDF (though the more specialised, and less
efficient, DRIZZLE can resample with only the forward transformation).
register ndfnames=false inlist='"list1.acc,list2.acc,list3.acc"'
fittype=3 placein=each in='"ndf1,ndf2,ndf3"' In this example the input
position lists are not associated with NDFs (ndfnames=false) and have
to be specified by name (no wildcards allowed). Since the position
lists are not associated with NDFs there is no natural home for the
new coordinate systems. In this example it has been decided to attach
the coordinate systems to a set of NDFs anyway. PLACEIN could also be
given as "SINGLE" in which case the coordinate systems would be
attached to a single NDF with Domain names CCD_REG_1, CCD_REG_2, ...



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
Files with EXTERNAL format may be used with this application but all
positions have to be present in all lists, no missing positions are
allowed.
In all cases, the coordinates in position lists are pixel coordinates.


+ NDF extension items.

If NDFNAMES is TRUE then the item "CURRENT_LIST" of the .MORE.CCDPACK
structure of the input NDFs will be located and assumed to contain the
names of the lists whose positions are to be used for registration.
On exit, a new coordinate frame with a Domain as given by the
OUTDOMAIN parameter will be inserted in the WCS component of the input
NDFs. Taken together these contain the registration information and
can be inspected using WCSEDIT.


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
Certain parameters (LOGTO, LOGFILE, NDFNAMES and USESET) have global
values. These global values will always take precedence, except when
an assignment is made on the command line. Global values may be set
and reset using the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995-2003 Central Laboratory of the Research Councils. All Rights
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


