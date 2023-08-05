

JSADICER
========


Purpose
~~~~~~~
Dice an image or cube into JSA tiles


Description
~~~~~~~~~~~
This routine creates multiple output NDFs by dicing a supplied 2D- or
3D- NDF up into JSA tiles (i.e. it is the inverse of JSAPASTER). The
spatial WCS of the input NDF must matches the JSA all-sky grid.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input 2D or 3D NDF - it need not have been created by a smurf
task. Currently, it should be gridded on the JSA all-sky pixel grid,
which means that in practice it probably will have been created by
MAKEMAP or MAKECUBE.



INSTRUMENT = LITERAL (Read)
```````````````````````````
The JCMT instrument (different instruments have different tiling
schemes and pixel sizes). The following instrument names are
recognised (unambiguous abbreviations may be supplied):
"SCUBA-2(450)", "SCUBA-2(850)", "ACSIS", "DAS". The dynamic default is
determined from the input NDF if possible. If this cannot be done,
then no dynamic default is provided, and the user is prompted for a
value if none was supplied on the command line. []



JSATILELIST() = _INTEGER (Write)
````````````````````````````````
Returned holding the zero-based indices of the created JSA tiles. The
number of such indices is given the "NTILE" parameter



NTILE = _INTEGER (Write)
````````````````````````
AN output parameter which is returned holding the number of output
NDFs created.



OUT = NDF (Write)
`````````````````
The base-name for the output NDFs. The names will be formed by
appending the tile number to the basename, preceded by an underscore.
A null(!) value causes the name of the input NDF to be used. [!]



OUTFILES = LITERAL (Write)
``````````````````````````
The name of a text file to create, in which to put the names of all
the output NDFs created by this application via parameter OUT (one per
line). If a null (!) value is supplied no file is created. [!]



PROJ = LITERAL (Read)
`````````````````````
Determines the projection used by the output NDFs. The allowed values
are "HPX" (HPX projection centred on RA=0h), "HPX12" (HPX projection
centred on RA=12h), "XPHN" (XPH projection centred on the north pole)
and "XPHS" (XPH projection centred on the south pole). A null (!)
value causes "HPX" to be used. ["HPX"]



TRIM = _INTEGER (Read)
``````````````````````
A zero or negative value results in each output NDF covering the full
area of the corresponding JSAtile. A value of one results in each
output NDF being cropped to the bounds of the supplied NDF. A value of
two or more results in each output NDF being cropped to remove any
blank borders. [2]



Copyright
~~~~~~~~~
Copyright (C) 2013-2014 Science and Technology Facilities Council. All
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


