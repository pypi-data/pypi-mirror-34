

TRIMFILE
========


Purpose
~~~~~~~
Creates a copy of an HDS file without unused space


Description
~~~~~~~~~~~
Certain changes to HDS files may cause them to contain unused space,
deleted or temporary structures, etc. This routine will create a new
copy of the file which will only contain actually used structures.
This is in fact only a call to HDS_COPY.


Usage
~~~~~


::

    
       trimfile in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = HDSOBJECT (Read)
`````````````````````
The HDS file suspected to contain a lot of garbage. The default
extension is .sdf. For other extensions use the @-sign and double
quotes as in @"file.dst".



OUT = _CHAR (Read)
``````````````````
The name of the new, clean copy of the HDS file. The default extension
is .sdf. For other extensions just specify them as in file2.dst or
"file2.dst", but not @"file2.dst".



