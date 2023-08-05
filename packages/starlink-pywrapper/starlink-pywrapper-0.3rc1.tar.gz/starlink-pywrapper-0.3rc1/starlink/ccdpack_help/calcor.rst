

CALCOR
======


Purpose
~~~~~~~
Subtracts a scaled dark or flash calibration image from a series of
images


Description
~~~~~~~~~~~
CALCOR subtracts dark or flash calibration data from a series of bias-
corrected images. The calibration data are multiplied by a constant
before subtraction, so that calibration data which have been
normalised to counts per unit of time per pixel, can be scaled to the
"exposure" times suitable for correcting the input data. If the
calibration frame data levels are already correct to perform the
necessary correction then the data should be scaled by a factor of
one. In addition to subtracting the calibration data CALCOR also
processes saturated values protecting them from modification. This
protection is necessary if the saturated pixels are not to become
differentiated.


Usage
~~~~~


::

    
       calcor in out cal expose [preserve] [title]
       



ADAM parameters
~~~~~~~~~~~~~~~



CAL = LITERAL (Read)
````````````````````
Name of the image containing the calibration data, this would normally
be the output from MAKECAL. The data should be normalised to one
exposure unit. It is expected that the calibration image contains dark
or flash exposure CCD data which have been bias corrected.
If USESET is true, CAL should be a group expression referring to one
calibration frame matching each of the Set Index attributes
represented in the IN list; again the name of the file produced by
MAKECAL will normally be suitable.
The name of this file may be specified using indirection through a
file. [Global calibration image]



EXPOSE = LITERAL (Read)
```````````````````````
A list of (comma separated) values specifying the numbers by which the
calibration data need to be multiplied before subtraction from the
input data. These are the "exposure" factors for the dark counts
expected in the input data or the flash exposure times. If the
calibration data have been normalised to reflect the number of counts
per second of time, then this is the number of seconds of flash
exposure or the number of seconds duration between readouts, if it is
a dark counts image. If the calibration image has been produced so
that the correct levels are already present, then these values should
be returned as one. A quick method of specifying that all the images
have the same "exposure" factors is to return a single value, this
will then be used for all input images.
The given values must be in the same order as the input images.
Indirection through an ASCII file may be used. If more than one line
is required to enter the information then a continuation line may be
requested by adding "-" to the end of the last value.



IN = LITERAL (Read)
```````````````````
Names of the images to be processed. The calibration data will be
scaled and subtracted from these. The image names should be separated
by commas and may include wildcards.
NOTE the use of wildcards with this program is NOT recommended unless
the input images all have the same calibration exposure factors. The
processing order of any wildcarded images cannot be guaranteed.



KEEPIN = _LOGICAL (Read)
````````````````````````
Whether to keep (i.e. not delete) the input images (parameter IN) or
not. Deleting the input images has the advantage of saving disk space,
but should probably only be used if this program is part of a sequence
of commands and the intermediary data produced by it are not
important.
The calibration master frame (parameter CAL) is never deleted.
The default for this parameter is TRUE and this cannot be overridden
except by assignment on the command line or in reponse to a forced
prompt. [TRUE]



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



OUT = LITERAL (Read)
````````````````````
Names of the output images. These may be specified as list of comma
separated names, using indirection if required, OR, as a single
modification element (of the input names). The simplest modification
element is the asterisk "*" which means call each of the output images
the same name as the corresponding input images. So, IN > * OUT > *
signifies that all the images in the current directory should be used
and the output images should have the same names.
Other types of modification can also occur, such as, OUT > tmp_* which
means call the output images the same as the input images but put tmp_
in front of the names. Replacement of a specified string with another
in the output file names can also be used, OUT >
tmp_*|debias|flattened| this replaces the string debias with flattened
in any of the output names tmp_*.
NOTE the use of wildcards with this program is not recommended unless
the input images all have the same calibration exposure factors. The
order of processing of any wildcarded images cannot be guaranteed.



