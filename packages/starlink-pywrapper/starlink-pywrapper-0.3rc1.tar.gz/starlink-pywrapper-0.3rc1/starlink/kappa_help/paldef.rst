

PALDEF
======


Purpose
~~~~~~~
Loads the default palette to a colour table


Description
~~~~~~~~~~~
This application loads the standard palette of colours to fill the
portion of the current image display's colour table which is reserved
for the palette. The palette comprises 16 colours and is intended to
provide coloured annotations, borders, axes, graphs etc. that are
unaffected by changes to the lookup table used for images.
Pen 0 (the background colour) and pen 1 (the foreground colour) are
set to the default values for the specified graphics device. Thus they
may be white on black for an X window, but black on white for a
printer. The other colours in the standard palette are:


+ 2: Red
+ 3: Green
+ 4: Blue
+ 5: Yellow
+ 6: Magenta
+ 7: Cyan
+ 8 to 15: Black




Usage
~~~~~


::

    
       paldef [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
Name of the image display to be used. [Current image-display device]



Examples
~~~~~~~~
paldef
This loads the standard palette into the reserved portion of the
colour table of the current image display.
paldef xwindows
This loads the standard palette into the reserved portion of the
colour table of the xwindows device.



Notes
~~~~~


+ The effects of this command will only be immediately apparent when
  run on X windows which have 256 colours (or other similar pseudocolour
  devices). On other devices (for instance, X windows with more than 256
  colours) the effects will only become apparent when subsequent
  graphics applications are run.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PALENTRY, PALREAD, PALSAVE.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1994 Science & Engineering Research Council.
Copyright (C) 1998-1999, 2004 Central Laboratory of the Research
Councils. All Rights Reserved.


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


