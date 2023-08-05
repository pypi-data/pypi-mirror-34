

FITSEXP
=======


Purpose
~~~~~~~
Exports NDF-extension information into an NDF FITS extension


Description
~~~~~~~~~~~
This application places the values of components of an NDF extension
into the FITS extension within the same NDF. This operation is needed
if auxiliary data are to appear in the header of a FITS file converted
from the NDF. The list of extension components whose values are to be
copied, their corresponding FITS keyword names, optional FITS inline
comments, and the location of the new FITS header are specified in a
"keyword translation table" held in a separate text file.


Usage
~~~~~


::

    
       fitsexp ndf table
       



ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read and Write)
``````````````````````````
The NDF in which the extension data are to be exported to the FITS
extension.



TABLE = FILE (Read)
```````````````````
The text file containing the keyword translation table. The format of
this file is described under "Table Format".



Examples
~~~~~~~~
fitsexp datafile fitstable.txt
This writes new FITS-extension elements for the NDF called datafile,
creating the FITS extension if it does not exist. The selection of
auxiliary components to export to the FITS extension, their keyword
names, locations, and comments are under the control of a keyword
translation table held in the file fitstable.txt.



Notes
~~~~~


+ Requests to assign values to the following reserved keywords in the
FITS extension are ignored: SIMPLE, BITPIX, NAXIS, NAXISn, EXTEND,
PCOUNT, GCOUNT, XTENSION, BLOCKED, and END.
+ Only scalar or one-element vector components may be transferred to
the FITS extension.
+ The data type of the component selects the type of the FITS value.
+ If the destination keyword exists, the existing value and comment
are replaced with the new values.
+ If an error is found within a line, processing continues to the next
line and the error reported.
+ To be sure that the resultant FITS extension is what you desired,
  you should inspect it using the command fitslist before exporting the
  data. If there is something wrong, you may find it convenient to use
  command FITSEDIT to make minor corrections.




References
~~~~~~~~~~
"A User's Guide for the Flexible Image Transport System (FITS)",
NASA/Science Office of Science and Technology (1994).


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSEDIT, FITSHEAD, FITSLIST, FITSMOD; CONVERT: NDF2FITS.


Table Format
~~~~~~~~~~~~
The keyword translation table should be held in a text file, with one
extension component specified per line. Each line should contain two
or three fields, separated by spaces and/or tabs, as follows.


+ Field 1: The name of the input extension component whose value is to
be copied to the FITS extension. For example, CCDPACK.FILTER would
copy the value of the component called FILTER in the extension called
CCDPACK; and IRAS90.ASTROMETRY.EQUINOX would copy the value of
component EQUINOX in the structure ASTROMETRY in the extension IRAS90.
The extension may not be FITS.
+ Field 2: The name of the FITS keyword to which the value is to be
copied. Hierarchical keywords are not permissible. The keyword name
may be followed by a further keyword name in parentheses (and no
spaces). This second keyword defines the card before which the new
keyword is to be placed. If this second keyword is not present in the
FITS extension or is not supplied, the new header card is placed at
the end of the existing cards, but immediately before any END card.
For example, EQUINOX(EPOCH) would write the keyword EQUINOX
immediately before the existing card with keyword EPOCH. FITS keywords
are limited to 8 characters and may only comprise uppercase alphabetic
characters, digits, underscore, and hyphen. While it is possible to
have multiple occurrences of the same keyword in a FITS header, it is
regarded as bad practice. For this and efficiency reasons, this
programme only looks for the first appearance of a keyword when
substituting the values, and so only the last value inserted appears
in the final FITS extension. (See "Implementation Status".)
+ Field 3: The comment to appear in the FITS header card for the
  chosen keyword. This field is optional. As much of the comment will
  appear in the header card as the value permits up to a maximum of 47
  characters.

Comments may appear at any point in the table and should begin with an
exclamation mark. The remainder of the line will then be ignored.


Timing
~~~~~~
Approximately proportional to the number of FITS keywords to be
translated.


Copyright
~~~~~~~~~
Copyright (C) 1994 Science & Engineering Research Council. Copyright
(C) 2004 Central Laboratory of the Research Councils. All Rights
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ The replacements are made in blocks of 32 to reduce the number of
time-consuming shuffles of the FITS extension. Thus it is possible to
locate a new keyword before another keyword, provided the latter
keyword appears in an earlier block, though reliance on this feature
is discouraged; instead run the application twice.
+ For each block the application inserts new cards or relocates old
  ones, marking each with different tokens, and then sorts the FITS
  extension into the requested order, removing the relocated cards. It
  then inserts the new values. If there are multiple occurrences of a
  keyword, this process can leave behind cards having the token value
  '{undefined}'.




