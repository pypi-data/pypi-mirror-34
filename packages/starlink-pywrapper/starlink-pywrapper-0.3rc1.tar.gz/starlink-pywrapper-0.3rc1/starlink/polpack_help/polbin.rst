

POLBIN
======


Purpose
~~~~~~~
Bins a catalogue containing Stokes parameters


Description
~~~~~~~~~~~
This application creates a new catalogue of polarization vectors by
binning the Stokes parameters in the supplied catalogue. The columns
in the supplied catalogue should correspond to those created by
POLVEC.
The bins used form a grid of equally sized rectangular cells, the
dimensions of each cell being specified by the parameter BOX in terms
of the X and Y columns in the catalogue. Spectropolarimetry data can
also be binned in the frequency axis (see parameter ZBOX). The grid
contains sufficient cells to include all the vector positions included
in the input catalogue. Each position in the output catalogue
corresponds to one of these cells. The Stokes parameters for the cell
are formed by combining together the Stokes parameters of all input
positions which fall within the cell, using the method specified by
the parameter METHOD. The degree of polarization, angle of
polarization, and polarized intensity are then derived from these
combined Stokes parameters. The vector position in the output
catalogue is the position at the centre of the corresponding cell.


Usage
~~~~~


::

    
       polbin in out box [method]
       



ADAM parameters
~~~~~~~~~~~~~~~



BOX( 2 ) = _REAL (Read)
```````````````````````
The x and y bin sizes. These values refer to the coordinate Frame
defined by columns "X" and "Y" and will usually be in units of pixels.
This parameter is not accessed if parameter INTEGRATE is TRUE.
Parameter ZBOX specifies binning along the frequency axis when dealing
with spectropolarimeter data.



DEBIAS = _LOGICAL (Read)
````````````````````````
TRUE if a correction for statistical bias is to be made to percentage
polarization and polarized intensity. The returned variance values are
unchanged. This correction only applies to calculations of linear
polarization, and cannot be used if the input catalogue does not
contain variance values. If a null value (!) is supplied, then the
correction is applied if output variances are being created, and not
otherwise. [!]



IN = LITERAL (Read)
```````````````````
The name of the input catalogue. A file type of .FIT is assumed if
none is provided.



INTEGRATE = LOGICAL_ (Read)
```````````````````````````
If TRUE, then all the input vectors are placed in a single bin. In
this case, parameter BOX is not used and the output catalogue will
contain only a single vector. [FALSE]



METHOD = LITERAL (Read)
```````````````````````
The method to be used when binning Stokes parameters. This may be set
to any unique abbreviation of the following:


+ MEAN -- Mean of the input data values
+ MEDIAN -- Median of the input data values
+ SIGMA -- A sigma clipped mean

In all cases, if variances are available for the input Stokes
parameters, then the reciprocals of these variances will be used to
weight the input Stokes parameters when forming the output Stokes
parameters using the selected method. [MEDIAN]



MINVAL = _INTEGER (Read)
````````````````````````
The minimum number of good input values which must be present in a
cell to create a good output value. [1]



OUT = LITERAL (Read)
````````````````````
The name of the output catalogue. A file type of .FIT is assumed if
none is provided.



RADEC = _LOGICAL (Read)
```````````````````````
If TRUE, columns holding the RA and DEC (FK5, J2000) are added to the
output catalogue, if the input catalogue contains the necessary WCS
information. If FALSE, no RA and DEC columns are written. For large
catalogues, creating RA and DEC columns can cause a significant delay.
[current value]



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations to reject data at. Only used if METHOD
is set to "SIGMA". [4.0]



ZBOX = _REAL (Read)
```````````````````
The bin size along the third (Z) axis in the input catalogue. a Z
column. The supplied value should usually be in units of pixels. This
parameter is not accessed if parameter INTEGRATE is TRUE, or if the
input catalogue does not contain a Z column.



Examples
~~~~~~~~
polbin intab outtab 4
Bins the Stokes parameters in catalogue "intab.FIT" and produces
catalogue "outtab.FIT" containing binned Stokes parameters and
corresponding polarization parameters. Each bin measures 4 pixels
along both the X and Y axes, and has a value based on the median of
the corresponding input Stokes values.



Notes
~~~~~


+ The reference direction for the Stokes vectors and polarization
vectors in the output catalogue will be north if the input catalogue
has a celestial co-ordinate Frame within its WCS information.
Otherwise, the reference direction will be the second pixel axis. The
POLANAL Frame in the WCS information of the output catalogue is
updated to describe the new reference direction.
+ The bottom left corner of each bin is chosen so that the origin of
  the (X,Y) Frame (or (X,Y,Z) Frame if the data is 3D) would correspond
  to a bin corner.




Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
Reserved.


