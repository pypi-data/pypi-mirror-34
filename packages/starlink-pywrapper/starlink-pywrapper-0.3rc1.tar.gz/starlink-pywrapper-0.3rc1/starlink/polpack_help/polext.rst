

POLEXT
======


Purpose
~~~~~~~
Sets explicit values in the POLPACK extension


Description
~~~~~~~~~~~
This application can be used to store information within the POLPACK
extensions of a group of data files so that they may subsequently be
processed with POLPACK. The values to store in the POLPACK extension
are supplied directly by the user in response to application parameter
prompts. If the required information is present within each data file
in the form of header cards in a FITS extension, then application
POLIMP may be used in place of POLEXT (POLIMP reads the required
values from the FITS extension instead of obtaining values from the
user).
New values for the POLPACK extension items are obtained using the
parameters described below. If supplied, these new values are stored
in the POLPACK extension items of the supplied data files. New POLPACK
extensions are created if necessary. If no new values are supplied for
an item, the existing item values (if any) are retained. The final
contents of the POLPACK extension are then listed. The values (on
exit) of the extension items in the last specified data file are
written to a set of output parameters.


Usage
~~~~~


::

    
       polext in
       



ADAM parameters
~~~~~~~~~~~~~~~



ANGROT = _REAL (Read)
`````````````````````
The anti-clockwise angle from the first (X) pixel axis of each image
to the polarimeter reference direction, in degrees. The supplied value
is not stored explicitly within the POLPACK extension. Instead, it is
used to create a new Frame within the WCS component of the NDF. This
Frame is given the Domain name POLANAL and its first axis corresponds
to the reference direction. If a null (!) value is supplied for this
parameter, any image which already has a POLANAL Frame retains the
existing Frame. Otherwise a POLANAL Frame is created using an ANGROT
value of zero (i.e. it is assumed that the reference direction
corresponds to the X pixel axis).
The reference direction depends on the type of polarimeter; in a
rotating half-wave plate polarimeter, it should correspond to the
direction of the fixed analyser; in polarimeters with multiple fixed
analysers or a single rotating analyser, it should correspond to the
direction specified by a zero value of ANLANG. [!]



ANLANG = _REAL (Read)
`````````````````````
Specifies the anti-clockwise angle in degrees from the reference
direction (established using the ANGROT parameter) to the analyser.
This parameter should only be used with polarimeters which have either
a rotating analyser or a set of fixed analysers. If your polarimetry
has a rotating half-wave plate instead, then you should use WPLATE
instead. The given value is stored in all supplied data files. If a
null (!) value is supplied, any image which already has an ANLANG
value retains its existing value, and any other images are left with
an undefined ANLANG value. [!]



EPS = _REAL (Read)
``````````````````
The analyser efficiency. This gives the efficiency with which the
analyser rejects light polarised across its axis. A perfect polariser
has a value of 1.0. A perfect piece of glass would have a value of
0.0. The stored value is used only when processing single-beam data.
The given value is stored in all supplied data files. If a null (!)
value is supplied, any image which already has an EPS value retains
its existing value, and any other images are left with an undefined
EPS value (this will cause a value of 1.0 to be used by POLCAL). [!]



FILTER = LITERAL (Read)
```````````````````````
The filter name. The value of extension item WPLATE or ANLANG
(whichever is available) is appended to the supplied filter value
before being stored, unless the filter value already contains the
WPLATE or ANLANG value. If a null (!) value is supplied, then any
existing FILTER value in the POLPACK extension is retained. If there
is no value in the POLPACK extension, then any value in the CCDPACK
extension is used instead. If there is no value in the CCDPACK
extension, then a default value equal to the value of WPLATE or ANLANG
is used. [!]



IMGID = LITERAL (Read)
``````````````````````
A group of image identifier strings. These are arbitrary strings used
to identify each original intensity frame. They are used when
processing dual-beam data to associate O and E ray images. They are
ignored when processing single-beam data. The supplied group may take
the form of a comma separated list of identifiers, or any of the other
forms described in the help on "Group Expressions". A separate, non-
blank identifier should be supplied for each data file specified by
parameter IN, in the same order as the data files. If a null (!) value
is supplied, then any existing IMGID values in the POLPACK extensions
are retained. Default values equal to the name of the data file are
used if there is no existing value. [!]



IN = LITERAL (Read)
```````````````````
A group of data files. This may take the form of a comma separated
list of file names, or any of the other forms described in the help on
"Group Expressions".



