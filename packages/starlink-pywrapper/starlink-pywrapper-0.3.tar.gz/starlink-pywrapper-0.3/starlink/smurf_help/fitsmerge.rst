

FITSMERGE
=========


Purpose
~~~~~~~
Merge FITS headers


Description
~~~~~~~~~~~
This routine reads the FITS headers of the files mentioned in the IN
Parameter and merges them using the smf_fits_outhdr function. The
merged headers are then written into the file specified by the NDF
Parameter.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Files containing input FITS headers.



NDF = NDF (Read and Write)
``````````````````````````
File to receive merged FITS headers.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSLIST, FITSMOD


Copyright
~~~~~~~~~
Copyright (C) 2014 Science and Technology Facilities Council. All
Rights Reserved.


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
02110-1301, USA


