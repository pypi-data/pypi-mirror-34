

TRANDAT
=======


Purpose
~~~~~~~
Converts free-format text data into an NDF


Description
~~~~~~~~~~~
This application takes grid data contained in a free-format text file
and stores them in the data array of an NDF. The data file could
contain, for example, mapping data or results from simulations which
are to be converted into an image for analysis.
There are two modes of operation which depend on whether the text file
contains co-ordinate information, or solely data values (determined by
parameter AUTO).
a) AUTO=FALSE If the file contains co-ordinate information the format
of the data is tabular; the positions and values are arranged in
columns and a record may contain information for only a single point.
Where data points are duplicated only the last value appears in the
NDF. Comment lines can be given, and are indicated by a hash or
exclamation mark in the first column. Here is an example file (the
vertical ellipses indicate missing lines in the file):
# Model 5, phi = 0.25, eta = 1.7 1 -40.0 40.0 1121.9 2 0.0 30.0 56.3 3
100.0 20.0 2983.2 4 120.0 85.0 339.3 . . . . . . . . . . . . <EOF>
The records do not need to be ordered (but see the warning in the
Notes), as the application searches for the maximum and minimum co-
ordinates in each dimension so that it can define the size of the
output image. Also, each record may contain other data fields
(separated by one or more spaces), which need not be all the same data
type. In the example above only columns 2, 3 and 4 are required. There
are parameters (POSCOLS, VALCOL) which select the co-ordinate and
value columns.
The distance between adjacent pixels (given by parameter PSCALE)
defaults to 1, and is in the same units as the read-in co-ordinates.
The pixel index of a data value is calculated using the expression
index = FLOOR( ( x - xoff ) / scale ) + 1
where x is the supplied co-ordinate and xoff is the value of the
POFFSET parameter (which defaults to the minimum supplied co-ordinate
along an axis), scale is the value of parameter PSCALE, and FLOOR is a
function that returns the largest integer that is smaller (i.e. more
negative) than its argument.
You are informed of the number of points found and the maximum and
minimum co-ordinate values for each dimension. There is no limit
imposed by the application on the number of points or the maximum
output array size, though there may be external constraints. The
derived array size is reported in case you have made a typing error in
the text file. If you realise that this has indeed occurred just abort
(!!) when prompted for the output NDF.
b) AUTO=TRUE If the text file contains no co-ordinates, the format is
quite flexible, however, the data are read into the data array in
Fortran order, i.e. the first dimension is the most rapidly varying,
followed by the second dimension and so on. The number of data values
that may appear on a line is variable; data values are separated by at
least a space, comma, tab or carriage return. A line can have up to
255 characters. In addition a record may have trailing comments
designated by a hash or exclamation mark. Here is an example file,
though a more regular format would be clearer for the human reader.
# test for the new TRANDAT 23 45.3 ! a comment 50.7,47.5 120. 46.67
47.89 42.4567 .1 23.3 45.2 43.2 56.0 30.9 29. 27. 26. 22.4 20. 18.
-12. 8. 9.2 11. <EOF>
Notice that the shape of the NDF is defined by a parameter rather than
explicitly in the file.


Usage
~~~~~


::

    
       trandat freename out [poscols] [valcol] [pscale] [dtype] [title]
       



ADAM parameters
~~~~~~~~~~~~~~~



AUTO = _LOGICAL (Read)
``````````````````````
If TRUE the text file does not contain co-ordinate information.
[FALSE]



BAD = _LOGICAL (Read)
`````````````````````
If TRUE the output NDF data array is initialised with the bad value,
otherwise it is filled with zeroes. [TRUE]



DTYPE = LITERAL (Read)
``````````````````````
The HDS type of the data values within the text file, and the type of
the data array in the output NDF. The options are: '_REAL', '_DOUBLE',
'_INTEGER', '_BYTE', '_UBYTE', '_WORD', '_UWORD'. (Note the leading
underscore.) ['_REAL']



FREENAME = FILENAME (Read)
``````````````````````````
Name of the text file containing the free-format data.



LBOUND( ) = _INTEGER (Read)
```````````````````````````
The lower bounds of the NDF to be created. The number of values must
match the number supplied to parameter SHAPE. It is only accessed in
automatic mode. If a null (!) value is supplied, the value used is 1
along each axis. [!]



POFFSET() = _REAL (Read)
````````````````````````
The supplied co-ordinates that correspond to the origin of floating
point pixel co-ordinates. It is only used in co-ordinate mode. Its
purpose is to permit an offset from some arbitrary units to pixels. If
a null (!) value is supplied, the value used is the minimum supplied
co-ordinate value for each dimension. [!]



