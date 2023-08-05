

SC2EXPANDMODEL
==============


Purpose
~~~~~~~
Expand a DIMM model component into a full time-series data cube


Description
~~~~~~~~~~~
This command is a stand-alone task for converting a DIMM model
component (which may be stored as a series of model parameters) into a
full time-series representation (a data cube with time along the third
axis).


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input files to be uncompressed and flatfielded.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output file(s).



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: makemap


Copyright
~~~~~~~~~
Copyright (C) 2010 University of British Columbia. All Rights
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
02110-1301, USA


