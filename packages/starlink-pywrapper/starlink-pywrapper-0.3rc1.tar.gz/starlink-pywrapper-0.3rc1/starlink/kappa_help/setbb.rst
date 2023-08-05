

SETBB
=====


Purpose
~~~~~~~
Sets a new value for the quality bad-bits mask of an NDF


Description
~~~~~~~~~~~
This application sets a new value for the bad-bits mask associated
with the quality component of an NDF. This 8-bit mask is used to
select which of the bits in the quality array should normally be used
to generate "bad" pixels when the NDF is accessed.
Wherever a bit is set to 1 in the bad-bits mask, the corresponding bit
will be extracted from the NDF's quality array value for each pixel
(the other quality bits being ignored). A pixel is then considered
"bad" if any of the extracted quality bits is set to 1. Effectively,
the bad-bits mask therefore allows selective activation of any of the
eight 1-bit masks which can be stored in the quality array.


Usage
~~~~~


::

    
       setbb ndf bb
       



ADAM parameters
~~~~~~~~~~~~~~~



AND = _LOGICAL (Read)
`````````````````````
By default, the value supplied via the BB parameter will be used
literally as the new bad-bits mask value. However, if a TRUE value is
given for the AND parameter, then a bit-wise `AND' will first be
performed with the old value of the mask. This facility allows
individual bits in within the mask to be cleared (i.e. reset to zero)
without affecting the current state of other bits (see the "Examples"
section).
The AND parameter is not used if a TRUE value is given for the OR
parameter. [FALSE]



BB = LITERAL (Read)
```````````````````
The new integer value for the bad-bits mask. This may either be
specified in normal decimal notation, or may be given using binary,
octal or hexadecimal notation by adding a "B", "O" or "Z" prefix
(respectively) to the appropriate string of digits. The value supplied
should lie in the range 0 to 255 decimal (or 8 bits of binary).
It may also be specified as a comma-separated list of quality names. A
quality name is a symbolic name that identifies a specific quality bit
(quality names can be defined using SETQUAL, and displayed using
SHOWQUAL).
If the AND and OR parameters are both FALSE, then the value supplied
will be used directly as the new mask value. However, if either of
these logical parameters is set to TRUE, then an appropriate bit-wise
`AND' or `OR' operation with the old mask value will first be
performed.
The default value suggested when prompting for this value is chosen so
as to leave the original mask value unchanged.



NDF = NDF (Read and Write)
``````````````````````````
The NDF whose bad-bits mask is to be modified.



OR = _LOGICAL (Read)
````````````````````
By default, the value supplied via the BB parameter will be used
literally as the new bad-bits mask value. However, if a TRUE value is
given for the OR parameter, then a bit-wise `OR' will first be
performed with the old value of the mask. This facility allows
individual bits in within the mask to be set to 1 without affecting
the current state of other bits (see the "Examples" section). [FALSE]



Examples
~~~~~~~~
setbb myframe 3
Sets the bad-bits mask value for the quality component of the NDF
called myframe to the value 3. This means that bits 1 and 2 of the
associated quality array will be used to generate bad pixels.
setbb myframe "SKY,BACK"
Sets the bad-bits mask value for the quality component of the NDF
called myframe so that any pixel that is flagged with either of the
two qualities "SKY" or "BACK" will be set bad. The NDF should contain
information that associates each of these quality names with a
specific bit in the quality array. Such information can for instance
be created using the SETQUAL command.
setbb ndf=myframe bb=b11
This example performs the same operation as above, but in this case
the new mask value has been specified using binary notation.
setbb xspec b10001000 or
Causes the bad-bits mask value in the NDF called xspec to undergo a
bit-wise `OR' operation with the binary value 10001000. This causes
bits 4 and 8 to be set without changing the state of any other bits in
the mask.
setbb quasar ze7 and
Causes the bad-bits mask value in the NDF called quasar to undergo a
bit-wise `AND' operation with the hexadecimal value E7 (binary
11100111). This causes bits 4 and 5 to be cleared (i.e. reset to zero)
without changing the state of any other bits in the mask.



Notes
~~~~~
The bad-bits value will be disregarded if the NDF supplied does not
have a quality component present. A warning message will be issued if
this should occur.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: QUALTOBAD, REMQUAL, SETQUAL, SHOWQUAL; Figaro: Q2BAD.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995 Central Laboratory of the Research Councils. Copyright (C)
2008 Science & Technology Facilities Council. All Rights Reserved.


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


