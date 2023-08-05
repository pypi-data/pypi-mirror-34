

ASTEXP
======


Purpose
~~~~~~~
Exports coordinate system information from images


Description
~~~~~~~~~~~
This task exports coordinate system information from a set of NDFs,
writing it to an AST file. For each NDF a frameset is written
containing information about how to map between a selected Base frame
and the NDF's Current frame. Each frameset is identified by a key
which is derived from the NDF itself, and matches keys which can be
derived from other NDFs to which similar framesets ought to apply. The
key should be generated in the same way when the AST file is used for
importing the mapping information by ASTIMP or MAKESET. Currently
these keys can be generated according to a FITS header card or the
order in which the NDFs are presented. Additional information may be
written describing what use to make of FITS headers in the NDFs.
Used together, the framesets written out to an AST file can thus
contain information about the positioning of images in a set of
related NDFs.
AST files written out by this program can be applied to other NDFs of
similar origin using the ASTIMP or MAKESET programs, so that
registration information present in the WCS components of one group of
NDFs (put there for instance by the REGISTER or WCSEDIT programs) can
be transferred using ASTIMP and ASTEXP to another similar set. This
"similar set" will typically be one from chips in the same mosaic
camera instrument.
A 2-frame frameset is output for each NDF. The Base frame is one
selected by the BASEFRAME parameter, and is identical in the exported
frameset to the one in the original NDF. The Current frame in the
exported frameset is the same as the Current frame in the original
NDF, but may be given a different Domain name by the OUTDOMAIN
parameter.
Under normal circumstances, the Current frames of all the input NDFs
should share the same Domain name, and so should the frames identified
by the BASEFRAME parameter. A warning will be issued if this is not
the case. Warnings will also be issued if the NDF identifiers are not
all unique.


Usage
~~~~~


::

    
       ASTEXP in astfile outdomain baseframe
       



ADAM parameters
~~~~~~~~~~~~~~~



ASTFILE = LITERAL (Read)
````````````````````````
The name of the AST file to be written.



BASEEPOCH = _DOUBLE (Read)
``````````````````````````
If a "Sky Co-ordinate System" specification is supplied (using
parameter BASEFRAME) for a celestial co-ordinate system, then an epoch
value is needed to qualify it. This is the epoch at which the supplied
sky positions were determined. It should be given as a decimal years
value, with or without decimal places ("1996.8" for example). Such
values are interpreted as a Besselian epoch if less than 1984.0 and as
a Julian epoch otherwise.



BASEFRAME = LITERAL (Read)
``````````````````````````
This parameter specifies the WCS frame from the NDFs relative to which
the Current frames will be defined in the output AST file. To be
useful, this must specify a frame which occurs in all the NDFs in the
IN list, and can be expected to occur in any NDF to which the AST file
will later be applied using ASTIMP.
The value of the parameter can be one of the following:

+ A domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95). A domain name is usually
  the most suitable choice.

Unlike the Current frame, the frame selected using this parameter is
copied to the AST file unmodified; in particular it retains the same
Domain name. [PIXEL]



FITSID = LITERAL (Read)
```````````````````````
If the IDTYPE parameter has the value FITSID, this parameter gives the
FITS header keyword whose value distinguishes frames with different
coordinate system information. If any lower case characters are given,
they are converted to upper case. This may be a compound name to
handle hierarchical keywords, in which case it has the form
keyword1.keyword2 etc. Each keyword must be no longer than 8
characters.



FITSROT = LITERAL (Read)
````````````````````````
If this parameter is not null, it gives the name of a FITS header
keyword whose value gives a number of degrees to rotate the coordinate
system by when it is imported. If any lower case characters are given,
they are converted to upper case. This may be a compound name to
handle hierarchical keywords, in which case it has the form
keyword1.keyword2 etc. Each keyword must be no longer than 8
characters. [!]



IDTYPE = LITERAL (Read)
```````````````````````
This parameter destermines the form of the ID value which
distinguishes the framesets from each other in the exported AST file.
It may have one of the following values:

+ FITSID -- ID is generated from FITS header (see also the FITSID
parameter).
+ INDEX -- ID is given by an integer as taken from the INDICES
parameter. This normally gives the frameset generated from the N'th
NDF in the IN list an ID with index N.
+ SET -- ID is given by an integer taken from the Set Index attribute
  of the CCDPACK Set header of each input file.

[INDEX]



