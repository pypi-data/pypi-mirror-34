

ASTCHEBYDOMAIN
==============


Purpose
~~~~~~~
Returns the bounding box of the domain of a ChebyMap


Description
~~~~~~~~~~~
This application returns the upper and lower limits of the box
defining the domain of either the forward or inverse transformation of
a ChebyMap. These are the values that were supplied when the ChebyMap
was created.


Usage
~~~~~


::

    
       astchebydomain this forward
       



ADAM parameters
~~~~~~~~~~~~~~~



FORWARD = _LOGICAL (Read)
`````````````````````````
A TRUE value indicates that the domain of the ChebyMap's forward
transformation is to be returned, while a FALSE value indicates that
the domain of the inverse transformation should be returned.



LBND() = _DOUBLE (Write)
````````````````````````
An array in which to return the lower axis bounds of the ChebyMap
domain. The number of elements should be at least equal to the number
of ChebyMap inputs (if FORWARD is .TRUE.), or outputs (if FORWARD is
.FALSE.).



THIS = LITERAL (Read)
`````````````````````
A text file holding the Region.



UBND() = _DOUBLE (Write)
````````````````````````
An array in which to return the upper axis bounds of the ChebyMap
domain. The number of elements should be at least equal to the number
of ChebyMap inputs (if FORWARD is .TRUE.), or outputs (if FORWARD is
.FALSE.).



Copyright
~~~~~~~~~
Copyright (C) 2017 East Asian Observatory. All Rights Reserved.


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


