

NDF2PGM
=======


Purpose
~~~~~~~
Converts an NDF into a PBMPLUS-style PGM-format file


Description
~~~~~~~~~~~
This application converts an NDF to a PBMPLUS PGM-format file. The
programme first finds the brightest and darkest pixel values in the
image. It then uses these to determine suitable scaling factors
convert the image into an 8-bit representation. These are then to a
simple greyscale PBMPLUS PGM file.


Usage
~~~~~


::

    
       ndf2pgm in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The name of the input NDF data structure (without the .sdf extension).
The suggested default is the current NDF if one exists, otherwise it
is the current value.



OUT = _CHAR (Read)
``````````````````
The name of the PGM file be generated. The .pgm name extension is
added to any output filename that does not contain it.



Examples
~~~~~~~~
ndf2pgm old new
This converts the NDF called old (in file old.sdf) to the PGM file
new.pgm.
ndf2pgm in=spectre out=spectre.pgm
This converts the NDF called spectre (in file spectre.sdf) to the PGM
file spectre.pgm.



Copyright
~~~~~~~~~
Copyright (C) 1995-1996, 2004 Central Laboratory of the Research
Councils. All Rights Reserved.


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
Bad values in the data array are replaced with zero in the output PGM
file.


