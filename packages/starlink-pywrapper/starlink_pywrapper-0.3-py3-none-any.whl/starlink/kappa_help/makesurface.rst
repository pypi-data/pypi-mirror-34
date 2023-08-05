

MAKESURFACE
===========


Purpose
~~~~~~~
Creates a two-dimensional NDF from the coefficients of a polynomial
surface


Description
~~~~~~~~~~~
The coefficients describing a two-dimensional polynomial surface are
read from a SURFACEFIT extension in an NDF (written by FITSURFACE),
and are used to create a two-dimensional surface of specified size and
extent. The surface is written to a new NDF.
The size and extent of the surface may be obtained from a template NDF
or given explicitly.
Elements in the new NDF outside the defined range of the polynomial or
spline will be set to bad values.


Usage
~~~~~


::

    
       makesurface in out [like] type=? lbound=? ubound=? xlimit=?
          ylimit=?
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The NDF containing the SURFACEFIT extension.



LBOUND( 2 ) = _INTEGER (Read)
`````````````````````````````
Lower bounds of new NDF (if LIKE=!). The suggested defaults are the
lower bounds of the IN NDF.



LIKE = NDF (Read)
`````````````````
An optional template NDF which, if specified, will be used to define
the labels, size, shape, data type and axis range of the new NDF. If a
null response (!) is given, the label, units, axis labels, and axis
units are taken from the IN NDF. The task prompts for the data type
and bounds, using those of the IN NDF as defaults, and the axis
ranges. [!]



OUT = NDF (Write)
`````````````````
The new NDF to contain the surface fit.



TITLE = LITERAL (Read)
``````````````````````
A title for the new NDF. If a null response (!) is given, the title
will be propagated either from LIKE, or from IN if LIKE=!. [!]



TYPE = LITERAL (Read)
`````````````````````
Data type for the new NDF (if LIKE=!). It must be one of the
following: "_DOUBLE", "_REAL", "_INTEGER", "_WORD", "_BYTE", "_UBYTE".
The suggested default is the data type of the data array in the IN
NDF.



UBOUND( 2 ) = _INTEGER (Read)
`````````````````````````````
Upper bounds of new NDF (if LIKE=!). The suggested defaults are the
upper bounds of the IN NDF.



VARIANCE = _LOGICAL (Read)
``````````````````````````
If TRUE, a uniform variance array equated to the mean squared residual
of the fit is created in the output NDF, provided the SURFACEFIT
structure contains the RMS component. [FALSE]



XLIMIT( 2 ) = _DOUBLE (Read)
````````````````````````````
Co-ordinates of the left then right edges of the x axis (if LIKE=!).
The suggested defaults are respectively the minimum and maximum x co-
ordinates of the IN NDF.



YLIMIT( 2 ) = _DOUBLE (Read)
````````````````````````````
Co-ordinates of the bottom then top edges of the y axis (if LIKE=!).
The suggested defaults are respectively the minimum and maximum y co-
ordinates of the IN NDF.



Examples
~~~~~~~~
makesurface flatin flatout \
This generates a two-dimensional image in the NDF called flatout using
the surface fit stored in the two-dimensional NDF flatin. The created
image has the same data type, bounds, and co-ordinate limits as the
data array of flatin.
makesurface flatin flatout type=_wo lbound=[1,1] ubound=[320,512]
As the previous example, except that the data array in flatout has
data type _WORD, and the bounds of flatout are 1:320, 1:512.
makesurface flatin flatout like=flatin
This has the same effect as the first example, except it has an
advantage. If the current co-ordinate system is "Data" and either or
both of the axes are inverted (values decrease with increasing pixel
index), the output image will be correctly oriented.
makesurface flatin flatout template title="Surface fit"
This generates a two-dimensional image in the NDF called flatout using
the surface fit stored in the two-dimensional NDF flatin. The created
image inherits the attributes of the NDF called template. The title of
flatout is "Surface fit".



Notes
~~~~~


+ The polynomial surface fit is stored in SURFACEFIT extension,
component FIT of type POLYNOMIAL, variant CHEBYSHEV or BSPLINE. This
extension is created by FITSURFACE. Also read from the SURFACEFIT
extension is the co-ordinate system (component COSYS), and the fit RMS
(component RMS).
+ When LIKE=!, COSYS="Data" or "Axis" and the original NDF had an axis
  that decreased with increasing pixel index, you may want to flip the
  co-ordinate limits (via parameters XLIMIT or YLIMIT) to match the
  original sense of the axis, otherwise the created surface will be
  flipped with respect to the image from which it was fitted.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSURFACE, SURFIT.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995, 1997-1998, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2007-2010 Science and Technology Facilities Council. All
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
LABEL, TITLE, UNITS, WCS, and HISTORY components of an NDF data
structure and propagates all extensions. However, neither QUALITY nor
a SURFACEFIT extension is propagated when LIKE is not null.
+ All non-complex numeric data types can be handled. Processing is
  performed in single- or double-precision floating point, as
  appropriate.




