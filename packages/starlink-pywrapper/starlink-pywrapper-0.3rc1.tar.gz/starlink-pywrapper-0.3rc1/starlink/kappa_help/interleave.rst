

INTERLEAVE
==========


Purpose
~~~~~~~
Forms a higher-resolution NDF by interleaving a set of NDFs


Description
~~~~~~~~~~~
This routine performs interleaving, also known as interlacing, in
order to restore resolution where the pixel dimension undersamples
data. Resolution may be improved by integer factors along one or more
dimensions. For an N-fold increase in resolution along a dimension,
INTERLEAVE demands N NDF structures that are displaced from each other
by i/N pixels, where i is an integer from 1 to N-1. It creates an NDF
whose dimensions are enlarged by N along that dimension.
The supplied NDFs should have the same dimensionality.


Usage
~~~~~


::

    
       interleave in out expand
       



ADAM parameters
~~~~~~~~~~~~~~~



EXPAND() = _INTEGER (Read)
``````````````````````````
Linear expansion factors to be used to create the new data array. The
number of factors should equal the number of dimensions in the input
NDF. If fewer are supplied the last value in the list of expansion
factors is given to the remaining dimensions. Thus if a uniform
expansion is required in all dimensions, just one value need be
entered. If the net expansion is one, an error results. The suggested
default is the current value.



FILL = LITERAL (Read)
`````````````````````
Specifies the value to use where the interleaving does not fill the
array, say because the shapes of the input NDFs are not the same, or
have additional shifts of origin. Allowed values are "Bad" or "Zero".
["Bad"]



IN = NDF (Read)
```````````````
A group of input NDFs to be interweaved. They may have different
shapes, but must all have the same number of dimensions. This should
be given as a comma-separated list, in which each list element can be:


+ an NDF name, optionally containing wild-cards and/or regular
expressions ("*", "?", "[a-z]" etc.).
+ the name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  wild-cards, etc.), or another file specification (preceded by a
  caret). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a hyphen "-", then
you are re-prompted for further input until a value is given which
does not end with a hyphen. All the datasets given in this way are
concatenated into a single group.



OUT = NDF (Write)
`````````````````
Output NDF structure.



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the input NDF to the output NDF. [!]



TRIM = _LOGICAL (Read)
``````````````````````
This parameter controls the shape of the output NDF before the
application of the expansion. If TRIM=TRUE, then the output NDF
reflects the shape of the intersection of all the input NDFs, i.e.
only pixels which appear in all the input arrays will be represented
in the output. If TRIM=FALSE, the output reflects shape of the union
of the inputs, i.e. every pixel which appears in the input arrays will
be represented in the output. [TRUE]



Examples
~~~~~~~~
interleave "vector1,vector2" weave 2
This interleaves the 1one-dimensional NDFs called vector1 and vector2
and stores the result in NDF weave. Only the intersection of the two
input NDFs is used.
interleave 'image*' weave [3,2] title="Interlaced image"
This interleaves the two-dimensional NDFs with names beginning with
"image" into an NDF called weave. The interleaving has three datasets
along the first dimension and two along the second. Therefore there
should be six input NDFs. The output NDF has title "Interlaced image".
interleave in='image*' out=weave expand=[3,2] notrim
As above except the title is not set and the union of the bounds of
the input NDFs is expanded to form the shape of the weave NDF.
interleave ^frames.lis finer 2
This interleaves the NDFs listed in the text file frames.lis to form
an enlarged NDF called finer. The interleaving is twofold along each
axis of those NDFs.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PIXDUPE; CCDPACK: DRIZZLE.


Copyright
~~~~~~~~~
Copyright (C) 2005-2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2010, 2012 Science & Technology Facilities Council. All
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


+ This routine processes the AXIS, DATA, QUALITY, and VARIANCE from
the all input NDF data structures. It also processes the WCS, LABEL,
TITLE, UNITS, and HISTORY components of the primary NDF data
structure, and propagates all of its extensions.
+ The AXIS centre values along each axis are formed by interleaving
the corresponding centres from the first NDF, and linearly
interpolating between those to complete the array.
+ The AXIS width and variance values in the output are formed by
interleaving the corresponding input AXIS values. Each array element
is assigned from the first applicable NDF. For example, for a two-
dimensional array with expansion factors of 2 and 3 respectively, the
first two NDFs would be used to define the array elements for the
first axis. The second axis's elements come from the first, third, and
fifth NDFs.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




