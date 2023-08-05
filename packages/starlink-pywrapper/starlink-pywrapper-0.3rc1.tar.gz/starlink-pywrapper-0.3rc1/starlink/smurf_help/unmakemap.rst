

UNMAKEMAP
=========


Purpose
~~~~~~~
Produce simulated time series data from a SCUBA-2 map


Description
~~~~~~~~~~~
This routine creates one or more simulated SCUBA-2 time series cubes,
from a supplied 2D image of the sky. Thus, it performs a sort of
inverse to the MAKEMAP application.
The output time series bolometer samples are created by interpolating
the supplied input sky image at the position of the reference time
series sample centre. Various interpolation methods can be used (see
parameter INTERP). Gaussian noise and pointing errors may also be
added (see parameters SIGMA and PERROR).
The output time series cubes inherit all meta-data from the
corresponding input reference time series. The only thing modified is
the values in the NDF "Data" array.


ADAM parameters
~~~~~~~~~~~~~~~



ALIGNSYS = _LOGICAL (Read)
``````````````````````````
If TRUE, then the spatial positions of the template time series data
are aligned with the supplied sky map in the current co-ordinate
system of the map, Otherwise, they are aligned in the ICRS co-ordinate
system. For instance, if the current co-ordinate system in the sky map
is AZEL, then setting ALIGNSYS to TRUE will result in the template
data being aligned in AZEL directly, disregarding the fact that a
given AZEL will correspond to different positions on the sky at
different times. [FALSE]



AMP2 = _DOUBLE (Read)
`````````````````````
Controls the amplitude of the 2 Hz signal in the analysed intensity
streams created in polarimetry mode (see "QIN" and "UIN"). This
parameter is only used if HARMONIC is set to its default value of 4 (a
value of zero is assumed otherwise). It gives the amplitude of the 2
Hz signal as a fraction of the total intensity. See also "PHASE2".
[0.0]



AMP4 = _DOUBLE (Read)
`````````````````````
Controls the amplitude of the 4 Hz signal in the analysed intensity
streams created in polarimetry mode (see "QIN" and "UIN"). This
parameter is only used if HARMONIC is set to its default value of 4 (a
value of zero is assumed otherwise). It gives the amplitude of the 4
Hz signal as a fraction of the total intensity. See also "PHASE4".
[0.0]



AMP16 = _DOUBLE (Read)
``````````````````````
Controls the amplitude of the 16 Hz signal in the analysed intensity
streams created in polarimetry mode (see "QIN" and "UIN"). This
parameter is only used if HARMONIC is set to its default value of 4 (a
value of zero is assumed otherwise). It gives the amplitude of the 16
Hz signal as a fraction of the total intensity. See also "PHASE16".
[0.0]



ANGROT = _DOUBLE (Read)
```````````````````````
The angle from the focal plane X axis to the POL2 fixed analyser, in
degrees. Measured positive in the same sense as rotation from focal
plane X to focal plane Y. [90.0]



COM = NDF (Read)
````````````````
A group of existing time series NDFs that supply the common-mode
signal to be added to the output time series data. The number of NDFs
supplied should match the number of NDFs supplied for parameter REF.
Each supplied NDF should be one-dimensional, with length at least
equal to the length of the time axis of the corresponding REF cube. If
null (!) is supplied, the common mode is set to a constant value given
by parameter COMVAL. [!]



COMVAL(2) = _DOUBLE (Read)
``````````````````````````
One or two values in pW that determine the common mode signal for all
time slices. Only accessed if parameter "COM" is set to null (!). If
two values are supplied, the first is taken to be the emission from
the sky and the second is taken to be an offset caused by the
electronics. The total common-mode signal is the sum of the two. If
only one value is supplied, it is assumed that the second value is
zero (i.e. the entire common-mode is caused by sky signal). Note -
when simulating POL-2 data, Instrumental Polarisation is based on just
the sky emission. Supplying zero or null results in no common mode
being included in the output time series data. [!]



GAI = NDF (Read)
````````````````
A group of existing 2D NDFs that specify the gain of each bolometer
for the corresponding IN file. If null (!) is supplied, all bolometer
gains are set to unity. Otherwise, each of the supplied 2D NDFs must
have dimensions of (32,40). The number of NDFs in the group must equal
the number of NDFs supplied for IN. [!]



HARMONIC = _INTEGER (Read)
``````````````````````````
The Q and U values are derived from the fourth harmonic of the half-
wave plate rotation. However, to allow investigation of other
instrumental effects, it is possible instead to derive equivalent
quantities from any specified harmonic. These quantities are
calculated in exactly the same way as Q and U, but use the harmonic
specified by this parameter. They are stored in the output NDFs given
by OUT, in place of the normal fourth harmonic signal. [4]



IN = NDF (Read)
```````````````
The input 2D image of the sky. If NDFs are supplied for the QIN and
UIN parameters, then IN should hold I values. For POL2 data, the input
I, Q and U pixel values are assumed to incorporate the effect of the
1.35 loss caused by placing POL2 in the beam.



