

HISLIST
=======


Purpose
~~~~~~~
Lists NDF history records


Description
~~~~~~~~~~~
This lists all the history records in an NDF. The reported information
comprises the date, time, and application name, and optionally the
history text.


Usage
~~~~~


::

    
       hislist ndf
       



ADAM parameters
~~~~~~~~~~~~~~~



BRIEF = _LOGICAL (Read)
```````````````````````
This controls whether a summary or the full history information is
reported. BRIEF=TRUE requests that only the date and application name
in each history record is listed. BRIEF=FALSE causes the task to
report the history text in addition. [FALSE]



NDF = NDF (Read)
````````````````
The NDF whose history information is to be reported.



Examples
~~~~~~~~
hislist vcc953
This lists the full history information for the NDF called vcc935. The
information comprises the names of the applications and the times they
were used, and the associated history text.
hislist vcc953 brief
This gives a summary of the history information for the NDF called
vcc935. It comprises the names of the applications and the times they
were used.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISCOM, HISSET, NDFTRACE.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995 Central Laboratory of the Research Councils. All Rights
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


