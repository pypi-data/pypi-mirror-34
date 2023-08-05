

FINDSLICES
==========


Purpose
~~~~~~~
Find time slices that are centred close to a given sky position


Description
~~~~~~~~~~~
This application lists the time-slices within a given set of time-
series files for which the telescope was close to a specified position
on the sky. For each such position, the file, time slice index and
distance (in arc-seconds) is displayed on the screen.
Each time the telescope scans past the supplied position, a continuous
group of time slices will fall within the specified radius of the
given position. By default, only the closest time slice within each
such group is displayed. This can be changed using parameter CLOSEST.


ADAM parameters
~~~~~~~~~~~~~~~



CLOSEST = _LOGICAL (Read)
`````````````````````````
If TRUE, then only a single time slice (the closest) is displayed for
each pass of the telescope past the specified position. If FALSE, then
all time slices within the specified radius of the specified positiopn
are displayed. [TRUE]



FRAME = NDF (Read)
``````````````````
The position specified by parameters XPOS and YPOS is assumed to be in
the current WCS Frame of the NDF supplied for parameter FRAME. If a
null (!) value is supplied for FRAME, the position is assumed to be in
the tracking system of the first NDF supplied for parameter IN. [!]



IN = NDF (Read)
```````````````
Input time-series file(s).



RADIUS = _DOUBLE (Read)
```````````````````````
The radius of the search circle, in ars-seconds. [300]



XPOS = LITERAL (Read)
`````````````````````
The first axis value at the search position. This should be a
formatted value for the first axis of the Frame specified by parameter
FRAME.



YPOS = LITERAL (Read)
`````````````````````
The second axis value at the search position. This should be a
formatted value for the second axis of the Frame specified by
parameter FRAME.



Copyright
~~~~~~~~~
Copyright (C) 2013 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


