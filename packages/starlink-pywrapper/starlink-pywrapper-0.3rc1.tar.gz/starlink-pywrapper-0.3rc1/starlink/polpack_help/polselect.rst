

POLSELECT
=========


Purpose
~~~~~~~
Select vectors from a catalogue


Description
~~~~~~~~~~~
This application creates an output catalogue that contains a subset of
the vectors in the specified input catalogue. The subset can be
specified in various ways (see parameter MODE):


+ using the bad pixels in a reference image to mask out unwanted
vectors
+ using ARD or AST region specifications to select the required
vectors
+ using an algebraic expression to select the required vectors on the
  basis of their column values




Usage
~~~~~


::

    
       polselect in out mode
       



ADAM parameters
~~~~~~~~~~~~~~~



EXP = LITERAL (Read)
````````````````````
This parameter is only used if parameter MODE is set to "EXPRESSION".
It should be set to a boolean expression that uses column names from
the input catalogue as variables. It should have the format used by
the CURSA 'CATSELECT' command (see sun/190). In general, the
arithmetic and boolean operators available in either C and Fortran can
be used (e.g. '.ge.', '>=', '.and.', '&&', etc.), as can the usual
mathematical functions (e.g. 'abs', 'tan', 'pow', etc). A vector is
selected if the expression evaluates to a true value.



IN = LITERAL (Read)
```````````````````
The name of the input catalogue. A file type of .FIT is assumed if
none is provided.



INVERT = _LOGICAL (Read)
````````````````````````
If FALSE, all selected vectors are copied to the output catalogue. If
TRUE, all unselected vectors are copied to the output catalogue.
[FALSE]



MASK = NDF (Read)
`````````````````
This parameter is only used if parameter MODE is set to "MASK". It
specifies the two-dimensional NDF to be used as a mask to select the
required vectors. Vectors corresponding to good pixel values in the
mask are selected. The mask is assumed to be aligned with the
catalogue in pixel coordinates.



MODE = LITERAL (Read)
`````````````````````
Specifies the manner in which the vectors are selected:


+ "MASK": The image specified by parameter MASK is used to select the
vectors. If a vector has a position that corresponds to a good pixel
in MASK, then the vector is selected.
+ "REGION": The ARD or AST region specified by parameter REGION is
used to select the vectors. If a vector falls within the region, then
it is selected.
+ "EXPRESSION": The boolean expression specified by parameter EXP is
  used to select the vectors. If the boolean expression evaluates to
  TRUE for a vector, then the vector is selected.





OUT = LITERAL (Write)
`````````````````````
The name of the output catalogue. A file type of .FIT is assumed if
none is provided.



REF = NDF (Read)
````````````````
This parameter is only used if parameter MODE is set to "REGION". It
specifies the NDF to which the ARD description refers. It is used to
define the pixel coordinate system used by the ARD description. If
null (!) is supplied, it is assumed that the pixel coordinate system
used by the ARD description is the pixel coordinate system of the
input catalogue. [!]



REGION = FILENAME (Read)
````````````````````````
This parameter is only used if parameter MODE is set to "REGION". It
should be set to the name of a text file containing a description of
the region containing the vectors to be selected. This can either be
in the form of an 'ARD description' (see SUN/183), or an 'AST Region'
(see SUN/210).



Copyright
~~~~~~~~~
Copyright (C) 2018 East Asian Observatory. All Rights Reserved.


