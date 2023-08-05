

AXCONV
======


Purpose
~~~~~~~
Expands spaced axes in an NDF into the primitive form


Description
~~~~~~~~~~~
This application routine converts in situ an NDF's axis centres in the
`spaced' form into `simple' form. Applications using the NDF_ library,
such as KAPPA, are not currently capable of supporting spaced arrays,
but there are packages that produce NDF files with this form of axis,
notably Asterix. This application provides a temporary method of
allowing KAPPA et al. to handle these NDF datasets.


Usage
~~~~~


::

    
       axconv ndf
       



ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read and Write)
``````````````````````````
The NDF to be modified.



Examples
~~~~~~~~
axconv rosat256
This converts the spaced axes in the NDF called rosat256 into simple
form.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SETAXIS.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995, 2004 Central Laboratory of the Research Councils. All Rights
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ Only axes with a real data type are created.




