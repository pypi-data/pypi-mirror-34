

PICLABEL
========


Purpose
~~~~~~~
Labels the current graphics-database picture


Description
~~~~~~~~~~~
This application annotates the current graphics-database picture of a
specified device with a label you define. This provides an easy-to-
remember handle for selecting pictures in subsequent processing.


Usage
~~~~~


::

    
       piclabel label [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The graphics device. [Current graphics device]



LABEL = LITERAL (Read)
``````````````````````
The label to be given to the current picture. It is limited to 15
characters, but may be in mixed case. If it is null (!) a blank label
is inserted in the database.



Examples
~~~~~~~~
piclabel GALAXY
This makes the current picture of the current graphics device have a
label of "GALAXY".
piclabel A3 xwindows
This labels the current xwindows picture "A3".



Notes
~~~~~
The label must be unique for the chosen device. If the new label
clashes with an existing one, then the existing label is deleted.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PICDEF, PICLIST, PICSEL.


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


