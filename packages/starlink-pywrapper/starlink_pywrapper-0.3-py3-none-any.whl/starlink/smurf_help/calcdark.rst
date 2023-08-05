

CALCDARK
========


Purpose
~~~~~~~
Calculate the 2d dark frame from dark observation


Description
~~~~~~~~~~~
Given a set of dark observations, calculate a mean dark frame from
each. A bad bolometer mask can be supplied to remove known bad
bolometers. Does not flatfield.


ADAM parameters
~~~~~~~~~~~~~~~



BBM = NDF (Read)
````````````````
Group of files to be used as bad bolometer masks. Each data file
specified with the IN parameter will be masked. The corresponding
previous mask for a subarray will be used. If there is no previous
mask the closest following one will be used. It is not an error for no
mask to match. A NULL parameter indicates no mask files to be
supplied. [!]



IN = NDF (Read)
```````````````
Input files to be processed. Non-darks will be filtered out.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output dark files. These can be used as bad bolometer masks in
subsequent processing steps via the BBM parameter in other SCUBA-2
SMURF commands.



Notes
~~~~~
Dark files will be subtracted from raw data during the flatfielding
step. Commands that flatfield data can use either raw dark files or
the output from CALCDARK.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: FLATFIELD, MAKEMAP


Copyright
~~~~~~~~~
Copyright (C) 2008 Science and Technology Facilities Council.
Copyright (C) 2008-2010 University of British Columbia. All Rights
Reserved.


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
02110-1301, USA.


