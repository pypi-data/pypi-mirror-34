

ODDEVEN
=======


Purpose
~~~~~~~
Removes odd-even defects from a one-dimensional NDF


Description
~~~~~~~~~~~
This application forms a smoothed signal for a one-dimensional NDF
whose elements have oscillating biases. It averages the signal levels
of alternating pixels. Both elements must be good and not deviate from
each other by more than a threshold for the averaging to take place.
This application is intended for images exhibiting alternating
patterns in columns or rows, the so called odd-even noise, arising
from electronic interference or readout through different channels.
However, you must supply a vector collapsed along the unaffected axis,
such that the vector exhibits the pattern. See task COLLAPSE using the
Mode or Median estimators. The smoothed image is then subtracted from
the supplied vector to yield the odd-even pattern.


Usage
~~~~~


::

    
       oddeven in out [thresh]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The one-dimensional NDF containing the input array to be filtered.



OUT = NDF (Write)
`````````````````
The NDF to contain the filtered image.



THRESH = _DOUBLE (Read)
```````````````````````
The maximum difference between adjacent elements for the averaging
filter to be applied. This allows anomalous pixels to be excluded. If
null, !, is given, then there is no limit. [!]



TITLE = LITERAL (Read)
``````````````````````
The title of the output NDF. A null (!) value means using the title of
the input NDF. [!]



Examples
~~~~~~~~
oddeven raw clean
The one-dimensional NDF called raw is filtered such that adjacent
pixels are averaged to form the output NDF call clean.
oddeven out=clean in=raw thresh=20
As above except only those adjacent pixels whose values differ by no
more than 20 are averaged.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: BLOCK, CHPIX, FFCLEAN, GLITCH, ZAPLIN; Figaro: BCLEAN, CLEAN,
ISEDIT, TIPPEX.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL,
TITLE, UNITS, WCS, and HISTORY components of an NDF data structure and
propagates all extensions.
+ VARIANCE is merely propagated.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single- or double-precision floating point as
  appropriate.




