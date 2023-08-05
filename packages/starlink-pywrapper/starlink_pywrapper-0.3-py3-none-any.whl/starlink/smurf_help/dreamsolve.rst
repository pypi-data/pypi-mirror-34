

DREAMSOLVE
==========


Purpose
~~~~~~~
Solve DREAM observations and generate 2-D images


Description
~~~~~~~~~~~
This command reconstructs a series of 2-D images from DREAM
observations. The images are written as NDFs under the .MORE.SCU2RED
extension.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Name of input data files.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Name of output files containing DREAM images. The DREAM images will be
written to extensions to match that in use by the SCUBA-2 data
acquisition system.



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: DREAMWEIGHTS, STARECALC; KAPPA: WCSMOSAIC; CCDPACK: MAKEMOS


Copyright
~~~~~~~~~
Copyright (C) 2008 Science and Technology Facilities Council.
Copyright (C) 2006 University of British Columbia. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA.


