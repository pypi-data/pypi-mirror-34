

CCDNDFAC
========


Purpose
~~~~~~~
Accesses a list of NDFs and writes their names to a file


Description
~~~~~~~~~~~
This routine accesses a list of NDFs and writes their names to a text
file. It is intended to be used as an aid to producing procedures
which require the facilities of NDF list access used in CCDPACK. For
this reason the usual application introductory message is suppressed.
The names of the NDFs may be written out to the terminal as an aid to
memory. If no NDFs are accessed then the output file will not be
created, testing for the existence of this file is a platform
independent way of determining if the invocation has been successful.


Usage
~~~~~


::

    
       ccdndfac namelist echo
       



ADAM parameters
~~~~~~~~~~~~~~~



ECHO = _LOGICAL (Read)
``````````````````````
If TRUE then the names of the NDFs will be written to the terminal
unless there is only one input NDF. [TRUE]



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



IN = LITERAL (Read)
```````````````````
A list of NDF names. The NDF names should be separated by commas and
may include wildcards. [!]



MAXNDF = _INTEGER (Read)
````````````````````````
The maximum number of NDFs which should be accessed. If a null return
"!" is given for this parameter then the normal CCDPACK limit will be
applied. [!]



NAMELIST = LITERAL (Read)
`````````````````````````
The name of the output file to contain the names of the accessed NDFs.
[CCDNDFAC.LIS]



Examples
~~~~~~~~
ccdndfac ndf_name_list true
In this example the list of NDF names is written to ndf_name_list and
the NDF names are echoed to the terminal. No constraint is placed on
the number of NDFs accessed (other than the normal CCDPACK limit).
ccdndfac ndf_name true maxndf=1
In this example only a single NDF name is accessed. The name is not
echoed to the terminal (even though echo is set TRUE).



Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application. The intrinsic default
behaviour of the application may be restored by using the RESET
keyword on the command line (you may well want to do this when using
the application from a procedure).
Certain parameters (LOGTO and LOGFILE) have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set and reset using
the CCDSETUP and CCDCLEAR commands.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1997, 2000 Central Laboratory of the Research Councils. All Rights
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


