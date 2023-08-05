

ASCIN
=====


Purpose
~~~~~~~
Read a 1-D or N-D data set from an ASCII table


Description
~~~~~~~~~~~
This routine reads axis values, pixel widths, data values, and data
errors from an ASCII table into an NDF data structure. Most of these
items are optional, mandatory are only axis values for each axis and
data values. Pixel widths can be read only in the one-dimensional
case.
The user specifies in which columns the different items are to be
found. A range of line numbers to be used can be specified. Comment
lines may be interspersed in this line range, if they are marked by an
exclamation mark in the first or second character. All columns
leftward of the rightmost used column must be numeric, non-numeric
data may follow in further columns. Up to 132 characters are read from
table lines. Numbers are read as _REAL.
If the result is one-dimensional, the axis values will be taken
literally to define a grid, which in general may be non-linear and
non-monotonic. If the result is multi-dimensional, the routine will
guess from the table a grid that is linear in all directions. The
parameter system is consulted to confirm or modify the suggested grid.
The data value read from a line will be stored into exactly one output
pixel, if and only if the table coordinates match that pixel's
coordinate to within a specified fraction of the pixel step. Pixels
for which no data are in the table are assigned the bad value. Table
data equal to a specified "alternative bad value" are replaced by the
bad value before insertion into the data set. Where more than one
table line corresponds to the same pixel, the pixel is assigned the
last value from the table. That is, later specifications of the same
pixel override previous ones.


Usage
~~~~~


::

    
       ascin in lines colaxes=? coldata=? [start=? step=? end=?] out=?
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, the routine will issue only error messages and no
informational messages. This parameter is of significance only if the
output is multi-dimensional. [YES]



TOL = _REAL (Read)
``````````````````
The tolerated fraction of the pixel size by which the table
coordinates may deviate from the pixel coordinates. For a line read
from the ASCII table, if any one of the axis values deviates by more
than TOL times the pixel step, then the information from the table is
disregarded. This parameter is of no significance, if the output is
one-dimensional, since in that case the axis values found will define
the exact (non-linear) grid. [0.2]



BAD = _REAL (Read)
``````````````````
The alternative bad value, i.e. the bad value used in the table. Any
data or error value found in the table that is equal to BAD, is
replaced by the bad value before insertion into the output. [-999999.]



IN = FILENAME (Read)
````````````````````
The file containing the ASCII table.



LINES( 2 ) = _INTEGER (Read)
````````````````````````````
The line numbers of the first and last lines to be used from the table
file. [1,9999]



COLAXES( 7 ) = _INTEGER (Read)
``````````````````````````````
The column numbers where the axis values are to be found. All axes
must be specified, i.e. at least one. The number of leading non-zero
elements defines the number of axes in the output. [1,2]



COLWIDTH = _INTEGER (Read)
``````````````````````````
The column numbers where the pixel width values are to be found. This
parameter is of significance only if the output is one-dimensional.
Enter a 0 if no width information is available. [0]



COLDATA( 2 ) = _INTEGER (Read)
``````````````````````````````
The column numbers where the data values (first element) and their
associated error values (second element) are to be found. If no error
information is available, enter 0 as second element. [3,0]



START( 7 ) = _REAL (Read)
`````````````````````````
The coordinates of the first pixel. This parameter is of no
significance, if the output is one-dimensional, since in that case the
axis values found will define the exact (non-linear) grid.



STEP( 7 ) = _REAL (Read)
````````````````````````
The coordinate increments per pixel. This parameter is of no
significance, if the output is one-dimensional, since in that case the
axis values found will define the exact (non-linear) grid.



END( 7 ) = _REAL (Read)
```````````````````````
The coordinates of the last pixel. This parameter is of no
significance, if the output is one-dimensional, since in that case the
axis values found will define the exact (non-linear) grid.



OUT = NDF (Read)
````````````````
The NDF where to store the data.



Examples
~~~~~~~~
ascin in [1,9999] colaxes=[1,2] coldata=[3,4]

start=[0,0] end=[2.5,5] step=[0.1,1] out=out
This will read the data from the ASCII file IN, using line numbers 1
to 9999 (or till end of file if there are less lines in IN). The 1st
axis data are taken from the first column, the 2nd axis data from the
second column. The image data are taken from the 3rd column and their
errors from the 4th column. The routine tries to store the table data
into a grid with the 1st axis running from 0 to 2.5 in steps of 0.1
(26 pixels) and the 2nd axis running from 0 to 5 in steps of 1 (6
pixels). If a coordinate pair from columns 1&2 matches any pixel
centre well enough, the data from columns 4&5 are entered into the
corresponding element of the data and errors array. The data file is
OUT.
ascin in out [25,39] colaxes=5 coldata=[3,0]
Here the output is one-dimensional and without errors array (thus the
zero in COLDATA). Only lines 25 to 39 from IN are used. The axis data
are from the 5th column and the spectrum data from the 3rd column.
(Note that columns 1, 2 and 4 must contain numeric data.) The axis
grid need not be specified. The axis values from the table will be
taken literally to form a grid that is in general non-linear and non-
monotonic.



Implementation Status
~~~~~~~~~~~~~~~~~~~~~
It is not possible to read axis values from the table in double
precision or create a double precision axis array.


