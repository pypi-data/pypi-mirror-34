

ASTMAPBOX
=========


Purpose
~~~~~~~
Find a bounding box for a Mapping


Description
~~~~~~~~~~~
This application allows you to find the "bounding box" which just
encloses another box after it has been transformed by a Mapping (using
either its forward or inverse transformation). A typical use might be
to calculate the size of an image after being transformed by a
Mapping.
The routine works on one dimension at a time. When supplied with the
lower and upper bounds of a rectangular region (box) of input
coordinate space, it finds the lowest and highest values taken by a
nominated output coordinate within that region. It also returns the
input coordinates where these bounding values are attained. It should
be used repeatedly to obtain the extent of the bounding box in more
than one dimension.


Usage
~~~~~


::

    
       astmapbox this lbndin ubndin forward coordout
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping. If an NDF is supplied, the
Mapping from the base Frame of the WCS FrameSet to the current Frame
will be used.



LBNDIN() = _DOUBLE (Read)
`````````````````````````
An array with one element for each Mapping input coordinate. This
should contain the lower bound of the input box in each input
dimension. If an NDF was supplied for THIS and FORWARD is true, then a
null (!) value can be supplied in which case a default will be used
corresponding to the GRID cordinates of the bottom left corner of the
bottom left pixel in the NDF (i.e. a value of 0.5 on every grid axis).



UBNDIN() = _DOUBLE (Read)
`````````````````````````
An array with one element for each Mapping input coordinate. This
should contain the upper bound of the input box in each input
dimension. Note that it is permissible for the upper bound to be less
than the corresponding lower bound, as the values will simply be
swapped before use. If an NDF was supplied for THIS and FORWARD is
true, then a null (!) value can be supplied in which case a default
will be used corresponding to the GRID cordinates of the top right
corner of the top right pixel in the NDF (i.e. a value of (DIM+0.5) on
every grid axis, where DIM is the number of pixels along the axis).



FORWARD = _LOGICAL (Read)
`````````````````````````
If this value is TRUE, then the Mapping's forward transformation will
be used to transform the input box. Otherwise, its inverse
transformation will be used.
(If the inverse transformation is selected, then references to "input"
and "output" coordinates in this description should be transposed. For
example, the size of the LBNDIN and UBNDIN arrays should match the
number of output coordinates, as given by the Mapping's Nout
attribute. Similarly, the COORDOUT argument, below, should nominate
one of the Mapping's input coordinates.)



COORDOUT = _INTEGER (Read)
``````````````````````````
The index of the output coordinate for which the lower and upper
bounds are required. This value should be at least one, and no larger
than the number of Mapping output coordinates.



LBNDOUT = _DOUBLE (Write)
`````````````````````````
The lowest value taken by the nominated output coordinate within the
specified region of input coordinate space.



UBNDOUT = _DOUBLE (Write)
`````````````````````````
The highest value taken by the nominated output coordinate within the
specified region of input coordinate space.



XL() = _DOUBLE (Write)
``````````````````````
An array with one element for each Mapping input coordinate. This will
return the coordinates of an input point (although not necessarily a
unique one) for which the nominated output coordinate attains the
lower bound value returned in LBNDOUT.



XU() = _DOUBLE (Write)
``````````````````````
An array with one element for each Mapping input coordinate. This will
return the coordinates of an input point (although not necessarily a
unique one) for which the nominated output coordinate attains the
upper bound value returned in UBNDOUT.



Copyright
~~~~~~~~~
Copyright (C) 2002, 2004 Central Laboratory of the Research Councils.
All Rights Reserved.


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


