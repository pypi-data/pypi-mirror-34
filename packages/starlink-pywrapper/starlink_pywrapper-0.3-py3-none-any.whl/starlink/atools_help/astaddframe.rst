

ASTADDFRAME
===========


Purpose
~~~~~~~
Add a Frame to a FrameSet to define a new coordinate system


Description
~~~~~~~~~~~
This application adds a new Frame and an associated Mapping to a
FrameSet so as to define a new coordinate system, derived from one
which already exists within the FrameSet. The new Frame then becomes
the FrameSet's current Frame.


Usage
~~~~~


::

    
       astaddframe this iframe map frame result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FRAME = LITERAL (Read)
``````````````````````
An NDF or text file holding the Frame that describes the new
coordinate system. This application may also be used to merge two
FrameSets by supplying a second FrameSet for this argument (see
SUN/210 for details). If an NDF is supplied, its WCS FrameSet will be
used.



IFRAME = LITERAL (Read)
```````````````````````
The integer index or Domain name of the Frame within the FrameSet
which describes the coordinate system upon which the new one is to be
based (the strings AST__BASE and AST__CURRENT may also be supplied).



MAP = LITERAL (Read)
````````````````````
An NDF or text file holding the Mapping which describes how to convert
coordinates from the old coordinate system (described by the Frame
with index IFRAME) into coordinates in the new system. The Mapping's
forward transformation should perform this conversion, and its inverse
transformation should convert in the opposite direction. If an NDF is
supplied, the Mapping from the Base Frame to the Current Frame of its
WCS FrameSet will be used.



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified FrameSet. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
FrameSet, if possible.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original FrameSet to which a new Frame
is to be added. If an NDF is supplied, the WCS FrameSet will be used.



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


