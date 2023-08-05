

CALPOL
======


Purpose
~~~~~~~
Calculates polarisation parameters


Description
~~~~~~~~~~~
This routine calculates various parameters describing the polarisation
described by four intensity arrays analysed at 0, 45, 90, and 135
degrees to a reference direction. Variance values are stored in the
output NDFs if all the input NDFs have variances and you give a true
value for parameter VARIANCE.
By default, three output NDFs are created holding percentage
polarisation, polarisation angle and total intensity. However, NDFs
holding other quantities, such as the Stokes parameters, can also be
produced by over-riding the default null values associated with the
corresponding parameters. The creation of any output NDF can be
suppressed by supplying a null value for the corresponding parameter.
There is an option to correct the calculated values of percentage
polarisation and polarised intensity to take account of the
statistical bias introduced by the asymmetric distribution of
percentage polarisation (see parameter DEBIAS). This correction
subtracts the variance of the percentage polarisation from the squared
percentage polarisation, and uses the square root of this as the
corrected percentage polarisation. The corresponding polarised
intensity is then found by multiplying the corrected percentage
polarisation by the total intensity. Returned variance values take no
account of this correction.


Usage
~~~~~


::

    
       calpol in1 in2 in3 in4 p theta i
       



ADAM parameters
~~~~~~~~~~~~~~~



DEBIAS = _LOGICAL (Read)
````````````````````````
TRUE if a correction for statistical bias is to be made to percentage
polarisation and polarised intensity. This correction cannot be used
if any of the input NDFs do not contain variance values, or if you
supply a FALSE value for parameter VARIANCE. [FALSE]



I = NDF (Write)
```````````````
An output NDF holding the total intensity derived from all four input
NDFs.



IN1 = NDF (Read)
````````````````
An NDF holding the measured intensity analysed at an angle of 0
degrees to the reference direction. The primary input NDF.



IN2 = NDF (Read)
````````````````
An NDF holding the measured intensity analysed at an angle of 45
degrees to the reference direction. The suggested default is the
current value.



IN3 = NDF (Read)
````````````````
An NDF holding the measured intensity analysed at an angle of 90
degrees to the reference direction. The suggested default is the
current value.



IN4 = NDF (Read)
````````````````
An NDF holding the measured intensity analysed at an angle of 135
degrees to the reference direction. The suggested default is the
current value.



IA = NDF (Write)
````````````````
An output NDF holding the total intensity derived from input NDFs IN1
and IN3. [!]



IB = NDF (Write)
````````````````
An output NDF holding the total intensity derived from input NDFs IN2
and IN4. [!]



IP = NDF (Write)
````````````````
An output NDF holding the polarised intensity. [!]



P = NDF (Write)
```````````````
An output NDF holding percentage polarisation.



Q = NDF (Write)
```````````````
An output NDF holding the normalised Stokes parameter, Q. [!]



U = NDF (Write)
```````````````
An output NDF holding the normalised Stokes parameter, U. [!]



THETA = NDF (Write)
```````````````````
An output NDF holding the polarisation angle in degrees.



VARIANCE = _LOGICAL (Read)
``````````````````````````
TRUE if output variances are to be calculated. This parameter is only
accessed if all input NDFs contain variances, otherwise no variances
are generated. [TRUE]



Examples
~~~~~~~~
calpol m51_0 m51_45 m51_90 m51_135 m51_p m51_t m51_i ip=m51_ip
This example produces NDFs holding percentage polarisation,
polarisation angle, total intensity and polarised intensity, based on
the four NDFs M51_0, m51_45, m51_90 and m51_135.
calpol m51_0 m51_45 m51_90 m51_135 m51_p m51_t m51_i ip=m51_ip

novariance
As above except that variance arrays are not computed.
calpol m51_0 m51_45 m51_90 m51_135 m51_p m51_t m51_i ip=m51_ip
As the first example except that there is a correction for statistical
bias in the percentage polarisation and polarised intensity, assuming
that all the input NDFs have a VARIANCE array.
calpol m51_0 m51_45 m51_90 m51_135 q=m51_q p=m51_p
This example produces NDFs holding the Stokes Q and U parameters,
again based on the four NDFs M51_0, m51_45, m51_90 and m51_135.



Notes
~~~~~


+ A bad value will appear in the output data and variance arrays when
any of the four input data values is bad, or if the total intensity in
the pixel is not positive. The output variance values are also
undefined when any of the four input variances is bad or negative, or
any computed variance is not positive, or the percentage polarisation
is not positive.
+ If the four input NDFs have different pixel-index bounds, then they
will be trimmed to match before being added. An error will result if
they have no pixels in common.
+ The output NDFs are deleted if there is an error during the
formation of the polarisation parameters.
+ The output NDFs obtain their QUALITY, AXIS information, and TITLE
  from the IN1 NDF. The following labels and units are also assigned: I
  "Total Intensity" UNITS of IN1 IA "Total Intensity" UNITS of IN1 IB
  "Total Intensity" UNITS of IN1 IP "Polarised Intensity" UNITS of IN1 P
  "Percentage Polarisation" "%" Q "Stokes Q" --- U "Stokes U" --- THETA
  "Polarisation Angle" "Degrees"




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: VECPLOT; IRCAMPACK: POLCAL, POLMAPC, POLMAPD, POLSKY,
POLSMOOTH, POLZAP; TSP.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2004 Central Laboratory of the Research Councils. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point.




