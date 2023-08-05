

RAWPRESS
========


Purpose
~~~~~~~
Compress raw data


Description
~~~~~~~~~~~
Compress the raw time series data. Currently two compression schemes
are available - see parameter "METHOD". This task is intended to be a
test bed of compression algorithms.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input files to be compressed.



METHOD = _CHAR (Read)
`````````````````````
The compression scheme to use:
"OLD" - converts 32-bit integers to 16-bit integers by calculating a
common mode signal at each time slice and a multiplicative value
(BZERO and BSCALE) after removing the first measurement (STACKZERO).
"DELTA" - stores the differences between adjacent bolometer samples as
16-bit integers. Any values for which the differences are too big to
be stored in 16 bits are stored explicitly in 32 bit integers (see
SUN/11 for full details).
[DELTA]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output file(s).



Notes
~~~~~


+ Data will be uncompressed automatically by any SMURF routine.
+ Files may well be larger when compressed.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: RAWUNPRESS


Copyright
~~~~~~~~~
Copyright (C) 2007-2010 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA


