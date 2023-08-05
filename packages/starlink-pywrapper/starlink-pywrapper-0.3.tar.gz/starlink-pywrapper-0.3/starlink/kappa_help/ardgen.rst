

ARDGEN
======


Purpose
~~~~~~~
Creates a text file describing selected regions of an image


Description
~~~~~~~~~~~
This is an interactive tool for selecting regions of a displayed image
using a cursor, and then storing a description of the selected regions
in a text file in the form of an `ARD Description' (see SUN/183). This
text file may subsequently be used in conjunction with packages such
as CCDPACK or ESP.
The application initially obtains a value for the SHAPE parameter and
then allows you to identify either one or many regions of the
specified shape, dependent on the value of Parameter STARTUP. When the
required regions have been identified, a value is obtained for
Parameter OPTION, and that value determines what happens next. Options
include obtaining further regions, changing the current region shape,
listing the currently defined regions, leaving the application, etc.
Once the selected action has been performed, another value is obtained
for OPTION, and this continues until you choose to leave the
application.
Instructions on the use of the cursor are displayed when the
application is run. The points required to define a region of the
requested shape are described whenever the current region shape is
changed using Parameter SHAPE. Once the points required to define a
region have been given an outline of the entire region is drawn on the
graphics device using the pen specified by Parameter PALNUM.
In the absence of any other information, subsequent application will
use the union (i.e. the logical OR) of all the defined regions.
However, regions can be combined in other ways using the COMBINE
option (see Parameter OPTION). For instance, two regions originally
defined using the cursor could be replaced by their region of
intersection (logical AND), or a single region could be replaced by
its own exterior (logical NOT). Other operators can also be used (see
Parameter OPERATOR).


Usage
~~~~~


::

    
       ardgen ardout shape option [device] [startup]
          { operands=? operator=?
          { regions=?
          option
       



ADAM parameters
~~~~~~~~~~~~~~~



ARDOUT = FILENAME (Write)
`````````````````````````
Name of the text file in which to store the description of the
selected regions.



DEVICE = DEVICE (Read)
``````````````````````
The graphics device on which the regions are to be selected. [Current
graphics device]



OPERANDS() = _INTEGER (Read)
````````````````````````````
A pair of indices for the regions which are to be combined together
using the operator specified by Parameter OPERATOR. If the operator is
"NOT", then only one region index need be supplied. Region indices are
displayed by the "List" option (see Parameter OPTION).



