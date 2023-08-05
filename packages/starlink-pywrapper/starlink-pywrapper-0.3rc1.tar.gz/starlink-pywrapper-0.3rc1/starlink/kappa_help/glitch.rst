

GLITCH
======


Purpose
~~~~~~~
Replaces bad pixels in a 2-d NDF with the local median


Description
~~~~~~~~~~~
This routine removes bad pixels from a 2-d NDF, replacing them with
the median of the eight (or less at the edges) neighbouring pixels. At
least three of these eight neighbouring pixels must have good values
(that is, they must not set to the bad value) otherwise the resultant
pixel becomes bad.
The positions of the pixels to be removed can be supplied in four ways
(see parameter MODE):


+ In response to parameter prompts. A single bad pixel position is
supplied at each prompt, and the user is re-prompted until a null
value is supplied.
+ Within a positions list such as produced by applications CURSOR,
LISTMAKE, etc.
+ Within a simple text file. Each line contains the position of a
pixel to be replaced.
+ Alternatively, each bad pixel in the input NDF can be used (subject
  to the above requirement that at least three out of the eight
  neighbouring pixels are not bad).




Usage
~~~~~


::

    
       glitch in out [title] { incat=?
                             { infile=?
                             { pixpos=?
                             mode
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input image.



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a positions list giving the pixels to be
replaced, such as produced by applications CURSOR, LISTMAKE, etc. Only
accessed if parameter MODE is given the value "Catalogue".



INFILE = FILENAME (Read)
````````````````````````
The name of a text file containing the positions of the pixels to be
replaced. The positions should be given in the current co-ordinate
Frame of the input NDF, one per line. Spaces or commas can be used as
delimiters between axis values. The file may contain comment lines
with the first character # or !. This parameter is only used if
parameter MODE is set to "File".



MODE = LITERAL (Read)
`````````````````````
The method used to obtain the positions of the pixels to be replaced.
The supplied string can be one of the following options.


+ "Bad" -- The bad pixels in the input NDF are used.
+ "Catalogue" -- Positions are obtained from a positions list using
parameter INCAT.
+ "File" -- The pixel positions are read from a text file specified by
parameter INFILE.
+ "Interface" -- The position of each pixel is obtained using
  parameter PIXPOS. The number of positions supplied must not exceed
  200.

[current value]



OUT = NDF (Write)
`````````````````
The output image.



PIXPOS = LITERAL (Read)
```````````````````````
The position of a pixel to be replaced, in the current co-ordinate
Frame of the input NDF. Axis values should be separated by spaces or
commas. This parameter is only used if parameter MODE is set to
"Interface". If a value is supplied on the command line, then the
application exits after processing the single specified pixel.
Otherwise, the application loops to obtain multiple pixels to replace,
until a null (!) value is supplied. Entering a colon (":") will result
in a description of the required co-ordinate Frame being displayed,
followed by a prompt for a new value.



TITLE = LITERAL (Read)
``````````````````````
Title for the output image. A null value (!) propagates the title from
the input image to the output image. [!]



Examples
~~~~~~~~
glitch m51 cleaned mode=cat incat=badpix.FIT
Reads pixel positions from the positions list stored in the FITS file
badpix.FIT, and replaces the corresponding pixels in the 2-d NDF
m51.sdf by the median of the surrounding neighbouring pixels. The
cleaned image is written to cleaned.sdf.



Notes
~~~~~


+ If the current co-ordinate Frame of the input NDF is not PIXEL, then
  the supplied positions are first mapped into the PIXEL Frame before
  being used.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDMASK, CHPIX, FILLBAD, ZAPLIN, NOMAGIC, REGIONMASK, SEGMENT,
SETMAGIC; Figaro: CSET, ICSET, NCSET, TIPPEX.


Copyright
~~~~~~~~~
Copyright (C) 2000, 2004 Central Laboratory of the Research Councils.
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ Only single and double precision floating point data can be
  processed directly. All integer data will be converted to floating
  point before being processed.




