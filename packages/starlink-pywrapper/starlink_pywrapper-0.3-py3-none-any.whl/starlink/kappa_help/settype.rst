

SETTYPE
=======


Purpose
~~~~~~~
Sets a new numeric type for the data and variance components of an NDF


Description
~~~~~~~~~~~
This application allows the numeric type of the data and variance
components of an NDF to be changed. The NDF is accessed in update mode
and the values stored in these components are converted in situ to the
new type. No other attributes of the NDF are changed.


Usage
~~~~~


::

    
       settype ndf type
       



ADAM parameters
~~~~~~~~~~~~~~~



COMPLEX = _LOGICAL (Read)
`````````````````````````
If a TRUE value is given for this parameter, then the NDF's array
components will be altered so that they hold complex values, an
imaginary part containing zeros being created if necessary. If a FALSE
value is given, then the components will be altered so that they hold
non-complex values, any imaginary part being deleted if necessary. If
a null (!) value is supplied, the value used is chosen so that no
change is made to the current state. [!]



DATA = _LOGICAL (Read)
``````````````````````
If a TRUE value is given for this parameter, then the numeric type of
the NDF's data array will be changed. Otherwise, this component's type
will remain unchanged. [TRUE]



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure whose array components are to have their
numeric type changed.



TYPE = LITERAL (Read)
`````````````````````
The new numeric type to which the NDF's array components are to be
converted. The value given should be one of the following: _DOUBLE,
_REAL, _INTEGER, _INT64, _WORD, _UWORD, _BYTE or _UBYTE (note the
leading underscore). Existing pixel values stored in the NDF will not
be lost, but will be converted to the new type. Any values which
cannot be represented using the new type will be replaced with the
bad-pixel value.



VARIANCE = _LOGICAL (Read)
``````````````````````````
If a TRUE value is given for this parameter, then the numeric type of
the NDF's variance array will be changed. Otherwise, this component's
type will remain unchanged. [TRUE]



Examples
~~~~~~~~
settype rawdata _real
Converts the data and variance values held in the NDF data structure
rawdata to have a numeric type of _REAL (i.e. to be stored as single-
precision floating-point numbers).
settype inst.run1 _word novariance
Converts the data array in the NDF structure inst.run1 to be stored as
word (i.e. Fortran INTEGER*2) values. No change is made to the
variance component.
settype hd26571 _double complex
Causes the data and variance components of the NDF structure hd26571
to be altered so as to hold complex values using double precision
numbers. The existing pixel values are converted to this new type.



Related Applications
~~~~~~~~~~~~~~~~~~~~
Figaro: RETYPE.


Timing
~~~~~~
The execution time is approximately proportional to the number of
pixel values to be converted.


Copyright
~~~~~~~~~
Copyright (C) 1990, 1992 Science & Engineering Research Council.
Copyright (C) 1995 Central Laboratory of the Research Councils. All
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


