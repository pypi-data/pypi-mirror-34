

ASTDSBFRAME
===========


Purpose
~~~~~~~
Create a DSBSpecFrame


Description
~~~~~~~~~~~
This application creates a new DSBSpecFrame and optionally initialises
its attributes. A DSBSpecFrame is a specialised form of SpecFrame
which represents positions in a spectrum obtained using a dual
sideband instrument. Such an instrument produces a spectrum in which
each point contains contributions from two distinctly different
frequencies, one from the "lower side band" (LSB) and one from the
"upper side band" (USB). Corresponding LSB and USB frequencies are
connected by the fact that they are an equal distance on either side
of a fixed central frequency known as the "Local Oscillator" (LO)
frequency.
When quoting a position within such a spectrum, it is necessary to
indicate whether the quoted position is the USB position or the
corresponding LSB position. The SideBand attribute provides this
indication.
In practice, the LO frequency is specified by giving the distance from
the LO frequency to some "central" spectral position. Typically this
central position is that of some interesting spectral feature. The
distance from this central position to the LO frequency is known as
the "intermediate frequency" (IF). The value supplied for IF can be a
signed value in order to indicate whether the LO frequency is above of
below the central position.


Usage
~~~~~


::

    
       astdsbframe options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new DSBSpecFrame.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new DSBSpecFrame.



Copyright
~~~~~~~~~
Copyright (C) 2004 Central Laboratory of the Research Councils. All
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


