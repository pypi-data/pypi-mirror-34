

WCSSLIDE
========


Purpose
~~~~~~~
Applies a translational correction to the WCS in an NDF


Description
~~~~~~~~~~~
This application modifies the WCS information in an NDF so that the
WCS position of a given pixel is moved by specified amount along each
WCS axis. The shifts to use are specified either by an absolute offset
vector given by the ABS parameter or by the difference between a
fiducial point and a standard object given by the FID and OBJ
parameters respectively. In each case the co-ordinates are specified
in the NDF's current WCS co-ordinate Frame.


Usage
~~~~~


::

    
       wcsslide ndf abs
       



ADAM parameters
~~~~~~~~~~~~~~~



ABS( ) = _DOUBLE (Read)
```````````````````````
Absolute shift for each WCS axis. The number of values supplied must
match the number of WCS axes in the NDF. It is only used if
STYPE="Absolute". Offsets for celestial longitude and latitude axes
should be specified in arcseconds. Offsets for all other types of axes
should be given directly in the units of the axis.



FID = LITERAL (Read)
````````````````````
A comma-separated list of formatted axis values giving the position of
the fiducial point in WCS co-ordinates. The number of values supplied
must match the number of WCS axes in the NDF. It is only used if
STYPE="Relative".



NDF = NDF (Update)
``````````````````
The NDF to be translated.



OBJ = LITERAL (Read)
````````````````````
A comma-separated list of formatted axis values giving the position of
the standard object in WCS co-ordinates. The number of values supplied
must match the number of WCS axes in the NDF. It is only used if
STYPE="Relative".



STYPE = LITERAL (Read)
``````````````````````
The sort of shift to be used. The choice is "Relative" or "Absolute".
["Absolute"]



Examples
~~~~~~~~
wcsslide m31 [32,23]
The (RA,Dec) axes in the NDF m31 are shifted by 32 arcseconds in right
ascension and 23 arcseconds in declination.
wcsslide speca stype=rel fid=211.2 obj=211.7
The spectral axis in the NDF speca (which measures frequency in GHz),
is shifted by 0.5 GHz (i.e. 211.7--211.2).
wcsslide speca stype=abs abs=0.5
This does just the same as the previous example.



Notes
~~~~~


+ The correction is affected by translating pixel co-ordinates by a
  constant amount before projection them into WCS co-ordinates.
  Therefore, whilst the translation will be constant across the array in
  pixel co-ordinates, it may vary in WCS co-ordinates depending on the
  nature of the pixel->WCS transformation. The size of the translation
  in pixel co-ordinates is chosen in order to produce the required shift
  in WCS co-ordinates at the OBJ position (if STYPE is "Relative"), or
  at the array centre (if STYPE is "Absolute").




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SLIDE.


Copyright
~~~~~~~~~
Copyright (C) 2008 Science & Technology Facilities Council. All Rights
Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ There can be an arbitrary number of NDF dimensions.




