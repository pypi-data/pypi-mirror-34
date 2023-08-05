

PARGET
======


Purpose
~~~~~~~
Obtains the value or values of an application parameter


Description
~~~~~~~~~~~
This application reports the value or values of a parameter from a
named task. It does this by searching the parameter file of the task.
The purpose is to offer an easier-to-use interface for passing values
(especially output parameters) between tasks in shell scripts. The
values are formatted in lines with as many values as can be
accommodated across the screen up to a maximum of 132 characters;
values are space separated. However, in scripts the values are likely
to be written to a script variable. Thus for example in the C-shell:
set med = `parget median histat`
would redirect the output to shell variable med, and thus a reference
to $med would substitute the median value obtained the last time
application HISTAT was invoked. If the parameter comprises a vector of
values these can be stored in a C-shell array. For instance,
set perval = `parget perval histat`
would assign elements of the shell array perval[1], perval[2], etc. to
the last-computed percentile values of HISTAT. For other scripting
languages such as Python, the alternative vector format produced by
setting parameter VECTOR to TRUE may be more appropriate.
Single elements of an parameter array may also be accessed using the
array index in parentheses.


Usage
~~~~~


::

    
       parget parname applic
       



ADAM parameters
~~~~~~~~~~~~~~~



APPLIC = LITERAL (Read)
```````````````````````
The name of the application from which the parameter comes.



PARNAME = LITERAL (Read)
````````````````````````
The parameter whose value or values are to be reported.



VECTOR = _LOGICAL (Read)
````````````````````````
If TRUE, then vector parameters will be displayed as a comma-separated
list of values enclosed in square brackets. If FALSE, vector values
are printed as a space-separated list with no enclosing brackets.
Additionally, if VECTOR is TRUE, string values (whether vector or
scalar) are enclosed in single quotes and any embedded quotes are
escaped using a backslash. [FALSE]



Examples
~~~~~~~~
parget mean stats
Report the value of parameter MEAN for the application STATS.
parget mincoord \
This reports the values of parameter MINCOORD of the current
application, in this case STATS.
parget applic=ndftrace parname=flabel(2)
This reports the value of the second element of parameter FLABEL for
the application NDFTRACE.



Notes
~~~~~


+ The parameter file is located in the $ADAM_USER directory, if
defined, otherwise in the adam subdirectory of $HOME. If it cannot be
located there, the task reports an error.
+ The parameter must exist in the selected application parameter file
and not be a structure, except one of type ADAM_PARNAME.
+ This task is not designed for use with ICL, where passing parameter
  values is quite straightforward. It does not operate with monolith
  parameter files.




Copyright
~~~~~~~~~
Copyright (C) 1995 Science & Engineering Research Council Copyright
(C) 2005-2006 Particle Physics and Astronomy Research Council.
Copyright (C) 2012 Science & Technology Facilities Council. All Rights
Reserved.


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


