

STARECALC
=========


Purpose
~~~~~~~
Calculate image for SCUBA-2 STARE observations


Description
~~~~~~~~~~~
This command is used for reconstructing 2-D images from STARE
observations. Files containing data not taken in STARE mode are
ignored. The user has the option to specify the number of frames to be
averaged together, but the default is to automatically calculate that
number to give 1-second averages.


ADAM parameters
~~~~~~~~~~~~~~~



BBM = NDF (Read)
````````````````
Group of files to be used as bad bolometer masks. Each data file
specified with the IN parameter will be masked. The corresponding
previous mask for a subarray will be used. If there is no previous
mask the closest following will be used. It is not an error for no
mask to match. A NULL parameter indicates no mask files to be
supplied. [!]



IN = NDF (Read)
```````````````
Name of input data file(s).



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NAVER = _INTEGER (Read)
```````````````````````
Number of frames to average together in output images. If a NULL value
is given, NAVER is calculated dynamically for each input file to give
output images which are 1-second averages. [!]



OUT = NDF (Write)
`````````````````
Name of output file containing STARE images.



OUTFILES = LITERAL (Write)
``````````````````````````
The name of a text file to create, in which to put the names of all
the output NDFs created by this application (one per line). If a null
(!) value is supplied no file is created. [!]



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: DREAMSOLVE; KAPPA: WCSMOSAIC; CCDPACK: MAKEMOS


Copyright
~~~~~~~~~
Copyright (C) 2008-2009 Science and Technology Facilities Council.
Copyright (C) 2006-2008,2013 University of British Columbia. All
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
02110-1301, USA


