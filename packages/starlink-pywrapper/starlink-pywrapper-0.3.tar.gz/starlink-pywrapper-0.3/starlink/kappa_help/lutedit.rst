

LUTEDIT
=======


Purpose
~~~~~~~
Create or edit an image-display colour lookup table


Description
~~~~~~~~~~~
This application allows a lookup table to be created or edited
interactively. The process is controlled through a graphical user
interface which presents curves of intensity against pen number, and
allows the user to change them in various ways. A specified image is
displayed as part of the interface in order to see the effects of the
changes. A histogram of pen values is also included. The colour of
each pen can be displayed either as red, green and blue intensity, or
as hue, saturation and value. More information on the use of the GUI
is available through the Help menu within the GUI.


Usage
~~~~~


::

    
       lutedit lut image device
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
The name of an image display device. If a null value is supplied for
parameter LUT, then the current LUT associated with the specified
device will be loaded into the editor initially. On exit, the final
contents of the editor (if saved) are established as the current LUT
for the specified device. [Current image-display device]



LUT = NDF (Read)
````````````````
Name of an exiting colour table to be edited. This should be an NDF
containing an array of red, green and blue intensities. The NDF must
be 2-dimensional, the first dimension being 3, and the second being
arbitrary. The method used to compress or expand the colour table if
the second dimension is different from the number of unreserved colour
indices is controlled by the "Interpolation" option in the GUI. If LUT
is null (!) the current KAPPA colour table for the device specified by
parameter DEVICE is used. [!]



IMAGE = NDF (Read)
``````````````````
Input NDF data structure containing the image to be displayed to show
the effect of the created colour table. If a null value is supplied a
default image is used.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LUTABLE, LUTREAD, LUTSAVE, LUTVIEW, PALREAD, PALSAVE; Figaro:
COLOUR.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2011 Science and Technology Facilities Council. All
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


