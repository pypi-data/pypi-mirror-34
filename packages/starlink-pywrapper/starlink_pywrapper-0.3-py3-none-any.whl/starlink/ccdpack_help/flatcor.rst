

FLATCOR
=======


Purpose
~~~~~~~
Divides a series of images by a flatfield


Description
~~~~~~~~~~~
This routine applies a flat field correction to a series of images. If
any of the input data have been flagged as saturated using a
saturation value (instead of being marked as BAD) then the saturation
values may be protected from modification.


Usage
~~~~~


::

    
       flatcor in out flat
       



ADAM parameters
~~~~~~~~~~~~~~~



FLAT = LITERAL (Read)
`````````````````````
Name of the image which contains the normalised (mean of one)
flatfield data. This should have been produced by a program such as
MAKEFLAT. The data should have a floating point HDS data type (_REAL
or _DOUBLE). If USESET is true, FLAT should be a group expression
referring to one flatfield data file matching each of the Set Index
attributes represented in the IN list; again the name of the file
produced by MAKEFLAT will normally be suitable. The name of this file
may be specified using indirection through a file. [Global flatfield]



IN = LITERAL (Read)
```````````````````
Names of the images containing the data which are to have the
flatfield correction applied. The image names should be separated by
commas and may include wildcards.



KEEPIN = _LOGICAL (Read)
````````````````````````
Whether to keep (i.e. not delete) the input images (parameter IN) or
not. Deleting the input images has the advantage of saving disk space,
but should probably only be used if this program is part of a sequence
of commands and the intermediary data produced by it are not
important.
The calibration master frame (parameter FLAT) is never deleted.
The default for this parameter is TRUE and this cannot be overridden
except by assignment on the command line or in response to a forced
prompt. [TRUE]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter then no logfile will be written, regardless of the value of
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

If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



OUT = LITERAL (Write)
`````````````````````
Names of the output images. These may be specified as list of comma
separated names, using indirection if required, or, as a single
modification element (of the input names). The simplest modification
element is the asterisk "*" which means call each of the output NDFs
the same name as the corresponding input images. So, IN > * OUT > *
signifies that all the images in the current directory should be used
and the output images should have the same names.
Other types of modification can also occur, such as, OUT > tmp_* which
means call the output images the same as the input images but put tmp_
in front of the names. Replacement of a specified string with another
in the output file names can also be used, OUT >
tmp_*|debias|flattened| this replaces the string debias with flattened
in any of the output names tmp_*.



SATURATION = _DOUBLE (Read)
```````````````````````````
The value at which the input data has been saturated. This is only
required if the saturation has been flagged using a non-BAD value.
[1.0D6]



SETSAT = _LOGICAL (Read)
````````````````````````
If the input data has had a saturation value applied then this value
should be set to TRUE. However, if the saturation has been applied
within CCDPACK then this will not be necessary as this information
will have been stored in the CCDPACK extension. Note that data with
different saturation properties (i.e. saturation values) which have
not been set within CCDPACK will require separate processing (see
notes). [FALSE]



PRESERVE = _LOGICAL (Read)
``````````````````````````
If the input data types are to be preserved and used for processing
then this parameter should be set TRUE [default]. If this parameter is
set FALSE then the input data will be processed and returned in a
suitable floating point representation. This option is useful if the
output data will have a significant number of BAD values due to
numeric errors (over or under flow), or if unacceptable loss of
precision will occur if the data are processed in the original data
type (due to rounding errors).
If a global value for this parameter has been set using CCDSETUP then
this will be used. [TRUE]



TITLE = LITERAL (Read)
``````````````````````
Title for the output images. [Output from FLATCOR]



USESET = _LOGICAL (Read)
````````````````````````
Whether to use Set header information or not. If USESET is false then
any Set header information will be ignored. If USESET is true, then
the FLAT parameter is taken to refer to a group of files, and each IN
file will be processed using a flatfield dataset with a Set Index
attribute which matches its own. An IN file with no Set header is
considered to match a FLAT file with no Set header, so USESET can
safely be set true (the default) when the input files contain no Set
header information.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



Examples
~~~~~~~~
flatcor frame1 frame1_f flatr
In this example the data in image frame1 are corrected for the
flatfield response stored in image flatr. The result of dividing
FRAME1 by flatr is written to image frame1_f. If a saturation value
has been applied to the data in frame1 then this will be automatically
accommodated by FLATCOR providing the saturation has been applied
within CCDPACK.
flatcor n4151r1 n4151r1f flatfield setsat=true saturation=32767
In this example the data have had a saturation value applied which has
not been recorded within CCDPACK and the required information has been
supplied.
flatcor in='*' out='*_flattened' flat=master_flatr
In this example all the images in the current directory are processed.
The resultant data are written to files with the same name as the
corresponding input images, but with the characters "_flattened"
appended to the filename.



Notes
~~~~~


+ If any of the input data have had their saturation values set by
  applications not within CCDPACK, then this routine will require this
  information if the values are to be propagated properly. If more than
  one saturation value has been used then the input frames will need to
  be processed singly. This is because FLATCOR only uses one saturation
  value per input group. If the saturation values have been set within
  CCDPACK (by DEBIAS) these will be processed correctly and may be
  different.




Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ TITLE -- always "Output from FLATCOR"
+ KEEPIN -- always TRUE

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new
datasets/different devices, or after a break of sometime. The
intrinsic default behaviour of the application may be restored by
using the RESET keyword on the command line.
Certain parameters (LOGTO, LOGFILE, PRESERVE, FLAT and USESET) have
global values. These global values will always take precedence, except
when an assignment is made on the command line. In general global
values may be set and reset using the CCDSETUP and CCDCLEAR commands,
however, the FLAT parameter may only be set by a run of the
application MAKEFLAT.


Copyright
~~~~~~~~~
Copyright (C) 1991-1992, 1994 Science & Engineering Research Council.
Copyright (C) 1995-1997, 1999-2001 Central Laboratory of the Research
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


+ Supports processing of all non-complex numeric types. BAD pixels are
  processed as are all NDF components.




