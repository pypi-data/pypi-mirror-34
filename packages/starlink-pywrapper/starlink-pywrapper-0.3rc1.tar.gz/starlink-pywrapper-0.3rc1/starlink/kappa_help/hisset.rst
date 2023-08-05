

HISSET
======


Purpose
~~~~~~~
Sets the NDF history update mode


Description
~~~~~~~~~~~
This task controls the level of history recording in an NDF, and can
also erase the history information.
The level is called the history update mode and it is a permanent
attribute of the HISTORY component of the NDF, and remains with the
NDF and any NDF created therefrom until the history is erased or the
update mode is modified (say by this task).


Usage
~~~~~


::

    
       hisset ndf [mode] ok=?
       



ADAM parameters
~~~~~~~~~~~~~~~



MODE = LITERAL (Read)
`````````````````````
The history update mode. It can take one of the following values.
"Disabled" --- No history recording is to take place. "Erase" ---
Erases the history of the NDF. "Normal" --- Normal history recording
is required. "Quiet" --- Only brief history information is to be
recorded. "Verbose" --- The fullest-possible history information is to
be recorded.
The suggested default is "Normal". ["Normal"]



NDF = (Read and Write)
``````````````````````
The NDF whose history update mode to be modified or history
information erased.



OK = _LOGICAL (Read)
````````````````````
This is used to confirm whether or not the history should be erased.
OK=TRUE lets the history records be erased; if OK=FALSE the history is
retained and a message will be issued to this effect.



Examples
~~~~~~~~
hisset final
This sets the history-recording level to be normal for the NDF called
final.
hisset final erase ok
This erases the history information from the NDF called final.
hisset mode=disabled ndf=spectrum
This disables history recording in the NDF called spectrum.
hisset test42 v
This sets the history-recording level to be verbose for the NDF called
test42 so that the fullest-possible history is included.
hisset ndf=test42 mode=q
This sets the history-recording level to be quiet for the NDF called
test42, so that only brief information is recorded.



Notes
~~~~~


+ A HISTORY component is created if it does not exist within the NDF,
except for MODE="Erase".
+ The task records the new history update mode within the history
  records, even if MODE="Disabled" provided the mode has changed. Thus
  the history information will show where there may be gaps in the
  recording.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISCOM, HISLIST, NDFTRACE.


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


