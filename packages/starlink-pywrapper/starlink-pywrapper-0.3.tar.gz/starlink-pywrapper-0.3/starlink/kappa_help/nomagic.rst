

NOMAGIC
=======


Purpose
~~~~~~~
Replaces all occurrences of magic value pixels in an NDF array with a
new value


Description
~~~~~~~~~~~
This function replaces the standard `magic value' assigned to bad
pixels in an NDF with an alternative value, or with random samples
taken from a Normal distribution. Input pixels which do not have the
magic value are left unchanged. The number of replacements is
reported. NOMAGIC's applications include the export of data to
software that has different magic values or does not support bad
values.
If a constant value is used to replace magic values (which will be the
case if parameter SIGMA is given the value zero), then the same
replacement value is used for both the data and variance arrays when
COMP="All". If the variance is being processed, the replacement value
is constrained to be non-negative.
Magic values are replaced by random values if the parameter SIGMA is
given a non-zero value. If both DATA and VARIANCE components are being
processed, then the random values are only stored in the DATA
component; a constant value equal to SIGMA squared is used to replace
all magic values in the VARIANCE component. If only a single component
is being processed (whether it be DATA, VARIANCE, or Error), then the
random values are used to replace the magic values. If random values
are generated which will not fit into the allowed numeric range of the
output NDF, then they are discarded and new random values are obtained
instead. This continues until a useable value is obtained. This could
introduce some statistical bias if many such re-tries are performed.
For this reason SIGMA is restricted so that there are at least 4
standard deviations between the mean (given by REPVAL) and the nearest
limit. NOMAGIC notifies of any re-tries that are required.


Usage
~~~~~


::

    
       nomagic in out repval sigma [comp]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The components whose flagged values are to be substituted. It may be
"Data", "Error", "Variance", or "All". The last of the options forces
substitution of bad pixels in both the data and variance arrays. This
parameter is ignored if the data array is the only array component
within the NDF. ["Data"]



IN = NDF (Read)
```````````````
Input NDF structure containing the data and/or variance array to have
its elements flagged with the magic value replaced by another value.



OUT = NDF (Write)
`````````````````
Output NDF structure containing the data and/or variance array without
any elements flagged with the magic value.



REPVAL = _DOUBLE (Read)
```````````````````````
The constant value to substitute for the magic values, or (if
parameter SIGMA is given a non-zero value) the mean of the
distribution from which replacement values are obtained. It must lie
within the minimum and maximum values of the data type of the array
with higher precision, except when variance is being processed, in
which case the minimum is constrained to be non-negative. The
replacement value is converted to the data type of the array being
converted. The suggested default is the current value.



SIGMA = _DOUBLE (Read)
``````````````````````
The standard deviation of the random values used to replace magic
values in the input NDF. If this is zero (or if a null value is
given), then a constant replacement value is used. The supplied value
must be positive and must be small enough to allow at least 4 standard
deviations between the mean value (given by REPVAL) and the closest
limit. [!]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



Examples
~~~~~~~~
nomagic aitoff irasmap repval=-2000000
This copies the NDF called aitoff to the NDF irasmap, except that any
bad values in the data array are replaced with the IPAC blank value,
-2000000, in the NDF called irasmap.
nomagic saturnb saturn 9999.0 comp=all
This copies the NDF called saturnb to the NDF saturn, except that any
bad values in the data and variance arrays are replaced with 9999 in
the NDF called saturn.
nomagic in=cleaned out=filled repval=0 sigma=10 comp=all
This copies the NDF called cleaned to the NDF filled, except that any
bad values in the data array are replaced by random samples taken from
a Normal distribition of mean zero and standard deviation 10. Bad
values in the variance array are replaced by the constant value 100.



Notes
~~~~~


+ If the NDF arrays have no bad pixels the application will abort.
+ Use GLITCH if a neighbourhood context is required to remove the bad
  values.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CHPIX, FILLBAD, GLITCH, SEGMENT, SETMAGIC, SUBSTITUTE, ZAPLIN;
SPECDRE: GOODVAR.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1994 Science & Engineering Research Council.
Copyright (C) 1998-1999, 2002, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2012 Science & Technology Facilities Council.
All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




