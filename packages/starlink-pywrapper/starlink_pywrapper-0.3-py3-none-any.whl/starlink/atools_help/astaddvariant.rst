

ASTADDVARIANT
=============


Purpose
~~~~~~~
Store a new variant Mapping for the current Frame in a FrameSet


Description
~~~~~~~~~~~
This application allows a new variant Mapping to be stored with the
current Frame in a FrameSet. See the "Variant" attribute for more
details. It can also be used to rename the currently selected variant
Mapping.


Usage
~~~~~


::

    
       astaddvariant this map name result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



MAP = LITERAL (Read)
````````````````````
An NDF or text file holding the Mapping which describes how to convert
coordinates from the current Frame to the new variant of the current
Frame. If null (!) is supplied, then the name associated with the
currently selected variant of the current Frame is set to the value
supplied for NAME, but no new variant is added. If an NDF is supplied,
the Mapping from the Base Frame to the Current Frame of its WCS
FrameSet will be used.



NAME = LITERAL (Read)
`````````````````````
The name to associate with the new variant Mapping (or the currently
selected variant Mapping if a null value is supplied for MAP).



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified FrameSet. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
FrameSet, if possible.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original FrameSet to which a new
variant Mapping is to be added. If an NDF is supplied, the WCS
FrameSet will be used.



Notes
~~~~~


+ The newly added Variant becomes the current variant on exit (this is
equivalent to setting the Variant attribute to the value supplied for
NAME).
+ An error is reported if a variant with the supplied name already
  exists in the current Frame.




Copyright
~~~~~~~~~
Copyright (C) 2013 Central Laboratory of the Research Councils. All
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


