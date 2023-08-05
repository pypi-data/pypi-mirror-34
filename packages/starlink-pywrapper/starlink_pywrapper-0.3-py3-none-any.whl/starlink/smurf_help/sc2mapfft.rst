

SC2MAPFFT
=========


Purpose
~~~~~~~
Fourier Transform 2D maps


Description
~~~~~~~~~~~
This routine performs the forward or inverse FFT of a 2D map. The FFT
of the data are stored in a 3-dimensional array with dimensions
xfrequency, yfrequency, component (where component is a dimension of
length 2 holding the real and imaginary parts, or ampliude and phase
if in polar form). The inverse flag is used to transform back to the
spatial domain from the frequency domain. If the data are already in
the requested domain, the ouput file is simply a copy of the input
file.


ADAM parameters
~~~~~~~~~~~~~~~



AZAVPSPEC = _LOGICAL (Read)
```````````````````````````
If true, calculate the azimuthally-averaged angular power power
spectrum. POLAR and POWER are set implicitly. [FALSE]



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



OUT = NDF (Write)
`````````````````
Output transformed files.



POLAR = _LOGICAL (Update)
`````````````````````````
Use polar representation (amplitude, argument) of FFT. [FALSE]



POWER = _LOGICAL (Update)
`````````````````````````
Use polar representation of FFT with squared amplitudes divided by the
frequency bin spacing (gives a power spectral density, PSD). [FALSE]



ZEROBAD = _LOGICAL (Read)
`````````````````````````
Zero any bad values in the data before taking FFT. [TRUE]



Notes
~~~~~
Transforming data loses the VARIANCE and QUALITY components.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2FFT


Copyright
~~~~~~~~~
Copyright (C) 2011 University of British Columbia. All Rights
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


