

CALCNOISE
=========


Purpose
~~~~~~~
Calculate noise image


Description
~~~~~~~~~~~
This routine cleans the supplied data and then calculates the white
noise on the array by performing an FFT to generate a power spectrum
and then extracting the data between two frequency ranges. It
additionally calculates an NEP image and an image of the ratio of the
power at a specified frequency to the whitenoise.


ADAM parameters
~~~~~~~~~~~~~~~



CONFIG = GROUP (Read)
`````````````````````
Specifies values for the cleaning parameters. If the string "def"
(case-insensitive) is supplied, a set of default configuration
parameter values will be used. CONFIG=! disables all cleaning and
simply applies apodisation. This is generally not a recommended use of
calcnoise.
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
by the iterative map-maker (method=ITER) and are are described in the
"Configuration Parameters" appendix of SUN/258. Default values will be
used for any unspecified parameters. Assigning the value "<def>" (case
insensitive) to a keyword has the effect of resetting it to its
default value. Options available to the map-maker but not understood
by CALCNOISE will be ignored. Parameters not understood will trigger
an error. Use the "cleandk." namespace for configuring cleaning
parameters for the dark squids.
If a null value (!) is given all cleaning will be disabled and the
full time series will be apodized with no padding. This differs to the
behaviour of SC2CLEAN where the defaults will be read and used.
[current value]



EFFNEP = _DOUBLE (Write)
````````````````````````
The effective noise of the .MORE.SMURF.NEP image. See the EFFNOISE
parameter for details of how it is calculated.



EFFNOISE = _DOUBLE (Write)
``````````````````````````
The effective noise of the primary output image. If this command was
run on raw data it will be the current noise and if run on flatfielded
data it will be the effective NEP. Calculated as the sqrt of
1/sum(1/sigma^2). See also the EFFNEP parameter.



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



FLOW = _DOUBLE (Given)
``````````````````````
Frequency to use when determining noise ratio image. The noise ratio
image is determined by dividing the power at this frequency by the
white noise [0.5]



FREQ = _DOUBLE (Given)
``````````````````````
Frequency range (Hz) to use to calculate the white noise [2,10]



IN = NDF (Read)
```````````````
Input files to be transformed. Files from the same sequence will be
combined.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NEPCLIPHIGH = _DOUBLE (Given)
`````````````````````````````
Flag NEP values this number of standard deviations above the median.
If a null (!) value is supplied now high-outlier clipping. [!]



NEPCLIPLOW = _DOUBLE (Given)
````````````````````````````
Flag NEP values this number of standard deviations below the median.
If a null (!) value is supplied now low-outlier clipping. [3]



NEPCLIPLOG = _LOGICAL (Given)
`````````````````````````````
Clip based on the log of the NEP. [TRUE]



NEPGOODBOL = _INTEGER (Write)
`````````````````````````````
The number of bolometers with good NEP measurements (see EFFNEP)



NOICLIPHIGH = _DOUBLE (Given)
`````````````````````````````
Flag NOISE values this number of standard deviations above the median.
If a null (!) value is supplied now high-outlier clipping. [!]



NOICLIPLOW = _DOUBLE (Given)
````````````````````````````
Flag NOISE values this number of standard deviations below the median.
If a null (!) value is supplied now low-outlier clipping. [3]



NOICLIPLOG = _LOGICAL (Given)
`````````````````````````````
Clip based on the log of the NOISE. [TRUE]



NOISEGOODBOL = _INTEGER (Write)
```````````````````````````````
The number of bolometers with good NOISE measurements (see EFFNOISE)



OUT = NDF (Write)
`````````````````
Output files (either noise or NEP images depending on the NEP
parameter). Number of output files may differ from the number of input
files. These will be 2 dimensional.



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line) from the OUT
parameter. If a null (!) value is supplied no file is created. [!]



POWER = NDF (Write)
```````````````````
Output files to contain the power spectra for each processed chunk.
There will be the same number of output files as created for the OUT
parameter. If a null (!) value is supplied no files will be created.
[!]



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



TSERIES = NDF (Write)
`````````````````````
Output files to contain the cleaned time-series for each processed
chunk. There will be the same number of output files as created for
the OUT parameter. If a null (!) value is supplied no files will be
created. [!]



Notes
~~~~~


+ NEP and NOISERATIO images are stored in the .MORE.SMURF extension
+ NEP image is only created for raw, unflatfielded data.
+ If the data have flatfield information available the noise and
NOISERATIO images will be masked by the flatfield bad bolometer mask.
The mask can be removed using SETQUAL or SETBB (clear the bad bits
mask).
+ NOICLIP[LOW/HIGH] and NEPCLIP[LOW/HIGH] are done independently for
  the NOISE and NEP images (so a bolometer may be clipped in one, but
  not the other).




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2CONCAT, SC2CLEAN, SC2FFT


Copyright
~~~~~~~~~
Copyright (C) 2009-2011 Science and Technology Facilities Council.
Copyright (C) 2011 University of British Columbia All Rights Reserved.


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


