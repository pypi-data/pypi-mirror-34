

COPYFLAT
========


Purpose
~~~~~~~
Copy the flatfield information from a reference file


Description
~~~~~~~~~~~
This routine copies the flatfield parameters from a reference data
file (usually a raw SCUBA-2 observation or the output from the
CALCFLAT command) to a group of files. The flatfield is updated in
place.


ADAM parameters
~~~~~~~~~~~~~~~



REF = NDF (Read)
````````````````
File from which to read the flatfield parameters. Can be a raw data
file that contains the required flatfield or output from the CALCFLAT
command. Only a single file for a single subarray can be provided.



IN = NDF (Read)
```````````````
Input files to be updated. The subarray must match that used for the
reference file.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: CALCFLAT


Copyright
~~~~~~~~~
Copyright (C) 2010 Science and Technology Facilities Council. All
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


