

RAWUNPRESS
==========


Purpose
~~~~~~~
Uncompress raw data


Description
~~~~~~~~~~~
Uncompress the raw time series data from 16-bit to 32-bit integers.
Does not flatfield and so the data are still in integer format. If the
data are not compressed they will be copied without change.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input files to be uncompressed.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output file.



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: FLATFIELD


Copyright
~~~~~~~~~
Copyright (C) 2005-2006 Particle Physics and Astronomy Research
Council. Copyright (C) 2006-2007 University of British Columbia.
Copyright (C) 2007-2008 Science and Technology Facilities Council. All
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


