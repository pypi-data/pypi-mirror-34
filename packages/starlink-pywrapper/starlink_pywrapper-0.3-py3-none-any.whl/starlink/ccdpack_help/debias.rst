

DEBIAS
======


Purpose
~~~~~~~
Performs the debiassing and initial preparation of CCD data


Description
~~~~~~~~~~~
This routine debiasses CCD frames, masks defects, sets variances,
corrects for CCD gain and deferred charge, sets saturated values and
extracts the useful portion of the CCD data.
The debiassing section operates in two basic modes -- with and without
a bias frame. If a bias frame is supplied then it is subtracted from
the data arrays of the input NDFs. The subtraction can either be
direct, or by offsetting the values of the bias by the mean value in
the bias-strip region(s). When determining the mean in the bias strips
a function of the distance from the edges is used, this reduces the
effect of any contamination. If you are offsetting to the bias strip
mean then the bias frame should be averaged to zero (MAKEBIAS does
this).
The second debiassing method which DEBIAS supports is the subtraction
of interpolated values. The interpolation is performed between the
bias strips. If only one strip is given the interpolation is really an
extrapolation and is limited to constant values either for each line
or for the frame as a whole. Interpolation between bias strips can be
as for a single strip or may be a straight line fit for each line, or
a fit of a plane to the bias strips (see parameter SMODE). The
interpolation uses weighting operations as for bias frame subtraction.
Bad values can also be rejected from the strips by sigma clipping, or
the noise can be reduced by smoothing the values.
Additional DEBIAS functionality includes the (optional) production of
variance estimates for the input CCD data. It does this by assuming
Poissonian statistics for the bias-subtracted data, together with a
contribution for the readout noise. The masking of bad data areas is
achieved using the transfer of quality information from an NDF, or by
using an ASCII Regions Definition (ARD) file. The expansion of the
data values into counts and the extraction of the useful area of the
CCD are also performed.


Usage
~~~~~


::

    
       debias in out bias [bounds] rnoise adc [mask]
       



ADAM parameters
~~~~~~~~~~~~~~~



ADC = _DOUBLE (Read)
````````````````````
The Analogue-to-Digital Conversion factor. This number converts input
ADUs to detected electrons. This value is used to estimate the
Poissonian noise in the output (debiassed) data values. If the EXPAND
parameter is true, then the output is multiplied by ADC so that the
output is in counts (electrons) rather than ADUs. If variances are not
being generated then this value will not be used.
If a global value for this parameter has been set using CCDSETUP then
this will be used. If USESET is true then a value specific to the Set
Index of each image will be sought. [1.0]



BADBITS = _INTEGER (Read)
`````````````````````````
If the first input NDF has no quality component, and you have
specified the SETBAD= FALSE option, you will be requested to supply a
value for BADBITS (SUN/33). The default for this is 1. BADBITS is a
byte value and hence can only be in the range 0-255. [1]



BIAS = LITERAL (Read)
`````````````````````
Name of the NDF which contains the bias calibration data. This
parameter may be specified as ! in which case either a constant or
values derived from the bias strip(s) are used. The name of this file
may be specified using indirection through an ASCII file. The offered
default is either the last used master bias name or (if one exists)
the name of the NDF produced by the last run of MAKEBIAS.
If USESET is true and you are using bias calibration data from a file,
BIAS should be a group expression referring to one master bias frame
matching each of the Set Index attributes represented in the IN list;
again the name of the file produced by MAKEBIAS will normally be
suitable. [Global master bias or !]



BOUNDS( 2 or 4 ) = _INTEGER (Read)
``````````````````````````````````
The pixel indices (see notes) of the upper and lower bounds of the
bias strip(s). These bounds can run in either the horizontal or
vertical directions. The direction is controlled by the DIRECTION
parameter. The bounds must be supplied in pairs. Pixel indices are the
actual number of pixels, starting at 1,1 at the lower left hand corner
of the NDF data array, which includes any origin offsets within the
input NDFs.
If global values for these bounds have been set using CCDSETUP then
those values will be used. If USESET is true then a value specific to
the Set Index of each image will be sought.



BOXSIZE( 2 ) = _INTEGER (Read)
``````````````````````````````
The sizes of the sides of the box to be used when smoothing the bias
strips. Only used when CMODE="BOX". [15,15]



