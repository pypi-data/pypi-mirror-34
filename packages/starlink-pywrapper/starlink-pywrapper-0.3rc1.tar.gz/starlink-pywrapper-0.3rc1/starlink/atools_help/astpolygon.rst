

ASTPOLYGON
==========


Purpose
~~~~~~~
Create a Polygon


Description
~~~~~~~~~~~
This application creates a new Polygon and optionally initialises its
attributes. The Polygon class implements a polygonal area, defined by
a collection of vertices, within a 2-dimensional Frame. The vertices
are connected together by geodesic curves within the encapsulated
Frame. For instance, if the encapsulated Frame is a simple Frame then
the geodesics will be straight lines, but if the Frame is a SkyFrame
then the geodesics will be great circles.


Usage
~~~~~


::

    
       astpolygon frame xin yin unc options result
       



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
It must have exactly 2 axes. If an NDF is supplied, the current Frame
in its WCS FrameSet will be used.



XIN = GROUP (Read)
``````````````````
A comma-separated list of floating point values to be used as the X
axis value of the vertices. A text file may be specified by preceeding
the name of the file with an up arrow character "^". If the supplied
value ends with a minus sign, the user is re-prompted for additional
values.



YIN = GROUP (Read)
``````````````````
A comma-separated list of floating point values to be used as the Y
axis value of the vertices. A text file may be specified by preceeding
the name of the file with an up arrow character "^". If the supplied
value ends with a minus sign, the user is re-prompted for additional
values.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new Polygon.



RESULT = LITERAL (Read)
```````````````````````
An text file to receive the new Polygon.



UNC = LITERAL (Read)
````````````````````
An optional text file containing an existing Region which specifies
the uncertainties associated with each point on the boundary of the
Polygon being created. The uncertainty at any point on the Polygon is
found by shifting the supplied "uncertainty" Region so that it is
centred at the point being considered. The area covered by the shifted
uncertainty Region then represents the uncertainty in the position.
The uncertainty is assumed to be the same for all points.
If supplied, the uncertainty Region must be either a Box, a Circle or
an Ellipse. Alternatively, a null value (!) may be supplied, in which
case a default uncertainty is used equivalent to a box 1.0E-6 of the
size of the bounding box of the Polygon being created.
The uncertainty Region has two uses: 1) when the astOverlap function
compares two Regions for equality the uncertainty Region is used to
determine the tolerance on the comparison, and 2) when a Region is
mapped into a different coordinate system and subsequently simplified
(using astSimplify), the uncertainties are used to determine if the
transformed boundary can be accurately represented by a specific shape
of Region.



Copyright
~~~~~~~~~
Copyright (C) 2005 Particle Physics & Astronomy Research Council. All
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


