

RESHAPE
=======


Purpose
~~~~~~~
Reshapes an NDF, treating its arrays as vectors


Description
~~~~~~~~~~~
This application reshapes an NDF to create another NDF by copying
array values. The array components in the input NDF are treated as
vectors. Each output array is filled in order with values from the
input vector, until it is full or the input vector is exhausted.
Output data and variance pixels not filled are set to the bad value;
unfilled quality pixels are set to zero. The filling is in Fortran
order, namely the first dimension, followed by the second
dimension,... to the highest dimension.
It is possible to form a vectorized NDF using parameter VECTORIZE
without having to specify the shape.


Usage
~~~~~


::

    
       reshape in out shape=?
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF to be reshaped.



OUT = NDF (Read)
````````````````
The NDF after reshaping.



SHAPE( ) = _INTEGER (Read)
``````````````````````````
The shape of the output NDF. For example, [50,30,20] would create 50
columns by 30 lines by 20 bands. It is only accessed when VECTORIZE =
FALSE.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the base NDF to the output NDF. [!]



VECTORIZE = _LOGICAL (Read)
```````````````````````````
If TRUE, the output NDF is the vectorized form of the input NDF. If
FALSE, parameter SHAPE is used to specify the new shape. [FALSE]



Examples
~~~~~~~~
reshape shear normal shape=[511,512]
This reshapes the NDF called shear to form NDF normal, whose shape is
511 x 512 pixels. One example is where the original image has 512 x
512 pixels but one pixel was omitted from each line during some data
capture, causing the image to be sheared between lines.
reshape cube cube1d vectorize
This vectorizes the NDF called cube to form NDF cube1d. This could be
used for a task that only permits one-dimensional data.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CHAIN, PASTE, RESHAPE.


Copyright
~~~~~~~~~
Copyright (C) 1997-1998, 2004 Central Laboratory of the Research
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


+ This routine correctly processes the DATA, QUALITY, VARIANCE, LABEL,
TITLE, UNITS, and HISTORY, components of an NDF data structure and
propagates all extensions. WCS and AXIS information is lost.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




