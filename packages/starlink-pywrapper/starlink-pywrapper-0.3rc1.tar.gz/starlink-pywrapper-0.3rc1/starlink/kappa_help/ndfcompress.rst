

NDFCOMPRESS
===========


Purpose
~~~~~~~
Compresses an NDF so that it occupies less disk space


Description
~~~~~~~~~~~
This application creates a copy of an NDF that occupies less disk
space. This compression does not affect the data values seen by
subsequent application, since all applications will automatically
uncompress the data.
Two compression methods are available: SCALE or DELTA (see Parameter
METHOD).


Usage
~~~~~


::

    
       ndfcompress in out method
       



ADAM parameters
~~~~~~~~~~~~~~~



DSCALE = _DOUBLE (Read)
```````````````````````
The scale factor to use for the DATA component, when compressing with
METHOD set to "SCALE". If a null (!) value is supplied for DSCALE or
DZERO, default values will be used for both that cause the scaled data
values to occupy 96% of the available range of the data type selected
using Parameter SCALEDTYPE. [!]



DZERO = _DOUBLE (Read)
``````````````````````
The zero offset to use for the DATA component, when compressing with
METHOD set to SCALE. If a null (!) value is supplied for DSCALE or
DZERO, default values will be used for both that cause the scaled data
values to occupy 96% of the available range of the data type selected
using Parameter SCALEDTYPE. [!]



IN = NDF (Read)
```````````````
The input NDF.



METHOD = LITERAL (Read)
```````````````````````
The compression method to use. The options are as follows.


+ "SCALED" -- A lossy compression scheme for all data types. See
"Scaled Compression" below, and Parameters DSCALE, DZERO, VSCALE,
VZERO, and SCALEDTYPE.
+ "DELTA" -- A lossless compression scheme for integer data types. See
  "Delta Compression" below, and Parameters ZAXIS, ZMINRATIO and ZTYPE.

The current value is the default, which is initially "DELTA". []



OUT = NDF (Write)
`````````````````
The output NDF.



SCALEDTYPE = LITERAL (Read)
```````````````````````````
The data type to use for the scaled data values. It is only used if
METHOD is "SCALED". It can be one of the following options.


+ "_INTEGER" -- four-byte signed integers
+ "_WORD" -- two-byte signed integers
+ "_UWORD" -- two-byte unsigned integers
+ "_BYTE" -- one-byte signed integers
+ "_UBYTE" -- one-byte unsigned integers

The same data type is used for both DATA and (if required) VARIANCE
components of the output NDF. The initial default value is "_WORD".
[current value]



VSCALE = _DOUBLE (Read)
```````````````````````
The scale factor to use for the VARIANCE component, when compressing
with METHOD set to SCALE. If a null (!) value is supplied for VSCALE
or VZERO, default values will be used for both that cause the scaled
variance values to occupy 96% of the available range of the data type
selected using Parameter SCALEDTYPE. [!]



VZERO = _DOUBLE (Read)
``````````````````````
The zero factor to use for the VARIANCE component, when compressing
with METHOD set to SCALE. If a null (!) value is supplied for VSCALE
or VZERO, default values will be used for both that cause the scaled
variance values to occupy 96% of the available range of the data type
selected using Parameter SCALEDTYPE. [!]



ZAXIS = _INTEGER (Read)
```````````````````````
The index of the pixel axis along which differences are to be taken,
when compressing with METHOD set to "DELTA". If this is zero, a
default value will be selected that gives the greatest compression.
[0]



ZMINRATIO = _REAL (Read)
````````````````````````
The minimum allowed compression ratio for an array (the ratio of the
supplied array size to the compressed array size), when compressing
with METHOD set to "DELTA". If compressing an array results in a
compression ratio smaller than or equal to ZMINRATIO, then the array
is left uncompressed in the new NDF. If the supplied value is zero or
negative, then each array will be compressed regardless of the
compression ratio. [1.0]



ZTYPE = LITERAL (Read)
``````````````````````
The data type to use for storing differences between adjacent
uncompressed data values, when compressing with METHOD set to "DELTA".
Must be one of _INTEGER, _WORD, _BYTE or blank. If a null (!) value or
blank value is supplied, the data type that gives the best compression
is determined and used. [!]



Examples
~~~~~~~~
ndfcompress infile outfile scale scaledtype=_uword
Copies the contents of the NDF structure infile to the new structure
outfile, scaling the values so that they fit into unsigned two-byte
integers. The scale and zero values used are chosen automatically.



Scaled Compression
~~~~~~~~~~~~~~~~~~
The SCALE compression method scales the supplied data values using a
linear transformation so that they fit into a smaller (integer) data
type. A description of the scaling uses is stored with the output NDF
so that later application can reconstruct the original unscaled
values. This method is not lossless, due to the truncation involved in
converting floatign point values to integers.


Delta Compression
~~~~~~~~~~~~~~~~~
DELTA compression is lossless, but can only be used on integer values.
It assumes that adjacent integer values in the input tend to be close
in value, and so differences between adjacent values can be
represented in fewer bits than the absolute values themselves. The
differences are taken along a nominated pixel axis within the supplied
array (specified by parameter ZAXIS). Any input value that differs
from its earlier neighbour by more than the data range of the selected
data type is stored explicitly using the data type of the input array.
Further compression is achieved by replacing runs of equal input
values by a single occurrence of the value with a corresponding
repetition count.
It should be noted that the degree of compression achieved is
dependent on the nature of the data, and it is possible for a
compressed array to occupy more space than the uncompressed array. The
mean compression factor actually achieved is displayed (the ratio of
the supplied NDF size to the compressed NDF size).
It is possible to delta compress an NDF that has already been scale
compressed. This provides a means of further compressing floating-
point arrays. However, note that the default values supplied for
DSCALE, DZERO, VSCALE, and VZERO may not be appropriate as they are
chosen to maximise the spread of the scaled integer values in order to
minimise the integer truncation error, but delta compression works
best on arrays of integers in which the spread of values is small.
If the input NDF is already DELTA compressed, it will be uncompressed
and then recompressed using the supplied parameter values.
More details of delta compression can be found in SUN/11 ("ARY - A
Subroutine Library for Accessing ARRAY Data Structures"), subsection
"Delta Compressed Array Form".


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFCOPY.


Copyright
~~~~~~~~~
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2010 Science & Technology Facilities Council. All Rights
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
The TITLE, LABEL, UNITS, DATA, VARIANCE, QUALITY, AXIS, WCS, and
HISTORY components are copied by this routine, together with all
extensions.


