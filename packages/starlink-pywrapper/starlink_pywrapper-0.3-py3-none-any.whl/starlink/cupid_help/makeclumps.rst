

MAKECLUMPS
==========


Purpose
~~~~~~~
Create simulated data containing clumps and noise


Description
~~~~~~~~~~~
This application creates a new 1-, 2- or 3-dimensional NDF containing
a collection of clumps with background noise. It also creates a
catalogue containing the clump parameters.
The clumps profiles are Gaussian, with elliptical isophotes. The
values of each parameter defining the clump shape can be either fixed
at a constant value or selected from a given probability distribution.
The clump positions can be distributed randomly, or may be on a
regular grid (see parameter GRID).


Usage
~~~~~


::

    
       makeclumps out outcat
       



ADAM parameters
~~~~~~~~~~~~~~~



ANGLE( 2 ) = _REAL (Read)
`````````````````````````
Defines the distribution from which the spatial position angle of the
major axis of the elliptical clump is chosen. Values should be
supplied in units of degrees. See parameter PARDIST for additional
information. Note, angles are always taken from a uniform
distribution, irrespective of the setting of PARDIST. [current value]



BEAMFWHM = _REAL (Read)
```````````````````````
The spatial FHWM (Full Width at Half Max) of the instrumental beam, in
pixels. The generated clumps are smoothed with a Gaussian beam of this
FWHM, before noise is added. No spatial smoothing is performed if
BEAMFWHM is zero. See also parameter PRECAT. [current value]



DECONV = _LOGICAL (Read)
````````````````````````
If TRUE, the clump properties stored in the output catalogue will be
modified to take account of the smoothing caused by the instrumental
beam width. Note, if parameter PRECAT is TRUE, then this deconvolution
has no effect since no smoothing has been applied to the clumps at the
time when the catalogue is created. [TRUE]



FWHM1( 2 ) = _REAL (Read)
`````````````````````````
Defines the distribution from which the FWHM (Full Width at Half Max)
for pixel axis 1 of each clump is chosen. Values should be supplied in
units of pixel. See parameter PARDIST for additional information.
[current value]



FWHM2( 2 ) = _REAL (Read)
`````````````````````````
Defines the distribution from which the FWHM (Full Width at Half Max)
for pixel axis 2 of each clump is chosen. Values should be supplied in
units of pixel. See parameter PARDIST for additional information.
[current value]



FWHM3( 2 ) = _REAL (Read)
`````````````````````````
Defines the distribution from which the FWHM (Full Width at Half Max)
for pixel axis 3 of each clump is chosen. Values should be supplied in
units of pixel. See parameter PARDIST for additional information.
[current value]



GRID = _INTEGER (Read)
``````````````````````
If null (!), the clump centres are distributed randomly over the
array. If not null, the clump centres are positioned on a regular grid
with dimensions specified by parameter NCLUMPS. The grid occupies the
entire output array, excluding a border of width equal to the integer
value supplied for parameter GRID (in pixels). [!]



LBND() = _INTEGER (Read)
````````````````````````
The lower pixel bounds of the output NDF. The number of values
supplied (1, 2 or 3) defines the number of pixel axes in the output
NDF (an error is reported if the number of values supplied for LBND
and UBND differ). If an NDF is supplied for parameter LIKE, the
suggested defaults for this parameter will be the lower pixel bounds
of the supplied NDF.



LIKE = NDF (Read)
`````````````````
An NDF from which to inherited WCS information. If a null (!) value is
supplied, the output catalogue will hold values in pixel coordinates,
and there will be no WCS in any of the output NDFs. [!]



