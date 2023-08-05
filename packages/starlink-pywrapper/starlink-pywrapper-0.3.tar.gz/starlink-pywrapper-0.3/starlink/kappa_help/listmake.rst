

LISTMAKE
========


Purpose
~~~~~~~
Creates a catalogue holding a positions list


Description
~~~~~~~~~~~
This application creates a catalogue containing a list of positions
supplied by the user, together with information describing the co-
ordinate Frames in which the positions are defined. Integer position
identifiers which allow positions to be distinguished are also stored
in the catalogue. The catalogue may be manipulated using the CURSA
package (SUN/190), and is stored in either FITS binary format or the
"Small Text List" (STL) format defined by CURSA.
If an NDF is specified using parameter NDF, then the positions should
be given in the current co-ordinate Frame of the NDF. Information
describing the co-ordinate Frames available within the NDF will be
copied to the output positions list. Subsequent applications can use
this information in order to align the positions with other data sets.
If no NDF is specified, then the user must indicate the co-ordinate
Frame in which the positions will be supplied using parameter FRAME. A
description of this Frame will be written to the output positions list
for use by subsequent applications.
The positions themselves may be supplied within a text file, or may be
given in response to repeated prompts for a parameter. Alternatively,
pixel centres in the NDF supplied for parameter NDF can be used (see
parameter MODE).
The output can be initialised by copying positions from an existing
positions list. Any positions supplied directly by the user are then
appended to the end of this initial list (see parameter INCAT).


Usage
~~~~~


