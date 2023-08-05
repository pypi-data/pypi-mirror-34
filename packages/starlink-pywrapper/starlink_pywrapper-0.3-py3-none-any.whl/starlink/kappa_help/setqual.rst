

SETQUAL
=======


Purpose
~~~~~~~
Assign a specified quality to selected pixels within an NDF


Description
~~~~~~~~~~~
This routine assigns (or optionally removes) the quality specified by
Parameter QNAME to (or from) selected pixels in an NDF. For more
information about using quality within KAPPA see the appendix "Using
Quality Names" within SUN/95.
The user can select the pixels to be operated on in one of three ways
(see Parameter SELECT).


+ By giving a `mask' NDF. Pixels with bad values in the mask NDF will
be selected from the corresponding input NDF.
+ By giving a list of pixel indices for the pixels which are to be
selected.
+ By giving an ARD file containing a description of the regions of the
  NDF which are to be selected. The ARD system (see SUN/183) uses a
  textual language to describe geometric regions of an array. Text files
  containing ARD description suitable for use with this routine can be
  created interactively using the routine ARDGEN.

The operation to be performed on the pixels is specified by Parameter
FUNCTION. The given quality may be assigned to or removed from pixels
within the NDF. The pixels operated on can either be those selected by
the user (as described above), or those not selected. The quality of
all other pixels is left unchanged (unless the Parameter FUNCTION is
given the value NS+HU or NU+HS). Thus for instance if pixel (1,1)
already held the quality specified by QNAME, and the quality was then
assigned to pixel (2,2) this would not cause the quality to be removed
from pixel (1,1).
This routine can also be used to copy all quality information from one
NDF to another (see Parameter LIKE).


Usage
~~~~~


::

    
       setqual ndf qname comment mask
       



ADAM parameters
~~~~~~~~~~~~~~~



ARDFILE = FILENAME (Read)
`````````````````````````
The name of the ARD file containing a description of the parts of the
NDF to be `selected'. The ARD parameter is only prompted for if the
SELECT parameter is given the value "ARD". The co-ordinate system in
which positions within this file are given should be indicated by
including suitable COFRAME or WCS statements within the file (see
SUN/183), but will default to pixel co-ordinates in the absence of any
such statements. For instance, starting the file with a line
containing the text "COFRAME(SKY,System=FK5)" would indicate that
positions are specified in RA/DEC (FK5,J2000). The statement
"COFRAME(PIXEL)" indicates explicitly that positions are specified in
pixel co-ordinates.



COMMENT = LITERAL (Read)
````````````````````````
A comment to store with the quality name. This parameter is only
prompted for if the NDF does not already contain a definition of the
quality name.



FUNCTION = LITERAL (Read)
`````````````````````````
This parameter specifies what function is to be performed on the
"selected" pixels specified using Parameters MASK, LIST or ARD. It can
take any of the following values.


+ "HS" -- Ensure that the quality specified by QNAME is held by all
the selected pixels. The quality of all other pixels is left
unchanged.
+ "HU" -- Ensure that the quality specified by QNAME is held by all
the pixels that have not been selected. The quality of the selected
pixels is left unchanged.
+ "NS" -- Ensure that the quality specified by QNAME is not held by
any of the selected pixels. The quality of all other pixels is left
unchanged.
+ "NU" -- Ensure that the quality specified by QNAME is not held by
any of the pixels that have not been selected. The quality of the
selected pixels is left unchanged.
+ "HS+NU" -- Ensure that the quality specified by QNAME is held by all
the selected pixels and not held by any of the other pixels.
+ "HU+NS" -- Ensure that the quality specified by QNAME is held by all
  the pixels that have not been selected and not held by any of the
  selected pixels. ["HS"]





