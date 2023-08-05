

ASTFORMAT
=========


Purpose
~~~~~~~
Format coordinate values for a Frame axis


Description
~~~~~~~~~~~
This application displays character strings containing the formatted
(character) versions of coordinate values for a Frame axis. The
formatting applied is determined by the Frame's attributes and, in
particular, by any Format attribute string that has been set for the
axis. A suitable default format (based on the Digits attribute value)
will be applied if necessary.


Usage
~~~~~


::

    
       astformat this axis value result
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = INTEGER (Read)
`````````````````````
The number of the Frame axis for which formatting is to be performed
(axis numbering starts at 1 for the first axis).



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



THIS = LITERAL (Read)
`````````````````````
An NDF, FITS file or text file holding the Frame. If an NDF is
supplied, the current Frame of the WCS FrameSet will be used. If a
FITS file is supplied, the Frame corresponding to the primary axis
descriptions will be used.



VALUE = GROUP (Read)
````````````````````
A comma-separated list of floating point values to be formatted. A
text file may be specified by preceeding the name of the file with an
up arrow character "^". If the supplied value ends with a minus sign,
the user is re-prompted for additional values.



RESULT = LITERAL (Read)
```````````````````````
The name of a text file in which to put the formatted axis values. No
file is produced if a null (!) value is supplied. One axis value is
stored on each line of the file. [!]



Copyright
~~~~~~~~~
Copyright (C) 2003 Central Laboratory of the Research Councils. All
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


