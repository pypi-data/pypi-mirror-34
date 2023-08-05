

DSUTILS
=======


Purpose
~~~~~~~
A collection of utilities for estimating focal plane distortion


Description
~~~~~~~~~~~
This routine provides various functions needed by the scripts that
determine a 2D polynomial describing the focal plane disortion
produced by SCUBA-2 optics.


ADAM parameters
~~~~~~~~~~~~~~~



BMAP = FILENAME (Read)
``````````````````````
Only accessed if a time series cube is specified via parameter "IN".
It gives the name of a text file in which to place an AST dump of a
Mapping from a modified PIXEL Frame to the SKY offset frame for a time
slice close to the middle of the data set The PIXEL frame is modified
in the sense that its origin (i.e. pixel coords (0,0,0.0) ) is shifted
so that it co-incides with the sky reference point. No file is created
if a null (!) value is supplied. [!]



BORDER = _INTEGER (Read)
````````````````````````
Only accessed if a time series cube is specified via parameter "IN",
and a null(!) value sispecified for parameter BMAP. It gives the
border width in pixels. Time slices with peak positions closer to any
edge than this amount will not be included in the output catalogue.
[4]



COLNAME = LITERAL (Read)
````````````````````````
Only accessed if a value is supplied for "INCAT". If supplied, COLNAME
should be the name of a column in the INCAT catalogue. An output NDF
holding these values will be created (see parameter COLNDF). [!]



COLNDF = NDF (Write)
````````````````````
Only accessed if a value is supplied for "COLNAME". If supplied, an
NDF is created holding the values from the catalogue column specified
by COLNAME. The column value from each row in the INCAT catalgue is
pasted into the output NDF at a position specified by the BD1/BF2
columns.



FORWARD = _LOGICAL (Read)
`````````````````````````
Only accessed if input NDFs are specified for parameter INFITX and
INFITY, and if a non-null (!) value is supplied for parameter OUTCODE.
It indices whether the code written to the OUTCODE file should
describe the forward or inverse PolyMap transformation.



FPIXSIZE = _DOUBLE (Read)
`````````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the pixel size (in mm), of the NDFs created via parameters
OUTANG and OUTMAG. [1.0]



FXHI = _DOUBLE (Read)
`````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the upper bound (in mm) on the focal plane X axis, of the
NDFs created via parameters OUTANG and OUTMAG. [50]



FXLO = _DOUBLE (Read)
`````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the lower bound (in mm) on the focal plane X axis, of the
NDFs created via parameters OUTANG and OUTMAG. [-50]



FXOFF = _DOUBLE (Read)
``````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the focal plane X coord for a point that defines a global
offset to be removed from OUTMAG and OUTANG. The point specified by
FXOFF and FYOFF will have value zero in OUTANG. No offset is removed
if a null (!) value is supplied. [!]



FYHI = _DOUBLE (Read)
`````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the upper bound (in mm) on the focal plane Y axis, of the
NDFs created via parameters OUTANG and OUTMAG. [50]



FYLO = _DOUBLE (Read)
`````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the lower bound (in mm) on the focal plane Y axis, of the
NDFs created via parameters OUTANG and OUTMAG. [-50]



FYOFF = _DOUBLE (Read)
``````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
It gives the focal plane Y coord for a point that defines a global
offset to be removed from OUTMAG and OUTANG. The point specified by
FXOFF and FYOFF will have value zero in OUTANG. No offset is removed
if a null (!) value is supplied. [!]



IN = NDF (Read)
```````````````
Only accessed if null (!) values are supplied for parameter INFITX,
INFITY, and INCAT. It should be a time series cube. If a non-null
value is supplied, then the BMAP parameter can be used to get the WCS
Mapping for a typical time slice, or the OUTCAT parameter can be used
to create a catalogue holding the expected source position (in GRID
coords) in every time slice. A single time slice from this cube can
also be written to an output NDF (see parameter OUTSLICE). A list of
time slices in which the reference point is close to a specified
bolometer can also be produced (see parameter XBOL).



INFITX = NDF (Read)
```````````````````
A 2D NDF holding fitted focal plane X offsets (in mm) at every
bolometer, or null (!). This NDF shoudl have been created by
KAPPA:FITSURFACE, and should hold the coefficients of the fit in the
SURFACEFIT extension. If NDFs are supplied for both INFITX and INFITY,
then the OUTCODE parameter can be used to create C source code
describing the coefficients in a form usable by the AST PolyMap
constructor. In addition, the OUTDX and OUTDY parameters can be used
to create output NDFs containing the values for the inverse
quantities.



INFITY = NDF (Read)
```````````````````
A 2D NDF holding fitted focal plane Y offsets (in mm) at every
bolometer, or null (!). See INFITX.



INCAT = FILENAME (Read)
```````````````````````
Only access if a null (!) value is supplied for INFITX or INFITY. It
is a text file holding a catalogue of corrected and uncorrected pixel
positions for every bolometer in the subarray specified by SUBARRAY.
These are used to create output NDFs holding the X and Y focal plane
offset (in mm) at every bolometer in the subarray (see OUTDX and
OUTDY). An output catalogue can also be produced holding extra
columns, and from which abberant rows have been rejected (see
parameter OUTCAT).



