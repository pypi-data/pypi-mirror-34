

SC2CLEAN
========


Purpose
~~~~~~~
Clean SCUBA-2 time-series data


Description
~~~~~~~~~~~
This command is a stand-alone task for cleaning SCUBA-2 time-series
data. Cleaning operations include:

+ flag entire bolometer data streams as bad based on a threshold
fraction of bad samples;
+ removing large-scale detector drifts by fitting and removing low-
order polynomial baselines;
+ identifying and repairing DC steps;
+ flagging spikes;
+ replacing spikes and other gaps in the data with a constrained
realization of noise; and
+ applying other frequency-domain filters, such as a high-pass or
  correction of the DA system response.

All the above operations can be performed on the dark squid data.
These take the same parameters used for cleaning the primary bolometer
data but use the "cleandk" namespace. For example, "dcthresh" would
become "cleandk.dcthresh".


ADAM parameters
~~~~~~~~~~~~~~~



BBM = NDF (Read)
````````````````
Group of files to be used as bad bolometer masks. Each data file
specified with the IN parameter will be masked. The corresponding
previous mask for a subarray will be used. If there is no previous
mask the closest following will be used. It is not an error for no
mask to match. A NULL parameter indicates no mask files to be
supplied. [!]



COM = NDF (Write)
`````````````````
If COMPREPROCESS is set in the configuration file, the common mode is
calculated and removed from the bolometer data. The COM adam parameter
can then be used to specify an NDF to store the common mode. See also
GAI. [!]



CONFIG = GROUP (Read)
`````````````````````
Specifies values for the cleaning parameters. If the string "def"
(case-insensitive) or a null (!) value is supplied, a set of default
configuration parameter values will be used.
The supplied value should be either a comma-separated list of strings
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated lists of strings. Each string
is either a "keyword=value" setting, or the name of a text file
preceded by an up-arrow character "^". Such text files should contain
further comma-separated lists which will be read and interpreted in
the same manner (any blank lines or lines beginning with "#" are
ignored). Within a text file, newlines can be used as delimiters, as
well as commas. Settings are applied in the order in which they occur
within the list, with later settings over-riding any earlier settings
given for the same keyword.
Each individual setting should be of the form:
<keyword>=<value>
The available parameters are identical to the cleaning parameters used
by the iterative map-maker (method=ITER) and the available parameters
are listed in the "Configuration Parameters" appendix of SUN/258.
Default values will be used for any unspecified parameters. Assigning
the value "<def>" (case insensitive) to a keyword has the effect of
resetting it to its default value. Options available to the map-maker
but not understood by SC2CLEAN will be ignored. Parameters not
understood will trigger an error. Use the "cleandk." namespace for
configuring cleaning parameters for the dark squids. [current value]



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



GAI = NDF (Write)
`````````````````
If COMPREPROCESS is set in the configuration file, the common mode is
calculated and removed from the bolometer data. The GAI adam parameter
can then be used to specify an NDF to store the
gain/offset/correlation coefficients of the common-mode template for
each bolometer. See also COM. [!]



IN = NDF (Read)
```````````````
Input files to be cleaned



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
Output file(s).



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



Notes
~~~~~


+ The default values and allowed parameters can be found in
$SMURF_DIR/smurf_sc2clean.def
+ An iterative map-maker config file can be used.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKEMAP, SC2CONCAT, SC2FFT


Copyright
~~~~~~~~~
Copyright (C) 2008-2010 Science and Technology Facilities Council.
Copyright (C) 2005-2006 Particle Physics and Astronomy Research
Council. Copyright (C) 2008-2011,2013 University of British Columbia.
All Rights Reserved.


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
02110-1301, USA


