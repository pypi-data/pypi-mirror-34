

MULT
====


Purpose
~~~~~~~
Multiplies two NDF data structures


Description
~~~~~~~~~~~
The routine multiplies two NDF data structures pixel-by-pixel to
produce a new NDF.


Usage
~~~~~


::

    
       mult in1 in2 out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN1 = NDF (Read)
````````````````
First NDF to be multiplied.



IN2 = NDF (Read)
````````````````
Second NDF to be multiplied.



OUT = NDF (Write)
`````````````````
Output NDF to contain the product of the two input NDFs.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN1 to be used instead. [!]



Examples
~~~~~~~~
mult a b c
This multiplies the NDF called a by the NDF called b, to make the NDF
called c. NDF c inherits its title from a.
mult out=c in1=a in2=b title="Normalised spectrum"
This multiplies the NDF called a by the NDF called b, to make the NDF
called c. NDF c has the title "Normalised spectrum".



Notes
~~~~~
If the two input NDFs have different pixel-index bounds, then they
will be trimmed to match before being multiplied. An error will result
if they have no pixels in common.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ADD, CADD, CDIV, CMULT, CSUB, DIV, MATHS, SUB.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2007 Science & Technology Facilities Council.
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
TITLE, UNITS, HISTORY, WCS, and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Calculations will
  be performed using either real or double precision arithmetic,
  whichever is more appropriate. If the input NDF structures contain
  values with other data types, then conversion will be performed as
  necessary.




