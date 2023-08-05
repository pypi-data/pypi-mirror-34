

ASTPOLYMAP
==========


Purpose
~~~~~~~
Create a PolyMap


Description
~~~~~~~~~~~
This application creates a new PolyMap and optionally initialises its
attributes.
A PolyMap is a form of Mapping which performs a general polynomial
transformation. Each output coordinate is a polynomial function of all
the input coordinates. The coefficients are specified separately for
each output coordinate. The forward and inverse transformations are
defined independantly by separate sets of coefficients.


Usage
~~~~~


::

    
       astpolymap nin nout ncoeff_f coeff_f ncoeff_i coeff_i options result
       



ADAM parameters
~~~~~~~~~~~~~~~



COEFF_F = LITERAL (Read)
````````````````````````
A group expression specifying the coefficients of the forward
transformation polynomials. Each sub-group of "2 + NIN" adjacent
elements describe a single coefficient of the forward transformation.
Within each such group, the first element is the coefficient value;
the next element is the integer index of the PolyMap output which uses
the coefficient within its defining polynomial (the first output has
index 1); the remaining elements of the group give the integer powers
to use with each input coordinate value (powers must not be negative,
and floating point values are rounded to the nearest integer).
For instance, if the PolyMap has 3 inputs and 2 outputs, each group
consisting of 5 elements, A groups such as "(1.2, 2.0, 1.0, 3.0, 0.0)"
describes a coefficient with value 1.2 which is used within the
definition of output 2. The output value is incremented by the product
of the coefficient value, the value of input coordinate 1 raised to
the power 1, and the value of input coordinate 2 raised to the power
3. Input coordinate 3 is not used since its power is specified as
zero. As another example, the group "(-1.0, 1.0, 0.0, 0.0, 0.0 )"
describes adds a constant value -1.0 onto output 1 (it is a constant
value since the power for every input axis is given as zero).
Each final output coordinate value is the sum of all the terms
described by the sub-groups within the supplied group. Supplying a
null (!) value will result in the forward transformation being
undefined.



COEFF_I = LITERAL (Read)
````````````````````````
A group expression specifying the coefficients of the inverse
transformation polynomials. Each sub-group of "2 + NOUT" adjacent
elements describe a single coefficient of the inverse transformation
using the same scheme as "COEFF_F", except that inputs and outputs are
transposed. Supplying a null (!) value will result in the inverse
transformation being undefined.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



NIN = _INTEGER (Read)
`````````````````````
The number of input coordinates.



NOUT = INTEGER (Read)
`````````````````````
The number of output coordinates.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new PolyMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new PolyMap.



Copyright
~~~~~~~~~
Copyright (C) 2003-2004 Central Laboratory of the Research Councils.
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