CMODE = LITERAL (Read)
``````````````````````
The "clean-up" mode for the bias strips. This parameter may take
values of "BOX", "SIGMA" or "WEIGHT". If CMODE="BOX" then the bias
strips are smoothed with a box filter before being processed. If
CMODE="SIGMA" then the bias strips are sigma clipped before being
processed. If CMODE="WEIGHT" then only the weighting as indicated by
the WMODE parameter is used to attempt to decrease the effects of
erroneous pixel values. [BOX]



DEFERRED = _DOUBLE (Read)
`````````````````````````
The deferred charge value. This is also often known as the "fat" or
"skinny" zero. It represents the amount of charge left behind in a
pixel on a readout transfer. This value is subtracted from the data.
If a global value for this parameter has been set using CCDSETUP then
this will be used. If USESET is true then a value specific to the Set
Index of each image will be sought. [0.0]



DIRECTION = LITERAL (Read)
``````````````````````````
The readout direction of the CCD. This parameter can take values of
"X" or "Y". X indicates that the readout direction is horizontal , Y
indicates that the readout direction is vertical. The BOUNDS parameter
values are assumed to be values along the readout direction.
If a global value for this parameter has been set using CCDSETUP then
this will be used. If USESET is true then a value specific to the Set
Index of each image will be sought. [X]



EXPAND = _LOGICAL (Read)
````````````````````````
This value controls whether or not the output data should be
multiplied by the ADC factor to convert the input ADUs to counts
(electrons). The output variance is affected accordingly (multiplied
by ADC**2). This option is disabled if no variances are generated.
Care should be taken when using this option with a large ADC factor
and data types of _WORD,_UWORD,_BYTE or _UBYTE as the output data
range may exceed that allowed with these types. In this case the best
option is to set the PRESERVE parameter FALSE.
[Default is TRUE if input data is not an unsigned data type otherwise
FALSE.]



EXTENT(4) = _INTEGER (Read)
```````````````````````````
The extent of the useful CCD area. This should be given in pixel index
values (see notes). The extent is restricted to that of the CCD frame,
so no padding of the data can occur. If values outside of those
permissable are given then they are modified to lie within the CCD
frame. The values should be given in the order XMIN,XMAX,YMIN,YMAX.
Normally the extent should be set so that the bias strips are excluded
from the output data, this is essential for flatfields whose
normalisation could be adversely biased.
If global values for these bounds have been set using CCDSETUP then
those values will be used. If USESET is true then a value specific to
the Set Index of each image will be sought.



FIXORIGIN = _LOGICAL (Read)
```````````````````````````
Whether to fix the origins of the output NDFs to 1,1, rather than the
lower corner as defined by the EXTENT parameter. This option is of
particular use if the analysis package you are going to use does not
support origins. [FALSE]



FMODE = LITERAL (Read)
``````````````````````
The fit mode which will be used when interpolating bias values. May
take values of "LINE" or "PLANE". This is used together with the SMODE
parameter to define the interpolation method, ie. FMODE="LINE",
SMODE="LINEAR", fits each row or column of the bias strips by a
straight line; FMODE="PLANE", SMODE="CONSTANT" derives a single
constant for the bias value; FMODE="PLANE", SMODE="LINEAR" fits a
plane to the bias-strip data. [LINE]



GENVAR = _LOGICAL (Read)
````````````````````````
If variances are to be generated then this value is set TRUE. If
variances are not to be generated then this value should be set FALSE.
Normally variances should be generated, even though disk and process
time savings can be made by their omission.
If a global value has been set up using CCDSETUP this value will be
used. [FALSE]



GETBIAS = _LOGICAL (Read)
`````````````````````````
This parameter controls whether or not an attempt is to be made to
access a master bias NDF. [TRUE]



GETMASK = _LOGICAL (Read)
`````````````````````````
This parameter controls whether or not an attempt is to be made to
access a defect mask using the parameter MASK. [TRUE]



IN = LITERAL (Read)
```````````````````
A list of the names of the NDFs which contain the raw CCD data. Note
that at present the input data must have a common processing mode,
i.e. have the same ADC factor, readout noise etc. These values are
represented by the parameter values of the task. The input data must
also use the same master bias frame except if USESET is true and the
input and bias images contain suitable CCDPACK Set header information,
in which case each input image will be processed using the bias image
with the corresponding Set Index attribute.
The NDF names should be separated by commas and may include wildcards.



