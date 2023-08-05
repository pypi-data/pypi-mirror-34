

CREFRAME
========


Purpose
~~~~~~~
Generates a test two-dimensional NDF with a selection of several forms


Description
~~~~~~~~~~~
This application creates a two-dimensional output NDF containing
artificial data of various forms (see Parameter MODE). The output NDF
can, optionally, have a VARIANCE component describing the noise in the
data array (see Parameter VARIANCE), and additionally a randomly
generated pattern of bad pixels (see Parameter BADPIX). Bad columns or
rows of pixels can also be generated.


Usage
~~~~~


::

    
       creframe out mode [lbound] [ubound]
           { mean=?
           { background=? distrib=? max=? min=? ngauss=? seeing=?
           { mean=? sigma=?
           { high=? low=?
           mode
       



ADAM parameters
~~~~~~~~~~~~~~~



BACKGROUND = _REAL (Read)
`````````````````````````
Background intensity to be used in the generated data array. Must not
be negative. (GS mode).



BADCOL = _INTEGER (Read)
````````````````````````
The number of bad columns to include. Only accessed if parameter
BADPIX is TRUE. The bad columns are distributed at random using a
uniform distribution. [0]



BADPIX = _LOGICAL (Read)
````````````````````````
Whether or not bad pixels are to be included. See also parameters
FRACTION, BADCOL and BADROW. [FALSE]



BADROW = _INTEGER (Read)
````````````````````````
The number of bad rows to include. Only accessed if parameter BADPIX
is TRUE. The bad rows are distributed at random using a uniform
distribution. [0]



DIRN = _INTEGER (Read)
``````````````````````
Direction of the ramp. 1 means left to right, 2 is right to left, 3 is
bottom to top, and 4 is top to bottom. (RA mode)



DISTRIB = _CHAR (Read)
``````````````````````
Radial distribution of the Gaussians to be used (GS mode).
Alternatives weightings are:


+ "FIX" -- fixed distance, and
+ "RSQ" -- one over radius squared.

["FIX"]



FRACTION = _REAL (Read)
```````````````````````
Fraction of bad pixels to be included. Only accessed if BADPIX is
TRUE. [0.01]



HIGH = _REAL (Read)
```````````````````
High value used in the generated data array (RA and RL modes).



LBOUND( 2 ) = _INTEGER (Read)
`````````````````````````````
Lower pixel bounds of the output NDF. Only accessed if Parameter LIKE
is set to null (!).



LIKE = NDF (Read)
`````````````````
An optional template NDF which, if specified, will be used to define
the bounds for the output NDF. If a null value (!) is given the bounds
are obtained via parameters LBOUND and UBOUND. [!]



LOGFILE = LITERAL (Read)
````````````````````````
Name of a log file in which to store details of the Gaussians added to
the output NDF (GS mode). If a null value is supplied no log file is
created. [!]



LOW = _REAL (Read)
``````````````````
Low value used in the generated data array (RA and RL modes).



MAX = _REAL (Read)
``````````````````
Peak Gaussian intensity to be used in the generated data array (GS
mode).



MEAN = _REAL (Read)
```````````````````
Mean value used in the generated data array (FL, RP and GN modes).



MIN = _REAL (Read)
``````````````````
Lowest Gaussian intensity to be used in the generated data array (GS
mode).



MODE = LITERAL (Read)
`````````````````````
The form of the data to be generated. The options are as follows.


+ "RR" -- Uniform noise between 0 and 1.
+ "RL" -- Uniform noise between specified limits.
+ "BL" -- A constant value of zero.
+ "FL" -- A specified constant value.
+ "RP" -- Poisson noise about a specified mean
+ "GN" -- Gaussian noise about a specified mean
+ "RA" -- Ramped between specified minimum and maximum values and a
choice of four directions.
+ "GS" -- A random distribution of 2-d Gaussians of defined FWHM and
  range of maximum peak values on a specified background, with
  Poissonian noise. There is a choice of spatial distributions for the
  Gaussians: fixed, or inverse square radially from the array centre.
  (In essence it is equivalent to a simulated star field.) The x-y
  position and peak value of each Gaussian may be stored in a log file,
  a positions list catalogue, or reported on the screen. Bad pixels may
  be included randomly, and/or in a column or line of the array.





NGAUSS = _INTEGER (Read)
````````````````````````
Number of Gaussian star-like images to be generated (GS mode).



OUT = NDF (Write)
`````````````````
The output NDF.



OUTCAT = FILENAME (Write)
`````````````````````````
An output catalogue in which to store the pixel co-ordinates of the
Gausians in the output NDF (GS mode). If a null value is supplied, no
output positions list is produced. [!]



SEEING = _REAL (Read)
`````````````````````
Seeing (FWHM) in pixels (not the same as the standard deviation) (GS
mode).



SIGMA = _REAL (Read)
````````````````````
Standard deviation of noise to be used in the generated data array (GN
mode).



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. ["KAPPA - Creframe"]



UBOUND( 2 ) = _INTEGER (Read)
`````````````````````````````
Upper pixel bounds of the output NDF. Only accessed if Parameter LIKE
is set to null (!).



VARIANCE = _LOGICAL (Read)
``````````````````````````
If TRUE, a VARIANCE component is added to the output NDF representing
the noise added to the field. If a null (!) value is supplied, a
default is used which is TRUE for modes which include noise, and FALSE
for modes which do not include any noise. [!]



Examples
~~~~~~~~
creframe out=file ubound=[128,128] mode=gs ngauss=5 badpix
badcol=2 max=200 min=20 background=20 seeing=1.5 Produces a 128x128
pixel data array with 5 gaussians with peak values of 200 counts and a
background of 20 counts. There will be two bad columns added to the
resulting data.



Notes
~~~~~


+ The Gaussian parameters (GS mode) are not displayed when the message
  filter environment variable MSG_FILTER is set to QUIET.




Copyright
~~~~~~~~~
Copyright (C) 2001, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2009 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ The DATA and VARIANCE components of the output NDF have a numerical
type of "_REAL" (single-precision floating point).
+ This routine does not assign values to any of the following
  components in the output NDF: LABEL, UNITS, QUALITY, AXIS, WCS.




