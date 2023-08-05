

ASTMATRIXMAP
============


Purpose
~~~~~~~
Create a MatrixMap


Description
~~~~~~~~~~~
This application creates a new MatrixMap and optionally initialises
its attributes. A MatrixMap is a form of Mapping which performs a
general linear transformation. Each set of input coordinates, regarded
as a column-vector, are pre-multiplied by a matrix (whose elements are
specified when the MatrixMap is created) to give a new column-vector
containing the output coordinates. If appropriate, the inverse
transformation may also be performed.


Usage
~~~~~


::

    
       astmatrixmap nin nout form matrix options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FORM = INTEGER (Read)
`````````````````````
An integer which indicates the form in which the matrix elements will
be supplied.
A value of zero indicates that a full NOUT x NIN matrix of values will
be supplied via the MATRIX parameter (below). In this case, the
elements should be given in row order (the elements of the first row,
followed by the elements of the second row, etc.).
A value of 1 indicates that only the diagonal elements of the matrix
will be supplied, and that all others should be zero. In this case,
the elements of MATRIX should contain only the diagonal elements,
stored consecutively.
A value of 2 indicates that a "unit" matrix is required, whose
diagonal elements are set to unity (with all other elements zero). In
this case, the MATRIX parameter is not used.



MATRIX() = _DOUBLE (Read)
`````````````````````````
The array of matrix elements to be used, stored according to the value
of FORM.



NIN = _INTEGER (Read)
`````````````````````
The number of input coordinates (i.e. the number of columns in the
matrix).



NOUT = INTEGER (Read)
`````````````````````
The number of output coordinates (i.e. the number of rows in the
matrix).



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new MatrixMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new MatrixMap.



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


