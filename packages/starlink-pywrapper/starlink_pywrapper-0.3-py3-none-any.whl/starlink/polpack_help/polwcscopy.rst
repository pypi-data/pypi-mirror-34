

POLWCSCOPY
==========


Purpose
~~~~~~~
Copies WCS from one catalogue to another


Description
~~~~~~~~~~~
This application creates a copy of the specified input catalogue. If
the input catalogue does not include any WCS information, then the WCS
information from a specified reference catalogue is included in the
output catalogue.
A typical use is to add WCS information back into a catalogue that has
been modified using STILTS or TOPCAT. For instance, if STILTS or
TOPCAT is used to create a new catalogue containing vectors selected
from an input POLPACK catalogue, then the new catalogue created by
STILTS or TOPCAT will not contain WCS information in a form that can
be used by POLPACK, KAPPA or GAIA. This application can then be used
to add WCS information back into the catalogue created by STILTS or
TOPCAT, copying the WCS from the original POLPACK catalogue.


Usage
~~~~~


::

    
       polwcscopy in out ref
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = LITERAL (Read)
```````````````````
The name of the input catalogue. A file type of .FIT is assumed if
none is provided.



OUT = LITERAL (Write)
`````````````````````
The name of the output catalogue. A file type of .FIT is assumed if
none is provided. This will be a copy of IN. If IN contains no WCS,
then the WCS in OUT will be copied from REF.



REF = LITERAL (Read)
````````````````````
The name of the input catalogue from which WCS is to be read. A file
type of .FIT is assumed if none is provided. An error is reported if
this catalogue does not contain any WCS information.



Copyright
~~~~~~~~~
Copyright (C) 2017 East Asian Observatory. All Rights Reserved.


