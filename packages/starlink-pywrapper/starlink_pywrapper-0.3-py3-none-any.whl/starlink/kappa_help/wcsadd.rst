

WCSADD
======


Purpose
~~~~~~~
Creates a Mapping and optionally adds a new co-ordinate Frame into the
WCS component of an NDF


Description
~~~~~~~~~~~
This application can be used to create a new AST Mapping and
optionally use the Mapping to add a new co-ordinate Frame into the WCS
component of an NDF (see parameter NDF). An output text file may also
be created holding a textual representation of the Mapping for future
use by other applications such as REGRID (see parameter MAPOUT). A
number of different types of Mapping can be used (see parameter
MAPTYPE).
When adding a new Frame to a WCS component, the Mapping is used to
connect the new Frame to an existing one (called the "basis" Frame:
see parameter FRAME). The specific type of Frame to add is specified
using parameter FRMTYPE (the default is to simply copy the basis
Frame). Optionally (see parameter TRANSFER), attributes which have
been assigned an explicit value in the basis Frame are transferred to
the new Frame (but only if they are relevant to the type of the new
Frame). The value of the Domain attribute for the new Frame can be
specified using parameter DOMAIN. Other attribute values for the new
Frame may be specified using parameters ATTRS. The new Frame becomes
the current co-ordinate Frame in the NDF (unless parameter RETAIN is
set TRUE).
WCSADD will only generate Mappings with the same number of input and
output axes; this number is determined by the number of axes in the
basis Frame if an NDF is supplied, or by the NAXES parameter
otherwise.


Usage
~~~~~


::

    
       wcsadd ndf frame domain maptype
       



ADAM parameters
~~~~~~~~~~~~~~~



ATTRS = GROUP (Read)
````````````````````
A group of attribute settings to be applied to the new Frame before
adding it into the NDF.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings over-riding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of an attribute appropriate to the type of
Frame specified by parameter FRMTYPE (see SUN/210 for a complete
description of all attributes), and <value> is the value to assign to
the attribute. Default values will be used for any unspecified
attributes---these defaults are inherited from the basis Frame. Any
unrecognised attributes are ignored (no error is reported).



CENTRE( 2 ) = _DOUBLE (Read)
````````````````````````````
The co-ordinates of the centre of a pincushion distortion. It is only
used when MAPTYPE="PINCUSHION". See also DISCO. [0,0]



DIAG( ) = _DOUBLE (Read)
````````````````````````
The elements along the diagonal of the linear transformation matrix.
There will be as many of these as there are axes in the basis Frame.
Each effectively gives the factor by which co-ordinates on the
corresponding axis should be multiplied. This parameter is only used
when MAPTYPE="DIAG".



DISCO = _DOUBLE (Read)
``````````````````````
The distortion coefficient of a pincushion distortion. Used in
conjunction with the CENTRE parameter, this defines the forward
transformation to be used as follows:
XX = X + D * (X - C1) * ( (X - C1)**2 + (Y - C2)**2 )
YY = Y + D * (Y - C2) * ( (X - C1)**2 + (Y - C2)**2 )
where (X,Y) are the input co-ordinates, (XX,YY) the output co-
ordinates, D is DISCO, and C1 and C2 are the two elements of CENTRE.
DISCO is only used when MAPTYPE=PINCUSHION.



