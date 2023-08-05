

SKYNOISE
========


Purpose
~~~~~~~
Generate a simulated sky background with spatial noise


Description
~~~~~~~~~~~
This generates a simulated sky background with spatial noise following
a power law spectrum.


ADAM parameters
~~~~~~~~~~~~~~~



FILENAME = _CHAR (Write)
````````````````````````
Name of the output file containing the sky noise image.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OBSPAR = GROUP (Read)
`````````````````````
Specifies values for the observation parameters used for skynoise
generation.
The supplied value should be either a comma-separated list of strings
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated (or line-break separated) lists
of strings. Each string is either a "keyword=value" setting, or the
name of a text file preceded by an up-arrow character "^". Such text
files should contain further comma-separated lists which will be read
and interpreted in the same manner (any blank lines or lines beginning
with "#" are ignored). Within a text file, newlines can be used as
delimiters, as well as commas. Settings are applied in the order in
which they occur within the list, with later settings over-riding any
earlier settings given for the same keyword.
Each individual setting should be of the form:
<keyword>=<value>
The parameter names and their default values are listed below. The
default values will be used for any unspecified parameters.
Unrecognized parameters are ignored (i.e. no error is reported).



SEED = INTEGER (Read)
`````````````````````
Seed for random number generator. If a seed is not specified, the
clock time in milliseconds is used.



SIMPAR = GROUP (Read)
`````````````````````
Specifies values for the simulation parameters. See the description
for OBSFILE for the file format.
The parameter names and their default values are listed below. The
default values will be used for any unspecified parameters.
Unrecognized parameters are ignored (i.e. no error is reported).



Observation Parameters
~~~~~~~~~~~~~~~~~~~~~~
lambda (DOUBLE) Wavelength of observation in m. [0.85e-3]


Simulation Parameters
~~~~~~~~~~~~~~~~~~~~~
aomega (DOUBLE) Coupling factor (0.179 for 850 microns, 0.721 for 450
microns). [0.179] atmname (CHAR) Name of the file containing the
atmospheric sky image. atmrefnu (DOUBLE) Atmospheric reference corner
frequency in Hz. [0.5] atmrefvel (DOUBLE) Atmospheric reference
velocity in m/s. [15.0] bandGHz (DOUBLE) Bandwidth in GHz. [35.0]
tauzen (DOUBLE) Optical depth at 225 GHz at the zenith. [0.052583]


Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: SC2SIM


Copyright
~~~~~~~~~
Copyright (C) 2006 University of British Columbia. All Rights
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