NAMELIST = LITERAL (Read)
`````````````````````````
The name of a file to create containing a list of the successfully
processed data files. This file can be used when specifying the input
data files for subsequent applications. No file is created if a null
(!) value is given. [!]



RAY = LITERAL (Read)
````````````````````
You should use this parameter only if the images contain either O or E
ray images obtained by a dual-beam polarimeter. You should not use
this parameter if your data is from a single-beam polarimeter, or if
the O and E ray images have not yet been extracted into separate
images. If used, the supplied value must be either "O" or "E". The
same value is stored in all supplied data files. If a null (!) value
is supplied, any existing RAY values are left unchanged, but no new
ones are added. [!]



STOKES = LITERAL (Read)
```````````````````````
You should use this parameter only if the supplied data files are 3D
cubes containing Stokes vectors. It should be a string in which each
character indicates the quantity stored in the corresponding plane of
the cube (I, Q, U or V). The length of the string should equal the
number of planes in the cube. If a null (!) value is supplied, any
existing STOKES values are left unchanged, but no new ones are added.
[!]



T = _REAL (Read)
````````````````
The analyser transmission. This gives the transparency of the analyser
to unpolarised light. A perfect polariser has a value of 1.0. A
perfect piece of glass would have a value of 2.0. The stored value is
only used when processing single-beam data. The given value is stored
in all supplied data files. If a null (!) value is supplied, any image
which already has a T value retains its existing value, and any other
images are left with an undefined T value (this will cause a value of
1.0 to be used by POLCAL). [!]



VANGROT = _REAL (Write)
```````````````````````
The ANGROT value stored in the last data file on exit will be written
to this output parameter.



VANLANG = _REAL (Write)
```````````````````````
The ANLANG value stored in the last data file on exit will be written
to this output parameter.



VEPS = _REAL (Write)
````````````````````
The EPS value stored in the last data file on exit will be written to
this output parameter.



VFILTER = LITERAL (Write)
`````````````````````````
The FILTER value stored in the last data file on exit will be written
to this output parameter.



VIMGID = LITERAL (Write)
````````````````````````
The IMGID value stored in the last data file on exit will be written
to this output parameter.



VRAY = LITERAL (Write)
``````````````````````
The RAY value stored in the last data file on exit will be written to
this output parameter.



VSTOKES = LITERAL (Write)
`````````````````````````
The STOKES value stored in the last data file on exit will be written
to this output parameter.



VT = _REAL (Write)
``````````````````
The T value stored in the last data file on exit will be written to
this output parameter.



VWPLATE = _REAL (Write)
```````````````````````
The WPLATE value stored in the last data file on exit will be written
to this output parameter.



VVERSION = LITERAL (Write)
``````````````````````````
The POLPACK version number which created the last data file will be
written to this output parameter.



WPLATE = _REAL (Read)
`````````````````````
The half-wave plate position, in degrees. Use parameter ANLANG if your
polarimeter does not have a half-wave plate. The given value is stored
in all supplied data files. If a null (!) value is supplied, any image
which already has an WPLATE value retains its existing value, and any
other images are left with an undefined WPLATE value. Note, when using
dual-beam data, Stokes vectors can only be calculated for WPLATE
values of 0.0, 22.5, 45.0 and 67.5. The POLCAL application will fail
if any other values are supplied. There are no such restrictions on
the value of WPLATE when using single-beam data. [!]



Examples
~~~~~~~~
polext in=cube
Displays the contents of the POLPACK extension of data file "cube",
leaving the values unchanged.
polext in=^files_0.txt wplate=0 filter=V angrot=45
This example processes all the data files listed in the text file
"files_0.txt", setting WPLATE to zero and ANGROT to 45. FILTER is set
to "V_0.0", and IMGID values are set to the name of the data file.



Notes
~~~~~


+ Errors are reported if the final POLPACK extension in a data file is
  illegal in any way.




Copyright
~~~~~~~~~
Copyright (C) 2009 Science & Technology Facilities Council. Copyright
(C) 1997-1999 Central Laboratory of the Research Councils All Rights
Reserved.


