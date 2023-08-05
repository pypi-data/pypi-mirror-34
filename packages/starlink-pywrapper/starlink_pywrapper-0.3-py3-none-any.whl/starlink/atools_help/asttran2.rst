

ASTTRAN2
========


Purpose
~~~~~~~
Use a Mapping to transform a set of position in two dimensions


Description
~~~~~~~~~~~
This application applies a Mapping to transform the coordinates of a
set of points in two dimensions. The input positions may be supplied
either directly or in a text file. The output positions are listed on
the screen ( an X value and a Y value on each line, separated by a
space) and may optionally be stored in output text files.


Usage
~~~~~


::

    
       asttran2 this xin yin forward xout yout
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



THIS = LITERAL (Read)
`````````````````````
An NDF, FITS file or text file holding the Mapping. If an NDF is
supplied, the Mapping from the base Frame of the WCS FrameSet to the
current Frame will be used. If a FITS file is supplied, the Mapping
from the pixel grid coordinates to the primary axis descriptions will
be used.



XIN = GROUP (Read)
``````````````````
A comma-separated list of floating point values to be used as the
input X axis value. A text file may be specified by preceeding the
name of the file with an up arrow character "^". If the supplied value
ends with a minus sign, the user is re-prompted for additional values.



YIN = GROUP (Read)
``````````````````
A comma-separated list of floating point values to be used as the
input Y axis value. A text file may be specified by preceeding the
name of the file with an up arrow character "^". If the supplied value
ends with a minus sign, the user is re-prompted for additional values.



FORWARD = _LOGICAL (Read)
`````````````````````````
If this value is TRUE, then the Mapping's forward transformation will
be used to transform the input positions. Otherwise, its inverse
transformation will be used.



XOUT = LITERAL (Read)
`````````````````````
The name of a text file in which to put the transformed X axis values.
No file is produced if a null (!) value is supplied. One axis value is
stored on each line of the file. [!]



XVAL = _DOUBLE (Write)
``````````````````````
An output parameter that is left holding the final transformed output
X value.



YOUT = LITERAL (Read)
`````````````````````
The name of a text file in which to put the transformed Y axis values.
No file is produced if a null (!) value is supplied. One axis value is
stored on each line of the file. [!]



YVAL = _DOUBLE (Write)
``````````````````````
An output parameter that is left holding the final transformed output
Y value.



Copyright
~~~~~~~~~
Copyright (C) 2003-2004 Central Laboratory of the Research Councils.
Copyright (C) 2013 Science & Technology Facilities Council. All Rights
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


