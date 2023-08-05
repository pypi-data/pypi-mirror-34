

COPOBJ
======


Purpose
~~~~~~~
Copy an HDS object


Description
~~~~~~~~~~~
This routine creates or modifies an object to be a copy of an existing
HDS object (in the same or a different container file). The
destination object can either be a newly created scalar object or an
existing cell of an array. If it is a cell of a structure array, it
must be an empty structure.


Usage
~~~~~


::

    
       copobj source object
       



ADAM parameters
~~~~~~~~~~~~~~~



SOURCE = HDSOBJECT (Read)
`````````````````````````
The existing HDS object to be copied. Specify beginning with directory
and file name in the syntax of the operating system, followed by the
dot-separated structure hierarchy. Elements of structure arrays are
specified in ordinary brackets ().



OBJECT = HDSOBJECT (Read)
`````````````````````````
The HDS object to be created or modified. Specify beginning with
directory and file name in the syntax of the operating system,
followed by the dot-separated structure hierarchy. Elements of
structure arrays are specified in ordinary brackets (). An array
element (cell) cannot be created, but an exisiting cell can be
modified.



Examples
~~~~~~~~
copobj source=@"file1.dst".Z.DATA object=file2.DATA_ARRAY
Copy the data array from a Figaro DST file into the data array of an
NDF. Note that file2.DATA_ARRAY must not exist beforehand, and that
file2 without DATA_ARRAY is not a legal NDF. So probably this would be
the first action after creation of the empty HDS file "file2".



