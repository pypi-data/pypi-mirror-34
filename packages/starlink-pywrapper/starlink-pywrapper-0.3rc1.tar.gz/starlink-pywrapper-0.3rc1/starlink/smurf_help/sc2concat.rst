

SC2CONCAT
=========


Purpose
~~~~~~~
Concatenate files into a larger file


Description
~~~~~~~~~~~
Given a list of input files this task concatenates them into larger
files. The rules it follows are:

+ data files are grouped by subarray;
+ files are only concatenated if they are continuous in time;
+ the longest a concatenated file may be is given by MAXLEN (in sec.);
+ for each continuous chunk of data, shorter than MAXLEN, a file is
  generated on disk for each subarray. The file name is determined as
  the name of the first input file for the chunk, with a suffix "_con".
  The can be modified using the parameter OUT.




ADAM parameters
~~~~~~~~~~~~~~~



FLAT = _LOGICAL (Read)
``````````````````````
If set ensure data are flatfielded. If not set do not scale the data
in any way (but convert to DOUBLE). [TRUE]



FLATMETH = _CHAR (Read)
```````````````````````
Method to use to calculate the flatfield solution. Options are
POLYNOMIAL and TABLE. Polynomial fits a polynomial to the measured
signal. Table uses an interpolation scheme between the measurements to
determine the power. [POLYNOMIAL]



FLATORDER = _INTEGER (Read)
```````````````````````````
The order of polynomial to use when choosing POLYNOMIAL method. [1]



FLATSNR = _DOUBLE (Read)
````````````````````````
Signal-to-noise ratio threshold to use when filtering the responsivity
data to determine valid bolometers for the flatfield. [3.0]



FLATUSENEXT = _LOGICAL (Read)
`````````````````````````````
If true the previous and following flatfield will be used to determine
the overall flatfield to apply to a sequence. If false only the
previous flatfield will be used. A null default will use both
flatfields for data when we did not heater track at the end, and will
use a single flatfield when we did heater track. The parameter value
is not sticky and will revert to the default unless explicitly over-
ridden. [!]



IN = NDF (Read)
```````````````
Input file(s).



MAXLEN = _DOUBLE (Read)
```````````````````````
Maximum length (in seconds) for concatenated file. The default is to
use all data if possible (subject to available memory). [!]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
Output concatenated files. Only used if OUTBASE is null (!). Note, the
correct number of output files must be specified for OUT. If this
number is not known, use parameter OUTBASE instead.



OUTBASE = LITERAL (Write)
`````````````````````````
The base name for the output NDFs. Each output NDF has a name equal to
"base_<n>" where <n> is an integer greater than or equal to 1. If a
null (!) value is supplied, the output NDFs are instead specified by
parameter OUT. [!]



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line). If a null (!)
value is supplied no file is created. [!]



PADEND = _INTEGER (Read)
````````````````````````
Number of samples to pad at end. Default is no padding. [!]



PADSTART = _INTEGER (Read)
``````````````````````````
Number of samples to pad at start. Default is no padding. [!]



RESIST = GROUP (Read)
`````````````````````
A group expression containing the resistor settings for each
bolometer. Usually specified as a text file using "^" syntax. An
example can be found in $STARLINK_DIR/share/smurf/resist.cfg
[$STARLINK_DIR/share/smurf/resist.cfg]



RESPMASK = _LOGICAL (Read)
``````````````````````````
If true, responsivity data will be used to mask bolometer data when
calculating the flatfield. [TRUE]



USEDARKS = _LOGICAL (Read)
``````````````````````````
Use darks to mask data. [TRUE]



Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2FFT, SC2CLEAN


Copyright
~~~~~~~~~
Copyright (C) 2005-2007 Particle Physics and Astronomy Research
Council. Copyright (C) 2005-2009,2013 University of British Columbia.
Copyright (C) 2008-2014 Science and Technology Facilities Council. All
Rights Reserved.


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


