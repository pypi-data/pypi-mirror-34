

EXPON
=====


Purpose
~~~~~~~
Takes the exponential (specified base) of an NDF data structure


Description
~~~~~~~~~~~
This routine takes the exponential to a specified base of each pixel
of a NDF to produce a new NDF data structure.


Usage
~~~~~


::

    
       expon in out base
       



ADAM parameters
~~~~~~~~~~~~~~~



BASE = LITERAL (Read)
`````````````````````
The base of the exponential to be applied. A special value "Natural"
gives natural (base-e) exponentiation.



IN = NDF (Read)
```````````````
Input NDF data structure.



OUT = NDF (Write)
`````````````````
Output NDF data structure being the exponential of the input NDF.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
expon a b 10
This takes exponentials to base ten of the pixels in the NDF called a,
to make the NDF called b. NDF b inherits its title from a.
expon base=8 title="HD123456" out=b in=a
This takes exponential to base eight of the pixels in the NDF called
a, to make the NDF called b. NDF b has the title "HD123456".



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LOG10, LOGAR, LOGE, EXP10, EXPE, POW; Figaro: IALOG, ILOG,
IPOWER.


Copyright
~~~~~~~~~
Copyright (C) 1997, 1999, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2012 Science & Technology facilities Council.
All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the free Software foundation; either Version 2 of the License, or (at
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
TITLE, UNITS, HISTORY, WCS, and VARIANCE components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




