

ASTIMP
======


Purpose
~~~~~~~
Imports coordinate system information into NDFs


Description
~~~~~~~~~~~
This task reads coordinate system information from an AST file and
uses it to modify the World Coordinate System (WCS) components of the
given NDFs. A new coordinate system is added (the same for each NDF)
within which a set of NDFs can be aligned. The newly added coordinate
system becomes the Current one.
If a coordinate system with the same Domain (name) already exists it
will be overwritten, and a warning message issued.
AST files for use by this program will normally be those written by
the ASTEXP program, and may either be standard ones designed for use
with a particular instrument, or prepared by the user.


Usage
~~~~~


::

    
       ASTIMP in astfile indomain
       



ADAM parameters
~~~~~~~~~~~~~~~



ASTFILE = LITERAL (Read)
````````````````````````
A file containing a sequence of framesets describing the relative
coordinate systems of NDFs from different sources.
It is intended that this file should be one written by the ASTEXP
application when a successful registration is made, and the user need
not be aware of its internal structure. The files are readable text
however, and can in principle be written by other applications or
doctored by hand, if this is done with care, and with knowledge of AST
objects (SUN/210). The format of the file is explained in the Notes
section.



FITSROT = LITERAL (Read)
````````````````````````
The name of a FITS header keyword whose value gives a number of
degrees to rotate the coordinate system by when it is imported. This
rotation is done after the mappings given in the AST file itself have
been applied. If any lower case characters are given, they are
converted to upper case. This may be a compound name to handle
hierarchical keywords, in which case it has the form keyword1.keyword2
etc. Each keyword must be no longer than 8 characters.
It will normally not be necessary to supply this keyword, since it can
be given instead within the AST file. If it is supplied however, it
overrides any value given there. [!]



IN = LITERAL (Read)
```````````````````
A list of NDF names whose WCS components are to be modified according
to ASTFILE. The NDF names may be specified using wildcards, or may be
specified using an indirection file (the indirection character is
"^").



INDICES( * ) = _INTEGER (Read)
``````````````````````````````
This parameter is a list of integers with as many elements as there
are NDFs accessed by the IN parameter. If the frameset identifiers are
of the type 'INDEX' then it indicates, for each NDF, what its index
number is. Thus if only one NDF is given in the IN list, and the value
of INDICES is [3], then the frameset with the identifier 'INDEX 3'
will be chosen. If set null (!) the NDFs will be considered in the
order 1,2,3,... which will be appropriate unless the NDFs are being
presented in a different order from that in which they were presented
to ASTEXP when generating the AST file. [!]



INDOMAIN = LITERAL (Read)
`````````````````````````
The Domain name to be used for the Current frames of the framesets
which are imported. If a null (!) value is given, the frames will
assume the same name as in the AST file. [!]



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



ROT = _DOUBLE (Read)
````````````````````
A fixed angle in degrees through which all the imported frames should
be rotated. This rotation is done after the mappings in the AST file
itself have been applied. [0]



Examples
~~~~~~~~
astimp data* camera.ast
This will apply the AST file "camera.ast" to all the NDFs in the
current directory with names beginning "data". The file "camera.ast"
has previously been written using ASTEXP with the parameter
ASTFILE=camera.ast. A new coordinate system, with a name that was
determined when the AST file was written, is attached to each NDF.
astimp "data3,data4" instrum.ast indomain=obs1 indices=[3,4]
This imports frameset information from the AST file instrum.ast which
was written by ASTEXP with the IDTYPE parameter set to INDEX. In this
case NDFs of only the third and fourth types described in that file
are being modified. The name of the new coordinate system will be
OBS1, overriding the name used when the AST file was written.
astimp astfile=instrum.ast in=! logto=terminal accept
This will simply report on the framesets contained within the AST file
"instrum.ast", writing the ID of each to the terminal only.



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


