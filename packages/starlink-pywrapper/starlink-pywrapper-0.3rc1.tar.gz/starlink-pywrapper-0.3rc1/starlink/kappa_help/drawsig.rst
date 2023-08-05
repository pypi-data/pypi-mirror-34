

DRAWSIG
=======


Purpose
~~~~~~~
Draws +/-n standard-deviation lines on a line plot


Description
~~~~~~~~~~~
This routine draws straight lines on an existing plot stored in the
graphics database, such as produced by LINPLOT or HISTOGRAM. The lines
are located at arbitrary multiples of the standard deviation (NSIGMA)
either side of the mean of a given dataset. The default dataset is the
one used to draw the existing plot. You can plot the lines
horizontally or vertically as appropriate. The lines extend the full
width or height of the plot's data area. Up to five different
multiples of the standard deviation may be presented in this fashion.
Each line can be drawn with a different style (see Parameter STYLE).
The application also computes statistics for those array values that
lie between each pair of plotted lines. In other words it finds the
statistics between clipping limits defined by each 2*NSIGMA range
centred on the unclipped mean.
The task tabulates NSIGMA, the mean, the standard deviation, and the
error in the mean after the application of each pair of clipping
limits. For comparison purposes the first line of the table presents
these values without clipping. The table is written at the normal
reporting level.


Usage
~~~~~


::

    
       drawsig ndf nsigma [axis] [comp]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = LITERAL (Read)
`````````````````````
The orientation of the lines, or put another way, the axis which
represents data value. Thus the allowed values are "Horizontal",
"Vertical", "X", or "Y". "Horizontal" is equivalent to "Y" and
"Vertical" is a synonym for "X". On LINPLOT output AXIS would be "Y",
but on a plot from HISTOGRAM it would be "X". The suggested default is
the current value. ["Y"]



COMP = LITERAL (Read)
`````````````````````
The name of the NDF array component from which to derive the mean and
standard deviation used to draw the lines: "Data", "Error", "Quality"
or "Variance" (where "Error" is the alternative to "Variance" and
causes the square root of the variance values to be taken before
computing the statistics). If "Quality" is specified, then the quality
values are treated as numerical values (in the range 0 to 255).
["Data"]



DEVICE = DEVICE (Read)
``````````````````````
The graphics device to draw the sigma lines on. [Current graphics
device]



NDF = NDF (Read)
````````````````
The NDF structure containing the data array whose error limits are to
be plotted. Usually this parameter is not defined thereby causing the
statistics to be derived from the dataset used to draw the plot. If,
however, you had plotted a section of a dataset but wanted to plot the
statistics from the whole dataset, you would specify the full dataset
with Parameter NDF. [The dataset used to create the existing plot.]



NSIGMA() = _REAL (Read)
```````````````````````
Number of standard deviations about the mean at which the lines should
be drawn. The null value or 0.0 causes a line to be drawn at the mean
value.



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use for
the lines.
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
The attributes Colour(Curves), Width(Curves), etc, can be used to
specify the style for the lines ("Lines" is recognised as a synonym
for "Curves"). These values apply to all lines unless subsequent
attributes over-ride them. Attributes for individual clipping levels
can be given by replacing "Curves" above by a string of the form
"Nsig<i>" where "<i>" is an integer index into the list of clipping
levels supplied for Parameter NSIGMA. Thus, "Colour(Nsig1)" will set
the colour for the lines associated with the first clipping level,
etc. The attribute settings can be restricted to one of the two lines
by appending either a "+" or a "-" to the "Nsig<i>" string. Thus,
"Width(Nsig2-)" sets the line width for the lower of the two lines
associated with the second clipping level, and "Width(Nsig2+)" sets
the width for the upper of the two lines. [current value]



Examples
~~~~~~~~
drawsig nsigma=3 style='style=1'
This draws solid horizontal lines on the last DATA picture on the
current graphics device located at plus and minus 3 standard
deviations about the mean. The statistics come from the data array
used to draw the DATA picture.
drawsig phot 2.5
This draws horizontal plus and minus 2.5 standard-deviation lines
about the mean for the data in the NDF called phot on the default
graphics device.
drawsig phot 2.5 style='"colour(nsig1-)=red,colour(nsig1+)=green"'
As above, but the lower line is drawn in red and the upper line is
drawn in green.
drawsig cluster [2,3] X Error
This draws vertical lines at plus and minus 2 and 3 standard
deviations about the mean for the error data in the NDF called cluster
on the default graphics device.
drawsig device=xwindows phot(20:119) 3 style="'colour=red,style=4'"
This draws red dotted horizontal lines on the xwindows device at +/- 3
standard deviations using the 100 pixels in NDF phot(20:119).



Notes
~~~~~
There must be an existing DATA picture stored within the graphics
database for the chosen device. Lines will only be plotted within this
picture.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISTOGRAM, LINPLOT, MLINPLOT, STATS.


Copyright
~~~~~~~~~
Copyright (C) 1996, 1998-1999, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2010, 2012 Science & Technology Facilities
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA, VARIANCE, and QUALITY,
components of the NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. The statistics
are calculated using double-precision floating point.
+ Any number of NDF dimensions is supported.




