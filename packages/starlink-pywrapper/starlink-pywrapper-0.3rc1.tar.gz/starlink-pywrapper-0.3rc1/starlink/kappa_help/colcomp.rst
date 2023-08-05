

COLCOMP
=======


Purpose
~~~~~~~
Produces a colour composite of up to three 2-dimensional NDFs


Description
~~~~~~~~~~~
This application combines up to three 2-dimensional NDFs, using a
different primary colour (red, green or blue) to represent each NDF.
The resulting colour composite image is available in two forms; as an
NDF with an associated colour table (see parameter OUT and LUT), and
as an ASCII PPM image file (see parameter PPM). The full pixel
resolution of the input NDFs is retained. Note, this application does
not actually display the image, it just creates various output files
which must be displayed using other tools (see below).
The data values in each of the input NDFs which are to be mapped on to
zero intensity and full intensity can be given manually using
parameters RLOW, RHIGH, GLOW, GHIGH, BLOW and BHIGH, but by default
they are evaluated automatically. This is done by finding specified
percentile points within the data histograms of each of the input
images (see parameter PERCENTILES).
The NDF outputs are intended to be displayed with KAPPA application
DISPLAY, using the command:
display <out> scale=no lut=<lut>
where "<out>" and "<lut>" are the names of the NDF image and colour
table created by this application using parameters OUT and LUT. The
main advantage of this NDF form of output over the PPM form is that
any WCS or AXIS information in the input NDFs is still available, and
can be used to create axis annotations by the DISPLAY command. The
graphics device which will be used to display the image must be
specified when running this application (see parameter DEVICE).
The PPM form of output can be displayed using tools such as "xv", or
converted into other forms (GIF or JPEG, for instance) using tools
such as "ppmtogif" and "cjpeg" from the NetPbm or PbmPlus packages.
These tools provide more sophisticated colour quantisation methods
than are used by this application when creating the NDF outputs, and
so may give better visual results.


Usage
~~~~~


::

    
       colcomp inr ing inb out lut device
       



ADAM parameters
~~~~~~~~~~~~~~~



BADCOL = LITERAL (Read)
```````````````````````
The colour with which to mark any bad (i.e. missing) pixels in the
display. There are a number of options described below:


+ "MAX" -- The maximum colour index used for the display of the image.
+ "MIN" -- The minimum colour index used for the display of the image.
+ An integer -- The actual colour index. It is constrained between 0
and the maximum colour index available on the device.
+ A named colour -- Uses the named colour from the palette, and if it
is not present, the nearest colour from the palette is selected.
+ An HTML colour code such as \#ff002d.

If the colour is to remain unaltered as the lookup table is
manipulated choose an integer between 0 and 15, or a named colour.
Note, if only the PPM output is to be created (see parameter PPM),
then a named colour must be given for BADCOL. [current value]



BHIGH = _DOUBLE (Read)
``````````````````````
The data value corresponding to full blue intensity. If a null (!)
value is supplied, the value actually used will be determined by
forming a histogram of the data values in the NDF specified by
parameter INB, and finding the data value at the second histogram
percentile specified by parameter PERCENTILES. [!]



BLOW = _DOUBLE (Read)
`````````````````````
The data value corresponding to zero blue intensity. If a null (!)
value is supplied, the value actually used will be determined by
forming a histogram of the data values in the NDF specified by
parameter INB, and finding the data value at the first histogram
percentile specified by parameter PERCENTILES. [!]



DEVICE = DEVICE (Read)
``````````````````````
The name of the graphics device which will be used to display the NDF
output (see parameter OUT). This is needed only to determine the
number of available colours. No graphics output is created by this
application. This parameter is not accessed if a null (!) value is
supplied for parameter OUT. The device must have at least 24 colour
indices or greyscale intensities. [current image-display device]



GHIGH = _DOUBLE (Read)
``````````````````````
The data value corresponding to full green intensity. If a null (!)
value is supplied, the value actually used will be determined by
forming a histogram of the data values in the NDF specified by
parameter ING, and finding the data value at the second histogram
percentile specified by parameter PERCENTILES. [!]



