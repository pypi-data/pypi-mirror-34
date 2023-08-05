

POLEXP
======


Purpose
~~~~~~~
Copies information from the POLPACK extension to named FITS keywords


Description
~~~~~~~~~~~
This application copies information from the POLPACK extension of a
group of NDFs, into the corresponding FITS extensions. It is intended
primarily for use when converting NDFs created by POLPACK into a
foreign data format. Appropriate FITS header cards are written to the
FITS extensions of the NDFs, replacing any existing cards for the same
keywords. The keywords used are listed below. Information exported to
the FITS extension can be imported back into the POLPACK extension
using POLIMP.


Usage
~~~~~


::

    
       polexp in
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
A group of data files. This may take the form of a comma separated
list of file names, or any of the other forms described in the help on
"Group Expressions".



NAMELIST = LITERAL (Read)
`````````````````````````
The name of a file to create containing a list of the successfully
processed NDFs. This file can be used when specifying the input NDFs
for subsequent applications. No file is created if a null (!) value is
given. [!]



Examples
~~~~~~~~
polexp in=^names.lis
This example processes the NDFs listed in the text file "names.lis".
The information stored in the POLPACK extension of each is exported to
the FITS extension.



FITS Keywords
~~~~~~~~~~~~~
The following FITS keywords are created. The POLPACK extension item
stored in the keyword is shown in parentheses (see POLIMP for a
description of these extension items):

+ PPCKANGR (ANGROT - derived from the WCS POLANAL Frame)
+ PPCKANLA (ANLANG)
+ PPCKEPS (EPS)
+ PPCKFILT (FILTER)
+ PPCKIMID (IMGID)
+ PPCKRAY (RAY)
+ PPCKSTOK (STOKES)
+ PPCKT (T)
+ PPCKWPLT (WPLATE)
+ PPCKVERS (VERSION)




Copyright
~~~~~~~~~
Copyright (C) 2009 Science & Technology Facilities Council. Copyright
(C) 1998 Central Laboratory of the Research Councils All Rights
Reserved.


