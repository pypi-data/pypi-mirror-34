

GSDSHOW
=======


Purpose
~~~~~~~
Display the contents of headers and arrays for GSD files


Description
~~~~~~~~~~~
Opens a GSD file for reading, and checks the version (currently only
supports GSD version 5.3). Then displays the contents of the headers
and data arrays.


ADAM parameters
~~~~~~~~~~~~~~~



DESCRIPTIONS = _LOGICAL (Read)
``````````````````````````````
Flag for showing header descriptions. [FALSE]



IN = CHAR (Read)
````````````````
Name of the input GSD file to be listed.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



SHOWDATA = _LOGICAL (Read)
``````````````````````````
Flag for showing data array. [FALSE]



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: GSD2ACSIS; GSDPRINT; SPECX; JCMTDR


Copyright
~~~~~~~~~
Copyright (C) 2008 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA.


