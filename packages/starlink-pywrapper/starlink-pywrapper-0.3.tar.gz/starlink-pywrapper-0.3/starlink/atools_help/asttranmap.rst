

ASTTRANMAP
==========


Purpose
~~~~~~~
Create a TranMap


Description
~~~~~~~~~~~
This application creates a new TranMap and optionally initialises its
attributes.
A TranMap is a Mapping which combines the forward transformation of a
supplied Mapping with the inverse transformation of another supplied
Mapping, ignoring the un-used transformation in each Mapping (indeed
the un-used transformation need not exist).
When the forward transformation of the TranMap is referred to, the
transformation actually used is the forward transformation of the
first Mapping supplied when the TranMap was constructed. Likewise,
when the inverse transformation of the TranMap is referred to, the
transformation actually used is the inverse transformation of the
second Mapping supplied when the TranMap was constructed.


Usage
~~~~~


::

    
       asttranmap map1 map2 options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



MAP1 = LITERAL (Read)
`````````````````````
An NDF or text file holding the first component Mapping, which defines
the forward transformation. If an NDF is supplied, the Mapping from
the Base Frame to the Current Frame of its WCS FrameSet will be used.



MAP2 = LITERAL (Read)
`````````````````````
An NDF or text file holding the second component Mapping, which
defines the inverse transformation. If an NDF is supplied, the Mapping
from the Base Frame to the Current Frame of its WCS FrameSet will be
used.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new TranMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new TranMap.



Copyright
~~~~~~~~~
Copyright (C) 2004 Central Laboratory of the Research Councils. All
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


