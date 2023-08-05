

POL2CHECK
=========


Purpose
~~~~~~~
Check if specified NDFs probably hold POL-2 data


Description
~~~~~~~~~~~
This application checks each supplied file to see if it looks like it
probably holds POL-2 data in a recognised form. If it does, it is
categorised as either:


+ raw analysed intensity time-series data
+ Q, U or I time-series data created by CALCQU
+ Q, U or I maps created by MAKEMAP.

If requested, output text files are created each holding a list of the
paths for the NDFs in each category.
The checks are based on NDF meta-data and FITS headers. It is possible
that an NDF could pass these checks and yet fail to open in other
smurf task if any of the additional meta-data required by those tasks
has been corrupted or is otherwise inappropriate.
An error is reported if POL2 data from more than one waveband (450 or
850) is present in the list of supplied data files.
By default, an error is also reported if POL2 data for more than one
object is present in the list of supplied data files (this check can
be disabled by setting parameter MULTIOBJECT to TRUE). The object is
given by FITS header "OBJECT".


ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
Input NDFs(s).



JUNKFILE = LITERAL (Read)
`````````````````````````
The name of a text file to create containing the paths to the input
NDFs that do not hold POL-2 data in any recognised form. Only accessed
if one or more such NDFs are found within the group of NDFs specified
by parameter IN. Supplying null (!) results in no file being created.
[!]



JUNKFOUND = _LOGICAL (Write)
````````````````````````````
Returned TRUE if one or more of the input NDFs is not a recognised
POL-2 file.



MAPFILE = LITERAL (Read)
````````````````````````
The name of a text file to create containing the paths to the input
NDFs that hold 2-dimensional maps of Q, U or I from POL-2 data. Only
accessed if one or more such NDFs are found within the group of NDFs
specified by parameter IN. Supplying null (!) results in no file being
created. [!]



MAPFOUND = _LOGICAL (Write)
```````````````````````````
Returned TRUE if one or more of the input NDFs holds 2-dimensonal maps
of Q, U or I from POL-2 data.



MAPINFO = LITERAL (Read)
````````````````````````
The name of a text file to create containing a line of information for
each input file listed in the MAPFILE file (in the same order). Each
line contains two space-sparated items: the first is a single letter
Q, U or I indicating the Stokes parameter, and the second is an
identifier of the form "<UT>_<OBS>_<SUBSCAN>", where <UT> is the 8
digit UT date, <OBS> is the 5 digit observation number and <SUBSCAN>
is the four digit number for the first subscan in the chunk (usually
"0003" except for observations made up of more than one discontiguous
chunks). No file is created if null (!) is supplied. [!]



MISSING = LITERAL (Read)
````````````````````````
The name of a text file to create identifying any missing raw data
sub-scans. No file is created if no sub-scans are missing or if no raw
data is supplied. The largest expected sub-scan number for all sub-
arrays is the largest sub-scan number for which any raw data was found
for any sub-array. The text file will contain a line for each sub-
array that has any missing sub-scans. Each line will start with the
sub-array name and be followed by a space spearated list of sub-scan
identifiers. For instance, "S8A: _0012 _0034".



MULTIOBJECT = _LOGICAL (Read)
`````````````````````````````
Indicates if it is acceptable for the list of input files to include
data for multiple objects. If FALSE, an error is reported if data for
more than one object is specified by parameter IN. Otherwise, no error
is reported if multiple objects are found. [FALSE]



RAWFILE = LITERAL (Read)
````````````````````````
The name of a text file to create containing the paths to the input
NDFs that hold raw analysed intensity POL-2 time-series data. Only
accessed if one or more such NDFs are found within the group of NDFs
specified by parameter IN. Supplying null (!) results in no file being
created. [!]



RAWFOUND = _LOGICAL (Write)
```````````````````````````
Returned TRUE if one or more of the input NDFs holds raw analysed
intensity POL-2 time-series data.



RAWINFO = LITERAL (Read)
````````````````````````
The name of a text file to create containing a line of information for
each input file listed in the RAWFILE file (in the same order). Each
line contains a key for the raw data file of the form ""<UT>_<OBS>",
where <UT> is the 8 digit UT date, and <OBS> is the 5 digit
observation number. No file is created if null (!) is supplied. [!]



STOKESFILE = LITERAL (Read)
```````````````````````````
The name of a text file to create containing the paths to the input
NDFs that hold Q, U or I POL-2 time-series data. Only accessed if one
or more such NDFs are found within the group of NDFs specified by
parameter IN. Supplying null (!) results in no file being created. [!]



STOKESFOUND = _LOGICAL (Write)
``````````````````````````````
Returned TRUE if one or more of the input NDFs holds Q, U or I POL-2
time-series data.



STOKESINFO = LITERAL (Read)
```````````````````````````
The name of a text file to create containing a line of information for
each input file listed in the STOKESFILE file (in the same order).
Each line contains two space-sparated items: the first is a single
letter Q, U or I indicating the Stokes parameter, and the second is an
identifier of the form "<UT>_<OBS>_<SUBSCAN>", where <UT> is the 8
digit UT date, <OBS> is the 5 digit observation number and <SUBSCAN>
is the four digit number for the first subscan in the chunk (usually
"0003" except for observations made up of more than one discontiguous
chunks). No file is created if null (!) is supplied. [!]



STOKES = LITERAL (Read)
```````````````````````
The name of a text file to create containing the identifiers



Notes
~~~~~


+ This application was written originally for use within the
  pol2scan.py script, as a means of speeding up operations that are very
  slow when imlemented via multiple calls to KAPPA commands such as
  "fitsval", etc.




Copyright
~~~~~~~~~
Copyright (C) 2016-2017 East Asian Observatory All Rights Reserved.


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


