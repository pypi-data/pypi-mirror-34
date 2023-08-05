

ARDPLOT
=======


Purpose
~~~~~~~
Plot regions described in an ARD file


Description
~~~~~~~~~~~
This application draws the outlines of regions described in a supplied
two-dimensional ARD file (an `ARD Description'--see SUN/183). If there
is an existing picture on the graphics device, the outlines are drawn
over the top of the previously displayed picture, aligned (if
possible) in the current co-ordinate Frame of the previously drawn
picture. If the graphics device is empty (or if the CLEAR parameter is
set TRUE) the outlines are drawn using a default projection - the size
of the area plotted can be controlled by the SIZE parameter. Note, the
facility to plot on an empty device is currently only available for
two-dimensional regions specified using parameter REGION.


Usage
~~~~~


::

    
       ardplot ardfile [device] [regval]
       



ADAM parameters
~~~~~~~~~~~~~~~



ARDFILE = FILENAME (Read)
`````````````````````````
The name of a file containing an `ARD Description' of the regions to
be outlined. The co-ordinate system in which positions within this
file are given should be indicated by including suitable COFRAME or
WCS statements within the file (see SUN/183), but will default to
pixel co-ordinates in the absence of any such statements. For
instance, starting the file with a line containing the text
"COFRAME(SKY,System=FK5)" would indicate that positions are specified
in RA/DEC (FK5,J2000). The statement "COFRAME(PIXEL)" indicates
explicitly that positions are specified in pixel co-ordinates. The
ARDFILE parameter is only accessed if Parameter REGION is given a null
(!) value.



CLEAR = _LOGICAL (Read)
```````````````````````
TRUE if the current picture is to be cleared before the Region is
display. [FALSE]



DEVICE = DEVICE (Read)
``````````````````````
The plotting device. [Current graphics device]



REGION = FILENAME (Read)
````````````````````````
The name of a file containing an AST Region to be outlined, or null
(!) if the ARD region defined by Parameter ARDFILE is to be outlined.
Suitable files can be created using the ATOOLS package. [!]



REGVAL = _INTEGER (Read)
````````````````````````
Indicates which regions within the ARD description are to be outlined.
If zero (the default) is supplied, then the plotted boundary encloses
all the regions within the ARD file. If a positive value is supplied,
then only the region with the specified index is outlined (the first
region in the ARD file has index 2, for historical reasons). If a
negative value is supplied, then all regions with indices greater than
or equal to the absolute value of the supplied index are outlined. See
SUN/183 for further information on the numbering of regions within an
ARD description. The REGVAL parameter is only accessed if Parameter
REGION is given a null (!) value. [0]



SIZE = _REAL (Read)
```````````````````
The size of the plot to create, given as a multiple of the size of the
Region being plotted. This parameter is only accessed if no DATA
picture can be found on the graphics device, or CLEAR is TRUE. A SIZE
value of 1.0 causes the plot to be the same size as the Region being
plotted. A value of 2.0 causes the plot to be twice the size of the
Region, etc. [2.0]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the curves.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings overriding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a plotting attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!)---the initial default---is supplied. To apply changes of
style to only the current invocation, begin these attributes with a
plus sign. A mixture of persistent and temporary style changes is
achieved by listing all the persistent attributes followed by a plus
sign then the list of temporary attributes.
See section "Plotting Attributes" in SUN/95 for a description of the
available attributes. Any unrecognised attributes are ignored (no
error is reported).
The appearance of the plotted curves is controlled by the attributes
Colour(Curves), Width(Curves), etc. [current value]



Examples
~~~~~~~~
ardplot bulge
Draws an outline around all the regions included in the ardfile named
"bulge". The outline is drawn on the current graphics device and is
drawn in alignment with the previous picture.



Notes
~~~~~


+ A DATA picture must already exist on the selected graphics device
before running this command. An error will be reported if no DATA
picture can be found.
+ The application stores a new DATA picture in the graphics database.
  On exit the current database picture for the chosen device reverts to
  the input picture.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDGEN, ARDMASK, LOOK.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2005 Particle Physics & Astronomy Research Council.
Copyright (C) 2007, 2010, 2014 Science & Technology Facilities
Council. All Rights Reserved.


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


