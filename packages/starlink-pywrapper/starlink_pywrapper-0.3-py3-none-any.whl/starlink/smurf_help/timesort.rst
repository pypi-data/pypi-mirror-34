

TIMESORT
========


Purpose
~~~~~~~
Re-order the time slices in a raw ACSIS data cube into increasing time


Description
~~~~~~~~~~~
This routine accepts as input one or more raw ACSIS data cubes,
spanned by (frequency, detector number, time) axes. It sorts the time
slices into monotonically increasing time value and writes the
resulting data to one or more new output NDFs. The ACSIS and JCMTSTATE
extensions and the WCS component are modified along with the main Data
array, so that the resulting cube remains internally consistent.
The main reason for using this routine is to ensure that data have a
defined transformation from WCS coordinates to pixel coordinates. It
can also be used to reduce the size of data files by excluding dead
detectors (see parameter DETPURGE). This command should be run before
attempting to merge multi-subsystem data.
There are two main modes, selected by parameter MERGE. If MERGE is
FALSE, then the time slices in each input NDF are sorted independently
of the other NDFs, and each output NDF contains data only from the
corresponding input NDF. If MERGE is TRUE, then the input NDFs are
sorted into groups that contain NDFs from the same observation and
sub-system (that is, all NDFs in a group have the same value for the
OBSIDSS FITS keyword). For each group, the time slices in all NDFs in
the group are sorted into a single list. This list is then divided up
into chunks (in a manner selected by parameter SIZELIMIT), and the
time slices are written out sequentially to a number of output NDFs.
If any time slice is present in more than one input NDF, then the data
values for the two or more input time slices are merged into a single
time slice.
MERGE = TRUE should be used to sort the time slices contained in a set
of sub-scans from a sub-system.


ADAM parameters
~~~~~~~~~~~~~~~



DETECTORS = LITERAL (Read)
``````````````````````````
A group of detector names to include in, or exclude from, the output
cube. If the first name starts with a minus sign, then the specified
detectors are excluded from the output cube (all other detectors are
included). Otherwise, the specified detectors are included from the
output cube (all other detectors are excluded). Information in the
ACSIS extension that is associated with excluded detectors is also
excluded from the output NDFs. If a null (!) value is supplied, data
from all detectors will be used. See also DETPURGE. [!]



DETPURGE = _LOGICAL (Read)
``````````````````````````
If TRUE, then any detectors that have no good data values in the input
NDFs will be excluded from the output NDFs. This is in addition to any
excluded detectors specified by the DETECTORS parameter. Information
in the ACSIS extension that is associated with such detectors is also
excluded from the output NDFs. Note, DETPURGE takes precedence over
DETECTORS. That is, if DETPURGE is set TRUE, then bad detectors will
be excluded even if the DETECTORS parameter indicates that they should
be included. [FALSE]



GENVAR = _LOGICAL (Read)
````````````````````````
If TRUE, then the Variance component in each output file is filled
with values determined from the Tsys values in the input files. These
variances values replace any inherited from the Variance component of
the input NDFs. [FALSE]



IN = NDF (Read)
```````````````
A group of input NDFs, each holding raw time series data.



LIMITTYPE = LITERAL (Read)
``````````````````````````
Only accessed if parameter MERGE is set TRUE and a positive value is
supplied for SIZELIMIT. Specifies the units of the SIZELIMIT value. It
must be one of:


+ "SPECTRA": SIZELIMIT is the maximum number of spectra in each output
NDF.
+ "SLICES": SIZELIMIT is the maximum number of time slices in each
output NDF.
+ "FILESIZE": SIZELIMIT is the maximum number of megabytes of data in
  each output NDF. Here, the SI definition of megabytes is used in which
  1 MB = 1,000,000 bytes.

Note, when using the FILESIZE option the specified file size only
includes the size of the Data and Variance components in the NDF.
Consequently, the actual file size may be a little larger than the
requested size because of the extra information held in NDF
extensions. ["FILESIZE"]



MERGE = _LOGICAL (Read)
```````````````````````
If FALSE, then each input NDF is sorted independently of the other
input NDFs, and the sorted data for each input NDF is written to a
separate output NDF. If TRUE, then the input NDFs are divided up into
groups relating to different observations. Each such group is then
further sub-divided up into groups relating to sub-systems within the
observation. Each group then holds sub-scans from a single observation
and sub-system. All the time slices from every NDF in each such group
are read into a single list, which is then sorted. The sorted data can
be written out to a single large output file (one for each observation
sub-system), or can be split up into several smaller output files, as
specified by the SIZELIMIT parameter. The dynamic default for this
parameter is TRUE if two or more of the input NDFs refer to the same
observation and sub-system number, and FALSE otherwise. []



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



NOUT = _INTEGER (Write)
```````````````````````
An output parameter in which is stored the total number of output NDFs
created.



OUT = NDF (Write)
`````````````````
A group of output NDFs. If parameter MERGE is FALSE, then a separate
output NDF is created for each input NDF and so the size of the
supplied group should equal the number of input NDF. If parameter
MERGE is TRUE, then the number of output NDFs is determined by the
SIZELIMIT parameter. In this case, the number of values in the
supplied group should equal the number of sub-systems represented in
the input data. If a GRP modification element is used to specify the
names, then the specified modifiation will be applied to a set of
names containing the first input NDF for each sub-system. If all the
input file names conform to the usual naming convention of ACSIS raw
time series files ("ayyyymmdd_nnnnn_nn_nnnn" with an optional
arbitrary trailing suffix that must begin with an underscore) then
each output NDF for a given sub-system will have an appropriately
incremented value for the trailing "_nnnn" field. If any of the input
NDFs do not conform to the ACSIS file naming convention, the strings
"_1", "_2", etc will be appended to the end of the supplied group of
names to form the output NDF names.



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line). If a null (!)
value is supplied no file is created. [!]



SIZELIMIT = _INTEGER (Read)
```````````````````````````
Only accessed if parameter MERGE is set TRUE. It is a number that
specifies the maximum size of each output NDF when merging data from
several input NDFs (see parameter MERGE). The minimum number of output
NDFs needed to hold all the input data will be used. The final output
NDF may be smaller than the specified maximum size. The value given is
either the file size in SI megabytes (1,000,000 bytes), the number of
time slices, or the number of spectra, as specified by parameter
LIMITTYPE. If a null (!) value is supplied, then the number of output
NDFs will be the same as the number of input NDFs, and all output NDFs
will have the same size. If a negative or zero value is supplied, then
a single output NDF will be created holding all the input data. [!]



SPECBND = LITERAL (Read)
````````````````````````
Indicates what to do if the input NDFs have differing pixel bounds on
the spectral axis.


+ "FIRST": The spectral axis in each output NDF will have the same
pixel bounds as the spectral axis in the first input NDF.
+ "UNION": The pixel bounds of the spectral axis in each output NDF
will be the union of the pixel bounds of the spectral axis in all
input NDFs.
+ "INTERSECTION": The pixel bounds of the spectral axis in each output
  NDF will be the intersection of the pixel bounds of the spectral axis
  in all input NDFs.

["FIRST"]



Notes
~~~~~


+ This command runs on ACSIS raw data files. SCUBA-2 files are
  guaranteed to be in time order.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKECUBE


Copyright
~~~~~~~~~
Copyright (C) 2007-2009,2012,2015 Science and Technology Facilities
Council. Copyright (C) 2013 University of British Columbia. All Rights
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


