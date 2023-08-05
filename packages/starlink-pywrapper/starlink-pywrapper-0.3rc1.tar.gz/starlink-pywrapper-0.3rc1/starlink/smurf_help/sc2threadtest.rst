

SC2THREADTEST
=============


Purpose
~~~~~~~
Task for testing speeds of different threading schemes


Description
~~~~~~~~~~~
This routine tests schemes for visiting large quantities of SCUBA-2
data using multiple threads. This is a developer tool.


ADAM parameters
~~~~~~~~~~~~~~~



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NCHUNKS = _INTEGER (Read)
`````````````````````````
Number of time chunks. [2]



NSUB = _INTEGER (Read)
``````````````````````
Number of subarrays. [4]



NTHREAD = _INTEGER (Read)
`````````````````````````
Number of threads to use. [2]



TSTEPS = _INTEGER (Read)
````````````````````````
Number of time samples in simulated data chunk. [6000]



Copyright
~~~~~~~~~
Copyright (C) 2008-2010 University of British Columbia. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


