

TRIG
====


Purpose
~~~~~~~
Performs a trigonometric transformation on a NDF


Description
~~~~~~~~~~~
This routine copies the supplied input NDF, performing a specified
trigonometric operation ( sine, tangent, etc.) on each value in the
DATA array. The VARIANCE component, if present, is modified
appropriately. Pixels for which the required value is undefined, or
outside the numerical range of the NDFs data type, are set bad in the
output.


Usage
~~~~~


::

    
       trig in trigfunc out title
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF structure.



OUT = NDF (Write)
`````````````````
The output NDF structure.



TRIGFUNC = LITERAL (Read)
`````````````````````````
Trigonometrical function to be applied. The options are:


+ ACOS: arc-cosine (radians)
+ ACOSD: arc-cosine (degrees)
+ ASIN: arc-sine (radians)
+ ASIND: arc-sine (degrees)
+ ATAN: arc-tangent (radians)
+ ATAND: arc-tangent (degrees)
+ COS: cosine (radians)
+ COSD: cosine (degrees)
+ SIN: sine (radians)
+ SIND: sine (degrees)
+ TAN: tangent (radians)
+ TAND: tangent (degrees)





TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null value will cause the title of the
NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
trig sindata asind data
Take the arc-sine of the data values in the NDF called sindata, and
store the results (in degrees) in the NDF called data.
trig sindata asin data
As above, but the output values are stored in radians.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ADD, CADD, CMULT, CDIV, CSUB, DIV, MATHS, MULT, SUB.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL,
TITLE, UNITS, HISTORY, WCS and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point, or double precision,
  if appropriate, but the numeric type of the input pixels is preserved
  in the output NDF.




