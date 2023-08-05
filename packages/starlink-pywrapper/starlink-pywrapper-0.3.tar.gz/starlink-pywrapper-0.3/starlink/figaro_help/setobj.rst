

SETOBJ
======


Purpose
~~~~~~~
Assign value to an HDS primitive


Description
~~~~~~~~~~~
This routine assigns a specified (numeric or string) value to an
existing HDS primitive. The destination object must exist. It can be a
primitive scalar or a cell in a primitive array.


Usage
~~~~~


::

    
       setobj value object
       



ADAM parameters
~~~~~~~~~~~~~~~



VALUE = LITERAL (Read)
``````````````````````
The value the scalar primitive HDS object is to assume.



OBJECT = HDSOBJECT (Read)
`````````````````````````
The HDS object to be modified. Specify beginning with directory and
file name in the syntax of the operating system, followed by the dot-
separated structure hierarchy. Elements of structure arrays are
specified in ordinary brackets ().



Examples
~~~~~~~~
setobj value=90. object=file.MORE.FIGARO.TIME
Store the number or string 90 in the existing scalar HDS object
MORE.FIGARO.TIME in the file "file".



