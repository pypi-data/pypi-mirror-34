

RIFT
====


Purpose
~~~~~~~
Adds a scalar to a section of an NDF data structure to correct rift-
valley defects


Description
~~~~~~~~~~~
The routine adds a scalar (i.e. constant) value to each pixel of an
NDF's data array within a sub-section to produce a new NDF data
structure.


Usage
~~~~~


::

    
       rift in scalar out section
       



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
The value to be added to the NDF's data array within the section.



SECTION = LITERAL (Read)
````````````````````````
The pixels to which a scalar is to be added. This is defined as an NDF
section, so that ranges can be defined along any axis, and be given as
pixel indices or axis (data) co-ordinates. So for example "3,4,5"
would select the pixel at (3,4,5); "3:5," would select all elements in
columns 3 to 5; ",4" selects line 4. See "NDF Sections" in SUN/95, or
the online documentation for details.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
rift aa 10.7 bb "100:105" 20
This adds 10 in the columns 100 to 105 in the data array of the NDF
called aa and stores the result in the NDF called bb. In other
respects bb is a copy of aa.
rift cubein -100 cubeout ",,4"
This adds -100 to all values in the fourth plane of the data array of
the NDF called cubein and stores the result in the NDF called cubeout.
In other respects cubeout is a copy of cubeout.
rift in=aa scalar=2 out=bb section="-10:5,200~9"
This adds 2 to the rectangular section between columns -10 to 5 and
lines 196 to 204 of the data array of the NDF called aa and stores the
result in the NDF called bb. In other respects bb is a copy of aa.



Notes
~~~~~
For similar operations performed on a subset, use the appropriate
application to process the relevant section and then run PASTE to
paste the result back into the full array.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CADD, CHPIX, GLITCH, PASTE, SEGMENT, ZAPLIN; Figaro: CSET,
ICSET, NCSET, TIPPEX.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2012 Science & Technology Facilities Council. All Rights
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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ The bad-pixel flag is set to TRUE if undefined values are created
during the arithmetic.
+ All non-complex numeric data types can be handled.




