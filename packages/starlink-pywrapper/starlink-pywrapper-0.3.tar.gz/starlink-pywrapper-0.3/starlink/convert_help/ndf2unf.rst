

NDF2UNF
=======


Purpose
~~~~~~~
Converts an NDF to a sequential unformatted file


Description
~~~~~~~~~~~
This application converts an NDF to a sequential unformatted Fortran
file. Only one of the array components may be copied to the output
file. Preceding the data there is an optional header consisting of
either the FITS extension with the values of certain keywords replaced
by information derived from the NDF, or a minimal FITS header also
derived from the NDF.


Usage
~~~~~


::

    
       ndf2unf in out [comp] [noperec]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The NDF component to be copied. It may be "Data", "Quality" or
"Variance". ["Data"]



FITS = _LOGICAL (Read)
``````````````````````
If TRUE, any FITS extension is written to start of the output file,
unless there is no extension whereupon a minimal FITS header is
written to the unformatted file. [FALSE]



IN = NDF (Read)
```````````````
Input NDF data structure. The suggested default is the current NDF if
one exists, otherwise it is the current value.



NOPEREC = _INTEGER (Read)
`````````````````````````
The number of data values per record of the output file. It must be
positive. The suggested default is the current value. [The first
dimension of the NDF]



OUT = FILENAME (Write)
``````````````````````
Name of the output sequential unformatted file. The file will normally
have variable-length records when there is a header, but always fixed-
length records when there is no header.



Examples
~~~~~~~~
ndf2unf cluster cluster.dat
This copies the data array of the NDF called cluster to an unformatted
file called cluster.dat. The number of data values per record is equal
to the size of the first dimension of the NDF.
ndf2unf cluster cluster.dat v
This copies the variance of the NDF called cluster to an unformatted
file called cluster.dat. The number of variance values per record is
equal to the size of the first dimension of the NDF.
ndf2unf cluster cluster.dat noperec=12
This copies the data array of the NDF called cluster to an unformatted
file called cluster.dat. There are twelve data values per record in
cluster.dat.
ndf2unf out=ndf234.dat fits in=@234
This copies the data array of the NDF called 234 to an unformatted
file called ndf234.dat. The number of data values per record is equal
to the size of the first dimension of the NDF. If there is a FITS
extension, it is copied to ndf234.dat with substitution of certain
keywords, otherwise a minimal FITS header is produced.



Notes
~~~~~
The details of the conversion are as follows:

+ the NDF array as selected by COMP is written to the unformatted file
in records following an optional header.
+ HISTORY is not propagated.
+ ORIGIN information is lost.
+ When a header is to be made, it is composed of FITS-like card images
as follows:
+ The number of dimensions of the data array is written to the keyword
NAXIS, and the actual dimensions to NAXIS1, NAXIS2 etc. as
appropriate.
+ If the NDF contains any linear axis structures the information
necessary to generate these structures is written to the FITS-like
headers. For example, if a linear AXIS(1) structure exists in the
input NDF the value of the first data point is stored with the keyword
CRVAL1, and the incremental value between successive axis data is
stored in keyword CDELT1. By definition the reference pixel is 1.0 and
is stored in keyword CRPIX1. If there is an axis label it is written
to keyword CTYPE1, and axis unit is written to CUNIT1. (Similarly for
AXIS(2) structures etc.) FITS does not have a standard method of
storing axis widths and variances, so these NDF components will not be
propagated to the header. Non-linear axis data arrays cannot be
represented by CRVALn and CDELTn, and must be ignored.
+ If the input NDF contains TITLE, LABEL or UNITS components these are
stored with the keywords TITLE, LABEL or BUNIT respectively.
+ If the input NDF contains a FITS extension, the FITS items may be
written to the FITS-like header, with the following exceptions: o
BITPIX is derived from the type of the NDF data array, and so it is
not copied from the NDF FITS extension. o NAXIS, and NAXISn are
derived from the dimensions of the NDF data array as described above,
so these items are not copied from the NDF FITS extension. o The
TITLE, LABEL, and BUNIT descriptors are only copied if no TITLE,
LABEL, and UNITS NDF components respectively have already been copied
into these headers. o The CDELTn, CRVALn, CTYPEn, CUNITn, and CRTYPEn
descriptors in the FITS extension are only copied if the input NDF
contained no linear axis structures. o The standard order of the FITS
keywords is preserved, thus BITPIX, NAXIS and NAXISn appear
immediately after the first card image, which should be SIMPLE. o
BSCALE and BZERO in a FITS extension are copied when BITPIX is
positive, i.e. the array is not floating-point.
+ An extra header record with keyword UNSIGNED and logical value T is
added when the array data type is one of the HDS unsigned integer
types. This is done because standard FITS does not support unsigned
integers, and allows (in conjunction with BITPIX) applications reading
the unformatted file to determine the data type of the array.
+ The last header record card will be the standard FITS END.
+ Other extensions are not propagated.




Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: UNF2NDF.


Copyright
~~~~~~~~~
Copyright (C) 1992-1993 Science & Engineering Research Council.
Copyright (C) 1995-1996, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2012 Science & Technology Facilities Council.
All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ The value of bad pixels is not written to a FITS-like header record
  with keyword BLANK.