INSTQ = NDF (Read)
``````````````````
An optional 2D input NDF holding the instrumental normalised Q value
for each bolometer, with respect to fixed analyser Ths parameter is
only used if parameter IPFORM is set to "USER". The NDF should have
dimensions of (32,40). The total intensity falling on each bolometer
is multiplied by the corresponding value in this file, to get the
instrumental Q value that is added onto the value read from the QIN
parameter. Bad values are treated as zero values. Note, currently
there is no facility to use different INSTQ values for different sub-
arrays - all data supplied via IN will use the same INSTQ values
regardless of sub-array. To overcome this restriction, run unmakemap
separately for each sub-array supplying a different INSTQ each time.



INSTU = NDF (Read)
``````````````````
An optional 2D input NDF holding the instrumental normalised U value
for each bolometer, with respect to fixed analyser Ths parameter is
only used if parameter IPFORM is set to "USER". The NDF should have
dimensions of (32,40). The total intensity falling on each bolometer
is multiplied by the corresponding value in this file, to get the
instrumental U value that is added onto the value read from the UIN
parameter. Bad values are treated as zero values. Note, currently
there is no facility to use different INSTU values for different sub-
arrays - all data supplied via IN will use the same INSTU values
regardless of sub-array. To overcome this restriction, run unmakemap
separately for each sub-array supplying a different INSTU each time.



INTERP = LITERAL (Read)
```````````````````````
The method to use when resampling the input sky image pixel values.
For details of these schemes, see the descriptions of routines
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



IPFORM = LITERAL (Read)
```````````````````````
Indicates the nature the instrumental polarisation (IP) to be added to
the returned time stream data if the template is a POL2 observation.
It can be any of the following (case-insensitive):


+ "JK": The Johnstone-Kennedy model based on analysis of skydip data.
+ "PL1": A simpler model based on analysis of planetary data.
+ "PL2": A simpler model based on analysis of planetary data.
+ "PL3": A simpler model based on analysis of planetary data.
+ "USER": IP is based on the values supplied for parameters INSTQ and
INSTU.
+ "NONE": No IP is added.

Note, if the PL1 or PL2 model is used, suitable values also need to be
supplied for parameter PLDATA (the default values for PLDATA are
appropriate for PL3).
Supplying a null value (!) value is equivalent to "NONE". ["PL3"]



JKDATA = LITERAL (Read)
```````````````````````
The path to an HDS container file holding data defining the parameters
of the Johnstone/Kennedy model of POL2 instrumental polarisation. This
parameter is only used if parameter IPFORM is set to "JK".
['$STARLINK_DIR/share/smurf/ipdata.sdf']



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
A group of output NDFs into which the simulated time series data will
be written. These will hold _DOUBLE data values. For POL2 data, the
values should be considered to incorporate the 1.35 loss caused by
POL2 .



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



PAOFF = _DOUBLE (Read)
``````````````````````
The angle from the fixed analyser to the have-wave plate for a POL_ANG
value of zero, in degrees. Measured positive in the same sense as
rotation from focal plane X to focal plane Y. [18.65]



PASIGN = _LOGICAL (Read)
````````````````````````
Indicates the sense of rotation of the spinning half-wave plate. If
TRUE, it is assumed that a positive POL_ANG value corresponds to
rotation from focal plane X to focal plane Y axis. If FALSE, it is
assumed that a positive POL_ANG value corresponds to rotation from
focal plane Y to focal plane X axis. [FALSE]



PHASE2 = _DOUBLE (Read)
```````````````````````
The phase offset to apply to the 2 Hz signal specified via parameter
AMP2, in degrees. [0.0]



