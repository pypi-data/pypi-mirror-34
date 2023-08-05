

ASTMATHMAP
==========


Purpose
~~~~~~~
Create a MathMap


Description
~~~~~~~~~~~
This application creates a new MathMap and optionally initialises its
attributes.
A MathMap is a Mapping which allows you to specify a set of forward
and/or inverse transformation functions using arithmetic operations
and mathematical functions similar to those available in Fortran. The
MathMap interprets these functions at run-time, whenever its forward
or inverse transformation is required. Because the functions are not
compiled in the normal sense (unlike an IntraMap), they may be used to
describe coordinate transformations in a transportable manner. A
MathMap therefore provides a flexible way of defining new types of
Mapping whose descriptions may be stored as part of a dataset and
interpreted by other programs.
See the reference documentation for the AstMathMap constructor in
SUN/210 for a complete description of the syntax of the transformation
functions.


Usage
~~~~~


::

    
       astmathmap nin nout fwd inv options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FWD = (Read)
````````````
A group expression specifying the expressions defining the forward
transformation. The number of forward transformation functions
supplied must be at least equal to NOUT, but may be increased to
accommodate any additional expressions which define intermediate
variables for the forward transformation. The syntax of these
expressions is described in SUN/210



INV = (Read)
````````````
A group expression specifying the expressions defining the inverse
transformation. The number of inverse transformation functions
supplied must be at least equal to NIN, but may be increased to
accommodate any additional expressions which define intermediate
variables for the inverse transformation. The syntax of these
expressions is described in SUN/210



NIN = _INTEGER (Read)
`````````````````````
Number of input variables for the MathMap. This determines the value
of its Nin attribute.



NOUT = _INTEGER (Read)
``````````````````````
Number of output variables for the MathMap. This determines the value
of its Nout attribute.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new MathMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new MathMap.



Copyright
~~~~~~~~~
Copyright (C) 2003 Central Laboratory of the Research Councils. All
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


