

WCSREG
======


Purpose
~~~~~~~
Aligns NDFs using multiple coordinate systems


Description
~~~~~~~~~~~
This application takes a set of NDFs which have World Coordinate
System (WCS) components, and tries to align them all according to a
given list of coordinate system domains (labels). If successful, it
adds a new coordinate frame to the WCS component of each within which
they are all aligned. The TRANLIST or TRANNDF applications can then be
used on the resulting NDFs.
This can be of use when different kinds of alignment information are
available between different members of a group of NDFs. By supplying
an ordered list of coordinate systems within which to align, the best
alignment available can be made between different members of the
group, falling back on second or third choices of alignment types
where first choices are not available.
The application operates on a set of NDFs, IN. A list of domains
DOMAINS within which to align, in order of preference, is specified,
and a reference NDF is denoted by REFPOS. On successful completion, a
new coordinate frame (which becomes Current), with a domain given by
OUTDOMAIN (default CCD_WCSREG) is added to each of the NDFs in the
input set. Any previously existing frames with this domain will be
removed.
The new coordinate system is a copy of the pixel coordinate system of
the reference NDF, so for the reference NDF there is a unit mapping
between its pixel and new Current coordinates. For each other NDF, the
program attempts to find a mapping from the reference NDF to it. If it
and the reference NDF do not share frames in any of the domains given
by the DOMAINS parameter, it will try to use the WCS components of
intermediate NDFs to find a path between them; this path is a subgraph
of a graph in which the nodes are the NDFs and an edge exists between
two nodes if the NDFs share a domain in the given list. The shortest
available path which connects a pair is chosen, and if there is more
than one which meets this criterion, one which uses domains near the
head of the list is preferred.
If the USESET parameter is true, then WCSREG will take account of
alignment information stored in the CCDPACK Set header; this means
that the alignment implied when images were previously grouped into a
Set can be guaranteed to be retained.
If the graph is not fully connected, a list of the existing subgraphs
is output, and the program will normally terminate, however it can be
made to continue with registration of the connected NDFs by setting
the OVERRIDE parameter.


Usage
~~~~~


::

    
       WCSREG in domains
       



ADAM parameters
~~~~~~~~~~~~~~~



DOMAINS( * ) = LITERAL (Read)
`````````````````````````````
This parameter should be a list of frame domains, in order of
preference for achieving alignment. Alignment paths between NDFs are
selected by shortness of path, but in case of a tie, those using
domains nearest the start of this list are used by preference. You
should not normally include the CCD_SET domain in this list; for
details of how this domain is treated specially, see the USESET
parameter.
Note that this parameter is an array of strings, so that either the
whole list should be surrounded by square brackets, or each element
should be surrounded by double quotes. The whole thing may need to be
protected from the Unix shell by using, e.g., single quotes.
Supplying the null value (!) is equivalent to specifying the current
domain of the reference NDF. The effect of this is to retain the
alignment already given by the Current coordinates of each image, but
to ensure that the pixels are aligned with the pixels of the reference
image. This will result in the images being aligned in a coordinate
system suitable for resampling with TRANNDF. [!]



IN = LITERAL (Read)
```````````````````
A list of the names of the NDFs which are to be aligned. The names
should be separated by commas and may include wildcards. They may
alternatively be specified using an indirection file (the indirection
character is "^").
If the program is successful, a new coordinate system with a domain
determined by the OUTDOMAIN parameter will be added to the WCS
component of each of the IN files containing the alignment
information. These will become the new Current coordinates.



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



NAMELIST = LITERAL (Read)
`````````````````````````
The name of an output file in which to record all the images to which
new coordinate systems were successfully added. This may not be the
same as the IN list if OVERRIDE is set true. [wcsreg.lis]



OUTDOMAIN = LITERAL (Read)
``````````````````````````
This gives the name of the domain for the new frame which is added to
the WCS components of the NDFs on successful completion. If any frames
in the same domain previously exist in the WCS component, they are
removed. The name is converted to upper case, and whitespace is
removed. [CCD_WCSREG]



OVERRIDE = _LOGICAL (Read)
``````````````````````````
If not all the NDFs can be aligned using the domains given in DOMAINS
then the application will report on which sets of NDFs form
connectable subsets of the IN list. In this case, if this parameter is
set FALSE, then the application will exit with an error message. If it
is set TRUE however, it will continue and insert new frames in those
NDFs which can be reached from the one indicated by REFPOS, making no
change to the others, except to remove any frames in the domain
OUTDOMAIN which already exist.
The NAMELIST parameter can be used to record which images were
successfully registered when OVERRIDE is true (if OVERRIDE is false,
then it will be the same as IN unless the program fails). [FALSE]



REFPOS = _INTEGER (Read)
````````````````````````
The position within the IN list which corresponds to the reference
NDF. The registration frame is a copy of (and unitmapped to) the pixel
frame of the reference NDF, and for each other NDF the program tries
to find a path from it to the reference NDF going from one NDF to
another only when they both have frames in the same one of the entries
in the DOMAINS list. [1]



USESET = _LOGICAL (Read)
````````````````````````
This parameter governs whether Set-based alignment information in the
NDFs, if it exists, should be used. If it is set to true, then
coordinate frames with the domain CCD_SET will take precedence over
all the ones named in the DOMAINS parameter. In this case, if two of
the NDFs both have a CCD_SET coordinate frame and also share the same
Set Name attribute, the connection will be made in CCD_SET frame. If
no CCD_SET frames are present, this parameter has no effect.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



Examples
~~~~~~~~
wcsreg * [ccd_reg,sky]
In this example all the NDFs in the current directory are being
aligned. All have an attached SKY coordinate sysetm with approximate
information about the pointing, added by the telescope system at
observation time. Some of the NDFs however overlap, and have been run
through the REGISTER program which has added a CCD_REG coordinate
system containing more accurate alignment information derived from
matching objects between different images. Where two of the images
have CCD_REG coordinates, these will be used to align them, but where
they do not, the program will fall back on the less accurate SKY
coordinates for alignment. The new coordinate frame added will be
given the default name CCD_WCSREG.
After this process, the NDFs can be presented to TRANNDF for
resampling prior to making a mosaic.
wcsreg "obs1_*,obs2_*" outdomain=final
domains=[ccd_reg,inst_obs1,inst_obs2] NDFs with names starting 'obs1_'
and 'obs2_' are aligned. Where they share CCD_REG coordinates this
will be used for alignment, but otherwise the INST_OBS1 and INST_OBS2
coordinate systems will be used. These perhaps contain information
about the relative alignment of CCDs on the focal plane of the
instrument, and may have been added to the WCS component using the
ASTIMP application. The name FINAL is used for the new domain added to
the WCS component.
wcsreg "skyfr1,skyfr2,skyfr3,skyfr4" refpos=2 domains=!
Here wcsreg is being used with a somewhat different intent. The images
named are already fully aligned in their current coordinates but
executing this command has the effect of aligning them in a new
coordinate system which is a copy of the pixel coordinate system of
'skyfr2'. Since this has units which are the size of pixels, the
resulting image files are suitable for resampling using TRANNDF.
Supposing that they were originally aligned in SKY coordinates they
could not have been resampled by TRANNDF in their initial state, since
the SKY coordinates have units of radians, which are much too large
compared to pixels.



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
Certain parameters (LOGTO, LOGFILE and USESET) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1999 Particle Physics & Astronomy Research Council


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


