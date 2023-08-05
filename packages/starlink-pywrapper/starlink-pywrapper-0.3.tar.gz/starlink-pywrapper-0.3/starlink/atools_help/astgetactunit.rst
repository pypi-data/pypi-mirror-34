

ASTGETACTUNIT
=============


Purpose
~~~~~~~
Get the value of the ActiveUnit flag for a rame


Description
~~~~~~~~~~~
This application displays the current value of the ActiveUnit flag for
a Frame (see the description of the ASTSETACTUNIT command for a
description of the ActiveUnit flag). The value of the flag is also
written to an output parameter.


Usage
~~~~~


::

    
       astgetactunit this
       



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
An NDF or text file holding the Frame. If an NDF is supplied, the WCS
FrameSet will be used.



VALUE = _LOGICAL (Write)
````````````````````````
On exit, this holds a boolean value indicating if the ActiveUnit flag
was set or not.



Notes
~~~~~


+ This application corresponds to the AST routine AST_GETACTIVEUNIT.
  The name has been abbreviated due to a limitation on the length of
  ADAM command names.




Copyright
~~~~~~~~~
Copyright (C) 2003 Central Laboratory of the Research Councils. All
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


