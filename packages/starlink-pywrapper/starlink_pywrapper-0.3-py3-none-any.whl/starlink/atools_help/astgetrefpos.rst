

ASTGETREFPOS
============


Purpose
~~~~~~~
Get the reference position for a SpecFrame


Description
~~~~~~~~~~~
This application returns the reference position (specified by
attributes RefRA and RefDec) converted to the celestial coordinate
system represented by a supplied SkyFrame. The formated celestial
longitude and latitude values are displayed.


Usage
~~~~~


::

    
       astgetrefpos this frm
       



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
system in which the reference longitude and latitude values should be
displayed. If an NDF is supplied, the current Frame of its WCS
FrameSet will be used. If a null (!) value is supplied, the reference
position will be displayed as FK5 J2000 right ascension and
declination.



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


