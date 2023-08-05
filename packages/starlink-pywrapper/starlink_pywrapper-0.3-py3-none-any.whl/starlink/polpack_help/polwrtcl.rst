

POLWRTCL
========


Purpose
~~~~~~~
Creates a text file holding the contents of a specified catalogue in
the form of a Tcl code fragment which can be used in a Tcl
applications such as GAIA


Description
~~~~~~~~~~~
This application creates a description of a POLPACK catalogue which
can be used by the Tcl applications such as the GAIA polarimetry
toolbox. The description includes the bulk data. Rows that contain any
bad values are omitted from the output catalogue.
The desciption of the catalogue is written to an output text file and
takes the form of a Tcl code fragment which assigns values to the
following Tcl variables:
gotwcs_ : Set to 1 if RA/DEC columns are available, or 0 if not.
headings_: A Tcl list holding the column headings. uses_ : A Tcl list
holding the quantity stored in each column. These will chosen from X,
Y, Z, RA, DEC, I, Q, U, V, DI, DQ, DU, DV, P, ANG, PI, DP, DANG, DPI,
ID (or will be null if the quantity in the column is not known). xlo_
: The minimum X pixel index value in the data ylo_ : The minimum Y
pixel index value in the data zlo_ : The minimum Z column value in the
data (only set if the catalogue has a Z column). xhi_ : The maximum X
pixel index value in the data yhi_ : The maximum Y pixel index value
in the data zhi_ : The maximum Z column value in the data (only set if
the catalogue has a Z column). ncol_ : The number of columns in the
catalogue nrow_ : The number of good rows in the catalogue data_ : A
Tcl list of rows. Each row is itself a Tcl list of column values. ra_
: A central RA value in h:m:s format (may be blank) dec_ : A central
DEC value in d:m:s format (may be blank) xrefpix_ : The pixel offset
to ra_/dec_ from the bottom-left corner of the bounding box. yrefpix_
: The pixel offset to ra_/dec_ from the bottom-left corner of the
bounding box. nxpix_ : No of pixels in X in bounding box nypix_ : No
of pixels in Y in bounding box secpix_ : An estimate of the pixel size
in arcseconds equinox_ : The equinox for the RA and DEC values in the
file (e.g. "2000" - may be blank) epoch_ : The epoch of observation
for the RA and DEC values fmts_ : A list of Tcl formats
specifications, one for each column. Column values are formatted with
this format. hfmts_ : A list of Tcl formats specifications, one for
each column. Column headings are formatted with this format. zaunit_ :
The units associated with the Z axis in the current Frame of the
catalogues WCS FrameSet. Not written if the catalogue does not have a
Z axis. zcunit_ : The units associated with the Z column in the
catalogue. Not written if the catalogue does not have a Z column.
refrot_ : The angle in degrees, from the Declination axis (FK5 J2000)
through the RA axis, to the referene direction. Assumed to be constant
across the map.


Usage
~~~~~


::

    
       polwrtcl in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = LITERAL (Read)
```````````````````
The name of the input catalogue. if none is provided.



OUT = LITERAL (Read)
````````````````````
The name of the output text file.



Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils


