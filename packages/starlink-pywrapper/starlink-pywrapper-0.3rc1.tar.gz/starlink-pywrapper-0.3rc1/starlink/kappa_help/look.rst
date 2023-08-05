

LOOK
====


Purpose
~~~~~~~
Lists pixel values in a one- or two-dimensional NDF


Description
~~~~~~~~~~~
This application lists pixel values within a region of a two-
dimensional NDF. The listing may be displayed on the screen and logged
in a text file (see Parameter LOGFILE). The region to be listed can be
specified either by giving its centre and size or its corners, or by
giving an `ARD Description' for the region (see Parameter MODE). The
top-right pixel value is also written to an output Parameter (VALUE).
The listing may be produced in several different formats (see
Parameter FORMAT), and the format of each individual displayed data
value can be controlled using Parameter STYLE.


Usage
~~~~~


::

    
       look ndf centre [size] [logfile] [format] [comp] [mode]
          { arddesc=?
          { ardfile=?
          { lbound=? ubound=?
          { centre=?
          mode
       



ADAM parameters
~~~~~~~~~~~~~~~



AGAIN = _LOGICAL (Read)
```````````````````````
If TRUE, the user is prompted for further regions to list until a
FALSE value is obtained. [FALSE]



ARDDESC = LITERAL (Read)
````````````````````````
An `ARD Description' for the parts of the image to be listed. Multiple
lines can be supplied by ending each line with a hyphen, in which case
further prompts for ARDDESC are made until a value is supplied which
does not end with a hyphen. All the supplied values are then
concatenated together (after removal of the trailing minus signs).
ARDDESC is only accessed if MODE is "ARD". Positions in the ARD
description are assumed to be in the current co-ordinate Frame of the
NDF unless there are COFRAME or WCS statements which indicate a
different system. See "Notes" below.



ARDFILE = FILENAME (Read)
`````````````````````````
The name of an existing text file containing an `ARD Description' for
the parts of the image to be listed. ARDFILE is only accessed if MODE
is "ARDFile". Positions in the ARD description are assumed to be in
pixel co-ordinates unless there are COFRAME or WCS statements that
indicate a different system. See "Notes" below.



CENTRE = LITERAL (Read)
```````````````````````
The co-ordinates of the data pixel at the centre of the area to be
displayed, in the current co-ordinate Frame of the NDF (supplying a
colon ":" will display details of the current co-ordinate Frame). The
position should be supplied as a list of formatted axis values
separated by spaces or commas. See also Parameter USEAXIS. CENTRE is
only acessed if MODE is "Centre".



COMP = LITERAL (Read)
`````````````````````
The NDF array component to be displayed. It may be "Data", "Quality",
"Variance", or "Error" (where "Error" is an alternative to "Variance"
and causes the square root of the variance values to be displayed). If
"Quality" is specified, then the quality values are treated as
numerical values (in the range 0 to 255). ["Data"]



FORMAT = LITERAL (Read)
```````````````````````
Specifies the format for the listing from the following options.


+ "strips" -- The area being displayed is divided up into vertical
strips of limited width. Each strip is displayed in turn, with Y pixel
index at the left of each row, and X pixel index at the top of each
column. The highest row is listed first in each strip. This format is
intended for human readers - the others are primarily intended for
being read by other software.
+ "clist" -- Each row of textual output consists of an X pixel index,
followed by a Y pixel index, followed by the pixel data value. No
headers or blank lines are included. The pixels are listed in "Fortran
order"---the lower left pixel first, and the upper right pixel last.
+ "cglist" -- Like "clist" except bad pixels are omitted from the
list.
+ "wlist" -- Each row of textual output consists of the WCS co-
ordinates of the pixel, followed by the pixel data value. No headers
or blank lines are included. The pixels are listed in "Fortran order"
---the lower left pixel first, and the upper right pixel last.
+ "wglist" -- Like "wlist" except bad pixels are omitted from the
list.
+ "vlist" -- Each row of textual output consists of just the pixel
data value. No headers or blank lines are included. The pixels are
listed in "Fortran order"---the lower-left pixel first, and the upper-
right pixel last.
+ "region" -- The pixel data values are listed as a two-dimensional
  region. Each row of textual output contains a whole row of data
  values. The textual output may be truncated if it is too wide. The
  lowest row is listed first.

In all cases, adjacent values are separated by spaces, and bad pixel
values are represented by the string "BAD". ["strips"]



LBOUND = LITERAL (Read)
```````````````````````
The co-ordinates of the data pixel at the bottom-left of the area to
be displayed, in the current co-ordinate Frame of the NDF (supplying a
colon ":" will display details of the current co-ordinate Frame). The
position should be supplied as a list of formatted axis values
separated by spaces or commas. See also Parameter USEAXIS. A null (!)
value causes the bottom-left corner of the supplied NDF to be used.
LBOUND is only accessed if MODE is "Bounds".



LOGFILE = FILENAME (Write)
``````````````````````````
The name of the text file in which the textual output may be stored.
See MAXLEN. A null string (!) means that no file is created. [!]



MAXLEN = _INTEGER (Read)
````````````````````````
The maximum number of characters in a line of textual output. The line
is truncated after the last complete value if it would extend beyond
this value. [80]



MODE = LITERAL (Read)
`````````````````````
Indicates how the region to be listed will be specified:


