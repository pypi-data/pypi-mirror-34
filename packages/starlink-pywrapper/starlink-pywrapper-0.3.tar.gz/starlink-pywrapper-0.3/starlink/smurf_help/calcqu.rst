

CALCQU
======


Purpose
~~~~~~~
Calculate Q and U images from a set of time-series data files


Description
~~~~~~~~~~~
This application creates Q and U values from a set of POL-2 time
series data files. It has two modes of operation, selected by the
LSQFIT parameter. The supplied time series data files are first flat-
fielded, cleaned and concatenated, before being used to create the Q
and U values.
If LSQFIT is set TRUE, then the output NDFs associated with parameters
OUTQ, OUTU and OUTI hold time series data in which the data values
represent Q, U and I respectively, rather than raw bolometer values.
These time-series are much shorter in length than the supplied input
time-series files. Each input time series is split into blocks of
adjacent time slices, and a single Q, U and I value is created for
each bolometer for each such block. The size of these blocks is
specified by the POLBOX configuration parameter, which is an integer
giving the size of each block as a multiple of the time taken for a
complete revolution of the half-waveplate. Each (Q,U,I) triplet is
found by doing a least squares fit to the supplied input data (i.e.
the analysed intensity data) within a single block of time slices. The
fitted function includes first, second, fourth and eight harmonics of
the half-waveplate, together with a linear background: ("w" is the
angle of the half-waveplate, and "itime" is the zero-based offset of
the time slice into the box):
y = A*sin(4*w) + B*cos(4*w) + C*sin(2*w) + D*cos(2*w) + E*sin(w) +
F*cos(w) + G*itime + H + J*sin(8*w) + K*cos(8*w)
The returned Q, U and I values are then:
U = 2*A Q = 2*B I = 2*( G*box/2 + H )
The Q and U values are specified with respect to either north or the
focal plane Y axis (see parameter NORTH). Each single pair of
corresponding Q and U values in the output NDFs are created from a
single least-squares fit, and the residuals of each such fit are used
to calculate a notional variance for the corresponding pair of Q and U
values. These are not "real" variances, but are just a scaled form of
the residuals variance using a scalaing factor that gives reasonable
agreement to the visible noise in the Q and U values measured in ten
test observations. These variances are intended for determining
relative weights for the Q and U values, and should not be used as
absolute variance values.
If LSQFIT is set FALSE, then the output NDFs associated with
parameters OUTQ, OUTU and OUTI are each 2D and contain a single Q, U
or I value for each bolometer. Multiple 2D images are created, as the
telescope slowly moves across the sky. Each image is created from a
block of time slices over which the sky position of each bolometer
does not change significantly (see parameters ARCERROR, MAXSIZE and
MINSIZE). The resulting set of Q images can be combined subsequently
using KAPPA:WCSMOSAIC, to form a single Q image (normally, the "I"
image should be used as the reference image when running WCSMOSIAC).
Likewise, the set of U images can be combined in the same way. All the
created Q and U images use the focal plane Y axis as the reference
direction (positive polarisation angles are in the same sense as
rotation from the focal plane X axis to the focal plane Y axis). Since
this direction may vary from block to block due to sky rotation, the
idividual Q and U images should be processed using POLPACK:POLROTREF
before combining them using KAPPA:WCSMOSAIC, to ensure that they all
use the same reference direction. Q and U values are determined from
the Fourier component of each time series corresponding to the
frequency of the spinning half-waveplate (6 - 12 Hz), and should be
largely unaffected by signal at other frequencies. For this reason,
the cleaning specified by parameter CONFIG should usually not include
any filtering that affects frequencies in the range 2 -16 Hz. There is
an option (see configuration parameter SUBMEAN) to subtract the mean
value from each time slice before using them to calculate Q and U.
Separate Q, U and I esimates are made for each half revolution of the
half-wave plate. The Data values in the returned NDFs are the mean of
these estimates. If there are four or more estimates per bolometer,
the output will also contain Variance values for each bolometer (these
variances represent the error on the final mean value, not the
variance of the individual values). A warning message will be
displayed if variances cannot be created due to insufficient input
data.
The current WCS Frame within the generated I, Q and U images will be
SKY (e.g. Right Ascension/Declination).


ADAM parameters
~~~~~~~~~~~~~~~



ARCERROR = _REAL (Read)
```````````````````````
The maximum spatial drift allowed within a single Q or U image, in
arc-seconds. The default value is wavelength dependant, and is equal
to half the default pixel size used by smurf:makemap. Only used if
LSQFIT is FALSE. []



CONFIG = GROUP (Read)
`````````````````````
Specifies values for various configuration parameters. If the string
"def" (case-insensitive) or a null (!) value is supplied, a set of
default configuration parameter values will be used.
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
The available parameters include the cleaning parameters used by the
SC2CLEAN and MAKEMAP commands, plus additional parameter related to
the calculation of Q and U. Further information about all these
parameters is available in the file $SMURF_DIR/smurf_calcqu.def.
Default values will be used for any unspecified parameters. Assigning
the value "<def>" (case insensitive) to a keyword has the effect of
resetting it to its default value. Parameters not understood will
trigger an error. [!]



