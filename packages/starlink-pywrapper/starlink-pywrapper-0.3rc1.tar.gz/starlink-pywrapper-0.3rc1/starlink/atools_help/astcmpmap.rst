

ASTCMPMAP
=========


Purpose
~~~~~~~
Create a CmpMap


Description
~~~~~~~~~~~
This application creates a new CmpMap and optionally initialises its
attributes. A CmpMap is a compound Mapping which allows two component
Mappings (of any class) to be connected together to form a more
complex Mapping. This connection may either be "in series" (where the
first Mapping is used to transform the coordinates of each point and
the second mapping is then applied to the result), or "in parallel"
where one Mapping transforms the earlier coordinates for each point
and the second Mapping simultaneously transforms the later
coordinates).
Since a CmpMap is itself a Mapping, it can be used as a component in
forming further CmpMaps. Mappings of arbitrary complexity may be built
from simple individual Mappings in this way.


Usage
~~~~~


::

    
       astcmpmap map1 map2 series options result
       



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
An NDF or text file holding the first component Mapping If an NDF is
supplied, the Mapping from the Base Frame to the Current Frame of its
WCS FrameSet will be used.



MAP2 = LITERAL (Read)
`````````````````````
An NDF or text file holding the second component Mapping If an NDF is
supplied, the Mapping from the Base Frame to the Current Frame of its
WCS FrameSet will be used.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new CmpMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new CmpMap.



SERIES = _LOGICAL (Read)
````````````````````````
If a true value is given for this parameter, the two component
Mappings will be connected in series. A false value requests that they
are connected in parallel.



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


