

DST2NDF
=======


Purpose
~~~~~~~
Converts a Figaro (Version 2) DST file to an NDF


Description
~~~~~~~~~~~
This application converts a Figaro Version-2 DST file to a Version-3
file, i.e. to an NDF. The rules for converting the various components
of a DST are listed in the notes. Since both are hierarchical formats
most files can be be converted with little or no information lost.


Usage
~~~~~


::

    
       dst2ndf in out [form]
       



ADAM parameters
~~~~~~~~~~~~~~~



FORM = LITERAL (Read)
`````````````````````
The storage form of the NDF's data and variance arrays. FORM =
"Simple" gives the simple form, where the array of data and variance
values is located in an ARRAY structure. Here it can have ancillary
data like the origin. This is the normal form for an NDF. FORM =
"Primitive" offers compatibility with earlier formats, such as IMAGE.
In the primitive form the data and variance arrays are primitive
components at the top level of the NDF structure, and hence it cannot
have ancillary information. ["Simple"]



IN = Figaro file (Read)
```````````````````````
The file name of the version 2 file. A file extension must not be
given after the name, since ".dst" is appended by the application. The
file name is limited to 80 characters.



OUT = NDF (Write)
`````````````````
The file name of the output NDF file. A file extension must not be
given after the name, since ".sdf" is appended by the application.
Since the NDF_ library is not used, a section definition may not be
given following the name. The file name is limited to 80 characters.



Examples
~~~~~~~~
dst2ndf old new
This converts the Figaro file old.dst to the NDF called new (in file
new.sdf). The NDF has the simple form.
dst2ndf horse horse p
This converts the Figaro file horse.dst to the NDF called horse (in
file HORSE.SDF). The NDF has the primitive form.



Notes
~~~~~
The rules for the conversion of the various components are as follows:
_________________________________________________________________
Figaro file NDF

+ ----------------------------------------------------------------
.Z.DATA -> .DATA_ARRAY.DATA (when FORM = "SIMPLE") .Z.DATA ->
.DATA_ARRAY (when FORM = "PRIMITIVE") .Z.ERRORS -> .VARIANCE.DATA
(after processing when FORM = "SIMPLE") .Z.ERRORS -> .VARIANCE (after
processing when FORM = "PRIMITIVE") .Z.QUALITY -> .QUALITY.QUALITY
(must be BYTE array) (see Bad-pixel handling below).
+ > .QUALITY.BADBITS = 255 .Z.LABEL -> .LABEL .Z.UNITS -> .UNITS
  .Z.IMAGINARY -> .DATA_ARRAY.IMAGINARY_DATA .Z.MAGFLAG ->
  .MORE.FIGARO.MAGFLAG .Z.RANGE -> .MORE.FIGARO.RANGE .Z.xxxx ->
  .MORE.FIGARO.Z.xxxx

.X.DATA -> .AXIS(1).DATA_ARRAY .X.ERRORS -> .AXIS(1).VARIANCE (after
processing) .X.WIDTH -> .AXIS(1).WIDTH .X.LABEL -> .AXIS(1).LABEL
.X.UNITS -> .AXIS(1).UNITS .X.LOG -> .AXIS(1).MORE.FIGARO.LOG .X.xxxx
-> .AXIS(1).MORE.FIGARO.xxxx (Similarly for .Y .T .U .V or .W
structures which are renamed to AXIS(2), ..., AXIS(6) in the NDF.)
.OBS.OBJECT -> .TITLE .OBS.SECZ -> .MORE.FIGARO.SECZ .OBS.TIME ->
.MORE.FIGARO.TIME .OBS.xxxx -> .MORE.FIGARO.OBS.xxxx
.FITS.xxxx -> .MORE.FITS(n) (into value part of the string)
.COMMENTS.xxxx -> .MORE.FITS(n) (into comment part of the string)
.FITS.xxxx.DATA -> .MORE.FITS(n) (into value part of the string)
.FITS.xxxx.DESCRIPTION -> .MORE.FITS(n) (into comment part of the
string) .FITS.xxxx.yyyy -> .MORE.FITS(n) (into blank-keyword comment
containing yyyy=value)
.MORE.xxxx -> .MORE.xxxx
.TABLE -> .MORE.FIGARO.TABLE .xxxx -> .MORE.FIGARO.xxxx


+ Axis arrays with dimensionality greater than one are not supported
  by the NDF. Therefore, if the application encounters such an axis
  array, it processes the array using the following rules, rather than
  those given above.

.X.DATA -> .AXIS(1).MORE.FIGARO.DATA_ARRAY (AXIS(1).DATA_ARRAY is
filled with pixel co-ordinates) .X.ERRORS ->
.AXIS(1).MORE.FIGARO.VARIANCE (after processing) .X.WIDTH ->
.AXIS(1).MORE.FIGARO.WIDTH


+ In addition to creating a blank-keyword NDF FITS-extension header
  for each component of a non-standard DST FITS structure
  (.FITS.xxxx.yyyy where yyyy is not DATA or DESCRIPTION), this set of
  related headers are bracketed by blank lines and a comment containing
  the name of the structure (i.e. xxxx).

Bad-pixel handling: The QUALITY array is only copied if the bad-pixel
flag (.Z.FLAGGED) is false or absent. A simple NDF with the bad-pixel
flag set to false (meaning that there are no bad-pixels present) is
created when .Z.FLAGGED is absent or false and FORM = "SIMPLE".


Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: NDF2DST.


Copyright
~~~~~~~~~
Copyright (C) 1989, 1992-1993 Science & Engineering Research Council.
Copyright (C) 1995-1996 Central Laboratory of the Research Councils.
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


+ The maximum number of dimensions is 6.




