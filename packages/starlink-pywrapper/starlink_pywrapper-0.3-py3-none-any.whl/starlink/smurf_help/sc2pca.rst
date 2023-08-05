

SC2PCA
======


Purpose
~~~~~~~
Use principal component analysis to identify correlated SCUBA-2
signals


Description
~~~~~~~~~~~
This routine calculates a new set of N statistically independent basis
vectors (i.e. with a diagonal covariance matrix) for the N bolometer
time series, and calculates the projection of the bolometers along
this new basis. This "Principal Component Analysis" is useful for
identifying time-correlated noise signals. The ouput array of
components contains the new basis vectors, normalized by their RMS,
though ordered by decreasing significance. The output amplitudes data
cube gives the amplitude of each component for each bolometer across
the focal plane. Generally speaking the component time series
illustrate the time-varying shape of the correlated signals, and the
amplitudes show how strong they are, and which bolometers are
affected.


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



FLAT = _LOGICAL (Read)
``````````````````````
If set ensure data are flatfielded. If not set do not scale the data
in any way (but convert to DOUBLE). [TRUE]



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



IN = NDF (Read)
```````````````
Input files to be uncompressed and flatfielded. Any darks provided
will be subtracted prior to flatfielding.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUTAMP = NDF (Write)
````````````````````
Amplitude data cube. The first two coordinates are bolometer location,
and the third enumerates component.



OUTAMPFILES = LITERAL (Write)
`````````````````````````````
The name of text file to create, in which to put the names of all the
output amplitude NDFs created by this application (one per line). If a
NULL (!) value is supplied no file is created. [!]



OUTCOMP = NDF (Write)
`````````````````````
Component vector data cubes (N components * 1 * M time slices). A cube
is created so that it may be run through SC2FFT if desired.



OUTCOMPFILES = LITERAL (Write)
``````````````````````````````
The name of text file to create, in which to put the names of all the
output component NDFs created by this application (one per line). If a
NULL (!) value is supplied no file is created. [!]



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



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2CLEAN, SC2FFT


Copyright
~~~~~~~~~
Copyright (C) 2006-2011,2013 University of British Columbia. All
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


