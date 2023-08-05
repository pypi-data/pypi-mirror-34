

PRESENT
=======


Purpose
~~~~~~~
Presents a list of NDFs to CCDPACK


Description
~~~~~~~~~~~
This routine enters reduction information into the CCDPACK extensions
of a list of NDFs. This information is required if an automated
reduction schedule is to be produced using SCHEDULE. Before using this
routine you should set up the CCDPACK global parameters, describing
the CCD characteristics, using the CCDSETUP application.
If the input NDFs have not already been categorised then this routine
performs this task for the "frame types" BIAS, TARGET, DARK, FLASH,
FLAT, MASTER_BIAS, MASTER_FLAT, MASTER_DARK and MASTER_FLASH (these
are input as different groups of NDFs).
Missing exposure times for DARK and FLASH counts can be entered as can
filter types.
This routine can also be used to check that a list of NDFs have the
minimum amount of information in their CCDPACK extensions to allow an
automated scheduling.


Usage
~~~~~


::

    
       present modify=? simple=? in=? bias=? target=? dark=? flash=?
               flat=? ftype=? filter=? darktime=? flashtime=?
       



ADAM parameters
~~~~~~~~~~~~~~~



ADC = _DOUBLE (Read)
````````````````````
The Analogue-to-Digital conversion factor. CCD readout values are
usually given in Analogue-to-Digital Units (ADUs). The ADC factor is
the value which converts ADUs back to the number of electrons which
were present in each pixel in the CCD after the integration had
finished. This value is required to allow proper estimates of the
inherent noise associated with each readout value. CCDPACK makes these
estimates and stores them in the variance component of the final NDFs.
Not supplying a value for this parameter (if prompted) may be a valid
response if variances are not to be generated.
This parameter normally accesses the value of the related CCDPACK
global association. This behaviour can only be superceded if ADC=value
is used on the command-line or if a prompt is forced (using using the
PROMPT keyword). The value of this parameter will be entered into the
extension of the input NDFs only if MODIFY is TRUE or the related
extension item does not exist. [!]



ADDDARK = _LOGICAL (Read)
`````````````````````````
Whether or not to prompt for a dark exposure time for the input NDFs
which require one. [Dynamic default, TRUE if dark count frames are
given, FALSE otherwise]



ADDFLASH = _LOGICAL (Read)
``````````````````````````
Whether or not to prompt for a pre-flash exposure time for the input
NDFs which require one. [Dynamic default, TRUE if pre-flash frames are
given, FALSE otherwise]



BIAS = LITERAL (Read)
`````````````````````
A list of the names of the NDFs which contain the raw bias data. These
are the NDFs which are to used to produce a "master" bias NDF. On exit
these NDFs will have their FTYPE extension item set to the value
"BIAS". [!]



BIASVALUE = _DOUBLE (Read)
``````````````````````````
If no raw bias frames exist and the data does not have any bias
strips, then the only way to remove the bias contribution is to
subtract a constant. If your data has already had its bias
contribution subtracted and you want to process it using CCDPACK (so
that you can generate variances for instance) then set this value to
zero. This parameter defaults to ! and is not prompted for so the only
way that a value can be supplied is on the command-line or by using
the PROMPT keyword. [!]



BOUNDS( 2 or 4 ) = _INTEGER (Read)
``````````````````````````````````
The bounds of the detector bias strips (if any exist). The bounds (if
given) should be in pixel indices and be given in pairs up to a limit
of 2. The sense of the bounds is along the readout direction. For
example, 2,16,400,416 means that the bias strips are located between
pixels 2 to 16 and 400 to 416 inclusive along the readout direction.
The bias strips are used to either offset the master bias NDF or as an
estimate of the bias which is to be interpolated across the NDF in
some way (see DEBIAS). Not supplying values for this parameter may be
a valid response if the bias frame is to be directly subtracted from
the data without offsetting or if a single constant is to be used as
the bias value for the whole NDF.
This parameter normally accesses the value of the related CCDPACK
global association. This behaviour can only be superceded if
BOUNDS=[value,...] is used on the command-line or if a prompt is
forced (using using the PROMPT keyword). The value of this parameter
will be entered into the extension of the input NDFs only if MODIFY is
TRUE or the related extension item does not exist. [!]



