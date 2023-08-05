

LUTVIEW
=======


Purpose
~~~~~~~
Draws a colour-table key


Description
~~~~~~~~~~~
This application displays a key to the current colour table on the
specified image display device using the whole of the current colour
table (excluding the low 16 pens which are reserved for axis
annotation, etc.). The key can either be a simple rectangular block of
colour which ramps through the colour table, a histogram-style key in
which the width of the block reflects the number of pixels allocated
to each colour index, or a set of RGB intensity curves. The choice is
made using the STYLE parameter.
By default, numerical data values are displayed along the long edge of
the key. The values corresponding to the maximum and minimum colour
index are supplied using Parameters HIGH and LOW. Intermediate colour
indices are labelled with values which are linearly interpolated
between these two extreme values.
The rectangular area in which the key (plus annotations) is drawn may
be specified either using a graphics cursor, or by specifying the co-
ordinates of two corners using Parameters LBOUND and UBOUND.
Additionally, there is an option to make the key fill the current
picture. See Parameter MODE. The key may be constrained to the current
picture using Parameter CURPIC.
The appearance of the annotation my be controlled in detail using the
STYLE parameter.


Usage
~~~~~


::

    
       lutview [mode] [low] [high] [curpic] [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The component (within the NDF given by Parameter NDF) which is
currently displayed. It may be "Data", "Quality", "Variance", or
"Error" (where "Error" is an alternative to "Variance" and causes the
square root of the variance values to be used). If "Quality" is
specified, then the quality values are treated as numerical values (in
the range 0 to 255). The dynamic default is obtained from global
Parameter COMP which is set by applications such as KAPPA:DISPLAY. []



CURPIC = _LOGICAL (Read)
````````````````````````
If CURPIC is TRUE, the colour table key is to lie within the current
picture, otherwise the new picture can lie anywhere within the BASE
picture. This parameter ignored if the current-picture mode is
selected. [FALSE]



DEVICE = DEVICE (Read)
``````````````````````
The image-display device on which the colour table is to be drawn. The
device must be in one of the following GNS categories: IMAGE_DISPLAY,
IMAGE_OVERLAY, MATRIX_PRINTER, or WINDOW, and have at least 24
greyscale intensities or colour indices. It must also not reset when
the device is opened (since the colour table would be lost) unless
Parameter LUT does not have the null value. [Current image-display
device]



FRAME = LITERAL (Read)
``````````````````````
Specifies the co-ordinate Frame of the positions supplied using
Parameters LBOUND and UBOUND. The following Frames will always be
available.


+ "GRAPHICS" -- gives positions in millimetres from the bottom-left
corner of the plotting surface.
+ "BASEPIC" -- gives positions in a normalised system in which the
bottom-left corner of the plotting surface is (0,0) and the shortest
dimension of the plotting surface has length 1.0. The scales on the
two axes are equal.
+ "CURPIC" -- gives positions in a normalised system in which the
bottom-left corner of the current picture is (0,0) and the shortest
dimension of the current picture has length 1.0. The scales on the two
axes are equal.
+ "NDC" -- gives positions in a normalised system in which the bottom-
left corner of the plotting surface is (0,0) and the top-right corner
is (1,1).
+ "CURNDC" -- gives positions in a normalised system in which the
  bottom-left corner of the current picture is (0,0) and the top-right
  corner is (1,1).

There may be additional Frames available, describing previously
displayed data. If a null value is supplied, the current Frame
associated with the displayed data (if any) is used. This parameter is
only accessed if Parameter MODE is set to "XY". ["BASEPIC"]



HIGH = _REAL (Read)
```````````````````
The value corresponding to the maximum colour index. It is used to
calculate the annotation scale for the key. If it is null (!) the
maximum colour index is used, and histogram style keys are not
available. [Current display linear-scaling maximum]



LBOUND = LITERAL (Read)
```````````````````````
Co-ordinates of the lower-left corner of the rectangular region
containing the colour ramp and annotation, in the co-ordinate Frame
specified by Parameter FRAME (supplying a colon ":" will display
details of the selected co-ordinate Frame). The position should be
supplied as a list of formatted axis values separated by spaces or
commas. A null (!) value causes the lower-left corner of the BASE or
(if CURPIC is TRUE) current picture to be used.



LOW = _REAL (Read)
``````````````````
The value corresponding to the minimum colour index. It is used to
calculate the annotation scale for the key. If it is null (!) the
minimum colour index is used, and histogram style keys are not
available. [Current display linear-scaling minimum]



LUT = NDF (Read)
````````````````
Name of the NDF containing a lookup table as its data array; the
lookup table is written to the image-display's colour table. The
purpose of this parameter is to provide a means of controlling the
appearance of the image on certain devices, such as colour printers,
that do not have a dynamic colour table, i.e. the colour table is
reset when the device is opened. If used with dynamic devices, such as
windows or Ikons, the new colour table remains after this application
has completed. A null, !, means that the existing colour table will be
used.
The LUT must be two-dimensional, the first dimension being 3, and the
second being arbitrary. The method used to compress or expand the
colour table if the second dimension is different from the number of
unreserved colour indices is controlled by Parameter NN. Also the
LUT's values must lie in the range 0.0--1.0. [!]



MODE = LITERAL (Read)
`````````````````````
Method for defining the position, size and shape of the rectangular
region containing the colour ramp and annotation. The options are:


+ "Cursor" -- The graphics cursor is used to supply two diametrically
opposite corners or the region.
+ "XY" -- The Parameters LBOUND and UBOUND are used to get the limits.
+ "Picture" -- The whole of the current picture is used. Additional
  positioning options are available by using other KAPPA applications to
  create new pictures and then specifying the picture mode.

["Cursor"]



NDF = NDF (Read)
````````````````
The NDF defining the image values to be used if a histogram-style key
is requested. This should normally be the NDF currently displayed in
the most recently created DATA picture. If a value is supplied on the
command line for this parameter it will be used. Otherwise, the NDF to
used is found by interrogating the graphics database (which contains
references to displayed images). If no reference NDF can be obtained
from the graphics database, the user will be prompted for a value.



NN = _LOGICAL (Read)
````````````````````
If NN is TRUE, the input lookup table is mapped to the colour table by
using the nearest-neighbour method. This preserves sharp edges and is
better for lookup tables with blocks of colour. If NN is FALSE, linear
interpolation is used, and this is suitable for smoothly varying
colour tables. NN is ignored unless LUT is not null. [FALSE]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the annotation.
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
Axis 1 is always the "data value" axis, whether it is displayed
horizontally or vertically. So for instance, to set the label for the
data value axis, assign a value to "Label(1)" in the supplied style.
To get a ramp key (the default), specify "form=ramp". To get a
histogram key (a coloured histogram of pen indices), specify
"form=histogram". To get a graph key (three curves of RGB
intensities), specify "form=graph". If a histogram key is produced,
the population axis can be either logarithmic or linear. To get a
logarithmic population axis, specify "logpop=1". To get a linear
population axis, specify "logpop=0" (the default). To annotate the
long axis with pen numbers instead of pixel value, specify "pennums=1"
(the default, "pennums=0", shows pixel values). [current value]



UBOUND = LITERAL (Read)
```````````````````````
Co-ordinates of the upper-right corner of the rectangular region
containing the colour ramp and annotation, in the co-ordinate Frame
specified by Parameter FRAME (supplying a colon ":" will display
details of the selected co-ordinate Frame). The position should be
supplied as a list of formatted axis values separated by spaces or
commas. A null (!) value causes the lower-left corner of the BASE or
(if CURPIC is TRUE) the current picture to be used.



Examples
~~~~~~~~
lutview
Draws an annotated colour table at a position selected via the cursor
on the current image-display device.
lutview style="form=hist,logpop=1"
As above, but the key has the form of a coloured histogram of the pen
numbers in the most recently displayed image. The second axis displays
the logarithm (base 10) of the bin population.
lutview style="form=graph,pennums=1"
The key is drawn as a set of three (or one if a monochrome colour
table is in use) curves indicating the red, green and blue intensity
for each pen. The first axis is annotated with pen numbers instead of
data values.
lutview style="edge(1)=right,label(1)=Data value in m31"
As above, but the data values are labelled on the right edge of the
box, and the values are labelled with the string "Data value in m31".
lutview style="textlab(1)=0,width(border)=3,colour(border)=white"
No textual label is drawn for the data values, and a thicker than
usual white box is drawn around the colour ramp.
lutview style="textlab(1)=0,numlab(1)=0,majticklen(1)=0"
Only the border is drawn around the colour ramp.
lutview style="textlab(1)=0,numlab(1)=0,majticklen(1)=0,border=0"
No annotation at all is drawn.
lutview p
Draws a colour table that fills the current picture on the current
image-display device.
lutview curpic
Draws a colour table within the current picture positioned via the
cursor.
lutview xy lut=my_lut device=ps_p lbound="0.92,0.2" ubound="0.98,0.8"
Draws the colour table in the NDF called my_lut with an outline within
the BASE picture on the device ps_p, defined by the x-y bounds
(0.92,0.2) and (0.98,0.8). In other words the plot is to the right-
hand side with increasing colour index with increasing y position.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: DISPLAY, LUTABLE; Figaro: COLOUR.


Copyright
~~~~~~~~~
Copyright (C) 1999-2002, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2010 Science & Technology Facilities Council.
All Rights Reserved.


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


