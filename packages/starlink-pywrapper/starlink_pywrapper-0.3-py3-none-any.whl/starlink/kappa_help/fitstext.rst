

FITSTEXT
========


Purpose
~~~~~~~
Creates an NDF FITS extension from a text file


Description
~~~~~~~~~~~
This application takes a version of a FITS header stored in a text
file, and inserts it into the FITS extension of an NDF. The header is
not copied verbatim as some validation of the headers as legal FITS
occurs. An existing FITS extension is removed.


Usage
~~~~~


::

    
       fitstext ndf file
       



ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read and Write)
``````````````````````````
The name of the NDF to store the FITS header information.



FILE = FILENAME (Read)
``````````````````````
The text file containing the FITS headers. Each record should be the
standard 80-character `card image'. If the file has been edited care
is needed to ensure that none of the cards are wrapped onto a second
line.



Examples
~~~~~~~~
fitstext hh73 headers.lis
This places the FITS headers stored in the text file called
headers.lis in the FITS extension of the NDF called hh73.



Notes
~~~~~


+ The validation process performs the following checks on each header
`card': a) the length of the header is no more than 80 characters,
otherwise it is truncated; b) the keyword only contains uppercase
Latin alphabetic characters, numbers, underscore, and hyphen (the
header will not be copied to the extension except when the invalid
characters are lowercase letters); c) value cards have an equals sign
in column 9 and a space in column 10; d) quotes enclose character
values; e) single quotes inside string values are doubled; f)
character values are left justified to column 11 (retaining leading
blanks) and contain at least 8 characters (padding with spaces if
necessary); g) non-character values are right justified to column 30,
except for non-mandatory keywords which have a double-precision value
requiring more than 20 digits; h) the comment delimiter is in column
32 or two characters following the value, whichever is greater; i) an
equals sign in column 9 of a commentary card is replaced by a space;
and j) comments begin at least two columns after the end of the
comment delimiter.
+ The validation issues warning messages at the normal reporting level
for violations a), b), c), d), and i).
+ The validation can only go so far. If any of your header lines are
  ambiguous, the resulting entry in the FITS extension may not be what
  you intended. Therefore, you should inspect the resulting FITS
  extension using the command FITSLIST before exporting the data. If
  there is something wrong, you may find it convenient to use command
  FITSEDIT to make minor corrections.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSEDIT, FITSEXP, FITSLIST; CONVERT: NDF2FITS.


Copyright
~~~~~~~~~
Copyright (C) 1994 Science & Engineering Research Council. Copyright
(C) 1996, 1998 Central Laboratory of the Research Councils. All Rights
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


