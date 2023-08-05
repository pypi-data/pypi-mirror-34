

PALSAVE
=======


Purpose
~~~~~~~
Saves the current palette of a colour table to an NDF


Description
~~~~~~~~~~~
This application reads the palette portion of the current image
display's colour table and saves it in an NDF. The palette comprises
16 colours and is intended to provide coloured annotations, borders,
axes, graphs etc. that are unaffected by changes to the lookup table
used for images. Thus once you have established a palette of colours
you prefer, it is straightforward to recover the palette at a future
time.


Usage
~~~~~


::

    
       palsave palette [device] [title]
       



ADAM parameters
~~~~~~~~~~~~~~~



DEVICE = DEVICE (Read)
``````````````````````
Name of the image display to be used. [Current image-display device]



PALETTE = NDF (Write)
`````````````````````
The NDF in which the current colour-table reserved pens are to be
stored. Thus if you have created non-standard colours for annotation,
doodling, colour of axes etc. they may be stored for future use.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. ["KAPPA - Palsave"]



Examples
~~~~~~~~
palsave rustic
This saves the palette of the colour table of the current image
display into the NDF called RUSTIC.
palsave hitec xwindows title="Hi-tech-look palette"
This saves the palette of the colour table of the xwindows device in
the NDF called hitec. The NDF has a title called "Hi-tech-look
palette".



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PALDEF, PALENTRY, PALREAD.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1999, 2004 Central Laboratory of the Research Councils. All Rights
Reserved.


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


