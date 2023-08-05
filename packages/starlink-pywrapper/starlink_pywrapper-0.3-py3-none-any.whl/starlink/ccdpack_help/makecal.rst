

MAKECAL
=======


Purpose
~~~~~~~
Produces a dark or pre-flash calibration NDF


Description
~~~~~~~~~~~
This routine performs the combination of a series of dark count or
pre-flash exposure frames. The input NDFs should have been bias
subtracted. The input data are divided by the exposure factors before
combination into a calibration "master", giving an output NDF whose
data represent one unit of the given exposure time per pixel. Thus the
calibration frame should be multiplied by the appropriate factor
before subtracting from other frames (i.e. by the dark time or the
flash-exposure time). This can be performed by CALCOR and should be
done prior to the production of a flatfield and flatfield correction.
The data combination methods give a mixture of very robust (median) to
very efficient (mean) methods to suit the data.


Usage
~~~~~


::

    
       makecal in expose out method { alpha=?
                                    { sigmas=? niter=?
                                    { niter=?
                                    { min=? max=?
       



ADAM parameters
~~~~~~~~~~~~~~~



ALPHA = _REAL (Read)
````````````````````
The fraction of extreme values to remove before combining the data at
any pixel. This fraction is removed from each extreme so can only take
a value in the range 0 to 0.5. Only used if METHOD="TRIMMED" [0.2]



EXPOSE = LITERAL (Read)
```````````````````````
Either: An exact number of exposure factors for the input NDFs. The
values must be in the same order as the input NDFs.
Or: A single value which applies to all the input NDFs.
Indirection through an ASCII file may be used to specify these values.
If more than one line is required at prompt time then a continuation
line may be requested by adding "-" to the end of the line.
This parameter will not be used if USEEXT is set TRUE.



IN = LITERAL (Read)
```````````````````
A list of NDF names which contain the calibration data. The NDF names
should be separated by commas and may include wildcards.
NOTE the use of wildcards with this program is not recommended unless
the input NDFs all have the same calibration exposure factors. The
order of processing of any wildcarded NDFs cannot be guaranteed.



KEEPIN = _LOGICAL (Read)
````````````````````````
Whether to keep (i.e. not delete) the input NDFs or not. Deleting the
input NDFs has the advantage of saving disk space, but should probably
only be used if this program is part of a sequence of commands and the
intermediary data used by it are not important.
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



MAX = _REAL (Read)
``````````````````
If METHOD = "THRESH" then this value defines the upper limit for
values which can be used when combining the data. This limit applies
to the range of the output data (i.e. the values after the exposure
factors have been divided into the input data).



METHOD = LITERAL (Read)
```````````````````````
The method to be used to combine the data components of the input
NDFs. This may be set to any unique abbreviation of the following:

+ MEAN -- Mean of the input data values
+ MEDIAN -- Weighted median of the input data values
+ TRIMMED -- An "alpha trimmed mean" in which a fraction alpha/2 of
the values are removed from each extreme
+ MODE -- An iteratively "sigma clipped" mean which approximates to
the modal value
+ SIGMA -- A sigma clipped mean
+ THRESHOLD -- Mean with values above and below given limits removed
+ MINMAX -- Mean with the highest and lowest values removed
+ BROADENED -- A broadened median (the mean of a small number of
central values)
+ CLIPMED -- A sigma clipped median (like SIGMA except that the median
of the clipped values is used)
+ FASTMED -- Unweighted median of input data values [MEDIAN]





MIN = _REAL (Read)
``````````````````
If METHOD = "THRESH" then this value defines the lower limit for
values which can be used when combining the data. This limit applies
to the range of the output data (i.e. the values after the exposure
factors have been divided into the input data).



MINPIX = _INTEGER (Read)
````````````````````````
The minimum number of good (ie. not BAD) pixels required to contribute
to the value of an output pixel. Output pixels not meeting this
requirement are set BAD. [1]



NITER = _INTEGER (Read)
```````````````````````
The number of refining iterations performed if METHOD = "MODE". [7]



OUT = LITERAL (Write)
`````````````````````
Name of the output NDF to contain the calibration data. Note this NDF
will have a type of at least _REAL. If USESET is true and multiple
Sets are represented in the IN list then this name will be used as the
name of an HDS container file containing one NDF for each Set Index
value. This name may be specified using indirection through a file.



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations to reject data at. Used for "MODE",
"SIGMA" and "CLIPMED" methods. For METHOD = "MODE" the standard
deviation is estimated from the population of values, for METHOD =
"SIGMA" the variances are used. If no variances exist then a
population estimate is used. [4.0]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. [Output from MAKECAL]



USESET = _LOGICAL (Read)
````````````````````````
Whether to use Set header information or not. If USESET is false then
any Set header information will be ignored. If USESET is true, then
input files will be considered in groups; a separate calibration frame
will be constructed for each group of corresponding input frames (i.e.
those sharing the same Set Index attribute). If this results in
multiple output calibration files, they will be written as separate
NDFs into a single HDS container file. If no Set header information is
present in the input files, then calibration is done on all the input
files together, so USESET can usually be safely set to TRUE.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



TYPE = LITERAL (Read)
`````````````````````
The frame types of the input data. This should be a recognised name
"FLASH", "DARK" or "NONE". The value of this parameter affects the
output NDF frame type which will be set to "MASTER_FLASH" or
"MASTER_DARK" or "MASTER_?". [NONE]



USEEXT = _LOGICAL (Read)
````````````````````````
If TRUE then the EXPOSE parameter of this program will not be used and
the required values will be obtained from the CCDPACK extensions of
the input NDFs instead. This method can only be used if the NDFs have
been "imported" using the programs PRESENT or IMPORT. Typically it is
used when processing using CCDPACK's "automated" methods.
Values obtained from the CCDPACK extension are identified in the
output log by the presence of a trailing asterisk (*). [FALSE]



Examples
~~~~~~~~
makecal in='"f1,f2,f3,f4"' expose='"100,200,300,400"' method=median
out=master_flash This example forms a flash calibration NDF from the
data in NDFs f1,f2,f3 and f4. The data are divided by the relative
exposure factors before combination. The combination method used is
the (weighted) median, the resultant data are written to the NDF
master_flash.
makecal '"d1,d2,d3,d4"' 1 master_dark trimmed alpha=0.2
This example produces a dark-count-calibration frame from the data in
NDFs d1,d2,d3 and d4. The exposure factors are given as 1 which
probably indicates that the dark-exposure times in these datasets are
exactly right to correct any subsequent data frames. The combination
mode used is the trimmed mean with trimming fraction 0.2 and the
output data are written to NDF master_dark.
makecal ^flash_frames ^flash_exposures flash_master
In this example a list of frames to be processed is passed to the
program by indirection through an ASCII file flash_frames.dat, the
corresponding exposure times are passed from the file
flash_exposures.dat. This is probably the only safe method for
entering NDFs to this routine other than as in the above examples.
Using wildcards for the file specifications will mean that the
exposures cannot be associated correctly. Thus wildcards should not be
used except when the input NDFs have the same exposure times.



Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ TITLE -- always "Output from MAKECAL"
+ KEEPIN -- always TRUE

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new
datasets/different devices, or after a break of sometime. The
intrinsic default behaviour of the application may be restored by
using the RESET keyword on the command line.
Certain parameters (LOGTO, LOGFILE and USESET) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.
The parameter EXPOSE will not be used if the USEEXT parameter is set
TRUE. In this case the necessary values will be extracted from the
CCDPACK extensions of the input NDFs.


Copyright
~~~~~~~~~
Copyright (C) 1998 Central Laboratory of the Research Councils


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


+ The routine supports BAD pixels and all data types except COMPLEX.
  All combinational arithmetic is performed in floating point. The AXIS
  and TITLE components are correctly propagated. The variances are
  propagated through the combination processing, assuming that the input
  data have a normal distribution.




