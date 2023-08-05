

MANIC
=====


Purpose
~~~~~~~
Change the dimensionality of all or part of an NDF


Description
~~~~~~~~~~~
This application manipulates the dimensionality of an NDF. The input
NDF can be projected on to any N-dimensional surface (line, plane,
etc.) by averaging the pixels in perpendicular directions, or grown
into new dimensions by duplicating an existing N-dimensional surface.
The order of the axes can also be changed at the same time. Any
combination of these operations is also possible.
The shape of the output NDF is specified using parameter AXES. This is
a list of integers, each element of which identifies the source of the
corresponding axis of the output---either the index of one ofthe pixel
axes of the input, or a zero indicating that the input should be
expanded with copies of itself along that axis. If any axis of the
input NDF is not referenced in the AXES list, the missing dimensions
will be collapsed to form the resulting data. Dimensions are collapsed
by averaging all the non-bad pixels along the relevant pixel axis (or
axes).


Usage
~~~~~


::

    
       manic in out axes
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES( ) = _INTEGER (Read)
`````````````````````````
An array of integers which define the pixel axes of the output NDF.
The array should contain one value for each pixel axis in the output
NDF. Each value can be either a positive integer or zero. If positive,
it is taken to be the index of a pixel axis within the input NDF which
is to be used as the output axis. If zero, the output axis will be
formed by replicating the entire output NDF a specified number of
times (see parameters LBOUND and UBOUND). At least one non-zero value
must appear in the list, and no input axis may be used more than once.



IN = NDF (Read)
```````````````
The input NDF.



LBOUND( ) = _INTEGER (Read)
```````````````````````````
An array holding the lower pixel bounds of any new axes in the output
NDF (that is, output axes which have a zero value in the corresponding
element of the AXES parameter). One element must be given for each
zero-valued element within AXES, in order of appearance within AXES.
The dynamic default is to use 1 for every element. []



OUT = NDF (Write)
`````````````````
The output NDF.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF. A null (!) means use the title from the
input NDF. [!]



UBOUND( ) = _INTEGER (Read)
```````````````````````````
An array holding the upper pixel bounds of any new axes in the output
NDF (that is, output axes which have a zero value in the corresponding
element of the AXES parameter). One element must be given for each
zero-valued element within AXES, in order of appearance within AXES.
The dynamic default is to use 1 for every element. []



Examples
~~~~~~~~
manic image transim [2,1]
This transposes the two-dimensional NDF image so that its X pixel co-
ordinates are in the Y direction and vice versa. The ordering of the
axes within the current WCS Frame will only be changed if the Domain
of the current Frame is PIXEL or AXES. For instance, if the current
Frame has Domain "SKY", with axis 1 being RA and axis 2 being DEC,
then these will be unchanged in the output NDF. However, the Mapping
which is used to relate (RA,DEC) positions to pixel positions will be
modified to take the permutation of the pixel axes into account.
manic cube summ 3
This creates a one-dimensional output NDF called summ, in which the
single pixel axis corresponds to the Z (third) axis in an input NDF
called (cube). Each element in the output is equal to the average data
value in the corresponding XY plane of the input.
manic line plane [0,1] lbound=1 ubound=25
This takes a one-dimensional NDF called line and expands it into a
two-dimensional NDF called plane. The second pixel axis of the output
NDF corresponds to the first (and only) pixel axis in the input NDF.
The first pixel axes of the output is formed by replicating the the
input NDF 25 times.
manic line plane [1,0] lbound=1 ubound=25
This does the same as the last example except that the output NDF is
transposed. That is, the input NDF is copied into the output NDF so
that it is parallel to pixel axis 1 (X) in the output NDF, instead of
pixel axis 2 (Y) as before.
manic cube hyper [1,0,0,0,0,0,3] ubound=[2,4,2,2,1] accept
This manic example projects the second dimension of an input three-
dimensional NDF on to the plane formed by its first and third
dimensions by averaging, and grows the resulting plane up through five
new dimensions with a variety of extents.



Notes
~~~~~


+ This application permutes the NDF pixel axes, and any associated
  AXIS structures. It does not change the axes of the current WCS co-
  ordinate Frame, either by permuting, adding or deleting, unless that
  frame has Domain "PIXEL" or "AXES". See the first example in the
  "Examples" section.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: COLLAPSE, PERMAXES.


Copyright
~~~~~~~~~
Copyright (C) 2001-2002, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2012 Science & Technology Facilities Council.
All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, VARIANCE, LABEL,
TITLE, UNITS, WCS, and HISTORY components of the input NDF and
propagates all extensions. QUALITY is also propagated if possible
(i.e. if no axes are collapsed).
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported, up to a maximum of 7.




