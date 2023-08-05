

ASTLINEARAPPROX
===============


Purpose
~~~~~~~
Find a linear approximation to a mapping


Description
~~~~~~~~~~~
This application allows you to find a linear approximation to a
mapping over a region in the base coordinates. A typical use might be
to calculate the orientation and scale of an image after being
transformed by a Mapping.


Usage
~~~~~


::

    
       astlinearapprox this lbndin ubndin fit
       



ADAM parameters
~~~~~~~~~~~~~~~



FIT() = _DOUBLE (Write)
```````````````````````
An array returning the co-efficients of the linear approximation to
the specified transformation. The first Nout elements hold the
constant offsets for the transformation outputs. The remaining
elements hold the gradients. So if the Mapping has 2 inputs and 2
outputs the linear approximation to the forward transformation is:
X_out = fit[0] + fit[2]*X_in + fit[3]*Y_in Y_out = fit[1] +
fit[4]*X_in + fit[5]*Y_in



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping. If an NDF is supplied, the
Mapping from the base Frame of the WCS FrameSet to the current Frame
will be used.



LBNDIN() = _DOUBLE (Read)
`````````````````````````
An array with one element for each Mapping input coordinate. This
should contain the lower bound of the input region in each input
dimension. If an NDF was supplied for THIS and FORWARD is true, then a
null (!) value can be supplied in which case a default will be used
corresponding to the GRID cordinates of the bottom left corner of the
bottom left pixel in the NDF (i.e. a value of 0.5 on every grid axis).



UBNDIN() = _DOUBLE (Read)
`````````````````````````
An array with one element for each Mapping input coordinate. This
should contain the upper bound of the input region in each input
dimension. Note that it is permissible for the upper bound to be less
than the corresponding lower bound, as the values will simply be
swapped before use. If an NDF was supplied for THIS and FORWARD is
true, then a null (!) value can be supplied in which case a default
will be used corresponding to the GRID cordinates of the top right
corner of the top right pixel in the NDF (i.e. a value of (DIM+0.5) on
every grid axis, where DIM is the number of pixels along the axis).



TOL = _DOUBLE (Read)
````````````````````
The maximum permitted deviation from linearity, expressed as a
positive Cartesian displacement in the output coordinate space of the
Mapping. If a linear fit to the forward transformation of the Mapping
deviates from the true transformation by more than this amount at any
point which is tested, then no fit coefficients will be returned.



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


