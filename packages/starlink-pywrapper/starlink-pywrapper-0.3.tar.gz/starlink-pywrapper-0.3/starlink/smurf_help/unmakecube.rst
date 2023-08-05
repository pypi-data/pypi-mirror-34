

UNMAKECUBE
==========


Purpose
~~~~~~~
Produce simulated time series data from a regrided ACSIS data cube


Description
~~~~~~~~~~~
This routine creates one or more time series cubes, spanned by
(frequency, detector number, time) axes, from one or more input sky
cubes spanned by (celestial longitude, celestial latitude, spectrum)
axes. Thus, it performs a sort of inverse to the MAKECUBE application.
The output time series detector samples are created by interpolating
the supplied input sky cubes at the position of the reference time
series sample centre. Various interpolation methods can be used (see
parameter INTERP).
The output time series cubes inherit all meta-data from the
corresponding input reference time series. The only thing modified is
the values in the NDF "Data" array.


ADAM parameters
~~~~~~~~~~~~~~~



DETECTORS = LITERAL (Read)
``````````````````````````
A group of detector names. Only data for the named detectors will be
included in the output time series cubes. If a null (!) value is
supplied, data for all detectors will be created. [!]



IN = NDF (Read)
```````````````
A group of input (ra,dec,spectrum) sky cubes (for instance, a set of
tiles produced by MAKECUBE). If these sky cubes have any spatial
overlap, then the output time series data will be derived from the
last supplied sky cube that covers the overlap region. That is, sky
cubes near the end of the supplied group take precedence over those
near the start.



INTERP = LITERAL (Read)
```````````````````````
The method to use when resampling the input sky cube pixel values. For
details of these schemes, see the descriptions of routines
AST_RESAMPLEx in SUN/210. INTERP can take the following values:


+ "Linear" -- The output sample values are calculated by bi-linear
interpolation among the four nearest pixels values in the input sky
cube. Produces smoother output NDFs than the nearest-neighbour scheme,
but is marginally slower.
+ "Nearest" -- The output sample values are assigned the value of the
single nearest input pixel. A very fast method.
+ "Sinc" -- Uses the sinc(pi*x) kernel, where x is the pixel offset
from the interpolation point and sinc(z)=sin(z)/z. Use of this scheme
is not recommended.
+ "SincSinc" -- Uses the sinc(pi*x)sinc(k*pi*x) kernel. A valuable
general-purpose scheme, intermediate in its visual effect on NDFs
between the bi-linear and nearest-neighbour schemes.
+ "SincCos" -- Uses the sinc(pi*x)cos(k*pi*x) kernel. Gives similar
results to the "Sincsinc" scheme.
+ "SincGauss" -- Uses the sinc(pi*x)exp(-k*x*x) kernel. Good results
can be obtained by matching the FWHM of the envelope function to the
point-spread function of the input data (see parameter PARAMS).
+ "Somb" -- Uses the somb(pi*x) kernel, where x is the pixel offset
from the interpolation point and somb(z)=2*J1(z)/z (J1 is the first-
order Bessel function of the first kind). This scheme is similar to
the "Sinc" scheme.
+ "SombCos" -- Uses the somb(pi*x)cos(k*pi*x) kernel. This scheme is
  similar to the "SincCos" scheme.

[current value]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
A group of output NDFs into which the simulated time series data will
be written.



PARAMS( 2 ) = _DOUBLE (Read)
````````````````````````````
An optional array which consists of additional parameters required by
the Sinc, SincSinc, SincCos, SincGauss, Somb and SombCos interpolation
schemes (see parameter INTERP).
PARAMS( 1 ) is required by all the above schemes. It is used to
specify how many pixels are to contribute to the interpolated result
on either side of the interpolation point in each dimension.
Typically, a value of 2 is appropriate and the minimum allowed value
is 1 (i.e. one pixel on each side). A value of zero or fewer indicates
that a suitable number of pixels should be calculated automatically.
[0]
PARAMS( 2 ) is required only by the SombCos, SincSinc, SincCos, and
SincGauss schemes. For the SombCos, SincSinc, and SincCos schemes, it
specifies the number of pixels at which the envelope of the function
goes to zero. The minimum value is 1.0, and the run-time default value
is 2.0. For the SincGauss scheme, it specifies the full-width at half-
maximum (FWHM) of the Gaussian envelope. The minimum value is 0.1, and
the run-time default is 1.0. Good results are often obtained by
approximately matching the FWHM of the envelope function, given by
PARAMS(2), to the point-spread function of the input data. []



REF = NDF (Read)
````````````````
A group of existing time series data cubes. These act as templates for
the new time series cubes created by this application, and specified
via parameter OUT.



USEDETPOS = _LOGICAL (Read)
```````````````````````````
If a true value is supplied, then the detector positions are read from
the detector position arrays in each template NDF. Otherwise, the
detector positions are calculated on the basis of the FPLANEX/Y
arrays. Both methods should (in the absence of bugs) result in
identical cubes. [TRUE]



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKECUBE


Copyright
~~~~~~~~~
Copyright (C) 2008-2009 Science and Technology Facilities Council. All
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


