

CCDNOTE
=======


Purpose
~~~~~~~
Adds a note to the current CCDPACK log file


Description
~~~~~~~~~~~
This routine allows you to add a note to the CCDPACK log file. Notes
are intended to cover such things as the object name, the person
responsible for the data processing, etc. Notes can span more than one
line if earlier lines are terminated by the continuation character
'-'.


Usage
~~~~~


::

    
       ccdnote note
       



ADAM parameters
~~~~~~~~~~~~~~~



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter, then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP, then the
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

If the logging system has been initialised using CCDSETUP, then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



NOTE = LITERAL (Read)
`````````````````````
The comment to enter into the CCDPACK logfile. This may be continued
on to other lines by using the continuation character "-". Input can
be terminated either by not ending a line with a continuation
character, or by use of the ! null character at the beginning of the
line.



Examples
~~~~~~~~
ccdnote '"Start of the NGC2261 CCD reduction - R filter"'

ccdnote '"Reduction performed by Tel. E. Scope using data

from the 1986 run"'
In this example a record of the object and observer is entered into
the current log file.



Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
The NOTE parameter has no default and retains no information about any
previous values.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. All Rights
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