DARK = LITERAL (Read)
`````````````````````
A list of the names of the NDFs which contain the raw dark count data.
These are the NDFs which are to used to produce a "master" dark counts
NDF. On exit these NDFs will have their FTYPE extension item set to
the value "DARK". [!]



DARKTIME = _DOUBLE (Read)
`````````````````````````
The time for which the data in the current NDF collected dark count
electrons. The dark count is basically charge which accumulates in the
detector pixels due to thermal noise. The effect of dark current is to
produce an additive quantity to the electron count in each pixel. Most
modern devices only produce a few ADU (or less) counts per pixel per
hour and so this effect can generally be ignored. This, however, is
not the case for Infra-Red detectors.
The value given does not need to be a number of seconds or minutes and
can be ratio of some kind, as long as it is consistently used for all
NDFs (so if all your NDFs have the same darktime then the value 1
could be used). NDFs which have no dark count should be given a
DARKTIME of 0. This parameter is only used if ADDDARK is TRUE. [!]



DEFERRED = _DOUBLE (Read)
`````````````````````````
The deferred charge value. Often known as the "fat" or "skinny" zero
(just for confusion). This is actually the charge which is not
transferred from a CCD pixel when the device is read out. Usually this
is zero or negligible and is only included for completeness and for
processing very old data.
This parameter normally accesses the value of the related CCDPACK
global association. This behaviour can only be superceded if
DEFERRED=value is used on the command-line or if a prompt is forced
(using using the PROMPT keyword). The value of this parameter will be
entered into the extension of the input NDFs only if MODIFY is TRUE or
the related extension item does not exist. [!]



DIRECTION = LITERAL (Read)
``````````````````````````
The readout direction of the detector. This may take the values X or
Y. A value of X indicates that the readout direction is along the
first (horizontal) direction, an Y indicates that the readout
direction is along the direction perpendicular to the X axis.
This parameter normally accesses the value of the related CCDPACK
global association. This behaviour can only be superceded if
DIRECTION=value is used on the command-line or if a prompt is forced
(using using the PROMPT keyword). The value of this parameter will be
entered into the extension of the input NDFs only if MODIFY is TRUE or
the related extension item does not exist. [!]



EXTENT( 4 ) = _INTEGER (Read)
`````````````````````````````
The extent of the useful detector area in pixel indices. The extent is
defined as a range in X values and a range in Y values
(XMIN,XMAX,YMIN,YMAX). These define a section of an NDF (see SUN/33).
Any parts of the detector surface area outside of this region will not
be present in the final output. This is useful for excluding bias
strips, badly vignetted parts etc.
This parameter normally accesses the value of the related CCDPACK
global association. This behaviour can only be superceded if
EXTENT=[XMIN,XMAX,YMIN,YMAX] is used on the command-line or if a
prompt is forced (using using the PROMPT keyword). The value of this
parameter will be entered into the extension of the input NDFs only if
MODIFY is TRUE or the related extension item does not exist. [!]



FILTER = LITERAL (Read)
```````````````````````
The filter name associated with the current NDF. The filter name is
stored in the extension item FILTER and is used when determining which
flatfields should be used for which data. NDFs with a frame type which
is independent of the filter will not use this parameter. The filter
type is a case sensitive string. [Current value]



FLASH = LITERAL (Read)
``````````````````````
A list of the names of the NDFs which contain the raw pre-flash
correction data. These are the NDFs which are to used to produce a
"master" pre-flash correction NDF. On exit these NDFs will have their
FTYPE extension item set to the value "FLASH". [!]



FLASHTIME = _DOUBLE (Read)
``````````````````````````
The time for which the data in the current NDF was exposed to pre-
flash.
The value given does not need to be a number of seconds or minutes and
can be ratio of some kind, as long as it is consistently used for all
NDFs (so if all your NDFs have the same darktime then the value 1
could be used). NDFs which have no pre-flash should be given a
FLASHTIME of 0. This parameter is only used if ADDFLASH is TRUE. [!]



FLAT = LITERAL (Read)
`````````````````````
A list of the names of the NDFs which contain the raw flatfield data.
These are the NDFs which are to used to produce "master" flatfields
(one for each filter type). On exit these NDFs will have their FTYPE
extension item set to the value "FLAT". [!]



