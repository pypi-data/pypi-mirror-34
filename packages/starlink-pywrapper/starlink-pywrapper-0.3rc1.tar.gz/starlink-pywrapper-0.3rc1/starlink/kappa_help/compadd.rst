

COMPADD
=======


Purpose
~~~~~~~
Reduces the size of an NDF by adding values in rectangular boxes


Description
~~~~~~~~~~~
This application takes an NDF data structure and reduces it in size by
integer factors along each dimension. The compression is achieved by
adding the values of the input NDF within non-overlapping
`rectangular' boxes whose dimensions are the compression factors. The
additions may be normalised to correct for any bad values present in
the input NDF. The exact placement of the boxes can be controlled
using parameter ALIGN.


Usage
~~~~~


::

    
       compadd in out compress [wlim]
       



ADAM parameters
~~~~~~~~~~~~~~~



ALIGN = LITERAL (Read)
``````````````````````
This parameter controls the placement of the compression boxes within
the input NDF (also see parameter TRIM). It can take any of the
following values:


+ "ORIGIN" --- The compression boxes are placed so that the origin of
the pixel co-ordinate Frame (i.e. pixel coords (0,0)) in the input NDF
corresponds to a corner of a compression box. This results in the
pixel origin being retained in the output NDF. For instance, if a pair
of 2-dimensional images which have previously been aligned in pixel
co-ordinates are compressed, then using this option ensures that the
compressed images will also be aligned in pixel co-ordinates.
+ "FIRST" --- The compression boxes are placed so that the first pixel
in the input NDF (for instance, the bottom left pixel in a
2-dimensional image) corresponds to the first pixel in a compression
box. This can result in the pixel origin being shifted by up to one
compression box in the output image. Thus, images which were
previously aligned in pixel co-ordinates may not be aligned after
compression. You may want to use this option if you are using a very
large box to reduce the number of dimensions in the data (for instance
summing across the entire width of an image to produce a 1-dimensional
array).
+ "LAST" --- The compression boxes are placed so that the last pixel
  in the input NDF (for instance, the top right pixel in a 2-dimensional
  image) corresponds to the last pixel in a compression box. See the
  "FIRST" option above for further comments. ["ORIGIN"]





AXWEIGHT = _LOGICAL (Read)
``````````````````````````
When there is an AXIS variance array present in the NDF and
AXWEIGHT=TRUE the application forms weighted averages of the axis
centres using the variance. For all other conditions the non-bad axis
centres are given equal weight during the averaging to form the output
axis centres. [FALSE]



COMPRESS( ) = _INTEGER (Read)
`````````````````````````````
Linear compression factors to be used to create the output NDF. There
should be one for each dimension of the NDF. If fewer are supplied the
last value in the list of compression factors is given to the
remaining dimensions. Thus if a uniform compression is required in all
dimensions, just one value need be entered. The suggested default is
the current value.



IN = NDF (Read)
```````````````
The NDF structure to be reduced in size.



NORMAL = _LOGICAL (Read)
````````````````````````
When there are bad pixels present in the summation box these are
ignored. Therefore a simple addition of the input-array component's
values will yield a result discordant with neighbouring output pixels
that were formed from summation of all the pixels in the box. When
NORMAL=TRUE the output values are normalised: the addition is
multiplied by the ratio of the number of pixels in the box to the
number of good pixels therein to arrive at the output value. When
NORMAL=FALSE the output values are always just the sum of the good
pixels. [TRUE]



OUT = NDF (Write)
`````````````````
NDF structure to contain compressed version of the input NDF.



PRESERVE = _LOGICAL (Read)
``````````````````````````
If the input data type is to be preserved on output then this
parameter should be set true. However, this may result in overflows
for integer types and hence additional bad values written to the
output NDF. If this parameter is set false then the output data type
will be one of _REAL or _DOUBLE, depending on the input type. [FALSE]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