PRESERVE = _LOGICAL (Read)
``````````````````````````
If the input data type is to be preserved and used for processing then
this parameter should be set TRUE. If this parameter is set FALSE then
the input data will be processed and returned in a suitable floating
point representation. This option is useful if the output data will
have a significant number of BAD values due to numeric errors (over or
under flow), or if unacceptable loss of precision will occur if the
data are processed in their initial data type (due to rounding
errors).
Note if a global value for this parameter has been set, using
CCDSETUP, then this will be used. [TRUE]



SATURATION = _DOUBLE (Read)
```````````````````````````
The data saturation value, if it has been applied. See SETSAT. [1.0D6]



SETSAT = _LOGICAL (Read)
````````````````````````
If the input data have had a saturation value applied then this
parameter should be given as TRUE. If the input data have been
processed within CCDPACK then the saturation value will have been
stored within the CCDPACK extension, if this is so then this value
will be used. Note that data with different saturation properties
(i.e. values) which have not been set within CCDPACK will require
separate processing (i.e. in groups with the same properties -- see
notes). [FALSE]



TITLE = LITERAL (Read)
``````````````````````
Title for the output images. [Output from CALCOR].



USESET = _LOGICAL (Read)
````````````````````````
Whether to use Set header information or not. If USESET is false then
any Set header information will be ignored. If USESET is true, then
the CAL parameter is taken to refer to a group of files, and each IN
file will be processed using a calibration image with a Set Index
attribute which matches its own. An IN file with no Set header is
considered to match a CAL file with no Set header, so USESET can
safely be set true when the input files contain no Set header
information.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



Examples
~~~~~~~~
calcor frame1 frame2 calibration 250
This example runs CALCOR in its most basic mode. The input data in
image frame1 has the data in image calibration subtracted, after
multiplying by 250. The resultant data is written to image frame2.
Note that if saturation values have been applied to the data in frame1
within CCDPACK, then this will be handled automatically. The output
data will be of the same type as the input data.
calcor in=^frames.dat out='*_darksub' cal=dark_master
expose=^dark_exposures In this example a list of images are
sequentially processed. The list of image names is stored in the file
frames.dat. The output images are named after the corresponding input
image with the characters _darksub appended. The dark times for each
input frame are read from the file dark_exposures. This is the
recommended method for processing lists of input images.
calcor l1551_f11 l1551_f11_ds dark_master 1.0 preserve=false
logto=both logfile=l1551_darkcor.log title=dark_corrected_data This
example follows a similar theme to the first example, except that the
output data type is now _REAL or _DOUBLE, depending on the precision
required to process the data. The calibration correction data are
assumed to have the right exposure factor. The output image is given
the title "dark_corrected_data" and the parameters used by CALCOR are
stored in the logfile l1551_darkcor.log.
calcor in=ngc4151r_f1 cal=flash_master out=ngc4151r_f1_dc
expose=310.0 setsat saturation=32767 In this example a saturation
value external to CCDPACK has been applied to the input image. This is
indicated by setting SETSAT TRUE and by supplying the saturation
value. Values which are greater than or equal to the saturation value
are left unmodified by the calibration frame subtraction. This may
leave the saturated values "displaced" from the local values, causing
a discontinuity in the local isophotes, but is the only method by
which the saturated pixels may still be readily identified after the
subtraction of the calibration frame.



Notes
~~~~~


+ If any of the input data have had their saturation values set by
  applications not within CCDPACK, then this routine will require the
  saturation value which has been used if the values are to be
  propagated properly. If more than one saturation value has been used
  then the input frames will need to be processed singly. This is
  because CALCOR only uses one saturation value per input group. If the
  saturation values have been set within CCDPACK (by DEBIAS) these will
  be processed correctly and may be different.




Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ TITLE -- always "Output from CALCOR"
+ KEEPIN -- always TRUE

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new
datasets/different devices, or after a break of sometime. The
intrinsic default behaviour of the application may be restored by
using the RESET keyword on the command line.
Certain parameters (LOGTO, LOGFILE, USESET, PRESERVE and CAL) have
global values. These global values will always take precedence, except
when an assignment is made on the command line. In general global
values may be set and reset using the CCDSETUP and CCDCLEAR commands,
however, the CAL parameter may only be set by a run of the application
MAKECAL.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1994 Science & Engineering Research Council.
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


+ Supports processing of all non-complex numeric types. BAD pixels are
  processed as are all NDF components.




