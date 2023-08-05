

QUALTOBAD
=========


Purpose
~~~~~~~
Sets selected NDF pixels bad on the basis of Quality


Description
~~~~~~~~~~~
This routine produces a copy of an input NDF in which selected pixels
are set bad. The selection is based on the values in the QUALITY
component of the input NDF; any pixel which holds a set of qualities
satisfying the quality expression given for parameter QEXP is set bad
in the output NDF. Named qualities can be associated with specified
pixels using the SETQUAL task.


Usage
~~~~~


::

    
       qualtobad in out qexp
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF.



OUT = NDF (Write)
`````````````````
The output NDF.



QEXP = LITERAL (Read)
`````````````````````
The quality expression.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. A null (!) value will cause the input title
to be used. [!]



Examples
~~~~~~~~
qualtobad m51* *_clean saturated.or.glitch
This example copies all NDFs starting with the string "m51" to a set
of corresponding output NDFs. The name of each output NDF is formed by
extending the name of the input NDF with the string "_clean". Any
pixels which hold either of the qualities "saturated" or "glitch" are
set to the bad value in the output NDFs.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: REMQUAL, SETBB, SETQUAL, SHOWQUAL.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 2002, 2004 Central Laboratory of the Research Councils. Copyright
(C) 2008, 2012 Science & Technology Facilities Council. All Rights
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


