

COMPICK
=======


Purpose
~~~~~~~
Reduces the size of an NDF by picking equally spaced pixels


Description
~~~~~~~~~~~
This application takes an NDF data structure and reduces it in size by
integer factors along each dimension. The input NDF is sampled at
these constant compression factors or intervals along each dimension,
starting from a defined origin, to form an output NDF structure. The
compression factors may be different in each dimension.


Usage
~~~~~


::

    
       compick in out compress [origin]
       



ADAM parameters
~~~~~~~~~~~~~~~



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



ORIGIN( ) = _INTEGER (Read)
```````````````````````````
The pixel indices of the first pixel to be selected. Thereafter the
selected pixels will be spaced equally by COMPRESS() pixels. The
origin must lie within the first selection intervals, therefore the
ith origin must be in the range LBND(i) to LBND(i)+COMPRESS(i)-1,
where LBND(i) is the lower bound of the ith dimension. If a null (!)
value is supplied, the first array element is used. [!]



OUT = NDF (Write)
`````````````````
NDF structure to contain compressed version of the input NDF.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



Examples
~~~~~~~~
compick cosmos galaxy 4
This compresses the NDF called cosmos selecting every fourth array
element along each dimension, starting from the first element in the
NDF, and stores the reduced data in the NDF called galaxy.
compick cosmos galaxy 4 [3,2]
This compresses the two-dimensional NDF called cosmos selecting every
fourth array element along each dimension, starting from the pixel
index (3,2), and stores the reduced data in the NDF called galaxy.
compick in=arp244 compress=[1,1,3] out=arp244cs
Suppose arp244 is a huge NDF storing a spectral-line data cube, with
the third dimension being the spectral axis. This command compresses
arp244 in the spectral dimension, sampling every third pixel, starting
from the first wavelength at each image position, to form the NDF
called arp244cs.



Notes
~~~~~


+ The compression is centred on the origin of the pixel co-ordinate
  Frame. That is, if a position has a value p(i) on the i'th pixel co-
  ordinate axis of the input NDF, then it will have position
  p(i)/COMPRESS(i) on the corresponding axis of the output NDF. The
  pixel index bounds of the output NDF are chosen accordingly.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: BLOCK, COMPADD, COMPAVE, PIXDUPE, SQORST, RESAMPLE; Figaro:
ISTRETCH.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2012 Science & Facilities Research Council. All Rights
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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




