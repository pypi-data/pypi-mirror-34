

FITSVAL
=======


Purpose
~~~~~~~
Reports the value of a keyword in the FITS airlock


Description
~~~~~~~~~~~
This application reports the value of a keyword in the FITS extension
(`airlock') of an NDF file. The keyword's value and comment are also
stored in output parameters.


Usage
~~~~~


::

    
       fitsval ndf keyword
       



ADAM parameters
~~~~~~~~~~~~~~~



COMMENT = LITERAL (Write)
`````````````````````````
The comment of the keyword.



KEYWORD = LITERAL (Read)
````````````````````````
The name of an existing keyword in the FITS extension whose value is
to be reported. A name may be compound to handle hierarchical
keywords, and it has the form keyword1.keyword2.keyword3 etc. The
maximum number of keywords per FITS card is 20. Each keyword must be
no longer than 8 characters, and be a valid FITS keyword comprising
only alphanumeric characters, hyphen, and underscore. Any lowercase
letters are converted to uppercase and blanks are removed before
insertion, or comparison with the existing keywords.
KEYWORD may have an occurrence specified in brackets [] following the
name. This enables editing of a keyword that is not the first
occurrence of that keyword, or locate a edited keyword not at the
first occurrence of the positional keyword. Note that it is not normal
to have multiple occurrences of a keyword in a FITS header, unless it
is blank, COMMENT or HISTORY. Any text between the brackets other than
a positive integer is interpreted as the first occurrence.



NDF = NDF (Read)
````````````````
The NDF containing the FITS keyword.



VALUE = LITERAL (Write)
```````````````````````
The value of the keyword.



Examples
~~~~~~~~
fitsval abc bscale
This reports the value of the FITS keyword BSCALE, which is located
within the FITS extension of the NDF called abc.
fitsval ndf=abc keyword=date[2]
This reports the value of the second occurrence FITS keyword DATE,
which is located within the FITS extension of the NDF called abc.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSEDIT, FITSEXIST, FITSHEAD, FITSLIST, FITSMOD.


Copyright
~~~~~~~~~
Copyright (C) 2005 Particle Physics & Astronomy Research Council.
Copyright (C) 2005 Science & Technology Facilities Council. All Rights
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


