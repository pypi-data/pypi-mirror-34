

ASTDOWNSIZE
===========


Purpose
~~~~~~~
Reduce the number of vertices in a Polygon


Description
~~~~~~~~~~~
This application returns a pointer to a new Polygon that contains a
subset of the vertices in the supplied Polygon. The subset is chosen
so that the returned Polygon is a good approximation to the supplied
Polygon, within the limits specified by the supplied parameter values.
That is, the density of points in the returned Polygon is greater at
points where the curvature of the boundary of the supplied Polygon is
greater.


Usage
~~~~~


::

    
       astdownsize this maxerr maxvert result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



MAXERR = _DOUBLE (Read)
```````````````````````
The maximum allowed discrepancy between the supplied and returned
Polygons, expressed as a geodesic distance within the Polygon's
coordinate frame. If this is zero or less, the returned Polygon will
have the number of vertices specified by MAXVERT.



MAXVERT = _INTEGER (Read)
`````````````````````````
The maximum allowed number of vertices in the returned Polygon. If
this is less than 3, the number of vertices in the returned Polygon
will be the minimum needed to achieve the maximum discrepancy
specified by MAXERR.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the modified Polygon.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping. If an NDF is supplied, the
current Frame in the WCS FrameSet will be used.



Copyright
~~~~~~~~~
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
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


