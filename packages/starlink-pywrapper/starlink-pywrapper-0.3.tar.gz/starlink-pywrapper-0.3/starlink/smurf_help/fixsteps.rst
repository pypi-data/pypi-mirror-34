

FIXSTEPS
========


Purpose
~~~~~~~
Fix DC steps in a supplied SCUBA-2 time series NDF


Description
~~~~~~~~~~~
This routine runs the DC step fixer on a supplied time series (see
parameter IN), and optionally writes the corrected data to an output
time series (see parameter OUT). It is primarily intended as a
debugging tool for the step fixing code. A description of the step
fixes performed can be written to a text file (see parameter
NEWSTEPS). This can then be supplied as input to a later run of this
application in order to check that the new results are the same as the
old results (see parameter OLDSTEPS). A warning message will be
displayed if any significant difference is found between the old step
fixes and the new step fixes.
Configuration parameters for the step fixing algorithm can be supplied
either within a "makemap"-style configuration file (see parameter
CONFIG), or via command line environment parameters DCFITBOX,
DCSMOOTH, etc.


ADAM parameters
~~~~~~~~~~~~~~~



CHANGED = _LOGICAL (Write)
``````````````````````````
An output parameter to which is written a flag indicating if any
significant differences were found between the step fixes produced by
the current invocation of this program, and the step fixes described
in the file specified via parameter OLDSTEPS.



CONFIG = GROUP (Read)
`````````````````````
Specifies default values for the configuration parameters used by the
step fixing algorithm. This should be a configuration such as supplied
for the MAKEMAP command. [!]



CONTINUE = _LOGICAL (Read)
``````````````````````````
This parameter is prompted for after each changed step is described.
If TRUE is supplied, then the program continues to display details of
further changed steps. If FALSE is supplied, the program aborts.



DCFITBOX = _REAL
````````````````
Number of samples (box size) in which the signal RMS is measured for
the DC step finder. The run time default value is obtained via the
CONFIG parameter. [!]



DCLIMCORR = _INTEGER
````````````````````
The detection threshold for steps that occur at the same time in many
bolometers. Set it to zero to suppress checks for correlated steps. If
dclimcorr is greater than zero, and a step is found at the same time
in more than "dclimcorr" bolometers, then all bolometers are assumed
to have a step at that time, and the step is fixed no matter how small
it is. The run time default value is obtained via the CONFIG
parameter. [!]



DCMAXSTEPS = _INTEGER
`````````````````````
The maximum number of steps that can be corrected in each minute of
good data (i.e. per 12000 samples) from a bolometer before the entire
bolometer is flagged as bad. A value of zero will cause a bolometer to
be rejected if any steps are found in the bolometer data stream. The
run time default value is obtained via the CONFIG parameter. [!]



DCSMOOTH = _INTEGER
```````````````````
The width of the median filter used to smooth a bolometer data stream
prior to finding DC jumps. The run time default value is obtained via
the CONFIG parameter. [!]



DCTHRESH = _REAL
````````````````
Threshold S/N to detect and flag DC (baseline) steps. The run time
default value is obtained via the CONFIG parameter. [!]



FIRST = _INTEGER
````````````````
The index of the first change to be display (the first change has
index 1). Each change report starts with an index followed by a colon.
[1]



IN = NDF (Read)
```````````````
The time series cube to be fixed. Note, the data must be time ordered
(like the original raw data), not bolometer ordered.



MEANSHIFT = _LOGICAL (Read)
```````````````````````````
Use a mean shift filter prior to step fixing? A mean-shift filter is
an edge-preserving smooth. It can help to identify smaller steps, but
does not work well if there are strong gradients in the bolometer time
stream. Therefore, MEANSHIFT should only be used if the common-mode
signal has been subtracted. The spatial width of the filter is given
by DCSMOOTH, and the range of data values accepted by the filter is 5
times the local RMS in the original time stream. [FALSE]



NEWSTEPS = FILENAME (Write)
```````````````````````````
Name of a text file to create, holding a description of each step that
was fixed by the step fixing algorithm. The created file can be re-
used in a later run via the OLDSTEPS parameter. It can also be viewed
using "topcat -f ascii". If a null (!) value is supplied for NEWSTEPS,
no file is created. [!]



NFIXED = _INTEGER (Write)
`````````````````````````
The number of steps fixed.



NREJECTED = _INTEGER (Write)
````````````````````````````
The number of bolometers rejected due to them containing too many
steps.



OLDSTEPS = FILENAME (Read)
``````````````````````````
Name of a text file holding a description of each step that should be
fixed, if the step fixing algorithm is working correctly. An error is
reported if there is a difference between the steps fixes described in
this text file, and the step fixes actually produced by runnning the
step fixing algorithm. The text file should have been created by an
earlier run of this command (see parameter NEWSTEPS). If a null (!)
value is supplied for OLDSTEPS, no check is performed. [!]



OUT = NDF (Write)
`````````````````
The fixed time series cube. May be null (!), in which case no output
NDF is created.



SIZETOL = _DOUBLE (Read)
````````````````````````
Gives the fraction (i.e. relative error) by which two step sizes must
differ for them to be considered different. In addition, the absolute
difference between two step sizes must also differ by more than
SIZETOL times the clipped RMS step size. [0.05]



Copyright
~~~~~~~~~
Copyright (C) 2010-2012 Science and Technology Facilities Council. All
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