FIX = _LOGICAL (Read)
`````````````````````
If TRUE, then attempt to fix up the data to take account of the POL-2
triggering issue that causes extra POL_ANG values to be introduced
into JCMTSTATE. [FALSE]



FLATUSENEXT = _LOGICAL (Read)
`````````````````````````````
If true the previous and following flatfield will be used to determine
the overall flatfield to apply to a sequence. If false only the
previous flatfield will be used. A null default will use both
flatfields for data when we did not heater track at the end, and will
use a single flatfield when we did heater track. The parameter value
is not sticky and will revert to the default unless explicitly over-
ridden. [!]



HARMONIC = _INTEGER (Read)
``````````````````````````
The Q and U values are derived from the fourth harmonic of the half-
wave plate rotation. However, to allow investigation of other
instrumental effects, it is possible instead to derive equivalent
quantities from any specified harmonic. These quantities are
calculated in exactly the same way as Q and U, but use the harmonic
specified by this parameter. They are stored in the output NDFs given
by the OUTQ, OUTU and OUTI parameters, in place of the normal Q, U and
I values. Only used if LSQFIT is FALSE. [4]



IN = NDF (Read)
```````````````
Input file(s).



LSQFIT = _LOGICAL (Read)
````````````````````````
Use least squares fitting method to generate I, Q and U time streams?
If not, the the output I, Q and U values are found by convolving each
input time stream with sine and cosine waves of the requested
harmonic. Note, the reference direction for LSQFIT Stokes vectors is
specified by parameter NORTH, whereas the reference direction for non-
LSQFIT Stokes vectors is always focal plane Y. [FALSE]



MAXSIZE = _INTEGER (Read)
`````````````````````````
The maximum number of time slices to include in any block. No upper
limit is imposed on block size if MAXSIZE is zero or negative. Only
used if LSQFIT is FALSE. [0]



MINSIZE = _INTEGER (Read)
`````````````````````````
The minimum number of time slices that can be included in a block No Q
or U values are created for blocks that are shorter than this value.
No lower limit is imposed on block size if MINSIZE is zero or
negative. Only used if LSQFIT is FALSE. [200]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NORTH = LITERAL (Read)
``````````````````````
Only used if LSQFIT is TRUE. Specifies the celestial coordinate system
to use as the reference direction for the returned Q and U values. For
instance if NORTH="AZEL", then they use the elevation axis as the
reference direction, and if "ICRS" is supplied, they use the ICRS
Declination axis. If "TRACKING" is supplied, they use north in the
tracking system - what ever that may be. If a null (!) value is
supplied, the Y axis of the focal plane system is used as the
reference direction. Note, Stokes parameters created with LSQFIT=FALSE
always use focal plane Y as the reference direction. ["TRACKING"]



OUTF = LITERAL (Write)
``````````````````````
The output files to contain the fitted analysed intensity. Only used
if LSQFIT is TRUE. It should be a group of time series NDFs. No fit
data files are created if a null (!) value is supplied. [!]



OUTFILESI = LITERAL (Write)
```````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line) that hold I
data. If a null (!) value is supplied no file is created. [!]



OUTFILESQ = LITERAL (Write)
```````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line) that hold Q
data. If a null (!) value is supplied no file is created. [!]



OUTFILESU = LITERAL (Write)
```````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line) that hold U
data. If a null (!) value is supplied no file is created. [!]



OUTI = LITERAL (Write)
``````````````````````
The output file to receive total intensity values. If LSQFIT is FALSE,
this will be an HDS container file containing the I images. The NDFs
within this container file are stored and named in the same way as
those in the "OUTQ" container file, but using "U" insead of "Q" in the
NDF names. If LSQFIT is TRUE, these will be a group of time series
NDFs. No I data files are created if a null (!) value is supplied. [!]



OUTQ = LITERAL (Write)
``````````````````````
The output file to receive Stokes Q values. If LSQFIT is FALSE, this
will be an HDS container file containing the Q images. Each image is
held in a separate 2D NDF within the container file. The NDF names
will be "Q<i>_<s>_<c>", where "<i>" is the integer one-based index of
the time slice block from which the image was made, "<s>" is the name
of the subarray (e.g. "s4a", etc), and "<c>" is an integer one-based
chunk index. If LSQFIT is TRUE, these will be a group of time series
NDFs.



OUTU = LITERAL (Write)
``````````````````````
The output file to receive Stokes U values. If LSQFIT is FALSE, this
will be an HDS container file containing the U images. Each image is
held in a separate 2D NDF within the container file. The NDF names
will be "U<i>_<s>_<c>", where "<i>" is the integer one-based index of
the time slice block from which the image was made, "<s>" is the name
of the subarray (e.g. "s4a", etc), and "<c>" is an integer one-based
chunk index. If LSQFIT is TRUE, these will be a group of time series
NDFs.



RESIST = GROUP (Read)
`````````````````````
A group expression containing the resistor settings for each
bolometer. Usually specified as a text file using "^" syntax. An
example can be found in $STARLINK_DIR/share/smurf/resist.cfg
[$STARLINK_DIR/share/smurf/resist.cfg]



Copyright
~~~~~~~~~
Copyright (C) 2011-2013 Science and Technology Facilities Council.
Copyright (C) 2015-2018 East Asian Observatory All Rights Reserved.


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


