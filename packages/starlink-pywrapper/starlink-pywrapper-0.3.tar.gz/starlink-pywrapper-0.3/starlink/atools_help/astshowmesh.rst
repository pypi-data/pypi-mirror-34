

ASTSHOWMESH
===========


Purpose
~~~~~~~
Display a mesh of points covering the surface of a Region


Description
~~~~~~~~~~~
This application writes a table to standard output containing the axis
values at a mesh of points covering the surface of the supplied
Region. Each row of output contains a tab-separated list of axis
values, one for each axis in the Frame encapsulated by the Region. The
number of points in the mesh is determined by the MeshSize attribute.
The table is preceeded by a given title string, and followed by a
single line containing the word "ENDMESH".


Usage
~~~~~


::

    
       astshowmesh this format ttl
       



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
An NDF, FITS file or text file holding the Frame. If an NDF is
supplied, the current Frame of the WCS FrameSet will be used. If a
FITS file is supplied, the Frame corresponding to the primary axis
descriptions will be used.



FORMAT = _LOGICAL (Read)
````````````````````````
If TRUE, then the output table contains axis values that have been
formatted using thew AST_FORMAT method. Otherwise, the table contains
floating point values displayed with a default format.



TITLE = LITERAL (Read)
``````````````````````
A text string to display before the table.



Copyright
~~~~~~~~~
Copyright (C) 2007 Science & Technology Facilities Council. All Rights
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


