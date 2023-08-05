

PICEMPTY
========


Purpose
~~~~~~~
Finds the first empty FRAME picture in the graphics database


Description
~~~~~~~~~~~
This application selects the first, i.e. oldest, empty FRAME picture
in the graphics database for a graphics device. Empty means that there
is no additional picture lying completely with its bounds. This
implies that the FRAME is clear for plotting. This task is probably
most useful for plotting data in a grid of FRAME pictures.


Usage
~~~~~


::

    
       picempty [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation. [The current graphics device]



Examples
~~~~~~~~
picempty
This selects the first empty FRAME picture for the current graphics
device.
picempty xwindows
This selects the first empty FRAME picture for the xwindows graphics
device.



Notes
~~~~~


+ An error is returned if there is no empty FRAME picture, and the
  current picture remains unchanged.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PICENTIRE, PICGRID, PICLAST, PICLIST, PICSEL, PICVIS.


Timing
~~~~~~
The execution time is approximately proportional to the number of
pictures in the database before the first empty FRAME picture is
identified.


Copyright
~~~~~~~~~
Copyright (C) 1995, 2004 Central Laboratory of the Research Councils.
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


