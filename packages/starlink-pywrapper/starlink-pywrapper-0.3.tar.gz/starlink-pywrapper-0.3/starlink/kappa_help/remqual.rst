

REMQUAL
=======


Purpose
~~~~~~~
Remove specified quality definitions from an NDF


Description
~~~~~~~~~~~
This routine removes selected quality name definitions from an NDF
(see task SETQUAL). All quality names information may be removed by
specifying a quality name of "ANY".
An error will be reported if an attempt is made to remove a quality
name that has been flagged as "read-only" (e.g. using the READONLY
parameter of the SETQUAL application).


Usage
~~~~~


::

    
       remqual ndf qnames
       



ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Update)
``````````````````
The NDF to be modified.



QNAMES = LITERAL (Read)
```````````````````````
A group of up to 10 quality names to be removed from the input NDF.
The group may be supplied as a comma separated list, or within a text
file (in which case the name of the text file should be given,
preceeded by a "^" character.) If more than 10 names are supplied,
only the first 10 are used. If any of the supplied quality names are
not defined in the NDF, then warning messages are given but the
application continues to remove any other specified quality names. If
the string ANY is specified, then all defined quality names are
removed. If no defined quality names remain, the structure used to
store quality name information is deleted. This feature can be used to
get rid of corrupted quality name information.



Examples
~~~~~~~~
remqual "m51*" any
This example will remove all defined quality names from all NDFs with
names starting with the string "m51".



Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 2002 Central Laboratory of the Research Councils. Copyright (C)
2008 Science & Technology Facilities Council. All Rights Reserved.


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


