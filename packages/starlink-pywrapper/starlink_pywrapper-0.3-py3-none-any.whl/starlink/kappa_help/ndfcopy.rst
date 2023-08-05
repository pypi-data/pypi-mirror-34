

NDFCOPY
=======


Purpose
~~~~~~~
Copies an NDF (or NDF section) to a new location


Description
~~~~~~~~~~~
This application copies an NDF to a new location. By supplying an NDF
section as input it may be used to extract a subset, or to change the
size or dimensionality of an NDF. A second NDF may also be supplied to
act as a shape template, and hence to define the region of the first
NDF which is to be copied.
Any unused space will be eliminated by the copying operation performed
by this routine, so it may be used as a way of compressing NDF
structures from which components have been deleted. This ability also
makes NDFCOPY a useful alternative to SETBOUND in cases where an NDF's
size is to be reduced.


Usage
~~~~~


::

    
       ndfcopy in out
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The name of an array component in the input NDF (specified by
Parameter IN) that will become the DATA_ARRAY in the output NDF
(specified by Parameter OUT). It has the following options.
"Data" -- Each array component present is propagated to its
counterpart. "Variance" -- The VARIANCE component in the input NDF
becomes the DATA_ARRAY in the output NDF and retains its data type.
The original DATA_ARRAY is not copied. "Error" -- The square root of
the VARIANCE component in the input NDF becomes the DATA_ARRAY in the
output NDF and retains the VARIANCE's data type. The original
DATA_ARRAY and VARIANCE components are not copied. "Quality" -- The
QUALITY component in the input NDF becomes the DATA_ARRAY in the
output NDF and will be data type _UBYTE. The original DATA_ARRAY and
VARIANCE components are not copied. ["Data"]



EXTEN = _LOGICAL (Read)
```````````````````````
If set to FALSE (the default), any NDFs contained within extensions of
the input NDF are copied to equivalent places within the output NDF
without change. If set TRUE, then any extension NDFs which have the
same bounds as the base input NDF are padded or trimmed as necessary
in order to ensure that they have the same bounds as the output NDF.
[FALSE]



IN = NDF (Read)
```````````````
The input NDF (or section) which is to be copied.



LIKE = NDF (Read)
`````````````````
This parameter may be used to supply an NDF to be used as a shape
template during the copying operation. If such a template is supplied,
then its shape will be used to select a matching section from the
input NDF before copying takes place. By default, no template will be
used and the shape of the output NDF will therefore match that of the
input NDF (or NDF section). The shape of the template in either pixel
indices or the current WCS Frame may be used, as selected by Parameter
LIKEWCS. [!]



LIKEWCS = _LOGICAL (Read)
`````````````````````````
If TRUE, then the WCS bounds of the template supplied via Parameter
LIKE are used to decide on the bounds of the output NDF. Otherwise,
the pixel bounds of the template are used. [FALSE]



OUT = NDF (Write)
`````````````````
The output NDF data structure.



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null value (the default) will cause the
title of the NDF supplied for Parameter IN to be used instead. [!]



TRIM = _LOGICAL (Read)
``````````````````````
If TRUE, then the number of pixel axes in the output NDF will be
reduced if necessary to remove any pixel axes which span only a single
pixel. For instance if "stokes" is a three-dimensional data cube with
pixel bounds (1:100,-50:40,1:3), and the Parameter IN is given the
value "stokes(,,2)", then the dimensionality of the output depends on
the setting of TRIM: if TRIM=FALSE, the output is three-dimensional
with pixel bounds (1:100,-50:40,2:2), and if TRIM=TRUE the output is
two-dimensional with pixel bounds (1:100,-50:40). In this example, the
third pixel axis spans only a single pixel and is consequently removed
if TRIM=TRUE. [FALSE]



TRIMBAD = _LOGICAL (Read)
`````````````````````````
If TRUE, then the pixel bounds of the output NDF are trimmed to
exclude any border of bad pixels within the input NDF. That is, the
output NDF will be the smallest NDF that encloses all good data values
in the input NDF. [FALSE]



