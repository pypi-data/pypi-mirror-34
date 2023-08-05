

ASTPERMMAP
==========


Purpose
~~~~~~~
Create a PermMap


Description
~~~~~~~~~~~
This application creates a new PermMap and optionally initialises its
attributes. A PermMap is a Mapping which permutes the order of
coordinates, and possibly also changes the number of coordinates,
between its input and output.
In addition to permuting the coordinate order, a PermMap may also
assign constant values to coordinates. This is useful when the number
of coordinates is being increased as it allows fixed values to be
assigned to any new ones.


Usage
~~~~~


::

    
       astpermmap inperm outperm constant options results
       



ADAM parameters
~~~~~~~~~~~~~~~



CONSTANT() = _DOUBLE (Read)
```````````````````````````
An array containing values which may be assigned to input and/or
output coordinates instead of deriving them from other coordinate
values. If either of the INPERM or OUTPERM arrays contains a negative
value, it is used to address this CONSTANT array (such that -1
addresses the first element, -2 addresses the second element, etc.)
and the value obtained is used as the corresponding coordinate value.
Care should be taken to ensure that locations lying outside the extent
of this array are not accidentally addressed. The array is not used if
the INPERM and OUTPERM arrays do not contain negative values. Supply a
null value (!) if no constants are needed.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



INPERM() = _INTEGER (Read)
``````````````````````````
An array of integers which, for each input coordinate, should contain
the number of the output coordinate whose value is to be used (note
that this array therefore defines the inverse coordinate
transformation). Coordinates are numbered starting from 1.
For details of additional special values that may be used in this
array, see the description of the CONSTANT parameter.



OUTPERM() = _INTEGER (Read)
```````````````````````````
An array which, for each output coordinate, should contain the number
of the input coordinate whose value is to be used (note that this
array therefore defines the forward coordinate transformation).
Coordinates are numbered starting from 1.
For details of additional special values that may be used in this
array, see the description of the CONSTANT argument.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new PermMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new PermMap.



Notes
~~~~~


+ The number of input coordinates (NIN) for the PermMap is equal to
the number of values supplied for parameter INPERM.
+ The number of output coordinates (NOUT) for the PermMap is equal to
  the number of values supplied for parameter OUTPERM.




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


