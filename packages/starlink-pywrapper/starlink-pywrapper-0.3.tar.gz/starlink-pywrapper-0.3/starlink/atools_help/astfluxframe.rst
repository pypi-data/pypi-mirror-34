

ASTFLUXFRAME
============


Purpose
~~~~~~~
Create a FluxFrame


Description
~~~~~~~~~~~
This application creates a new FluxFrame and optionally initialises
its attributes.
A FluxFrame is a specialised form of one-dimensional Frame which
represents various systems used to represent the signal level in an
observation. The particular coordinate system to be used is specified
by setting the FluxFrame's System attribute qualified, as necessary,
by other attributes such as the units, etc (see the description of the
System attribute for details).
All flux values are assumed to be measured at the same frequency or
wavelength (as given by the SpecVal attribute). Thus this class is
more appropriate for use with images rather than spectra.


Usage
~~~~~


::

    
       astfluxframe specval specfrm options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



SPECFRM = LITERAL (Read)
````````````````````````
An NDF or text file holding a SpecFrame describing the spectral
coordinate system in which the SPECVAL parameter is given. Only
accessed if a non-null value is supplied for SPECVAL. If an NDF is
supplied, the current Frame in the WCS FrameSet will be used (which
must be a SpecFrame)



SPECVAL = _DOUBLE (Read)
````````````````````````
The spectral value to which the flux values refer, given in the
spectral coordinate system specified by SPECFRM. The value supplied
for the SPECVAL parameter becomes the default value for the SpecVal
attribute. A null value (!) may be supplied if the spectral position
is unknown (in which case no value will be set for SpecVal), but this
may result in it not being possible for the AST_CONVERT function to
determine a Mapping between the new FluxFrame and some other
FluxFrames.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new FluxFrame.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new FluxFrame.



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


