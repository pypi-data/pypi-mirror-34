

COPYBAD
=======


Purpose
~~~~~~~
Copies bad pixels from one NDF file to another


Description
~~~~~~~~~~~
This application copies bad pixels from one NDF file to another. It
takes in two NDFs (parameters IN and REF), and creates a third
(parameter OUT) which is a copy of IN, except that any pixel which is
set bad in the DATA array of REF, is also set bad in the DATA and
VARIANCE (if available) arrays in OUT.
By setting the INVERT parameter TRUE, the opposite effect can be
produced (i.e. any pixel which is not set bad in the DATA array of
REF, is set bad in OUT and the others are left unchanged).


Usage
~~~~~


::

    
       copybad in ref out title
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
NDF containing the data to be copied to OUT.



INVERT = _LOGICAL (Read)
````````````````````````
If TRUE, then the bad and good pixels within the reference NDF
specified by parameter REF are inverted before being used (that is,
good pixels are treated as bad and bad pixels are treated as good).
[FALSE]



NBAD = _INTEGER (Write)
```````````````````````
The number of bad pixels copied to the output NDF.



NGOOD = _INTEGER (Write)
````````````````````````
The number of pixels not made bad in the output NDF.



OUT = NDF (Write)
`````````````````
The output NDF.



REF = NDF (Read)
````````````````
NDF containing the bad pixels to be copied to OUT.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
copybad in=a ref=b out=c title="New image"
This creates a NDF called c, which is a copy of the NDF called a. Any
bad pixels present in the NDF called b are copied into the
corresponding positions in c (non-bad pixels in b are ignored). The
title of c is "New image".



Notes
~~~~~


+ If the two input NDFs have different pixel-index bounds, then they
  will be trimmed to match before being processed. An error will result
  if they have no pixels in common.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SUBSTITUTE, NOMAGIC, FILLBAD, PASTE, GLITCH.


Copyright
~~~~~~~~~
Copyright (C) 1998, 2000, 2003-2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. Copyright (C) 2008, 2009, 2012, 2014 Science and Technology
Facilities Council. All Rights Reserved.


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
+ The BAD_PIXEL flag is set appropriately.
+ All non-complex numeric data types can be handled.




