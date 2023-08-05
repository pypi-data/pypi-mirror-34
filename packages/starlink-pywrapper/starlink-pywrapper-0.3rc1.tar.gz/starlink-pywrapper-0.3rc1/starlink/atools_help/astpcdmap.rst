

ASTPCDMAP
=========


Purpose
~~~~~~~
Create a PcdMap


Description
~~~~~~~~~~~
This application creates a new PcdMap and optionally initialises its
attributes. A PcdMap is a non-linear Mapping which transforms
2-dimensional positions to correct for the radial distortion
introduced by some cameras and telescopes. This can take the form
either of pincushion or barrel distortion, and is characterized by a
single distortion coefficient.
A PcdMap is specified by giving this distortion coefficient and the
coordinates of the centre of the radial distortion. The forward
transformation of a PcdMap applies the distortion:
RD = R * ( 1 + C * R * R )
where R is the undistorted radial distance from the distortion centre
(specified by parameter PCDCEN), RD is the radial distance from the
same centre in the presence of distortion, and C is the distortion
coefficient (given by parameter DISCO).
The inverse transformation of a PcdMap removes the distortion produced
by the forward transformation. The expression used to derive R from RD
is an approximate inverse of the expression above.


Usage
~~~~~


::

    
       astpcdmap disco pcdcen options result
       



ADAM parameters
~~~~~~~~~~~~~~~



DISCO = _DOUBLE (Read)
``````````````````````
The distortion coefficient. Negative values give barrel distortion,
positive values give pincushion distortion, and zero gives no
distortion.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new PcdMap.



PCDCEN( 2 ) = _DOUBLE (Read)
````````````````````````````
An array containing the coordinates of the centre of the distortion.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new PcdMap.



Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils. All
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


