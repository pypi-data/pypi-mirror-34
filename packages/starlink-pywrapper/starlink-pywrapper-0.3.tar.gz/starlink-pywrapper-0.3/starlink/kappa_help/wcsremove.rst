

WCSREMOVE
=========


Purpose
~~~~~~~
Remove co-ordinate Frames from the WCS component of an NDF


Description
~~~~~~~~~~~
This application allows you to remove one or more co-ordinate Frames
from the WCS component in an NDF. The indices of any remaining Frames
are "shuffled down" to fill the gaps left by the removed Frames.


Usage
~~~~~


::

    
       wcsremove ndf frames
       



ADAM parameters
~~~~~~~~~~~~~~~



FRAMES() = LITERAL (Read
````````````````````````
Specifies the Frame(s) to be removed. It can be a list of indices
(within the WCS component of the supplied NDF) or list of Domain
names. If one or more Domain name are specified, any WCS Frames which
have a matching Domain are removed. If a list of indices is supplied,
any indices outside the range of the available Frames are ignored.
Single Frames or a set of adjacent Frames may be specified, e.g.
typing [4,6-9,12,14-16] will remove Frames 4,6,7,8,9,12,14,15,16.
(Note that the brackets are required to distinguish this array of
characters from a single string including commas. The brackets are
unnecessary when there only one item.) If you wish to remove all the
files enter the wildcard *. 5-* will remove from 5 to the last Frame.



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure.



Examples
~~~~~~~~
wcsremove m51 "SKY,SKY-SPECTRUM"
This removes any Frames that have Domain SKY or SKY-SPECTRUM.
wcsremove m51 "3-5"
This removes Frames 3, 4 and 5 from the NDF "m51". Any remaining
Frames with indices higher than 5 will be re-numbered to fill the gaps
left by the removed Frames (i.e. the original Frame 6 will become
Frame 3, etc).



Notes
~~~~~


+ The Frames within the WCS component of an NDF may be examined using
  application NDFTRACE.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFTRACE, WCSADD, WCSFRAME, WCSATTRIB, WCSCOPY


Copyright
~~~~~~~~~
Copyright (C) 1998-2000 Central Laboratory of the Research Councils.
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


