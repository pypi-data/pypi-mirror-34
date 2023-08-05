

SHOWSET
=======


Purpose
~~~~~~~
Outputs NDF Set header information


Description
~~~~~~~~~~~
This routine is used to examine the Set membership attributes of NDFs.
It will show the Set Name and Set Index attributes for each NDF, and
whether it contains a CCD_SET coordinate frame in its WCS component.
The NDFs are output grouped by Set Name or Set Index. If required, a
restricted list of NDFs, those with certain Name and/or Index
attributes, may be selected for output; in this case the acceptable
Names/Indexes can be given explicitly or as a list of template NDFs
whose attributes they have to match. The names of the NDFs selected
for output may be written to a list file. SHOWSET can therefore be
used to construct files listing those NDFs in a given Set, or
corresponding NDFs in different Sets.


Usage
~~~~~


::

    
       showset in
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = LITERAL (Read)
```````````````````
A list of NDFs to examine.



INDEX = LITERAL (Read)
``````````````````````
If PICKINDEX=EQUAL this parameter restricts which files will be
selected for output. It must be a group expression (a comma-separated
list) each member of which is an acceptable INDEX value. Only files
with a Set Index value equal to one of these will be selected.



INDEXLIKE = LITERAL (Read)
``````````````````````````
If PICKINDEX=LIKE this parameter restricts which files will be
selected for output. It must be a group expression (a comma-separated
list which may employ wildcards or indirection) each member of which
represents an image to be used as a template. Only images with a Set
Index value matching that of one of the template images will be
selected.



LISTBY = LITERAL (Read)
```````````````````````
Indicates the way in which NDFs should be grouped for output. It may
take the values 'NAME', 'INDEX' or 'NONE'. If set to NAME, then all
the NDFs in the same Set are grouped together in the output; if set to
INDEX then all the corresponding NDFs from different Sets are grouped
together, and if set to NONE NDFs will be listed in the same order as
the IN parameter. If only NDFs with the same Name or with the same
Index are being output, this will have no effect. [NAME]



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



NAME = LITERAL (Read)
`````````````````````
If PICKNAME=EQUAL this parameter restricts which files will be
selected for output. It must be a group expression (a comma-separated
list) each member of which is a string. Only files with a Set Name
value the same as one of these will be selected.



NAMELIKE = LITERAL (Read)
`````````````````````````
If PICKNAME=LIKE this parameter restricts which files will be selected
for output. It must be a group expression (a comma-separated list
which may employ wildcards or indirection) each member of which
represents an image to be used as a template. Only images with a Set
Name value matching that of one of the template images will be
selected.



NAMELIST = LITERAL (Read)
`````````````````````````
The name of an output file in which to write the names of the images
selected for output. The (non-comment) lines of this file are of the
form:
ndf-name # set-index set-name
since the set-index and set-name values appear to the right of a
comment character, the file can thus be used as an indirection file
for input to other CCDPACK commands. [showset.lis]



PICKINDEX = LITERAL (Read)
``````````````````````````
Indicates how NDFs are to be filtered by Set Index attribute for
output. Takes one of the following values:

+ ALL -- All Index values are acceptable
+ EQUAL -- Only Index values listed in the INDEX parameter value are
acceptable
+ LIKE -- Only Index values the same as those of the images listed in
  the INDEXLIKE parameter are acceptable.

[ALL]



PICKNAME = LITERAL (Read)
`````````````````````````
Indicates how NDFs are to be filtered by Set Name attribute for
output. Takes one of the following values:

+ ALL -- All Name values are acceptable
+ EQUAL -- Only Name values listed in the NAME parameter value are
acceptable
+ LIKE -- Only Name values the same as those of the images listed in
  the NAMELIKE parameter are acceptable.

[ALL]



SETLESS = _LOGICAL (Read)
`````````````````````````
If there are no restrictions on which Sets to display, because
PICKNAME and PICKINDEX are both set to ALL, this parameter determines
what happens to NDFs which have no Set headers. If SETLESS is true,
they are selected for output, but if SETLESS is false, they are
discarded. [FALSE]



Examples
~~~~~~~~
showset *
This will list all the NDFs in the current directory which contain Set
header information; the listing will be grouped by the Set Name
attribute and Set Index will be shown.
showset * setless=true
This will do the same as the previous example, except that those NDFs
with no Set header information will be displayed as well.
showset * pickname=like namelike="gc6235a,gc4021a" namelist=gc.lis
This will list all the NDFs in the current directory which are in the
same Set as the NDFs gc6235a and gc4021a. As well as showing the Set
information of these files on the screen, the names of the files thus
selected will be written to the file gc.lis.
showset fdata setless reset
This will just show the Name and Set information of the file fdata. If
fdata is a container file, it will show the Set information for all
the datasets within it. Since the SETLESS parameter is given, even if
it has no Set header output will be written.
showset dat* pickindex=equal index=3 logto=neither namelist=out.lis
This will write a list of NDF names to the file out.lis choosing only
those which have a Set Index attribute value of 3. There will be no
output to the screen or log file.



Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application. The intrinsic default
behaviour of the application may be restored by using the RESET
keyword on the command line.
Certain parameters (LOGTO and LOGFILE) have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set and reset using
the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils


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


