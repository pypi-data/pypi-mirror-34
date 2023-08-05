

HISCOM
======


Purpose
~~~~~~~
Adds commentary to the history of an NDF


Description
~~~~~~~~~~~
This task allows application-independent commentary to be added to the
history records of an NDF. The text may be read from a text file or
obtained through a parameter.


Usage
~~~~~


::

    
       hiscom ndf [mode] { file=?
                         { comment=?
                        mode
       



ADAM parameters
~~~~~~~~~~~~~~~



COMMENT = LITERAL (Read)
````````````````````````
A line of commentary limited to 72 characters. If the value is
supplied on the command line only that line of commentary will be
written into the history. Otherwise repeated prompting enables a
series of commentary lines to be supplied. A null value (!) terminates
the loop. Blank lines delimit paragraphs. Paragraph wrapping is
enabled by parameter WRAP. There is no suggested default to allow more
room for entering the value.



DATE = LITERAL (Read)
`````````````````````
The date and time to associated with the new history record. Normally,
a null (!) value should be supplied, in which case the current UTC
date and time will be used. If a value is supplied, it should be in
one of the following forms.
Gregorian Calendar Date --- With the month expressed either as an
integer or a 3-character abbreviation, and with optional decimal
places to represent a fraction of a day ("1996-10-2" or "1996-Oct-2.6"
for example). If no fractional part of a day is given, the time refers
to the start of the day (zero hours).
Gregorian Date and Time --- Any calendar date (as above) but with a
fraction of a day expressed as hours, minutes and seconds ("1996-Oct-2
12:13:56.985" for example). The date and time can be separated by a
space or by a "T" (as used by ISO 8601 format).
Modified Julian Date --- With or without decimal places ("MJD 54321.4"
for example).
Julian Date --- With or without decimal places ("JD 2454321.9" for
example). [!]



FILE = FILENAME (Read)
``````````````````````
Name of the text file containing the commentary. It is only accessed
if MODE="File".



MODE = LITERAL (Read)
`````````````````````
The interaction mode. The allowed values are described below.
"File" --- The commentary is to be read from a text file. The
formatting and layout of the text is preserved in the history unless
WRAP=TRUE and there are lines longer than the width of the history
records. "Interface" --- The commentary is to be supplied through a
parameter. See parameter COMMENT.
["Interface"]



NDF = (Read and Write)
``````````````````````
The NDF for which commentary is to be added to the history.



WRAP = _LOGICAL (Read)
``````````````````````
WRAP=TRUE requests that the paragraphs of comments are wrapped to make
as much text fit on to each line of the history record as possible.
WRAP=FALSE means that the commentary text beyond the width of the
history records (72 characters) is lost. If a null (!) value is
supplied, the value used is TRUE when MODE="Interface" and FALSE if
MODE="File". [!]



Examples
~~~~~~~~
hiscom frame256 comment="This image has a non-uniform background"
This adds the comment "This image has a non-uniform background" to the
history records of the NDF called frame256.
hiscom ndf=eso146-g14 comment="This galaxy is retarded" mode=i
This adds the comment "This galaxy is retarded" to the history records
of the NDF called eso146-g14.
hiscom hh14_k file file=ircam_info.lis
This reads the file ircam_info.lis and places the text contained
therein into the history records of the NDF called hh14_k. Any lines
longer than 72 characters are truncated to that length.
hiscom hh14_k file file=ircam_info.lis wrap
As the previous example except the text in each paragraph is wrapped
to a width of 72 characters within the history records.



Notes
~~~~~


+ A HISTORY component is created if it does not exist within the NDF.
The width of the history record is 72 characters.
+ An error will result if the current history update mode of the NDF
is "Disabled", and no commentary is written. Otherwise the commentary
is written at the priority equal to the current history update mode.
+ A warning messages (at the normal reporting level) is issued if
lines in the text file are too long for the history record and
WRAP=FALSE, though the first 72 characters are stored.
+ The maximum line length in the file is 200 characters.
+ Paragraphs should have fewer than 33 lines. Longer ones will be
  divided.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: HISLIST, HISSET, NDFTRACE.


Copyright
~~~~~~~~~
Copyright (C) 1995 Central Laboratory of the Research Councils.
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
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


