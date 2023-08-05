

SMURFCOPY
=========


Purpose
~~~~~~~
Copy a 2d image out of a time series file


Description
~~~~~~~~~~~
This task can be used to extract data from a file for a particular
time slice. The world coordinates will be valid on this slice so the
data can be used for display or image overlay (e.g. when using the
KAPPA OUTLINE command to determine where this slice lies in relation
to the reconstructed map).
KAPPA NDFCOPY will not add the specific astrometry information when
used to extract a slice and so cannot be used when WCS is required.


ADAM parameters
~~~~~~~~~~~~~~~



FTSPORT = _CHAR (Read)
``````````````````````
The FTS-2 port to use in calculating the WCS for the output NDF, or
null if FTS-2 was not in the beam. If set, this parameter should be
"tracking" or "image". [!]



IN = NDF (Read)
```````````````
Input file. Cannot be a DARK frame. If the input file is raw data it
will be flatfielded before writing out. This allows a reasonable bad
pixel mask to be applied.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output file. Extensions are not propagated.



POINTING = LITERAL (Read)
`````````````````````````
The name of a text file containing corrections to the pointing read
from the input data files. If null (!) is supplied, no corrections are
used. If a file is supplied, it should start with one or more lines
containing "#" in column one. These are comment lines, but if any
comment line has the form "# SYSTEM=AZEL" or "# SYSTEM=TRACKING" then
it determines the system in which the pointing correction are
specified (SYSTEM defaults to AZEL). The last comment line should be a
space-separated list of column names, including "TAI", "DLON" and
"DLAT". Each remaining line should contain numerical values for each
column, separated by white space. The TAI column should contain the
TAI time given as an MJD. The DLON and DLAT columns should give arc-
distance offsets parallel to the longitude and latitude axes, in arc-
seconds. The TAI values should be monotonic increasing with row
number. The longitude and latitude axes are either AXEL or TRACKING as
determined by the SYSTEM value in the header comments. Blank lines are
ignored. The DLON and DLAT values are added onto the SMU jiggle
positions stored in the JCMTSTATE extension of the input NDFs. DLON
and DLAT values for non-tabulated times are determined by
interpolation. [!]



SLICE = _INTEGER (Read)
```````````````````````
Index of time axis (GRID coordinates). 0 can be used to specify the
last slice in the file without having to know how many slices are in
the file.



Notes
~~~~~


+ Currently, this routine cannot support multiple input files or
multiple indices from a single input file. Once extracted the output
file can no longer be processed by SMURF routines.
+ Currently only understands SCUBA-2 data.
+ SCUBA-2 data will be flatfielded in the output slice if the input
  file is raw.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CONTOUR, OUTLINE; SMURF: jcmtstate2cat


Copyright
~~~~~~~~~
Copyright (C) 2008-2013 Science and Technology Facilities Council. All
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


