

ASTWINMAP
=========


Purpose
~~~~~~~
Create a WinMap


Description
~~~~~~~~~~~
This application creates a new WinMap and optionally initialises its
attributes. A Winmap is a linear Mapping which transforms a
rectangular window in one coordinate system into a similar window in
another coordinate system by scaling and shifting each axis (the
window edges being parallel to the coordinate axes).
A WinMap is specified by giving the coordinates of two opposite
corners (A and B) of the window in both the input and output
coordinate systems.


Usage
~~~~~


::

    
       astwinmap ncoord ina inb outa outb options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



INA() = _DOUBLE (Read)
``````````````````````
The coordinates of corner A of the window in the input coordinate
system.



INB() = _DOUBLE (Read)
``````````````````````
The coordinates of corner B of the window in the input coordinate
system.



NCOORD = _INTEGER (Read)
````````````````````````
The number of coordinate values for the WinMap (the same value is used
for both input and output axes).



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new WinMap.



OUTA() = _DOUBLE (Read)
```````````````````````
The coordinates of corner A of the window in the output coordinate
system.



OUTB() = _DOUBLE (Read)
```````````````````````
The coordinates of corner B of the window in the output coordinate
system.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new WinMap.



Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils. All
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


