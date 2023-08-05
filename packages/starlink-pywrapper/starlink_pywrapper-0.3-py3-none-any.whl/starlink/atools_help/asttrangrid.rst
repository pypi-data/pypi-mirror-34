

ASTTRANGRID
===========


Purpose
~~~~~~~
Transform a grid of positions


Description
~~~~~~~~~~~
This application uses a supplied Mapping to transforms the pixel
coordinates at the centre of every pixel in a grid with specified
pixel index bounds. The resulting coordinate values are stored in an
output NDF with the same pixel bounds. This output NDF has an extra
trailing pixel axis that enumerates the outputs from the Mapping. This
extra axis has pixel index bounds "1:Nout", where "Nout" is the number
of axis values produced by the supplied Mapping.
Efficiency is improved by first approximating the Mapping with a
linear transformation applied over the whole region of the input grid
which is being used. If this proves to be insufficiently accurate, the
input region is sub-divided into two along its largest dimension and
the process is repeated within each of the resulting sub-regions. This
process of sub-division continues until a sufficiently good linear
approximation is found, or the region to which it is being applied
becomes too small (in which case the original Mapping is used
directly).


Usage
~~~~~


::

    
       asttrangrid this lbnd ubnd tol maxpix forward result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



LBND() = _INTEGER (Read)
````````````````````````
The lower pixel index bounds of the output NDF. The number of values
supplied should equal the Nin attribute of the supplied Mapping.



FORWARD = _LOGICAL (Read)
`````````````````````````
A TRUE value indicates that the Mapping's forward coordinate
transformation is to be applied, while a FALSE value indicates that
the inverse transformation should be used. [TRUE]



MAXPIX = _INTEGER (Read)
````````````````````````
A value which specifies an initial scale size (in input grid points)
for the adaptive algorithm which approximates non-linear Mappings with
piece-wise linear transformations. Normally, this should be a large
value (larger than any dimension of the region of the input grid being
used). In this case, a first attempt to approximate the Mapping by a
linear transformation will be made over the entire input region.
If a smaller value is used, the input region will first be divided
into sub-regions whose size does not exceed "maxpix" grid points in
any dimension. Only at this point will attempts at approximation
commence.
This value may occasionally be useful in preventing false convergence
of the adaptive algorithm in cases where the Mapping appears
approximately linear on large scales, but has irregularities (e.g.
holes) on smaller scales. A value of, say, 50 to 100 grid points can
also be employed as a safeguard in general-purpose software, since the
effect on performance is minimal.
If too small a value is given, it will have the effect of inhibiting
linear approximation altogether (equivalent to setting "tol" to zero).
Although this may degrade performance, accurate results will still be
obtained. [100]



RESULT = NDF (Write)
````````````````````
The output NDF. This will have "Nin+1" pixel axes, where "Nin" is the
number of inputs for the supplied Mapping. The extra pixel axis in the
output NDF will have bounds "1:Nout", where "Nout" is the number of
outputs for the supplied Mapping. The bounds on the first Nin axes of
the output NDF are given by LBND and UBND.



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the Mapping. If an NDF is supplied, the
Mapping from the base Frame of the WCS FrameSet to the current Frame
will be used. The inputs of this Mapping correspond to pixel
coordinates within the output NDF.



TOL = _DOUBLE (Read)
````````````````````
The maximum tolerable geometrical distortion which may be introduced
as a result of approximating non-linear Mappings by a set of piece-
wise linear transformations. This should be expressed as a
displacement within the output coordinate system of the Mapping.
If piece-wise linear approximation is not required, a value of zero
may be given. This will ensure that the Mapping is used without any
approximation, but may increase execution time.
If the value is too high, discontinuities between the linear
approximations used in adjacent panel will be higher. If this is a
problem, reduce the tolerance value used. [0.0]



UBND() = _INTEGER (Read)
````````````````````````
The upper pixel index bounds of the output NDF. The number of values
supplied should equal the Nin attribute of the supplied Mapping.



Notes
~~~~~


+ The supplied Mapping inputs correspond to pixel coordinates in the
  grid. Particularly, this means that integer values are located at
  pixel corners. But astTranGrid assumes an input coordinate system in
  which integer values are located at pixel centres. Therefore, the
  supplied Mapping is modified before passing it to astTranGrid. This
  modification consists of prepending a Shiftmap that shifts each input
  axis value by -0.5.




Copyright
~~~~~~~~~
Copyright (C) 2010 Science & Technology Facilities Council. All Rights
Reserved.


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


