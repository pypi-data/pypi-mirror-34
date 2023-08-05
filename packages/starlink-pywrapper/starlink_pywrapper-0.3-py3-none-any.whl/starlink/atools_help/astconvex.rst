

ASTCONVEX
=========


Purpose
~~~~~~~
Create a new Polygon representing the convex hull of a 2D data grid


Description
~~~~~~~~~~~
This application creates the shortest Polygon that encloses all pixels
with a specified value within a 2-dimensional NDF.
By default, the returned Polygon is defined in the NDF PIXEL
coordinate system, but can be mapped into the current Frame of the NDF
using parameter CURRENT.


Usage
~~~~~


::

    
       astconvex value oper array result
       



ADAM parameters
~~~~~~~~~~~~~~~



ARRAY = NDF (Read)
``````````````````
A 2-dimensional NDF containing the data to be processed.



CURRENT = _LOGICAL (Read)
`````````````````````````
If TRUE, then the polygon is mapped into the current frame of the
supplied NDF before being returned. Otherwise, it is left in PIXEL
coordinates as created by the astConvex function. [FALSE]



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



NVERT = _INTEGER (Write)
````````````````````````
The number of vertices in the returned polygon.



OPER = LITERAL (Given)
``````````````````````
Indicates how the VALUE parameter is used to select the included
pixels. It can have any of the following values:

+ "LT": include pixels with value less than VALUE.
+ "LE": include pixels with value less than or equal to VALUE.
+ "EQ": include pixels with value equal to VALUE.
+ "NE": include pixels with value not equal to VALUE.
+ "GE": include pixels with value greater than or equal to VALUE.
+ "GT": include pixels with value greater than VALUE.





RESULT = LITERAL (Read)
```````````````````````
An text file to receive the new Polygon.



VALUE = _DOUBLE (Read)
``````````````````````
A data value that specifies the pixels to be outlined, or "bad".



Copyright
~~~~~~~~~
Copyright (C) 2014 Science & Technology Facilities Council. All Rights
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


