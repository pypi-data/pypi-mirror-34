

ASTMASK
=======


Purpose
~~~~~~~
Mask a region of a data grid


Description
~~~~~~~~~~~
This application masks out regions within an NDF. It creates a copy of
the supplied input NDF and then modifies the copy by assigning a
specified value to all samples which are inside (or outside if INSIDE
is FALSE) the specified Region.


Usage
~~~~~


::

    
       astmask this map inside val in out
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



IN = NDF (Read)
```````````````
The input NDF that is to be masked.



INSIDE = _LOGICAL (Read)
````````````````````````
Indicates which pixel of the input NDF are to be masked. If TRUE is
supplied, then all pixels with centres inside the supplied Region are
assigned the value given by parameter VAL, and all other pixels are
left unchanged. If FALSE is supplied, then all pixels with centres not
inside the supplied Region are assigned the value given by VAL, and
all other pixels are left unchanged. Note, the Negated attribute of
the Region is used to determine which pixel are inside the Region and
which are outside. So the inside of a Region which has not been
negated is the same as the outside of the corresponding negated
Region.
For types of Region such as PointList which have zero volume, pixel
centres will rarely fall exactly within the Region. For this reason,
the inclusion criterion is changed for zero-volume Regions so that
pixels are included (or excluded) if any part of the Region passes
through the pixel. For a PointList, this means that pixels are
included (or excluded) if they contain at least one of the points
listed in the PointList.



MAP = LITERAL (Read)
````````````````````
An NDF or text file holding a Mapping (if an NDF is supplied, the
Mapping from PIXEL coordinates to the Current WCS Frame is used). The
inverse (note, inverse) transformation is used to map positions in the
coordinate system of the supplied Region into PIXEL coordinates of the
input NDF. A null (!) value can be supplied if the coordinate system
of the supplied Region corresponds to PIXEL coordinates. This is
equivalent to supplying a UnitMap.
The number of inputs for this Mapping (as given by its Nin attribute)
should match the number of axes in the supplied Region (as given by
the Naxes attribute of the Region). The number of outputs for the
Mapping (as given by its Nout attribute) should match the number of
pixel axes in the input NDF.
Note, in this context "pixel coordinates" are standard NDF pixel
coordinates. The AST_GRID function within the AST library uses a
slightly different form of pixel coordinates (it assumes integral
values are at the centre rather than the corners of each pixel) and so
requires a slightly different Mapping.
The suggested default is the input NDF. If accepted, this default
means that he supplied Region is assumed to be defined in the current
WCS Frame of the supplied NDF.



OUT = NDF (Read)
````````````````
The output NDF.



RESULT = _INTEGER (Write)
`````````````````````````
The number of output pixels that were modified.



THIS = LITERAL (Read)
`````````````````````
A text file holding the Region to use.



VAL = _DOUBLE (Read)
````````````````````
The value used to flag values in the output NDF (see parameter
INSIDE). This can also be "Bad".



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


