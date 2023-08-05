

PASTE
=====


Purpose
~~~~~~~
Pastes a series of NDFs upon each other


Description
~~~~~~~~~~~
This application copies a series of NDFs, in the order supplied and
taking account of origin information, on to a `base' NDF to produce an
output NDF. The output NDF is therefore a copy of the base NDF
obscured wholly or partially by the other input NDFs. This operation
is analogous to pasting in publishing. It is intended for image
editing and the creation of insets.
The dimensions of the NDFs may be different, and indeed so may their
dimensionalities. The output NDF can be constrained to have the
dimensions of the base NDF, so the pasted NDFs are clipped. Normally,
the output NDF will have dimensions such that all the input NDFs are
accommodated in full.
Bad values in the pasted NDFs are by default transparent, so the
underlying data are not replaced during the copying.
Input NDFs can be shifted in pixel space before pasting them into the
output NDF (see Parameter SHIFT).


Usage
~~~~~


::

    
       paste in p1 [p2] ... [p25] out=?
       



ADAM parameters
~~~~~~~~~~~~~~~



CONFINE = _LOGICAL (Read)
`````````````````````````
This parameter controls the dimensions of the output NDF. If CONFINE
is FALSE the output NDF just accommodates all the input NDFs. If
CONFINE is TRUE, the output NDF's dimensions matches those of the base
NDF. [FALSE]



IN = NDF (Read)
```````````````
This parameter is either: a) the base NDF on to which the other input
NDFs supplied via parameters P1 to P25 will be pasted; or b) a group
of input NDFs (of any dimensionality) comprising all the input NDFs,
of which the first is deemed to be the base NDF, and the remainder are
to be pasted in the order supplied.
The group should be given as a comma-separated list, in which each
list element can be:


+ an NDF name, optionally containing wild-cards and/or regular
expressions ("*", "?", "[a-z]" etc.).
+ the name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  wild-cards, etc.), or another file specification (preceded by an up-
  arrow). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a hyphen "-", then
you are re-prompted for further input until a value is given which
does not end with a hyphen. All the NDFs given in this way are
concatenated into a single group.
The group can contain no more than 1000 names.



OUT = NDF (Write)
`````````````````
The NDF resulting from pasting of the input NDFs onto the base NDF.
Its dimensions may be different from the base NDF. See parameter
CONFINE.



P1-P25 = NDF (Read)
```````````````````
The NDFs to be pasted on to the base NDF. The NDFs are pasted in the
order P1, P2, ... P25. There can be no missing NDFs, e.g. in order for
P3 to be processed there must be a P2 given as well. A null value (!)
indicates that there is no NDF. NDFs P2 to P25 are defaulted to !. At
least one NDF must be pasted, therefore P1 may not be null.
P1 to P25 are ignored if the group specified through parameter IN
comprises more than one NDF.



SHIFT( * ) = _INTEGER (Read)
````````````````````````````
An incremental shift to apply to the pixel origin of each input NDF
before pasting it into the output NDF. If supplied, this parameter
allows a set of NDFs with the same pixel bounds to be placed "side-by-
side" in the output NDF. For instance, this allows a set of images to
be pasted into a cube. The first input NDF is not shifted. The pixel
origin of the second NDF is shifted by the number of pixels given in
SHIFT. The pixel origin of the third NDF is shifted by twice the
number of pixels given in SHIFT. Each subsequent input NDF is shifted
by a further multiple of SHIFT. If null (!) is supplied, no shifts are
applied. [!]



TITLE = LITERAL (Read)
``````````````````````
Title for the output NDF structure. A null value (!) propagates the
title from the base NDF to the output NDF. [!]



TRANSP = _LOGICAL (Read)
````````````````````````
If TRANSP is TRUE, bad values within the pasted NDFs are not copied to
the output NDF as if the bad values were transparent. If TRANSP is
FALSE, all values are copied during the paste and a bad value will
obscure an underlying value. [TRUE]



Examples
~~~~~~~~
paste aa inset out=bb
This pastes the NDF called inset on to the arrays in the NDF called aa
to produce the NDF bb. Bad values are transparent. The bounds and
dimensionality of bb may be larger than those of aa.
paste aa inset out=bb notransp
As above except that bad values are copied from the NDF inset to NDF
bb.
paste aa inset out=bb confine
As the first example except that the bounds of NDF bb match those of
NDF aa.
paste in="aa,inset" out=bb
The same as the first example.
paste in="aa,inset,inset2,inset3" out=bb
Similar to first example, but now two further NDFs inset2 and inset3
are also pasted.
paste ccd fudge inset out=ccdc
This pastes the NDF called fudge, followed by NDF inset on to the
arrays in the NDF called ccd to produce the NDF ccdc. Bad values are
transparent. The bounds and dimensionality of ccd may be larger than
those of ccdc.
paste in="canvas,^shapes.lis" out=collage confine
This pastes the NDFs listed in the text file shapes.lis in the order
given on the NDF called canvas. Bad values are transparent. The bounds
of NDF collage match those of NDF canvas.
paste in=^planes out=cube shift=[0,0,1]
Assuming the text file planes contains a list of two-dimensional NDFs,
this arranges them into a cube, one behind the other.



Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1998, 2004 Central Laboratory of the Research Councils. Copyright
(C) 2005 Particle Physics & Astronomy Research Council. Copyright (C)
2012 Science & Technology Facilities Council. All Rights Reserved.


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
LABEL, TITLE, UNITS, WCS and HISTORY, components of an NDF data
structure and propagates all extensions. Propagation is from the base
NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




