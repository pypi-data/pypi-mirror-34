

SETNORM
=======


Purpose
~~~~~~~
Sets a new value for one or all of an NDF's axis-normalisation flags


Description
~~~~~~~~~~~
This routine sets a new value for one or all the normalisation flags
in an NDF AXIS data structure. The NDF is accessed in update mode.
This flag determines how the NDF's data and variance arrays behave
when the associated axis information is modified.
If an AXIS structure does not exist, a new one whose centres are pixel
co-ordinates is created.


Usage
~~~~~


::

    
       setnorm ndf dim
       



ADAM parameters
~~~~~~~~~~~~~~~



ANORM = _LOGICAL (Read)
```````````````````````
The normalisation flag for the axis. TRUE means that the data and
variance values in the NDF are normalised to the pixel width values
for the chosen axis so that the product of data value and width, and
variance and the squared width are constant if the width is altered.
A FALSE value means that the data and variance need not alter as the
pixel widths are varied. This is the default for an axis. The
suggested default is the current value.



DIM = _INTEGER (Read)
`````````````````````
The axis dimension for which the normalisation flag is to be modified.
There are separate units for each NDF dimension. A value of 0 sets the
normalisation flag for all the axes. The value must lie between 0 and
the number of dimensions of the NDF. This defaults to 1 for a
1-dimensional NDF. The suggested default is the current value. []



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure in which an axis-normalisation flag is to be
modified.



Examples
~~~~~~~~
setnorm hd23568 0 anorm
This sets the normalisation flags along all axes of the NDF structure
hd23568 to be true.
setnorm ndf=spect noanorm
This sets the normalisation flag of the 1-dimensional NDF structure
spect to be false.
setnorm borg 3 anorm
This sets the normalisation flag for the third dimension in the NDF
structure borg.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SETAXIS.


Axis Normalisation
~~~~~~~~~~~~~~~~~~
In general, the axis-normalisation property is not needed. An example
where it is relevant is a spectrum in which data values representing
energy per unit wavelength and each pixel has a known spread in
wavelength. The sum of each pixel's data value multiplied by its width
gives the energy in a part of the spectrum. A change to the axis
width, say to allow for the redshift, necessitates a corresponding
modification to the data value to retain this property. In two
dimensions an example is where the data measure flux per unit area of
sky and the pixel widths are defined in terms of angular size.


Copyright
~~~~~~~~~
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


