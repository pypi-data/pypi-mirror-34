

ASTTRANN
========


Purpose
~~~~~~~
Transform N-dimensional coordinates


Description
~~~~~~~~~~~
This application uses a Mapping to transform the coordinates of a set
of points in an arbitrary number of dimensions. The input positions
may be supplied either as columns of pixel values in an NDF, or as a
group of formatted axis values (see parameter POSIN).


Usage
~~~~~


::

    
       asttrann this incols in forward outcols out
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FORWARD = _LOGICAL (Read)
`````````````````````````
A TRUE value indicates that the Mapping's forward coordinate
transformaton is to be used (in which case the number of values
supplied for the INCOLS parameter must be equal to the Nin attribute
of the Mapping, and the number of values supplied for the OUTCOLS
parameter must be equal to the Nout attribute). A FALSE value
indicates that the Mapping's inverse coordinate transformaton is to be
used (in which case the number of values supplied for the INCOLS
parameter must be equal to the Nout attribute of the Mapping, and the
number of values supplied for the OUTCOLS parameter must be equal to
the Nin attribute).



IN = LITERAL (Read)
```````````````````
Only used if a null(!) value is supplied for POSIN. A 2-dimensional
NDF holding the positions to be transformed. The DATA array of this
NDF is interpreted as a table in which each column of pixels holds
values for a specified quantity, some of which are the axis values at
the positions to be transformed. Each row of pixels corresponds to a
separate position. The columns holding the axis values are specified
using parameter INCOLS.



INCOLS() = INTEGER (Read)
`````````````````````````
Only used if a null(!) value is supplied for POSIN. A set of distinct
column indices within the NDF specified by parameter IN. These should
identify the columns holding the axis values to be transformed, in the
order required by the Mapping. If a null (!) value is supplied the
lowest N columns will be used, where N is the number of axes required
by the Mapping (see parameter FORWARD). [!]



OUT = LITERAL (Read)
````````````````````
Only used if a null(!) value is supplied for POSIN. A 2-dimensional
NDF to receive the transformed positions. The DATA array of this NDF
is interpreted as a table in which each column of pixels holds values
for a specified quantity, some of which are the axis values at the
transformed positions. Each row of pixels corresponds to a separate
position. The columns to receive the transformed axis values are
specified using parameter OUTCOLS. The output NDF is formed by taking
a copy of the input NDF, and then expanding its bounds to accomodate
any extra columns specified by parameter OUTCOLS (any such extra
columns are initialized to hold bad values). The initial values for
the columns specified by parameter OUTCOLS are then over-written with
the transformed axis values.



OUTCOLS() = INTEGER (Read)
``````````````````````````
Only used if a null(!) value is supplied for POSIN. A set of distinct
column indices within the NDF specified by parameter OUT. These should
identify the columns in which the transformed axis values should be
stored, in the order produced by the Mapping (see parameter FORWARD).
There is no restriction on the values which may be supplied (the
output NDF will be expanded to accomodate all supplied column
indices). If the number of input and output axes required by the
Mapping are equal, the run-time default is to use the same columns as
those used for parameter INCOLS. If the number of input and output
axes are different, there is no run-time default and the user is
prompted. []



POSIN = LITERAL (Read)
``````````````````````
A comma-separated list of floating point values to be used as the
input axis values. The list should start with all the values for input
axis 1, followed by all the values for input axis 2, etc. A text file
may be specified by preceeding the name of the file with an up arrow
character "^". If the supplied value ends with a minus sign, the user
is re-prompted for additional values. If a null (!) value is supplied,
the input positions are obtained using parameter IN. [!]



POSOUT = LITERAL (Read)
```````````````````````
Only accessed if a value is supplied for parameter POSIN. The name of
a text file in which to put the transformed axis values. No file is
produced if a null (!) value is supplied. One axis value is stored on
each line of the file. All the values for axis 1 comes first, followed
by all the values for aixs 2, etc. [!]



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping to use. If an NDF is supplied,
the Mapping from the Base Frame to the Current Frame of its WCS
FrameSet will be used.



Copyright
~~~~~~~~~
Copyright (C) 2001-2006 Particle Physics and Astronomy Research
Council. All Rights Reserved.


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


