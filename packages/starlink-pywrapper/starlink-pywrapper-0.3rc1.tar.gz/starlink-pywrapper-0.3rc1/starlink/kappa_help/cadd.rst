

CADD
====


Purpose
~~~~~~~
Adds a scalar to an NDF data structure


Description
~~~~~~~~~~~
The routine adds a scalar (i.e. constant) value to each pixel of an
NDF's data array to produce a new NDF data structure.


Usage
~~~~~


::

    
       cadd in scalar out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input NDF data structure, to which the value is to be added.



OUT = NDF (Write)
`````````````````
Output NDF data structure.



SCALAR = _DOUBLE (Read)
```````````````````````
The value to be added to the NDF's data array.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
cadd a 10 b
This adds ten to the NDF called a, to make the NDF called b. NDF b
inherits its title from a.
cadd title="HD123456" out=b in=a scalar=17.3
This adds 17.3 to the NDF called a, to make the NDF called b. NDF b
has the title "HD123456".



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ADD, CDIV, CMULT, CSUB, DIV, MATHS, MULT, SUB.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2012 Science & Facilities Research Council.
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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL,
TITLE, UNITS, HISTORY, WCS and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




