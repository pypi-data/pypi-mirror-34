

RAWRECREATEWCS
==============


Purpose
~~~~~~~
Fix broken raw ACSIS files by enabling the spectral WCS to be
reconstructed


Description
~~~~~~~~~~~
Some ACSIS faults result in a file being written with the frequency
axis unable to be written because of an error in the FITS WCS stored
in the FITS header. This command lets the spectral WCS be recreated
once the FITS header has been fixed following a manual intervention.
This command will fail on files that already have had the WCS
information stripped from the FITS header.


ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read)
````````````````
Input files to be fixed.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



Notes
~~~~~


+ Supports ACSIS raw data files




Copyright
~~~~~~~~~
Copyright (C) 2011 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA


