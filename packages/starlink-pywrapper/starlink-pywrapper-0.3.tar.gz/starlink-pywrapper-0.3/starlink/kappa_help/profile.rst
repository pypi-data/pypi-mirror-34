

PROFILE
=======


Purpose
~~~~~~~
Creates a 1-dimensional profile through an N-dimensional NDF


Description
~~~~~~~~~~~
This application samples an N-dimensional NDF at a set of positions,
producing a one-dimensional output NDF containing the sample values.
Nearest-neighbour interpolation is used.
The samples can be placed at specified positions within the input NDF,
or can be spaced evenly along a poly-line joining a set of vertices
(see parameter MODE). The positions of the samples may be saved in an
output positions list (see parameter OUTCAT).


Usage
~~~~~


::

    
       profile in out { start finish [nsamp]
                      { incat=?
                      mode
       



ADAM parameters
~~~~~~~~~~~~~~~



CATFRAME = LITERAL (Read)
`````````````````````````
A string determining the co-ordinate Frame in which positions are to
be stored in the output catalogue associated with parameter OUTCAT.
The string supplied for CATFRAME can be one of the following options.


+ A Domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame.
+ An IRAS90 Sky Co-ordinate System (SCS) values such as EQUAT(J2000)
  (see SUN/163).

If a null (!) value is supplied, the positions will be stored in the
current SKY Frame. [!]



CATEPOCH = DOUBLE PRECISION (Read)
``````````````````````````````````
The epoch at which the sky positions stored in the output catalogue
were determined. It will only be accessed if an epoch value is needed
to qualify the co-ordinate Frame specified by COLFRAME. If required,
it should be given as a decimal years value, with or without decimal
places ("1996.8", for example). Such values are interpreted as a
Besselian epoch if less than 1984.0 and as a Julian epoch otherwise.



FINISH = LITERAL (Read)
```````````````````````
The co-ordinates of the last sample in the profile, in the current co-
ordinate Frame of the NDF (supplying ":" will display details of the
required co-ordinate Frame). The position should be supplied as a list
of formatted axis values separated by spaces. This parameter is only
accessed if parameter MODE is set to "Curve" and a null (!) value is
given for INCAT. If the last (top right) pixel in the NDF has valid
co-ordinates in the current co-ordinate Frame of the NDF, then these
co-ordinates will be used as the suggested default. Otherwise there
will be no suggested default.



GEODESIC = LOGICAL (Read)
`````````````````````````
If TRUE then the line segments which form the profile will be geodesic
curves within the current co-ordinate Frame of the NDF. Otherwise, the
line segments are simple straight lines. This parameter is only
accessed if parameter MODE is set to "Curve".
As an example, consider a profile consisting of a single line segment
which starts at RA=0h DEC=+80d and finishes at RA=12h DEC=+80d. If
GEODESIC is FALSE, the line segment will be a line of constant
declination, i.e. the "straight" line from the position (0,80) to the
position (12,80), passing through (1,80), (2,80), etc. If GEODESIC is
TRUE, then the line segment will be the curve of shortest distance on
the celestial sphere between the start and end. In this particaular
case, this will be a great circle passing through the north celestial
pole. [FALSE]



IN = NDF (Read)
```````````````
Input NDF structure containing the data to be profiled.



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a set of vertices or sample positions defining
the required profile. The file should be in the format of a "positions
list" such as produced by applications CURSOR and LISTMAKE. If a null
value (!) is given then parameters START and FINISH will be used to
obtain the vertex positions. If parameter MODE is given the value
"Curve", then the parameter INCAT is only accessed if a value is given
for it on the command line (otherwise a null value is assumed).



MODE = LITERAL (Read)
`````````````````````
The mode by which the sample positions are selected. The alternatives
are listed below.


+ "Curve" -- The samples are placed evenly along a curve specified by
a set of vertices obtained from the user. The line segments joining
these vertices may be linear or geodesic (see parameter GEODESIC).
Multiple vertices may be supplied using a text file (see parameter
INCAT). Alternatively, a single line segment can be specified using
parameters START and FINISH. The number of samples to take along the
curve is specified by parameter NSAMP.
+ "Points" -- The positions at which samples should be taken are given
  explicitly by the user in a text file (see parameter INCAT). No other
  sample positions are used.

["Curve"]



NSAMP = INTEGER (Read)
``````````````````````
The number of samples required along the length of the profile. The
first sample is at the first supplied vertex, and the last sample is
at the last supplied vertex. The sample positions are evenly spaced
within the current co-ordinate Frame of the NDF. If a null value is
supplied, a default value is used equal to one more than the length of
the profile in pixels. This is only accessed if parameter MODE is
given the value "Curve". [!]



OUT = NDF (Write)
`````````````````
The output NDF. This will be one-dimensional with length specified by
parameter NSAMP.



OUTCAT = FILENAME (Write)
`````````````````````````
An output positions list in which to store the sample positions. This
is the name of a catalogue which can be used to communicate positions
to subsequent applications. It includes information describing the
available WCS co-ordinate Frames as well as the positions themselves.
If a null value is supplied, no output positions list is produced. See
also parameter CATFRAME. [!]



START = LITERAL (Read)
``````````````````````
The co-ordinates of the first sample in the profile, in the current
co-ordinate Frame of the NDF (supplying ":" will display details of
the required co-ordinate Frame). The position should be supplied as a
list of formatted axis values separated by spaces. This parameter is
only accessed if parameter MODE is set to "Curve" and a null (!) value
is given for INCAT. If the first (bottom left) pixel in the NDF has
valid co-ordinates in the current co-ordinate Frame of the NDF, then
these co-ordinates will be used as the suggested default. Otherwise
there will be no suggested default.



Examples
~~~~~~~~
profile my_data prof "0 0" "100 100" 40 outcat=samps
Create a one-dimensional NDF called prof, holding a profile of the
data values in the input NDF my_data along a profile starting at pixel
co-ordinates [0.0,0.0] and ending at pixel co-ordinates [100.0,100.0].
The profile consists of forty samples spread evenly (in the pixel co-
ordinate Frame) between these two positions. This example assumes that
the current co-ordinate Frame in the NDF my_data represents pixel co-
ordinates. This can be ensured by issuing the command "wcsframe
my_data pixel" before running profile. A FITS binary catalogue is
created called samps.FIT containing the positions of all samples in
the profile, together with information describing all the co-ordinate
Frames in which the positions of the samples are known. This file may
be examined using application LISTSHOW.
profile my_data prof "15:32:47 23:40:08" "15:32:47 23:42"
This example is the same as the last one except that it is assumed
that the current co-ordinate Frame in the input NDF my_data is an
equatorial (RA/DEC) system. It creates a one-dimensional profile
starting at RA=15:32:47 DEC=23:40:08, and ending at the same RA and
DEC=23:42:00. The number of points in the profile is determined by the
resolution of the data.
profile allsky prof incat=prof_path npoint=200 geodesic
outcat=aa.fit This examples creates a profile of the NDF allsky
through a set of points given in a FITS binary catalogue called
prof_path.FIT. Such catalogues can be created (for example) using
application CURSOR. Each line segment is a geodesic curve. The profile
is sampled at 200 points. The samples positions are written to the
output positions list aa.fit.
profile allsky2 prof2 mode=point incat=aa.fit
This examples creates a profile of the NDF allsky2 containing samples
at the positions given in the positions list aa.fit. Thus, the
profiles created by this example and the previous example will sample
the two images allsky and allsky2 at the same positions and so can be
compared directly.



Notes
~~~~~


+ This application uses the conventions of the CURSA package (SUN/190)
  for determining the formats of input and output positions list
  catalogues. If a file type of .fit is given, then the catalogue is
  assumed to be a FITS binary table. If a file type of .txt is given,
  then the catalogue is assumed to be stored in a text file in "Small
  Text List" (STL) format. If no file type is given, then ".fit" is
  assumed.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: LINPLOT, CURSOR, LISTMAKE, LISTSHOW; CURSA: XCATVIEW.


Copyright
~~~~~~~~~
Copyright (C) 1998-1999, 2001, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. All Rights Reserved.


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


+ This routine correctly processes the DATA, VARIANCE, WCS, LABEL,
TITLE, and UNITS components of the NDF.
+ All non-complex numeric data types can be handled. Only double-
  precision floating-point data can be processed directly. Other non-
  complex data types will undergo a type conversion before the profile
  is produced.




