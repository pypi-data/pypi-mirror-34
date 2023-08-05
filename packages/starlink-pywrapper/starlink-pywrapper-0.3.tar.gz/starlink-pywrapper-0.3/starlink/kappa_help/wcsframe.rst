

WCSFRAME
========


Purpose
~~~~~~~
Change the current co-ordinate Frame in the WCS component of an NDF


Description
~~~~~~~~~~~
This application displays the current co-ordinate Frame associated
with an NDF and then allows the user to specify a new Frame. The
current co-ordinate Frame determines the co-ordinate system in which
positions within the NDF will be expressed when communicating with the
user.
Having selected a new current co-ordinate Frame, its attributes (such
the specific system it uses to represents points within its Domain,
its units, etc.) can be changed using KAPPA command WCSATTRIB.


Usage
~~~~~


::

    
       wcsframe ndf frame epoch
       



ADAM parameters
~~~~~~~~~~~~~~~



EPOCH = _DOUBLE (Read)
``````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter FRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



FRAME = LITERAL (Read)
``````````````````````
A string specifying the new co-ordinate Frame. If a null parameter
value is supplied, then the current Frame is left unchanged. The
suggested default is the Domain (or index if the Domain is not set) of
the current Frame. The string can be one of the following:


+ A domain name such as SKY, SPECTRUM, AXIS, PIXEL, etc. The two
"pseudo-domains" WORLD and DATA may be supplied and will be translated
into PIXEL and AXIS respectively, so long as the WCS component of the
NDF does not contain Frames with these domains.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95). Using an SCS value is
  equivalent to specifying "SKY" for this parameter and then setting the
  System attribute (to "FK5", "Galactic", etc.) using KAPPA command
  WCSATTRIB. The specific system used to describe positions in other
  Domains (SPECTRUM, for instance) must be set using WCSATTRIB.





NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure in which the current co-ordinate Frame is to be
modified.



Examples
~~~~~~~~
wcsframe m51 pixel
This chooses pixel co-ordinates for the current co-ordinate Frame in
the NDF m51.
wcsframe m51 sky
This chooses celestial co-ordinates for the current co-ordinate Frame
in the NDF m51 (if available). The specific celestial co-ordinate
system (FK5, Galactic, etc.) will depend on the contents of the WCS
component of the NDF, but may be changed by setting a new value for
the System attribute using the WCSATTRIB command.
wcsframe m51 spectrum
This chooses spectral co-ordinates for the current co-ordinate Frame
in the NDF m51 (if available). The specific spectral co-ordinate
system (wavelength, frequency, etc) will depend on the contents of the
WCS component of the NDF, but may be changed by setting a new value
for the System attribute using the WCSATTRIB command.
wcsframe m51 equ(J2000) epoch=1998.2
This chooses equatorial (RA/DEC) co-ordinates referred to the equinox
at Julian epoch 2000.0 for the current co-ordinate Frame in the NDF
m51. The positions were determined at the Julian epoch 1998.2 (this is
needed to correct positions for the fictitious proper motions which
may be introduced when converting between different celestial co-
ordinate systems).
wcsframe m51 2
This chooses the second co-ordinate Frame in the WCS component of the
NDF.
wcsframe m51 data
This chooses a co-ordinate Frame with domain DATA if one exists, or
the AXIS co-ordinate Frame otherwise.
wcsframe m51 world
This chooses a co-ordinate Frame with domain WORLD if one exists, or
the PIXEL co-ordinate Frame otherwise.



Notes
~~~~~


+ The current co-ordinate Frame in the supplied NDF is not displayed
if a value is assigned to parameter FRAME on the command line.
+ This routine may add a new co-ordinate Frame into the WCS component
of the NDF.
+ The NDFTRACE command can be used to examine the co-ordinate Frames
  in the WCS component of an NDF.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFTRACE, WCSREMOVE, WCSCOPY, WCSATTRIB


Copyright
~~~~~~~~~
Copyright (C) 2011 Science & Technology Facilities Council. Copyright
(C) 1998-1999 Central Laboratory of the Research Councils. All Rights
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


