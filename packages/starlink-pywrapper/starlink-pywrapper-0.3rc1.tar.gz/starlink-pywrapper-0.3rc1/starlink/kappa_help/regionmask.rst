

REGIONMASK
==========


Purpose
~~~~~~~
Applies a mask to a region of an NDF


Description
~~~~~~~~~~~
This routine masks out a region of an NDF by setting pixels to the bad
value, or to a specified constant value. The region to be masked is
specified within a text file (see Parameter REGION) that should
contain a description of the region in the form of an "AST Region".
This is the system used by the AST library for describing regions (see
SUN/211 or SUN/210). Such text files can, for instance, be created
using the Starlink ATOOLS package (a high-level interface to the
facilities of the AST library).


Usage
~~~~~


::

    
       regionmask in region out
       



ADAM parameters
~~~~~~~~~~~~~~~



CONST = LITERAL (Given)
```````````````````````
The constant numerical value to assign to the region, or the string
"Bad". ["Bad"]



IN = NDF (Read)
```````````````
The name of the input NDF.



INSIDE = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, the constant value is assigned to the
inside of the region. Otherwise, it is assigned to the outside. [TRUE]



OUT = NDF (Write)
`````````````````
The name of the output NDF.



REGION = FILENAME (Read)
````````````````````````
The name of the text file containing a text dump of an AST Region. Any
sub-class of Region may be supplied (e.g. Box, Polygon, CmpRegion,
Prism, etc.). If the axes spanned by this Region are not the same as
those of the current WCS Frame in the input NDF, an attempt will be
made to create an equivalent new Region that does match the current
WCS Frame. An error will be reported if this is not possible.



Examples
~~~~~~~~
regionmask a1060 galaxies.txt a1060_sky
This copies input NDF a1060 to the output NDF a1060_sky, setting
pixels bad if they are contained within the Region specified in text
file "galaxies.txt".



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDMASK; ATOOLS: ASTBOX, ASTCMPREGION, ASTELLIPSE, ASTINTERVAL,
ASTPOLYGON.


Copyright
~~~~~~~~~
Copyright (C) 2008, 2009 Science & Technology Facilities Council. All
Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the WCS, AXIS, DATA, QUALITY,
LABEL, TITLE, UNITS, HISTORY, and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




