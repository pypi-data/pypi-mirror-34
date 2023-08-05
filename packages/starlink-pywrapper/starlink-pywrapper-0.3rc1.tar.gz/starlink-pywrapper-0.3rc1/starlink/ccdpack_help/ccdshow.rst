

CCDSHOW
=======


Purpose
~~~~~~~
Displays the value of the CCDPACK global parameters


Description
~~~~~~~~~~~
This routine shows the current value of any CCDPACK global parameters.
It can also be used to save the current setup to a file for
restoration by CCDSETUP.


Usage
~~~~~


::

    
       ccdshow
       



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



SAVE = _LOGICAL (Read)
``````````````````````
Whether or not to save the values of the program parameters to a
"restoration" file, which can later be used by CCDSETUP to restore the
current values of the global parameters. If TRUE then you'll need to
specify the name of the file using the SAVEFILE parameter. [FALSE]



SAVEFILE = FILENAME (Read)
``````````````````````````
This parameter is only used if the SAVE parameters is TRUE. It allows
you to give the name of the restoration file to be used when saving
the program parameters. [CCDPACK_SETUP.DAT]



USESET = _LOGICAL (Read)
````````````````````````
This parameter determines whether values keyed by Set Index are to be
displayed. If CCDSETUP has been used to set up different global
parameter values for different members of each Set, and this parameter
is true, CCDSHOW will display the parameter values specific to each
Set Index value as well as the current unkeyed value. [FALSE]



Examples
~~~~~~~~
ccdshow
This displays the current values of all the CCDPACK global parameters
to the screen.
ccdshow save savefile=params.save
As well as displaying the global parameter values to the screen, this
will also write them to a restoration file called 'params.save'. This
file can be used at a later date to restore the current global
parameter setup using CCDSETUP.



Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
The parameters LOGTO, LOGFILE and USESET have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set using the
CCDSETUP command.


Copyright
~~~~~~~~~
Copyright (C) 1991-1994 Science & Engineering Research Council.
Copyright (C) 2001 Central Laboratory of the Research Councils. All
Rights Reserved.


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


