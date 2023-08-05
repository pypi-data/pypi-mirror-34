

SHOWQUAL
========


Purpose
~~~~~~~
Displays the quality names defined in an NDF


Description
~~~~~~~~~~~
This routine displays a list of all the quality names currently
defined within a supplied NDF (see Task SETQUAL). The descriptive
comments which were stored with the quality names when they were
originally defined are also displayed. An option exists for also
displaying the number of pixels which hold each quality.


Usage
~~~~~


::

    
       showqual ndf [count]
       



ADAM parameters
~~~~~~~~~~~~~~~



COUNT = _LOGICAL (Read)
```````````````````````
If true, then the number of pixels in each NDF which holds each
defined quality is displayed. These figures are shown in parentheses
between the quality name and associated comment. This option adds
significantly to the run time. [NO]



NDF = NDF (Read)
````````````````
The NDF whose quality names are to be listed.



QNAMES( ) = LITERAL (Write)
```````````````````````````
The quality names associated with each bit, starting from the lowest
significant bit. Unassigned bits have blank strings.



Examples
~~~~~~~~
showqual "m51,cena" yes
This example displays all the quality names currently defined for the
two NDFs "m51" and "cena" together with the number of pixels holding
each quality.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: REMQUAL, QUALTOBAD, SETQUAL.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 2002 Central Laboratory of the Research Councils. Copyright (C)
2010, 2011 Science & Technology Facilities Council. All Rights
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


