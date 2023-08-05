

CSUB
====


Purpose
~~~~~~~
To subtract a continuum from 2 dimensional data


Description
~~~~~~~~~~~
A polynomial is fitted to the continuum and this is subtracted. As
with VIG, lines can be excluded from the polynomial fitting. CSUB
stores the polynomial fitting coefficients in the actual data file.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) Name of image for input OLD = LOGICAL (Read) Old
coefficients are to be used for correction OUTPUT = FILE (Write) Name
of output file OUTPUT is the name of the resulting spectrum. If OUTPUT
is the same as INPUT the data in the input file will be modified in
situ. Otherwise a new file will be created.