::

    
       listmake outcat [ndf] [mode] { file=?
                                    { position=?
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
current Frame. [!]



CATEPOCH = DOUBLE PRECISION (Read)
``````````````````````````````````
The epoch at which the sky positions stored in the output catalogue
were determined. It will only be accessed if an epoch value is needed
to qualify the co-ordinate Frame specified by COLFRAME. If required,
it should be given as a decimal years value, with or without decimal
places ("1996.8" for example). Such values are interpreted as a
Besselian epoch if less than 1984.0 and as a Julian epoch otherwise.



DESCRIBE = LOGICAL (Read)
`````````````````````````
If TRUE, a detailed description of the co-ordinate Frame in which
positions are required will be displayed before the positions are
obtained using either parameter POSITION or FILE. [Current value]



DIM = _INTEGER (Read)
`````````````````````
The number of axes for each position. It is only accessed if a null
value is supplied for parameter NDF.



EPOCH = _DOUBLE (Read)
``````````````````````
If an IRAS90 Sky Co-ordinate System specification is supplied (using
parameter DOMAIN) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



FILE = FILENAME (Read)
``````````````````````
A text file containing the positions to be stored in the output
positions list. Each line should contain the formatted axis values for
a single position, separated by white space. It is only accessed if
parameter MODE is given the value "File".



FRAME = LITERAL (Read)
``````````````````````
Specifies the co-ordinate Frame of the positions supplied through
Parameters POSITION or FILE. There is a cascade of allowed
interpretations of this parameter value; the search for the co-
ordinate Frame ends once there is a successful interpretation,
otherwise the search moves on to the next possible meaning in the
following order.


+ An HDS path containing a WCS FrameSet, whose current Frame defines
the co-ordinate Frame.
+ The name of an NDF, whose current WCS co-ordinate Frame is used.
+ If the parameter value ends with ".FIT", an attempt is made to
interpret the parameter value as the name of a FITS file. If
successful, the primary WCS co-ordinate system from the primary HDU
headers is used.
+ A text file containing either an AST Frame dump (such as produced by
commands in the ATOOLS package), or a set of FITS WCS headers.
+ An IRAS90 "Sky Co-ordinate System" (SCS) string such as
"EQUAT(J2000)" (see SUN/163}), whereupon the positions are assumed to
be two-dimensional celestial co-ordinates in the specified system.
+ Domain name without any interpretation. Any Domain name may be
  supplied, but normally one of the standard Domain names, such as GRID,
  PIXEL, GRAPHICS should be given. Parameter DIM is used to determine
  the number of axes in the Frame.

This parameter is only accessed if the parameter NDF is given a null
value.



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing an existing positions list which is to be
included at the start of the output positions list. These positions
are mapped into the current co-ordinate Frame of the supplied NDF, or
into the Frame specified by parameter FRAME if no NDF was supplied. A
message is displayed indicating the Frame in which alignment occurred.
They are then stored in the output list before any further positions
are added. A null value may be supplied if there is no input positions
list. [!]



MODE = LITERAL (Read)
`````````````````````
The mode by which the positions are to be obtained. The options are as
follows.


+ "Interface" -- The positions are obtained using parameter POSITION.
+ "File" -- The positions are to be read from a text file specified
using parameter FILE.
+ "Good" -- The positions used are the pixel centres in the data file
specified by parameter NDF. Only the pixels that have good values in
the Data array of the NDF are used.
+ "Pixel" -- The positions used are the pixel centres in the data file
  specified by parameter NDF. All pixel are used, whether the pixel
  values are good or not.

["Interface"]



NDF = NDF (READ)
````````````````
The NDF which defines the available co-ordinate Frames in the output
positions list. If an NDF is supplied, the positions obtained using
parameter POSITION or FILE are assumed to be in the current co-
ordinate Frame of the NDF, and the WCS component of the NDF is copied
to the output positions list. If a null value is supplied, the single
co-ordinate Frame defined by parameter FRAME is stored in the output
positions list, and supplied positions are assumed to be in the same
Frame. [!]



OUTCAT = FILENAME (Write)
`````````````````````````
The catalogue holding the output positions list. See also parameter
CATFRAME.



POSITION = LITERAL (Read)
`````````````````````````
The co-ordinates of a single position to be stored in the output
positions list. Supplying ":" will display details of the co-ordinate
Frame in which the position is required. The position should be given
as a list of formatted axis values separated by white space. You are
prompted for new values for this parameter until a null value is
entered. It is only accessed if parameter MODE is given the value
"Interface".



TITLE = LITERAL (Read)
``````````````````````
A title for the output positions list. If a null (!) value is
supplied, the value used is obtained from the input positions list if
one is supplied. Otherwise, it is obtained from the NDF if one is
supplied. Otherwise, it is "Output from LISTMAKE". [!]



Examples
~~~~~~~~
listmake newlist frame=pixel dim=2
This creates a FITS binary catalogue called newlist.FIT containing a
list of positions, together with a description of a single two-
dimensional pixel co-ordinate Frame. The positions are supplied as a
set of space-separated pixel co-ordinates in response to repeated
prompts for the parameter POSITION.
listmake stars.txt frame=equat(B1950) epoch=1962.3
This creates a catalogue called stars.txt containing a list of
positions, together with a description of a single FK4 equatorial
RA/DEC co-ordinate Frame (referenced to the B1950 equinox). The
catalogue is stored in a text file using the CAT "Small Text List"
format ("STL" - see SUN/190). The positions were determined at epoch
B1962.3. The epoch of observation is required since the underlying
model on which the FK4 system is based is non-inertial and rotates
slowly with time, introducing fictitious proper motions. The positions
are supplied hours and degrees values in reponse to repeated prompts
for parameter POSITIONS.
listmake outlist ndf=allsky mode=file file=stars catframe=gal
This creates a FITS binary catalogue called outlist.FIT containing a
list of positions, together with descriptions of all the co-ordinate
Frames contained in the NDF allsky. The positions are supplied as co-
ordinates within the current co-ordinate Frame of the NDF. Application
WCSFRAME can be used to find out what this Frame is. The positions are
supplied in a text file called stars. The positions are transformed
into galactic co-ordinates before being stored in the output.
listmake out.txt incat=old.fit frame=gal
This creates an STL format catalogue stored in a text file called
out.txt containing a list of positions, together with a description of
a single galactic co-ordinate Frame. The positions contained in the
existing binary FITS catalogue old.fit are mapped into galactic co-
ordinates (if possible) and stored in the output positions list.
Further galactic co-ordinate positions are then obtained by repeated
prompting for the parameter POSITION. These positions are appended to
the positions obtained from file old.fit.
listmake out.txt incat=old.fit ndf=cobe
As above but the output positions list contains copies of all the
Frames in the NDF cobe. The positions in old.fit are mapped into the
current co-ordinate Frame of the NDF (if possible) before being stored
in the output positions list. The new positons must also be supplied
in the same Frame (using parameter POSITION).
listmake profpos.fit ndf=prof1 mode=pixel
This creates a positions list called profpos.fit containing the
positions of all the pixel centres in the one-dimensional NDF called
prof. This could for instance be used as input to application PROFILE
in order to produce another profile in which the samples are at the
same positions as those in NDF prof.



Notes
~~~~~


+ This application uses the conventions of the CURSA package for
determining the formats of input and output catalogues. If a file type
of .fit is given, then the catalogue is assumed to be a FITS binary
table. If a file type of .txt is given, then the catalogue is assumed
to be stored in a text file in STL format. If no file type is given,
then ".fit" is assumed.
+ There is a limit of 200 on the number of positions which can be
given using parameter POSITION. There is no limit on the number of
positions which can be given using parameter FILE.
+ Position identifiers are asigned to the supplied positions in the
  order in which they are supplied. If no input positions list is given
  using parameter INCAT, then the first supplied position will be
  assigned the identifier "1". If an input positions list is given, then
  the first supplied position is assigned an identifier one greater than
  the largest identifier in the input positions list.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CURSOR, LISTSHOW; CURSA: XCATVIEW, CATSELECT.


Copyright
~~~~~~~~~
Copyright (C) 1998-1999, 2001, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. Copyright (C) 2009 Science & Technology Facilities Council.
All Rights Reserved.


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


