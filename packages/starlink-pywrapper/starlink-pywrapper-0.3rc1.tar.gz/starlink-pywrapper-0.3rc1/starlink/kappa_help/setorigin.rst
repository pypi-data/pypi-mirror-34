

SETORIGIN
=========


Purpose
~~~~~~~
Sets a new pixel origin for an NDF


Description
~~~~~~~~~~~
This application sets a new pixel origin value for an NDF data
structure. The NDF is accessed in update mode and the indices of the
first pixel (the NDF's lower pixel-index bounds) are set to specified
integer values, which may be positive or negative. No other properties
of the NDF are altered. If required, a template NDF may be supplied
and the new origin values will be derived from it.


Usage
~~~~~


::

    
       setorigin ndf origin
       



ADAM parameters
~~~~~~~~~~~~~~~



LIKE = NDF (Read)
`````````````````
This parameter may be used to supply an NDF which is to be used as a
template. If such a template is supplied, then its origin (its lower
pixel-index bounds) will be used as the new origin value for the NDF
supplied via the NDF parameter. By default, no template will be used
and the new origin will be specified via the ORIGIN parameter. [!]



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure whose pixel origin is to be modified.



ORIGIN() = _INTEGER (Read)
``````````````````````````
A 1-dimensional array specifying the new pixel origin values, one for
each NDF dimension.



Examples
~~~~~~~~
setorigin image_2d [1,1]
Sets the indices of the first pixel in the 2-dimensional image
image_2d to be (1,1). The image pixel values are unaltered.
setorigin ndf=starfield
A new pixel origin is set for the NDF structure called starfield.
SETORIGIN will prompt for the new origin values, supplying the
existing values as defaults.
setorigin ndf=cube origin=[-128,-128]
Sets the pixel origin values for the first two dimensions of the
3-dimensional NDF called cube to be (-128,-128). A value for the third
dimension is not specified, so the origin of this dimension will
remain unchanged.
setorigin betapic like=alphapic
Sets the pixel origin of the NDF called betapic to be equal to that of
the NDF called alphapic.



Notes
~~~~~
If the number of new pixel origin values is less than the number of
NDF dimensions, then the pixel origin of the extra dimensions will
remain unchanged. If the number of values exceeds the number of NDF
dimensions, then the excess values will be ignored.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SETBOUND.


Timing
~~~~~~
Setting a new pixel origin is a quick operation whose timing does not
depend on the size of the NDF.


Copyright
~~~~~~~~~
Copyright (C) 1990-1991 Science & Engineering Research Council.
Copyright (C) 1995 Central Laboratory of the Research Councils. All
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


