

NDF2TIFF
========


Purpose
~~~~~~~
Converts an NDF into an 8-bit TIFF-6.0-format file


Description
~~~~~~~~~~~
This application converts an NDF to a Image File Format (TIFF). One-
or two-dimensional arrays can be handled and various methods of
scaling the data are provided.
The routine first finds the brightest and darkest pixel values
required by the particular scaling method in use. It then uses these
to determine suitable scaling factors and converts the image into an
8-bit representation which is then output to a simple greyscale
TIFF-6.0 file.
If the 'high' scaling value is less than the 'low' value, the output
image will be a negative. Bad values are set to 0 for positives and
255 for negatives.


Usage
~~~~~


::

    
       ndf2tiff in out [scale] {high=? low=?
                               {percentiles=[?,?], [numbin=?]
                               {sigmas=[?,?]
       



Examples
~~~~~~~~
ndf2tiff old new
This converts the NDF called old (in file old.sdf) into a TIFF file
new.tif.
ndf2tiff horse horse pe
This converts the NDF called horse (in file horse.sdf) into a TIFF
file horse.tif using percentile scaling. The user will be prompted for
the percentiles to use.



Parameters
~~~~~~~~~~
HIGH = _DOUBLE (Read) The array value that scales to 255 in the TIFF
file. It is only required if SCALE is "Scale". All larger array values
are set to 255 when HIGH is greater than LOW, otherwise all array
values less than HIGH are set to 255. The dynamic default is the
maximum data value. There is an efficiency gain when both LOW and HIGH
are given on the command line, because the extreme values need not be
computed. The highest data value is suggested in prompts. IN = NDF
(Read) Input NDF data structure containing the image to be displayed.
LOW = _DOUBLE (Read) The array value that scales to 0 in the TIFF
file. It is only required if SCALE is "Scale". All smaller array
values are also set to 0 when LOW is less than HIGH, otherwise all
array values greater than LOW are set to 0. The dynamic default is the
minimum data value. There is an efficiency gain when both LOW and HIGH
are given on the command line, because the extreme values need not be
computed. The lowest data value is suggested in prompts. MSG_FILTER =
LITERAL (Read) The output message filtering level, QUIET, NORMAL or
VERBOSE. If set to verbose, the scaling limits used will be displayed.
[NORMAL] NUMBIN = _INTEGER (Read) The number of histogram bins used to
compute percentiles for scaling. It is only used if SCALE is
"Percentiles". [2048] OUT = _CHAR (Read) The name of the TIFF file to
be generated. A .tif name extension is added if it is omitted. Any
existing file with the same name will be overwritten. PERCENTILES( 2 )
= _REAL (Read) The percentiles that define the scaling limits. For
example, [25,75] would scale between the quartile values. It is only
required if SCALE is "Percentiles". SCAHIGH = _DOUBLE (Write) The
array value scaled to the maximum colour index. SCALE = LITERAL (Read)
The type of scaling to be applied to the array. [Range] The options,
which may be abbreviated to an unambiguous string and are case-
insensitive, are described below. "Range" - The image is scaled
between the minimum and maximum data values. (This is the default.)
"Faint" - The image is scaled from the mean minus one standard
deviation to the mean plus seven standard deviations. "Percentiles" -
The image is scaled between the values corresponding to two
percentiles. "Scale" - You define the upper and lower limits between
which the image is to be scaled. The application suggests the maximum
and the minimum values when prompting. "Sigmas" - The image is scaled
between two standard- deviation limits. SCALOW = _DOUBLE (Write) The
array value scaled to the minimum colour index. SIGMAS( 2 ) = _REAL
(Read) The standard-deviation bounds that define the scaling limits.
It is only required if SCALE is "Sigmas". To obtain values either side
of the mean both a negative and a positive value are required. Thus
[-2,3] would scale between the mean minus two and the mean plus three
standard deviations. [3,-2] would give the negative of that.


Related Applications
~~~~~~~~~~~~~~~~~~~~
TIFF2NDF


Copyright
~~~~~~~~~
Copyright (C) 1995-1996, 1999, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2008, 2011 Science & Technology Facilities
Council. All Rights Reserved.


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


