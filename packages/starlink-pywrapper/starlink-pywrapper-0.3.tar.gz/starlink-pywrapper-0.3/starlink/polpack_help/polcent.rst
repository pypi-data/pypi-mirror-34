

POLCENT
=======


Purpose
~~~~~~~
Find the centroid of a set of positions in an image


Description
~~~~~~~~~~~
This routine is equivalent to CCDPACK:FINDCENT, but is simpler and
therefore faster. It is tailored to the needs of the Polka
application, and is not intended for public use. The algorithm used by
CCG1_CENR has been modified to improve the background subtraction
prior to forming the marginal profiles.


ADAM parameters
~~~~~~~~~~~~~~~



ISIZE = _INTEGER (Read)
```````````````````````
The size of a box side (in pixels) centered on current position which
will be used to form the marginal profiles used to estimate the
centroid. [9]



MAXITER = _INTEGER (Read)
`````````````````````````
The maximum number of iterations which may be used in estimating the
centroid. Only used if the tolerance criterion is not met in this
number of iterations. [3]



MAXSHIFT = _DOUBLE (Read)
`````````````````````````
The maximum shift (in pixels) allowed from an initial position. [5.5]



NDF = NDF (Read)
````````````````
The NDF in which to search for the image feature.



POSITIVE = _LOGICAL (Read)
``````````````````````````
If TRUE then the image features have increasing values otherwise they
are negative. [TRUE]



TOLER = _DOUBLE (Read)
``````````````````````
The required tolerance in the positional accuracy of the centroid. On
each iteration the box of data from which the centroid is estimated is
updated. If the new centroid does not differ from the previous value
by more than this amount (in X and Y) then iteration stops. Failure to
meet this level of accuracy does not result in the centroid being
rejected, the centroiding process just stops after the permitted
number of iterations (MAXITER). [0.05]



INFILE = LITERAL (Read)
```````````````````````
The name of a text file containing the the X and Y values to be used
as the initial guess at accurate positions. Each line should hold the
X value followed by the Y value separated by spaces.



OUTFILE = LITERAL (Read)
````````````````````````
The name of a text file to create containing the accurate positions.
Each line will hold the accurate X and Y values for the corresponding
input position, separated by spaces. Positions which cannot be found
are set to -100000 (both X and Y).



XYOUT = LITERAL (Write)
```````````````````````
A string holding the last accurate X and Y values, separated by a
space.



Copyright
~~~~~~~~~
Copyright (C) 1998 Central Laboratory of the Research Councils


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ Bad pixels can be handled. The NDF is accessed as an array of single
  precision values.




