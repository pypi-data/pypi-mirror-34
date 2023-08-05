

RAWFIXMETA
==========


Purpose
~~~~~~~
Fix metadata associated with a raw data file


Description
~~~~~~~~~~~
Report any issues associated the metadata of a particular file. In
most cases SMURF applications will automatically apply these
corrections but the command can be used to investigate issues prior to
making a map.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input files to be checked.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



STEPTIME = _DOUBLE (Write)
``````````````````````````
Average steptime for the given file in seconds. Only written if a
single file is given.



Notes
~~~~~


+ Supports ACSIS raw data files
+ In the future this command may gain the ability to fix the data
  files.




Copyright
~~~~~~~~~
Copyright (C) 2009 Science and Technology Facilities Council.
Copyright (C) 2012 University of British Columbia All Rights Reserved.


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