OPERATOR = LITERAL (Read)
`````````````````````````
The operator to use when combining two regions into a single region.
The pixels included in the resulting region depend on which of the
following operators is selected.


+ "AND" -- Pixels are included if they are in both of the regions
specified by Parameter OPERANDS.
+ "EQV" -- Pixels are included if they are in both or neither of the
regions specified by Parameter OPERANDS.
+ "NOT" -- Pixels are included if they are not inside the region
specified by Parameter OPERANDS.
+ "OR" -- Pixels are included if they are in either of the regions
specified by Parameter OPERANDS. Note, an OR operator is implicitly
assumed to exist between each pair of adjacent regions unless some
other operator is specified.
+ "XOR" -- Pixels are included if they are in one, but not both, of
  the regions specified by Parameter OPERANDS.





OPTION= LITERAL (Read)
``````````````````````
A value for this parameter is obtained when you choose to end cursor
input (by pressing the relevant button as described when the
application starts up). It determines what to do next. The following
options are available:


+ "Combine" -- Combine two previously defined regions into a single
region using a Boolean operator, or invert a previously defined region
using a Boolean .NOT. operator. See parameters OPERANDS and OPERATOR.
The original regions are deleted and the new combined (or inverted)
region is added to the end of the list of defined regions.
+ "Delete" -- Delete previously defined regions, see parameter
REGIONS.
+ "Draw" -- Draw the outline of the union of one or more previously
defined regions, see Parameter REGIONS.
+ "Exit" -- Write out the currently defined regions to a text file and
exit the application.
+ "List" -- List the textual descriptions of the currently defined
regions on the screen. Each region is described by an index value, a
"keyword" corresponding to the shape, and various arguments describing
the extent and position of the shape. These arguments are described in
the "Notes" section below.
+ "Multi" -- The cursor is displayed and you can then identify
multiple regions of the current shape, without being re-prompted for
OPTION after each one. These regions are added to the end of the list
of currently defined regions. If the current shape is "Polygon",
"Frame" or "Whole" (see Parameter SHAPE) then multiple regions cannot
be defined and the selected option automatically reverts to "Single".
+ "Single" -- The cursor is displayed and you can then identify single
region of the current shape. You are re-prompted for Parameter OPTION
once you have defined the region. The identified region is added to
the end of the list of currently defined regions.
+ "Shape" -- Change the shape of the regions created by the "Single"
and "Multi" options. This causes a new value for Parameter SHAPE to be
obtained.
+ "Style" -- Change the drawing style by providing a new value for
Parameter STYLE.
+ "Quit" -- Quit the application without saving the currently defined
regions.
+ "Undo" -- Undo the changes made to the list of ARD regions by the
  previous option. Note, the undo list can contain up to 30 entries.
  Entries are only stored for options which actually produce a change in
  the list of regions.





REGIONS() = LITERAL (Read)
``````````````````````````
The list of regions to be deleted or drawn. Regions are numbered
consecutively from 1 and can be listed using the "List" option (see
Parameter OPTION). Single regions or a set of adjacent regions may be
specified, e.g. assigning [4,6-9,12,14-16] will delete regions
4,6,7,8,9,12,14,15,16. (Note that the brackets are required to
distinguish this array of characters from a single string including
commas. The brackets are unnecessary when there is only one item.) The
numbers need not be in ascending order.
If you wish to delete or draw all the regions enter the wildcard *.
5-* will delete or draw from 5 to the last region.



SHAPE = LITERAL (Read)
``````````````````````
The shape of the regions to be defined using the cursor. After
selecting a new shape, you are immediately requested to identify
multiple regions as if "Multi" had been specified for Parameter
OPTION. The currently available shapes are listed below.


+ "Box" -- A rectangular box with sides parallel to the co-ordinate
axes, defined by its centre and one of its corners.
+ "Circle" -- A circle, defined by its centre and radius.
+ "Column" -- A single value on Axis 1, spanning all values on Axis 2.
+ "Ellipse" -- An ellipse, defined by its centre, one end of the major
axis, and one other point which can be anywhere on the ellipse.
+ "Frame" -- The whole image excluding a border of constant width,
defined by a single point on the frame.
+ "Point" -- A single pixel.
+ "Polygon" -- Any general polygonal region, defined by up to 200
vertices.
+ "Rectangle" -- A rectangular box with sides parallel to the co-
ordinate axes, defined by a pair of diagonally opposite corners.
+ "Rotbox" -- A rotated box, defined by both ends of an edge, and one
point on the opposite edge.
+ "Row" -- A single value on Axis 2, spanning all values on Axis 1.
+ "Whole" -- The whole of the displayed image.





STARTUP = LITERAL (Read)
````````````````````````
Determines if the application starts up in "Multi" or "Single" mode
(see Parameter OPTION). ["Multi"]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the regions.
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
The appearance of the lines forming the edges of each region is
controlled by the attributes Colour(Curves), Width(Curves), etc. The
appearance of the vertex markers is controlled by the attributes
Colour(Markers), Size(Markers), etc. [current value]



UNDO = _LOGICAL (Read)
``````````````````````
Used to confirm that it is OK to proceed with an "Undo" option. The
consequences of proceeding are described before the parameter is
obtained.



Examples
~~~~~~~~
ardgen extract.txt circle exit startup=single
This example allows you to create a text file (extract.txt) describing
a single circular region of the image displayed on the current
graphics device. The application immediately exits after the region
has been identified. This example may be useful in scripts or command
procedures since there is no prompting.



Notes
~~~~~


+ An image must previously have been displayed on the graphics device.
+ The arguments for the textual description of each shape are as
follows :
+ "Box" -- The co-ordinates of the centre, followed by the lengths of
the two sides.
+ "Circle" -- The co-ordinates of the centre, followed by the radius.
+ "Column" -- The Axis 1 co-ordinate of the column.
+ "Ellipse" -- The co-ordinates of the centre, followed by the lengths
of the semi-major and semi-minor axes, followed by the angle between
Axis 1 and the semi-major axis (in radians).
+ "Frame" -- The width of the border.
+ "Point" -- The co-ordinates of the pixel.
+ "Polygon" -- The co-ordinates of each vertex in the order given.
+ "Rectangle" -- The co-ordinates of two diagonally opposite corners.
+ "Rotbox" -- The co-ordinates of the box centre, followed by the
lengths of the two sides, followed by the angle between the first side
and Axis 1 (in radians).
+ "Row" -- The Axis 2 co-ordinate of the row.
+ "Whole" -- No arguments.
+ The shapes are defined within the current co-ordinate Frame of the
  displayed NDF. For instance, if the current co-ordinate Frame of the
  displayed NDF is RA/DEC, then "COLUMN" regions will be curves of
  constant DEC, "ROW" regions will be curves of constant RA (assuming
  Axis 1 is RA and Axis 2 is DEC), straight lines will correspond to
  geodesics, etc. Numerical values will be stored in the output text
  file in the current coordinate Frame of the NDF. WCS information will
  also be stored in the output text file allowing the stored positions
  to be converted to other systems (pixel co-ordinates, for instance).




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDPLOT, ARDMASK; CCDPACK; ESP.


Copyright
~~~~~~~~~
Copyright (C) 1994 Science & Engineering Research Council. Copyright
(C) 1995, 1999, 2001 Central Laboratory of the Research Councils.
Copyright (C) 2010 Science & Technology Facilities Council. All Rights
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