DOMAIN = LITERAL (Read)
```````````````````````
The value for the Domain attribute for the new Frame. Care should be
taken to ensure that domain names are used consistently. This will
usually mean avoiding any domain names that are already in use within
the WCS component, particularly the standard domain names such as
GRID, FRACTION, PIXEL, AXIS, and GRAPHICS. The supplied value is
stripped of spaces, and converted to upper case before being used.
Note, if parameter MAPTYPE is set to "REFNDF", then the value supplied
for parameter "DOMAIN" indicates the Domain of the Frame within the
reference NDF that is to be copied (see parameter REFNDF).



EPOCH = _DOUBLE (Read)
``````````````````````
If the basis Frame is specified using a "Sky Co-ordinate System"
specification for a celestial co-ordinate system (see parameter
FRAME), then an epoch value is needed to qualify it. This is the epoch
at which the supplied sky positions were determined. It should be
given as a decimal-years value, with or without decimal places
("1996.8" for example). Such values are interpreted as a Besselian
epoch if less than 1984.0 and as a Julian epoch otherwise. The
suggested default is the value stored in the basis Frame.



FOREXP = LITERAL (Read)
```````````````````````
A group of expressions to be used for the forward co-ordinate
transformations in a MathMap. There must be at least as many
expressions as the number of axes of the Mapping, but there may be
more if intermediate expressions are to be used. The expressions may
be given directly in response to the prompt, or read from a text file,
in which case the name of the file should be given, preceded by a "^"
character. Individual expression should be separated by commas or, if
they are supplied in a file, new-lines (see SUN/95 section "Specifying
Groups of Objects" which is within the section "Parameters"). The
syntax for each expression is Fortran-like; see the "Examples" section
below, and the Appendix entitled "Using MathMaps" in SUN/95 for
details. FOREXP is only used when MAPTYPE="MATH".



FRAME = LITERAL (Read)
``````````````````````
A string specifying the basis Frame. If a null value is supplied the
current co-ordinate Frame in the NDF is used. The string can be one of
the following:


+ A domain name such as SKY, AXIS, PIXEL, etc. The two "pseudo-
domains" WORLD and DATA may be supplied and will be translated into
PIXEL and AXIS respectively, so long as the WCS component of the NDF
does not contain Frames with these domains.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95).





FRMTYPE = LITERAL (Read)
````````````````````````
The type of Frame to add to the NDF. If a null (!) value is supplied,
a copy of the basis Frame is used (as modified by parameters ATTRS and
DOMAIN). The allows values are:


+ FRAME -- A simple Cartesian Frame (the number of axes is equal to
the number of outputs from the Mapping)
+ SKYFRAME -- A two-dimensional Frame representing positions on the
celestial sphere.
+ SPECFRAME -- A one-dimensional Frame representing positions within
an electromagnetic spectrum.
+ TIMEFRAME -- A one-dimensional Frame representing moments in time.

Note, if parameter MAPTYPE is set to "REFNDF", then parameter
"FRMTYPE" will not be used - the Frame used will instead always be a
copy of the Frame from the reference NDF (as selected by parameter
DOMAIN). [!]



INVEXP = LITERAL (Read)
```````````````````````
The expressions to be used for the inverse co-ordinate transformations
in a MathMap. See FOREXP. INVEXP is only used when MAPTYPE="MATH".



MAPIN = FILENAME (Read)
```````````````````````
The name of a file containing an AST Mapping with which to connect the
basis Frame to the new one. The file may be a text file which contains
the textual representation of an AST Mapping, or a FITS file which
contains the Mapping as an AST object encoded in its headers, or an
NDF. If it is an NDF, the Mapping from its base (GRID-domain) to
current Frame will be used. Only used when MAPTYPE="FILE".



MAPOUT = FILENAME (Write)
`````````````````````````
The name of a text file in which to store a textual representation of
the Mapping. This can be used, for instance, by the REGRID
application. If a null (!) value is supplied, no file is created. [!]



MAPTYPE = LITERAL (Read)
````````````````````````
The type of Mapping to be used to connect the new Frame to the basis
Frame. It must be one of the following strings, each of which require
some additional parameters as indicated:


+ DIAGONAL -- A linear mapping with no translation of off-diagonal
coefficients (see parameter DIAG)
+ FILE -- A mapping defined by an AST Mapping supplied in a separate
file (see parameter MAPIN)
+ LINEAR -- A general linear mapping (see parameter TR)
+ MATH -- A general algebraically defined mapping (see parameters
FOREXP, INVEXP, SIMPFI, SIMPIF)
+ PINCUSHION -- A pincushion/barrel distortion (see parameters DISCO
and CENTRE)
+ REFNDF -- The Mapping is obtained by aligning the NDF with a second
reference NDF (see parameters REFNDF)
+ SHIFT -- A translation (see parameter SHIFT)
+ UNIT -- A unit mapping
+ ZOOM -- A uniform expansion/contraction (see parameter ZOOM)

["LINEAR"]



NAXES = _INTEGER (Read)
```````````````````````
The number of input and output axes which the Mapping will have. Only
used if a null value is supplied for parameter NDF.



