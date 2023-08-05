

ICUR
====


Purpose
~~~~~~~
Inspect image with cursor


Description
~~~~~~~~~~~
This routine displays the position and data value according to the
position of the cursor on the image display. Up to 50 pixel positions
can be recorded for later use by other applications.
Use the cursor to select a position in the image previously displayed
with the application IMAGE. Press one of the following:
D to display coordinates and pixel value, <space> to record pixel
position, Q to quit the application.
Any other key is treated like 'D', alphabetic keys are case-
insensitive.


ADAM parameters
~~~~~~~~~~~~~~~



IDEV = _CHAR (Read)
```````````````````
The name of the imaging device, normally got from a global parameter
which was set with the IDEV command.



IMARRAY( 12 ) = _REAL (Read)
````````````````````````````
Information about the displayed part of the image and the part of the
display used - set by IMAGE or similar.



IMFILE = _CHAR (Read)
`````````````````````
File name of the image displayed - set by IMAGE or similar.



XPIXELS( 50 ) = _REAL (Write)
`````````````````````````````
The pixel numbers in X for the points indicated by the cursor.



YPIXELS( 50 ) = _REAL (Write)
`````````````````````````````
The pixel numbers in Y for the points indicated by the cursor.



NPIXELS = _REAL (Write)
```````````````````````
The number of points selected by the cursor. Note: if no points are
selected, the values of NPIXELS, XPIXELS, YPIXELS are left unchanged.



Implementation Status
~~~~~~~~~~~~~~~~~~~~~
This routine does not provide a continuous display of coordinates and
image value.


