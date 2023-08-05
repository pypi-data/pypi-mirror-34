

CDIV
====


Purpose
~~~~~~~
Divides an NDF by a scalar


Description
~~~~~~~~~~~
This application divides each pixel of an NDF by a scalar (constant)
value to produce a new NDF.


Usage
~~~~~


::

    
       cdiv in scalar out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input NDF structure whose pixels are to be divided by a scalar.



OUT = NDF (Write)
`````````````````
Output NDF structure.



SCALAR = _DOUBLE (Read)
```````````````````````
The value by which the NDF's pixels are to be divided.



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null value will cause the title of the
NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
cdiv a 100.0 b
Divides all the pixels in the NDF called a by the constant value 100.0
to produce a new NDF called b.
cdiv in=data1 out=data2 scalar=-38
Divides all the pixels in the NDF called data1 by -38 to give data2.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ADD, CADD, CMULT, CSUB, DIV, MATHS, MULT, SUB.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2012 Science & Facilities Research Council. All Rights
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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL,
TITLE, UNITS, HISTORY, WCS and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  carried out using the appropriate floating-point type, but the numeric
  type of the input pixels is preserved in the output NDF.