NDF = NDF (Read and Write)
``````````````````````````
The NDF in which to store a new co-ordinate Frame. Supply a null (!)
value if you do not wish to add a Frame to an NDF (you can still use
the MAPOUT parameter to write the Mapping to a text file).



REFNDF = NDF (Read)
```````````````````
A reference NDF from which to obtain the Mapping and Frame. The NDFs
specified by parameters NDF and REFNDF are aligned in a suitable
coordinate system (usually their current Frames - an error is reported
if the two NDFs cannot be aligned). The Mapping from the basis Frame
in "NDF" (specified by parameter FRAME) to the required Frame in
"REFNDF" (specified by parameter DOMAIN) is then found and used. The
Frame added into "NDF" is always a copy of the reference Frame -
regardless of the setting of parameter FRMTYPE. Parameter REFNDF is
only used when parameter MAPTYPE is set to "REFNDF", in which case a
value must also be supplied for parameter NDF (an error will be
reported otherwise).



RETAIN = _LOGICAL (Read)
````````````````````````
Indicates whether the original current Frame should be retained within
the WCS FrameSet of the modified NDF (see parameter NDF). If FALSE,
the newly added Frame is the current Frame on exit. Otherwise, the
original current Frame is retained on exit. [FALSE]



SHIFT( ) = _DOUBLE (Read)
`````````````````````````
A vector giving the displacement represented by the translation. There
must be one element for each axis. SHIFT is only used when
MAPTYPE="SHIFT".



SIMPFI = _LOGICAL (Read)
````````````````````````
The value of the Mapping's SimpFI attribute (whether it is legitimate
to simplify the forward followed by the inverse transformation to a
unit transformation). This parameter is only used when MAPTYPE="MATH".
[TRUE]



SIMPIF = _LOGICAL (Read)
````````````````````````
The value of the Mapping's SimpIF attribute (whether it is legitimate
to simplify the inverse followed by the forward transformation to a
unit transformation). This parameter is only used when MAPTYPE="MATH".
[TRUE]



TR( ) = _DOUBLE (Read)
``````````````````````
The values of this parameter are the coefficients of a linear
transformation from the basis Frame specified by parameter FRAME to
the new Frame. This parameter is only used when MAPTYPE="LINEAR". For
instance, if a feature has co-ordinates (X,Y,Z,...) in the basis
Frame, and co-ordinates (U,V,W,...) in the new Frame, then the
following transformations would be used, depending on how many axes
the two Frames have:


+ one-dimensional:

U = TR(1) + TR(2)*X


+ two-dimensional:

U = TR(1) + TR(2)*X + TR(3)*Y
V = TR(4) + TR(5)*X + TR(6)*Y


+ three-dimensional:

U = TR(1) + TR(2)*X + TR(3)*Y + TR(4)*Z
V = TR(5) + TR(6)*X + TR(7)*Y + TR(8)*Z
W = TR(9) + TR(10)*X + TR(11)*Y + TR(12)*Z
The correct number of values must be supplied (that is, N*(N+1) where
N is the number of axes in the new and old Frames). If a null value
(!) is given it is assumed that the new Frame and the basis Frame are
connected using a unit mapping (i.e. corresponding axis values are
identical in the two Frames). This parameter is only used when
MAPTYPE="LINEAR". [!]



TRANSFER = _LOGICAL (Read)
``````````````````````````
If TRUE, attributes which have explicitly set values in the basis
Frame (specified by parameter FRAME) are transferred to the new Frame
(Specified by parameter FRMTYPE), if they are applicable to the new
Frame. If FALSE, no attribute values are transferred. The dynamic
default is TRUE if and only if the two Frames are of the same class
and have the same value for their Domain attributes. []



