

PICSEL
======


Purpose
~~~~~~~
Selects a graphics-database picture by its label


Description
~~~~~~~~~~~
This application selects by label a graphics-database picture of a
specified device. If such a picture is found then it becomes the
current picture on exit, otherwise the input picture remains current.
Labels in the database are stored in the case supplied when they were
created. However, the comparisons of the label you supply with the
labels in the database are made in uppercase, and leading spaces are
ignored.
Should the label not be found the current picture is unchanged.


Usage
~~~~~


::

    
       picsel label [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The graphics device. [Current graphics device]



LABEL = LITERAL (Read)
``````````````````````
The label of the picture to be selected.



Examples
~~~~~~~~
picsel GALAXY
This makes the picture labelled "GALAXY" the current picture on the
current graphics device. Should there be no picture of this name, the
current picture is unchanged.
picsel A3 xwindows
This makes the picture labelled "A3" the current picture on the
xwindows device. Should there be no picture of this name, the current
picture is unchanged.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PICDATA, PICDEF, PICEMPTY, PICENTIRE, PICFRAME, PICLABEL,
PICLAST, PICVIS.


Copyright
~~~~~~~~~
Copyright (C) 1990-1991 Science & Engineering Research Council.
Copyright (C) 2004 Central Laboratory of the Research Councils. All
Rights Reserved.


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


