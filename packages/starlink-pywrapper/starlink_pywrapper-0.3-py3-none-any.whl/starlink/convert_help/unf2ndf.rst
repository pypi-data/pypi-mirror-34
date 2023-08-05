

UNF2NDF
=======


Purpose
~~~~~~~
Converts a sequential unformatted file to an NDF


Description
~~~~~~~~~~~
This application converts a sequential unformatted Fortran file to an
NDF. Only one of the array components may be created from the input
file. Preceding the input data there may be an optional header. This
header may be skipped, or may consist of a simple FITS header. In the
former case the shape of the NDF has be to be supplied.


Usage
~~~~~


::

    
       unf2ndf in out [comp] noperec [skip] shape [type]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The NDF component to be copied. It may be "Data", "Quality" or
"Variance". To create a variance or quality array the NDF must already
exist. ["Data"]



FITS = _LOGICAL (Read)
``````````````````````
If TRUE, the initial records of the unformatted file are interpreted
as a FITS header (with one card image per record) from which the
shape, data type, and axis centres are derived. The last record of the
FITS-like header must be terminated by an END keyword; subsequent
records in the input file are treated as an array component given by
COMP. [FALSE]



IN = FILENAME (Read)
````````````````````
Name of the input sequential unformatted Fortran file. The file will
normally have variable-length records when there is a header, but
always fixed-length records when there is no header.



NOPEREC = _INTEGER (Read)
`````````````````````````
The number of data values per record of the input file. It must be
positive on UNIX systems. The suggested default is the size of the
first dimension of the array if there is no current value. A null (!)
value for NOPEREC causes the size of first dimension to be used.



OUT = NDF (Read and Write)
``````````````````````````
Output NDF data structure. When COMP is not "Data" the NDF is modified
rather than a new NDF created. It becomes the new current NDF.



SHAPE = _INTEGER (Read)
```````````````````````
The shape of the NDF to be created. For example, [40,30,20] would
create 40 columns by 30 lines by 10 bands. It is only accessed when
FITS is FALSE.



SKIP = INTEGER (Read)
`````````````````````
The number of header records to be skipped at the start of the input
file before finding the data array or FITS-like header. [0]



TYPE = LITERAL (Read)
`````````````````````
The data type of the input file and output NDF. It must be one of the
following HDS types: "_BYTE", "_WORD", "_REAL", "_INTEGER", "_INT64",
"_DOUBLE", "_UBYTE", "_UWORD" corresponding to signed byte, signed
word, real, integer, 64-bit integer, double precision, unsigned byte,
and unsigned word. See SUN/92 for further details. An unambiguous
abbreviation may be given. TYPE is ignored when COMP = "Quality" since
the QUALITY component must comprise unsigned bytes (equivalent to TYPE
= "_UBYTE") to be a valid NDF. The suggested default is the current
value. TYPE is also only accessed when FITS is FALSE. ["_REAL"]



Examples
~~~~~~~~
unf2ndf ngc253.dat ngc253 shape=[100,60] noperec=8
This copies a data array from the unformatted file ngc253.dat to the
NDF called ngc253. The input file does not contain a header section.
The NDF is two-dimensional: 100 elements in x by 60 in y. Its data
array has type _REAL. The data records each have 8 values.
unf2ndf ngc253q.dat ngc253 q 100 shape=[100,60]
This copies a quality array from the unformatted file ngc253q.dat to
an existing NDF called ngc253 (such as created in the first example).
The input file does not contain a header section. The NDF is two-
dimensional: 100 elements in x by 60 in y. Its data array has type
_UBYTE. The data records each have 100 values.
unf2ndf ngc253.dat ngc253 fits noperec=!
This copies a data array from the unformatted file ngc253.dat to the
NDF called ngc253. The input file contains a FITS-like header section,
which is copied to the FITS extension of the NDF. The shape of the NDF
is controlled by the mandatory FITS keywords NAXIS, AXIS1, ..., AXISn,
and the data type by keywords BITPIX and UNSIGNED. Each data record
has AXIS1 values (except perhaps for the last).
unf2ndf type="_uword" in=ngc253.dat out=ngc253 \
This copies a data array from the unformatted file ngc253.dat to the
NDF called ngc253. The input file does not contain a header section.
The NDF has the current shape and data type is unsigned word. The
current number of values per record is used.
unf2ndf spectrum zz skip=2 shape=200 noperec=!
This copies a data array from the unformatted file spectrum to the NDF
called zz. The input file contains two header records that are
ignored. The NDF is one-dimensional comprising 200 elements of type
_REAL. There is one data record containing the whole array.
unf2ndf spectrum.lis ZZ skip=1 fits noperec=20
This copies a data array from the unformatted file spectrum.lis to the
NDF called ZZ. The input file contains one header record, that is
ignored, followed by a FITS-like header section, which is copied to
the FITS extension of the NDF. The shape of the NDF is controlled by
the mandatory FITS keywords NAXIS, AXIS1, ..., AXISn, and the data
type by keywords BITPIX and UNSIGNED. Each data record has AXIS1
values (except perhaps for the last).



Notes
~~~~~
The details of the conversion are as follows:

+ the unformatted-file array is written to the NDF array as selected
by COMP. When the NDF is being modified, the shape of the new
component must match that of the NDF.
+ If the input file contains a FITS-like header, and a new NDF is
created, i.e. COMP = "Data", the header records are placed within the
NDF's FITS extension. This enables more than one array (input file) to
be used to form an NDF. Note that the data array must be created first
to make a valid NDF, and it's the FITS structure associated with that
array that is wanted. Indeed the application prevents you from doing
otherwise.
+ The FITS-like header defines the properties of the NDF as follows: o
BITPIX defines the data type: 8 gives _BYTE, 16 produces _WORD, 32
makes _INTEGER, 64 creates _INT64, -32 gives _REAL, and -64 generates
_DOUBLE. For the first two, if there is an extra header record with
the keyword UNSIGNED and logical value T, these types become _UBYTE
and _UWORD respectively. UNSIGNED is non-standard, since unsigned
integers would not follow in a proper FITS file. However, here it is
useful to enable unsigned types to be input into an NDF. UNSIGNED may
be created by this application's sister, NDF2UNF. BITPIX is ignored
for QUALITY data; type _UBYTE is used. o NAXIS, and NAXISn define the
shape of the NDF. o The TITLE, LABEL, and BUNIT are copied to the NDF
TITLE, LABEL, and UNITS NDF components respectively. o The CDELTn,
CRVALn, CTYPEn, and CUNITn keywords make linear axis structures within
the NDF. CUNITn define the axis units, and the axis labels are
assigned to CTYPEn If some are missing, pixel co-ordinates are used
for those axes. o BSCALE and BZERO in a FITS extension are ignored. o
BLANK is not used to indicate which input array values should be
assigned to a standard bad value. o END indicates the last header
record unless it terminates a dummy header, and the actual data is in
an extension.
+ Other data item such as HISTORY, data ORIGIN, and axis widths are
  not supported, because the unformatted file has a simple structure to
  enable a diverse set of input files to be converted to NDFs, and to
  limitations of the standard FITS header.




Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: NDF2UNF.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1996, 2004 Central Laboratory of the Research Councils. Copyright
(C) 2012 Science & Technology Facilities Council. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