KEEPIN = _LOGICAL (Read)
````````````````````````
Whether to keep (i.e. not delete) the input NDFs (parameter IN) or
not. Deleting the input NDFs has the advantage of saving disk space,
but should probably only be used if this program is part of a sequence
of commands and the intermediary data produced by it are not
important.
The calibration master frames (parameters BIAS and possibly MASK) are
never deleted.
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



MASK = LITERAL (Read)
`````````````````````
The name of an NDF or ASCII Regions Definition (ARD) file.
If an NDF is given then any regions of BAD values (set through
explicit BAD values or by BADBITS in the quality component) will be
transferred to the output NDF.
If an ARD file is given then its regions will be interpreted and
transferred to the output NDF. ARD is described in its own section.
The regions whose quality is to be set are probably hot spots, line
defects etc. which contain little or no useful information. This
parameters may be returned as ! indicating that no mask is to be
applied.
If a global value for this parameter has been set using CCDSETUP then
this will be used. If USESET is true then a value specific to the Set
Index of each image will be sought.
The name of this file may be specified using indirection through a
file. [!]



NSIGMA = _REAL (Read)
`````````````````````
The number of standard deviations to clip the bias strips at. This is
only used in CMODE="SIGMA". The actual clipping occurs at
NSIGMA*RNOISE. If no variances are being generated then the RNOISE
value is estimated from the data values in the strips. [4.0]



OFFSET = _LOGICAL (Read)
````````````````````````
If TRUE then the input bias data array is offset by the mean value
derived from the bias-strip areas. If FALSE then the bias data is
directly subtracted. This parameter is disabled for unsigned data
types as the bias data cannot have been previously zeroed. [TRUE]



OUT = LITERAL (Write)
`````````````````````
Names of the output NDFs. These may be specified as list of comma
separated names, using indirection if required, OR, as a single
modification element (of the input names). The simplest modification
element is the asterisk "*" which means call each of the output NDFs
the same name as the corresponding input NDFs. So, IN > * OUT > *
signifies that all the NDFs in the current directory should be used
and the output NDFs should have the same names.
Other types of modification can also occur, such as, OUT > tmp_* which
means call the output NDFs the same as the input NDFs but put tmp_ in
front of the names. Replacement of a specified string with another in
the output file names can also be used, OUT > tmp_*|debias|flattened|
this replaces the string debias with flattened in any of the output
names tmp_*.



PRESERVE = _LOGICAL (Read)
``````````````````````````
If TRUE then the data type of the input NDFs are used for processing
and are preserved on exit from this routine. If FALSE then a suitable
floating point type will be chosen for the output type and the
processing will be performed using this choice.
This option should be used when a unacceptable loss of accuracy may
occur, or when the data range can no longer be represented in the
range of the present data type. The latter effect may occur when
expanding input ADU values into electrons, if the ADC factor is large
and the input data have types of _WORD,_UWORD,_BYTE or _UBYTE.
If a global value for this parameter has been set using CCDSETUP then
this will be used. [TRUE]



RNOISE = _DOUBLE (Read)
```````````````````````
The readout noise in input data units (ADUs). An estimate of the
readout noise is shown for unweighted values in the bias strips, if
the bias strips are used. If variances are not generated then this
value is not used. If variances are generated then the readout noise
is included in the variance estimates.
If a global value has been set using CCDSETUP then this will be used.
If USESET is true then a value specific to the Set Index of each image
will be sought. [Dynamic default or 1.0]



SATURATE = _LOGICAL (Read)
``````````````````````````
This parameter controls whether the data are to be processed to detect
saturated values or not. The actual saturation value is given using
the SATURATION parameter. [FALSE]



