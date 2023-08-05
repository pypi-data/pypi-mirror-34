

ASTPICKAXES
===========


Purpose
~~~~~~~
Create a new Frame by picking axes from an existing one


Description
~~~~~~~~~~~
This application creates a new Frame whose axes are copied from an
existing Frame along with other Frame attributes, such as its Title.
Any number (zero or more) of the original Frame's axes may be copied,
in any order, and additional axes with default attributes may also be
included in the new Frame.
A Mapping that converts between the coordinate systems described by
the two Frames may also be created.


Usage
~~~~~


::

    
       astpickaxes this axes map result
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES() = _INTEGER (Read)
````````````````````````
A vector of integers which lists the axes to be copied. These should
be given in the order required in the new Frame, using the axis
numbering in the original Frame (which starts at 1 for the first
axis). Axes may be selected in any order, but each may only be used
once. If additional (default) axes are also to be included, the
corresponding elements of this array should be set to zero.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



MAP = LITERAL (Read)
````````````````````
A text file to receive a new Mapping. This will be a PermMap (or a
UnitMap as a special case) that describes the axis permutation that
has taken place between the original and new Frames. The Mapping's
forward transformation will convert coordinates from the original
Frame into the new one, and vice versa. If this Mapping is not
required, a null (!) value may be supplied for this parameter. [!]



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new Frame.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original FrameSet to which a new Frame
is to be added. If an NDF is supplied, the current Frame of the WCS
FrameSet will be used.



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