IN = LITERAL (Read)
```````````````````
A list of NDFs from which framesets are to be extracted. The Current
frame of each should normally be the same, and should be a frame in
which the different NDFs are correctly registered. The NDF names may
be specified using wildcards, or may be specified using an indirection
file (the indirection character is "^").



INDICES( * ) = _INTEGER (Read)
``````````````````````````````
If IDTYPE is set to INDEX, then this parameter is a list of integers
with as many elements as there are NDFs accessed by the IN parameter.
It gives the sequence of indices N to be used for generating the ID
values. If set null (!) the NDFs will be considered in the order
1,2,3,... which will normally be appropriate unless the NDFs are being
presented in an order different from that in which they are likely to
be presented to ASTIMP. [!]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is
"CCDPACK.LOG". [CCDPACK.LOG]



LOGTO = LITERAL (Read)
``````````````````````
Every CCDPACK application has the ability to log its output for future
reference as well as for display on the terminal. This parameter
controls this process, and may be set to any unique abbreviation of
the following:

+ TERMINAL -- Send output to the terminal only
+ LOGFILE -- Send output to the logfile only (see the LOGFILE
parameter)
+ BOTH -- Send output to both the terminal and the logfile
+ NEITHER -- Produce no output at all

If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



OUTDOMAIN = LITERAL (Read)
``````````````````````````
This parameter gives the name of the new alignment domain for the
frames written out to the AST file. It is a good idea to choose a
value which is not likely to exist previously in the WCS components of
the NDFs to which ASTFILE will be applied. A suitable value might be
the name of the instrument from which the NDFs are obtained.
Note that the frames which are written to the AST file are always the
Current frames of the NDFs supplied; this parameter only gives the
name that the frames will have in the AST file, and consequently the
name by which they will be known when the WCS information is imported
into other NDFs using ASTIMP or MAKESET.
The name is converted to upper case, and whitespace is removed.
[CCD_EXPORT]



Examples
~~~~~~~~
astexp reg_data* camera.ast idtype=fitsid fitsid=CHIPNUM
outdomain=camera This will save the information about the relative
positioning of the NDFs 'reg_data*' to the file 'camera.ast', calling
the alignment domain 'CAMERA'. The file 'camera.ast' can later be used
by the ASTIMP or MAKESET applications to add the same coordinate
information to a different set of NDFs from the same instrument.
Before running this, the NDFs 'reg_data*' should be correctly aligned
in their Current domain. CHIPNUM must be the name of a FITS header
keyword present in the FITS extension of each NDF whose value
distinguishes the CCDs from each other (presumably present in the
unreduced data). The mappings between the pixel coordinates and
Current coordinates of the input NDFs are recorded.
astexp "im1,im2,im3" astfile=camera.ast baseframe=axis
title="Focal plane alignment" accept In this case the OUTDOMAIN
parameter takes its default value of 'CCD_EXPORT', but mappings are
between the Current coordinates of the input NDFs and their 'AXIS'
coordinates. This could be a good idea if the images had been shrunk
using KAPPA's COMPAVE or something similar, which modifies the PIXEL
coordinates but leaves the AXIS coordinates unchanged. No suitable
FITS header is available to distinguish the different types of NDF, so
the IDTYPE parameter is allowed to assume its default value of INDEX.
When camera.ast is used for importing frameset information, the NDFs
from the three different chips must be listed in the same order as
when this command was invoked. The title of the output Current frame
will be as given.
astexp "r10595[2345]" wfc.ast outdomain=wfc
idtype=fitsid fitsid=CHIPNAME fitsrot=ROTSKYPA This exports the
alignment information from the four named NDFs to a file wfc.ast. The
CHIPNAME FITS header identifies the source CCD for each, and the
ROTSKYPA FITS header gives a number of degrees to rotate each frame
additional to the relative alignment information.



Notes
~~~~~
AST file format: The AST file is designed to be written by ASTEXP and
read by ASTIMP or MAKESET, and the user does not need to understand
its format. It is however a text file, and if care is taken it may be
edited by hand. Removing entire framesets and modifying ID values or
domain names may be done fairly easily, but care should be taken (see
SUN/210) if any more involved changes are to be undertaken. The format
of the file is explained here.
The AST file consists of the following, in order:
<global modifiers> (blank line) <frameset 1> <frameset 1 modifiers>
(blank line) <frameset 2> <frameset 2 modifiers> (blank line) ... (end
of file)
Characters after a '#' character are normally ignored. The constituent
parts are composed as follows:
Blank line: A single blank line, which may contain spaces but no
comments.
Frameset: The framesets are written in AST native format, as explained
in SUN/210.
Each frameset has an ID, and contains two frames (a Base frame and a
Current frame) and a mapping between them. The domains of all the Base
frames should normally be the same, and likewise for all the Current
frames. For the NDFs to which the file will be applied by ASTIMP,
their WCS components should contain frames in the same domain as the
AST file's Base frame.
The ID of each frameset is used to determine, for each NDF, which of
the framesets in the file should be applied to it. This ID is a string
which can assume one of the following forms:


+ "FITSID KEY VALUE" This will match an NDF if the first FITS header
card with the keyword KEY has the value VALUE. If the value is of type
CHARACTER it must be in single quotes. KEY may be compound (of the
form keyword1.keyword2 etc) to permit reading of hierarchical
keywords.
+ "INDEX N" This associates a frameset with an integer N. Usually N
will take the values 1,2,3,... for the framesets in the file.
Typically the N'th NDF in a list will match the one with an ID of
"INDEX N".
+ "SET N" This will match an NDF if the Set Index attribute in its
  CCDPACK Set header is equal to the integer N.

Modifiers: Modifiers describe additional modifications to be made to
the framesets on import. They are of the form
USE keyword arguments
Currently the only modifier defined is FITSROT, which defines the name
of a FITS header which specifies how many degrees to rotate the image
before use. This rotation is carried out after the mapping defined by
the frameset itself.
Global modifiers affect all NDFs processed with the AST file. Frameset
modifiers affect only those NDFs which correspond to their frameset.
Rigorous error checking of the AST file is not performed, so that
unhelpful modifications to the WCS components of the target NDFs may
occur if it is not in accordance with these requirements.


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when using the application on new datasets or
after a break of sometime. The intrinsic default behaviour of the
application may be restored by using the RESET keyword on the command
line.
Certain parameters (LOGTO and LOGFILE) have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set and reset using
the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1999 Central Laboratory of the Research Councils


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


