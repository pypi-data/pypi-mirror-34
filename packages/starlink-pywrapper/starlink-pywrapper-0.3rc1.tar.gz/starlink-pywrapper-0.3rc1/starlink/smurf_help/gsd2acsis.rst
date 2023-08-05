

GSD2ACSIS
=========


Purpose
~~~~~~~
Convert a GSD format DAS data file to an ACSIS format NDF


Description
~~~~~~~~~~~
Opens a GSD file for reading, and checks the version (currently only
supports GSD Version 5.3). The data are converted to ACSIS format and
written to disk. Metadata are converted to appropriate FITS headers.


ADAM parameters
~~~~~~~~~~~~~~~



DIRECTORY = _CHAR (Read)
````````````````````````
Directory for output ACSIS files. A NULL value will use the current
working directory. This command will create a subdir in this directory
named after the observation number.



IN = CHAR (Read)
````````````````
Name of the input GSD file to be converted.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OBSNUM = INT (Read)
```````````````````
Observation number for files prior to Feb 03. For newer observations
this parameter is not required. Default value will be the observation
number read from the file but prior to Feb 03 this number was the
number within the project rather than the number from the night and
may lead to name clashes since ACSIS data are numbered for a UT date.



Notes
~~~~~


+ Whilst this command does a reasonable job of converting common data
to ACSIS format it still has to undergo extensive testing to ensure
that it is always doing the correct thing. Testing of this command and
comparing its results with SPECX maps will be welcomed.
+ The ORAC-DR recipe defaults to REDUCE_SCIENCE. The exceptions are as
follows:
+ REDUCE_SCIENCE_CONTINUUM for solar-system objects (Sun, Moon,
planets, Titan);
+ REDUCE_POINTING for a FIVEPOINT observation type and a DAS backend;
+ REDUCE_FOCUS for a focus observation type; and
+ REDUCE_SCIENCE_BROADLINE for objects with radial velocities above
  120 km/s.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKECUBE, GSDSHOW; CONVERT: SPECX2NDF; SPECX; GSDPRINT; JCMTDR.


Copyright
~~~~~~~~~
Copyright (C) 2008, 2013 Science and Technology Facilities Council.
All Rights Reserved.


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


