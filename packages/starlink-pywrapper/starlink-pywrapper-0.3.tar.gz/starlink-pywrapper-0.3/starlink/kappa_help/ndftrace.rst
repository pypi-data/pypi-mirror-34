

NDFTRACE
========


Purpose
~~~~~~~
Displays the attributes of an NDF data structure


Description
~~~~~~~~~~~
This routine displays the attributes of an NDF data structure
including:


+ its name;
+ the values of its character components (title, label and units);
+ its shape (pixel bounds, dimension sizes, number of dimensions and
total number of pixels);
+ axis co-ordinate information (axis labels, units and extents);
+ optionally, axis array attributes (type and storage form) and the
values of the axis normalisation flags;
+ attributes of the main data array and any other array components
present (including the type and storage form and an indication of
whether `bad' pixels may be present);
+ attributes of the current co-ordinate Frame in the WCS component
(title, domain, and, optionally, axis labels and axis units, plus the
system epoch and projection for sky co-ordinate Frames). In addition
the bounding box of the NDF within the Frame is displayed.
+ optionally, attributes of all other co-ordinate Frames in the WCS
component.
+ a list of any NDF extensions present, together with their data
types; and
+ history information (creation and last-updated dates, the update
  mode and the number of history records).

Most of this information is output to parameters.


Usage
~~~~~


::

    
       ndftrace ndf
       



ADAM parameters
~~~~~~~~~~~~~~~



AEND( ) = _DOUBLE (Write)
`````````````````````````
The axis upper extents of the NDF. For non-monotonic axes, zero is
used. See parameter AMONO. This is not assigned if AXIS is FALSE.



AFORM( ) = LITERAL (Write)
``````````````````````````
The storage forms of the axis centres of the NDF. This is only written
when FULLAXIS is TRUE and AXIS is TRUE.



ALABEL( ) = LITERAL (Write)
```````````````````````````
The axis labels of the NDF. This is not assigned if AXIS is FALSE.



AMONO( ) = _LOGICAL (Write)
```````````````````````````
These are TRUE when the axis centres are monotonic, and FALSE
otherwise. This is not assigned if AXIS is FALSE.



ANORM( ) = _LOGICAL (Write)
```````````````````````````
The axis normalisation flags of the NDF. This is only written when
FULLAXIS is TRUE and AXIS is TRUE.



ASTART( ) = _DOUBLE (Write)
```````````````````````````
The axis lower extents of the NDF. For non-monotonic axes, zero is
used. See parameter AMONO. This is not assigned if AXIS is FALSE.



ATYPE( ) = LITERAL (Write)
``````````````````````````
The data types of the axis centres of the NDF. This is only written
when FULLAXIS is TRUE and AXIS is TRUE.



AUNITS( ) = LITERAL (Write)
```````````````````````````
The axis units of the NDF. This is not assigned if AXIS is FALSE.



AVARIANCE( ) = _LOGICAL (Write)
```````````````````````````````
Whether or not there are axis variance arrays present in the NDF. This
is only written when FULLAXIS is TRUE and AXIS is TRUE.



AXIS = _LOGICAL (Write)
```````````````````````
Whether or not the NDF has an axis system.



BAD = _LOGICAL (Write)
``````````````````````
If TRUE, the NDF's data array may contain bad values.



BADBITS = LITERAL (Write)
`````````````````````````
The BADBITS mask. This is only valid when QUALITY is TRUE.



CURRENT = _INTEGER (Write)
``````````````````````````
The integer Frame index of the current co-ordinate Frame in the WCS
component.



DIMS( ) = _INTEGER (Write)
``````````````````````````
The dimensions of the NDF.



EXTNAME( ) = LITERAL (Write)
````````````````````````````
The names of the extensions in the NDF. It is only written when NEXTN
is positive.



EXTTYPE( ) = LITERAL (Write)
````````````````````````````
The types of the extensions in the NDF. Their order corresponds to the
names in EXTNAME. It is only written when NEXTN is positive.



FDIM( ) = _INTEGER (Write)
``````````````````````````
The numbers of axes in each co-ordinate Frame stored in the WCS
component of the NDF. The elements in this parameter correspond to
those in the FDOMAIN and FTITLE parameters. The number of elements in
each of these parameters is given by NFRAME.



FDOMAIN( ) = LITERAL (Write)
````````````````````````````
The domain of each co-ordinate Frame stored in the WCS component of
the NDF. The elements in this parameter correspond to those in the
FDIM and FTITLE parameters. The number of elements in each of these
parameters is given by NFRAME.



FLABEL( ) = LITERAL (Write)
```````````````````````````
The axis labels from the current WCS Frame of the NDF.



FLBND( ) = _DOUBLE (Write)
``````````````````````````
The lower bounds of the bounding box enclosing the NDF in the current
WCS Frame. The number of elements in this parameter is equal to the
number of axes in the current WCS Frame (see FDIM). Celestial axis
values will be in units of radians.



FUBND( ) = _DOUBLE (Write)
``````````````````````````
The upper bounds of the bounding box enclosing the NDF in the current
WCS Frame. The number of elements in this parameter is equal to the
number of axes in the current WCS Frame (see FDIM). Celestial axis
values will be in units of radians.



FORM = LITERAL (Write)
``````````````````````
The storage form of the NDF's data array. This will be "SIMPLE",
"PRIMITIVE", "SCALED" or "DELTA".



FPIXSCALE( ) = LITERAL (Write)
``````````````````````````````
The nominal WCS pixel scale for each axis in the current WCS Frame.
For celestial axes, the value stored will be in arc-seconds. For other
axes, the value stored will be in the units given by the corresponding
element of FUNIT.



FTITLE( ) = LITERAL (Write)
```````````````````````````
The title of each co-ordinate Frame stored in the WCS component of the
NDF. The elements in this parameter correspond to those in the FDOMAIN
and FDIM parameters. The number of elements in each of these
parameters is given by NFRAME.



FULLAXIS = _LOGICAL (Read)
``````````````````````````
If the NDF being examined has an axis co-ordinate system defined, then
by default only the label, units and extent of each axis will be
displayed. However, if a TRUE value is given for this parameter, full
details of the attributes of all the axis arrays will also be given.
[FALSE]



FULLFRAME = _LOGICAL (Read)
```````````````````````````
If a FALSE value is given for this parameter then only the Title and
Domain attributes plus the axis labels and units are displayed for a
co-ordinate Frame. Otherwise, a more complete description is given,
including the bounds of the NDF within the Frame. [FALSE]



FULLWCS = _LOGICAL (Read)
`````````````````````````
If a TRUE value is given for this parameter then all co-ordinate
Frames in the WCS component of the NDF are displayed. Otherwise, only
the current co-ordinate Frame is displayed. [FALSE]



FUNIT( ) = LITERAL (Write)
``````````````````````````
The axis units from the current WCS Frame of the NDF.



HISTORY = _LOGICAL (Write)
``````````````````````````
Whether or not the NDF contains HISTORY records.



LABEL = LITERAL (Write)
```````````````````````
The label of the NDF.



LBOUND( ) = _INTEGER (Write)
````````````````````````````
The lower bounds of the NDF.



NDF = NDF (Read)
````````````````
The NDF data structure whose attributes are to be displayed.



NDIM = _INTEGER (Write)
```````````````````````
The number of dimensions of the NDF.



NEXTN = _INTEGER (Write)
````````````````````````
The number of extensions in the NDF.



NFRAME = _INTEGER (Write)
`````````````````````````
The number of WCS Frames described by parameters FDIM, FDOMAIN and
FTITLE. Set to zero if WCS is FALSE.



QUALITY = _LOGICAL (Write)
``````````````````````````
Whether or not the NDF contains a QUALITY array.



SCALE = _DOUBLE (Write)
```````````````````````
The scale factor associated with the data array. This will be 1.0
unless the Data array is stored in SCALED form. See also SCTYPE, ZERO
and FORM. The unscaled data values are derived from the scaled values
as follows: "unscaled = SCALE*scaled + ZERO".



SCTYPE = LITERAL (Write)
````````````````````````
The data type of the scaled values stored in the NDF's data array.
This will be the same as TYPE unless the Data array is stored in
SCALED form. See also FORM, SCALE and ZERO.



TITLE = LITERAL (Write)
```````````````````````
The title of the NDF.



TYPE = LITERAL (Write)
``````````````````````
The data type of the NDF's data array.



UBOUND( ) = _INTEGER (Write)
````````````````````````````
The upper bounds of the NDF.



UNITS = LITERAL (Write)
```````````````````````
The units of the NDF.



VARIANCE = _LOGICAL (Write)
```````````````````````````
Whether or not the NDF contains a variance array.



WCS = _LOGICAL (Write)
``````````````````````
Whether or not the NDF has any WCS co-ordinate Frames, over and above
the default GRID, PIXEL and AXIS Frames.



WIDTH( ) = _LOGICAL (Write)
```````````````````````````
Whether or not there are axis width arrays present in the NDF. This is
only written when FULLAXIS is TRUE and AXIS is TRUE.



ZERO = _DOUBLE (Write)
``````````````````````
The zero offset associated with the data array. This will be 0.0
unless the Data array is stored in SCALED form. See also SCTYPE, SCALE
and FORM. The unscaled data values are derived from the scaled values
as follows: "unscaled = SCALE*scaled + ZERO".



Examples
~~~~~~~~
ndftrace mydata
Displays information about the attributes of the NDF structure called
mydata.
ndftrace ndf=r106 fullaxis
Displays information about the NDF structure r106, including full
details of any axis arrays present.
ndftrace mydata ndim=(mdim)
Passes the number of dimensions of the NDF called mydata into the ICL
variable mdim.



Notes
~~~~~


+ If the WCS component of the NDF is undefined, then an attempt is
made to find WCS information from two other sources: first, an IRAS90
astrometry structure, and second, the FITS extension. If either of
these sources yield usable WCS information, then it is displayed in
the same way as the NDF WCS component. Other KAPPA applications will
use this WCS information as if it were stored in the WCS component.
+ The reporting of NDF attributes is suppressed when the message
  filter environment variable MSG_FILTER is set to QUIET. It benefits
  procedures and scripts where only the output parameters are needed.
  The creation of output parameters is unaffected by MSG_FILTER.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: WCSFRAME; HDSTRACE


Copyright
~~~~~~~~~
Copyright (C) 1990-1994 Science & Engineering Research Council.
Copyright (C) 1995, 1997, 1999-2000, 2003-2004 Central Laboratory of
the Research Councils. Copyright (C) 2005-2006 Particle Physics &
Astronomy Research Council. Copyright (C) 2009 Science and Technology
Facilities Council. All Rights Reserved.


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