TRIMWCS = _LOGICAL (Read)
`````````````````````````
This parameter is only accessed if Parameter TRIM is TRUE. It controls
the number of axes in the current WCS co-ordinate Frame of the output
NDF. If TRIMWCS=TRUE, then the current Frame in the output NDF will
have the same number of axes as there are pixel axes in the output
NDF. If this involves removing axes, then the axes to retain are
specified by Parameter USEAXIS. If TRIMWCS=FALSE, then all axes are
retained in the current WCS Frame of the output NDF. Using the example
in the description of the TRIM parameter, if the input NDF "stokes"
has a three-dimensional current WCS Frame with axes (RA,Dec,Stokes)
and TRIMWCS=TRUE, then an axis will be removed from the current Frame
to make it two-dimensional (that is, to match the number of pixel axes
remaining after the removal of insignificant pixel axes). The choice
of which two axes to retain is controlled by Parameter USEAXIS. If, on
the other hand, TRIMWCS was set to FALSE, then the output NDF would
still have two pixel axes, but the current WCS Frame would retain all
three axes from the input NDF. If one or more current Frame axes are
removed, the transformation from the current Frame to pixel Frame may
become undefined resulting in some WCS operations being unusable. The
inverse of this transformation (from pixel Frame to current Frame) is
unchanged however. [TRUE]



USEAXIS = LITERAL (Read)
````````````````````````
This parameter is only accessed if TRIM and TRIMWCS are both TRUE, and
some axes need to be removed from the current WCS Frame of the output
NDF. It gives the axes which are to be retained in the current WCS
Frame of the output NDF. Each axis can be specified using one of the
following options.


+ An integer index of an axis within the current Frame of the input
NDF (in the range 1 to the number of axes in the current Frame).
+ An axis symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

The dynamic default selects the axes with the same indices as the
pixel axes being copied. The value should be given as a comma-
separated list. []



Examples
~~~~~~~~
ndfcopy infile outfile
Copies the contents of the NDF structure infile to the new structure
outfile. Any unused space will be eliminated during the copying
operation.
ndfcopy infile outfile comp=var
As the previous example except that the VARIANCE component of NDF
infile becomes the DATA_ARRAY of NDF outfile.
ndfcopy in=data1(3:40,-3:17) out=data2 title="Extracted section"
Copies the section (3:40,-3:17) of the NDF called data1 to a new NDF
called data2. The output NDF is assigned the new title "Extracted
section", which replaces the title derived from the input NDF.
ndfcopy galaxy newgalaxy like=oldgalaxy
Copies a section of the NDF called galaxy to form a new NDF called
newgalaxy. The section which is copied will correspond in shape with
the template oldgalaxy. Thus, after the copying operation, both
newgalaxy and oldgalaxy will have the same pixel-index bounds.
ndfcopy aa(20~11,20~11) bb like=aa
Copies from the NDF section consisting of an 11x11 pixel region of aa
centred on pixel (20,20), into a new NDF called bb. The shape of the
region copied is made to match the original shape of aa. The effect is
to extract the selected square region of pixels into a new NDF of the
same shape as the original, setting the surrounding region to the bad-
pixel value.
ndfcopy survey(12h23m:12h39m,11d:13d50m,) virgo trimwcs trim
Copies a section specified by equatorial co-ordinate ranges from the
three-dimensional NDF called survey, whose third pixel axis has only
one element, to a two-dimensional NDF called virgo. Information on the
third WCS axis is removed too.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: SETBOUND; Figaro: ISUBSET.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 1998, 2000, 2003-2004 Central Laboratory of the Research
Councils. Copyright (C) 2005-2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2009, 2013 Science & Technology
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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~
If present, an NDF's TITLE, LABEL, UNITS, DATA, VARIANCE, QUALITY,
AXIS WCS and HISTORY components are copied by this routine, together
with all extensions. The output NDF's title may be modified, if
required, by specifying a new value via the TITLE parameter.


