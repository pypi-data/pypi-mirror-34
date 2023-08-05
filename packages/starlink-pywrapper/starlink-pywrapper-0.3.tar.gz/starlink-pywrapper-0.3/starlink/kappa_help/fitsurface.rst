

FITSURFACE
==========


Purpose
~~~~~~~
Fits a polynomial surface to two-dimensional data array


Description
~~~~~~~~~~~
This task fits a surface to a two-dimensional data array stored array
within an NDF data structure. At present it only permits a fit with a
polynomial, and the coefficients of that surface are stored in a
POLYNOMIAL structure (SGP/38) as an extension to that NDF.
Unlike SURFIT, neither does it bin the data nor does it reject
outliers.


Usage
~~~~~


::

    
       fitsurface ndf [fittype] { nxpar nypar
                                { [knots]
                             fittype
       



ADAM parameters
~~~~~~~~~~~~~~~



COSYS = LITERAL (Read)
``````````````````````
The co-ordinate system to be used. This can be either "World" or
"Data". If COSYS = "World" the co-ordinates used to fits the surface
are pixel co-ordinates. If COSYS = "Data" the data co-ordinates used
are used in the fit, provided there are axis centres present in the
NDF. COSYS="World" is recommended. [Current co-ordinate system]



FITTYPE = LITERAL (Read)
````````````````````````
The type of fit. It must be either "Polynomial" for a polynomial or
"Spline" for a bi-cubic spline. ["Polynomial"]



KNOTS( 2 ) = _INTEGER (Read)
````````````````````````````
The number of interior knots used for the bi-cubic-spline fit along
the x and y axes. These knots are equally spaced within the image.
Both values must be in the range 0 to 11. If you supply a single
value, it applies to both axes. Thus 1 creates one interior knot,
[5,4] gives five along the x axis and four along the y direction.
Increasing this parameter values increases the flexibility of the
surface. Normally, 4 is a reasonable value. The upper limit of
acceptable values will be reduced along each axis when its binned
array dimension is fewer than 29. KNOTS is only accessed when
FITTYPE="Spline". The default is the current value, which is 4
initially. []



NDF = NDF (Update)
``````````````````
The NDF containing the two-dimensional data array to be fitted.



NXPAR = _INTEGER (Read)
```````````````````````
The number of fitting parameters to be used in the x direction. It
must be in the range 1 to 15 for a polynomial fit. Thus 1 gives a
constant, 2 a linear fit, 3 a quadratic etc. Increasing this parameter
increases the flexibility of the surface in the x direction. The upper
limit of acceptable values will be reduced for arrays with an x
dimension less than 29. NXPAR is only accessed when
FITTYPE="Polynomial".



NYPAR = _INTEGER (Read)
```````````````````````
The number of fitting parameters to be used in the y direction. It
must be in the range 1 to 15 for a polynomial fit. Thus 1 gives a
constant, 2 a linear fit, 3 a quadratic etc. Increasing this parameter
increases the flexibility of the surface in the y direction. The upper
limit of acceptable values will be reduced for arrays with a y
dimension less than 29. NYPAR is only accessed when
FITTYPE="Polynomial".



OVERWRITE = _LOGICAL (Read)
```````````````````````````
OVERWRITE=TRUE, allows an NDF extension containing an existing surface
fit to be overwritten. OVERWRITE=FALSE protects an existing surface-
fit extension, and should one exist, an error condition will result
and the task terminated. [TRUE]



VARIANCE = _LOGICAL (Read)
``````````````````````````
A flag indicating whether any variance array present in the NDF is
used to define the weights for the fit. If VARIANCE is TRUE and the
NDF contains a variance array this will be used to define the weights,
otherwise all the weights will be set equal. [TRUE]



XMAX = _DOUBLE (Read)
`````````````````````
The maximum x value to be used in the fit. This must be greater than
or equal to the x co-ordinate of the right-hand pixel in the data
array. Normally this parameter is automatically set to the maximum x
co-ordinate found in the data, but this mechanism can be overridden by
specifying XMAX on the command line. The parameter is provided to
allow the fit limits to be fine tuned for special purposes. It should
not normally be altered. If a null (!) value is supplied, the value
used is the maximum x co-ordinate of the fitted data. [!]



XMIN = _DOUBLE (Read)
`````````````````````
The minimum x value to be used in the fit. This must be smaller than
or equal to the x co-ordinate of the left-hand pixel in the data
array. Normally this parameter is automatically set to the minimum x
co-ordinate found in the data, but this mechanism can be overridden by
specifying XMIN on the command line. The parameter is provided to
allow the fit limits to be fine tuned for special purposes. It should
not normally be altered. If a null (!) value is supplied, the value
used is the minimum x co-ordinate of the fitted data. [!]



YMAX = _DOUBLE (Read)
`````````````````````
The maximum y value to be used in the fit. This must be greater than
or equal to the y co-ordinate of the top pixel in the data array.
Normally this parameter is automatically set to the maximum y co-
ordinate found in the data, but this mechanism can be overridden by
specifying YMAX on the command line. The parameter is provided to
allow the fit limits to be fine tuned for special purposes. It should
not normally be altered. If a null (!) value is supplied, the value
used is the maximum y co-ordinate of the fitted data. [!]



YMIN = _DOUBLE (Read)
`````````````````````
The minimum y value to be used in the fit. This must be smaller than
or equal to the y co-ordinate of the bottom pixel in the data array.
Normally this parameter is automatically set to the minimum y co-
ordinate found in the data, but this mechanism can be overridden by
specifying YMIN on the command line. The parameter is provided to
allow the fit limits to be fine tuned for special purposes. It should
not normally be altered. If a null (!) value is supplied, the value
used is the minimum y co-ordinate of the fitted data. [!]



Examples
~~~~~~~~
fitsurface virgo nxpar=4 nypar=4 novariance
This fits a bi-cubic polynomial surface to the data array in the NDF
called virgo. All the data values are given equal weight. The
coefficients of the fitted surface are stored in an extension of
virgo.
fitsurface virgo nxpar=4 nypar=4
As the first example except the data variance, if present, is used to
weight the data values.
fitsurface virgo fittype=spl
As the previous example except a B-spline fit is made using four
interior knots along both axes.
fitsurface virgo fittype=spl knots=[10,7]
As the previous example except now there are ten interior knots along
the x axis and seven along the y axis.
fitsurface mkn231 nxpar=6 nypar=2 cosys=d xmin=-10.0 xmax=8.5
This fits a polynomial surface to the data array in the NDF called
mkn231. A fifth order is used along the x direction, but only a linear
fit along the y direction. The fit is made between x data co-ordinates
-10.0 to 8.5. The variance weights the data values. The coefficients
of the fitted surface are stored in an extension of mkn231.



Notes
~~~~~
A polynomial surface fit is stored in a SURFACEFIT extension,
component FIT of type POLYNOMIAL, variant CHEBYSHEV or BSPLINE. This
is read by MAKESURFACE to create a NDF of the fitted surface.
For further details of the CHEBYSHEV variant see SGP/38. The CHEBYSHEV
variant includes the fitting variance for each coefficient.
The BSPLINE variant structure is provisional. It contain the spline
coefficients in the two-dimensional DATA_ARRAY component, the knots in
XKNOTS and YKNOTS arrays, and a scaling factor to restore the original
values after spline evaluation recorded in component SCALE. All of
these components have type _REAL.
Also stored in the SURFACEFIT extension are the r.m.s. deviation to
the fit (component RMS), the maximum absolute deviation (component
RSMAX), and the co-ordinate system (component COSYS) translated to AST
Domain names AXIS (for parameter COSYS="Data") and PIXEL ("World").


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: MAKESURFACE, SURFIT.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995-1997, 2003-2004 Central Laboratory of the Research Councils.
Copyright (C) 2007, 2009 Science & Technology Facilities Council. All
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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
and HISTORY components of an NDF data structure.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using double-precision floating point.




