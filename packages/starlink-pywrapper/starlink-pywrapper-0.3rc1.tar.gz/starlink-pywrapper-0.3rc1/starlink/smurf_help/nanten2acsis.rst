

NANTEN2ACSIS
============


Purpose
~~~~~~~
Convert NANTEN2 FITS format data files to an ACSIS format NDF


Description
~~~~~~~~~~~
Opens NANTEN2 SDFITS-style files for reading, and writes out the
spectra in ACSIS format. Metadata are converted to appropriate FITS
headers. The NANTEN2 spectra must have been calibrated.


ADAM parameters
~~~~~~~~~~~~~~~



DIRECTORY = _CHAR (Read)
````````````````````````
Directory for output ACSIS files. A NULL value will use the current
working directory. This command will create a subdir in this directory
named after the observation number.



IN = GROUP (Read)
`````````````````
Name of the input NANTEN2 FITS files to be converted.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



Notes
~~~~~


+ Whilst this command does a reasonable job of converting common data
to ACSIS format it still has to undergo extensive testing to ensure
that it is always doing the correct thing.
+ The ORAC-DR recipe defaults to REDUCE_SCIENCE.
+ This routine works with NANTEN data exported from CLASS as a single
  SDFITS-style file per observation with the data in a binary table.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKECUBE, GSD2ACSIS, SUPERCAM2ACSIS;


Copyright
~~~~~~~~~
Copyright (C) 2014 Cornell University All Rights Reserved.


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


