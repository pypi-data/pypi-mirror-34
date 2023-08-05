

FLIP
====


Purpose
~~~~~~~
Reverses an NDF's pixels along a specified dimension


Description
~~~~~~~~~~~
This application reverses the order of an NDF's pixels along a
specified dimension, leaving all other aspects of the data structure
unchanged.


Usage
~~~~~


::

    
       flip in out dim
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = _LOGICAL (Read)
``````````````````````
If a TRUE value is given for this parameter (the default), then any
axis values and WCS information associated with the NDF dimension
being reversed will also be reversed in the same way. If a FALSE value
is given, then all axis values and WCS information will be left
unchanged. [TRUE]



DIM = _INTEGER (Read)
`````````````````````
The number of the dimension along which the NDF's pixels should be
reversed. The value should lie between 1 and the total number of NDF
dimensions. If the NDF has only a single dimension, then this
parameter is not used, a value of 1 being assumed.



IN = NDF (Read)
```````````````
The input NDF data structure whose pixel order is to be reversed.



OUT = NDF (Write)
`````````````````
The output NDF data structure.



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null value will cause the title of the
NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
flip a b 2
Reverses the pixels in the NDF called a along its second dimension to
create the new NDF called b.
flip specin specout
If specin is a 1-dimensional spectrum, then this example reverses the
order of its pixels to create a new spectrum specout. Note that no
value for the DIM parameter need be supplied in this case.
flip in=cube out=newcube dim=2 noaxis
Reverses the order of the pixels along dimension 2 of the NDF called
cube to give newcube, but leaves the associated axis values in their
original order.



Notes
~~~~~
The pixel-index bounds of the NDF are unchanged by this routine.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ROTATE, RESAMPLE; Figaro: IREVX, IREVY, IROT90.


Copyright
~~~~~~~~~
Copyright (C) 1991-1992 Science & Engineering Research Council.
Copyright (C) 1998, 2004 Central Laboratory of the Research Councils.
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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. The data type of
  the input pixels is preserved in the output NDF.




