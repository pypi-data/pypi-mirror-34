

ASTFINDFRAME
============


Purpose
~~~~~~~
Find a coordinate system with specified characteristics


Description
~~~~~~~~~~~
This application uses a "template" Frame to search another Frame (or
FrameSet) to identify a coordinate system which has a specified set of
characteristics. If a suitable coordinate system can be found, the
function returns a pointer to a FrameSet which describes the required
coordinate system and how to convert coordinates to and from it.
The index of the closest matching Frame in the target FrameSet is
displayed on the screen and returned in output parameter IFRAME.


Usage
~~~~~


::

    
       astfindframe target template domainlist result
       



ADAM parameters
~~~~~~~~~~~~~~~



DOMAINLIST = LITERAL (Read)
```````````````````````````
A string containing a comma-separated list of Frame domains. This may
be used to establish a priority order for the different types of
coordinate system that might be found.
The function will first try to find a suitable coordinate system whose
Domain attribute equals the first domain in this list. If this fails,
the second domain in the list will be used, and so on, until a result
is obtained. A blank domain (e.g. two consecutive commas) indicates
that any coordinate system is acceptable (subject to the template)
regardless of its domain.
This list is case-insensitive and all white space is ignored. If you
do not wish to restrict the domain in this way, you should supply a
blank string or null (!) value.



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



IFRAME = INTEGER (Write)
````````````````````````
On exit, this holds the index of the closest matching Frame in the
target FrameSet, or zero if no matching Frame was found. If the Target
is a Frame instead of a FrameSet, then a value of 1 is returned if a
match is found, and zero otherwise.



RESULT = LITERAL (Read)
```````````````````````
If the search is successful, a FrameSet is written to the specified
text file or NDF. Otherwise, a warning message is displayed. If
created, the FrameSet will contain two Frames. Frame number 1 (its
base Frame) represents the target coordinate system and will be the
same as the (base Frame of the) target. Frame number 2 (its current
Frame) will be a Frame representing the coordinate system which the
function found. The Mapping which inter-relates these two Frames will
describe how to convert between their respective coordinate systems.



TARGET = LITERAL (Read)
```````````````````````
An NDF or text file holding a Frame or FrameSet. If an NDF is
supplied, the WCS FrameSet will be used.



TEMPLATE = LITERAL (Read)
`````````````````````````
An NDF or text file holding a Frame. If an NDF is supplied, the
current Frame of the WCS FrameSet will be used. The Frame should be an
instance of the type of Frame you wish to find. If you wanted to find
a Frame describing a celestial coordinate system, for example, then
you might use a SkyFrame here.



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


