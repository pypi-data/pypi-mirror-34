

ROTATE
======


Purpose
~~~~~~~
Rotates a two-dimensional NDF about its centre through any angle


Description
~~~~~~~~~~~
This routine rotates an array stored in an NDF data structure by an
arbitrary angle. The rotation angle can be chosen automatically to
make north vertical in the output NDF (see parameter ANGLE). The
origin of the rotation is around the point (0,0) in pixel co-
ordinates. The output array dimensions just accommodate the rotated
array. Output pixels can be generated from the input array by one of
two methods: nearest-neighbour substitution or by bi-linear
interpolation. The latter is slower, but gives better results. Output
pixels not corresponding to input pixels take the bad value.
The NDF may have two or three dimensions. If it has three dimensions,
then the rotation is applied in turn to each plane in the cube and the
result written to the corresponding plane in the output cube. The
orientation of the rotation plane can be specified using the AXES
parameter.


Usage
~~~~~


::

    
       rotate in out angle
       



ADAM parameters
~~~~~~~~~~~~~~~



ANGLE = _REAL (Read)
````````````````````
Number of clockwise degrees by which the data array is to be rotated.
It must lie between -360 and 360 degrees. The suggested default is the
current value. If a null (!) value is supplied, then the rotation
angle is chosen to make north vertical at the centre of the image. If
the current co-ordinate Frame in the input NDF is not a celestial co-
ordinate frame, then the rotation angle is chosen to make the second
axis of the current Frame vertical.



ANGLEUSED = _REAL (Write)
`````````````````````````
An output parameter holding the rotation angle actually used, in
degrees. This is useful if a null value is supplied for parameter
ANGLE.



AXES(2) = _INTEGER (Read)
`````````````````````````
This parameter is only accessed if the NDF has exactly three
significant pixel axes. It should be set to the indices of the NDF
pixel axes which span the plane in which rotation is to be applied.
All pixel planes parallel to the specified plane will be rotated
independently of each other. The dynamic default comprises the indices
of the first two significant axes in the NDF. Note that excluding the
first significant axis may be very inefficient for large cubes; a
prior reconfiguration with application PERMAXES that is compatible
with the dynamic default for AXES, will often prove beneficial. []



IN = NDF (Read)
```````````````
NDF structure containing the two- or three-dimensional array to be
rotated.



NNMETH = _LOGICAL (Read)
````````````````````````
If TRUE, the nearest-neighbour method will be used to evaluate the
output data-array pixels. This is only accessed when the rotation is
not a multiple of 90 degrees. [FALSE]



OUT = NDF (Write)
`````````````````
Output NDF to contain the rotated arrays.



QUALITY = _LOGICAL (Read)
`````````````````````````
This parameter is only accessed when NNMETH is FALSE and ANGLE is not
a multiple of 90 degrees. Strictly, the quality values are undefined
by the bi-linear interpolation and hence cannot be propagated.
However, QUALITY = TRUE offers an approximation to the quality array
by propagating the nearest-neighbour quality to the output NDF.
[FALSE]



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null value will cause the title of the
NDF supplied for parameter IN to be used instead. [!]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of two strings should be supplied
specifying the two axes which are to be used when determining the
rotation angle needed to make north vertical. Each axis can be
specified using one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the two used pixel axes within the NDF are used. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
A TRUE value causes variance values to be used as weights for the
pixel values in bi-linear interpolation, and also causes output
variances to be created. This parameter is ignored if ANGLE is a
multiple of 90 degrees or NNMETH=TRUE; in these cases the variance
array is merely propagated. If a null (!) value is supplied, the value
used is TRUE if the input NDF has a VARIANCE component, and FALSE
otherwise. Note that following this operation the errors are no longer
independent. [!]



Examples
~~~~~~~~
rotate ns ew 90
This rotates the array components in the NDF called ns by 90 degrees
clockwise around pixel co-ordinates [0,0] and stores the result in the
NDF called ew. The former x axis becomes the new y axis, and the
former y axis becomes the new x axis. The former y-axis arrays are
also reversed in the process.
rotate m31 m31r angle=!
This rotates the NDF called m31 so that north is vertical and stores
the results in an NDF called m31r. This assumes that the current WCS
Frame in the input NDF is a celestial co-ordinate Frame.
rotate angle=180 out=sn in=ns
This rotates the array components in the NDF called ns by 180 degrees
clockwise around the pixel co-ordinates [0,0], and stores the result
in the NDF called sn. The axis arrays are flipped in the output NDF.
rotate f1 f1r 37.2 novariance
This rotates the array components in the NDF called f1 by 37.2 degrees
clockwise around the pixel co-ordinates [0,0], and stores the result
in the NDF called f1r. The original axis information is lost. Bi-
linear interpolation is used without variance information. No quality
or variance information is propagated.
rotate f1 f1r 106 nnmeth title="Reoriented features map"
This rotates the array components in the NDF called f1 by 106 degrees
clockwise around the pixel co-ordinates [0,0], and stores the result
in the NDF called f1r. The original axis information is lost. The
resultant array components, all of which are propagated, are
calculated by the nearest-neighbour method. The title of the output
NDF is "Reoriented features map".
rotate velmap rotvelmap 70
This rotates the array components in the three-dimensional NDF called
velmap by 70 degrees clockwise around the pixel co-ordinates [0,0],
and stores the result in the NDF called rotvelmap. The rotation is
applied to the first two pixel axes repeated for all the planes in the
cube's third pixel axis.
rotate velmap rotvelmap 70 axes=[1,3]
This as the previous example except that the rotation is applied in
the plane given by the first and third pixel axes.



Notes
~~~~~


+ Bad pixels are ignored in the bi-linear interpolation. If all four
  pixels are bad, the result is bad.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FLIP, RESAMPLE; Figaro: IREVX, IREVY, IROT90.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1998-1999, 2002, 2004 Central Laboratory of the
Research Councils. Copyright (C) 2005-2006 Particle Physics &
Astronomy Research Council. Copyright (C) 2008-2009, 2012 Science and
Technology Facilities Council. All Rights Reserved.


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
The propagation rules depend on parameters ANGLE and NNMETH.


+ For rotations that are multiples of 90-degrees, VARIANCE, QUALITY,
AXIS, HISTORY, LABEL WCS, and UNITS components of the input NDF are
propagated to the output NDF. The axis and WCS components are switched
and flipped as appropriate.
+ For the nearest-neighbour method VARIANCE, QUALITY, HISTORY, LABEL,
WCS, and UNITS components of the input NDF are propagated to the
output NDF.
+ For the linear interpolation method HISTORY, LABEL, WCS, and UNITS
components of the input NDF are propagated to the output NDF. In
addition if parameter VARIANCE is TRUE, variance information is
derived from the input variance; and if parameter QUALITY is TRUE,
QUALITY is propagated using the nearest neighbour.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric types are supported, though for linear
  interpolation the arithmetic is performed using single- or double-
  precision floating point as appropriate; and for 90 and 270-degree
  rotations _INTEGER is used for all integer types.




