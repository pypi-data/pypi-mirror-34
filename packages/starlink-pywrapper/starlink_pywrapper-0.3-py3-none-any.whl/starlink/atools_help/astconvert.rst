

ASTCONVERT
==========


Purpose
~~~~~~~
Determine how to convert between two coordinate systems


Description
~~~~~~~~~~~
This application compares two FrameSets (or Frames) and determines
whether it is possible to convert between the coordinate systems which
they represent. If conversion is possible, it returns a FrameSet which
describes the conversion and which may be used (as a Mapping) to
transform coordinate values in either direction.


Usage
~~~~~


::

    
       astconvert from to domainlist result
       



ADAM parameters
~~~~~~~~~~~~~~~



DOMAINLIST = LITERAL (Read)
```````````````````````````
A string containing a comma-separated list of Frame domains. This may
be used to define a priority order for the different intermediate
coordinate systems that might be used to perform the conversion. If a
blank or null (!) value indicates that all coordinate systems should
be considered, regardless of their domains.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FROM = LITERAL (Read)
`````````````````````
An NDF or text file holding a Frame or FrameSet. If an NDF is
supplied, the WCS FrameSet will be used. It represents the "source"
coordinate system. This is the coordinate system in which you already
have coordinates available. If a FrameSet is given, its current Frame
is taken to describe the source coordinate system.



TO = LITERAL (Read)
```````````````````
An NDF or text file holding a Frame or FrameSet. If an NDF is
supplied, the WCS FrameSet will be used. It represents the
"destination" coordinate system. This is the coordinate system into
which you wish to convert your coordinates. If a FrameSet is given,
its current Frame is taken to describe the destination coordinate
system.



RESULT = LITERAL (Read)
```````````````````````
If the requested coordinate conversion is possible, a FrameSet is
written to the specified text file. Otherwise, a warning message is
displayed. If created, the FrameSet will contain two Frames. Frame
number 1 (its base Frame) will describe the source coordinate system,
corresponding to the FROM parameter. Frame number 2 (its current
Frame) will describe the destination coordinate system, corresponding
to the TO parameter. The Mapping which inter-relates these two Frames
will perform the required conversion between their respective
coordinate systems.



Copyright
~~~~~~~~~
Copyright (C) 2001 Central Laboratory of the Research Councils. All
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


