

SHADOW
======


Purpose
~~~~~~~
Enhances edges in a 2-dimensional NDF using a shadow effect


Description
~~~~~~~~~~~
This routine enhances a 2-dimensional NDF by creating a bas-relief or
shadow effect, that causes features in an array to appear as though
they have been illuminated from the side by some imaginary light
source. The enhancement is useful in locating edges and fine detail in
an array.


Usage
~~~~~


::

    
       shadow in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The 2-dimensional NDF to be enhanced.



OUT = NDF (Write)
`````````````````
The output NDF containing the enhanced image.



SHIFT( 2 ) = _INTEGER (Given)
`````````````````````````````
The shift in x and y pixel indices to be used in the enhancement. If
the x shift is positive, positive features in the original array will
appear to be lit from the positive x direction, i.e. from the right.
Similarly, if the y shift is positive, the light source will appear to
be shining from the top of the array. A one- or two-pixel shift is
normally adequate. [1,1]



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
shadow horse horse_bas
This enhances the NDF called horse by making it appear to be
illuminated from the top right, and stores the result in the NDF
called horse_bas.
shadow out=aash in=aa [-1,-1] title="Bas relief"
This enhances the NDF called aa by making it appear to be illuminated
from the bottom left, and stores the result in the NDF called aash,
which has the title "Bas relief".



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LAPLACE, MEDIAN; Figaro: ICONV3.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2012 Science & Technology Facilities Council.
All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, AXIS and HISTORY components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ The output NDF will be trimmed compared with the input NDF by the
  shifts applied.




