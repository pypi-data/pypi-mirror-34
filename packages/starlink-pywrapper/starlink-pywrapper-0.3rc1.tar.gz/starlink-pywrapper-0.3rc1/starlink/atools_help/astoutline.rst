

ASTOUTLINE
==========


Purpose
~~~~~~~
Create a new Polygon outling values in a 2D NDF


Description
~~~~~~~~~~~
This application creates a Polygon enclosing a single contiguous set
of pixels that have a specified value within a 2-dimensional NDF.
By default, the returned Polygon is defined in the NDF PIXEL
coordinate system, but can be mapped into the current Frame of the NDF
using parameter CURRENT.
The MAXERR and MAXVERT parameters can be used to control how
accurately the returned Polygon represents the required region in the
data array. The number of vertices in the returned Polygon will be the
minimum needed to achieve the required accuracy.


Usage
~~~~~


::

    
       astoutline value oper array maxerr maxvert inside result
       



ADAM parameters
~~~~~~~~~~~~~~~



ARRAY = NDF (Read)
``````````````````
A 2-dimensional NDF containing the data to be processed.



CURRENT = _LOGICAL (Read)
`````````````````````````
If TRUE, then the polygon is mapped into the current frame of the
supplied NDF before being returned. Otherwise, it is left in PIXEL
coordinates as created by the astOutline function. [FALSE]



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



INSIDE( 2 ) = _INTEGER (Read)
`````````````````````````````
The indices of a pixel known to be inside the required region. This is
needed because the supplied data array may contain several disjoint
areas of pixels that satisfy the criterion specified by VALUE and
OPER. In such cases, the area described by the returned Polygon will
be the one that contains the pixel specified by INSIDE. If a null (!)
value is supplied, or if the specified pixel is outside the bounds of
the NDF given by paramater ARRAY, or has a value that does not meet
the criterion specified by VALUE and OPER, then this routine will
search for a suitable pixel. The search starts at the central pixel
and proceeds in a spiral manner until a pixel is found that meets the
specified crierion.



MAXERR = _DOUBLE (Read)
```````````````````````
Together with MAXVERT, this determines how accurately the returned
Polygon represents the required region of the data array. It gives the
maximum allowed discrepancy between the returned Polygon and the
accurate outline in the datta array, expressed as a number of pixels.
If this is zero or less, the returned Polygon will have the number of
vertices specified by MAXVERT. Note, this value should be expressed in
units of pixels even if parameter CURRENT is set TRUE.



MAXVERT = _INTEGER (Read)
`````````````````````````
Together with MAXERR, this determines how accurately the returned
Polygon represents the required region of the data array. It gives the
maximum allowed number of vertices in the returned Polygon. If this is
less than 3, the number of vertices in the returned Polygon will be
the minimum needed to achieve the maximum discrepancy specified by
MAXERR.



NVERT = _INTEGER (Write)
````````````````````````
The number of vertices in the returned polygon.



OPER = LITERAL (Given)
``````````````````````
Indicates how the VALUE parameter is used to select the outlined
pixels. It can have any of the following values:

+ "LT": outline pixels with value less than VALUE.
+ "LE": outline pixels with value less than or equal to VALUE.
+ "EQ": outline pixels with value equal to VALUE.
+ "NE": outline pixels with value not equal to VALUE.
+ "GE": outline pixels with value greater than or equal to VALUE.
+ "GT": outline pixels with value greater than VALUE.





RESULT = LITERAL (Read)
```````````````````````
An text file to receive the new Polygon.



VALUE = _DOUBLE (Read)
``````````````````````
A data value that specifies the pixels to be outlined, or "bad".



Copyright
~~~~~~~~~
Copyright (C) 2009,2014 Science & Technology Facilities Council. All
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