POSCOLS() = _INTEGER (Read)
```````````````````````````
Column positions of the co-ordinates in an input record of the text
file, starting from x to higher dimensions. It is only used in co-
ordinate mode. The columns must be different amongst themselves and
also different from the column containing the values. If there is
duplication, new values for both POSCOLS and VALCOL will be requested.
[1,2]



PSCALE() = _REAL (Read)
```````````````````````
Pixel-to-pixel distance in co-ordinate units for each dimension. It is
only used in co-ordinate mode. Its purpose is to permit linear scaling
from some arbitrary units to pixels. If a null (!) value is supplied,
the value used is 1.0 for each co-ordinate dimension. [!]



QUANTUM = _INTEGER (Read)
`````````````````````````
You can safely ignore this parameter. It is used for fine- tuning
performance in the co-ordinate mode.
The application obtains work space to store the position-value data
before they can be copied into the output NDF so that the array bounds
can be computed. Since the number of lines in the text file is
unknown, the application obtains chunks of work space whose size is
three times this parameter whenever it runs out of storage. (Three
because the parameter specifies the number of lines in the file rather
than the number of data items.) If you have a large number of points
there are efficiency gains if you make this parameter either about 20
--30 per cent or slightly greater than or equal to the number of lines
your text file. A value slightly less than the number of lines is
inefficient as it creates nearly 50 per cent unused space. A value
that is too small can cause unnecessary unmapping, expansion and re-
mapping of the work space. For most purposes the default should give
acceptable performance. It must lie between 32 and 2097152. [2048]



SHAPE( ) = _INTEGER (Read)
``````````````````````````
The shape of the NDF to be created. For example, [50,30,20] would
create 50 columns by 30 lines by 10 bands. It is only accessed in
automatic mode.



NDF = NDF (Write)
`````````````````
Output NDF for the generated data array.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. ["KAPPA - Trandat"]



VALCOL = _INTEGER (Read)
````````````````````````
Column position of the array values in an input record of the text
file. It is only used in co-ordinate mode. The column position must be
different from those specified for the co-ordinate columns. If there
is duplication, new values for both POSCOLS and VALCOL will be
requested. [3]



Examples
~~~~~~~~
trandat simdata.dat model
Reads the text file simdata.dat and stores the data into the data
array of a two-dimensional, _REAL NDF called model. The input file
should have the co-ordinates and real values arranged in columns, with
the x-y positions in columns 1 and 2 respectively, and the real data
in column 3.
trandat freename=simdata out=model auto shape=[50,40,9]
Reads the text file simdata and stores the data into the data array of
a three-dimensional, _REAL NDF called model. Its x dimension is 50, y
is 40 and z is 9. The input file only contains real values and
comments.
trandat freename=simdata out=model auto shape=[50,40,9] dtype=_i
As the previous example except an _INTEGER NDF is created, and the
text file must contain integer data.
trandat simdata.dat model [6,3,4] 2
Reads the text file simdata.dat and stores the data into the data
array of a three-dimensional, _REAL NDF called model. The input file
should have the co-ordinates and real values arranged in columns, with
the x-y-z positions in columns 6, 3 and 4 respectively, and the real
data in column 2.
trandat spectrum.dat lacertid noauto poscols=2 valcol=4 pscale=2.3
Reads the text file spectrum.dat and stores the data into the data
array of a one-dimensional, _REAL NDF called lacertid. The input file
should have the co-ordinate and real values arranged in columns, with
its co-ordinates in columns 2, and the real data in column 4. A one-
pixel step in the NDF corresponds to 2.3 in units of the supplied co-
ordinates.



Notes
~~~~~


+ Bad data values may be represented by the string "BAD" (case
insensitive) within the input text file.
+ All non-complex numeric data types can be handled. However, byte,
unsigned byte, word and unsigned word require data conversion, and
therefore involve additional processing. to a vector element (for n-d
generality).
+ WARNING: In non-automatic mode it is strongly advisable for large
output NDFs to place the data in Fortran order, i.e. the first
dimension is the most rapidly varying, followed by the second
dimension and so on. This gives optimum performance. The meaning of
"large" will depend on working-set quotas on your system, but a few
megabytes gives an idea. If you jump randomly backwards and forwards,
or worse, have a text file in reverse- Fortran order, this can have
disastrous performance consequences for you and other users.
+ In non-automatic mode, the co-ordinates for each dimension are
stored in the NDF axis structure. The first centre is at the minimum
value found in the list of positions for the dimension plus half of
the scale factor. Subsequent centres are incremented by the scale
factor.
+ The output NDF may have between one and seven dimensions.
+ In automatic mode, an error is reported if the shape does not use
  all the data points in the file.




Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: ASCII2NDF, NDF2ASCII; SPECDRE: ASCIN, ASCOUT.


Copyright
~~~~~~~~~
Copyright (C) 1990-1992 Science & Engineering Research Council.
Copyright (C) 1995-1996, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2010 Science & Technology Facilities Council.
All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


