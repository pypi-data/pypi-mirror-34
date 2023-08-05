

POLZCONV
========


Purpose
~~~~~~~
Convert a Z axis value to a Z column value


Description
~~~~~~~~~~~
This application converts a supplied Z axis value into the
corresponding Z column value within a given catalogue, returning the
nearest value for which some data exists within the catalogue. The
resulting Z column value and Z axis value are written to output
parameters. This application is primarily for use within scripts.


Usage
~~~~~


::

    
       polzconv cat
       



ADAM parameters
~~~~~~~~~~~~~~~



CAT = LITERAL (Read)
````````````````````
The name of the input catalogue. This may be in any format supported
by the CAT library (see SUN/181). A file type of .FIT is assumed if no
file type is supplied.



COLX = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the position of each
vector along the first axis. A list of available column names is
displayed if a non-existent column name is given. See the "Notes"
section below for further details of how these positions are
interpreted. [X]



COLY = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the position of each
vector along the second axis. A list of available column names is
displayed if a non-existent column name is given. See the "Notes"
section below for further details of how these positions are
interpreted. [Y]



COLZ = LITERAL (Read)
`````````````````````
The name of the catalogue column which gives the position of each
vector along a third axis. A list of available column names is
displayed if a non-existent column name is given. A null (!) value
should be supplied if no third axis is to be used. The dynamic default
is 'Z' if the catalogue contains a Z column, and null (!) otherwise.
See also parameter ZAXVAL. []



ZAXVAL = LITERAL (Read)
```````````````````````
Specifies the Z axis value to be converted. The given value should be
in the current coordinate Frame of the supplied catalogue (see
parameter COLZ). For instance, if the current coordinate Frame
contains a calibrated wavelength axis, the value should be given in
the units specified in that frame (anstroms, nanometres, etc.). If the
wavelength axis has not been calibrated, the value will probably need
to be supplied in units of pixels. Entering a colon (":") for the
parameter will result in a description of the current coordinate Frame
being shown. This may help to determine the units in which a value is
expected. The value actually used is the closest available value
within the catalogue. This value is displayed on the screen and
written to parameter ZVALUE. The ZAXVAL parameter is only accessed if
a null (!) value is supplied for parameter ZCOLVAL. See also parameter
COLZ.



ZCOLVAL = _REAL (Read)
``````````````````````
Specifies the Z column value for the vectors to be displayed. The
given value should be in the same coordinate system as the values
stored in the Z column of the catalogue (usually pixels). This
parameter provides an alternative to the ZAXVAL parameter. Use the
ZCOLVAL parameter to specify the Z value in pixels, and the ZAXVAL
parameter to specify the Z value in Hertz, angstroms, nanometres, etc
(if the Z axis has been calibrated). If a null value is supplied for
ZCOLVAL, then ZAXVAL is used to determine the Z value to display. [!]



ZCOLUSED = LITERAL (Write)
``````````````````````````
The formatted Z column value to use. This is the nearest value to the
supplied ZCOLVAL or ZAXVAL for which data exists in the catalogue. The
string "***" is stored if the catalogue does not include a Z axis.



ZAXUSED = LITERAL (Write)
`````````````````````````
The formatted Z axis value to use. This is the nearest value to the
supplied ZAXVAL for which data exists in the catalogue. The string
"***" is stored if the catalogue does not include a Z axis, or if a
vcalue for supplied for ZCOLVAL.



Notes
~~~~~


+ The columns specified by parameters COLX and COLY should hold
  coordinates in the "Base Frame" of the WCS information stored as an
  AST FrameSet (see SUN/210) in the supplied catalogue. If the catalogue
  has been produced by one of the POLPACK application polvec or polbin,
  then the Base Frame will be pixel co-ordinates within the aligned
  intensity images, and these will be stored in columns with names "X"
  and "Y".




Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils


