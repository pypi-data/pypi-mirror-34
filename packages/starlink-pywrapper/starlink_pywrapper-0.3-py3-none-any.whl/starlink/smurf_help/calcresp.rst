

CALCRESP
========


Purpose
~~~~~~~
Calculate bolometer responsivity from stored flatfield solution


Description
~~~~~~~~~~~
This routine calculates a bolometer responsivity image from a stored
flatfield solution. To calculate a new flatfield solution, use the
CALCFLAT command on a FLATFIELD observation.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input files to be processed. Each input file is processed
independently so will work with all observation files including dark
observations and a combination of sub-arrays.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NGOOD() = _INTEGER (Write)
``````````````````````````
Number of bolometers with good responsivities. Integer array, one
entry for each input file.



RESIST = GROUP (Read)
`````````````````````
A group expression containing the resistor settings for each
bolometer. Usually specified as a text file using "^" syntax. An
example can be found in $STARLINK_DIR/share/smurf/resist.cfg
[$STARLINK_DIR/share/smurf/resist.cfg]



OUT = NDF (Write)
`````````````````
Output responsivity images. If the input files were each taken with
the same stored FLATFIELD solution the output responsivity images will
be identical.



Notes
~~~~~


+ Works on all raw data files. The responsivity image will be
identical for all files in a single observation since it is only
updated following a FLATFIELD observation.
+ Provenance is not propagated to the output files, since the output
files do not depend on the bolometer data.
+ The responsivity data are filtered using a signal-to-noise ratio of
5.0. The number of bolometers passing this criterion is reported in
the NGOOD parameter. The variance is stored in the output files so
additional filtering is possible.
+ For TABLE flatfields the CALCFLAT calculation of responsivity can
  use the variance of each measurement to calculate a weighted fit. The
  data files themselves do not store the variance in the flatfield
  solution so the answer from CALCRESP may differ slightly to the answer
  calculated with CALCFLAT.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: FLATFIELD, CALCFLAT KAPPA: MAKESNR


Copyright
~~~~~~~~~
Copyright (C) 2009-2010 Science and Technology Facilities Council. All
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
02110-1301, USA.


