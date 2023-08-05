

REDUCE
======


Purpose
~~~~~~~
Automatic CCD data reduction facility (command-line version)


Description
~~~~~~~~~~~
This routine provides a command-line interface to the automated
reduction facilities of CCDPACK.
It guides you though the selection of the appropriate route for
performing a reduction. Possible routes are using an import control
table to interpret FITS headers, choosing from a list of known
detector setups or just supplying all the necessary information.
Using FITS headers is only possible if your data contains the correct
information. If a table is not listed for your telescope/detector
combination then you will need to create one. The contents of import
tables are described in the help for the program IMPORT. Unless you
(and perhaps your colleagues) are going to reduce large amounts of
data from an unknown telescope then you should use the normal setup
and data organization techniques.
If you do not choose a detector setup file or have none you will need
to organize your data into different frame types (bias, flat, target
etc.), so either use a naming scheme that allows you to distinguish
between them using wildcard patterns or create lists of the names in
files.
If you cannot select from any of the known detectors then the most
crucial information that you require is a knowledge of where the bias
strips are and the useful CCD area (if these are appropriate for the
type of data you're reducing). If you are sitting at an X display then
the CCD geometry can be determined from within reduce. Otherwise you
will need to determine these before running reduce.


Usage
~~~~~


::

    
       REDUCE
       



ADAM parameters
~~~~~~~~~~~~~~~



CHOICE = _CHAR (Read)
`````````````````````
The operation that you want to use on the selected file. Either
"view", "select" or "continue". Continue means you do not want to
selected a file. ["view"]



CLEAR = _LOGICAL (Read)
```````````````````````
Whether or not to clear any existing CCD global parameters. [TRUE]



INDEX = INTEGER (Read)
``````````````````````
The index of the known detector file that you want to view or select.



KNOWN = _LOGICAL (Read)
```````````````````````
Whether or not you want to select or view the list of known detectors.
[FALSE]



MANUAL = _LOGICAL (Read)
````````````````````````
Whether the types of the input data will be assigned manually (by
running PRESENT) or not. [TRUE]



RESTORE = _LOGICAL (Read)
`````````````````````````
Whether or not a "restoration" file will be used to reset the CCDPACK
global parameters, or not. [FALSE]



RESTOREFILE = _CHAR (Read)
``````````````````````````
The name of an existing "restoration" file. This musy have been
created by a previous run of the CCDSETUP command.



SETGEOM = _LOGICAL (Read)
`````````````````````````
Whether or not a graphical method will be used to determine the
geometries of the CCD (i.e. the position of the useful region of the
CCD and the bias strips). [TRUE]



TABLE = _CHAR (Read)
````````````````````
The name of an import control table (see the IMPORT command for
details about this) to be used to import information from the FITS
extension of an NDF.



Notes
~~~~~
Unknown detectors. If you do develop an import table or restoration
(setup) file for a telescope/detector pass these on to the maintainer
of this package, together with a description. They will be distributed
in future releases for the benefit of others.


Copyright
~~~~~~~~~
Copyright (C) 1997, 2001 Central Laboratory of the Research Councils.
All Rights Reserved.


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


