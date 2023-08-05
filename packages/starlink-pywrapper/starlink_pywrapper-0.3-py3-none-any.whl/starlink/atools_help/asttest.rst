

ASTTEST
=======


Purpose
~~~~~~~
Test if an Object attribute value is set


Description
~~~~~~~~~~~
This application displays a logical value indicating whether a value
has been explicitly set for one of an Object's attributes. This
logical value is also written to an output parameter.


Usage
~~~~~


::

    
       asttest this attrib
       



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



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Object. If an NDF is supplied, the WCS
FrameSet will be used.



VALUE = _LOGICAL (Write)
````````````````````````
On exit, this holds a boolean value indicating if the attribute was
set or not.



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


