

PALENTRY
========


Purpose
~~~~~~~
Enters a colour into an image display's palette


Description
~~~~~~~~~~~
This application obtains a colour and enters it into the palette
portion of the current image display's colour table. The palette
comprises up to 16 colours and is intended to provide coloured
annotations, borders, axes, graphs etc. that are unaffected by changes
to the lookup table used for images.
A colour is specified either by the giving the red, green, blue
intensities; or named colours.


Usage
~~~~~


::

    
       palentry palnum colour [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



COLOUR() = LITERAL (Read)
`````````````````````````
A colour to be added to the palette at the entry given by parameter
PALNUM. It is one of the following options.
o A named colour from the standard colour set, which may be
abbreviated. If the abbreviated name is ambiguous the first match (in
alphabetical order) is selected. The case of the name is ignored. Some
examples are "Pink", "Yellow", "Aquamarine", and "Orchid".
o Normalised red, green, and blue intensities separated by commas or
spaces. Each value must lie in the range 0.0--1.0. For example,
"0.7,0.7,1.0" would give a pale blue.
o An HTML colour code such as #ff002d.



DEVICE = DEVICE (Read)
``````````````````````
Name of the image display to be used. [Current image-display device]



PALNUM = _INTEGER (Read)
````````````````````````
The number of the palette entry whose colour is to be modified. PALNUM
must lie in the range zero to the minimum of 15 or the number of
colour indices minus one. The suggested default is 1.



Examples
~~~~~~~~
palentry 5 gold
This makes palette entry number 5 have the colour gold in the reserved
portion of the colour table of the current image display.
palentry 12 [1.0,1.0,0.3] xwindows
This makes the xwindows device's palette entry number 12 have a pale-
yellow colour.



Notes
~~~~~


+ The effects of this command will only be immediately apparent when
  run on X windows which have 256 colours (or other similar pseudocolour
  devices). On other devices (for instance, X windows with more than 256
  colours) the effects will only become apparent when subsequent
  graphics applications are run.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PALDEF, PALREAD, PALSAVE.


Copyright
~~~~~~~~~
Copyright (C) 1991-1992 Science & Engineering Research Council.
Copyright (C) 1998-1999, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. All Rights Reserved.


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


