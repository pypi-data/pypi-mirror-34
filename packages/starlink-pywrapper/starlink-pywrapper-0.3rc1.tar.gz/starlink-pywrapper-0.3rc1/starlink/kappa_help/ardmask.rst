

ARDMASK
=======


Purpose
~~~~~~~
Uses an ARD file to set some pixels of an NDF to be bad


Description
~~~~~~~~~~~
This task allows regions of an NDF's to be masked, so that they can
(for instance) be excluded from subsequent data processing. ARD (ASCII
Region Definition) descriptions stored in a text file define which
pixels of the data array are masked. An output NDF is created which is
the same as the input file except that all pixels specified by the ARD
file have been assigned either the bad value or a specified constant
value. This value can be assigned to either the inside or the outside
of the specified ARD region.
If positions in the ARD description are given using a co-ordinate
system that has one fewer axes than the input NDF, then each plane in
the NDF will be masked independently using the supplied ARD
description. For instance, if a 2-D ARD description that uses (RA,Dec)
to specify positions is used to mask a 3-D (ra,dec,velocity) NDF, then
each velocity plane in the NDF will be masked independently.


Usage
~~~~~


::

    
       ardmask in ardfile out
       



ADAM parameters
~~~~~~~~~~~~~~~



ARDFILE = FILENAME (Read)
`````````````````````````
The name of the ARD file containing a description of the parts of the
image to be masked out, i.e. set to bad. The co-ordinate system in
which positions within this file are given should be indicated by
including suitable COFRAME or WCS statements within the file (see
SUN/183), but will default to pixel or current WCS Frame co-ordinates
in the absence of any such statements (see parameter DEFPIX). For
instance, starting the file with a line containing the text
"COFRAME(SKY,System=FK5)" would indicate that positions are specified
in RA/DEC (FK5,J2000). The statement "COFRAME(PIXEL)" indicates
explicitly that positions are specified in pixel co-ordinates.



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be masked. It may be "Data", or "Variance",
or "Error", or "All" (where "Error" is equivalent to "Variance").
["All"]



CONST = LITERAL (Given)
```````````````````````
The constant numerical value to assign to the region, or the string
"bad". ["bad"]



DEFPIX = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied for DEFPIX, then co-ordinates in the
supplied ARD file will be assumed to be pixel coordinates. Otherwise,
they are assumed to be in the current WCS co-ordinate system of the
supplied NDF. [TRUE]



IN = NDF (Read)
```````````````
The name of the source NDF.



INSIDE = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, the constant value is assigned to the
inside of the region specified by the ARD file. Otherwise, it is
assigned to the outside. [TRUE]



OUT = NDF (Write)
`````````````````
The name of the masked NDF.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



Examples
~~~~~~~~
ardmask a1060 galaxies.ard a1060_sky title="A1060 galaxies masked"
This flags pixels defined by the ARD file galaxies.ard within the NDF
called a1060 to create a new NDF called a1060_sky. a1060_sky has a
title="A1060 galaxies masked". This might be to flag the pixels where
bright galaxies are located to exclude them from sky-background
fitting.
ardmask in=ic3374 ardfil=ardfile.txt out=ic3374a
This example uses as the source image the NDF called ic3374 and sets
the pixels specified by the ARD description contained in ardfile.txt
to the bad value. The resultant image is output to the NDF called
ic3374a. The title is unchanged.



ASCII-region-definition Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ARD file may be created by ARDGEN or written manually. In the
latter case consult SUN/183 for full details of the ARD descriptors
and syntax; however, much may be learnt from looking at the ARD files
created by ARDGEN and the ARDGEN documentation. There is also a
summary with examples in the main body of SUN/95.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDGEN, ARDPLOT, LOOK.


Copyright
~~~~~~~~~
Copyright (C) 1994 Science & Engineering Research Council. Copyright
(C) 1995-1998, 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2007, 2012 Science & Technology Facilities Council. All
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