LIKE = NDF (Read)
`````````````````
An existing NDF from which the QUALITY component and quality names are
to be copied. These overwrite any corresponding information in the NDF
given by Parameter NDF. If null (!), then the operation of this
command is instead determined by Parameter SELECT. [!]



LIST = LITERAL (Read)
`````````````````````
A group of pixels positions within the input NDF listing the pixels
that are to be `selected' (see Parameter FUNCTION). Each position
should be giving as a list of pixel indices (eg X1, Y1, X2, Y2,... for
a two dimensional NDF). LIST is only prompted for if Parameter SELECT
is given the value LIST.



MASK = NDF (Read)
`````````````````
A mask NDF used to define the `selected' pixels within the input NDF
(see Parameter FUNCTION). The mask should be aligned pixel-for-pixel
with the input NDF. Pixels that are bad in the mask NDF are
`selected'. The quality of any pixels that lie outside the bounds of
the mask NDF are left unaltered. This parameter is only prompted for
if the Parameter SELECT is given the value MASK.



NDF = NDF (Update)
``````````````````
The NDF in which the quality information is to be stored.



QNAME = LITERAL (Read)
``````````````````````
The quality name. If the supplied name is not already defined within
the input NDF, then a definition of the name is added to the NDF. The
user is warned if the quality name is already defined within the NDF.



READONLY = _LOGICAL (Read)
``````````````````````````
If TRUE, then an error will be reported if any attempt is subsequently
made to remove the quality name (e.g. using REMQUAL). [FALSE]



SELECT = LITERAL (Read)
```````````````````````
If Parameter LIKE is null, then this parameter determines how the
pixels are selected, and can take the values "Mask", "List" or "ARD"
(see Parameters MASK, LIST, and ARD). ["Mask"]



QVALUE = _INTEGER (Read)
````````````````````````
If not null, then the whole Quality array is filled with the constant
value given by QVALUE, which must be in the range 0 to 255. No other
changes are made to the NDF. [!]



XNAME = LITERAL (Read)
``````````````````````
If an NDF already contains any quality name definitions then new
quality names are put in the same extension as the old names. If no
previous quality names have been stored in the NDF then Parameter
XNAME will be used to obtain the name of an NDF extension in which to
store the new quality name. The extension will be created if it does
not already exist (see Parameter XTYPE). [QUALITY_NAMES]



XTYPE = LITERAL (Read)
``````````````````````
If a new NDF extension is created to hold quality names (see Parameter
XNAME), then Parameter XTYPE is used to obtain the HDS data type for
the created extension. The run time default is to give the extension a
type identical to its name. []



Examples
~~~~~~~~
setqual m51 saturated "Saturated pixels" m51_cut
This example ensures that the quality "SATURATED" is defined within
the NDF "M51". The comment "Saturated pixels" is stored with the
quality name if it did not already exist in the NDF. The quality
SATURATED is then assigned to all pixels for which the corresponding
pixel in NDF M51_CUT is bad. The quality of all other pixels is left
unchanged.
setqual "m51,cena" source_a select=list list=^source_a.lis
function=hs+nu
This example ensures that pixels within the two NDFs m51 and cena
which are included in the list of pixel indices held in text file
source_a.lis, have the quality "SOURCE_A", and also ensures that none
of the pixels which were not included in source_a.lis have the
quality.
setqual m51 source_b select=ard ard=background.ard
This example assigns the quality "source_b" to pixels of the NDF "m51"
as described by an ARD description stored in the text file
"background.ard". This text file could for instance have been created
using routine ARDGEN.



Notes
~~~~~


+ All the quality names which are currently defined within an NDF can
  be listed by application SHOWQUAL. Quality name definitions can be
  removed from an NDF using application REMQUAL. If there is no room for
  any more quality names to be added to the NDF then REMQUAL can be used
  to remove a quality name in order to make room for the new quality
  names.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: QUALTOBAD, REMQUAL, SHOWQUAL.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1994 Science & Engineering Research Council.
Copyright (C) 2002, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2008,2013 Science & Technology Facilities Council. All
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