PHASE4 = _DOUBLE (Read)
```````````````````````
The phase offset to apply to the 4 Hz signal specified via parameter
AMP4, in degrees. [0.0]



PHASE16 = _DOUBLE (Read)
````````````````````````
The phase offset to apply to the 16 Hz signal specified via parameter
AMP16, in degrees. [0.0]



PLDATA() = DOUBLE (Read)
````````````````````````
The numerical parameters of the PL1, PL2 or PL3 IP model for POL2
data. This parameter is only used if parameter IPFORM is set to "PL1",
"PL2" or "PL3". This should be a vector of three (PL1) or four (PL2
and PL3) values, being the coefficients of a quadratic polynomial that
gives the fractional polarisation produced by instrumental
polarisation, as a function of elevation (in radians):
fractional IP = A + B*elev + C*elev*elev
where the vector (A,B,C) are given by the first three elements of
parameter PLDATA. The PL1 model assumes that the IP is parallel to the
elevation axis at all elevations. The PL2 and PL3 require a fourth
value to indicate the offset between the IP and the elevation axis.
The default values are appropriate for PL3.
[2.624E-3,4.216E-2,-2.410E-2,-3.400E-2]



POINTING = LITERAL (Read)
`````````````````````````
The name of a text file containing corrections to the pointing read
from the reference data files. If null (!) is supplied, no corrections
are used. If a file is supplied, it should start with one or more
lines containing "#" in column one. These are comment lines, but if
any comment line has the form "# SYSTEM=AZEL" or "# SYSTEM=TRACKING"
then it determines the system in which the pointing correction are
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
positions stored in the JCMTSTATE extension of the reference NDFs.
DLON and DLAT values for non-tabulated times are determined by
interpolation. [!]



PERROR = _DOUBLE (Read)
```````````````````````
The standard deviation of the pointing errors to include in the output
data, in arc-seconds. [0.0]



QIN = NDF (Read)
````````````````
The input 2D image of the sky Q values, with respect to the second
pixel axis (i.e. the pixel Y axis). Positive polarisation angles are
in the same sense as rotation from the pixel X axis to the pixel Y
axis. If QIN and UIN are both supplied, then the time series specified
by the REF parameter should contain flat-fielded POL2 data. These
values are assumed to incorporate the effect of the 1.35 loss caused
by placing POL2 in the beam. [!]



REF = NDF (Read)
````````````````
A group of existing time series data cubes. These act as templates for
the new time series cubes created by this application, and specified
via parameter OUT. They should contain _DOUBLE (i.e. flat-fielded)
data values.



SIGMA = _DOUBLE (Read)
``````````````````````
The standard deviation of the Gaussian noise to add to the output
data. [0.0]



UIN = NDF (Read)
````````````````
The input 2D image of the sky U values, with respect to the second
pixel axis (i.e. the pixel Y axis). Positive polarisation angles are
in the same sense as rotation from the pixel X axis to the pixel Y
axis. If QIN and UIN are both supplied, then the time series specified
by the REF parameter should contain flat-fielded POL2 data. These
values are assumed to incorporate the effect of the 1.35 loss caused
by placing POL2 in the beam. [!]



USEAXIS = LITERAL (Read)
````````````````````````
A set of 2 axes to be selected from the Current Frame in the sky map.
Each axis can be specified either by giving its index within the
Current Frame in the range 1 to the number of axes in the Frame, or by
giving its symbol. This parameter is only accessed if the Current
Frame in the supplied NDF has more than 2 axes. The dynamic default
selects the axes with the same indices as the significant NDF axes.



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKEMAP


Copyright
~~~~~~~~~
Copyright (C) 2011 Science and Technology Facilities Council.
Copyright (C) 2015-2017 East Asian Observatory. All Rights Reserved.


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


