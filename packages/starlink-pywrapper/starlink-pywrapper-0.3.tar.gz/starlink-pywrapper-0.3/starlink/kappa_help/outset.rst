

OUTSET
======


Purpose
~~~~~~~
Mask pixels inside or outside a specified circle in a two-dimensional
NDF


Description
~~~~~~~~~~~
This routine assigns a specified value (which may be "bad") to either
the outside or inside of a specified circle within a specified
component of a given two-dimensional NDF.


Usage
~~~~~


::

    
       outset in out centre diam
       



ADAM parameters
~~~~~~~~~~~~~~~



CENTRE = LITERAL (Read)
```````````````````````
The co-ordinates of the centre of the circle. The position must be
given in the current co-ordinate Frame of the NDF (supplying a colon
":" will display details of the current co-ordinate Frame). The
position should be supplied as a list of formatted axis values
separated by spaces or commas. See also parameter USEAXIS. The current
co-ordinate Frame can be changed using KAPPA:WCSFRAME.



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be masked. It may be "Data", or "Variance",
or "Error" (where "Error" is equivalent to "Variance"). ["Data"]



CONST = LITERAL (Given)
```````````````````````
The constant numerical value to assign to the masked pixels, or the
string "bad". ["bad"]



DIAM = LITERAL (Read)
`````````````````````
The diameter of the circle. If the current co-ordinate Frame of the
NDF is a SKY Frame (e.g. RA and DEC), then the value should be
supplied as an increment of celestial latitude (e.g. DEC). Thus,
"10.2" means 10.2 arc-seconds, "30:0" would mean 30 arc-minutes, and
"1:0:0" would mean 1 degree. If the current co-ordinate Frame is not a
SKY Frame, then the diameter should be specified as an increment along
axis 1 of the current co-ordinate Frame. Thus, if the current Frame is
PIXEL, the value should be given simply as a number of pixels.



IN = NDF (Read)
```````````````
The name of the source NDF.



INSIDE = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, the constant value is assigned to the
inside of the circle. Otherwise, it is assigned to the outside.
[FALSE]



OUT = NDF (Write)
`````````````````
The name of the masked NDF.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of strings should be supplied
specifying the axes which are to be used when specifying the circle
parameters CENTRE and DIAM. Each axis can be specified using one of
the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the two used pixel axes within the NDF are used. [!]



Examples
~~~~~~~~
outset neb1 nebm "13.5,201.3" 20 const=0
This copies NDF "neb1" to "nebm", setting pixels to zero in the DATA
array if they fall outside the specified circle. Assuming the current
co-ordinate Frame of neb1 is PIXEL, the circle is centred at pixel co-
ordinates (13.5, 201.3) and has a diameter of 20 pixels.
outset neb1 nebm "15:23:43.2 -22:23:34.2" "10:0" inside comp=var
This copies NDF "neb1" to "nebm", setting pixels bad in the variance
array if they fall inside the specified circle. Assuming the current
co-ordinate Frame of neb1 is a SKY Frame describing RA and DEC, the
aperture is centred at RA 15:23:43.2 and DEC -22:23:34.2, and has a
diameter of 10 arc-minutes.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDMASK, REGIONMASK.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
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


+ This routine correctly processes the WCS, AXIS, DATA, QUALITY,
LABEL, TITLE, UNITS, HISTORY, and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ Bad pixels and automatic quality masking are supported.
+ All non-complex numeric data types can be handled.




