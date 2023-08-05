

MAKEFLAT
========


Purpose
~~~~~~~
Produces a flatfield calibration NDF


Description
~~~~~~~~~~~
This routine combines a set of frames into a flatfield. The input data
should be of a photometrically flat source, and should be corrected
for any instrumental effects. The output calibration frame is
normalised to have an average value of one or can be left unnormalised
if a larger scaled normalisation is more appropriate (over a CCD
mosaic).
The input data are filtered in an attempt to remove any small
blemishes etc. before combination. This is achieved by smoothing using
a boxfilter and then comparing with the original data. An estimate of
the standard deviation of each pixel from its surroundings is made.
Pixels deviating by more than GAMMA standard deviations are rejected.
This procedure is then iterated ITER times. In this way, all image
features with a scale size comparable with, or smaller than, the
smoothing area size are rejected.


Usage
~~~~~


::

    
       makeflat in out method { alpha=?
                              { sigmas=?
                              { sigmas=? niter=?
                              { min=? max=?
       



ADAM parameters
~~~~~~~~~~~~~~~



ALPHA = _REAL (Read)
````````````````````
The fraction of extreme values to remove before combining the data at
any pixel. This fraction is removed from each extreme so can only take
a value in the range 0 to 0.5. Only used if METHOD="TRIMMED" [0.2]



BOXSIZE(2) = _INTEGER (Read)
````````````````````````````
The X and Y sizes (in pixels) of the rectangular box to be applied to
smooth the input images. If only a single value is given, then it will
be duplicated so that a square filter is used. The values given will
be rounded up to positive odd integers if necessary. The values should
be adjusted to be larger than the size of any expected defects.
[15,15]



CLEAN = _LOGICAL (Read)
```````````````````````
Whether or not to attempt to clean the input images of any defects.
For some data types (i.e. spectra) small scale strutures and sharp
edges may be real and can be protected against removal by setting this
parameter FALSE. [TRUE]



GAMMA = _REAL (Read)
````````````````````
The number of standard deviations by which a value has to deviate from
the local mean (defined by the mean within a box of BOXSIZE(1) by
BOXSIZE(2) pixels) before it is considered to be in error. Aberrant
pixels are removed from the data before the next "cleaning" iteration
is performed. [3.0]



GENVAR = _LOGICAL (Read)
````````````````````````
If TRUE and USEVAR is also FALSE, then "variances" for the output
image will be generated using the natural variation in the input
images. These values can be used to estimate the quality of the output
flatfield.
Note that for this option to work well you should have many images and
that any output pixels that only have one input image contributing to
their value will have their variances set bad. [FALSE]



IN = LITERAL (Read)
```````````````````
A list NDF names. These contain the flatfield data. The NDF names
should be separated by commas and may include wildcards.



ITER = _INTEGER (Read)
``````````````````````
The number of defect rejecting iterations. [3]



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
to the output data range.



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
+ FASTMED -- Unweighted median of input data values [MEDIAN]





MIN = _REAL (Read)
``````````````````
If METHOD = "THRESH" then this value defines the lower limit for
values which can be used when combining the data. This limit applies
to the output data range.



MINPIX = _INTEGER (Read)
````````````````````````
The minimum number of good (ie. not BAD) pixels required which are
required to contribute to the value of an output pixel. Output pixels
not meeting this requirement are set BAD. [1]



NITER = _INTEGER (Read)
```````````````````````
The number of refining iterations performed if METHOD = "MODE". [7]



NORM = _LOGICAL (Read)
``````````````````````
Whether to normalise the output NDF to have a mean of one. [TRUE]



OUT = LITERAL (Write)
`````````````````````
Name of an output file to contain the output flatfield data. Note that
output NDFs have a precision of at least _REAL. If USESET is true and
multiple Sets are represented in the IN list then this name will be
used as the name of an HDS container file containing one NDF for each
Set Index value. This name may be specified using indirection through
a file. [TRUE]



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations to reject data at. Used for "MODE",
"SIGMA" and "CLIPMED" methods. For METHOD = "MODE" the standard
deviation is estimated from the population of values. For METHOD =
"SIGMA" this value is the pixel variance if one exists, otherwise one
is estimated from the population of values. [4.0]



USESET = _LOGICAL (Read)
````````````````````````
Whether to use Set header information or not. If USESET is false then
any Set header information will be ignored. If USESET is true, then
input files will be considered in groups; a separate flatfield will be
constructed for each group of corresponding input frames (i.e. those
sharing the same Set Index attribute). If this results in multiple
output flatfields, they will be written as separate NDFs into a single
HDS container file. If no Set header information is present in the
input files, then flatfielding is done on all the input files
together, so USESET can usually be safely set to TRUE.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



USEVAR = _LOGICAL (Read)
````````````````````````
If TRUE and all the input images contain error information
(variances), then these will be used as weights during image
combination and will be propagated to the output image. [TRUE]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. [Output from MAKEFLAT]



Examples
~~~~~~~~
makeflat in='"f1,f2,f3,f4,f5"' method=median out=mflat
This forms a master flat field from NDFs f1 to f5. The input data are
first cleaned using the default values for the GAMMA and ITER
parameters. The combination mode chosen is the median. The output NDF
is mflat. Note the quotes when entering a comma separated list on the
command line.
makeflat in=^flat_frames.lis out=master_flat
In this example the list of NDFs is read from the file
flat_frames.lis. This file may contain indirection to other files up
to a depth of 7.
makeflat in='flatr/*' out='flatr/master_flat' gamma=2.5 iter=5
In this example all the NDFs in the subdirectory bias/ are used. The
input data are severely cleaned using a noise cut of 2.5 standard
deviations (current) and 5 iterations. Such severe cleaning is only
recommended when many input frames are given, if this is not the case
then BAD areas may be seen in the output NDF.
makeflat in='ff*' out=master_flat gamma=10 iter=1
In this example all the frames "ff*" are combined into a master
flatfield. Defect rejection is still performed but with gamma set so
high and by performing only one iteration almost no bad data will be
detected.



Notes
~~~~~


+ The data input into this routine should have bias strip regions and
any badly vignetted parts removed.
+ The input images are normalised to have a mean of one before being
  combined. This makes sure that all input images contribute to the
  final result (even though, for instance, they were taken on a source
  of varying brightness, e.g. the twilight sky).




Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ TITLE -- always "Output from MAKEFLAT"
+ KEEPIN -- always TRUE
+ NORM -- always TRUE

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
  All combinational arithmetic is performed using floating point. The
  AXIS and TITLE components are correctly propagated. The output is a
  ratio so the units are set to blank. The variances are propagated
  through the combination processing, assuming that the input data have
  a normal distribution.




