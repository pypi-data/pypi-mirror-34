

ASTCMPFRAME
===========


Purpose
~~~~~~~
Create a CmpFrame


Description
~~~~~~~~~~~
This application creates a new CmpFrame and optionally initialises its
attributes. A CmpFrame is a compound Frame which allows two component
Frames (of any class) to be merged together to form a more complex
Frame. The axes of the two component Frames then appear together in
the resulting CmpFrame (those of the first Frame, followed by those of
the second Frame).
Since a CmpFrame is itself a Frame, it can be used as a component in
forming further CmpFrames. Frames of arbitrary complexity may be built
from simple individual Frames in this way.


Usage
~~~~~


::

    
       astcmpframe frame1 frame2 options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FRAME1 = LITERAL (Read)
```````````````````````
An NDF or text file holding the first component Frame. If an NDF is
supplied, the current Frame in its WCS FrameSet will be used.



FRAME2 = LITERAL (Read)
```````````````````````
An NDF or text file holding the second component Frame. If an NDF is
supplied, the current Frame in its WCS FrameSet will be used.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new CmpFrame.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new CmpFrame.



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


