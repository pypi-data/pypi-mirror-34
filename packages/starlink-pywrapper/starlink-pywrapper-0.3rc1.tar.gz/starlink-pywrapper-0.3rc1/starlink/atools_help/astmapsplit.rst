

ASTMAPSPLIT
===========


Purpose
~~~~~~~
Split a Mapping up into parallel component Mappings


Description
~~~~~~~~~~~
This application returns a Mapping that will convert coordinates
between the coordinate systems represented by two Frames in a
FrameSet.
This application creates a new Mapping which connects specified inputs
within a supplied Mapping to the corresponding outputs of the supplied
Mapping. This is only possible if the specified inputs correspond to
some subset of the Mapping outputs. That is, there must exist a subset
of the Mapping outputs for which each output depends only on the
selected Mapping inputs, and not on any of the inputs which have not
been selected. If this condition is not met by the supplied Mapping,
then an error is reported.


Usage
~~~~~


::

    
       astmapsplit this in out map
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



IN() = _INTEGER (Read)
``````````````````````
A vector of integers which are the indices within the supplied Mapping
(THIS) of the inputs which are to be picked from the Mapping (the
first Mapping input has index 1).



MAP = LITERAL (Read)
````````````````````
An text file to receive the output Mapping. The number of inputs to
this Mapping will be the same as the number of values supplied for the
IN parameter (the number of outputs may be different).



OUT() = _INTEGER (Write)
````````````````````````
An output parameter to which is written a vector of integers which are
the indices of the outputs of the supplied Mapping fed by the picked
inputs. A value of one is used to refer to the first Mapping output.
The number of values stored in the array on exit will equal the number
of outputs in the returned Mapping. The i'th element in the returned
array holds the index within the supplied Mapping which corresponds to
the i'th output of the returned Mapping.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the input Mapping. If an NDF is supplied,
the base to current Mapping within the WCS FrameSet will be used.



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


