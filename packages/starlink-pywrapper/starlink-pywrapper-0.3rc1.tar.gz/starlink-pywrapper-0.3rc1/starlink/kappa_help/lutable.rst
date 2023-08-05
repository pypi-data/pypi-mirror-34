

LUTABLE
=======


Purpose
~~~~~~~
Manipulates an image-display colour table


Description
~~~~~~~~~~~
This application allows manipulation of the colour table of an image-
display device provided some data are, according to the graphics
database, already displayed upon the device. A 2-dimensional data
array, stored in the input NDF structure, may be nominated to assist
in defining the colour table via an histogram equalisation. There are
two stages to the running of this application.
1. The way in which the lookup table (LUT) is to distributed amongst
the pens (colour indices) of the colour table is required. Some pens
are reserved by KAPPA as a palette, particularly for annotation. This
application only modifies the unreserved portion of the colour table.
2. The lookup table is now chosen from a programmed selection or read
from an NDF.
The two stages may be repeated cyclically if desired. To exit the loop
give the null response, !, to a prompt. Looping will not occur if the
lookup table and the distribution method are supplied on the command
line.


Usage
~~~~~


::

    
       lutable mapping coltab lut [device] ndf percentiles shade
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
Name of the image display to be used. [Current image-display device]



COLTAB = LITERAL (Read)
```````````````````````
The lookup table required. The options are listed below. "Negative" -
This is negative grey scale with black assigned to the highest pen,
and white assigned to the lowest available pen. "Colour" - This
consists of eighteen standard colour blocks. "Grey" - This a standard
grey scale. "External" - Obtain a lookup table stored in an NDF's data
array. If the table cannot be found in the specified NDF or if it is
not a LUT then a grey scale is used.



FULL = _LOGICAL (Read)
``````````````````````
If TRUE the whole colour-table for the device is stored including the
reserved pens. This is necessary to save a colour table written by
another package that does not reserve colour indices. For colour
tables produced by KAPPA this should be FALSE. [FALSE]



LUT = NDF (Read)
````````````````
Name of the NDF containing the lookup table as its data array. The LUT
must be 2-dimensional, the first dimension being 3, and the second
being arbitrary. The method used to compress or expand the colour
table if the second dimension is different from the number of
unreserved colour indices is controlled by parameter NN. Also the
LUT's values must lie in the range 0.0--1.0.



MAPPING = LITERAL (Read)
````````````````````````
The way in which the colours are to be distributed among the pens. If
NINTS is the number of unreserved colour indices the mapping options
are described below.
"Histogram" - The colours are fitted to the pens using histogram
equalisation of an NDF, given by parameter IN, so that the colours
approximately have an even distribution. In other words each pen is
used approximately an equal number of times to display the
2-dimensional NDF array. There must be an existing image displayed.
This is determined by looking for a DATA picture in the database. This
is not foolproof as this may be a line plot rather an image. "Linear"
- The colours are fitted directly to the pens. "Logarithmic" - The
colours are fitted logarithmically to the pens, with colour 1 given to
the first available pen and colour NINTS given to the last pen.



NDF = NDF (Read)
````````````````
The input NDF structure containing the 2-dimensional data array to be
used for the histogram-equalisation mapping of the pens. The the data
object referenced by the last DATA picture in the graphics database is
reported. This assumes that the displayed data picture was derived
from the nominated NDF data array.



NN = _LOGICAL (Read)
````````````````````
If TRUE the input lookup table is mapped to the colour table by using
the nearest-neighbour method. This preserves sharp edges and is better
for lookup tables with blocks of colour. If NN is FALSE linear
interpolation is used, and this is suitable for smoothly varying
colour tables. [FALSE]



PERCENTILES( 2 ) = _REAL (Read)
```````````````````````````````
The percentiles that define the range of the histogram to be
equalised. For example, [25,75] would scale between the quartile
values. It is advisable not to choose the limits less than 3 per cent
and greater than 97. The percentiles are only required for histogram
mapping. All values in the NDF's data array less than the value
corresponding to the lower percentile will have the colour of the
first unreserved pen. All values greater than the value corresponding
to the upper percentile will have the colour of the last unreserved
pen.



SHADE = _REAL (Read)
````````````````````
The type of shading. This only required for the histogram mapping. A
value of -1 emphasises low values; +1 emphasises high values; 0 is
neutral, all values have equal weight. The shade must lie in the range
-1 to +1.



Examples
~~~~~~~~
lutable lo co
Changes the colour table on the current image-display device to a
series of coloured blocks whose size increase logarithmically with the
table index number.
lutable li ex rococo
This maps the lookup table stored in the NDF called rococo linearly to
the colour table on the current image-display device.
lutable li ex rococo full
This maps the lookup table stored in the NDF called rococo linearly to
the full colour table on the current image-display device, i.e.
ignoring the reserved pens.
lutable hi gr ndf=nebula shade=0 percentiles=[5 90]
This maps the greyscale lookup table via histogram equalisation
between the 5 and 90 percentiles of an NDF called nebula to the colour
table on the current image-display device. There is no bias or shading
to white or black.



Notes
~~~~~


+ The effects of this command will only be immediately apparent when
  run on X windows which have 256 colours (or other similar pseudocolour
  devices). On other devices (for instance, X windows with more than 256
  colours) the effects will only become apparent when subsequent
  graphics applications are run.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LUTREAD, LUTSAVE, LUTEDIT, LUTVIEW; Figaro: COLOUR.


Copyright
~~~~~~~~~
Copyright (C) 1991-1992, 1994 Science & Engineering Research Council.
Copyright (C) 1995, 1999, 2001, 2004 Central Laboratory of the
Research Councils. All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ Processing of bad pixels and automatic quality masking are supported
for the image NDF
+ All non-complex numeric data types can be handled. Processing is
  performed using single- or double-precision floating point, as
  appropriate.