ZOOM = _DOUBLE (Read)
`````````````````````
The scaling factor for a ZoomMap; every coordinate will be multiplied
by this factor in the forward transformation. ZOOM is only used when
MAPTYPE="ZOOM".



Examples
~~~~~~~~
wcsadd speca axis frmtype=specframe maptype=unit \
attrs="'system=wave,unit=Angstrom'" This example assumes the NDF
"speca" has an Axis structure describing wavelength in Angstroms. It
adds a corresponding SpecFrame into the WCS component of the NDF. The
SpecFrame is connected to the Frame describing the NDF Axis structure
using a unit Mapping. Subsequently, WCSATTRIB can be used to modify
the SpecFrame so that it describes the spectral axis value in some
other system (frequency, velocities of various forms, energy, wave
number, etc).
wcsadd ngc5128 pixel old_pixel unit
This adds a new co-ordinate Frame into the WCS component of the NDF
called ngc5128. The new Frame is given the domain OLD_PIXEL and is a
copy of the existing PIXEL Frame. This OLD_PIXEL Frame will be
retained through further processing and can be used as a record of the
original pixel co-ordinate Frame.
wcsadd my_data dist-lum dist(au)-lum linear tr=[0,2.0628E5,0,0,0,1]
This adds a new co-ordinate Frame into the WCS component of the NDF
called my_data. The new Frame is given the domain DIST(AU)-LUM and is
a copy of an existing Frame with domain DIST-LUM. The first axis in
the new Frame is derived from the first axis in the basis Frame but is
in different units (AU instead of parsecs). This change of units is
achieved by multiplying the old Frame axis 1 values by 2.0628E5. The
values on the second axis are copied without change. You could then
use application WCSATTRIB to set the "Unit" attribute for axis 1 of
the new Frame to "AU".
wcsadd my_data dist-lum dist(au)-lum diag diag=[2.0628E5,1]
This does exactly the same as the previous example.
wcsadd ax322 ! shrunk zoom zoom=0.25 mapout=zoom.ast
This adds a new Frame to the WCS component of ax322 which is a one-
quarter-scale copy of its current co-ordinate Frame. The Mapping is
also stored in the text file "zoom.ast".
wcsadd cube grid slid shift shift=[0,0,1024]
This adds a new Frame to the WCS component of the NDF cube which
matches the GRID-domain co-ordinates in the first two axes, but is
translated by 1024 pixels on the third axis.
wcsadd plane pixel polar math simpif simpfi
forexp="'r=sqrt(x*x+y*y),theta=atan2(y,x)'"
invexp="'x=r*cos(theta),y=r*sin(theta)'" A new Frame is added which
gives pixel positions in polar co-ordinates. Fortran-like expressions
are supplied which define both the forward and inverse transformations
of the Mapping. The symbols "x" and "y" are used to represent the two
input Cartesian pixel co-ordinate axes, and the symbols "r" and
"theta" are used to represent the output polar co-ordinates. Note, the
single quotes are needed when running from the Unix shell in order to
prevent the shell interpreting the parentheses and commas within the
expressions.
wcsadd plane pixel polar math simpif simpfi forexp=^ft invexp=^it
As above, but the expressions defining the transformations are
supplied in two text files called "ft" and "it", instead of being
supplied directly. Each file could contain the two expression on two
separate lines.
wcsadd ndf=! naxes=2 mapout=pcd.ast maptype=pincushion
disco=5.3e-10 This constructs a pincushion-type distortion Mapping
centred on the origin with a distortion coefficient of 5.3e-10, and
writes out the Mapping as a text file called pcd.ast. This file could
then be used by REGRID to resample the pixels of an NDF according to
this transformation. No NDF is accessed.
wcsadd qmosaic frame=grid domain=polanal maptype=refndf refndf=imosaic
This adds a new co-ordinate Frame into the WCS component of the NDF
called qmosaic. The new Frame has domain "POLANAL" and is copied from
the NDF called imosaic (an error is reported if there is no such Frame
with imosaic). The new co-ordinate Frame is attached to the base Frame
(i.e. GRID co-ordinates) within qmosaic using a Mapping that produces
alignment between qmosaic and imosaic.



Notes
~~~~~


+ The new Frame has the same number of axes as the basis Frame.
+ An error is reported if the transformation supplied using parameter
  TR is singular.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFTRACE, REGRID, WCSFRAME, WCSREMOVE, WCSATTRIB; CCDPACK:
WCSEDIT.


Copyright
~~~~~~~~~
Copyright (C) 1998-1999, 2001-2003 Central Laboratory of the Research
Councils. Copyright (C) 2005-2006 Particle Physics & Astronomy
Research Council. All Rights Reserved.


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


