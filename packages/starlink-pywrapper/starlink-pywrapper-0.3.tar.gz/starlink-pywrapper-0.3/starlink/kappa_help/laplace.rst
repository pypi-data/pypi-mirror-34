

LAPLACE
=======


Purpose
~~~~~~~
Performs a Laplacian convolution as an edge detector in a 2-d NDF


Description
~~~~~~~~~~~
This routine calculates the Laplacian of the supplied 2-d NDF, and
subtracts it from the original array to create the output NDF. The
subtractions can be done a specified integer number of times. This
operation can be approximated by a convolution with the kernel:


+ N -N -N
+ N +8N -N
+ N -N -N

where N is the integer number of times the Laplacian is subtracted.
This convolution is used as a uni-directional edge detector. Areas
where the input data array is flat become zero in the output data
array.


Usage
~~~~~


::

    
       laplace in number out title
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input NDF.



NUMBER = _INTEGER (Read)
````````````````````````
Number of Laplacians to remove. [1]



OUT = NDF (Write)
`````````````````
Output NDF.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
laplace a 10 b
This subtracts 10 Laplacians from the NDF called a, to make the NDF
called b. NDF b inherits its title from a.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SHADOW, MEDIAN; Figaro: ICONV3.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
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


+ This routine correctly processes the WCS, AXIS, DATA, and VARIANCE
components of an NDF data structure. QUALITY is propagated.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




