

ASTQUADAPPROX
=============


Purpose
~~~~~~~
Obtain a quadratic approximation to a 2D Mapping


Description
~~~~~~~~~~~
This application returns the co-efficients of a quadratic fit to the
supplied Mapping over the input area specified by LBND and UBND. The
Mapping must have 2 inputs, but may have any number of outputs. The
i'th Mapping output is modelled as a quadratic function of the 2
inputs (x,y):
output_i = a_i_0 + a_i_1*x + a_i_2*y + a_i_3*x*y + a_i_4*x*x +
a_i_5*y*y
The FIT array is returned holding the values of the co-efficients
a_0_0, a_0_1, etc.


Usage
~~~~~


::

    
       astquadapprox this lbnd ubnd nx ny
       



ADAM parameters
~~~~~~~~~~~~~~~



FIT() = _DOUBLE (Write)
```````````````````````
An array returning the co-efficients of the quadratic approximation to
the specified transformation. The first 6 elements hold the fit to the
first Mapping output. The next 6 elements hold the fit to the second
Mapping output, etc. So if the Mapping has 2 inputs and 2 outputs the
quadratic approximation to the forward transformation is:
X_out = fit(1) + fit(2)*X_in + fit(3)*Y_in + fit(4)*X_in*Y_in +
fit(5)*X_in*X_in + fit(6)*Y_in*Y_in
Y_out = fit(7) + fit(8)*X_in + fit(9)*Y_in + fit(10)*X_in*Y_in +
fit(11)*X_in*X_in + fit(12)*Y_in*Y_in



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
will be used. The Mapping must have 2 inputs.



LBND( 2 ) = _DOUBLE (Read)
``````````````````````````
A two element array containing the lower bound of the input region in
each input dimension. If an NDF was supplied for THIS, then a null (!)
value can be supplied in which case a default will be used
corresponding to the GRID cordinates of the bottom left corner of the
bottom left pixel in the NDF (i.e. a value of 0.5 on every grid axis).



NX = _INTEGER (Read)
````````````````````
The number of points to place along the first Mapping input. The first
point is at LBND( 1 ) and the last is at UBND( 1 ). If a value less
than three is supplied a value of three will be used. If an NDF was
supplied for THIS, then a null (!) value can be supplied in which case
a default will be used corresponding to the number of pixels along the
axis.



NY = _INTEGER (Read)
````````````````````
The number of points to place along the second Mapping input. The
first point is at LBND( 2 ) and the last is at UBND( 2 ). If a value
less than three is supplied a value of three will be used. If an NDF
was supplied for THIS, then a null (!) value can be supplied in which
case a default will be used corresponding to the number of pixels
along the axis.



RMS = _DOUBLE (Write)
`````````````````````
The RMS residual between the mapping and the fit, taken over all
outputs.



UBND( 2 ) = _DOUBLE (Read)
``````````````````````````
A two element array containing the upper bound of the input region in
each input dimension. If an NDF was supplied for THIS, then a null (!)
value can be supplied in which case a default will be used
corresponding to the GRID cordinates of the top right corner of the
top right pixel in the NDF (i.e. a value of (DIM+0.5) on every grid
axis, where DIM is the number of pixels along the axis).



Copyright
~~~~~~~~~
Copyright (C) 2010 Science and Technology Facilities Council Councils.
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