FTYPE = LITERAL (Read)
``````````````````````
The "frame" type of the current NDF. Each NDF is processed in turn and
if SIMPLE is TRUE and a frame type extension item does not exist then
this parameter will be used to prompt for a value. A prompt will also
be made if SIMPLE is TRUE and MODIFY is TRUE regardless of whether the
item already exists or not. If SIMPLE is FALSE then this parameter
will not be used. [Current value]



IN = LITERAL (Read)
```````````````````
A list of the names of the NDFs which contain the raw CCD data. NDFs
entered using this parameter must already have the correct "frame
type" information (extension item FTYPE) entered into their CCDPACK
extensions. This parameter is only used if SIMPLE is TRUE.
The NDF names should be separated by commas and may include wildcards.



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



MASTERBIAS = LITERAL (Read)
```````````````````````````
The name of a master bias frame. If this has been created by CCDPACK
then there is no need to present it. This parameter is designed for
the import of frames created by other packages. [!]



MASTERDARK = LITERAL (Read)
```````````````````````````
The name of a master dark counts frame. If this has been created by
CCDPACK then there is no need to present it (unless for some reason it
has been assigned the wrong frame type). This parameter is designed
for the import of frames created by other packages.



MASTERFLASH = LITERAL (Read)
````````````````````````````
The name of a master pre-flash frame. If this has been created by
CCDPACK then there is no need to present it (unless for some reason it
has been assigned the wrong frame type). This parameter is designed
for the import of frames created by other packages. [!]



MASTERFLAT = LITERAL (Read)
```````````````````````````
The names of a set of master flatfield frames (one for each filter
type used). If these have been created by CCDPACK then there is no
need to present them (unless for some reason they have been assigned
the wrong frame type or filter). This parameter is designed for the
import of frames created by other packages (such as those that
specifically process spectral data). [!]



MASTERS = _LOGICAL (Read)
`````````````````````````
If this parameter is TRUE then prompts will be made for all the master
calibration types (MASTERBIAS, MASTERDARK, MASTERFLAT and
MASTERFLASH). [FALSE]



MODIFY = _LOGICAL (Read)
````````````````````````
If the input NDFs already contain information in their CCDPACK
extensions, then this parameter controls whether this information will
be overwritten (if a new value exists) or not. [TRUE]



MULTIENTRY = _LOGICAL (Read)
````````````````````````````
Whether or not the names of the input NDFs, their frame types, filters
and related exposure factors are all given in response to the IN
parameter (SIMPLE must be TRUE). If this option is selected then the
parameters FTYPE, FILTER, DARKTIME and FLASHTIME will be set up with
these values as defaults. If MODIFY is TRUE then you will be given an
opportunity to modify them, otherwise these values will be entered
into the NDF CCDPACK extensions.
The input record format is five fields separated by commas. These are:


+ 1 NDF name
+ 2 Frame type
+ 3 Filter name
+ 4 Dark exposure time
+ 5 Flash exposure time

The latter three fields can be specified as "!" in which case they are
not set (they may not be relevant). Multiple records can be entered
and can be read in from a text file. So for instance if the file
"XREDUCE.NDFS" had the following as its contents:
DATA1,target,!,!,! DATA2,target,!,!,! DATA3,target,!,!,!
FF1,flat,!,!,! FF2,flat,!,!,! FF3,flat,!,!,! BIAS1,bias,!,!,!
BIAS2,bias,!,!,! BIAS3,bias,!,!,!
Then it would be invoked using parameters


+ SIMPLE MULTIENTRY IN=^XREDUCE.NDFS

This parameter is intended as an aid when using this program non-
interactively (i.e. from scripts) and shouldn't normally be used,
hence its default is FALSE and this can only be overridden by
assignment on the command line or in response to a forced prompt.
[FALSE]



NAMELIST = LITERAL (Read)
`````````````````````````
The name of a file to contain a listing of the name of the input NDFs.
This is intended to be of use when using these same names with other
applications (such as SCHEDULE). [!]



