

ASTUNITMAP
==========


Purpose
~~~~~~~
Create a UnitMap


Description
~~~~~~~~~~~
This application creates a new UnitMap and optionally initialises its
attributes. A UnitMap is a unit (null) Mapping that has no effect on
the coordinates supplied to it. They are simply copied.


Usage
~~~~~


::

    
       astunitmap ncoord options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



NCOORD = _INTEGER (Read)
````````````````````````
The number of input and output coordinates (these numbers are
necessarily the same).



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new UnitMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new UnitMap.



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


