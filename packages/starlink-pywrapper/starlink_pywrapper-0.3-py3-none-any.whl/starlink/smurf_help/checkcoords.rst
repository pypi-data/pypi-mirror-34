

CHECKCOORDS
===========


Purpose
~~~~~~~
Check for discrepancies between AZEL and TRACKING coordinates


Description
~~~~~~~~~~~
This routine checks that the AZEL boresight positions stored in the
TCS_AZ_AC1/2 arrays in the JCMTSTATE extension of the supplied input
NDF are in agreement with the corresponding TRACKING positions given
by the TCS_TR_AC1/2 arrays. It does this by using AST to convert each
TCS_AZ_AC1/2 into the tracking system and then finding the arc-
distance from this converted position to the corresponding
TCS_TR_AC1/2 position. This is done for every time slice, and the
statistics of the resulting separations are displayed, in arc-seconds.
A warning message is reported if any separations larger than 3 arc-
seconds are found.


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The time series to be checked.



Copyright
~~~~~~~~~
Copyright (C) 2017 East Asian Observatory. Copyright (C) 2013 Science
and Technology Facilities Council. All Rights Reserved.


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


