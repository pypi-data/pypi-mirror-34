

BADBOLOS
========


Purpose
~~~~~~~
Generate a map of random dead bolometers and add it as an NDF
extension to the input file


Description
~~~~~~~~~~~
Given an input NDF file, retrieve the array size and randomly generate
a user-specified number of bad bolometers. These bad bolometers are
defined by bad rows, bad columns, or bad individual bolometers. Bad
individual bolometers are created in excess of any bolometers already
consider bad as part of a bad row or column. Alternatively the user
can supply an ARD description for the bad bolometer mask.


ADAM parameters
~~~~~~~~~~~~~~~



ARD = ARD description (Read)
````````````````````````````
ARD description of bad bolometer mask. In the case that the user
selects the ARD method of bad bolometer masking, a correctly formatted
ARD description will need to be supplied. The ARD description is
treated as a one-to-one correspondence between its values and the
rows/columns of bolometers in a subarray.



BAD_BOLOS = _INTEGER (Read)
```````````````````````````
If the user selects the random generation of bad bolometers, this
value indicates the desired number of dead bolometers in excess of
those flagged as bad.



BAD_COLUMNS = _INTEGER (Read)
`````````````````````````````
If the user selects the random generation of bad bolometers, this
value indicates the desired number of dead columns of bolometers to be
randomly generated.



BAD_ROWS = _INTEGER (Read)
``````````````````````````
If the user selects the random generation of bad bolometers, this
value indicates the desired number of dead rows of bolometers to be
randomly generated.



IN = NDF (Read)
```````````````
Input NDF file. If the supplied file already has a bad bolometer mask,
it will be overwritten by this routine. Only a single file can be
given and it is modified in place.



METHOD = _CHAR (Read)
`````````````````````
Bad bolometer generation method (either random, or from an ARD
description) as part of the BAD_ROWS and BAD_COLUMNS.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



SEED = INTEGER (Read)
`````````````````````
Seed for random number generator. If a seed is not specified, the
clock time in milliseconds is used.



Notes
~~~~~
This application is designed to be used in conjunction with the
simulator to mask bolometers. It does not currently function correctly
and is deprecated.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2SIM


Copyright
~~~~~~~~~
Copyright (C) 2006-2008 University of British Columbia. All Rights
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


