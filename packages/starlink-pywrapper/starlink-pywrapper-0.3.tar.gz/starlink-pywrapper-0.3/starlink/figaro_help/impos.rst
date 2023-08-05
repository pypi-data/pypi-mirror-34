

IMPOS
=====


Purpose
~~~~~~~
Input positions from a file to the environment variables used by
CENTERS


Description
~~~~~~~~~~~
Input a list of positions from a file to the environment variables
from which CENTERS obtains its input.
CENTERS requires a list of approximate X,Y input positions which it
reads from environment variables. Usually this list is created
interactively with ICUR or IGCUR. IMPOS creates the list by reading it
from a text file, thus allowing CENTERS to be used non-interactively.
The input file is free-format, with one X,Y position per line. The X
and Y values should be separated by one or more spaces and be
expressed in pixels. Up to a hundred positions may be included.


Usage
~~~~~


::

    
       impos file-name
       



ADAM parameters
~~~~~~~~~~~~~~~



INPFLE = _CHAR (Read)
`````````````````````
Name of the input file containing the list of positions.



XPIXELS = _REAL (Write)
```````````````````````
List of X coordinates (pixels).



YPIXELS = _REAL (Write)
```````````````````````
List of Y coordinates (pixels).



NPIXELS = _REAL (Write)
```````````````````````
Number of points in the list.



Examples
~~~~~~~~
The contents of an example input file containing positions for

three objects might be:
103.4 67.8 231.6 134.5 246.7 89.2



Bugs
~~~~
None known.


