

FITSEXIST
=========


Purpose
~~~~~~~
Inquires whether or not a keyword exists in a FITS extension


Description
~~~~~~~~~~~
This application reports whether or not a keyword exists in an the
FITS extension of an NDF file.


Usage
~~~~~


::

    
       fitsexist ndf keyword
       



ADAM parameters
~~~~~~~~~~~~~~~



EXISTS = _LOGICAL (Write)
`````````````````````````
The result of the last existence test.



KEYWORD = LITERAL (Read)
````````````````````````
The name of the keyword to be edited in the FITS extension. A name may
be compound to handle hierarchical keywords, and it has the form
keyword1.keyword2.keyword3 etc. The maximum number of keywords per
FITS card is 20. Each keyword must be no longer than 8 characters, and
be a valid FITS keyword comprising only alphanumeric characters,
hyphen, and underscore. Any lowercase letters are converted to
uppercase and blanks are removed before insertion, or comparison with
the existing keywords.
KEYWORD may have an occurrence specified in brackets [] following the
name. This enables editing of a keyword that is not the first
occurrence of that keyword, or locate a edited keyword not at the
first occurrence of the positional keyword. Note that it is not normal
to have multiple occurrences of a keyword in a FITS header, unless it
is blank, COMMENT or HISTORY. Any text between the brackets other than
a positive integer is interpreted as the first occurrence.



NDF = NDF (Read)
````````````````
The NDF to be tested for the presence of the FITS keyword.



Examples
~~~~~~~~
fitsexist abc bscale
This reports TRUE or FALSE depending on whether or not the FITS
keyword BSCALE exists in the FITS extension of the NDF called abc.
fitsexist ndf=abc keyword=date[2]
This reports TRUE or FALSE depending on whether or not the FITS there
are at least two occurrences of the keyword DATE.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSEDIT, FITSHEAD, FITSLIST, FITSVAL.


Copyright
~~~~~~~~~
Copyright (C) 2005 Particle Physics & Astronomy Research Council. All
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


