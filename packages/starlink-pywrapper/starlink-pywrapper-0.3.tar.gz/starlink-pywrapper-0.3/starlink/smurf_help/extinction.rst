

EXTINCTION
==========


Purpose
~~~~~~~
Extinction correct SCUBA-2 data


Description
~~~~~~~~~~~
This application can be used to extinction correct data in a number of
ways.


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



CSOTAU = _REAL (Read)
`````````````````````
Value of the 225 GHz zenith optical depth. Only used if TAUSRC equals
`CSOTAU' or 'AUTO'. If a NULL (!) value is given, the task will use
the appropriate value from the FITS header of each file. Note that if
a value is entered by the user, that value is used for all input
files. In AUTO mode the value might not be used.



FILTERTAU = _REAL (Read)
````````````````````````
Value of the zenith optical depth for the current wavelength. Only
used if TAUSRC equals `FILTERTAU'. Note that no check is made to
ensure that all the input files share the same filter.



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



HASSKYREM = _LOGICAL (Read)
```````````````````````````
Indicate that the data have been sky removed even if the fact can not
be verified. This is useful for the case where the sky background has
been removed using an application other than SMURF REMSKY. [FALSE]



IN = NDF (Read)
```````````````
Input file(s). The input data must have had the sky signal removed



METHOD = _CHAR (Read)
`````````````````````
Method to use for airmass calculation. Options are:

+ ADAPTIVE - Determine whether to use QUICK or FULL based on the
elevation of the source and the opacity.
+ FULL - Calculate the airmass of each bolometer.
+ QUICK - Use a single airmass for each time slice.

[ADAPTIVE]



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



TAUREL = GROUP (Read)
`````````````````````
Specifies values to be used for scaling the 225 GHz tau to the
specific filter. These values will only be used if CSOTAU or WVMRAW
methods are used to determine the tau. The group should have the form:
ext.taurelation.<FILT> = (a,b)
where <FILT> is the filter name and "a" and "b" are the coefficients
for a relationship of the form
tau_filt = a ( tau_cso + b )
A null value will use the default relations. [!]



TAUSRC = _CHAR (Read)
`````````````````````
Source of optical depth data. Options are:

+ WVMRAW - use the Water Vapour Monitor time series data
+ WVMFIT - use a fit to the Water Vapor Monitor data
+ CSOFIT - use a fit to the CSO 225 GHz tau data
+ CSOTAU - use a single 225 GHz tau value
+ FILTERTAU - use a single tau value for this wavelength
+ AUTO - Use WVM if available and reliable, else a WVM or CSO fit.

[AUTO]



Notes
~~~~~


+ The iterative map-maker will extinction correct the data itself and
this command will not be necessary.
+ QLMAKEMAP automatically applies an extinction correction.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: REMSKY, MAKEMAP; SURF: EXTINCTION


Copyright
~~~~~~~~~
Copyright (C) 2008-2010, 2013 Science and Technology Facilities
Council. Copyright (C) 2005 Particle Physics and Astronomy Research
Council. Copyright (C) 2005-2010,2013 University of British Columbia.
All Rights Reserved.


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


