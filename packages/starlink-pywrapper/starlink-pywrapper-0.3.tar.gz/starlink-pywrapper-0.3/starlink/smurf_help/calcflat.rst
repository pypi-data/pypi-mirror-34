

CALCFLAT
========


Purpose
~~~~~~~
Calculate a flatfield solution from a flatfield observation


Description
~~~~~~~~~~~
This routine calculates a flatfield solution from a flatfield
observation.
The flatfield observation consists of a series of measurements taken
at various pixel heater settings. One standard SCUBA-2 raw data file
is stored for each measurement.
An optimum pixel heater setting is chosen at the time of observation.
The procedure is to record measurements at heater settings around this
optimum value, continually returning to the optimum, which is used as
a reference to subtract pixel zero-point drifts.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input files to be processed. Must all be from the same observation and
the same subarray.



METHOD = _CHAR (Read)
`````````````````````
Method to use to calculate the flatfield solution. Options are
POLYNOMIAL and TABLE. Polynomial fits a polynomial to the measured
signal. Table uses an interpolation scheme between the measurements to
determine the power. [POLYNOMIAL]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NGOOD = _INTEGER (Write)
````````````````````````
Number of bolometers with good responsivities.



OUT = NDF (Write)
`````````````````
Output flatfield file. The primary data array contains the dark
subtracted measurements for each heater setting. The flatfield itself
is stored in the .MORE.SCUBA2.FLATCAL extension. A default output
filename based on the date of observation number, subarray name and
observation number will be suggested.



ORDER = _INTEGER (Read)
```````````````````````
The order of polynomial to use when choosing POLYNOMIAL method. [1]



REFRES = _DOUBLE (Read)
```````````````````````
Reference pixel heat resistance. Defines the mean power scale to be
used. [2.0]



RESIST = GROUP (Read)
`````````````````````
A group expression containing the resistor settings for each
bolometer. Usually specified as a text file using "^" syntax. An
example can be found in $STARLINK_DIR/share/smurf/resist.cfg
[$STARLINK_DIR/share/smurf/resist.cfg]



RESP = NDF (Write)
``````````````````
Responsivity image with variance. No image is written if NULL. [!]



RESPMASK = _LOGICAL (Read)
``````````````````````````
If true, responsivity data will be used to mask bolometer data when
calculating the flatfield. [TRUE]



SNRMIN = _DOUBLE (Read)
```````````````````````
Signal-to-noise ratio threshold to use when filtering the responsivity
data to determine valid bolometers for the flatfield. [3.0]



Notes
~~~~~
Works with Dark and Sky flatfields but not with black-body flatfields.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: CALCRESP, FLATFIELD


Copyright
~~~~~~~~~
Copyright (C) 2008-2010 Science and Technology Facilities Council.
Copyright (C) 2009 University of British Columbia. All Rights
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


