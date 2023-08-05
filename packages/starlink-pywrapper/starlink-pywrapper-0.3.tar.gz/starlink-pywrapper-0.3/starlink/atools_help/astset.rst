

ASTSET
======


Purpose
~~~~~~~
Set an attribute value for an Object


Description
~~~~~~~~~~~
This application sets a specified attribute value for an Object.


Usage
~~~~~


::

    
       astset this attrib value result
       



ADAM parameters
~~~~~~~~~~~~~~~



ATTRIB = LITERAL (Read)
```````````````````````
A string containing the name of the attribute.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified Object. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
Object if possible (if it is a FrameSet in which the base Frame has
Domain GRID and has 1 axis for each NDF dimension).



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original Object. If an NDF is
supplied, the WCS FrameSet will be used.



VALUE = LITERAL (Read)
``````````````````````
The formatted value to assign to the attribute.



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


