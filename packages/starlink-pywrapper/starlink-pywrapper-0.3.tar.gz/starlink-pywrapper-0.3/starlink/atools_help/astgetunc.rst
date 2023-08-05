

ASTGETUNC
=========


Purpose
~~~~~~~
Obtain uncertainty information from a Region


Description
~~~~~~~~~~~
This application returns a Region which represents the uncertainty
associated with positions within the supplied Region. See astSetUnc
for more information about Region uncertainties and their use.


Usage
~~~~~


::

    
       astgetunc this def result
       



ADAM parameters
~~~~~~~~~~~~~~~



DEF = _LOGICAL (Read)
`````````````````````
Controls what is returned if no uncertainty information has been
associated explicitly with the supplied Region. If a TRUE value is
supplied, then the default uncertainty Region used internally within
AST is returned. If FALSE is supplied, then an error is reported.
[TRUE]



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the new Region describing the
uncertainty in the supplied Region.



THIS = LITERAL (Read)
`````````````````````
A text file holding the Region.



Copyright
~~~~~~~~~
Copyright (C) 2013 Science & Technology Facilities Council. All Rights
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


