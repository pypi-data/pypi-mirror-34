

EXCLUDEBAD
==========


Purpose
~~~~~~~
Excludes bad rows or columns from a two-dimensional NDF


Description
~~~~~~~~~~~
This application produces a copy of a two-dimensional NDF, but
excludes any rows that contain too many bad data values. Rows with
higher pixel indices are shuffled down to fill the gaps left by the
omission of bad rows. Thus if any bad rows are found, the output NDF
will have fewer rows than the input NDF, but the order of the
remaining rows will be unchanged. The number of good pixels required
in a row for the row to be retained is specified by Parameter WLIM.
Bad columns may be omitted instead of bad rows (see Parameter ROWS).


Usage
~~~~~


::

    
       excludebad in out [rows] [wlim]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input two-dimensional NDF.



OUT = NDF (Write)
`````````````````
The output NDF.



ROWS = _LOGICAL (Read)
``````````````````````
If TRUE, bad rows are excluded from the output NDF. If FALSE, bad
columns are excluded. [TRUE]



WLIM = _REAL (Read)
```````````````````
The minimum fraction of the pixels that must be good in order for a
row to be retained. A value of 1.0 results in rows being excluded if
they contain one or more bad values. A value of 0.0 results in rows
being excluded only if they contain no good values. [0.0]



Examples
~~~~~~~~
excludebad ifuframe goodonly false
Columns within NDF ifuframe that contain any good data are copied to
NDF goodonly.



Notes
~~~~~


+ The lower pixel bounds of the output will be the same as those of
  the input, but the upper pixel bounds will be different if any bad
  rows or columns are excluded.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CHPIX, FILLBAD, GLITCH, NOMAGIC, ZAPLIN; Figaro: BCLEAN, CLEAN,
ISEDIT, REMBAD, TIPPEX.


Copyright
~~~~~~~~~
Copyright (C) 2014 Science & Technology Facilities Council. All Rights
Reserved.


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
  LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
  propagates all extensions.




