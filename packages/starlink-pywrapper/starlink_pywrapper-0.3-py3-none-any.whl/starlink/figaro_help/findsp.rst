

FINDSP
======


Purpose
~~~~~~~
Locate spectra in fibre frame


Description
~~~~~~~~~~~
This routine locates spectra in a large fibre frame and produces a
polynomial file. The polynomial file has a version 2 format. Version 1
format uses the coefficients of a Chebyshev series, while version 2
format uses ordinary polynomial coeffients.
The technique of this routine is to
1 Compress the data array, 2 Follow ridges from start positions by
centroiding, 3 Fit a polynomial Y(X) to the centroids, 4 Write the
polynomial coefficients to a text file.
The text file can be read by the applications OVERPF and POLEXT. Those
applications will also be able to read text files in version 1 format.


ADAM parameters
~~~~~~~~~~~~~~~



IMAGE = LITERAL (Read)
``````````````````````
The fibre frame - one with distorted fibre spectra equally spaced.



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



NUMFIB = _INTEGER (Read)
````````````````````````
The total number of fibres used in the observation, including any dud
fibres.



NORDER = _INTEGER (Read)
````````````````````````
The order of the polynomial to be fitted along each spectrum. The
default is 6 and the maximum order allowed is 10. An even order is
suggested by the presence of 'barrel' distortion.



NPTS = _INTEGER (Read)
``````````````````````
The image is compressed in the X (wavelength) direction before the
centroids are determined. This parameter fixes the number X-direction
bins in the compressed frame. This parameter also by definition is the
number of points along the spectrum to be used for fitting the
polynomial. Choice of this parameter is a trade-off between having
enough points along the spectra that the the curved spectra can be
reliably followed and having enough S/N in the compressed image to
determine a reliable centroid.



FWCENT = _INTEGER (Read)
````````````````````````
The 'full-width' of the centroiding range in the vertical direction.



CFW = _REAL (Read)
``````````````````
To get the initial centre for the centroiding the program does a
linear extrapolation from the last two centroids. The program searches
out from the previously determined central centroids. In order to
supress large fluctuations that sometimes occur it is necessary to
have damping in the extrapolation. If fact this 'Centroid Weighting
Function' parameter is the constant that the true gradient of the
linear extrapolation is multiplied by to guess the next centroid.
Hence a value of CFW less than 1 damps the extrapolation toward the
horizontal.



YFIRST = _REAL (Read)
`````````````````````
The position of the centre of the first spectrum. This is expressed as
the number of pixels up from the bottom of the image as viewed on the
ARGS. Note that the default is only a guess from the size of the
image.



YSEP = _REAL (Read)
```````````````````
The average number of pixels separating each spectrum in the input
image. Again the default value represents a guess.



PFILE = LITERAL (Write)
```````````````````````
The file to which the results of the spectrum fitting performed by
FINDSP is to be written. If no extension is specified, `.pol' is used.



ADJUST = _LOGICAL (Read)
````````````````````````
Used to ask whether centroid start points need adjustment.



CHGPAR = _LOGICAL (Read)
````````````````````````
Used to ask whether analysis to be repeated with changed parameters.



REJECT = _REAL (Read)
`````````````````````
The number of a fibre to be rejected.



CHGREJ = _LOGICAL (Read)
````````````````````````
Used to ask whether the set of fibres to be rejected should be
revised.



