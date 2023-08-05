

JSAJOIN
=======


Purpose
~~~~~~~
Create a single tangent-plane NDF from a set of JSA tiles


Description
~~~~~~~~~~~
This script pastes together one or more JSA tiles and then resamples
the resulting montage onto a tangent-plane projection with square
pixels and celestial north upwards. It can also restrict the output
NDF to a specified sub-section of this montage.
By default, the output NDF contains all the data from all the tiles
specified by parameter TILES. Alternatively, an existing NDF can be
specified for parameter REGION, in which case the output NDF will
contain only the data that falls within the supplied NDF. Another way
to specify the bounds of the output NDF is to give the centre and
radius of a circle on the sky using parameters CENTRE1, CENTRE2,
RADIUS and SYSTEM.
The pixel size of the output may be specified by parameter PIXSIZE,
but defaults to the nominal pixel size of the JSA tiles.


Usage
~~~~~


::

    
       jsajoin tiles out [centre1] [centre2] [radius] [system] [region]
               [pixsize] [retain]
       



ADAM parameters
~~~~~~~~~~~~~~~



CENTRE1 = LITERAL (Read)
````````````````````````
The formatted RA or Galactic longitude at the centre of a circle that
defines the required extent of the output NDF. See also CENTRE2 and
RADIUS. The coordinate system is specified by parameter SYSTEM. It is
only accessed if a null (!) value is supplied for parameter REGION. If
a null value is supplied for both CENTRE1 and REGION, the output NDF
will encompass all the data specified by parameter TILES. [!]



CENTRE2 = LITERAL (Read)
````````````````````````
The formatted Dec or Galactic latitude at the centre of a circle that
defines the required extent of the output NDF. See also CENTRE1 and
RADIUS. The coordinate system is specified by parameter SYSTEM. It is
only accessed if a null (!) value is supplied for parameter REGION and
a non-null value is supplied for parameter CENTRE1.



INSTRUMENT = LITERAL (Read)
```````````````````````````
Selects the tiling scheme to be used. The following instrument names
are recognised (unambiguous abbreviations may be supplied):
"SCUBA-2(450)", "SCUBA-2(850)", "ACSIS", "DAS". If the first input NDF
contains JCMT data, the default value for this parameter is determined
from the FITS headers in the input NDF. Otherwise, there is no default
and an explicit value must be supplied. []



OUT = NDF (Read)
````````````````
The output NDF.



PIXSIZE = _REAL (Read)
``````````````````````
The pixel size to use for the output NDF, in arc-seconds. Not used if
an NDF is supplied for parameter REGION. If a null (!) value is
supplied, a default pixel size is used equal to the geometric mean of
the pixel dimensions in the middle tile specified by parameter TILES.
[!]



RADIUS = _DOUBLE (Read)
```````````````````````
The radius of the circle that defines the required extent of the
output NDF, in arc-minutes. See also CENTRE1 and CENTRE2. It is only
accessed if a null (!) value is supplied for parameter REGION and a
non-null value is supplied for parameter CENTRE1.



REGION = LITERAL (Read)
```````````````````````
Specifies the required extent of the output NDF. It can be either a
text file holding an AST Region description, or an NDF. If it is an
NDF, it also defines the WCS and pixel grid of the output NDF. If a
null (!) value is supplied, the region is specified using parameter
CENTRE1, CENTRE2 and RADIUS. [!]



RETAIN = _LOGICAL (Read)
````````````````````````
Should the temporary directory containing the intermediate files
created by this script be retained? If not, it will be deleted before
the script exits. If retained, a message will be displayed at the end
specifying the path to the directory. [FALSE]



SYSTEM = LITERAL (Read)
```````````````````````
The celestial coordinate system used by the CENTRE1 and CENTRE2
parameters. It can be either "ICRS" or "Galactic". The output NDF
inherits this same system as its current WCS Frame. ["ICRS"]



TILES = NDF (Read)
``````````````````
A group of NDFs each of which corresponds to a JSA tile. They should
all relate to a single instrument.



Copyright
~~~~~~~~~
Copyright (C) 2013 Science & Technology Facilities Council. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


