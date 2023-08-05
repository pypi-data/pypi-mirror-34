

ASTFRAMESET
===========


Purpose
~~~~~~~
Create a FrameSet


Description
~~~~~~~~~~~
This application creates a new FrameSet and optionally initialises its
attributes. A FrameSet consists of a set of one or more Frames (which
describe coordinate systems), connected together by Mappings (which
describe how the coordinate systems are inter-related). A FrameSet
makes it possible to obtain a Mapping between any pair of these Frames
(i.e. to convert between any of the coordinate systems which it
describes). The individual Frames are identified within the FrameSet
by an integer index, with Frames being numbered consecutively from one
as they are added to the FrameSet.
Every FrameSet has a "base" Frame and a "current" Frame (which are
allowed to be the same). Any of the Frames may be nominated to hold
these positions, and the choice is determined by the values of the
FrameSet's Base and Current attributes, which hold the indices of the
relevant Frames. By default, the first Frame added to a FrameSet is
its base Frame, and the last one added is its current Frame.
The base Frame describes the "native" coordinate system of whatever
the FrameSet is used to calibrate (e.g. the pixel coordinates of an
image) and the current Frame describes the "apparent" coordinate
system in which it should be viewed (e.g. displayed, etc.). Any
further Frames represent a library of alternative coordinate systems,
which may be selected by making them current.
When a FrameSet is used in a context that requires a Frame, (e.g.
obtaining its Title value, or number of axes), the current Frame is
used. A FrameSet may therefore be used in place of its current Frame
in most situations.
When a FrameSet is used in a context that requires a Mapping, the
Mapping used is the one between its base Frame and its current Frame.
Thus, a FrameSet may be used to convert "native" coordinates into
"apparent" ones, and vice versa. Like any Mapping, a FrameSet may also
be inverted (see AST_INVERT), which has the effect of interchanging
its base and current Frames and hence of reversing the Mapping between
them.


Usage
~~~~~


::

    
       astframeset frame options result
       



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
An NDF or text file holding the first Frame to be inserted into the
FrameSet. This initially becomes both the base and the current Frame.
(Further Frames may be added using the addframe). If an NDF is
supplied, the current Frame in its WCS FrameSet will be used.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new FrameSet.



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the new FrameSet. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
FrameSet, if possible.



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


