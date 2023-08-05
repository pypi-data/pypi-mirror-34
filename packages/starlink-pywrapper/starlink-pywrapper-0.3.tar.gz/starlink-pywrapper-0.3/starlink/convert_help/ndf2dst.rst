

NDF2DST
=======


Purpose
~~~~~~~
Converts an NDF to a Figaro (Version 2) DST file


Description
~~~~~~~~~~~
This application converts an NDF to a Figaro (Version 2) `DST' file.
The rules for converting the various components of a DST are listed in
the Notes. Since both are hierarchical formats most files can be be
converted with little or no information lost.


Usage
~~~~~


::

    
       ndf2dst in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input NDF data structure. The suggested default is the current NDF if
one exists, otherwise it is the current value.



OUT = Figaro (Write)
````````````````````
Output Figaro file name. This excludes the file extension. The file
created will be given extension ".dst".



Examples
~~~~~~~~
ndf2dst old new
This converts the NDF called old (in file old.sdf) to the Figaro file
new.dst.
ndf2dst spectre spectre
This converts the NDF called spectre (in file spectre.sdf) to the
Figaro file spectre.dst.



Notes
~~~~~
The rules for the conversion are as follows:
_________________________________________________________________ NDF
Figaro file

+ ----------------------------------------------------------------
  Main data array -> .Z.DATA Imaginary array -> .Z.IMAGINARY Bad-pixel
  flag -> .Z.FLAGGED Units -> .Z.UNITS Label -> .Z.LABEL Variance ->
  .Z.ERRORS (after processing) Quality -> It is not copied directly
  though bad values indicated by QUALITY flags will be flagged in
  .Z.DATA in addition to any flagged values actually in the input main
  data array. .Z.FLAGGED is set accordingly. Title -> .OBS.OBJECT

AXIS(1) structure -> .X AXIS(1) Data -> .X.DATA (unless there is a
DATA_ARRAY component of AXIS(1).MORE.FIGARO to allow for a
non-1-dimensional array) AXIS(1) Variance -> .X.VARIANCE (unless there
is a VARIANCE component of AXIS(1).MORE.FIGARO to allow for a
non-1-dimensional array) AXIS(1) Width -> .X.WIDTH (unless there is a
WIDTH component of AXIS(1).MORE.FIGARO to allow for a
non-1-dimensional array) AXIS(1) Units -> .X.UNITS AXIS(1) Label ->
.X.LABEL AXIS(1).MORE.FIGARO.xxx -> .X.xxx (Similarly for AXIS(2),
..., AXIS(6) which are renamed to .Y .T .U .V or .W)
FIGARO extension: .MORE.FIGARO.MAGFLAG -> .Z.MAGFLAG
.MORE.FIGARO.RANGE -> .Z.RANGE .MORE.FIGARO.SECZ -> .OBS.SECZ
.MORE.FIGARO.TIME -> .OBS.TIME .MORE.FIGARO.xxx -> .xxx (recursively)
FITS extension: .MORE.FITS Items -> .FITS.xxx Comments ->
.COMMENTS.xxx
Other extensions: .MORE.other -> .MORE.other


Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: DST2NDF.


Copyright
~~~~~~~~~
Copyright (C) 1991-1992 Science & Engineering Research Council.
Copyright (C) 1995-1997, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2009 Science & Technology Facilities Council.
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


