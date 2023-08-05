

LUTSAVE
=======


Purpose
~~~~~~~
Saves the current colour table of an image-display device in an NDF


Description
~~~~~~~~~~~
This routine saves the colour table of a nominated image display to an
NDF LUT file and/or a text file.


Usage
~~~~~


::

    
       lutsave lut [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The name of the image-display device whose colour table is to be
saved. [Current image display]



FULL = _LOGICAL (Read)
``````````````````````
If TRUE the whole colour-table for the device is stored including the
reserved pens. This is necessary to save a colour table written by
another package that does not reserve colour indices. For colour
tables produced by KAPPA this should be FALSE. [FALSE]



LOGFILE = FILENAME (Write)
``````````````````````````
The name of a text file to receive the formatted values in the colour
table. Each line i the file contains the red, green and blue
intensities for a single pen, separated by spaces. A null string (!)
means that no file is created. [!]



LUT = NDF (Write)
`````````````````
The output NDF into which the colour table is to be stored. Its second
dimension equals the number of colour-table entries that are stored.
This will be less than the total number of colour indices on the
device if FULL is FALSE. No NDF is created if a null (!) value is
given.



TITLE = LITERAL (Read)
``````````````````````
The title for the output NDF. ["KAPPA - Lutsave"]



Examples
~~~~~~~~
lutsave pizza
This saves the current colour table on the current image-display
device to an NDF called pizza.
lutsave redshift full
This saves in full the current colour table on the current image-
display device to an NDF called redshift.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LUTREAD, LUTABLE, LUTEDIT, LUTVIEW.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
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


