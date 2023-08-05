

POLIMAGE
========


Purpose
~~~~~~~
Converts a catalogue into an NDF


Description
~~~~~~~~~~~
This application creates an NDF from a supplied catalogue. The output
NDF can be either a simple 1-dimensional list of column values without
any spatial information, or it can be a 2 or 3 dimensional array in
which column values retain their spatial positions (see parameter
SHAPE). The columns containing data value and (optionally) variance
are specified using parameters COLDAT and COLVAR.
If parameter SHAPE is set TRUE, a 2 or 3 dimensional NDF is created in
which the spatial position of each data value is read from the
catalogue columns specified using parameters COLX, COLY and COLZ. The
NDF is formed by binning the catalogue values into a grid of equally
sized rectangular cells, the dimensions of each cell being given by
parameter BOX. Each pixel in the output NDF corresponds to one of
these cells. The data values for the cell are formed by combining
together the COLDAT values of all input positions which fall within
the cell, using the method specified by the parameter METHOD.
If parameter SHAPE is set FALSE, a 1D NDF is created in which the
spatial position of each data value is ignored. The data values are
just copied into the 1D NDF in the same order that they appear in the
input catalogue. That is, the first value in the catalogue becomes
pixel 1, the seconds catalogue value becomes pixel 2, etc. This avoids
any binning of the data values, and is useful if applications which do
not use spatial information (such as the KAPPA applications STATS,
HISTOGRAM, etc) are to be used.


Usage
~~~~~


::

    
       polimage in out coldat [colvar] [colx] [coly] [method] [colz]
       



ADAM parameters
~~~~~~~~~~~~~~~



BOX( 3 ) = _REAL (Read)
```````````````````````
The x, y and z bin sizes. These values refer to the co-ordinate Frame
given by parameters COLX and COLY. Only accessed if parameter SHAPE is
TRUE. If not supplied, the third value defaults to 1.0 and the second
value defaults to the first value.



COLDAT = LITERAL (Read)
```````````````````````
The name of the catalogue column holding the values to be stored in
the DATA component of the output NDF. A list of available column names
is displayed if a non-existent column name is given. An arbitrary
algebraic combination of columns may be used by supplying a CURSA
expression instead of a single column name. See SUN/190 for details of
the syntax of these expressions.



COLVAR = LITERAL (Read)
```````````````````````
The name of the catalogue column holding the values to be stored in
the VARIANCE component of the output NDF. A list of available column
names is displayed if a non-existent column name is given. If a null
(!) value is supplied, no VARIANCE component is created. An arbitrary
algebraic combination of columns may be used by supplying a CURSA
expression instead of a single column name. For instance, supplying
the string "DP**2" causes the square of the values in column DP to be
used. See SUN/190 for details of the syntax of these expressions. [!]



COLX = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the coordinate of each
data value along the first axis. A list of available column names is
displayed if a non-existent column name is given. An arbitrary
algebraic combination of columns may be used by supplying a CURSA
expression instead of a single column name. See SUN/190 for details of
the syntax of these expressions. Only accessed if parameter SHAPE is
TRUE. [X]



COLY = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the coordinate of each
data value along the second axis. See COLX for further details. [Y]



COLZ = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the coordinate of each
data value along a third axis. If a null (!) value is supplied the
output NDF will be 2-dimensional. The dynamic default is "Z" if the
catalogue contains a column named "Z", and is null (!) otherwise. See
COLX for further details. []



IN = LITERAL (Read)
```````````````````
The name of the input catalogue. This may be in any format supported
by the CAT library (see SUN/181). A file type of .FIT is assumed if no
file type is supplied.



METHOD = LITERAL (Read)
```````````````````````
The method to be used when binning data values. This may be set to any
unique abbreviation of the following:


+ MEAN -- Mean of the input data values
+ MEDIAN -- Median of the input data values
+ SIGMA -- A sigma clipped mean

Only accessed if parameter SHAPE is TRUE. [MEAN]



MINVAL = _INTEGER (Read)
````````````````````````
The minimum number of good input values which must be present in a
cell to create a good output value. Only accessed if parameter SHAPE
is TRUE. [1]



OUT = NDF (Read)
````````````````
The name of the output NDF.



SHAPE = _LOGICAL (Read)
```````````````````````
If a TRUE value is supplied for parameter SHAPE, then the output NDF
is 2 or 3-dimensional and inherits the spatial positions given in the
columns specified by COLX, COLY and COLZ. If a FALSE value is
supplied, the output NDF is 1-dimensional and the spatial position of
each data value is ignored. In this case, the number of pixels in the
output NDF will equal the number of rows in the input catalogue. The
data values are stored in the NDF in the same order as in the input
catalogue. [TRUE]



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations to reject data at. Only used if METHOD
is set to "SIGMA". Only accessed if parameter SHAPE is TRUE. [4.0]



Examples
~~~~~~~~
polimage incat outimg p
Creates a 2-D NDF called "outimg" containing the values of column P in
the catalogue "incat.FIT". The catalogue values are binned into a 2-D
grid of pixels using the spatial positions given in the columns "X"
and "Y".
polimage incat outimg p noshape
Creates a 1-D NDF called "outimg" containing the values of column P in
the catalogue "incat.FIT". The number of pixels in the output is equal
to the number of rows in the catalogue, and the catalogue values are
copied into the output in the order in which they occur in the
catalogue.



Notes
~~~~~


+ If parameter SHAPE is set TRUE, the output NDF will have an AXIS
component representing the COLX, COLY and COLZ values. It will also
inherit any WCS information from the catalogue so long as the Base
Frame of the WCS information is spanned by axes with symbols equal to
the names of the columns given by COLX, COLY and COLZ.
+ If parameter SHAPE is set FALSE, the output NDF will contain no AXIS
  or WCS components.




Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
Reserved.


