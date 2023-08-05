

PICLIST
=======


Purpose
~~~~~~~
Lists the pictures in the graphics database for a device


Description
~~~~~~~~~~~
This application produces a summary of the contents of the graphics
database for a graphics device, and/or permits a picture specified by
its order in the list to be made the new current picture. The list may
either be reported or written to a text file.
The headed list has one line per picture. Each line comprises a
reference number; the picture's name, comment (up to 24 characters),
and label; and a flag to indicate whether or not there is a reference
data object associated with the picture. A `C' in the first column
indicates that the picture that was current when this application was
invoked. In the text file, because there is more room, the name of the
reference object is given (up to 64 characters) instead of the
reference flag. Pictures are listed in chronological order of their
creation.


Usage
~~~~~


::

    
       piclist [name] [logfile] [device] picnum=?
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation. [The current graphics device]



LOGFILE = FILENAME (Write)
``````````````````````````
The name of the text file in which the list of pictures will be made.
A null string (!) means the list will be reported to you. The
suggested default is the current value. [!]



NAME = LITERAL (Read)
`````````````````````
Only pictures of this name are to be selected. A null string (!) or
blanks means that pictures of all names may be selected. [!]



PICNUM = LITERAL (Read)
```````````````````````
The reference number of the picture to be made the current picture
when the application exits. PICNUM="Last" selects the last picture in
the database. Parameter PICNUM is not accessed if the list is written
to the text file. A null (!) or any other error causes the current
picture on entry to be current again on exit. The suggested default is
null.



Examples
~~~~~~~~
piclist
This reports all the pictures in the graphics database for the current
graphics device.
piclist device=ps_l
This reports all the pictures in the graphics database for the ps_l
device.
piclist data
This reports all the DATA pictures in the graphics database for the
current graphics device.
piclist data logfile=datapic.dat
This lists all the DATA pictures in the graphics database for the
current graphics device into the text file datapic.dat.
piclist frame picnum=5
This selects the fifth most ancient FRAME picture (in the graphics
database for the current graphics device) as the current picture. The
pictures are not listed.
piclist picnum=last
This makes the last picture in the graphics database for the current
graphics device current. The pictures are not listed.



Notes
~~~~~


+ The list is not reported to the user when PICNUM is specified on the
  command line. This feature is useful where a procedure just wants to
  select a new current picture (hiding the details from the user). A new
  current picture cannot be selected with text-file output, and so the
  presence of PICNUM on the command line does not affect writing to a
  text file.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PICBASE, PICDATA, PICEMPTY, PICENTIRE, PICFRAME, PICIN,
PICLAST, PICSEL, PICVIS.


Timing
~~~~~~
The execution time is approximately proportional to the number of
pictures in the database for the chosen graphics device. Selecting
only a subset by name is slightly faster.


Copyright
~~~~~~~~~
Copyright (C) 1991-1993 Science & Engineering Research Council.
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ Assumes that there are no more than 9999 pictures in the database.




