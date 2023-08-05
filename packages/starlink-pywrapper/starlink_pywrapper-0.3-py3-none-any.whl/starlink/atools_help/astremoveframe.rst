

ASTREMOVEFRAME
==============


Purpose
~~~~~~~
Remove a Frame from a FrameSet


Description
~~~~~~~~~~~
This application removes a Frame from a FrameSet. All other Frames in
the FrameSet have their indices re-numbered from one (if necessary),
but are otherwise unchanged.


Usage
~~~~~


::

    
       astremoveframe this iframe result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



IFRAME = LITERAL (Read)
```````````````````````
The integer index or Domain name of the Frame within the FrameSet
which is to be removed (the strings AST__BASE and AST__CURRENT may
also be supplied).



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified FrameSet. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
FrameSet, if possible.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original FrameSet from which a Frame
is to be removed. If an NDF is supplied, the WCS FrameSet will be
used.



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


