

SETLABEL
========


Purpose
~~~~~~~
Sets a new label for an NDF data structure


Description
~~~~~~~~~~~
This routine sets a new value for the LABEL component of an existing
NDF data structure. The NDF is accessed in update mode and any pre-
existing label is over-written with a new value. Alternatively, if a
`null' value (!) is given for the LABEL parameter, then the NDF's
label will be erased.


Usage
~~~~~


::

    
       setlabel ndf label
       



ADAM parameters
~~~~~~~~~~~~~~~



LABEL = LITERAL (Read)
``````````````````````
The value to be assigned to the NDF's LABEL component. This should
describe the type of quantity represented in the NDF's data array
(e.g. "Surface Brightness" or "Flux Density"). The value may later be
used by other applications, for instance to label the axes of graphs
where the NDF's data values are plotted. The suggested default is the
current value.



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure whose label is to be modified.



Examples
~~~~~~~~
setlabel ngc1068 "Surface Brightness"
Sets the LABEL component of the NDF structure ngc1068 to be "Surface
Brightness".
setlabel ndf=datastruct label="Flux Density"
Sets the LABEL component of the NDF structure datastruct to be "Flux
Density".
setlabel raw_data label=!
By specifying a null value (!), this example erases any previous value
of the LABEL component in the NDF structure raw_data.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: AXLABEL, SETTITLE, SETUNITS.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992 Science & Engineering Research Council.
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