ITIME = _INTEGER (Read)
```````````````````````
The integer index of a time slice to be dumped to an NDF (see
OUTSLICE). If supplied, the application terminates without further
action once the NDF has been created. [!]



LOWFACTOR = _REAL (Read)
````````````````````````
Only accessed if a value is supplied for parameter IN. It gives the
lowest time slice data sum (as a fraction of the largest time slice
data sum in the supplied timne series cube) for usable time slices.
Any time slices that have total data sums less than this value are
skipped.



NITER = _INTEGER (Read)
```````````````````````
Only accessed if a value is supplied for parameter INCAT. It gives the
number of sigma-clipping iterations to be performed whilst creating
the output NDFs. [3]



OUTCAT = FILENAME (Write)
`````````````````````````
If a value was supplied for INCAT, then OUTCAT is the name of an
output catalogue to create, containing a copy of the input catalogue
form which abberant rows have been removed, and contaiing some extra
informative columns (e.g. offsets in focal plane and pixel
coordinates). No catalogue is created if a null (!) value is supplied.
If a value is supplied for IN, then OUTCAT will hold the expected
source position in each time slice.



OUTCODE = FILENAME (Write)
``````````````````````````
If a value was supplied for INFITX and INFITY, then OUTCODE is the
name of an output text file in which to store the C code describing
the coefficients of the forward or inverse distortion polynomial.



OUTDX = NDF (Write)
```````````````````
If a value was supplied for INFITX and INFITY, then OUTDX gives the
name of the NDF in which to store the inverse X axis corrections at
each bolometer in the subarray (in mm). If a value was supplied for
INCAT, then OUTDX is the name of an NDF to recieve the forward X axis
correctiosn at every bolometer in the subarray (in mm).



OUTDY = NDF (Write)
```````````````````
If a value was supplied for INFITX and INFITY, then OUTDX gives the
name of the NDF in which to store the inverse Y axis corrections at
each bolometer in the subarray (in mm). If a value was supplied for
INCAT, then OUTDX is the name of an NDF to recieve the forward Y axis
correction at every bolometer in the subarray (in mm).



OUTANG = NDF (Write)
````````````````````
Only acccessed if a non-null value is supplied for parameter OUTMAG.
OUTANG specifies the output NDF to receive the orientation of the
distortion (in degrees anti-clockwise from the positive Y axis) at
each point in the focal plane.



OUTFX = NDF (Write)
```````````````````
The name of an NDF to recieve the focal plane X value (in arc-sec) at
each bolometer in the subarray specified by SUBARRAY. Only produced if
a non-null value is also supplied for OUTFY. [!]



OUTFY = NDF (Write)
```````````````````
The name of an NDF to recieve the focal plane Y value (in arc-sec) at
each bolometer in the subarray specified by SUBARRAY. Only produced if
a non-null value is also supplied for OUTFX. [!]



OUTMAG = NDF (Write)
````````````````````
An output NDF to receive the magnitude of the distortion (in mm) at
each point in the focal plane. If a null (!) value is supplied, no NDF
will be created. The NDFs specified by OUTMAG and OUTANG can be
displayed as a vector plot using KAPPA:VECPLOT. In addition, the
outline of any sub-array can be over-plotted by changing the current
coordinate Frame and then using KAPPA:ARDPLOT (for instance "wcsframe
outmag s8a" followed by "ardplot s8a"). Note, for some distortions
(e.g. NEW4) the distortion at 450 and 850 are different. The waveband
to use is determined by the value supplied for the SUBARRAY parameter.
[!]



OUTSLICE = NDF (Write)
``````````````````````
If a value was supplied for IN and ITIME, then OUTSLICE gives the name
of the NDF in which to store the bolometer data for the given time
slice, including celestial WCS.



SUBARRAY = LITERAL (Write)
``````````````````````````
The name of the subarray being processed: one of "s8a", "s8b", "s8b",
"s8d", "s4a", "s4b", "s4b", "s4d". If OUTMAG is not null, then the
value supplied for SUBARRAY determines the waveband for which the
distortion is returned.



XBOL = _INTEGER (Read)
``````````````````````
The index of a test bolometer on the first GRID axis within the sub-
array containing the bolometer. If values are supplied for all of IN,
XBOL, YBOL and RADIUS, then a list of time slice indices are
displayed. These are the indices of the time slice in which the
reference point is close to the bolometer specified by (XBOL,YBOL).
The RADIUS parameter spcified the distance limit. [!]



YBOL = _INTEGER (Read)
``````````````````````
The index of a test bolometer on the second GRID axis within the sub-
array containing the bolometer. See XBOL. [!]



RADIUS = _REAL (Given)
``````````````````````
The radius of a test circle, in bolometers. See XBOL. [!]



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: DISTORTION, SHOWDISTORTION


Copyright
~~~~~~~~~
Copyright (C) 2009-2011 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


