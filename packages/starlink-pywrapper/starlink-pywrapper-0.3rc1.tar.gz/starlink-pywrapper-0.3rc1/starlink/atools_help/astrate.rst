

ASTRATE
=======


Purpose
~~~~~~~
Calculate the rate of change of a Mapping output


Description
~~~~~~~~~~~
This application evaluates the rate of change of a specified output of
the supplied Mapping with respect to a specified input, at a specified
input position.
The result is estimated by interpolating the function using a fourth
order polynomial in the neighbourhood of the specified position. The
size of the neighbourhood used is chosen to minimise the RMS residual
per unit length between the interpolating polynomial and the supplied
Mapping function. This method produces good accuracy but can involve
evaluating the Mapping one hundred times or more.


Usage
~~~~~


::

    
       astrate this at ax1 ax2
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



RATE = _DOUBLE (Write)
``````````````````````
A scale in which to store the rate of change of Mapping output AX1
with respect to input AX2, evaluated at AT.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping. If an NDF is supplied, the
Mapping from the base Frame of the WCS FrameSet to the current Frame
will be used.



AT() = _DOUBLE (Read)
`````````````````````
An array holding the axis values at the position at which the rate of
change is to be evaluated. The number of elements in



this array should equal the number of inputs to the Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AX1 = _INTEGER (Read) The index of the Mapping output for which the
rate of change is to be found (output numbering starts at 1 for the
first output). AX2 = _INTEGER (Read) The index of the Mapping input
which is to be varied in order to find the rate of change (input
numbering starts at 1 for the first input).


Copyright
~~~~~~~~~
Copyright (C) 2009 Science and Technology Facilities Council Councils.
All Rights Reserved.


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


