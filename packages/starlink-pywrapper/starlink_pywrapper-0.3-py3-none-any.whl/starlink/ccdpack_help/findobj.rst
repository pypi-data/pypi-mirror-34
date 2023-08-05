

FINDOBJ
=======


Purpose
~~~~~~~
Locates and centroids image features


Description
~~~~~~~~~~~
This routine processes a list of NDFs, locating and centroiding image
features (such as stars) which have groups of connected pixels above
threshold values.
Connected groups of pixels are accepted as objects if they have more
than a minimum number of pixels. Such groups may be rejected if they
contact the edges of the data array.
Threshold estimation is performed using either a percentage data point
(i.e. the value for which this percentage of pixels have a lower
value) or by using a standard deviation and background value
determined by fitting a gaussian to the data histogram.


Usage
~~~~~


::

    
       findobj in minpix outlist
       



ADAM parameters
~~~~~~~~~~~~~~~



AUTOTHRESH = _LOGICAL (Read)
````````````````````````````
If this parameter is TRUE then a threshold determined by this routine
for each of the NDFs will be used. If FALSE then you will be prompted
for a threshold value for each NDF. [TRUE]



BINFRAC = _DOUBLE (Read)
````````````````````````
The minimum fraction of the image area (expressed as a percentage)
which is required in the peak bin when forming the histogram. Ensuring
that at least one bin contains this fraction of counts is intended to
make sure that the image histogram is well sampled. This increases the
robustness of mode estimates made from the histogram but decreases the
accuracy. Only used if USEPER is FALSE. [2.5]



COUNTS = _INTEGER (Write)
`````````````````````````
On exit this parameter contains a list of the number of objects
detected in each input image. This may be useful in scripts where the
values can be accessed using the KAPPA (SUN/95) PARGET command.



IN = LITERAL (Read)
```````````````````
A list of NDF names which contain the data components to be scanned
for image features. The NDF names should be separated by commas and
may include wildcards.



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



MINPIX = _INTEGER (Read)
````````````````````````
The minimum number of non-BAD pixels which must be present in a
connected group for acceptance as an image feature. [6]



NAMELIST = LITERAL (Read)
`````````````````````````
The name of a file to contain the names of the output position lists.
The names written to this file are those generated using the
expression given to the OUTLIST parameter. The file may be used in an
indirection expression to input all the position lists output from
this routine into another routine. [FINDOBJ.LIS]



NSIGMA = _DOUBLE (Read)
```````````````````````
The number of standard deviations above the background that should be
used as the threshold. This parameter is only accessed if the USEPER
parameter is FALSE and a gaussian is being fitted to the background.
[5]



OUTLIST = LITERAL (Read)
````````````````````````
The names of the output lists.
These may be specified as list of comma separated names, using
indirection if required, OR, as a single modification element (of the
input NDF names). The simplest modification element is the asterisk
"*" which means call each of the output lists the same name as the
corresponding input NDFs (but without the ".sdf" extension). So, IN >
* OUTLIST > * signifies that all the NDFs in the current directory
should be used and the output lists should have the same names.
Other types of modification can also occur, such as, OUTLIST >
*_objs.dat which means call the position lists the same as the input
NDFs but put "_objs.dat" after the names. Replacement of a specified
string with another in the output file names can also be used, OUTLIST
> *|_debias|_images.dat| this replaces the string "_debias" with
"_images.dat" in any of the output names.
If wildcarded names for the input NDFs are used then is it recommended
that wildcards are also used for the position list names (the order of
input names is not guaranteed).
The output files contain an integer index for each image feature
followed by the X and Y centroid (formed using all the intensity
information) and finally the mean intensity of pixels in the group.
[*.DAT]



OVERRIDE = _LOGICAL (Read)
``````````````````````````
If TRUE then it is not a fatal error to detect no objects on an image.
In this case the output list of positions will not be written and the
value in the COUNTS parameter will be set to 0. [FALSE]



OVERSAMP = _INTEGER (Read)
``````````````````````````
An oversampling factor which is used when forming the initial
histogram (greater than 1). The oversample is estimated by making the
initial histogram mean count OVERSAMP times smaller than the mean
count which would give BINFRAC in every bin. Increasing the oversample
will increase the probability that only one bin will meet the BINFRAC
criterion. Only used if USEPER is FALSE. [5]



