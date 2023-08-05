

ASTSPHMAP
=========


Purpose
~~~~~~~
Create a SphMap


Description
~~~~~~~~~~~
This application creates a new SphMap and optionally initialises its
attributes. A SphMap is a Mapping which transforms points from a
3-dimensional Cartesian coordinate system into a 2-dimensional
spherical coordinate system (longitude and latitude on a unit sphere
centred at the origin). It works by regarding the input coordinates as
position vectors and finding their intersection with the sphere
surface. The inverse transformation always produces points which are a
unit distance from the origin (i.e. unit vectors).


Usage
~~~~~


::

    
       astunitmap options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new SphMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new SphMap.



Copyright
~~~~~~~~~
Copyright (C) 2013 Science & Technology Facilities Council. All Rights
Reserved.


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


