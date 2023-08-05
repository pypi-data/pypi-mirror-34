

SLIDE
=====


Purpose
~~~~~~~
Realigns an NDF using a translation


Description
~~~~~~~~~~~
The pixels of an NDF are shifted by a given number of pixels along
each pixel axis. The shift need not be an integer number of pixels,
and pixel interpolation will be performed if necessary using the
scheme selected by Parameter METHOD. The shifts to use are specified
either by an absolute vector given by the ABS parameter or by the
difference between a fiducial point and a standard object given by the
FID and OBJ parameters respectively. In each case the co-ordinates are
specified in the NDF's pixel co-ordinate Frame.


Usage
~~~~~


::

    
       slide in out abs method
       



ADAM parameters
~~~~~~~~~~~~~~~



ABS( ) = _DOUBLE (Read)
```````````````````````
Absolute shifts in pixels. The number of values supplied must match
the number of pixel axes in the NDF. It is only used if
STYPE="Absolute".



FID( ) = _DOUBLE (Read)
```````````````````````
Position of the fiducial point in pixel co-ordinates. The number of
values supplied must match the number of pixel axes in the NDF. It is
only used if STYPE="Relative".
An object centred at the pixel co-ordinates given by Parameter OBJ in
the input NDF will be centred at the pixel co-ordinates given by
Parameter FID in the output NDF.



IN = NDF (Read)
```````````````
The NDF to be translated.



METHOD = LITERAL (Read)
```````````````````````
The interpolation method used to perform the translation. The
following values are permitted:


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
+ "BlockAve" -- Block averaging over all pixels in the surrounding
  N-dimensional cube.

In the above, sinc(z)=sin(z)/z. Some of these schemes will require
additional parameters to be supplied via the PARAMS parameter. A more-
detailed discussion of these schemes is given in the "Sub-Pixel
Interpolation Schemes" section below. the initial default is "Linear".
[current value]



OBJ = LITERAL (Read)
````````````````````
Position of the standard object in pixel co-ordinates. The number of
values supplied must match the number of pixel axes in the NDF. It is
only used if STYPE="Relative".
An object centred at the pixel co-ordinates given by Parameter OBJ in
the input NDF will be centred at the pixel co-ordinates given by
Parameter FID in the output NDF.



OUT = NDF (Write)
`````````````````
The translated NDF.



PARAMS( ) = _DOUBLE (Read)
``````````````````````````
Parameters required to control the resampling scheme. One or more
values may be required to specify the exact resampling behaviour,
according to the value of the METHOD parameter. See the section on
"Sub-Pixel Interpolation Schemes".



STYPE = LITERAL (Read)
``````````````````````
The sort of shift to be used. The choice is "Relative" or "Absolute".
["Absolute"]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. A null (!) value will cause the input title
to be used. [!]



Examples
~~~~~~~~
slide m31 m31_acc [3.2,2.3]
The pixels in the NDF m31 are shifted by 3.2 pixels in X and 2.3
pixels in Y, and written to NDF m31_acc. Linear interpolation is used
to produce the output data (and, if present, variance) array.
slide m31 m31_acc [3.2,2.3] nearest
The same as the previous example except that nearest-neighbour
resampling is used. This will be somewhat faster, but may result in
features shifted by up to half a pixel.
slide speca specb stype=rel fid=11.2 obj=11.7
The pixels in the NDF speca are shifted by 0.5 (i.e. 11.7 - 11.2)
pixels and the output NDF is written as specb.
slide speca specb stype=abs abs=0.5
This does just the same as the previous example.



Notes
~~~~~


+ If the NDF is shifted by a whole number of pixels along each axis,
this application merely changes the pixel origin in the NDF. It can
thus be compared to the SETORIGIN command.
+ Resampled axis centres that are beyond the bounds of the input NDF
  are given extrapolated values from the first (or last) pair of valid
  centres.




Sub-Pixel Interpolation Schemes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When performing the translation the pixels are resampled from the
input grid to the output grid by default using linear interpolation.
For many purposes this default scheme will be adequate, but for
greater control over the resampling process the METHOD and PARAMS
parameters can be used. Detailed discussion of the use of these
parameters can be found in the "Sub-pixel Interpolation Schemes"
section of the REGRID task documentation.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: REGRID, SQORST, WCSADD.


Copyright
~~~~~~~~~
Copyright (C) 2002 Central Laboratory of the Research Councils.
Copyright (C) 2005 Particle Physics & Astronomy Research Council.
Copyright (C) 2012 Science & Technology Facilities Council. All Rights
Reserved.


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
propagated. TITLE is controlled by the TITLE parameter. DATA,
VARIANCE, AXIS and WCS are propagated after appropriate modification.
QUALITY component is also propagated if nearest-neighbour
interpolation is being used.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ There can be an arbitrary number of NDF dimensions.