ONEDARKTIME = _LOGICAL (Read)
`````````````````````````````
If the input data have the same dark count exposure time then this
parameter may be set to inhibit repeated prompting for an exposure for
every frame. This parameter is of particular use when running from
scripts. [FALSE]



ONEFILTER = _LOGICAL (Read)
```````````````````````````
If the input data have only one filter type then this parameter may be
set to inhibit repeated prompting for a filter name for every frame
(that is filter dependent). This parameter is of particular use when
running from scripts. [FALSE]



ONEFLASHTIME = _LOGICAL (Read)
``````````````````````````````
If the input data have the same pre-flash exposure time then this
parameter may be set to inhibit repeated prompting for an exposure for
every frame. This parameter is of particular use when running from
scripts. [FALSE]



RNOISE = _DOUBLE (Read)
```````````````````````
The readout noise of the detector (in ADUs). Usually the readout noise
of a detector is estimated by the observatory at which the data was
taken and this is the value which should be supplied. Not supplying a
value for this parameter may be a valid response if variances are not
to be generated.
This parameter normally accesses the value of the related CCDPACK
global association (which is the readout noise value). This behaviour
can only be superceded if RNOISE=value is used on the command-line or
if a prompt is forced (using using the PROMPT keyword). The value of
this parameter will be entered into the extension of the input NDFs
only if MODIFY is TRUE or the related extension item does not exist.
[!]



SATURATION = _DOUBLE (Read)
```````````````````````````
The saturation value of the detector pixels (in ADUs).
This parameter normally accesses the value of the related CCDPACK
global association. This behaviour can only be superceded if
SATURATION=value is used on the command-line or if a prompt is forced
(using using the PROMPT keyword). The value of this parameter will be
entered into the extension of the input NDFs only if MODIFY is TRUE or
the related extension item does not exist. [!]



SIMPLE = _LOGICAL (Read)
````````````````````````
Whether or not the input NDFs already contain "frame type" (extension
item FTYPE) information in their CCDPACK extensions or not. Usually
NDFs to be presented to CCDPACK do not contain this information,
unless it has been imported from FITS information using IMPORT, or the
NDFs have already been presented and this pass is to modify existing
extension items. [FALSE]



TARGET = LITERAL (Read)
```````````````````````
A list of the names of the NDFs which contain the "target" data. These
are the NDFs which contain the images or spectra etc. On exit these
NDFs will have their FTYPE extension item set to the value "TARGET".
[!]



ZEROED = _LOGICAL (Read)
````````````````````````
If a master bias frame is given, then this parameter indicates whether
or not it has a mean value of zero. If SIMPLE and MULTIENTRY are TRUE
then this value (TRUE or FALSE) can be entered as the fourth field to
the IN parameter. [FALSE]



Examples
~~~~~~~~
present simple in='*' modify
In this example PRESENT processes all the NDFs in the current
directory. The NDFs should already have a valid frame type (such as
TARGET, FLAT etc.). The any existing global variables describing the
detector are accessed and written into the NDF extension overwriting
any values which already exist.
present simple=false bias='bias*' target='data*' dark=! flash=!
flat='ff*' In this example the input NDFs are organised into their
respective frame types using the specially designed input parameters.
On exit the output NDFs will have the correct frame types entered into
their CCDPACK extensions (provided MODIFY is TRUE).
present modify=false simple=true in='*'
In this example all the NDFs in the current directory are accessed. If
any required extension or global associated items are missing then
they will be entered into the NDF extension. If all extension items
are present then a listing of their values will be made.
present masters simple=false masterflat="2dspectraff"
In this example a master flatfield is imported to be used in an
automated reduction of spectral data.



Copyright
~~~~~~~~~
Copyright (C) 1992, 1994 Science & Engineering Research Council.
Copyright (C) 1995, 2000 Central Laboratory of the Research Councils.
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


