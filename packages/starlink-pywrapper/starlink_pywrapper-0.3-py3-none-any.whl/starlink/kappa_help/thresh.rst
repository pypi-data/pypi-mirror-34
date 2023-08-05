

THRESH
======


Purpose
~~~~~~~
Edits an NDF to replace values between or outside given limits with
specified constant values


Description
~~~~~~~~~~~
This application creates an output NDF by copying values from an input
NDF, replacing all values within given data ranges by a user-specified
constant or by the bad value. Upper and lower thresholds are supplied
using parameters THRLO and THRHI.
If THRLO is less than or equal to THRHI, values between and including
the two thresholds are copied from the input to output array. Any
values in the input array greater than the upper threshold will be set
to the value of parameter NEWHI, and anything less than the lower
threshold will be set to the value of parameter NEWLO, in the output
data array. Thus the output NDF is constrained to lie between the two
bounds.
If THRLO is greater than THRHI, values greater than or equal to THRLO
are copied from the input to output array, together with values less
than or equal to THRHI. Any values between THRLO and THRHI will be set
to the value of parameter NEWLO in the output NDF.
Each replacement value may be the bad-pixel value for masking.


Usage
~~~~~


::

    
       thresh in out thrlo thrhi newlo newhi [comp]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The components whose values are to be constrained between thresholds.
The options are limited to the arrays within the supplied NDF. In
general the value may be "Data", "Quality", "Error", or "Variance". If
"Quality" is specified, then the quality values are treated as
numerical values in the range 0 to 255. ["Data"]



IN = NDF (Read)
```````````````
Input NDF structure containing the array to have thresholds applied.



NEWHI = LITERAL (Read)
``````````````````````
This gives the value to which all input array-element values greater
than the upper threshold are set. If this is set to "Bad", the bad
value is substituted. Numerical values of NEWHI must lie in within the
minimum and maximum values of the data type of the array being
processed. The suggested default is the upper threshold. This
parameter is ignored if THRLO is greater than THRHI.



NEWLO = LITERAL (Read)
``````````````````````
This gives the value to which all input array-element values less than
the lower threshold are set. If this is set to "Bad", the bad value is
substituted. Numerical values of NEWLO must lie in within the minimum
and maximum values of the data type of the array being processed. The
suggested default is the lower threshold.



NUMHI = _INTEGER (Write)
````````````````````````
The number of pixels whose values were thresholded as being greater
than the THRHI threshold.



NUMLO = _INTEGER (Write)
````````````````````````
The number of pixels whose values were thresholded as being less than
the THRLO threshold.



NUMRANGE = _INTEGER (Write)
```````````````````````````
The number of pixels whose values were thresholded as being between
the THRLO and THRHI thresholds, if THRLO is greater than THRHI.



NUMSAME = _INTEGER (Write)
``````````````````````````
The number of unchanged pixels.



OUT = NDF (Write)
`````````````````
Output NDF structure containing the thresholded version of the array.



THRHI = _DOUBLE (Read)
``````````````````````
The upper threshold value within the input array. It must lie in
within the minimum and maximum values of the data type of the array
being processed. The suggested default is the current value.



THRLO = _DOUBLE (Read)
``````````````````````
The lower threshold value within the input array. It must lie within
the minimum and maximum values of the data type of the array being
processed. The suggested default is the current value.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



Examples
~~~~~~~~
thresh zzcam zzcam2 100 500 0 0
This copies the data array in the NDF called zzcam to the NDF called
zzcam2. Any data value less than 100 or greater than 500 in zzcam is
set to 0 in zzcam2.
thresh zzcam zzcam2 500 100 0
This copies the data array in the NDF called zzcam to the NDF called
zzcam2. Any data value less than 500 and greater than 100 in zzcam is
set to 0 in zzcam2.
thresh zzcam zzcam2 100 500 0 0 comp=Variance
As above except that the data array is copied unchanged and the
thresholds apply to the variance array.
thresh n253 n253cl thrlo=-0.5 thrhi=10.1 \
This copies the data array in the NDF called n253 to the NDF called
n253cl. Any data value less than -0.5 in n253 is set to -0.5 in
n253cl, and any value greater than 10.1 in n253 becomes 10.1 in
n253cl.
thresh pavo pavosky -0.02 0.02 bad bad
All data values outside the range -0.02 to 0.02 in the NDF called pavo
become bad in the NDF called pavosky. All values within this range are
copied from pavo to pavosky.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISTEQ, MATHS; Figaro: CLIP, IDIFF, RESCALE.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1994 Science & Engineering Research Council.
Copyright (C) 1996, 1998, 2000-2001, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2012 Science & Technology Facilities
Council. All Rights Reserved.


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




