

PICCUR
======


Purpose
~~~~~~~
Uses a graphics cursor to change the current picture


Description
~~~~~~~~~~~
This application allows you to select a new current picture in the
graphics database using the cursor. Each time a position is selected
(usually by pressing a button on the mouse), details of the topmost
picture in the AGI database which encompasses that position are
displayed, together with the cursor position (in millimetres from the
bottom left corner of the graphics device). On exit the last picture
selected becomes the current picture.


Usage
~~~~~


::

    
       piccur [device] [name]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation. [The current graphics device]



NAME = LITERAL (Read)
`````````````````````
Only pictures of this name are to be selected. For instance, if you
want to select a DATA picture which is covered by a transparent FRAME
picture, then you could specify NAME=DATA. A null (!) or blank string
means that pictures of all names may be selected. [!]



SINGLE = _LOGICAL (Read)
````````````````````````
If TRUE then the user can supply only one position using the cursor,
where-upon the application immediately exits, leaving the selected
picture as the current picture. If FALSE is supplied, then the user
can supply multiple positions. Once all positions have been supplied,
a button is pressed to indicate that no more positions are required.
[FALSE]



Examples
~~~~~~~~
piccur
This selects a picture on the current graphics device by use of the
cursor. The picture containing the last-selected point becomes the
current picture.
piccur name=data
This is like the previous example, but only DATA pictures can be
selected.



Notes
~~~~~


+ Nothing is displayed on the screen when the message filter
  environment variable MSG_FILTER is set to QUIET.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CURSOR, PICBASE, PICDATA, PICEMPTY, PICENTIRE, PICFRAME,
PICLIST, PICSEL, PICVIS.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2009 Science and Technology Facilities Council. All
Rights Reserved.


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


