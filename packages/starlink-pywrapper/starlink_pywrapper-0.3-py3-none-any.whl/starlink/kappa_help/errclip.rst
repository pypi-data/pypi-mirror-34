

ERRCLIP
=======


Purpose
~~~~~~~
Removes pixels with large errors from an NDF


Description
~~~~~~~~~~~
This application produces a copy of the input NDF in which pixels with
errors greater than a specified limit are set invalid in both DATA and
VARIANCE components. The error limit may be specified as the maximum
acceptable standard deviation (or variance), or the minimum acceptable
signal-to-noise ratio.


Usage
~~~~~


::

    
       errclip in out limit [mode]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF. An error is reported if it contains no VARIANCE
component.



OUT = NDF (Write)
`````````````````
The output NDF.



LIMIT = _DOUBLE (Read)
``````````````````````
Either the maximum acceptable standard deviation or variance value, or
the minimum acceptable signal-to-noise ratio (depending on the value
given for MODE). It must be positive.



MODE = LITERAL (Read)
`````````````````````
Determines how the value supplied for LIMIT is to be interpreted:
"Sigma" for a standard deviation, "Variance" for variance, or "SNR"
for minimum signal-to-noise ratio. ["Sigma"]



Examples
~~~~~~~~
errclip m51 m51_good 2.0
The NDF m51_good is created holding a copy of m51 in which all pixels
with standard deviation greater than 2 are set invalid.
errclip m51 m51_good 2.0 snr
The NDF m51_good is created holding a copy of m51 in which all pixels
with a signal-to-noise ratio less than 2 are set invalid.
errclip m51 m51_good mode=v limit=100
The NDF m51_good is created holding a copy of m51 in which all pixels
with a variance greater than 100 are set invalid.



Notes
~~~~~


+ The limit and the number of rejected pixels are reported.
+ A pair of output data and variance values are set bad when either of
the input data or variances values is bad.
+ For MODE="SNR" the comparison is with respect to the absolute data
  value.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FFCLEAN, PASTE, SEGMENT, SETMAGIC, THRESH.


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
LABEL, TITLE, UNITS, WCS and HISTORY components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. The output NDF
  has the same numeric type as the input NDF. However, all internal
  calculations are performed in double precision.




