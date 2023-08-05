

ERASE
=====


Purpose
~~~~~~~
Erases an HDS object


Description
~~~~~~~~~~~
This routine erases a specified HDS object or container file. If the
object is a structure, then all the structure's components (and sub-
components, etc.) are also erased. If a slice or cell of an array is
specified, then the entire array is erased.


Usage
~~~~~


::

    
       erase object
       



ADAM parameters
~~~~~~~~~~~~~~~



OBJECT = UNIV (Write)
`````````````````````
The HDS object or container file to be erased.



OK = _LOGICAL (Read)
````````````````````
This parameter is used to seek confirmation before an object is
erased. If a TRUE value is given, then the HDS object will be erased.
If a FALSE value is given, then the object will not be erased and a
message will be issued to this effect.



REPORT = _LOGICAL (Read)
````````````````````````
This parameter controls what happens if the named OBJECT does not
exist. If TRUE, an error is reported. Otherwise no error is reported.
[TRUE]



Examples
~~~~~~~~
erase horse
This erases the HDS container file called horse.sdf.
erase fig123.axis
This erases the AXIS component of the HDS file called fig123.sdf. If
AXIS is a structure, all its components are erased too.
erase fig123.axis(1).label
This erases the LABEL component within the first element of the AXIS
structure of the HDS file called fig123.sdf.
erase $AGI_USER/agi_restar.agi_3200_1
This erases the AGIDEV_3200_1 structure of the HDS file called
$AGI_USER/agi_restar.sdf.



Related Applications
~~~~~~~~~~~~~~~~~~~~
Figaro: CREOBJ, DELOBJ, RENOBJ; HDSTOOLS: HCREATE, HDELETE, HRENAME.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992 Science & Engineering Research Council.
Copyright (C) 1995 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics and Astronomy Research Council.
All Rights Reserved.


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


