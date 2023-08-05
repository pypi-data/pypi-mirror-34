

ASTCIRCLE
=========


Purpose
~~~~~~~
Create a Circle


Description
~~~~~~~~~~~
This application creates a new Circle and optionally initialises its
attributes. The Circle class implements a Region which represents a
circle or sphere within a Frame.


Usage
~~~~~


::

    
       astcircle frame form centre point unc options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FRAME = LITERAL (Read)
``````````````````````
An NDF or text file holding the Frame in which the region is defined.
If an NDF is supplied, the current Frame in its WCS FrameSet will be
used.



FORM = _INTEGER (Read)
``````````````````````
Indicates how the circle is described by the remaining parameters. A
value of zero indicates that the circle is specified by a centre
position and a position on the circumference. A value of one indicates
that the circle is specified by a centre position and a scalar radius.



CENTRE() = _DOUBLE (Read)
`````````````````````````
An array with one element for each Frame axis (Naxes attribute)
containing the coordinates at the centre of the circle or sphere.



POINT() = _DOUBLE (Read)
````````````````````````
If FORM is zero, then this array should have one element for each
Frame axis (Naxes attribute), and should be supplied holding the
coordinates at a point on the circumference of the circle or sphere.
If FORM is one, then this array should have one element only which
should be supplied holding the scalar radius of the circle or sphere,
as a geodesic distance within the Frame.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new Circle.



RESULT = LITERAL (Read)
```````````````````````
An text file to receive the new Circle.



UNC = LITERAL (Read)
````````````````````
An optional text file containing an existing Region which specifies
the uncertainties associated with each point on the boundary of the
Circle being created. The uncertainty at any point on the Circle is
found by shifting the supplied "uncertainty" Region so that it is
centred at the point being considered. The area covered by the shifted
uncertainty Region then represents the uncertainty in the position.
The uncertainty is assumed to be the same for all points.
If supplied, the uncertainty Region must be either a Box, a Circle or
an Circle. Alternatively, a null value (!) may be supplied, in which
case a default uncertainty is used equivalent to a box 1.0E-6 of the
size of the bounding box of the Circle being created.
The uncertainty Region has two uses: 1) when the astOverlap function
compares two Regions for equality the uncertainty Region is used to
determine the tolerance on the comparison, and 2) when a Region is
mapped into a different coordinate system and subsequently simplified
(using astSimplify), the uncertainties are used to determine if the
transformed boundary can be accurately represented by a specific shape
of Region.



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


