

ASTREMOVEREGION
===============


Purpose
~~~~~~~
Remove any Regions from a Mapping


Description
~~~~~~~~~~~
This application searches the supplied Mapping (which may be a
compound Mapping such as a CmpMap) for any component Mappings that are
instances of the AST Region class. It then creates a new Mapping from
which all Regions have been removed. If a Region cannot simply be
removed (for instance, if it is a component of a parallel CmpMap),
then it is replaced with an equivalent UnitMap in the returned
Mapping.


Usage
~~~~~


::

    
       astremoveregion this result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the modified Mapping.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping. If an NDF is supplied, the
Mapping from the base Frame of the WCS FrameSet to the current Frame
will be used.



Copyright
~~~~~~~~~
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
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


