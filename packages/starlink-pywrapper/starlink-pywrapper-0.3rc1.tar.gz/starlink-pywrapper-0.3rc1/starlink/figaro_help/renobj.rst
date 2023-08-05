

RENOBJ
======


Purpose
~~~~~~~
Change the name or location of an object within an HDS file


Description
~~~~~~~~~~~
This routine either renames an HDS object in place or moves it to a
different place in the structure hierarchy of the same file. It is not
possible to reshape objects, i.e. to change their dimensions or
dimensionality.


Usage
~~~~~


::

    
       renobj source=? destin=?
       



ADAM parameters
~~~~~~~~~~~~~~~



SOURCE = HDSOBJECT (Read)
`````````````````````````
The existing HDS object to be renamed. Specify beginning with
directory and file name in the syntax of the operating system,
followed by the dot-separated structure hierarchy. Elements of
structure arrays are specified in ordinary brackets (). An array
element cannot be renamed.



DESTIN = HDSOBJECT (Read)
`````````````````````````
The new name for the HDS object. Specify beginning with directory and
file name in the syntax of the operating system, followed by the dot-
separated structure hierarchy. Elements of structure arrays are
specified in ordinary brackets (). The destination cannot be an array
element. The destination object must not exist beforehand.



Examples
~~~~~~~~
renobj source=file.MORE.FIGARO.OBS.TIME destin=file.MORE.FIGARO.TIME
This moves the time specification from .MORE.FIGARO.OBS one level up
into .MORE.FIGARO.
renobj source=file.ERRORS destin=file.VARIANCE
This renames the object ERRORS into VARIANCE, but the location remains
the same. (The contents remain the same anyway.)



