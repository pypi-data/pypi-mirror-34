

DREAMWEIGHTS
============


Purpose
~~~~~~~
Generate DREAM weights matrix


Description
~~~~~~~~~~~
This is the main routine for (re)calculating the DREAM weights array
and inverse matrix.


ADAM parameters
~~~~~~~~~~~~~~~



CONFIG = Literal (Read)
```````````````````````
Specifies values for the configuration parameters used to determine
the grid properties. If the string "def" (case-insensitive) or a null
(!) value is supplied, a set of default configuration parameter values
will be used.
The supplied value should be either a comma-separated list of strings
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated list of strings. Each string is
either a "keyword=value" setting, or the name of a text file preceded
by an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner (any blank lines or lines beginning with "#" are ignored).
Within a text file, newlines can be used as delimiters as well as
commas. Settings are applied in the order in which they occur within
the list, with later settings over-riding any earlier settings given
for the same keyword.
Each individual setting should be of the form:
<keyword>=<value>
The parameters available for are listed in the "Configuration
Parameters" sections below. Default values will be used for any
unspecified parameters. Unrecognised options are ignored (that is, no
error is reported). [current value]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NDF = NDF (Read)
````````````````
Raw DREAM data file(s)



OUT = NDF (Write)
`````````````````
Output weights file(s)



Notes
~~~~~


+ Raw data MUST be passed in at present (this is due to a limitation
in smf_open_file)
+ Should allow for a list of bad (dead) bolometers.
+ This application interface is not finalised. Please do not rely on
  this command in scripts.




Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~
GRIDSTEP = INTEGER Scale size of the dream grid pattern. [6.28 arcsec]
GRIDMINMAX = INTEGER Array of integers specify the extent of the DREAM
pattern in pixels. Order is xmin, xmax, ymin, ymax [(-4,4,-4,4)]


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: DREAMSOLVE


Copyright
~~~~~~~~~
Copyright (C) 2008-2009 Science and Technology Facilities Council.
Copyright (C) 2006-2009 the University of British Columbia. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


