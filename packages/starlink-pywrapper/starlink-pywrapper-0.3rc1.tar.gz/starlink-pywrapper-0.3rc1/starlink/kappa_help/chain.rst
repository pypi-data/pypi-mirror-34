

CHAIN
=====


Purpose
~~~~~~~
Concatenates a series of vectorized NDFs


Description
~~~~~~~~~~~
This application concatenates a series of NDFs, in the order supplied
and treated as vectors, to form a 1-dimensional output NDF. The
dimensions of the NDFs may be different, and indeed so may their
dimensionalities.


Usage
~~~~~


::

    
       chain in c1 [c2] [c3] ... [c25] out=?
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The base NDF after which the other input NDFs will be concatenated.



OUT = NDF (Write)
`````````````````
The one-dimensional NDF resulting from concatenating the input NDFs.



C1-C25 = NDF (Read)
```````````````````
The NDFs to be concatenated to the base NDF. The NDFs are joined in
the order C1, C2, ... C25. There can be no missing NDFs, e.g. in order
for C3 to be processed there must be a C2 given as well. A null value
(!) indicates that there is no NDF. NDFs C2 to C25 are defaulted to !.
At least one NDF must be pasted, therefore C1 may not be null.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the base NDF to the output NDF. [!]



Examples
~~~~~~~~
chain obs1 obs2 out=stream
This concatenates the NDF called obs2 on to the arrays in the NDF
called obs1 to produce the 1-dimensional NDF stream.
chain c1=obs2 c2=obs1 in=obs3 out=stream
This concatenates the NDF called obs2 on to the arrays in the NDF
called obs3, and then concatenates the arrays from obs1 to them to
produce the 1-dimensional NDF stream.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PASTE, RESHAPE.


Copyright
~~~~~~~~~
Copyright (C) 1997, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
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


+ This routine correctly processes the DATA, QUALITY, VARIANCE, LABEL,
TITLE, UNITS, and HISTORY, components of an NDF data structure and
propagates all extensions. Propagation is from the base NDF. WCS and
AXIS information is lost.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