SATURATION = _DOUBLE (Read)
```````````````````````````
The data saturation value. Only used if SATURATE is TRUE.
If a global value has been set using CCDSETUP then this will be used.
If USESET is true then a value specific to the Set Index of each image
will be sought. [1.0D6]



SETBAD = _LOGICAL (Read)
````````````````````````
If TRUE then the quality information will be transferred from the MASK
NDF to the output NDFs in the form of BAD ("flagged") values in the
data component. This is the usual method of indicating the presence of
pixels with no value. If FALSE then the quality information will be
transferred into the quality component, all output quality pixels will
have their BADBITS set. (Note that if the input NDF already has a
quality component the BADBITS will be set by a logical OR of the
current bits with the BADBITS value). [TRUE]



SETSAT = _LOGICAL (Read)
````````````````````````
This parameter controls how saturated data will be flagged. If it is
set TRUE then saturated values will be replaced by the value of the
parameter SATURATION (which is also the value used to detect saturated
data). If it is FALSE then saturated values will be set to BAD (also
known as invalid). [FALSE]



SMODE = LITERAL (Read)
``````````````````````
The mode which will be used to perform any interpolation fit between
the bias strips. Can take values of "CONSTANT" or "LINEAR". If only
one bias strip is given this may only take the value "CONSTANT". This
is used together with the FMODE parameter to define the interpolation
method, i.e. FMODE="LINE", SMODE="LINEAR", fits each row or column of
the bias strips by a straight line; FMODE="PLANE", SMODE="CONSTANT"
derives a single constant for the bias value; FMODE="PLANE",
SMODE="LINEAR" fits a plane to the bias-strip data. [CONSTANT]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. [Output from DEBIAS]



USECON = _LOGICAL (Read)
````````````````````````
If TRUE then you can supply an estimate for the bias contribution
(parameter ZERO). This value is then subtracted from the input NDF.
Only use this option if you do not have any bias frames or bias strips
and you have good reason to believe that the value you are supplying
is accurate enough for your purposes. [FALSE]



USEEXT = _LOGICAL (Read)
````````````````````````
If TRUE then certain of the parameters of this program will not be
used and the required values will be obtained from the CCDPACK
extensions of the input NDFs instead. This method can only be used if
the NDFs have been "imported" using the programs PRESENT or IMPORT.
Typically it is used when processing using CCDPACK's "automated"
methods (in this case the input NDFs should contain all the
information necessary to process them).
The parameters that this affects are: ADC BOUNDS DEFERRED DIRECTION
EXTENT RNOISE SATURATION ZERO
Values obtained from the CCDPACK extension are identified in the
output log by the presence of a trailing asterisk (*). [FALSE]



USESET = _LOGICAL (Read)
````````````````````````
Whether to use Set header information or not. If USESET is false then
any Set header information will be ignored. If USESET is true, then
the BIAS parameter is taken to refer to a group of files, and each IN
file will be processed using a master bias image with a Set Index
attribute which matches its own. An IN file with no Set header is
considered to match a master bias file with no Set header, so USESET
can safely be set true when the input files contain no Set header
information.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



WMODE = LITERAL (Read)
``````````````````````
The weighting method which is to be used when deriving means or
performing the least squares interpolation fits using any bias strips.
Can take the values "LINEAR", "EXP", or "NONE". "LINEAR" and
"EXP"-onential produce weights which are maximum in the centre of each
bias strip and which fall off towards the edges. "LINEAR" weighting
gives zero weighting for the edge lines and so is the more robust.
[LINEAR]



ZERO = _DOUBLE (Read)
`````````````````````
If USECON=TRUE then this value is subtracted from the input NDF.



Examples
~~~~~~~~
debias r1 r1b bias '[2,10,400,415]' adc=1.1 rnoise=8
This example debiasses the data array in NDF r1 writing the result to
NDF r1b. It uses the data component of NDF BIAS as the bias estimator.
The bias is offset by the mean value found within the ranges 2-10 and
400-415 pixels along the X axis. The data in the bias strips are
smoothed by a box filter and weighted linearly from the edges inwards.
The output variance is produced by a combination of the Poisson
statistics (using an ADC value of 1.1) and readout noise (value 8),
together with the variance of the bias NDF (if present).
debias in=r1 out=r2 bounds='[2,10,401,416]' adc=2.5 rnoise=10
This example debiasses the NDF r1 data component writing the result to
the NDF r2. The bias is estimated by an interpolation of a constant
for each data row. The constant is the result of a linearly weighted
average of the bias strip data which has been box filtered.
debias in=r1 out=r2 bounds='[2,10,401,416]' smode=linear adc=5
fmode=plane direct=y wmode=exp cmode=sigma rnoise=10 nsigma=4 This
example debiasses the NDF r1 data component writing the result to the
NDF r2. The bias is estimated by the fitting of a plane to the data in
the bias strips. The bias-strip data are first sigma clipped at a
level RNOISE*NSIGMA. The fit is performed with weighting based on a
exponential fall off from the centre of the strips. The bias strips
are defined by the bounds applied up the Y axis.
debias in='*' out='*_debias' bounds='[3,16,912,940]' adc=1 rnoise=4
bias=bias/master_bias In this example all the NDFs in the current
directory are debiassed. The names of the output NDFs are as those of
the corresponding input NDFs, except that they are trailed by the
"_debias" string.



