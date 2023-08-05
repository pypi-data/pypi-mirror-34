

ASTINTERVAL
===========


Purpose
~~~~~~~
Create a Interval


Description
~~~~~~~~~~~
This application creates a new Interval and optionally initialises its
attributes.
The Interval class implements a Region which represents upper and/or
lower limits on one or more axes of a Frame. For a point to be within
the region represented by the Interval, the point must satisfy all the
restrictions placed on all the axes. The point is outside the region
if it fails to satisfy any one of the restrictions. Each axis may have
either an upper limit, a lower limit, both or neither. If both limits
are supplied but are in reverse order (so that the lower limit is
greater than the upper limit), then the interval is an excluded
interval, rather than an included interval.


Usage
~~~~~


::

    
       astinterval frame lbnd ubnd unc options result
       



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



LBND = GROUP (Read)
```````````````````
A comma-separated list of floating point values to be used as the
lower limits on each axis. Set a value to "AST__BAD" to indicate that
the axis has no lower limit. There should be one element for each
Frame axis.



UBND = GROUP (Read)
```````````````````
A comma-separated list of floating point values to be used as the
upper limits on each axis. Set a value to "AST__BAD" to indicate that
the axis has no upper limit. There should be one element for each
Frame axis.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new Interval.



RESULT = LITERAL (Read)
```````````````````````
An text file to receive the new Interval.



UNC = LITERAL (Read)
````````````````````
An optional text file containing an existing Region which specifies
the uncertainties associated with each point on the boundary of the
Interval being created. The uncertainty at any point on the Interval
is found by shifting the supplied "uncertainty" Region so that it is
centred at the point being considered. The area covered by the shifted
uncertainty Region then represents the uncertainty in the position.
The uncertainty is assumed to be the same for all points.
If supplied, the uncertainty Region must be either a Box, a Circle or
an Ellipse. Alternatively, a null value (!) may be supplied, in which
case a default uncertainty is used equivalent to a box 1.0E-6 of the
size of the bounding box of the Interval being created.
The uncertainty Region has two uses: 1) when the astOverlap function
compares two Regions for equality the uncertainty Region is used to
determine the tolerance on the comparison, and 2) when a Region is
mapped into a different coordinate system and subsequently simplified
(using astSimplify), the uncertainties are used to determine if the
transformed boundary can be accurately represented by a specific shape
of Region.



Copyright
~~~~~~~~~
Copyright (C) 2006 Particle Physics & Astronomy Research Council. All
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


