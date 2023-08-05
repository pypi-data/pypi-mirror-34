

SCHEDULE
========


Purpose
~~~~~~~
Schedules an automated CCDPACK reduction


Description
~~~~~~~~~~~
This routine accepts a list of input NDFs and uses the information in
their CCDPACK extensions to schedule a reduction. The schedule is
produced as a command script which may be executed immediately or
retained for execution using the standard CCDPACK facilities
(CCDFORK).
The reduction schedule produced covers the following stages of data
reduction (this is order).
1) production of a master bias 2) removal of the bias contribution 3)
production of a master dark 4) removal of dark count contribution 5)
production of a master pre-flash 6) removal of pre-flash contribution
5) production of master flatfields (one for each filter type) 6)
correction of data for flatfield response
The stages which are preformed for each NDF depend on the type of NDF
(TARGET, FLAT, BIAS, DARK etc.) and any processing which has already
taken place. For instance if calibration masters of any type already
exist then they will be used in preference to the production of any
new masters. If all the TARGET frames have already been flatfielded
then no further processing will be performed, if no BIAS frames of any
type exist then debiassing will be performed using bias strip
interpolation or by subtracting a single constant etc. Reductions
which have failed (due to a lack of resources) can be "picked up" and
restarted from the position at which they failed (by a re-invocation
of this routine). Facilities for controlling the use of disk space are
also available.
Before you can use this routine you must make sure that all the
necessary information is entered into the NDF extensions. You can do
this using the routines IMPORT or CCDSETUP and PRESENT or any
combination of these which give the desired effect.


Usage
~~~~~


::

    
       schedule in script stype debias=? execute=? interp=? spacesave=?
       



ADAM parameters
~~~~~~~~~~~~~~~



DARKEXT = LITERAL (Read)
````````````````````````
The extension which added to the names of any NDFs processed by CALCOR
when performing dark count correction. This makes the parameter
OUT=*"darkext"
form the names of the NDFs output from CALCOR. [-dk]



DEBIAS = _INTEGER (Read)
````````````````````````
The form of debiassing that should be used. This is an integer which
represents one of the following: 1 = produce a master and offset to
bias strips (master bias is zeroed) 2 = produce a master and do not
offset to strips (in this case the master bias is not zeroed) 3 = use
interpolation between bias strip(s) 4 = subtract a constant as bias.
Using the information about the frame types which are available and
the presence or not of bias strips etc. a list of the possible
debiassing options is shown, before this parameter is accessed. Any of
the above methods can be selected regardless of this advice, but the
reduction may then fail unless action is taken (such as adapting the
output script).
If the interpolation option is selected then the method is determined
by the INTERP parameter.



DEBIASEXT = LITERAL (Read)
``````````````````````````
The extension which added to the names of any NDFs processed by
DEBIAS. This makes the parameter
OUT=*"debiasext"
form the names of the NDFs output from DEBIAS. [-db]



EXECUTE = _LOGICAL (Read)
`````````````````````````
Whether to execute the output command script immediately or not. If
the option to execute is chosen then a background process is started
which performs the actual execution. Do not execute the procedure
using this method if your system supports a queuing system which
should be used instead (if you expect the reduction to take some
time). This option does not work for ICL scripts at this time. [FALSE]



EXELOGFILE = LITERAL (Read)
```````````````````````````
If the reduction is started immediately then the output will be
redirected to this file. [SCHEDULE.LOG]



FLASHEXT = LITERAL (Read)
`````````````````````````
The extension which added to the names of any NDFs processed by CALCOR
when performing pre-flash correction. This makes the parameter
OUT=*"flashext"
form the names of the NDFs output from CALCOR. [-dk]



FLATEXT = LITERAL (Read)
````````````````````````
The extension which added to the names of any NDFs processed by
FLATCOR. This makes the parameter
OUT=*"flatext"
form the names of the NDFs output from FLATCOR. [-flt]



IN = LITERAL (Read)
```````````````````
A list of the names of the NDFs which contain the data to be reduced.
All NDFs must already have the correct "frame type" information
(extension item FTYPE) entered into their CCDPACK extensions. Together
with any other relevant information (such as filter type, position of
the bias strips, useful area etc., see IMPORT and/or PRESENT).
The NDF names should be separated by commas and may include wildcards.



