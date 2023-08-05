

PIXDUPE
=======


Purpose
~~~~~~~
Expands an NDF by pixel duplication


Description
~~~~~~~~~~~
This routine expands the size of an NDF structure by duplicating each
input pixel a specified number of times along each dimension, to
create a new NDF structure. Each block of output pixels (formed by
duplicating a single input pixel) can optionally be masked, for
instance to set selected pixels within each output block bad.


Usage
~~~~~


::

    
       pixdupe in out expand
       



ADAM parameters
~~~~~~~~~~~~~~~



EXPAND() = _INTEGER (Read)
``````````````````````````
Linear expansion factors to be used to create the new data array. The
number of factors should equal the number of dimensions in the input
NDF. If fewer are supplied the last value in the list of expansion
factors is given to the remaining dimensions. Thus if a uniform
expansion is required in all dimensions, just one value need be
entered. If the net expansion is one, an error results. The suggested
default is the current value.



IMASK() = INTEGER (Read)
````````````````````````
Only used if a null (!) value is supplied for parameter MASK. If
accessed, the number of values supplied for this parameter should
equal the number of pixel axes in the output NDF. A mask array is then
created which has bad values at every element except for the element
with indices given by IMASK, which is set to the value 1.0. See
parameter MASK for a description of the use of the mask array. If a
null (!) value is supplied for IMASK, then no mask is used, and every
output pixel in an output block is set to the value of the
corresponding input pixel. [!]



IN = NDF (Read)
```````````````
Input NDF structure to be expanded.



MASK = NDF (Read)
`````````````````
An input NDF structure holding the mask to be used. If a null (!)
value is supplied, parameter IMASK will be used to determine the mask.
If supplied, the NDF Data array will be trimmed or padded (with bad
values) to create an array in which the lengths of the pixel axes are
equal to the values supplied for parameter EXPAND. Each block of
pixels in the output array (i.e. the block of output pixels which are
created from a single input pixel) are multiplied by this mask array
before being stored in the output NDF. [!]



OUT = NDF (Write)
`````````````````
Output NDF structure.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



Examples
~~~~~~~~
pixdupe aa bb 2
This expands the NDF called aa duplicating pixels along each
dimension, and stores the enlarged data in the NDF called bb. Thus if
aa is 2-dimensional, this command would result in a four-fold increase
in the array components.
pixdupe cosmos galaxy [2,1]
This expands the NDF called cosmos by duplicating along the first
axis, and stores the enlarged data in the NDF called galaxy.
pixdupe cube1 cube2 [3,1,2] title="Reconfigured cube"
This expands the NDF called cube1 by having three pixels for each
pixel along the first axis and duplicating along the third axis, and
stores the enlarged data in the NDF called cube2. The title of cube2
is "Reconfigured cube".



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: COMPADD, COMPAVE, COMPICK, PIXDUPE.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1998-1999, 2001, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2010, 2012 Science & Technology
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


+ This routine processes the WCS, AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, and HISTORY, components of an NDF data structure,
and propagates all extensions.
+ The AXIS centre, width and variance values in the output are formed
by duplicating the corresponding input AXIS values.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




