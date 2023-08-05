

ASTPOLYTRAN
===========


Purpose
~~~~~~~
Fit a PolyMap inverse or forward transformation


Description
~~~~~~~~~~~
This application creates a new PolyMap which is a copy of the supplied
PolyMap, in which a specified transformation (forward or inverse) has
been replaced by a new polynomial function. The coefficients of the
new transformation are estimated by sampling the other transformation
and performing a least squares polynomial fit in the opposite
direction to the sampled positions and values.
The transformation to create is specified by the FORWARD parameter. In
what follows "X" refers to the inputs of the PolyMap, and "Y" to the
outputs of the PolyMap. The forward transformation transforms input
values (X) into output values (Y), and the inverse transformation
transforms output values (Y) into input values (X). Within a PolyMap,
each transformation is represented by an independent set of
polynomials: Y=P_f(X) for the forward transformation and X=P_i(Y) for
the inverse transformation.
If FORWARD is FALSE, a new inverse transformation is created by first
finding the output values (Y) using the forward transformation (which
must be available) at a regular grid of points (X) covering a
rectangular region of the PolyMap's input space. The coefficients of
the required inverse polynomial, X=P_i(Y), are chosen in order to
minimise the sum of the squared residuals between the sampled values
of X and P_i(Y).
If FORWARD is TRUE, a new forward transformation is created by first
finding the input values (X) using the inverse transformation (which
must be available) at a regular grid of points (Y) covering a
rectangular region of the PolyMap's output space. The coefficients of
the required forward polynomial, Y=P_f(X), are chosen in order to
minimise the sum of the squared residuals between the sampled values
of Y and P_f(X).
This fitting process is performed repeatedly with increasing
polynomial orders (starting with quadratic) until the target accuracy
is achieved, or a specified maximum order (MAXORDER) is reached. If
the target accuracy cannot be achieved even with this maximum-order
polynomial, the best fitting maximum-order polynomial is returned so
long as its accuracy is better than MAXACC. If it is not, an error is
reported.


Usage
~~~~~


::

    
       astpolytran this forward acc maxacc maxorder lbnd ubnd result
       



ADAM parameters
~~~~~~~~~~~~~~~



ACC = DOUBLE (Given)
````````````````````
The required accuracy, expressed as a geodesic distance within the
PolyMap's input space (if FORWARD is FALSE) or output space (if
FORWARD is TRUE).



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FORWARD = _LOGICAL (Read)
`````````````````````````
If TRUE, the forward PolyMap transformation is replaced. Otherwise the
inverse transformation is replaced.



LBND() = _DOUBLE (Read)
```````````````````````
An array holding the lower bounds of a rectangular region within the
PolyMap's input space (if FORWARD is FALSE) or output space (if
FORWARD is TRUE). The new polynomial will be evaluated over this
rectangle. The length of this array should equal the value of the
PolyMap's Nin or Nout attribute, depending on FORWARD.



MAXACC = DOUBLE (Read)
``````````````````````
The maximum allowed accuracy for an acceptable polynomial, expressed
as a geodesic distance within the PolyMap's input space (if FORWARD is
FALSE) or output space (if FORWARD is TRUE).



MAXORDER = INTEGER (Read)
`````````````````````````
The maximum allowed polynomial order. This is one more than the
maximum power of either input axis. So for instance, a value of 3
refers to a quadratic polynomial.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new PolyMap.



THIS = LITERAL (Read)
`````````````````````
A text file holding the PolyMap.



UBND() = _DOUBLE (Read)
```````````````````````
An array holding the upper bounds of a rectangular region within the
PolyMap's input space (if FORWARD is FALSE) or output space (if
FORWARD is TRUE). The new polynomial will be evaluated over this
rectangle. The length of this array should equal the value of the
PolyMap's Nin or Nout attribute, depending on FORWARD.



Copyright
~~~~~~~~~
Copyright (C) 2011 Science & Technology Facilities Council. All Rights
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


