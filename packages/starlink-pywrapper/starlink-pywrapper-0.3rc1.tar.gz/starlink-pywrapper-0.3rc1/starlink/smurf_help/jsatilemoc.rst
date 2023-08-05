

JSATILEMOC
==========


Purpose
~~~~~~~
Create an image MOC based on a JSA tile


Description
~~~~~~~~~~~
This script takes a JSA tile and produces a MOC representation of the
area covered by good pixels.


Usage
~~~~~


::

    
       jsatilemoc in out [maxorder]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
An NDF (or FITS) file containing a JSA tile. It must have a TILENUM
header indicating the JSA tile number accompanied by a comment
including the HEALPix Nside value. The JSA tile must not have been
trimmed. It could either be created with the trimming options
disabled, or be untrimmed using the UNTRIM_JSA_TILES PICARD recipe.



MAXORDER = _INTEGER (Read)
``````````````````````````
The maximum HEALPix order to be included in the MOC. [29]



OUT = FITS (Read)
`````````````````
The output MOC FITS file name.



Copyright
~~~~~~~~~
Copyright (C) 2013-2014 Science & Technology Facilities Council. All
Rights Reserved.


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