INTERP = _INTEGER (Read)
````````````````````````
If the interpolation method is chosen using the DEBIAS parameter then
this parameter controls how the interpolation should be performed. The
possible returns are:
1 = fit a constant for each row/column 2 = fit a single value for
whole NDF 3 = fit a line to each row/column 4 = fit a plane to whole
NDF
The possible options given the input information about the presence of
bias strips are shown before the value of this parameter is accessed.



IRFLATS = _LOGICAL (Read)
`````````````````````````
This parameter allows input frames of type TARGET to be also used as
flatfields. This is designed for use when no real flatfields exist. IR
data is often calibrated in this way, and less commonly optical data.
In both these cases it is asummed that the objects are moved on the
sky sufficiently, between exposures, so that taking the median of a
stack of frames results in the rejection of any object data (leaving
the equivalent of a map of a blank piece of sky).
TARGET frames will only be used to create flatfields, if no flatfields
(of the correct colour) are present in the input list. [FALSE]



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
+ NEITHER -- Produce no output at all If the logging system has been
  initialised using CCDSETUP then the value specified there will be
  used. Otherwise, the default is "BOTH". [BOTH]





MASTERBIAS = LITERAL (Read)
```````````````````````````
The name which will be given to a master bias NDF if one is created.
[MASTER_BIAS]



MASTERDARK = LITERAL (Read)
```````````````````````````
The name which will be given to a master dark NDF if one is created.
[MASTER_DARK]



MASTERFLASH = LITERAL (Read)
````````````````````````````
The name which will be given to a master flash NDF if one is created.
[MASTER_FLASH]



MASTERFLAT = LITERAL (Read)
```````````````````````````
The prefix of the name which will be given to any master flat NDFs
which are created. The filter name will be appended to this.
[MASTER_FLAT]



SCRIPT = LITERAL (Read)
```````````````````````
The name of the output file which will contain the CCDPACK commands
which need to be executed to perform the reduction. The nature of this
script is controlled by the STYPE parameter. The default name is
dynamically set to be SCHEDULE with a type set by the choice of STYPE.
The extension of the script name should always be the same as STYPE.
[schedule."stype"]



SPACESAVE = LITERAL (Read)
``````````````````````````
This parameter controls if any disk space management should be used or
not. It can take one of the values, "NONE", "SOME" or "LOTS".
"NONE" indicates that no NDFs should be deleted. "SOME" indicates that
all intermediate NDFs should be deleted. This occurs after they are
processed. "LOTS" indicates that all processed NDFs should be deleted.
In this case all intermediary NDFs and the original NDFs are deleted
when processed.
Intermediary NDFs are deleted by the CCDPACK applications when they
are finished processing then. So for instance in the case of FLATCOR
each NDF is deleted in turn, so the additional disk space required is
one NDF. Using "SOME" preserves the original NDFs. Calibration masters
are never deleted. [NONE]



STYPE = LITERAL (Read)
``````````````````````
The type of CCDPACK command procedure to be produced. This should be
one of "CSH" or "ICL". Once a type has been chosen the output script
(parameter SCRIPT) can only be executed using the selected
interpreter. Note that if you choose ICL then the resultant script
cannot be executed immediately, you must activate this yourself. [CSH]



Examples
~~~~~~~~
schedule '*' ccdreduce csh debias=1
This example processes all the NDFs in the current directory producing
a script file called ccdreduce.csh which is suitable for executing
from the C-shell. The debiassing method chosen is to use a zeroed
master bias which is offset to the bias strip data level.
schedule '*' ccdreduce csh debias=1 execute=true
As above except that the script ccdreduce.csh is forked into a
background process and executed. The output from this job will be
found in the file schedule.log.
schedule '*' tryinterp debias=3 interp=3
In this example the debiassing is performed using interpolation
between the bias strips.
schedule spacesave=lots
In this example the command script will be written so that all
intermediary NDFs (those produced by the various applications) and the
original raw NDFs, will be deleted as and when they are processed.
schedule 'data*' irflats debias=4
In this example the frames 'data*' are scheduled for reduction. The
debiassing method is subtraction of a constant (this should be set by
PRESENT) and a flatfield is produced by median stacking all the data
frames.



Copyright
~~~~~~~~~
Copyright (C) 1993-1994 Science & Engineering Research Council.
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


