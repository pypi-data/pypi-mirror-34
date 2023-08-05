

FTS2GAIA
========


Purpose
~~~~~~~
Display in-band FTS-2 spectrum in gaia


Description
~~~~~~~~~~~
Display those frames of an FTS-2 spectrum which fall within the band-
pass. For 850 um, this band is between 11.2 and 12.2 cm^-1 wave
numbers, and for 450 um, it is between 22.1 and 23.3 cm^-1 wave
numbers. This translates to the peak of the spectrum of the target,
found near the middle of the sensor array plus and minus some number
of frames corresponding to the desired portion of the band pass.


Usage
~~~~~


::

    
       fts2gaia in
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The NDF FTS-2 spectrum file to be displayed.



Copyright
~~~~~~~~~
Copyright (C) 2013 University of Lethbridge. All Rights Reserved.


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


