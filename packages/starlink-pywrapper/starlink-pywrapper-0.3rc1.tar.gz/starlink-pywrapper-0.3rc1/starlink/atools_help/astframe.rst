

ASTFRAME
========


Purpose
~~~~~~~
Create a Frame


Description
~~~~~~~~~~~
This application creates a new Frame and optionally initialises its
attributes. A Frame is used to represent a coordinate system. It does
this in rather the same way that a frame around a graph describes the
coordinate space in which data are plotted. Consequently, a Frame has
a Title (string) attribute, which describes the coordinate space, and
contains axes which in turn hold information such as Label and Units
strings which are used for labelling (e.g.) graphical output. In
general, however, the number of axes is not restricted to two.


Usage
~~~~~


::

    
       astframe naxes options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



NAXES = _INTEGER (Read)
```````````````````````
The number of Frame axes (i.e. the number of dimensions of the
coordinate space which the Frame describes).



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new Frame.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new Frame.



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