GLOW = _DOUBLE (Read)
`````````````````````
The data value corresponding to zero green intensity. If a null (!)
value is supplied, the value actually used will be determined by
forming a histogram of the data values in the NDF specified by
parameter ING, and finding the data value at the first histogram
percentile specified by parameter PERCENTILES. [!]



INB = NDF (Read)
````````````````
The input NDF containing the data to be displayed in blue. A null (!)
value may be supplied in which case the blue intensity in the output
will be zero at every pixel.



ING = NDF (Read)
````````````````
The input NDF containing the data to be displayed in green. A null (!)
value may be supplied in which case the green intensity in the output
will be zero at every pixel.



INR = NDF (Read)
````````````````
The input NDF containing the data to be displayed in red. A null (!)
value may be supplied in which case the red intensity in the output
will be zero at every pixel.



LUT = NDF (Write)
`````````````````
Name of the output NDF to contain the colour lookup table which should
be used when displaying the NDF created using parameter OUT. This
colour table can be loaded using LUTREAD, or specified when the image
is displayed. This parameter is not accessed if a null (!) value is
given for parameter OUT.



RHIGH = _DOUBLE (Read)
``````````````````````
The data value corresponding to full red intensity. If a null (!)
value is supplied, the value actually used will be determined by
forming a histogram of the data values in the NDF specified by
parameter INR, and finding the data value at the second histogram
percentile specified by parameter PERCENTILES. [!]



RLOW = _DOUBLE (Read)
`````````````````````
The data value corresponding to zero red intensity. If a null (!)
value is supplied, the value actually used will be determined by
forming a histogram of the data values in the NDF specified by
parameter INR, and finding the data value at the first histogram
percentile specified by parameter PERCENTILES. [!]



OUT = NDF (Write)
`````````````````
The output colour composite image in NDF format. Values in this output
image are integer colour indices into the colour table created using
parameter LUT. The values are shifted to account for the indices
reserved for the palette (i.e. the first entry in the colour table is
addressed as entry 16, not entry 1). The NDF is intended to be used as
the input data in conjunction with DISPLAY SCALE=FALSE. If a null
value (!) is supplied, no output NDF will be created.



PERCENTILES( 2 ) = _REAL (Read)
```````````````````````````````
The percentiles that define the default scaling limits. For example,
[25,75] would scale between the quartile values. [5,95]



PPM = FILE (Write)
``````````````````
The name of the output text file to contain the PPM form of the colour
composite image. The colours specified in this file represent the
input data values directly. They are not quantised or dithered in any
way. Also note that because this is a text file, containing formatted
data values, it is portable, but can be very large, and slow to read
and write. If a null (!) value is supplied, no PPM output is created.
[!]



Examples
~~~~~~~~
colcomp m31_r m31_g m31_b m31_col m31_lut
Combines the 3 NDFs m31_r, m31_g, and m31_b to create a colour
composite image stored in NDF m31_col. A colour look-up table is also
created and stored in NDF m31_lut. It is assumed that the output image
will be displayed on the current graphics device. The created colour
composite image should be displayed using the command:
display m31_col scale=no lut=m31_lut
colcomp m31_r m31_g m31_b out=! ppm=m31.ppm
As above, but no NDF outputs are created. Instead, a file called
m31.ppm is created which (for instance) can be displayed using the
command:
xv m31.ppm
It can be converted to a GIF (for instance, for inclusion in WWW
pages) using the command:
ppmquant 256 m31.ppm | ppmtogif > m31.gif
These commands assume you have "xv", "ppmquant" and "ppmtogif"
installed at your site. None of them command are part of KAPPA.



Notes
~~~~~


+ The output image (PPM or NDF) covers the area of overlap between the
input NDFs at full resolution.
+ The output image is based on the values in the DATA components of
  the input NDFs. Any VARIANCE and QUALITY arrays in the input NDFs are
  ignored.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: DISPLAY, LUTREAD; XV; PBMPLUS; NETPBM.


Copyright
~~~~~~~~~
Copyright (C) 2011 Science & Technology Facilities Council. Copyright
(C) 1999, 2004 Central Laboratory of the Research Councils. Copyright
(C) 2006 Particle Physics & Astronomy Research Council. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ The HISTORY, WCS and AXIS components, together with any extensions
are propagated to the output NDF, from the first supplied input NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ Only data of type _REAL can be processed directly. Data of other
  types will be converted to _REAL before being processed.




