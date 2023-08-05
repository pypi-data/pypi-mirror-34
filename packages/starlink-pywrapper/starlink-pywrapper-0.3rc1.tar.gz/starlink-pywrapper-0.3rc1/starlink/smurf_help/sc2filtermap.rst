

SC2FILTERMAP
============


Purpose
~~~~~~~
Filter a 2-d map


Description
~~~~~~~~~~~
This routine takes the FFT of a 2D map, applies a Fourier-space
filter, and then transforms back to real-space before writing out.
Currently the only available filter is a whitening filter which is
measured using a supplied reference image.


ADAM parameters
~~~~~~~~~~~~~~~



FILT_EDGEHIGH = _REAL (Write)
`````````````````````````````
High-pass filter frequency (1/arcsec)



FILT_EDGELOW = _REAL (Write)
````````````````````````````
Low-pass filter frequency (1/arcsec)



IN = NDF (Read)
```````````````
Input files to be transformed.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output transformed files.



OUTFILTER = NDF (Write)
```````````````````````
Optional NDF for the filter.



WHITEN = _LOGICAL (Read)
````````````````````````
If selected, measure azimuthally-averaged angular power spectrum in
WHITEREFMAP, fit a model A/F^B + W, and apply its complement to the
FFT of the data (normalized to W). AZAVSPEC is set implicitly. [FALSE]



WHITEREFMAP = NDF (Read)
````````````````````````
Reference map in which to measure whitening filter. [FALSE]



ZEROBAD = _LOGICAL (Read)
`````````````````````````
Zero any bad values in the data before taking FFT. [TRUE]



Notes
~~~~~
Transforming data loses the VARIANCE and QUALITY components.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2MAPFFT


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


