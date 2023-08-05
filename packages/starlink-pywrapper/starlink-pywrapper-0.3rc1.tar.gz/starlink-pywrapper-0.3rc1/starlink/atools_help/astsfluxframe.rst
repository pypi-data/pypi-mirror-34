

ASTSFLUXFRAME
=============


Purpose
~~~~~~~
Create a SpecFluxFrame


Description
~~~~~~~~~~~
This application creates a new SpecFluxFrame and optionally
initialises its attributes.
A SpecFluxFrame combines a SpecFrame and a FluxFrame into a single
2-dimensional compound Frame. Such a Frame can for instance be used to
describe a Plot of a spectrum in which the first axis represents
spectral position and the second axis represents flux.


Usage
~~~~~


::

    
       astspecfluxframe frame1 frame2 options result
       



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
An NDF or text file holding the SpecFrame. This will form the first
axis in the new SpecFluxFrame. If an NDF is supplied, the current
Frame in its WCS FrameSet will be used (which must be a SpecFrame).



FRAME2 = LITERAL (Read)
```````````````````````
An NDF or text file holding the FluxFrame. This will form the second
axis in the new SpecFluxFrame. The "SpecVal" attribute of this
FluxFrame is not used by the SpecFluxFrame class and so may be set
null when the FluxFrame is created. If an NDF is supplied, the current
Frame in its WCS FrameSet will be used (which must be a FluxFrame).



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new SpecFluxFrame.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new SpecFluxFrame.



Copyright
~~~~~~~~~
Copyright (C) 2005 Particle Physics & Astronomy Research Council. All
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


