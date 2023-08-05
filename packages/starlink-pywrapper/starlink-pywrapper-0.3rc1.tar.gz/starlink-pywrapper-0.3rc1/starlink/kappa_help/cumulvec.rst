

CUMULVEC
========


Purpose
~~~~~~~
Sums the values cumulatively in a one-dimensional NDF


Description
~~~~~~~~~~~
This application forms the cumulative sum of the values of a one-
dimensional NDF starting from the first to the last element. thus the
first output pixel will be unchanged but the second will be the sum of
the first two input pixels, third output pixel is the sum of the first
three input pixels and so on. Anomalous values may be excluded from
the summation by setting a threshold.


Usage
~~~~~


::

    
       cumulvec in out [thresh]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The one-dimensional NDF containing the vector to be summed.



OUT = NDF (Write)
`````````````````
The NDF to contain the summed image.



THRESH = _DOUBLE (Read)
```````````````````````
The maximum difference between adjacent elements for the summation to
ocur. For increments outside the allowed range, the increment becomes
zero. If null, !, is given, then there is no limit. [!]



TITLE = LITERAL (Read)
``````````````````````
The title of the output NDF. A null (!) value means using the title of
the input NDF. [!]



Examples
~~~~~~~~
cumulvec gradient profile
The one-dimensional NDF called gradient is summed cumulatively to form
NDF profile.
cumulvec in=gradient out=profile thresh=20
As above but only adjacent values separated by less than 20 are
included in the summation.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISTOGRAM.


Copyright
~~~~~~~~~
Copyright (C) 2006 Central Laboratory of the Research Councils. All
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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS, and HISTORY components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported. Bad pixels are propagated and excluded from the summation.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single- or double-precision floating point as
  appropriate.




