

SETVAR
======


Purpose
~~~~~~~
Set new values for the VARIANCE component of an NDF data structure


Description
~~~~~~~~~~~
This routine sets new values for the VARIANCE component of an NDF data
structure. The new values can be copied from a specified component of
a second NDF or can be generated from the supplied NDF's data array by
means of a Fortran-like arithmetic expression. Any previous variance
information is over-written with the new values. Alternatively, if a
`null' value (!) is given for the variance, then any pre-existing
variance information is erased.


Usage
~~~~~


::

    
       ndf variance
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The name of an NDF array component within the NDF specified by
parameter FROM. The values in this array component are used as the new
variance values to be stored in the VARIANCE component of the NDF
specified by parameter NDF. The supplied value must be one of "Data"
or "Variance". ["Data"]



FROM = NDF (Read)
`````````````````
An NDF data structure containing the values to be used as the new
variance values. The NDF component from which to read the new variance
values is specified by parameter COMP. If NDF is not contained
completely within FROM, then the VARIANCE component of NDF will be
padded with bad values. If a null (!) value is supplied, the new
variance values are determined by the expression given for parameter
VARIANCE. [!]



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure whose variance values are to be modified.



VARIANCE = LITERAL (Read)
`````````````````````````
A Fortran-like arithmetic expression giving the variance value to be
assigned to each pixel in terms of the variable DATA, which represents
the value of the corresponding data array pixel. For example,
VARIANCE="DATA" implies normal `root N' error estimates, whereas
VARIANCE="DATA + 50.7" might be used if a sky background of 50.7 units
had previously been subtracted.
If a `null' value (!) is given for this parameter, then no new
VARIANCE component will be created and any pre-existing variance
values will be erased.



Examples
~~~~~~~~
setvar ngc4709 data
This sets the VARIANCE component within the NDF structure ngc4709 to
equal its corresponding data-array component.
setvar ngc4709 from=noise comp=data
This sets the VARIANCE component within the NDF structure ngc4709 to
equal the values in the Data array of the NDF structure noise.
setvar ndf=arcspec "data - 0.31"
This sets the VARIANCE component within the NDF structure arcspec to
be its corresponding data-array component less a constant 0.31.
setvar cube4 variance=!
This erases the values of the VARIANCE component within the NDF
structure cube4, if it exists.



Notes
~~~~~


+ All of the standard Fortran 77 intrinsic functions are available for
use in the variance expression, plus a few others (see SUN/61 for
details and an up-to-date list).
+ Calculations are performed using real arithmetic (or double
precision if appropriate) and are constrained to be non-negative.
+ The data type of the VARIANCE component is set to match that of the
  DATA component.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ERRCLIP; Figaro: GOODVAR.


Copyright
~~~~~~~~~
Copyright (C) 1989-1990, 1992 Science & Engineering Research Council.
Copyright (C) 1995, 2004 Central Laboratory of the Research Councils.
All Rights Reserved.


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


