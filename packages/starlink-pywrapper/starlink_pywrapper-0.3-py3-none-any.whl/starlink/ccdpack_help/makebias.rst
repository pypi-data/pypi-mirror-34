

MAKEBIAS
========


Purpose
~~~~~~~
Produces a master from a set of bias frames


Description
~~~~~~~~~~~
This routine processes a series of bias frames (stored in NDFs), so as
to produce a single "master bias" frame in which the noise levels are
reduced. This master bias frame can then be used to de-bias other CCD
frames (using DEBIAS). Using the given readout noise an, optional,
variance component may be produced for the output data. The use of a
variance component allows the effects of noise in bias subtraction to
be properly monitored.
MAKEBIAS also performs other functions during processing, such as
estimating the readout noise (which it displays for comparison with
the nominal value), estimating the data levels, zeroing the average
value of the input data before combination (to more closely follow any
drifts in the zero level) and also supports many different methods for
performing the bias-frame data combination. The combination methods
offer a mixture of very robust (median) to very efficient (mean)
estimators.


Usage
~~~~~


::

    
       makebias in out rnoise method  { alpha=?
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



GENVAR = _LOGICAL (Read)
````````````````````````
If TRUE then a variance component representative of the readout noise
will be generated. If FALSE then no variance component will be
generated. If a variance component is not generated then any future
estimates of variance made using the output NDF will be
underestimates, however, disk space savings can be made using this
option, if future error analyses are not important. If this parameter
is set FALSE then a readout noise estimate will not be requested.
If a global value has been set using CCDSETUP this value will be used,
and will be shown as the default. [FALSE]



IN = LITERAL (Read)
```````````````````
A list of NDF names which contain the raw bias frame data. The NDF
names should be separated by commas and may include wildcards.



KEEPIN = _LOGICAL (Read)
````````````````````````
Whether to keep (i.e. not delete) the input NDFs or not. Deleting the
input NDFs has the advantage of saving disk space, but since the NDFs
input to this routine are raw data files (rather than processed
intermediary files) they should be always be keep unless space
considerations are at a very high premium.
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
values which can be used when combining data. Note that the value used
for this parameter will not be corrected for zero pointing. Hence if
the output NDF is to be zeroed then the maximum value should be a
offset from zero (say some positive number 2 or 3 sigmas large). This
could be used as a form of sigma clipping if no variances are to be
generated.



METHOD = LITERAL (Read)
```````````````````````
The method to be used to combine the data components of the input
NDFs. This may be set to any unique abbreviation of the following:

+ MEAN -- Mean of the input data values
+ MEDIAN -- Weighted median of the input data values
+ TRIMMED -- An "alpha trimmed mean" in which a fraction alpha of the
values are removed from each extreme
+ MODE -- An iteratively "sigma clipped" mean which approximates to
the modal value
+ SIGMA -- A sigma clipped mean
+ THRESHOLD -- Mean with values above and below given limits removed
+ MINMAX -- Mean with the highest and lowest values removed
+ BROADENED -- A broadened median (the mean of a small number of
central values)
+ CLIPMED -- A sigma clipped median (like SIGMA except that the median
of the clipped values is used)
+ FASTMED -- Unweighted median of the input data values [MEDIAN]





MIN = _REAL (Read)
``````````````````
If METHOD = "THRESH" then this value defines the lower limit for
values which can be used when combining the data. Note that the value
used for this parameter will not be corrected for zero pointing. Hence
if the output NDF is to be zeroed then the minimum value should be a
offset from zero (say some negative number 2 or 3 sigmas large). This
could be used as a form of sigma clipping if no variances are to be
generated.



MINPIX = _INTEGER (Read)
````````````````````````
The minimum number of good (i.e. not BAD) pixels required to
contribute to the value of an output pixel. Output pixels not meeting
this requirement are set BAD. [1]



NITER = _INTEGER (Read)
```````````````````````
The number of refining iterations performed if METHOD = "MODE". [7]



OUT = LITERAL (Read)
````````````````````
Name of the output NDF. This has the master bias frame and the
estimated variances. If USESET is true and multiple Sets are
represented in the IN list, then this name will be used as the name of
an HDS container file containing one NDF for each Set Index value.
This name may be specified using indirection through a file.



PRESERVE = _LOGICAL (Read)
``````````````````````````
If TRUE then this indicates that the input data type is to be used for
processing. If not then the output type will either be _REAL or
_DOUBLE, the precision at which the combinations are performed.
If a global value has been set using CCDSETUP then this will be used.
[TRUE]



RNOISE = _DOUBLE (Read)
```````````````````````
The readout-noise standard deviation. This should be in the input data
units (ADUs). A value for this will be worked out for each frame and
reported at the end of the task. The average of these values is
reported immediately before this parameter is accessed and can be used
if a better estimate is not known. Note that the supplied estimate has
some resilience to large-scale structure in the input frames, but will
be incorrect if the input-frame backgrounds are severely sloped. If
variances are not generated then this value will not be accessed.
The value of this parameter may not be used if the USEEXT parameter is
TRUE and will not be used if GENVAR is FALSE (i.e. no variances are
being generated). If USEEXT is TRUE then readout noise values will be
extracted from the NDFs CCDPACK extensions. Only if a suitable value
is not present will the value associated with this parameter be used.
If a global value has been set up using CCDSETUP this value will be
used, and will be shown as the default. If USESET is true, a global
value specific to each image's Set Index value will be sought.
[Dynamically derived value]



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations to reject data at. Used for "MODE",
"SIGMA" and "CLIPMED" methods. For METHOD = "MODE" the standard
deviation is estimated from the population of values. For METHOD =
"SIGMA" and "CLIPMED" this value is the readout noise. [4]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF [Output from MAKEBIAS].



USEEXT = _LOGICAL (Read)
````````````````````````
If TRUE then the parameter RNOISE of this program will not be used and
the required values will be obtained from the CCDPACK extensions of
the input NDFs instead. This method can only be used if the NDFs have
been "imported" using the programs PRESENT or IMPORT. Typically it is
used when processing using CCDPACK's "automated" methods.
Values obtained from the CCDPACK extension are identified in the
output log by the presence of a trailing asterisk (*). [FALSE]



USESET = _LOGICAL (Read)
````````````````````````
Whether to use Set header information or not. If USESET is false then
any Set header information will be ignored.
If USESET is true, then input files will be considered in groups; a
separate master bias frame will be constructed for each group of
corresponding input frames (i.e. those sharing the same Set Index
attribute). If this results in multiple output master bias frames,
they will be written as separate NDFs into a single HDS container
file. If no Set header information is present in the input files, then
all the input files are combined together to form the master bias, so
USESET can usually be safely set to TRUE.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



ZERO = _LOGICAL (Read)
``````````````````````
Flag indicating whether the output master bias is to have a mean value
of zero or not. If TRUE the input data components are ZERO-ed before
combination, of the data. Note that if this option is chosen then it
will be necessary to offset the master bias to the data before
subtraction. This option is not allowed for unsigned input data type
(unless PRESERVE is FALSE) as zeroing will make around half the data
values invalid. [TRUE]



Examples
~~~~~~~~
makebias in='"b1,b2,b3,b4,b5"' method=median out=mbias rnoise=10
This forms a master bias from the data components of the NDFs b1-b5.
The combination mode chosen is the median. The output NDF is mbias
whose variance has values based on a readout noise of 10 data units.
Note the quotes when entering a comma separated list on the command
line.
makebias in=^bias_frames.lis out=master_bias
In this example the list of NDFs is read from the file
bias_frames.lis. This file may contain indirection to other files up
to a depth of 7.
makebias in='*' out=master_bias
In this example all the NDFs in the directory are used.



Notes
~~~~~


+ If a variance component is present it will not be propagated.




Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ RNOISE -- dynamic value (but see below)
+ TITLE -- always "Output from MAKEBIAS"
+ KEEPIN -- always TRUE

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new
datasets/different devices, or after a break of sometime. The
intrinsic default behaviour of the application may be restored by
using the RESET keyword on the command line.
Certain parameters (LOGTO, LOGFILE, RNOISE, GENVAR, PRESERVE and
USESET) have global values. These global values will always take
precedence, except when an assignment is made on the command line.
Global values may be set and reset using the CCDSETUP and CCDCLEAR
commands. If USESET is true then a global value of RNOISE specific to
the Set Index of each image will be used if one is available.
The parameter RNOISE will not be used if the USEEXT parameter is set
TRUE. In this case values will be obtained from the input NDFs CCDPACK
extensions.


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


+ The routine supports BAD pixels and all numeric data types except
  COMPLEX. All combinational arithmetic is performed using floating
  values. The UNITS, AXIS and TITLE components are correctly propagated.
  Any input variances are ignored.