+ "All" -- The entire NDF is used.
+ "Centre" -- The centre and size of the region are specified using
parameters CENTRE and SIZE.
+ "Bounds" -- The bounds of the region are specified using parameters
LBOUND and UBOUND.
+ "ARDFile" -- The region is given by an `ARD Description' supplied
within a text file specified using Parameter ARDFILE. Pixels outside
the ARD region are represented by the string "OUT".
+ "ARD" -- The region is given using an ARD description supplied
  directly using Parameter ARDDESC. Pixels outside the ARD region are
  represented by the string "OUT".

["Centre"]



NDF = NDF (Read)
````````````````
The input NDF structure containing the data to be displayed.



SIZE( 2 ) = _INTEGER (Read)
```````````````````````````
The dimensions of the rectangular area to be displayed, in pixels. If
a single value is given, it is used for both axes. The area is centred
on the position specified by parameter CENTRE. It is only accessed if
MODE is "Centre". [7]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the format to use for
individual data values.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings over-riding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a Frame attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!) is supplied. See Section "Plotting Attributes" in SUN/95 for
a description of the available attributes. Any unrecognised attributes
are ignored (no error is reported).
Data values are formatted using attributes Format(1) and Digits(1).
[current value]



UBOUND = LITERAL (Read)
```````````````````````
The co-ordinates of the data pixel at the top-right corner of the area
to be displayed, in the current co-ordinate Frame of the NDF
(supplying a colon ":" will display details of the current co-ordinate
Frame). The position should be supplied as a list of formatted axis
values separated by spaces or commas. See also Parameter USEAXIS. A
null (!) value causes the top-right corner of the supplied NDF to be
used. UBOUND is only accessed if MODE is "Bounds".



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of two strings should be supplied
specifying the two axes which are to be used when supplying positions
for parameters CENTRE, LBOUND and UBOUND. Each axis can be specified
using one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if you supply an illegal
value. If a null (!) value is supplied, the axes with the same indices
as the two used pixel axes within the NDF are selected. [!]



VALUE = _DOUBLE (Write)
```````````````````````
An output parameter to which is written the data value at the top-
right pixel in the displayed rectangle.



Examples
~~~~~~~~
look ngc6872 "1:27:23 -22:41:12" logfile=log
Lists a 7x7 block of pixel values centred on RA/DEC 1:27:23,

+ 22:41:12 (this assumes that the current co-ordinate Frame in the NDF
  is an RA/DEC Frame). The listing is written to the text file "log".


look m57 mode=bo lbound="18 20" ubound="203 241"
Lists the pixel values in an NDF called m57, within a rectangular
region from pixel (18,20) to (203,241) (this assumes that the current
co-ordinate Frame in the NDF is pixel co-ordinates). The listing is
displayed on the screen only.
look ngc6872 "10 11" 1
Stores the value of pixel (10,11) in output parameter VALUE, but does
not store it in a log file. This assumes that the current co-ordinate
Frame in the NDF is pixel co-ordinates.
look ngc6872 mode=ard arddesc="circle(1:27:23,-22:41:12,0:0:10)"
Lists the pixel values within a circle of radius 10 arcseconds,
centred on RA=1:27:23 DEC=-22:41:12. This assumes that the current co-
ordinate Frame in the NDF is an RA/DEC Frame.
look ngc6872 mode=ardfile ardfile=central.ard
Lists the pixel values specified by the ARD description stored in the
text file "central.dat".



Notes
~~~~~


+ ARD files may be created by ARDGEN or written manually. In the
latter case consult SUN/183 for full details of the ARD descriptors
and syntax; however, much may be learnt from looking at the ARD files
created by ARDGEN and the ARDGEN documentation. There is also a
summary with examples in the main body of SUN/95.
+ The co-ordinate system in which positions are given within ARD
descriptions can be indicated by including suitable COFRAME or WCS
statements within the description (see SUN/183). For instance,
starting the description with the text "COFRAME(PIXEL)" will indicate
that positions are specified in pixel co-ordinates. The statement
"COFRAME(SKY,System=FK5)" would indicate that positions are specified
in RA/DEC (FK5,J2000). If no such statements are included, then a
default co-ordinate system is used as specified in the parameter
description above.
+ Output messages are not displayed on the screen when the message
  filter environment variable MSG_FILTER is set to QUIET. The creation
  of output parameters and the log file is unaffected by MSG_FILTER.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: TRANDAT, ARDGEN, ARDMASK, ARDPLOT.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA, QUALITY and VARIANCE
components of the input NDF.
+ Processing of bad pixels and automatic quality masking are
  supported.




