

POLPREP
=======


Purpose
~~~~~~~
Prepare an input image for use by Polka


Description
~~~~~~~~~~~
This application prepares an input image for subsequent use by Polka.
It is called from within the Polka.tcl script and is not intended to
be used directly by users.


Usage
~~~~~


::

    
       polprep in out ref
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF which is to be prepared.



OUT = NDF (Write)
`````````````````
The output NDF data structure containing a prepared copy of IN.



REF = _LOGICAL (Read)
`````````````````````
Should be TRUE if the supplied IN image is the reference image. In
this case the IN image does not need to have a POLPACK extension.



FRAME = LITERAL (Write)
```````````````````````
The Current Frame Domain in the IN image. If REF is FALSE., then a the
string "BADPOL" is returned if the IN image does not have a usable
POLPACK extension.



