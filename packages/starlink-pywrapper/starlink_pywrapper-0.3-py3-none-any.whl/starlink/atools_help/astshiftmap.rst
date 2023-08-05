

ASTSHIFTMAP
===========


Purpose
~~~~~~~
Create a ShiftMap


Description
~~~~~~~~~~~
This application creates a new ShiftMap and optionally initialises its
attributes. A Winmap is a linear Mapping which transforms a
rectangular window in one coordinate system into a similar window in
another coordinate system by shifting each axis (the window edges
being parallel to the coordinate axes). Thus, a ShiftMap is equivalent
to a WinMap with unit scaling on each axis.


Usage
~~~~~


::

    
       astshiftmap ncoord shift options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



SHIFT() = _DOUBLE (Read)
````````````````````````
The values to be added to each axis of the input coordinate system.
There should be one value for each coordinate axis.



NCOORD = _INTEGER (Read)
````````````````````````
The number of coordinate values for the ShiftMap (the same value is
used for both input and output axes).



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new ShiftMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new ShiftMap.



Copyright
~~~~~~~~~
Copyright (C) 2003 Central Laboratory of the Research Councils. All
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


