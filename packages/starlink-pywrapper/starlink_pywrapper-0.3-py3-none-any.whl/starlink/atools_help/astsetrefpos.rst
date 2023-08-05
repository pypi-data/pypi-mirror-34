

ASTSETREFPOS
============


Purpose
~~~~~~~
Set the reference position for a SpecFrame


Description
~~~~~~~~~~~
This application sets the reference position of a SpecFrame (specified
by attributes RefRA and RefDec) using axis values (in radians)
supplied within the celestial coordinate system represented by a
supplied SkyFrame.


Usage
~~~~~


::

    
       astsetrefpos this frm lon lat result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FRM = LITERAL (Read)
````````````````````
An NDF or text file holding the SkyFrame that describes the coordinate
system to which the LON and LAT parameter values refer. If an NDF is
supplied, the current Frame of its WCS FrameSet will be used. If a
null (!) value is supplied, LON and LAT will be assumed to be FK5
J2000 right ascension and declination.



LAT = LITERAL (Read)
````````````````````
The formatted sky latitude value of the reference position, in the
system specified by FRM.



LON = _DOUBLE (Read)
````````````````````
The formatted sky longitude value of the reference position, in the
system specified by FRM.



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified SpecFrame. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
Object if possible (if it is a FrameSet in which the base Frame has
Domain GRID and has 1 axis for each NDF dimension).



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the SpecFrame. If an NDF is supplied, the
current Frame in the WCS FrameSet will be used.



Copyright
~~~~~~~~~
Copyright (C) 2003 Central Laboratory of the Research Councils. All
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


