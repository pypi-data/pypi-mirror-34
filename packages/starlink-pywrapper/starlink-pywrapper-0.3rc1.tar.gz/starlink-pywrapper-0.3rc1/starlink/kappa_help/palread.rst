

PALREAD
=======


Purpose
~~~~~~~
Fills the palette of a colour table from an NDF


Description
~~~~~~~~~~~
This application reads a palette of colours from an NDF, stored as
red, green and blue intensities, to fill the portion of the current
image display's colour table which is reserved for the palette. The
palette comprises 16 colours and is intended to provide coloured
annotations, borders, axes, graphs etc. that are unaffected by changes
to the lookup table used for images.


Usage
~~~~~


::

    
       palread palette [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
Name of the image display to be used. [Current image-display device]



PALETTE = NDF (Read)
````````````````````
The name of the NDF containing the palette of reserved colours as its
data array. The palette must be 2-dimensional, the first dimension
being 3, and the second 16. If the second dimension is greater than 16
only the first 16 colours are used; if it has less than 16 just fill
as much of the palette as is possible starting from the first colour.
The palette's values must lie in the range 0.0--1.0.



Examples
~~~~~~~~
palread rustic
This loads the palette stored in the NDF called rustic into the
reserved portion of the colour table of the current image display.
palread rustic xwindows
This loads the palette stored in the NDF called rustic into the
reserved portion of the colour table of the xwindows device.



Notes
~~~~~


+ The effects of this command will only be immediately apparent when
  run on X windows which have 256 colours (or other similar pseudocolour
  devices). On other devices (for instance, X windows with more than 256
  colours) the effects will only become apparent when subsequent
  graphics applications are run.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PALDEF, PALENTRY, PALSAVE.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1998-1999, 2004 Central Laboratory of the Research Councils. All
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


