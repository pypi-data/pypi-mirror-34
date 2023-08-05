

IMAGE
=====


Purpose
~~~~~~~
Display an image


Description
~~~~~~~~~~~
This routine displays an image on the image display. Note that the
colour tables are not changed by this command, nor is the device
reset. The data can be logarithmised and/or histogram-optimised prior
to display.


Usage
~~~~~


::

    
       image image ystart yend xstart xend low high xplaces yplaces
          atx aty xorigin yorigin xpixels ypixels optimize=?
          [autoscale=? negative=? aspect=? log=? erase=? hardcopy=?]
       



ADAM parameters
~~~~~~~~~~~~~~~



IMAGE = _CHAR (Read)
````````````````````
The image to be displayed.



YSTART = _REAL (Read)
`````````````````````
The first Y value to be displayed.



YEND = _REAL (Read)
```````````````````
The last Y value to be displayed.



XSTART = _REAL (Read)
`````````````````````
The first X value to be displayed.



XEND = _REAL (Read)
```````````````````
The last X value to be displayed.



LOW = _REAL (Read)
``````````````````
The lowest data value to be displayed. [0.]



HIGH = _REAL (Read)
```````````````````
The highest data value to be displayed. [1000.]



XPLACES = _INTEGER (Read)
`````````````````````````
If not 0, the number of sub-displays in X. Enter 0 to specify a
display region explicitly through X/YORIGIN and X/YPIXELS. [1]



YPLACES = _INTEGER (Read)
`````````````````````````
If not 0, the number of sub-displays in Y. [1]



ATX = _INTEGER (Read)
`````````````````````
Which sub-display in X to use, counting from 1. [1]



ATY = _INTEGER (Read)
`````````````````````
Which sub-display in Y to use, counting from 1. [1]



XORIGIN = _INTEGER (Read)
`````````````````````````
The first pixel in X to be used for display, counting from 0. [0]



YORIGIN = _INTEGER (Read)
`````````````````````````
The first pixel in Y to be used for display, counting from 0. [0]



XPIXELS = _INTEGER (Read)
`````````````````````````
How many pixels to use in X.



YPIXELS = _INTEGER (Read)
`````````````````````````
How many pixels to use in Y.



OPTIMIZE = _REAL (Read)
```````````````````````
The degree of histogram optimisation to be applied. 0 for no
optimsation, 1 for full optimisation. Optimisation is applied after
taking common logarithms if LOG is true. [0.5]



AUTOSCALE = _LOGICAL (Read)
```````````````````````````
True if the display thresholds are to be the minimum and maximum data
values in the subset to be displayed. [T]



NEGATIVE = _LOGICAL (Read)
``````````````````````````
True if the auto-scaling should be reversed. [F]



ASPECT = _LOGICAL (Read)
````````````````````````
True if data pixels are to be displayed as square pixels. [T]



LOG = _LOGICAL (Read)
`````````````````````
True if the common logarithm of data is to be displayed rather than
the data themselves. [F]



ERASE = _LOGICAL (Read)
```````````````````````
True if the display is to be erased before display. [F]



HARDCOPY = _LOGICAL (Read)
``````````````````````````
True if the display is to be on the device set by the HARD command.
The "idev" device is commonly a screen display, while the "hard"
device is commonly a printer.
Be wary of the NEGATIVE keyword in conjunction with HARDCOPY: A
"positive" display will display the minimum as white and the maximum
as black, and it in that sense negative. If you set the NEGATIVE
keyword true, your hard copy will be "positive".



IDEV = _CHAR (Read)
```````````````````
The name of the imaging device, normally got from a global parameter
which was set with the IDEV command.



HARD = _CHAR (Read)
```````````````````
The name of the "hard" device, normally got from a global parameter
which was set with the HARD command.



IMARRAY( 12 ) = _REAL (Write)
`````````````````````````````
Information about the displayed part of the image and the part of the
display used.



IMFILE = _CHAR (Write)
``````````````````````
File name of the image displayed.



