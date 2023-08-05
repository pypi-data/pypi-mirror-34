

OVERPF
======


Purpose
~~~~~~~
Overlay polynomial fits on an image


Description
~~~~~~~~~~~
Overlays the Polynominal Fits on an image. Displaying a zoomed part of
the image is possible. To be used with FINDSP and POLEXT.


ADAM parameters
~~~~~~~~~~~~~~~



IMAGE = LITERAL (Read)
``````````````````````
The fibre frame - one with distorted fibre spectra approximately
equally spaced.



BLACK = _REAL (Read)
````````````````````
The data value below which the image display is to have the background
colour. The display is scaled linearly between the data values
specified as BLACK and WHITE.



WHITE = _REAL (Read)
````````````````````
The data value above which the image display is to have the foreground
colour. The display is scaled linearly between the data values
specified as BLACK and WHITE.



PFILE = LITERAL (Read)
``````````````````````
The file containing the polynominal fits. If no extension is
specified, `.pol' is used.



YSTART = _REAL (Read)
`````````````````````
First Y value to be displayed.



YEND = _REAL (Read)
```````````````````
Last Y value to be displayed.



XSTART = _REAL (Read)
`````````````````````
First X value to be displayed.



XEND = _REAL (Read)
```````````````````
Last X value to be displayed.



EXTWID = _REAL (Read)
`````````````````````
The input may be integer or real. An integer input causes edges of
pixels included to be drawn, whereas real input causes trams lines of
width EXTWID to be drawn surrounding each polynomial fit.



REPEAT = _CHAR (Read)
`````````````````````
Used to ask whether a display with different parameters should be
made.



