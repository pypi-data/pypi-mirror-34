

CCDCLEAR
========


Purpose
~~~~~~~
Clears CCDPACK global parameters


Description
~~~~~~~~~~~
CCDCLEAR removes CCDPACK specific parameters from the globals file. It
has the capability of removing all the CCDPACK global parameters or
just a named subset.


Usage
~~~~~


::

    
       ccdclear byname
       



ADAM parameters
~~~~~~~~~~~~~~~



BYNAME = _LOGICAL (Read)
````````````````````````
This parameter controls how the parameters are cleared. If FALSE then
all CCDPACK global parameters will be cleared. If TRUE then a list of
the names of the global parameters to clear is requested (see
parameter NAMES). [FALSE]



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



NAMES = LITERAL (Read)
``````````````````````
Only used when BYNAME is TRUE. The response to this parameter should
be a comma separated list of the names of the CCDPACK parameters which
are to be cleared. Valid names are:
ADC, BIAS, BOUNDS, CAL, DEFERRED, DIRECTION, EXTENT, FLAT, GENVAR,
MASK, NDFNAMES, PRESERVE, RNOISE, SATURATE, SATURATION, SETSAT, USESET
These correspond to the parameter names used in CCDSETUP (and in the
other applications which access these parameters).
The names may be abbreviated to unique values.



Examples
~~~~~~~~
ccdclear
Invoking CCDCLEAR without any arguments will clear all the CCDPACK
globals, unless the BYNAME=TRUE option has been used in a previous
invocation.
ccdclear false
Using this invocation will definitely clear all the CCDPACK global
parameters.
ccdclear byname names='"adc,rnoise,direc"'
This example shows how to clear specific CCDPACK global parameters.
The NAMES need only be unique amongst the possibilities so could have
been abbreviated to "a,r,di".



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
Certain parameters (LOGTO and LOGFILE ) have global values. These
global values will always take precedence, except when an assignment
is made on the command line. Global values may be set using the
CCDSETUP command.


Deficiencies
~~~~~~~~~~~~


+ Uses direct HDS calls to erase GLOBAL parameter file components.




Copyright
~~~~~~~~~
Copyright (C) 1991, 1993-1994 Science & Engineering Research Council.
Copyright (C) 1995, 2000-2001 Central Laboratory of the Research
Councils. All Rights Reserved.


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


