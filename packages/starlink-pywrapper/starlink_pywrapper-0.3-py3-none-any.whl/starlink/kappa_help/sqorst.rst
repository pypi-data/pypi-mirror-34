

SQORST
======


Purpose
~~~~~~~
Squashes or stretches an NDF


Description
~~~~~~~~~~~
An output NDF is produced by squashing or stretching an input NDF
along one or more of its dimensions. The shape of the output NDF can
be specified in one of two ways, according to the value of the MODE
parameter; either a distortion factor is given for each dimension, or
its lower and upper pixel bounds are given explicitly.


Usage
~~~~~


::

    
       sqorst in out { factors
                     { lbound=? ubound=?
                     { pixscale=?
                    mode
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = _INTEGER (Read)
``````````````````````
Assigning a value to this parameter indicates that a single axis
should be squashed or stretched. If a null (!) value is supplied for
AXIS, a squash or stretch factor must be supplied for each axis in the
manner indicated by the MODE parameter. If a non-null value is
supplied for AXIS, it should be the integer index of the axis to be
squashed or stretched (the first axis has index 1). In this case, only
a single squash or stretch factor should be supplied, and all other
axes will be left unchanged. If MODE is set to "PixelScale" then the
supplied value should be the index of a WCS axis. Otherwise it should
be the index of a pixel axis. [!]



CONSERVE = _LOGICAL (Read)
``````````````````````````
If set TRUE, then the output pixel values will be scaled in such a way
as to preserve the total data value in a feature on the sky. The
scaling factor is the ratio of the output pixel size to the input
pixel size. This ratio is evaluated once for each panel of a piece-
wise linear approximation to the Mapping, and is assumed to be
constant for all output pixels in the panel. [FALSE]



FACTORS( ) = _DOUBLE (Read)
```````````````````````````
This parameter is only used if MODE="Factors". It defines the factor
by which each dimension will be distorted to produce the output NDF. A
factor greater than one is a stretch and less than one is a squash. If
no value has been supplied for Parameter AXIS, the number of values
supplied for FACTORS must be the same as the number of pixel axes in
the NDF. If a non-null value has been supplied for Parameter AXIS,
then only a single value should be supplied for FACTORS and that value
will be used to distort the axis indicated by Parameter AXIS.



IN = NDF (Read)
```````````````
The NDF to be squashed or stretched.



LBOUND( ) = _INTEGER (Read)
```````````````````````````
This parameter is only used if MODE="Bounds". It specifies the lower
pixel-index values of the output NDF. If no value has been supplied
for Parameter AXIS, the number of values supplied for LBOUND must be
the same as the number of pixel axes in the NDF. If a non-null value
has been supplied for Parameter AXIS, then only a single value should
be supplied for LBOUND and the supplied value will be used as the new
lower bounds on the axis indicated by Parameter AXIS. If null (!) is
given, the lower pixel bounds of the input NDF will be used.



METHOD = LITERAL (Read)
```````````````````````
The interpolation method used to perform the one-dimensional
resampling operations which constitute the squash or stretch. The
following values are permitted.


+ "Auto" -- Equivalent to "BlockAve" with an appropriate PARAMS for
squashes by a factor of two or more, otherwise equivalent to "Linear".
+ "Nearest" -- Nearest neighbour sampling.
+ "Linear" -- Linear interpolation.
+ "Sinc" -- Sum of surrounding pixels weighted using a 1-d sinc(pi*x)
kernel.
+ "SincSinc" -- Sum of surrounding pixels weighted using a 1-d
sinc(pi*x)*sinc(k*pi*x) kernel.
+ "SincCos" -- Sum of surrounding pixels weighted using a 1-d
sinc(pi*x)*cos(k*pi*x) kernel.
+ "SincGauss" -- Sum of surrounding pixels weighted using a 1-d
sinc(pi*x)*exp(-k*x*x) kernel.
+ "BlockAve" -- Block averaging over surrounding pixels.

In the above, sinc(z)=sin(z)/z. Some of these schemes will require
additional parameters to be supplied via the PARAMS parameter. A more
detailed discussion of these schemes is given in the "Sub-Pixel
Interpolation Schemes" section below. ["Auto"]



MODE = LITERAL (Read)
`````````````````````
This determines how the shape of the output NDF is to be specified.
The allowed values and their meanings are as follows.


+ "Factors" -- the FACTORS parameter will be used to determine the
factor by which each dimension should be multiplied.
+ "Bounds" -- the LBOUND and UBOUND parameters will be used to get the
lower and upper pixel bounds of the output NDF.
+ "PixelScale" -- the PIXSCALE parameter will be used to obtain the
  new pixel scale to use for each WCS axis.

["Factors"]



OUT = NDF (Write)
`````````````````
The squashed or stretched NDF.



PIXSCALE = LITERAL (Read)
`````````````````````````
The PIXSCALE parameter is only used if Parameter MODE is set to
"PixelScale". It should be supplied as a comma-separated list of the
required new pixel scales. In this context, a pixel scale for a WCS
axis is the increment in WCS axis value caused by a movement of one
pixel along the WCS axis, and are measured at the first pixel in the
array. Pixel scales for celestial axes should be given in arcseconds.
An asterisk, "*", can be used instead of a numerical value to indicate
that an axis should retain its current scale. The suggested default
values are the current pixel scales. If no value has been supplied for
Parameter AXIS, the number of values supplied for PIXSCALE must be the
same as the number of WCS axes in the NDF. If a non-null value has
been supplied for Parameter AXIS, then only a single value should be
supplied for PIXSCALE and that value will be used as the new pixel
scale on the WCS axis indicated by Parameter AXIS.



PARAMS( ) = _DOUBLE (Read)
``````````````````````````
Parameters required to control the resampling scheme. One or more
values may be required to specify the exact resampling behaviour,
according to the value of the METHOD parameter. See the section on
"Sub-Pixel Interpolation Schemes".



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. A null (!) value causes the input title to
be used. [!]



UBOUND( ) = _INTEGER (Read)
```````````````````````````
This parameter is only used if MODE="Bounds". It specifies the upper
pixel-index values of the output NDF. If no value has been supplied
for Parameter AXIS, the number of values supplied for UBOUND must be
the same as the number of pixel axes in the NDF. If a non-null value
has been supplied for Parameter AXIS, then only a single value should
be supplied for UBOUND and the supplied value will be used as the new
upper bounds on the axis indicated by Parameter AXIS. If null (!) is
given, the upper pixel bounds of the input NDF will be used.



Examples
~~~~~~~~
sqorst block blocktall [1,2,1]
The three-dimensional NDF called block is stretched by a factor of two
along its second axis to produce an NDF called blocktall with twice as
many pixels. The same data block is represented, but each pixel in the
output NDF corresponds to half a pixel in the input NDF. The default
resampling scheme, linear interpolation in the stretch direction, is
used.
sqorst block blocktall [1,2,1] method=sincsinc params=[2,2]
The same operation as the previous example is performed, except that a
Lanczos kernel is used for the interpolation.
sqorst cygnus1 squish1 mode=bounds lbound=[1,1] ubound=[50,50]
This turns the two-dimensional NDF cygnus1 into a new NDF squish1
which has 50 pixels along each side. The same region of sky is
represented, but the input image is squashed along both axes to fit
the specified dimensions.
sqorst fred mode=pixelscale pixscale=5 axis=3
This resamples a cube NDF called fred on to a velocity scale of 5 km/s
per pixel along its third axis.



Notes
~~~~~
If the input NDF contains a VARIANCE component, a VARIANCE component
will be written to the output NDF. It will be calculated on the
assumption that errors on the input data values are statistically
independent and that their variance estimates may simply be summed
(with appropriate weighting factors) when several input pixels
contribute to an output data value. If this assumption is not valid,
then the output error estimates may be biased. In addition, note that
the statistical errors on neighbouring output data values (as well as
the estimates of those errors) may often be correlated, even if the
above assumption about the input data is correct, because of the sub-
pixel interpolation schemes employed.


Sub-Pixel Interpolation Schemes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When squashing or stretching an NDF, a separate one-dimensional
resampling operation is performed for each of the dimensions in which
a resize is being done. By default (when METHOD="Auto") this is done
using linear interpolation, unless it is a squash of a factor of two
or more, in which case a block- averaging scheme which averages over
1/FACTOR pixels. For many purposes this default scheme will be
adequate, but for greater control over the resampling process the
METHOD and PARAMS parameters can be used. Detailed discussion of the
use of these parameters can be found in the "Sub-pixel Interpolation
Schemes" section of the REGRID task documentation. By default, all
interpolation schemes preserve flux density rather than total flux,
but this may be changed using the CONSERVE parameter.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: REGRID, SLIDE, WCSADD.


Copyright
~~~~~~~~~
Copyright (C) 2002, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2012, 2015 Science & Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ The LABEL, UNITS, and HISTORY components, and all extensions are
propagated. TITLE is controlled by the TITLE parameter. DATA.
VARIANCE, AXIS and WCS are propagated after appropriate modification.
The QUALITY component is also propagated if nearest-neighbour
interpolation is being used.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ There can be an arbitrary number of NDF dimensions.




