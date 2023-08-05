

STACKFRAMES
===========


Purpose
~~~~~~~
Stack 2d processed frames into time series cube


Description
~~~~~~~~~~~
Takes a stack of 2d frames of bolometer data, usually noise images or
responsivity images, and combines them into a single cube with, if
sort is enabled, an annotated time axis or an axis based on a numeric
FITS header item. This makes it easy to look at the behaviour of a
single detector as it varies with time. Not all observations include
time information or should be sorted at all and for those set SORT to
false. The 3rd axis will not be a sorted axis in that case. This can
be useful for examining bolometer maps created by MAKEMAP.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input file(s). Files must all be 2-d and have the same dimensions. For
the SORT option to be available they must have a DATE-OBS FITS header.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Single output file with all the 2d images stacked into a single
observation.



SORT = _LOGICAL (Read)
``````````````````````
Should the data be sorted into time order (true) or left in the order
given in IN (false). If the first file in IN has no date information
sorting will be disabled automatically. Default is true if date
information is available.



SORTBY = _CHAR (Read)
`````````````````````
If the data are sorted (SORT=TRUE) this parameter controls which
header item should be used to do the sorting. Options are MJD (the
date) or the name of a numeric FITS header. MJD is not allowed if no
date items are present. [MJD]



Notes
~~~~~


+ No special SCUBA-2 processing is applied. The assumption is simply
that you have some images that are all the same size and you want to
put them into a single cube with a time axis.
+ Variations in pixel origin are ignored. Make sure images are aligned
and are the same size.
+ Useful for looking at the variations in bolometer parameters such as
  images created by CALCNOISE or CALCFLAT.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: CALCNOISE, CALCFLAT, MAKEMAP


Copyright
~~~~~~~~~
Copyright (C) 2009-2011 Science and Technology Facilities Council. All
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


