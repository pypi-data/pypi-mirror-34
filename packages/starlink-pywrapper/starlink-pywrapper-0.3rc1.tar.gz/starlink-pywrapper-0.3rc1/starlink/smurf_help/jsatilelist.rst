

JSATILELIST
===========


Purpose
~~~~~~~
List the sky tiles that overlap a given set of data files or an AST
Region


Description
~~~~~~~~~~~
This routine returns a list containing the indices of the sky tiles
(for a named JCMT instrument) that overlap a supplied AST Region, map,
cube or group of raw data files.


ADAM parameters
~~~~~~~~~~~~~~~



IN = LITERAL (Read)
```````````````````
Specifies the region of sky for which tiles should be listed. It may
be:


+ The name of a text file containing an AST Region. The Region can be
either 2D or 3D but must include celestial axes.
+ The path to a 2- or 3-D NDF holding a reduced map or cube. This need
not necessarily hold JCMT data, but must have celestial axes in its
current WCS Frame.
+ A group of raw JCMT data files.
+ A null (!) value, in which case a polygon region is used as defined
  by the parameters VERTEX_RA and VERTEX_DEC.





INSTRUMENT = LITERAL (Read)
```````````````````````````
The JCMT instrument (different instruments have different tiling
schemes and pixel sizes). The following instrument names are
recognised (unambiguous abbreviations may be supplied):
"SCUBA-2(450)", "SCUBA-2(850)", "ACSIS", "DAS". If one or more NDFs
are supplied for parameter IN, then a dynamic default is determined if
possible from the first NDF. If this cannot be done, or if a Region is
supplied for parameter IN, then no dynamic default is provided, and
the user is prompted for a value if none was supplied on the command
line. []



PROJ = LITERAL (Write)
``````````````````````
The type of JSA projection that should be used to describe the area of
sky covered by the returned lost of tiles. Will be one of "HPX",
"HPX12", "XPHN" or "XPHS". The choice is made to minimise the
possibility of a projection discontinuity falling within the sky area
covered by the tiles.



TILES(*) = _INTEGER (Write)
```````````````````````````
An output parameter to which is written the list of integer tile
indices.



VERTEX_DEC(*) = _DOUBLE (Read)
``````````````````````````````
The ICRA Dec value at each vertex of a polygon, in degrees. Only used
if IN is null.



VERTEX_RA(*) = _DOUBLE (Read)
`````````````````````````````
The ICRA RA value at each vertex of a polygon, in degrees. Only used
if IN is null.



Tile Definitions
~~~~~~~~~~~~~~~~
It should never be necessary to know the specific details of the
tiling scheme used by SMURF. But for reference, it works as follows:
The whole sky is covered by an HPX (HEALPix) projection containing 12
basic square facets, the reference point of the projection is put at
(RA,Dec)=(0,0) (except for facet six that has a reference point of
(12h,0)). The projection plane is rotated by 45 degrees so that the
edges of each facet are parallel to X and Y (as in Fig.3 of the A&A
paper "Mapping on the HEALPix grid" by Calabretta and Roukema). Each
facet is then divided up into NxN tiles, where N is 64 for SCUBA-2 and
128 for ACSIS. Each tile is then divided into PxP pixels, where P is
412 for ACSIS, 825 for SCUBA-2 850 um, 1650 for SCUBA-2 450 um. Facets
are numbered from 0 to 11 as defined in the HEALPix paper (Gorsky et.
al. 2005 ApJ 622, 759) (note that the facet six is split equally into
two triangles, one at the bottom left and one at the top right of the
projection plane). Within a facet, tiles are indexed using the
"nested" scheme described in the HEALPix paper. This starts with pixel
zero in the southern corner of the facet. The even bits number the
position in the north-east direction and the odd bits number the
position in the north-west direction. All the tiles in the first facet
come first, followed by all the tiles in the second facet, etc.
This is a fairly complex scheme. To help understanding, the
SMURF:TILEINFO command can create an all-sky map in which each pixel
corresponds to a single tile, and has a pixel value equal to the
corresponding tile index. Displaying this map can help to visualise
the indexing scheme described above.


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKECUBE, MAKEMAP, TILEINFO.


Copyright
~~~~~~~~~
Copyright (C) 2011,2013,2014 Science and Technology Facilities
Council. All Rights Reserved.


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
Foundation, Inc., 59 Temple Place,Suite 330, Boston, MA 02111-1307,
USA


