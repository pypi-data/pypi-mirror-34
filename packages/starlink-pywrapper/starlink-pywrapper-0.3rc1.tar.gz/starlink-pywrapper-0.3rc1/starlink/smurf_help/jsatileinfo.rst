

JSATILEINFO
===========


Purpose
~~~~~~~
Return information about a specified sky tile


Description
~~~~~~~~~~~
This routine returns information about a single standard sky tile for
a named JCMT instrument (specified by parameter ITILE). This includes
the RA and Dec. of the tile centre, the tile size, the tile WCS, and
whether the NDF containing the accumulated co-added data for the tile
currently exists. If not, there is an option to create it and fill it
with zeros (see parameter CREATE). In addition, an NDF can be created
containing the tile index at every point on the whole sky (see
parameter ALLSKY).
Also, the bounds of the overlap in pixel indices between the tile and
a specified NDF or Region can be found (see parameter TARGET).
The environment variable JSA_TILE_DIR should be defined prior to using
this command, and should hold the path to the directory in which the
NDFs containing the accumulated co-added data for each tile are
stored. Tiles for a specified instrument will be stored within a sub-
directory of this directory (see parameter INSTRUMENT). If
JSA_TILE_DIR is undefined, the current directory is used.


ADAM parameters
~~~~~~~~~~~~~~~



ALLSKY = NDF (Write)
````````````````````
If not null (!), this is the name of a new 2D NDF to create holding
the tile index at every point on the sky. The pixel size in this image
is much larger than in an individual tile in order to keep the NDF
size managable. Each pixel holds the integer index of a tile. Pixels
that have no corresponding tile hold a bad value. [!]



CREATE = _LOGICAL (Read)
````````````````````````
Indicates if the NDF containing co-added data for the tile should be
created if it does not already exist. If TRUE, and if the tile's NDF
does not exist on entry to this command, a new NDF will be created for
the tile and filled with zeros. The instrument subdirectory within the
JSA_TILE_DIR directory will be created if it does not already exist.
[FALSE]



DECCEN = _DOUBLE (Write)
````````````````````````
An output parameter to which is written the ICRS Declination of the
tile centre, in radians.



EXISTS = _LOGICAL (Write)
`````````````````````````
An output parameter that is set TRUE if the NDF containing co-added
data for the tile existed on entry to this command (FALSE otherwise).



HEADER = LITERAL (Read)
```````````````````````
The name of a new text file in which to store the WCS and extent of
the tile in the form of a set of FITS-WCS headers. [!]



INSTRUMENT = LITERAL (Read)
```````````````````````````
The JCMT instrument (different instruments have different tiling
schemes and pixel sizes). The following instrument names are
recognised (unambiguous abbreviations may be supplied):
"SCUBA-2(450)", "SCUBA-2(850)", "ACSIS", "DAS". NDFs containing co-
added data for the selected instrument reside within a corresponding
sub-directory of the directory specified by environment variable
JSA_TILE_DIR. These sub-directories are called "scuba2-450",
"scuba2-850", "acsis" and "das".



ITILE = _INTEGER (Read)
```````````````````````
The index of the tile about which information is required. The first
tile has index 0. The largest allowed tile index is always returned in
output parameter MAXTILE. If a null (!) value is supplied for ITILE,
the MAXTILE parameter is still written, but the command will then exit
immediately without further action (and without error).



LBND( 2 ) = _INTEGER (Write)
````````````````````````````
An output parameter to which are written the lower pixel bounds of the
NDF containing the co-added data for the tile.



LOCAL = _LOGICAL (Read)
```````````````````````
If TRUE, the FITS reference point is put at the centre of the tile.
Otherwise, it is put at RA=0 Dec=0. [FALSE]



MAXTILE = _INTEGER (Write)
``````````````````````````
An output parameter to which is written the largest tile index
associated with the instrument specified by parameter INSTRUMENT.



PROJ = LITERAL (Read)
`````````````````````
Determines the JSA projection to use. The allowed values are "HPX"
(HPX projection centred on RA=0h), "HPX12" (HPX projection centred on
RA=12h), "XPHN" (XPH projection centred on the north pole) and "XPHS"
(XPH projection centred on the south pole). A null (!) value causes
"HPX" to be used. ["HPX"]



RACEN = LITERAL (Write)
```````````````````````
An output parameter to which is written the ICRS Right Ascension of
the tile centre, in radians.



REGION = LITERAL (Read)
```````````````````````
The name of a new text file in which to store the WCS and extent of
the tile in the form of an AST Region. [!]



SIZE = _DOUBLE (Write)
``````````````````````
An output parameter to which is written the arc-length of each side of
a square bounding box for the tile, in radians.



TARGET = LITERAL (Read)
```````````````````````
Defines the region of interest. The pixel index bounds of the area of
the specified tile that overlaps this region are found and reported
(see parameter TLBND and TUBND). The value supplied for TARGET can be
either the name of a text file containing an AST Region, or the path
for an NDF, in which case a Region is created that covers the region
of sky that maps onto the rectangular pixel grid of the NDF. [!]



TILENDF = LITERAL (Write)
`````````````````````````
An output parameter to which is written the full path to the NDF
containing co-added data for the tile. Note, it is not guaranteed that
this NDF exists on exit from this command (see parameters EXISTS and
CREATE).



TLBND( 2 ) = _INTEGER (Write)
`````````````````````````````
An output parameter to which are written the lower pixel bounds of the
area of the tile NDF that overlaps the region specified by parameter
TARGET. If there is no overlap, the TLBND values are returned greater
than the TUBND values.



TUBND( 2 ) = _INTEGER (Write)
`````````````````````````````
An output parameter to which are written the upper pixel bounds of the
area of the tile NDF that overlaps the region specified by parameter
TARGET. If there is no overlap, the TLBND values are returned greater
than the TUBND values.



UBND( 2 ) = _INTEGER (Write)
````````````````````````````
An output parameter to which are written the upper pixel bounds of the
NDF containing the co-added data for the tile.



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKECUBE, MAKEMAP, TILELIST.


Copyright
~~~~~~~~~
Copyright (C) 2011-2014 Science and Technology Facilities Council. All
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
Foundation, Inc., 59 Temple Place,Suite 330, Boston, MA 02111-1307,
USA


