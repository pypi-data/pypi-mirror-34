

CLUMPINFO
=========


Purpose
~~~~~~~
Obtain information about one or more previously identified clumps


Description
~~~~~~~~~~~
This application returns various items of information about a single
clump, or a collection of clumps, previously identified using
FINDCLUMPS or EXTRACTCLUMPS.


Usage
~~~~~


::

    
       clumpinfo ndf clumps quiet
       



ADAM parameters
~~~~~~~~~~~~~~~



CLUMPS = LITERAL (Read)
```````````````````````
Specifies the indices of the clumps to be included in the returned
information. It can take any of the following values:


+ "ALL" or "*" -- All clumps.
+ "xx,yy,zz" -- A list of clump indices.
+ "xx:yy" -- Clump indices between xx and yy inclusively. When xx is
omitted the range begins from one; when yy is omitted the range ends
with the final clump index.
+ Any reasonable combination of above values separated by commas.





FLBND( ) = _DOUBLE (Write)
``````````````````````````
The lower bounds of the bounding box enclosing the selected clumps in
the current WCS Frame of the input NDF. Celestial axis values are
always in units of radians, but spectral axis units will be in the
spectral units used by the current WCS Frame.



FUBND( ) = _DOUBLE (Write)
``````````````````````````
The upper bounds of the bounding box enclosing the selected clumps.
See parameter FLBND for more details.



LBOUND( ) = _INTEGER (Write)
````````````````````````````
The lower pixel bounds of bounding box enclosing the selected clumps.



NCLUMPS = _INTEGER (Write)
``````````````````````````
The total number of clumps descrriptions stored within the supplied
NDF.



NDF = NDF (Read)
````````````````
The NDF defining the previously identified clumps. This should contain
a CUPID extension describing all the identified clumps, in the format
produced by FINDCLUMPS or EXTRACTCLUMPS.



QUIET = _LOGICAL (Read)
```````````````````````
If TRUE, then no information is written out to the screen, although
the output parameters are still assigned values. [FALSE]



UBOUND( ) = _INTEGER (Write)
````````````````````````````
The upper pixel bounds of bounding box enclosing the selected clumps.



Notes
~~~~~


+ It is hoped to extend the range of information reported by this
  application as new requirements arise.




Synopsis
~~~~~~~~
void clumpinfo( int *status );


Copyright
~~~~~~~~~
Copyright (C) 2007 Particle Physics & Astronomy Research Council. All
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