PERCENTILE = _DOUBLE (Read)
```````````````````````````
The percentage point in the data histogram which is to be used as the
threshold estimate. For data which has a significant background count
this value should always be much greater than 50 (the median) and
probably greater than the upper quantile (75). Only used if USEPER is
TRUE. [96]



THRESH = _DOUBLE (Read)
```````````````````````
The threshold which is to be used for detecting image features.
Connected pixel groups above this threshold form image features. This
parameter is only used if the AUTOTHRESH parameter is set FALSE. In
this case a value may be supplied for each NDF which is being
processed. [Dynamic default]



TOUCH = _LOGICAL (Read)
```````````````````````
If TRUE then pixel groups may contact the edges of the data array.
Contact is defined as any pixel in the connected group of pixels being
on the first or last column or row of the actual data array (not
including any NDF origin information). Setting this FALSE decreases
the probability of incomplete pixel groups being centroided which
would result in inaccurate positions. [FALSE]



USEPER = _LOGICAL (Read)
````````````````````````
If TRUE then a percentage point (of the total counts) in the histogram
will be used to estimate the threshold. Otherwise a gaussian fit to
the data histogram will be used to estimate the background value.
[TRUE]



Examples
~~~~~~~~
findobj in='*' minpix=10 outlist='*.find'
In this example FINDOBJ processes all the NDFs in the current
directory locating objects with connected pixel groups which have more
than 9 pixels above the threshold.
findobj '"ndf1,ndf2,ndf10"' 6 '"obj1.dat,obj2.dat,obj3.dat"'
useper=false nsigma=3 In this example FINDOBJ estimates the threshold
using the mode value in the histogram of data values as an estimate of
the background and the fit of a gaussian to this to estimate the
background standard deviation. The threshold used for each NDF is then
3 times the standard deviation above the estimated background.



Notes
~~~~~


+ Threshold estimation.

The algorithm used for calculating the values of percentiles for
threshold determination should give good results even in the presence
of pixel values which lie very far away from the bulk of the data.
However, the sampling of the histogram used to estimate the mode and
standard deviation may be poor in the presence of extreme outliers. If
there are extreme outliers therefore, the percentile method (USEPER
set to TRUE) of determining the threshold should be used.
The histogram used by FINDOBJ when USEPER is FALSE is formed by (if
necessary) re-binning until the BINFRAC criterion is met, it is
expected that this will always result in a well sampled histogram. The
background value is the mode of this histogram and is not refined
during the gaussian fitting. The gaussian fitting just estimates the
standard deviation of the background and uses a fixed peak value and
position (the mode of the histogram) and iterates rejecting bins whose
counts fall below 20 percent of the peak value, stopping when either 3
iterations have been performed or the standard deviation does not
change by more than one bin width in data values.
FINDOBJ is optimised to determine a reliable detection threshold and
is not concerned with the accurate determination of the background
value on a frame (as it performs no photometric measurements). For
this reason the histogram which it uses to determine the background
value is made in such a way that it is usually very well sampled
(probably oversampled, for most other purposes). FINDOBJ should not be
used in a manner for which it is not suited without understanding how
if differs from other more specialized routines.


+ NDF extension items.

On exit the CURRENT_LIST items in the CCDPACK extensions
(.MORE.CCDPACK) of the input NDFs are set to the names of the
appropriate output lists. These items will be used by other CCDPACK
position list processing routines to automatically access the lists.


+ Output position list format.

CCDPACK format - Position lists in CCDPACK are formatted files whose
first three columns are interpreted as the following.


+ Column 1: an integer identifier
+ Column 2: the X position
+ Column 3: the Y position

The column one value must be an integer and is used to identify
positions which may have different locations but are to be considered
as the same point. Comments may be included in the file using the
characters # and !. Columns may be separated by the use of commas or
spaces.
In all cases the coordinates in position lists are pixel coordinates.


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ THRESH -- dynamic value
+ OVERRIDE -- always FALSE

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when re-using the application after a break of
sometime. The intrinsic default behaviour of the application may be
restored by using the RESET keyword on the command line.
Certain parameters (LOGTO and LOGFILE) have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set and reset using
the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995-2000 Central Laboratory of the Research Councils. All Rights
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA and QUALITY components of
  an NDF data structure. Bad pixels and all non-complex numeric data
  types can be handled.




