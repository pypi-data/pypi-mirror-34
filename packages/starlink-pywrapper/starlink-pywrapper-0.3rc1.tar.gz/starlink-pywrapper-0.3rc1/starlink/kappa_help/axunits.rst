

AXUNITS
=======


Purpose
~~~~~~~
Sets a new units value for an axis within an NDF data structure


Description
~~~~~~~~~~~
This routine sets a new value for a UNITS component of an existing NDF
AXIS data structure. The NDF is accessed in update mode and any pre-
existing UNITS component is over-written with a new value.
Alternatively, if a `null' value (!) is given for the UNITS parameter,
then the NDF's axis UNITS component will be erased. If an AXIS
structure does not exist, a new one whose centres are pixel co-
ordinates is created.


Usage
~~~~~


::

    
       axunits ndf units dim
       



ADAM parameters
~~~~~~~~~~~~~~~



DIM = _INTEGER (Read)
`````````````````````
The axis dimension for which the units is to be modified. There are
separate units for each NDF dimension. The value must lie between 1
and the number of dimensions of the NDF. This defaults to 1 for a
1-dimensional NDF. The suggested default is the current value. []



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure in which an axis UNITS component is to be
modified.



UNITS = LITERAL (Read)
``````````````````````
The value to be assigned to the NDF's axis UNITS component (e.g.
"Pixels" or "km/s"). UNITS describes the physical units of the
quantity measured along the axis. This value may later be used by
other applications for labelling graphs and other forms of display
where the NDF's axis co-ordinates are shown. The suggested default is
the current value.



Examples
~~~~~~~~
axunits ngc253 "arcsec" 2
Sets the UNITS component of the second axis dimension of the NDF
structure ngc253 to have the value "arcsec".
axunits ndf=spect units=Angstrom
Sets the axis UNITS component of the 1-dimensional NDF structure spect
to have the value "Angstrom".
axunits datafile units=! dim=3
By specifying a null value (!), this example erases any previous value
of the UNITS component for the third dimension in the NDF structure
datafile.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: AXLABEL, SETAXIS, SETUNITS.


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


