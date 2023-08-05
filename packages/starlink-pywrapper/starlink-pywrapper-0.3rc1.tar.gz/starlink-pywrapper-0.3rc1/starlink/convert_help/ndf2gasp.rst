

NDF2GASP
========


Purpose
~~~~~~~
Converts a two-dimensional NDF into a GASP image


Description
~~~~~~~~~~~
This application converts a two-dimensional NDF into the GAlaxy
Surface Photometry (GASP) package's format. See the Notes for the
details of the conversion.


Usage
~~~~~


::

    
       ndf2gasp in out [fillbad]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF data structure. The suggested default is the current NDF
if one exists, otherwise it is the current value.



FILLBAD = _INTEGER (Read)
`````````````````````````
The value used to replace bad pixels in the NDF's data array before it
is copied to the GASP file. The value must be in the range of signed
words (-32768 to 32767). A null value (!) means no replacements are to
be made. This parameter is ignored if there are no bad values. [!]



OUT = FILENAME (Write)
``````````````````````
The name of the output GASP image. Two files are produced with the
same name but different extensions. The ".dat" file contains the data
array, and ".hdr" is the associated header file that specifies the
dimensions of the image. The suggested default is the current value.



Examples
~~~~~~~~
ndf2gasp abell1367 a1367
Converts an NDF called abell1367 into the GASP image comprising the
pixel file a1367.dat and the header file a1367.hdr. If there are any
bad values present they are copied verbatim to the GASP image.
ndf2gasp ngc253 ngc253 fillbad=-1
Converts the NDF called ngc253 to a GASP image comprising the pixel
file ngc253.dat and the header file ngc253.hdr. Any bad values in the
data array are replaced by minus one.



Notes
~~~~~
The rules for the conversion are as follows:

+ The NDF data array is copied to the ".dat" file.
+ The dimensions of the NDF data array is written to the ".hdr" header
file.
+ All other NDF components are ignored.




References
~~~~~~~~~~
GASP documentation (MUD/66).


Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: GASP2NDF.


Keywords
~~~~~~~~
CONVERT, GASP


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1999, 2004 Central Laboratory of the Research Councils. Copyright
(C) 2008 Science & Technology Facilities Council. All Rights Reserved.


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


+ The GASP image produced has by definition type SIGNED WORD. There is
type conversion of the data array to this type.
+ Bad values may arise due to type conversion. These too are
substituted by the (non-null) value of FILLBAD.
+ For an NDF with an odd number of columns, the last column from the
  GASP image is trimmed.




