

CUBE2LONG
=========


Purpose
~~~~~~~
To take a longslit spectrum from a non-sorted TAURUS cube


Description
~~~~~~~~~~~
This uses cubic spline interpolation to create a 2-d file from a 3-d
file, given a location, angle and length.


Parameters
~~~~~~~~~~
CUBE = FILE (Read) Sorted TAURUS cube XPOINT = REAL (Read) X point
anywhere on slit YPOINT = REAL (Read) Y point anywhere on slit ANGLE =
REAL (Read) Position angle (degrees) OUTPUT = FILE (Write) Output
longslit spectrum


