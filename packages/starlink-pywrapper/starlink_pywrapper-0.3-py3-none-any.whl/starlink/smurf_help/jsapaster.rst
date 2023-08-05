

JSAPASTER
=========


Purpose
~~~~~~~
Paste several JSA tiles into a single mosaic


Description
~~~~~~~~~~~
This routine creates a single output NDF by pasting together a
supplied list of 2D- or 3D- JSA tiles (i.e. it is the inverse of
JSADICER). The spatial WCS of each input NDF must matches the JSA all-
sky pixel grid. The output NDF will usually be gridded using an HPX
projection, but an XPH projection will be used if the mosaic would
cross a discontinuity in the HPX projection.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
A group of input JSA tiles.



INSTRUMENT = LITERAL (Read)
```````````````````````````
The JCMT instrument (different instruments have different tiling
schemes and pixel sizes). The following instrument names are
recognised (unambiguous abbreviations may be supplied):
"SCUBA-2(450)", "SCUBA-2(850)", "ACSIS", "DAS". The dynamic default is
determined from the input NDF if possible. If this cannot be done,
then no dynamic default is provided, and the user is prompted for a
value if none was supplied on the command line. []



OUT = NDF (Write)
`````````````````
The mosaic.



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


