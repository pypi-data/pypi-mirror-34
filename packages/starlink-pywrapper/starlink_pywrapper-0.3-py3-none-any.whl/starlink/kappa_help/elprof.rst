

ELPROF
======


Purpose
~~~~~~~
Creates a radial or azimuthal profile of a 2-dimensional image


Description
~~~~~~~~~~~
This application will bin the input image into elliptical annuli, or
into a `fan' of adjacent sectors, centred on a specified position. The
typical data values in each bin are found (see parameter ESTIMATOR),
and stored in a 1-dimensional NDF which can be examined using LINPLOT,
INSPECT, etc. A 2-dimensional mask image can optionally be produced
indicating which bin each input pixel was placed in.
The area of the input image which is to be binned is the annulus
enclosed between the two concentric ellipses defined by parameter
RATIO, ANGMAJ, RMIN and RMAX. The binned area can be restricted to an
azimuthal section of this annulus using parameter ANGLIM. Input data
outside the area selected by these parameters is ignored. The selected
area can be binned in two ways, specified by parameter RADIAL:


+ If radial binning is selected (the default), then each bin is an
elliptical annulus concentric with the ellipses bounding the binned
area. The number of bins is specified by parameter NBIN and the radial
thickness of each bin is specified by WIDTH.
+ If azimuthal binning is selected, then each bin is a sector (i.e. a
  wedge-shape), with its vertex given by parameters XC and YC, and its
  opening angle given by parameters WIDTH. The number of bins is
  specified by NBIN.




Usage
~~~~~


::

    
       elprof in out nbin xc yc
       



ADAM parameters
~~~~~~~~~~~~~~~



ANGLIM( 2 ) = _REAL (Read)
``````````````````````````
Defines the wedge-shaped sector within which binning is to be
performed. The first value should be the azimuthal angle of the
clockwise boundary of the sector, and the second should be the
azimuthal angle of the anti-clockwise boundary. The angles are
measured in degrees from the x-axis, and rotation from the x-axis to
the y-axis is positive. If only a single value is supplied, or if both
values are equal, the sector starts at the given angle and extends for
360 degrees. [0.0]



ANGMAJ = _REAL (Read)
`````````````````````
The angle between the x-axis and the major axis of the ellipse, in
degrees. Rotation from the x-axis to the y-axis is positive. [0.0]



ESTIMATOR = LITERAL (Read)
``````````````````````````
The method to use for estimating the output pixel values. It can be
either "Mean" or "Weighted Mean". If the weighted mean option is
selected but no variances are available in the input data, the
unweighted mean will be used instead. ["Mean"]



IN = NDF (Read)
```````````````
The input NDF containing the 2-dimensional image from which a profile
is to be generated.



MASK = NDF (Write)
``````````````````
An output NDF of the same shape and size as the input NDF indicating
the bin into which each input pixel was placed. For radial profiles,
the bins are identified by a mask value equal to the radius (in
pixels) measured on the major axis, at the centre of the annular bin.
For azimuthal profiles, the bins are identified by a mask value equal
to the angle from the x-axis to the centre of the sector-shaped bin
(in degrees). If a null value is supplied, then no mask NDF is
produced. [!]



MTITLE = LITERAL (Read)
```````````````````````
A title for the mask NDF. If a null value is given, the title is
propagated from the input NDF. This is only prompted for if MASK is
given a non-null value. ["Mask created by KAPPA - Elprof"]



NBIN = _INTEGER (Read)
``````````````````````
The number of radial or azimuthal bins required.



OUT = NDF (Write)
`````````````````
The output 1-dimensional NDF containing the required profile. For
radial profiles, it has associated axis information describing the
radius, in pixels, at the centre of each annular bin (the radius is
measured on the major axis). For azimuthal profiles, the axis
information describes the azimuthal angle, in degrees, at the centre
of each sector-shaped bin. It will contain associated variance
information if the input NDF has associated variance information.



RADIAL = _LOGICAL (Read)
````````````````````````
Specifies the sort of profile required. If RADIAL is TRUE, then a
radial profile is produced in which each bin is an elliptical annulus.
Otherwise, an azimuthal profile is produced in which each bin is a
wedge-shaped sector. [TRUE]



RATIO = _REAL (Read)
````````````````````
The ratio of the length of the minor axis of the ellipse to the length
of the major axis. It must be in the range 0.0 to 1.0. [1.0]



RMAX = _REAL (Read)
```````````````````
The radius in pixels, measured on the major axis, at the outer edge of
the elliptical annulus to be binned. If a null value (!) is supplied
the value used is the distance from the ellipse centre (specified by
XC and YC) to the furthest corner of the image. This will cause the
entire image to fall within the outer edge of the binning area. [!]



RMIN = _REAL (Read)
```````````````````
The radius in pixels, measured on the major axis, at the inner edge of
the elliptical region to be binned. [0.0]



TITLE = LITERAL (Read)
``````````````````````
A title for the output profile NDF. If a null value is supplied the
title is propagated from the input NDF. ["KAPPA - Elprof"]



WIDTH = _REAL (Read)
````````````````````
The width of each bin. If a radial profile is being created (see
parameter RADIAL) this is the width of each annulus in pixels
(measured on the major axis). If an azimuthal profile is being
created, it is the opening angle of each sector, in degrees. If a null
(!) value is supplied, the value used is chosen so that there are no
gaps between adjacent bins. Smaller values will result in gaps
appearing between adjacent bins. The supplied value must be small
enough to ensure that adjacent bins do not overlap. The supplied value
must be at least 1.0. [!]



XC = _REAL (Read)
`````````````````
The x pixel co-ordinate of the centre of the ellipse, and the vertex
of the sectors.



YC = _REAL (Read)
`````````````````
The y pixel co-ordinate of the centre of the ellipse, and the vertex
of the sectors.



Examples
~~~~~~~~
elprof galaxy galprof 20 113 210 angmaj=49 rmin=10 rmax=210 ratio=0.5
This example will create a 1-dimensional NDF called galprof containing
a radial profile of the 2-dimensional NDF called galaxy. The profile
will contain 20 bins and it will be centred on the pixel co-ordinates
(113,210). Each bin will be an annulus of an ellipse with axis ratio
of 0.5 and inclination of 49 degrees to the x-axis. The image will be
binned between radii of 10 pixels, and 210 pixels (measured on the
major axis), and there will be no gaps between adjacent bins (i.e.
each bin will have a width on the major axis of about 10 pixels).
elprof galaxy galprof 10 113 210 radial=f anglim=20 rmin=50

rmax=60
This example also creates a 1-dimensional NDF called galprof, this
time containing an azimuthal profile of the 2-dimensional NDF called
"galaxy", containing 10 bins. Each bin will be a wedge-shaped sector
with vertex at pixel co-ordinates (113,210). The clockwise edge of the
first bin will be at an angle of 20 degrees to the x-axis, and each
bin will have a width (opening angle) of 36 degrees (so that 360
degrees are covered in total). Only the section of each sector bounded
by radii of 50 and 60 pixels is included in the profile. In this case
the default value of 1.0 is accepted for parameter RATIO and so the
bins will form a circular annulus of width 10 pixels.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: INSPECT; ESP: ELLFOU, ELLPRO, SECTOR.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1999, 2001, 2004 Central Laboratory of the
Research Councils. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA, VARIANCE, TITLE, UNITS,
WCS (if RADIAL is true) and HISTORY components of the input NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point.




