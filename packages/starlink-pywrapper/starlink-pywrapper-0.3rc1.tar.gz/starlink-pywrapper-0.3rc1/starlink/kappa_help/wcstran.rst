

WCSTRAN
=======


Purpose
~~~~~~~
Transform a position from one NDF co-ordinate Frame to another


Description
~~~~~~~~~~~
This application transforms a position from one NDF co-ordinate Frame
to another. The input and output Frames may be chosen freely from the
Frames available in the WCS component of the supplied NDF. The
transformed position is formatted for display and written to the
screen and also to an output parameter.


Usage
~~~~~


::

    
       wcstran ndf posin framein [frameout]
       



ADAM parameters
~~~~~~~~~~~~~~~



EPOCHIN = _DOUBLE (Read)
````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
Parameter FRAMEIN) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky position was determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



EPOCHOUT = _DOUBLE (Read)
`````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
Parameter FRAMEOUT) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the
transformed sky position is required. It should be given as a decimal
years value, with or without decimal places ("1996.8" for example).
Such values are interpreted as a Besselian epoch if less than 1984.0
and as a Julian epoch otherwise.



FRAMEIN = LITERAL (Read)
````````````````````````
A string specifying the co-ordinate Frame in which the input position
is supplied (see Parameter POSIN). If a null parameter value is
supplied, then the current Frame in the NDF is used. The string can be
one of the following:


+ A domain name such as SKY, AXIS, PIXEL, etc. The two "pseudo-
domains" WORLD and DATA may be supplied and will be translated into
PIXEL and AXIS respectively, so long as the WCS component of the NDF
does not contain Frames with these domains.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).





FRAMEOUT = LITERAL (Read)
`````````````````````````
A string specifying the co-ordinate Frame in which the transformed
position is required. If a null parameter value is supplied, then the
current Frame in the NDF is used. The string can be one of the
following:


+ A domain name such as SKY, AXIS, PIXEL, etc. The two "pseudo-
domains" WORLD and DATA may be supplied and will be translated into
PIXEL and AXIS respectively, so long as the WCS component of the NDF
does not contain Frames with these domains.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95). [!]





NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure containing the required co-ordinate Frames.



POSIN = LITERAL (Read)
``````````````````````
The co-ordinates of the position to be transformed, in the co-ordinate
Frame specified by Parameter FRAMEIN (supplying a colon ":" will
display details of the required co-ordinate Frame). The position
should be supplied as a list of formatted axis values separated by
spaces or commas.



POSOUT = LITERAL (Write)
````````````````````````
The formatted co-ordinates of the transformed position, in the co-
ordinate Frame specified by Parameter FRAMEOUT. The position will be
stored as a list of formatted axis values separated by spaces or
commas.



SKYDEG = _INTEGER (Read)
````````````````````````
If greater than zero, the values for any celestial longitude or
latitude axes are formatted as decimal degrees, irrespective of the
Format attributes in the NDF WCS component. The supplied integer value
indicates the number of decimal places required. If the SKYDEG value
is less than or equal to zero, the formats specified by the Format
attributes in the WCS component are honoured. [0]



Examples
~~~~~~~~
wcstran m51 "100.1 21.5" pixel
This transforms the pixel position "100.1 21.5" into the current co-
ordinate Frame of the NDF m51. The results are displayed on the screen
and written to the output Parameter POSOUT.
wcstran m51 "1:00:00 -12:30" equ(B1950) pixel
This transforms the RA/DEC position "1:00:00 -12:30" (referred to the
J2000 equinox) into pixel co-ordinates within the NDF m51. The results
are written to the output Parameter POSOUT.
wcstran m51 "1:00:00 -12:30" equ(B1950) equ(j2000)
This is like the previous example except that the position is
transformed into RA/DEC referred to the B1950 equinox, instead of
pixel co-ordinates.



Notes
~~~~~


+ The transformed position is not written to the screen when the
  message filter environment variable MSG_FILTER is set to QUIET. The
  creation of the output Parameter POSOUT is unaffected by MSG_FILTER.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LISTMAKE, LISTSHOW, WCSFRAME, NDFTRACE, WCSATTRIB


Copyright
~~~~~~~~~
Copyright (C) 1998-1999 Central Laboratory of the Research Councils.
Copyright (C) 2009 Science and Technology Facilities Council. All
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


