

ASTSETACTUNIT
=============


Purpose
~~~~~~~
Set the ActiveUnit flag for a Frame


Description
~~~~~~~~~~~
This application sets the current value of the ActiveUnit flag for a
Frame, which controls how the Frame behaves when it is used (by
ASTFINDFRAME) as a template to match another (target) Frame, or is
used as the TO Frame by ASTCONVERT. It determines if the Mapping
between the template and target Frames should take differences in axis
units into account. The default value for simple Frames is FALSE,
which preserves the behaviour of versions of AST prior to version 2.0.
If the ActiveUnit flag of the template Frame is FALSE, then the
Mapping will ignore any difference in the Unit attributes of
corresponding template and target axes. In this mode, the Unit
attributes are purely descriptive commentary for the benefit of human
readers and do not influence the Mappings between Frames. This is the
behaviour which all Frames had in older version of AST, prior to the
introduction of this attribute.
If the ActiveUnit flag of the template Frame is .TRUE., then the
Mapping from template to target will take account of any difference in
the axis Unit attributes, where-ever possible. For instance, if
corresponding target and template axes have Unit strings of "km" and
"m", then the FrameSet class will use a ZoomMap to connect them which
introduces a scaling of 1000. If no Mapping can be found between the
corresponding units string, then an error is reported. In this mode,
it is assumed that values of the Unit attribute conform to the syntax
for units strings described in the FITS WCS Paper I "Representations
of world coordinates in FITS" (Greisen & Calabretta). Particularly,
any of the named unit symbols, functions, operators or standard
multiplier prefixes listed within that paper can be used within a
units string. A units string may contain symbols for unit which are
not listed in the FITS paper, but transformation to any other units
will then not be possible (except to units which depend only on the
same unknown units - thus "flops" can be transformed to "Mflops" even
though "flops" is not a standard FITS unit symbol).
If the ActiveUnit flag is .TRUE., setting a new Unit value for an axis
may also change its Label and Symbol attributes. For instance, if an
axis has Unit "Hz" and Label "frequency", then changing its Unit to
"log(Hz)" will change its Label to "log( frequency )". In addition,
the Axis Format attribute will be cleared when-ever a new value is
assigned to the Unit attribute.
Note, if a TRUE value is set for the ActiveUnit flag, then changing a
Unit value for the current Frame within a FrameSet will result in the
Frame being re-mapped (that is, the Mappings which define the
relationships between Frames within the FrameSet will be modified to
take into account the change in Units).


Usage
~~~~~


::

    
       astsetactunit this value result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



RESULT = LITERAL (Read)
```````````````````````
An NDF or text file to receive the modified Frame. If an NDF is
supplied, the WCS FrameSet within the NDF will be replaced by the new
Object if possible (i.e. if it is a FrameSet in which the base Frame
has Domain GRID and has 1 axis for each NDF dimension).



THIS = LITERAL (Read)
`````````````````````
An NDF or text file holding the original Frame. If an NDF is supplied,
the WCS FrameSet will be used.



VALUE = _LOGICAL (Read)
```````````````````````
The value to assign to the ActiveUnit flag.



Notes
~~~~~


+ This application corresponds to the AST routine AST_SETACTIVEUNIT.
  The name has been abbreviated due to a limitation on the length of
  ADAM command names.




Copyright
~~~~~~~~~
Copyright (C) 2003 Central Laboratory of the Research Councils. All
Rights Reserved.


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


