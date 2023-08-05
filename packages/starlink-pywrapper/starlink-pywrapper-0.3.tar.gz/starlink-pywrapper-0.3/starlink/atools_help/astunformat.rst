

ASTUNFORMAT
===========


Purpose
~~~~~~~
Read a formatted coordinate value for a Frame axis


Description
~~~~~~~~~~~
This application reads a formatted coordinate value (given as a
literal string) for a Frame axis and displays the equivalent numerical
value. It also displays the number of characters read from the string.
The principle use of this function is in decoding user-supplied input
which contains formatted coordinate values. Free-format input is
supported as far as possible. If input is ambiguous, it is interpreted
with reference to the Frame's attributes (in particular, the Format
string associated with the Frame's axis). This function is, in
essence, the inverse of AST_FORMAT.


Usage
~~~~~


::

    
       astunformat this axis value result
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = _INTEGER (Read)
``````````````````````
The number of the Frame axis for which unformatting is to be performed
(axis numbering starts at 1 for the first axis).



DVAL = _DOUBLE (Write)
``````````````````````
An output parameter left holding the last unformatted value.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



RESULT = LITERAL (Read)
```````````````````````
The name of a text file in which to put the unformatted axis values.
No file is produced if a null (!) value is supplied. One axis value is
stored on each line of the file. [!]



THIS = LITERAL (Read)
`````````````````````
An NDF, FITS file or text file holding the Frame. If an NDF is
supplied, the current Frame of the WCS FrameSet will be used. If a
FITS file is supplied, the Frame corresponding to the primary axis
descriptions will be used.



VALUE = GROUP (Read)
````````````````````
A comma-separated list of formatted axis values to be read. A text
file may be specified by preceeding the name of the file with an up
arrow character "^". If the supplied value ends with a minus sign, the
user is re-prompted for additional values.



Copyright
~~~~~~~~~
Copyright (C) 2006 Central Laboratory of the Research Councils. All
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