MODEL = NDF (Write)
```````````````````
The NDF to receive the simulated data, excluding noise. A CUPID
extension is added to this NDF, containing information about each
clump in the same format as produced by the FINDCLUMPS command. This
includes an NDF holding an of the individual clump.



NCLUMP() = _INTEGER (Read)
``````````````````````````
The number of clumps to create. If parameter GRID is null (!), a
single value should be supplied, and the specified number of clumps
are positioned randomly over the output array. If parameter GRID is
not null, the number of values supplied should match the number of
pixel axes in the output array, and each value is then the number of
clumps along the corresponding pixel axis. Note, any clumps that touch
an edge of the aray will be excluded from the output array.



OUT = NDF (Write)
`````````````````
The NDF to receive the simulated data, including instrumental blurring
and noise.



OUTCAT = FILENAME (Write)
`````````````````````````
The output catalogue in which to store the clump parameters. There
will be one row per clump, with the following columns:


+ Peak1: The position of the clump peak value on axis 1.
+ Peak2: The position of the clump peak value on axis 2.
+ Peak3: The position of the clump peak value on axis 3.
+ Cen1: The position of the clump centroid on axis 1.
+ Cen2: The position of the clump centroid on axis 2.
+ Cen3: The position of the clump centroid on axis 3.
+ Size1: The size of the clump along pixel axis 1.
+ Size2: The size of the clump along pixel axis 2.
+ Size3: The size of the clump along pixel axis 3.
+ Sum: The total data sum in the clump.
+ Peak: The peak value in the clump.
+ Volume: The total number of pixels falling within the clump.

There is also an optional column called "Shape" containing an STC-S
description of the spatial coverage of each clump. See parameter
SHAPE.
The coordinate system used to describe the peak and centroid positions
is determined by the value supplied for parameter LIKE. If LIKE is
null (!), then positions are specified in the pixel coordinate system.
In addition, the clump sizes are specified in units of pixels, and the
clump volume is specified in units of cubic pixels (square pixels for
2D data). If an NDF is supplied for LIKE, then positions are specified
in the current coordinate system of the specified NDF. In addition,
the clump sizes and volumes are specified in WCS units. Note, the
sizes are still measured parallel to the pixel axes, but are recorded
in WCS units rather than pixel units. Celestial coordinate positions
are units of degrees, sizes are in units are arc-seconds, and areas in
square arc-seconds. Spectral coordinates are in the units displayed by
the KAPPA command "ndftrace".
If the data has less than 3 pixel axes, then the columns describing
the missing axes will not be present in the catalogue.
The catalogue inherits any WCS information from the NDF supplied for
parameter LIKE.
The "size" of the clump on an axis is the RMS deviation of each pixel
centre from the clump centroid, where each pixel is weighted by the
correspinding pixel data value. This excludes the instrumental
smoothing specified by BEAMFWHM and VELFWHM.
The KAPPA command "listshow" can be used to draw markers at the
central positions of the clumps described in a catalogue. For
instance, the command "listshow fred plot=mark" will draw markers
identifying the positions of the clumps described in file fred.FIT,
overlaying the markers on top of the currently displayed image.
Specifying "plot=STCS" instead of "plot=mark" will cause the spatial
outline of the clump to be drawn if it is present in the catalogue
(see parameter SHAPE).



PARDIST = LITERAL (Read)
````````````````````````
The shape of the distribution from which clump parameter values are
chosen. Can be "Normal", "Uniform" or "Poisson". The distribution for
each clump parameter is specified by its own ADAM parameter containing
two values; the mean and the width of the distribution. If PARDIST is
"Normal", the width is the standard deviation. If PARDIST is
"Uniform", the width is half the range between the maximum and minimum
parameter values. In either of these two cases, if a width of zero is
supplied, the relevant parameter is given a constant value equal to
the specified mean. If PARDIST is "Poisson", the width is ignored.
[current value]



PEAK( 2 ) = _REAL (Read)
````````````````````````
Defines the distribution from which the peak value (above the local
background) of each clump is chosen. See parameter PARDIST for
additional information. [current value]



PRECAT = _LOGICAL (Read)
````````````````````````
If FALSE, the output catalogue is created from the clumps after the
instrumental smoothing specified by parameters BEAMFWHM and VELFWHM
has been applied. If TRUE, the catalogue is created from the data
before the instrumental smoothing is applied (in which case parameter
DECONV has no effect). [FALSE]



RMS = _REAL (Read)
``````````````````
The RMS (Gaussian) noise to be added to the output data. [current
value]



SHAPE = LITERAL (Read)
``````````````````````
Specifies the shape that should be used to describe the spatial
coverage of each clump in the output catalogue. It can be set to
"None", "Polygon" or "Ellipse". If it is set to "None", the spatial
shape of each clump is not recorded in the output catalogue.
Otherwise, the catalogue will have an extra column named "Shape"
holding an STC-S description of the spatial coverage of each clump.
"STC-S" is a textual format developed by the IVOA for describing
regions within a WCS - see
http://www.ivoa.net/Documents/latest/STC-S.html for details. These
STC-S desriptions can be displayed by the KAPPA:LISTSHOW command, or
using GAIA. Since STC-S cannot describe regions within a pixel array,
it is necessary to provide an NDF to define the WCS (using parameter
LIKE) if using this option. An error will be reported if the WCS in
the NDF does not contain a pair of celestial sky axes.


+ Polygon: Each polygon will have, at most, 15 vertices. If the data
is 2-dimensional, the polygon is a fit to the clump's outer boundary
(the region containing all godo data values). If the data is
3-dimensional, the spatial footprint of each clump is determined by
rejecting the least significant 10% of spatial pixels, where
"significance" is measured by the number of spectral channels that
contribute to the spatial pixel. The polygon is then a fit to the
outer boundary of the remaining spatial pixels.
+ Ellipse: All data values in the clump are projected onto the spatial
  plane and "size" of the collapsed clump at four different position
  angles - all separated by 45 degrees - is found (see the OUTCAT
  parameter for a description of clump "size"). The ellipse that
  generates the same sizes at the four position angles is then found and
  used as the clump shape.

In general, "Ellipse" will outline the brighter, inner regions of each
clump, and "Polygon" will include the fainter outer regions. ["None"]



TRUNC = _REAL (Read)
````````````````````
The level (above the local background) at which clumps should be
truncated to zero, given as a fraction of the noise level specified by
RMS. [current value]



UBND() = _INTEGER (Read)
````````````````````````
The upper pixel bounds of the output NDF. The number of values
supplied (1, 2 or 3) defines the number of pixel axes in the output
NDF (an error is reported if the number of values supplied for LBND
and UBND differ). If an NDF is supplied for parameter LIKE, the
suggested defaults for this parameter will be the upper pixel bounds
of the supplied NDF.



VELFWHM = _REAL (Read)
``````````````````````
The FWHM of the Gaussian velocity resolution of the instrument, in
pixels. The generated clumps are smoothed on the velocity axis with a
Gaussian beam of this FWHM, before noise is added. No velocity
smoothing is performed if VELFWHM is zero. See also parameter PRECAT.
[current value]



VGRAD1( 2 ) = _REAL (Read)
``````````````````````````
Defines the distribution from which the projection of the internal
velocity gradient vector onto pixel axis 1 of each clump is chosen.
Values should be supplied in dimensionless units of "velocity pixels
per spatial pixel". See parameter PARDIST for additional information.
[current value]



VGRAD2( 2 ) = _REAL (Read)
``````````````````````````
Defines the distribution from which the projection of the internal
velocity gradient vector onto pixel axis 2 of each clump is chosen.
Values should be supplied in dimensionless units of "velocity pixels
per spatial pixel". See parameter PARDIST for additional information.
[current value]



Notes
~~~~~


+ If 3D data is created, pixel axes 1 and 2 are the spatial axes, and
pixel axis 3 is the velocity axis.
+ The positions of the clumps are chosen from a uniform distribution
  on each axis.




Synopsis
~~~~~~~~
void makeclumps( int *status );


Copyright
~~~~~~~~~
Copyright (C) 2005 Particle Physics & Astronomy Research Council. All
Rights Reserved.


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


