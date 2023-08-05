

ASTREMAPFRAME
=============


Purpose
~~~~~~~
Modify a Frame's relationship to other Frames in a FrameSet


Description
~~~~~~~~~~~
This application modifies the relationship (i.e. Mapping) between a
specified Frame in a FrameSet and the other Frames in that FrameSet.
Typically, this might be required if the FrameSet has been used to
calibrate (say) an image, and that image is re-binned. The Frame
describing the image will then have undergone a coordinate
transformation, and this should be communicated to the associated
FrameSet using this routine.


Usage
~~~~~


::

    
       astremapframe this iframe map result
       



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
The integer index or Domain name of the Frame to be modified within
the FrameSet (the strings AST__BASE and AST__CURRENT may also be
supplied).



MAP = LITERAL (Read)
````````````````````
An NDF or text file holding a Mapping whose forward transformation
converts coordinate values from the original coordinate system
described by the Frame to the new one, and whose inverse
transformation converts in the opposite direction. If an NDF is
supplied, the Mapping from the Base Frame to the Current Frame of its
WCS FrameSet will be used.



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified FrameSet. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
FrameSet, if possible.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original FrameSet. If an NDF is
supplied, the WCS FrameSet will be used.



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


