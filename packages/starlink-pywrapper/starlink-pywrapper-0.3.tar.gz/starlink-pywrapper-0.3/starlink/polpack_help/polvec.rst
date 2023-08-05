

POLVEC
======


Purpose
~~~~~~~
Calculates polarization vectors from supplied Stokes parameters


Description
~~~~~~~~~~~
This application calculates values of percentage polarization,
polarization angle, total intensity and polarized intensity, based on
Stokes parameters in the supplied input NDF (which will normally have
been created by POLKA or POLCAL). These calculated values may be
stored either in a series of output NDFs, or in a single catalogue.
The reference direction of the output catalogue and NDFs is determined
by parameter REFUPDATE.


Usage
~~~~~


::

    
       polvec in cat [p] [ang] [i] [ip] [q] [u] [v]
       



ADAM parameters
~~~~~~~~~~~~~~~



ANG = NDF (Write)
`````````````````
An output NDF holding the polarization angle (anti-clockwise from the
reference direction to the plane of polarization - in degrees). In the
the case of circular polarization, a value of zero is stored if the
normalised Stokes parameter V is positive, and a value of 90 is stored
otherwise. A null value can be supplied if this output image is not
required. [!]



BOX( 2 ) = _INTEGER (Read)
``````````````````````````
The x and y sizes (in pixels) of the bins to be used when binning the
supplied Stokes parameters prior to estimating the polarization
vectors. If only a single value is given, then it will be duplicated
so that a square bin is used. A value of 1 produces no binning, and
causes the origin of the output NDFs and catalogue to be the same as
the x-y origin in the input cube (the output origin is set to
[0.0,0.0] if any binning is performed).
This parameter is not accessed and no binning is performed if the
input NDF is 4D. Note, if the output vectors are being stored in a
catalogue, you should usually use the POLBIN application to bin the
Stokes vectors (this applies to both 3D and 4D data). [1]



CAT = LITERAL (Read)
````````````````````
The name of a catalogue to create, holding the calculated polarization
parameters tabulated at each point for which Stokes parameters are
available. If a null (!) value is supplied, then no catalogue is
created. The catalogue will contain the following columns (all stored
as single precision _REAL values):

+ X -- The pixel X coordinate at the tabulated point.
+ Y -- The pixel Y coordinate at the tabulated point.
+ Z -- The pixel Z coordinate at the tabulated point (this is only
included if the input NDF is 4D).
+ I -- The total intensity.
+ Q -- The Stokes Q parameter.
+ U -- The Stokes U parameter.
+ P -- The percentage polarization.
+ ANG -- The polarization angle (anti-clockwise from the reference
direction to the plane of polarization - in degrees).
+ PI -- The polarized intensity.

If VARIANCE is TRUE, then the catalogue will also contain additional
columns giving the standard deviation on each of the tabulated values
(excluding the X, Y and Z columns). The names of these columns will be
formed by prepending the letter D to the start of the column names
listed above.
IF RADEC is TRUE, the columns will also contain RA and DEC columns, so
long as the input cube contains appropriate WCS information.
When measuring circular polarization, the columns describing Q and U
will be replaced by equivalent columns describing V; and the ANG value
will be zero if the normalised Stokes parameter V is positive, and 90
otherwise.
The coordinates contained in columns X and Y refer to pixel
coordinates after any binning. For this reason it is usually better to
avoid binning the Stokes vectors in this application (see parameter
BOX). Information describing the mappings between pixel coordinates
and any other known coordinate Frames will be stored in the catalogue
in textual form, as an AST FrameSet (see SUN/210).
The storage format of the catalogue is determined by the "file type"
specified with the file name. If no file type is supplied, the
catalogue will be stored in the form of a FITS binary table with file
extension ".FIT". Other possibilities are described in SUN/190.



DEBIAS = _LOGICAL (Read)
````````````````````````
TRUE if a correction for statistical bias is to be made to percentage
polarization and polarized intensity. The returned variance values are
unchanged. This correction only applies to calculations of linear
polarization, and cannot be used if the input cube does not contain
variance values. If a null value (!) is supplied, then the correction
is applied if output variances are being created, and not otherwise.
[!]



I = NDF (Write)
```````````````
An output NDF holding the total intensity. A null value can be
supplied if this output image is not required. [!]



IN = NDF (Read)
```````````````
The 3D (or 4D) cube holding the Stokes parameters. This should have
been created by POLKA or POLCAL.



IP = NDF (Write)
````````````````
An output NDF holding the polarized intensity. A null value can be
supplied if this output image is not required. [!]



METHOD = LITERAL (Read)
```````````````````````
The method to be used when binning Stokes parameters. This may be set
to any unique abbreviation of the following:

+ MEAN -- Mean of the input data values
+ MEDIAN -- Median of the input data values
+ SIGMA -- A sigma clipped mean Note, only the MEAN method may be used
  with bins containing more than 100 values. [MEDIAN]





P = NDF (Write)
```````````````
An output NDF holding percentage polarization. A null value can be
supplied if this output image is not required. [!]



Q = NDF (Write)
```````````````
An output NDF holding the Q Stokes parameter. A null value can be
supplied if this output image is not required. [!]



RADEC = _LOGICAL (Read)
```````````````````````
If TRUE, columns holding the RA and DEC (FK5, J2000) are added to the
output catalogue, if the input cube contains the necessary WCS
information. If FALSE, no RA and DEC columns are written. For large
catalogues, creating RA and DEC columns can cause a significant delay.
[current value]



REFUPDATE = _LOGICAL (Read)
```````````````````````````
Determines the reference direction in the output catalogue and NDFs.
If REFUPDATE is TRUE, the output reference direction will be north if
the input NDF has a celestial co-ordinate Frame within its WCS
component (teh direction of north is determined at the centre of the
image). Otherwise, the reference direction will be the second pixel
axis. The POLANAL Frame in the WCS information of the output catalogue
or NDFs is updated to describe the new reference direction. If
REFUPDATE is FALSE, the output reference direction will be the same as
the input reference direction. [TRUE]



SIGMAS = _REAL (Read)
`````````````````````
Number of standard deviations to reject data at. Only used if METHOD
is set to "SIGMA". [4.0]



U = NDF (Write)
```````````````
An output NDF holding the U Stokes parameter. A null value can be
supplied if this output image is not required. [!]



V = NDF (Write)
```````````````
An output NDF holding the V Stokes parameter. A null value can be
supplied if this output image is not required. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
TRUE if output variances are to be calculated. This parameter is only
accessed if the supplied Stokes cube contains variances, otherwise no
variances are generated. [TRUE]



WLIM = _REAL (Read)
```````````````````
If the input cube contains bad pixels, then this parameter may be used
to determine the number of good Stokes parameters which must be
present within each bin before a valid output vector is generated. It
can be used, for example, to prevent output vectors from being
generated in regions where there are relatively few good Stokes
parameters to contribute to the bin.
The value given for WLIM specifies the minimum fraction of good pixels
which must be present in each bin in order to generate a good output
vector. If this specified minimum fraction of good input pixels is not
present, then a bad output vector will result. The value of this
parameter should lie between 0.0 and 1.0 (the actual number used will
be rounded up if necessary to correspond to at least 1 pixel). [0.0]



Notes
~~~~~


+ The output NDFs are deleted if there is an error during the
  formation of the polarization parameters.




Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils


