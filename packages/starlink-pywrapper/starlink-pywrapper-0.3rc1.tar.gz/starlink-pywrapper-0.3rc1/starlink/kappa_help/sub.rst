

SUB
===


Purpose
~~~~~~~
Subtracts one NDF data structure from another


Description
~~~~~~~~~~~
The routine subtracts one NDF data structure from another pixel-by-
pixel to produce a new NDF.


Usage
~~~~~


::

    
       sub in1 in2 out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN1 = NDF (Read)
````````````````
First NDF, from which the second NDF is to be subtracted.



IN2 = NDF (Read)
````````````````
Second NDF, to be subtracted from the first NDF.



OUT = NDF (Write)
`````````````````
Output NDF to contain the difference of the two input NDFs.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN1 to be used instead. [!]



Examples
~~~~~~~~
sub a b c
This subtracts the NDF called b from the NDF called a, to make the NDF
called c. NDF c inherits its title from a.
sub out=c in1=a in2=b title="Background subtracted"
This subtracts the NDF called b from the NDF called a, to make the NDF
called c. NDF c has the title "Background subtracted".



Notes
~~~~~
If the two input NDFs have different pixel-index bounds, then they
will be trimmed to match before being subtracted. An error will result
if they have no pixels in common.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ADD, CADD, CDIV, CMULT, CSUB, DIV, MATHS, MULT.


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
TITLE, HISTORY, WCS and VARIANCE components of an NDF data structure
and propagates all extensions.
+ The UNITS component is propagated only if it has the same value in
both input NDFs.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




