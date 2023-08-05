

REMSKY
======


Purpose
~~~~~~~
Remove sky background from SCUBA-2 data


Description
~~~~~~~~~~~
This command can be used to fit and remove the sky signal from a
SCUBA-2 time series file.


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



FIT = _CHAR (Read)
``````````````````
Type of fit to be carried out for the PLANE sky removal method.
Choices are Mean, Slope (to fit in elevation only) or Plane. No
default.



FLATMETH = _CHAR (Read)
```````````````````````
Method to use to calculate the flatfield solution. Options are
POLYNOMIAL and TABLE. Polynomial fits a polynomial to the measured
signal. Table uses an interpolation scheme between the measurements to
determine the power. [POLYNOMIAL]



FLATORDER = _INTEGER (Read)
```````````````````````````
The order of polynomial to use when choosing POLYNOMIAL method. [1]



FLATSNR = _DOUBLE (Read)
````````````````````````
Signal-to-noise ratio threshold to use when filtering the responsivity
data to determine valid bolometers for the flatfield. [3.0]



FLATUSENEXT = _LOGICAL (Read)
`````````````````````````````
If true the previous and following flatfield will be used to determine
the overall flatfield to apply to a sequence. If false only the
previous flatfield will be used. A null default will use both
flatfields for data when we did not heater track at the end, and will
use a single flatfield when we did heater track. The parameter value
is not sticky and will revert to the default unless explicitly over-
ridden. [!]



GROUP = _LOGICAL (Read)
```````````````````````
If true, group related files together for processing as a single data
set, else process each file independently. [FALSE]



IN = NDF (Read)
```````````````
Input file(s).



METHOD = _CHAR (Read)
`````````````````````
Sky removal method, either POLY or PLANE.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output file(s)



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line). If a null (!)
value is supplied no file is created. [!]



RESIST = GROUP (Read)
`````````````````````
A group expression containing the resistor settings for each
bolometer. Usually specified as a text file using "^" syntax. An
example can be found in $STARLINK_DIR/share/smurf/resist.cfg
[$STARLINK_DIR/share/smurf/resist.cfg]



RESPMASK = _LOGICAL (Read)
``````````````````````````
If true, responsivity data will be used to mask bolometer data when
calculating the flatfield. [TRUE]



Notes
~~~~~


+ SC2CLEAN can calculate the common-mode signal much more accurately
than the naive algorithm implemented in this routine.
+ The iterative map-maker will calculate the sky signal itself and
  this command should not be used if that variant of the map-maker is to
  be used.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: EXTINCTION, MAKEMAP, SC2CLEAN; SURF: REMSKY


Copyright
~~~~~~~~~
Copyright (C) 2006-2010,2013 University of British Columbia. Copyright
(C) 2006 Particle Physics and Astronomy Research Council. Copyright
(C) 2008-2009 Science and Technology Facilities Council. All Rights
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


