

SC2FFT
======


Purpose
~~~~~~~
Fourier Transform SCUBA-2 time-series data


Description
~~~~~~~~~~~
This routine performs the forward or inverse FFT of SCUBA-2 time-
series data. The FFT of the data are stored in a 4-dimensional array
with dimensions frequency, xbolo, ybolo, component (where component is
a dimension of length 2 holding the real and imaginary parts). The
inverse flag is used to transform back to the time domain from the
frequency domain. If the data are already in the requested domain, the
ouput file is simply a copy of the input file.


ADAM parameters
~~~~~~~~~~~~~~~



AVPSPEC = _LOGICAL (Read)
`````````````````````````
Calculate average power spectral density over "good" bolometers. By
default a 1/noise^2 weight is applued (see WEIGHTAVPSPEC). [FALSE]



AVPSPECTHRESH = _DOUBLE (Read)
``````````````````````````````
N-sigma noise threshold to define "good" bolometers for AVPSPEC [5]



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
Input files to be transformed.



INVERSE = _LOGICAL (Read)
`````````````````````````
Perform inverse transform. [FALSE]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NGOOD = _INTEGER (Write)
````````````````````````
Number of good bolometers which contribute to average power spectrum.



OUT = NDF (Write)
`````````````````
Output files. The number of output files can differ from the number of
input files due to darks being filtered out and also to files from the
same sequence being concatenated before aplying the FFT.



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line). If a null (!)
value is supplied no file is created. [!]



POLAR = _LOGICAL (Read)
```````````````````````
Use polar representation (amplitude, argument) of FFT. [FALSE]



POWER = _LOGICAL (Read)
```````````````````````
Use polar representation of FFT with squared amplitudes divided by the
frequency bin spacing (gives a power spectral density, PSD). [FALSE]



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



WEIGHTAVPSPEC = _LOGICAL (Read)
```````````````````````````````
If set, weight power spectrum of each bolo by 1/noise^2 when
calculating the average (estimated from 2--20 Hz spectrum). [TRUE]



ZEROBAD = _LOGICAL (Read)
`````````````````````````
Zero any bad values in the data before taking FFT. [TRUE]



Notes
~~~~~
Transforming data loses the VARIANCE and QUALITY components.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2CONCAT, SC2CLEAN, CALCNOISE


Copyright
~~~~~~~~~
Copyright (C) 2008-2011 Science and Technology Facilities Council.
Copyright (C) 2008-2011,2013 University of British Columbia. All
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