Notes
~~~~~


+ If the input NDFs have variance components and no variances are to
be generated then they are processed.
+ Pixel indices. The bounds supplied to DEBIAS should be given as
  pixel indices. These usually start at 1,1 for the pixel at the lower
  left-hand corner of the data-array component (this may not be true if
  the NDFs have been sectioned, in which case the lower left hand pixel
  will have pixel indices equal to the data component origin values).
  Pixel indices are different from pixel coordinates in that they are
  non-continuous, i.e. can only have integer values, and start at 1,1
  not 0,0. To change from pixel coordinates add 0.5 and round to the
  nearest integer.




ASCII region definition files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEBIAS allows regions which are to be defined as having poor quality
(either by setting the appropriate pixels BAD or by setting part of
the quality component) to be described within an ordinary text file
using the ARD (ASCII Region Definition) language. The ARD language is
based on a set of keywords that identify simple shapes. Some of the
regions which can be defined are:


+ BOX
+ CIRCLE
+ COLUMN
+ ELLIPSE
+ LINE
+ PIXEL
+ POLYGON
+ RECT
+ ROTBOX
+ ROW

ARD descriptions can be created using the KAPPA application ARDGEN, or
you can of course create your own by hand. An example of the contents
of an ARD file follows.
# # ARD description file for bad regions of my CCD.
COLUMN( 41, 177, 212 ) # Three bad columns PIXEL( 201, 143, 153, 167 )
# Two Bad pixels BOX( 188, 313, 5, 5 ) # One Hot spot centred at
188,313 ELLIPSE( 99, 120, 21.2, 5.4, 45.0 )
# Polygons defining badly vignetted corners POLYGON( 2.2, 96.4, 12.1,
81.5, 26.9, 63.7, 47.7, 41.9, 61.5, 24.1, 84.3, 0.0 , 0.0, 0.0 )
POLYGON( 6.2, 294.3, 27.9, 321.0, 52.6, 348.7, 74.4, 371.5, 80.0,
384.0, 0.0, 384.0 ) #


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply. The exceptions to this rule are:

+ TITLE -- always "Output from DEBIAS"
+ KEEPIN -- always TRUE

Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new
datasets/different devices, or after a break of sometime. The
intrinsic default behaviour of the application may be restored by
using the RESET keyword on the command line.
Certain parameters (ADC, BIAS, BOUNDS, DEFERRED, DIRECTION, EXTENT,
GENVAR, LOGFILE, LOGTO, MASK, PRESERVE, RNOISE, SATURATE, SATURATION,
SETSAT and USESET) have global values. These global values will always
take precedence, except when an assignment is made on the command
line. If USESET is true, then global values of some of these
parameters (ADC, BOUNDS, DEFERRED, DIRECTION, EXTENT, MASK, RNOISE,
SATURATION) specific to the Set Index of each image will be used if
available. In general global values may be set and reset using the
CCDSETUP and CCDCLEAR commands, however, the BIAS parameter may only
be set by a run of the application MAKEBIAS.
If the parameter USEEXT is TRUE then the following parameters are not
used: ADC, BOUNDS, DEFERRED, DIRECTION, EXTENT, RNOISE, SATURATION and
ZERO. Values are obtained from the input NDF extensions instead.


Copyright
~~~~~~~~~
Copyright (C) 1991-1994 Science & Engineering Research Council.
Copyright (C) 1995-2005 Central Laboratory of the Research Councils.
Copyright (C) 2007 Science and Technology Facilities Council. All
Rights Reserved.


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


+ This task supports all components of an NDF. If requested [default]
  a variance is produced from the bias subtracted values. The task
  processes BAD pixels. The UNITS of the output NDF are set to ADUs or
  electrons depending on whether data expansion has occurred or not.
  Processing is supported for all HDS (non-complex) numeric types.