TRIM = _LOGICAL (Read)
``````````````````````
If parameter TRIM is set TRUE, the output NDF only contains data for
compression boxes which are entirely contained within the input NDF.
Any pixels around the edge of the input NDF which are not contained
within a compression box are ignored. If TRIM is set FALSE, the output
NDF contains data for all compression boxes which have any overlap
with the input NDF. All pixels outside the bounds of the NDF are
assumed to be bad. That is, any boxes which extend beyond the bounds
of the input NDF are padded with bad pixels. See also parameter ALIGN.
[current value]



WLIM = _REAL (Read)
```````````````````
If the input NDF contains bad pixels, then this parameter may be used
to determine the number of good pixels which must be present within
the addition box before a valid output pixel is generated. It can be
used, for example, to prevent output pixels from being generated in
regions where there are relatively few good pixels to contribute to
the smoothed result.
WLIM specifies the minimum fraction of good pixels which must be
present in the summation box in order to generate a good output pixel.
If this specified minimum fraction of good input pixels is not
present, then a bad output pixel will result, otherwise the output
value will be the sum of the good values. The value of this parameter
should lie between 0.0 and 1.0 (the actual number used will be rounded
up if necessary to correspond to at least 1 pixel). [0.3]



Examples
~~~~~~~~
compadd cosmos galaxy 4
This compresses the NDF called cosmos summing four times in each
dimension, and stores the reduced data in the NDF called galaxy. Thus
if cosmos is two-dimensional, this command would result in a sixteen-
fold reduction in the array components.
compadd cosmos profile [10000,1] wlim=0 align=first trim=no
This compresses the 2-dimensional NDF called cosmos to produce a
1-dimensional NDF called profile. This is done using a compression box
which is 1 pixel high, but which is wider than the whole input image.
Each pixel in the output NDF thus corresponds to the sum of the
corresponding row in the input image. WLIM is set to zero to ensure
that bad pixels are ignored. ALIGN is set to FIRST so that each
compression box is flush with the left edge of the input image. TRIM
is set to NO so that compression boxes which extend outside the bounds
of the input image (which will be all of them if the input image is
narrower than 10000 pixels) are retained in the output NDF.
compadd cosmos galaxy 4 wlim=1.0
This compresses the NDF called cosmos adding four times in each
dimension, and stores the reduced data in the NDF called galaxy. Thus
if cosmos is two-dimensional, this command would result in a sixteen-
fold reduction in the array components. If a summation box contains
any bad pixels, the output pixel is set to bad.
compadd cosmos galaxy 4 0.0 preserve
As above except that a summation box need only contains a single non-
bad pixels for the output pixel to be good, and galaxy's array
components will have the same as those in cosmos.
compadd cosmos galaxy [4,3] nonormal title="COSMOS compressed"
This compresses the NDF called cosmos adding four times in the first
dimension and three times in higher dimensions, and stores the reduced
data in the NDF called galaxy. Thus if cosmos is two-dimensional, this
command would result in a twelve-fold reduction in the array
components. Also, if there are bad pixels there will be no
normalisation correction for the missing values. The title of the
output NDF is "COSMOS compressed".
compadd in=arp244 compress=[1,1,3] out=arp244cs
Suppose arp244 is a huge NDF storing a spectral-line data cube, with
the third dimension being the spectral axis. This command compresses
arp244 in the spectral dimension, adding every three pixels to form
the NDF called arp244cs.



Notes
~~~~~


+ The axis centres and variances are averaged, whilst the widths are
  summed and always normalised for bad values.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: BLOCK, COMPAVE, COMPICK, PIXDUPE, SQORST, RESAMPLE; Figaro:
ISTRETCH, YSTRACT.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 1998-2000, 2004 Central Laboratory of the Research Councils.
All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, VARIANCE, LABEL,
TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions. QUALITY is not processed since it is a
series of flags, not numerical values.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




