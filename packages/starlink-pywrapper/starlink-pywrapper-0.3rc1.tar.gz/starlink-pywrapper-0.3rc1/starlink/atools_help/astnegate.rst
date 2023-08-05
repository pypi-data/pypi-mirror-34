

ASTNEGATE
=========


Purpose
~~~~~~~
Negate the area represented by a Region


Description
~~~~~~~~~~~
This application negates the area represented by a Region. That is,
points which were previously inside the region will then be outside,
and points which were outside will be inside. This is acomplished by
toggling the state of the Negated attribute for the supplied region.


Usage
~~~~~


::

    
       astnegate this result
       



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
A text file to receive the negated Region.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Region. If an NDF is supplied, the
current Frame of the WCS FrameSet will be used (if it is a Region).



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


