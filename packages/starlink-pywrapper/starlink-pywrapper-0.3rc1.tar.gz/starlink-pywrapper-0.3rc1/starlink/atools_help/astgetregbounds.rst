

ASTGETREGBOUNDS
===============


Purpose
~~~~~~~
Returns the bounding box of Region


Description
~~~~~~~~~~~
This application returns the upper and lower limits of a box which
just encompasses the supplied Region. The limits are returned as axis
values within the Frame represented by the Region. The value of the
Negated attribute is ignored (i.e. it is assumed that the Region has
not been negated).
The corresponding AST function is AST_GETREGIONBOUDS, but the name has
been contracted to "astgetregbounds" for the purposes of this ATOOLS
command in order not to exceed the allowed length of HDS component
names.


Usage
~~~~~


::

    
       ast_getregbounds this
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



LBND() = _DOUBLE (Write)
````````````````````````
An array in which to return the lower axis bounds covered by the
Region. It should have at least as many elements as there are axes in
the Region. If an axis has no lower limit, the returned value will be
the largest possible negative value.



THIS = LITERAL (Read)
`````````````````````
A text file holding the Region.



UBND() = _DOUBLE (Write)
````````````````````````
An array in which to return the upper axis bounds covered by the
Region. It should have at least as many elements as there are axes in
the Region. If an axis has no upper limit, the returned value will be
the largest possible positive value.



Copyright
~~~~~~~~~
Copyright (C) 2007 Science & Technology Facilities Council. All Rights
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


