

HISTEQ
======


Purpose
~~~~~~~
Performs an histogram equalisation on an NDF


Description
~~~~~~~~~~~
This application transforms an NDF via histogram equalisation.
Histogram equalisation is an image-processing technique in which the
distribution (between limits) of data values in the input array is
adjusted so that in the output array there are approximately equal
numbers of elements in each histogram bin. To achieve this the
histogram bin size is no longer a constant. This technique is commonly
known as histogram equalisation. It is useful for displaying features
across a wide dynamic range, sometimes called a maximum information
picture. The transformed array is output to a new NDF.


Usage
~~~~~


::

    
       histeq in out [numbin]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The NDF structure to be transformed.



NUMBIN = INTEGER (Read)
```````````````````````
The number of histogram bins to be used. This should be a large
number, say 2000, to reduce quantisation errors. It must be in the
range 100 to 10000. [2048]



OUT = NDF (Write)
`````````````````
The NDF structure to contain the transformed data array.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



Examples
~~~~~~~~
histeq halley maxinf
The data array in the NDF called halley is remapped via histogram
equalisation to form the new NDF called maxinf.
histeq halley maxinf 10000 title="Maximum information of Halley"
The data array in the NDF called halley is remapped via histogram
equalisation to form the new NDF called maxinf. Ten thousand bins in
the histogram are required rather than the default of 2048. The title
of NDF maxinf is "Maximum information of Halley".



Notes
~~~~~
If there are a few outliers in the data and most of the points
concentrated about a value it may be wise to truncate the data array
via THRESH, or have a large number of histogram bins.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LAPLACE, LUTABLE, SHADOW, THRESH; Figaro: HOPT.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2012 Science & Technology Facilities Council. All Rights
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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL,
TITLE, WCS and HISTORY components of an NDF data structure and
propagates all extensions. UNITS and VARIANCE become undefined by the
transformation, and so are not propagated.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




