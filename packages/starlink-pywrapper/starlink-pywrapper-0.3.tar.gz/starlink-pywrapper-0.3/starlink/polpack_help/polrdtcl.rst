

POLRDTCL
========


Purpose
~~~~~~~
Reads a text file holding the contents of a specified catalogue in the
form of a Tcl code frament and produces an output catalogue


Description
~~~~~~~~~~~
This application reads a description of a POLPACK catalogue supplied
in the form created by POLWRTCL, and creates an output catalogue.
Other information (e.g. WCS etc) is copied from a second specified
catalogue.


Usage
~~~~~


::

    
       polrdtcl in ref out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = LITERAL (Read)
```````````````````
The name of the input text file holding the Tcl code.



REF = LITERAL (Read)
````````````````````
The name of an existing catalogue from which extra information should
be copied. If none is supplied, no extra information is stored in the
output catalogue.



OUT = LITERAL (Read)
````````````````````
The name of the output catalogue.



Copyright
~~~~~~~~~
Copyright (C) 2000 Central Laboratory of the Research Councils


