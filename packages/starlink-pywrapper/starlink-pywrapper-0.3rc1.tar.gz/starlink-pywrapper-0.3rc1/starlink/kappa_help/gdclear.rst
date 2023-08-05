

GDCLEAR
=======


Purpose
~~~~~~~
Clears a graphics device and purges its database entries


Description
~~~~~~~~~~~
This application software resets a graphics device. In effect the
device is cleared. It purges the graphics-database entries for the
device. Optionally, only the current picture is cleared and the
database unchanged. (Note the clearing of the current picture may not
work on some graphics devices.)


Usage
~~~~~


::

    
       gdclear [device] [current]
       



ADAM parameters
~~~~~~~~~~~~~~~



CURRENT = _LOGICAL (Read)
`````````````````````````
If TRUE then only the current picture is cleared. [FALSE]



DEVICE = DEVICE (Read)
``````````````````````
The device to be cleared. [Current graphics device]



Examples
~~~~~~~~
gdclear
Clears the current graphics device and purges its graphics database
entries.
gdclear current
Clears the current picture on the current graphics device.
gdclear xw
Clears the xw device and purges its graphics database entries.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: GDSET, GDSTATE.


Copyright
~~~~~~~~~
Copyright (C) 1989-1992 Science & Engineering Research Council.
Copyright (C) 1999, 2004 Central Laboratory of the Research Councils.
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


