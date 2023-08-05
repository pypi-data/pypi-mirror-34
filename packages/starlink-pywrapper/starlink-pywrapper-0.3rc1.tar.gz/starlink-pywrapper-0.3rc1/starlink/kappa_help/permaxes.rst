

PERMAXES
========


Purpose
~~~~~~~
Permute an NDF's pixel axes


Description
~~~~~~~~~~~
This application re-orders the pixel axes of an NDF, together with all
related information (AXIS structures, and the axes of all co-ordinate
Frames stored in the WCS component of the NDF).


Usage
~~~~~


::

    
       permaxes in out perm
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF data structure.



OUT = NDF (Write)
`````````````````
The output NDF data structure.



PERM() = _INTEGER (Read)
````````````````````````
A list of integers defining how the pixel axes are to be permuted. The
list must contain one element for each pixel axis in the NDF. The
first element is the index of the pixel axis within the input NDF
which is to become axis 1 in the output NDF. The second element is the
index of the pixel axis within the input NDF which is to become axis 2
in the output NDF, etc. Axes are numbered from 1.



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null value will cause the title of the
NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
permaxes a b [2,1]
Swaps the axes in the 2-dimensional NDF called "a", to produce a new
two-dimensional NDF called "b".
permaxes a b [3,1,2]
Creates a new three-dimensional NDF called "b" in which axis 1
corresponds to axis 3 in the input three-dimensional NDF called "a",
axis 2 corresponds to input axis 1, axis 3 corresponds to input axis
2.



Notes
~~~~~


+ If any WCS co-ordinate Frame has more axes then the number of pixel
axes in the NDF, then the high numbered surplus axes in the WCS Frame
are left unchanged.
+ If any WCS co-ordinate Frame has fewer axes then the number of pixel
  axes in the NDF, then the Frame is left unchanged if the specified
  permutation would change any of the high numbered surplus pixel axes.
  A warning message is issued if this occurs.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ROTATE, FLIP; Figaro: IREVX, IREVY, IROT90.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2008, 2012 Science and Technology Facilities Council.
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
LABEL, TITLE, UNITS, WCS, and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. The data type of
  the input pixels is preserved in the output NDF.




