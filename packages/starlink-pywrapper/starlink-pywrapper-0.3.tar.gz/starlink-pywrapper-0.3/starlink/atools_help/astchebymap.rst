

ASTCHEBYMAP
===========


Purpose
~~~~~~~
Create a ChebyMap


Description
~~~~~~~~~~~
This application creates a new ChebyMap and optionally initialises its
attributes.
A ChebyMap is a form of Mapping which performs a Chebyshev polynomial
transformation. Each output coordinate is a linear combination of
Chebyshev polynomials of the first kind, of order zero up to a
specified maximum order, evaluated at the input coordinates. The
coefficients to be used in the linear combination are specified
separately for each output coordinate.
For a 1-dimensional ChebyMap, the forward transformation is defined as
follows:
f(x) = c0.T0(x') + c1.T1(x') + c2.T2(x') + ...
where:

+ Tn(x') is the nth Chebyshev polynomial of the first kind:
+ T0(x') = 1
+ T1(x') = x'
+ Tn+1(x') = 2.x'.Tn(x') + Tn-1(x')
+ x' is the inpux axis value, x, offset and scaled to the range [-1,
  1] as x ranges over a specified bounding box, given when the ChebyMap
  is created. The input positions, x, supplied to the forward
  transformation must fall within the bounding box - bad axis values
  (AST__BAD) are generated for points outside the bounding box.

For an N-dimensional ChebyMap, the forward transformation is a
generalisation of the above form. Each output axis value is the sum of
NCOEFF terms, where each term is the product of a single coefficient
value and N factors of the form Tn(x'_i), where "x'_i" is the
normalised value of the i'th input axis value.
The forward and inverse transformations are defined independantly by
separate sets of coefficients, supplied when the ChebyMap is created.
If no coefficients are supplied to define the inverse transformation,
the AST_POLYTRAN method of the parent PolyMap class can instead be
used to create an inverse transformation. The inverse transformation
so generated will be a Chebyshev polynomial with coefficients chosen
to minimise the residuals left by a round trip (forward transformation
followed by inverse transformation).


Usage
~~~~~


::

    
       astchebymap nin nout coeff_f coeff_i lbnd_f ubnd_f lbnd_i ubnd_i
                   options result
       



ADAM parameters
~~~~~~~~~~~~~~~



COEFF_F = LITERAL (Read)
````````````````````````
A group expression specifying the coefficients of the forward
transformation polynomials. Each sub-group of "2 + NIN" adjacent
elements describe a single coefficient of the forward transformation.
Within each such group, the first element is the coefficient value;
the next element is the integer index of the ChebyMap output which
uses the coefficient within its defining polynomial (the first output
has index 1); the remaining elements of the group give the integer
powers to use with each input coordinate value (powers must not be
negative, and floating point values are rounded to the nearest
integer).
For instance, if the ChebyMap has 3 inputs and 2 outputs, each group
consisting of 5 elements, A groups such as "(1.2, 2.0, 1.0, 3.0, 0.0)"
describes a coefficient with value 1.2 which is used within the
definition of output 2. The output value is incremented by the product
of the coefficient value, the value of the Chebyshev polynomial of
power 1 evaluated at input coordinate 1, and the value of the
Chebyshev polynomial of power 3 evaluated at input coordinate 2. Input
coordinate 3 is not used since its power is specified as zero. As
another example, the group "(-1.0, 1.0, 0.0, 0.0, 0.0 )" describes
adds a constant value -1.0 onto output 1 (it is a constant value since
the power for every input axis is given as zero).
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



LBND_F() = _DOUBLE (Read)
`````````````````````````
An array containing the lower bounds of the input bounding box within
which the ChebyMap is defined. The array should contain NIN elements.
Only accessed if a non-null value is supplied for COEFF_F.



UBND_F() = _DOUBLE (Read)
`````````````````````````
An array containing the upper bounds of the input bounding box within
which the ChebyMap is defined. The array should contain NIN elements.
Only accessed if a non-null value is supplied for COEFF_F.



LBND_I() = _DOUBLE (Read)
`````````````````````````
An array containing the lower bounds of the output bounding box within
which the inverse ChebyMap is defined. The array should contain NOUT
elements. Only accessed if a non-null value is supplied for COEFF_I.



UBND_I() = _DOUBLE (Read)
`````````````````````````
An array containing the upper bounds of the output bounding box within
which the inverse ChebyMap is defined. The array should contain NOUT
elements. Only accessed if a non-null value is supplied for COEFF_I.



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
assignments to be used for initialising the new ChebyMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new ChebyMap.



Copyright
~~~~~~~~~
Copyright (C) 2017 East Asian Observatory. Councils. All Rights
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


