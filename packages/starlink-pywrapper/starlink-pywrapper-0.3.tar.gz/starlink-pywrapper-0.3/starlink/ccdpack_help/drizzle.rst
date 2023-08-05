

DRIZZLE
=======


Purpose
~~~~~~~
Resamples and mosaics using the drizzling algorithm


Description
~~~~~~~~~~~
This routine transforms a set of NDFs from their pixel into their
Current coordinate system. The resulting NDFs are combined together
onto a single output grid, which can therefore form a mosaic of the
input images. Normalisation of the images can optionally be carried
out so that in overlapping regions the scaling and zero point values
of the images are consistent with each other.
The algorithm used for combining the images on the output grid is
Variable-Pixel Linear Reconstruction, or so-called 'drizzling'. The
user is allowed to shrink the input pixels to a smaller size (drops)
so that each pixel of the input image only affects pixels in the
output image under the corresponding drop.


Usage
~~~~~


::

    
       drizzle in out
       



ADAM parameters
~~~~~~~~~~~~~~~



CORRECT = LITERAL (Read)
````````````````````````
Name of the sequential file containing the SCALE and ZERO point
corrections for the list of input NDFs given by the IN parameter [!]



GENVAR = _LOGICAL (Read)
````````````````````````
If GENVAR is set to TRUE and some of the input images supplied contain
statistical error (variance) information, then variance information
will also be calculated for the output image. [TRUE]



IN = LITERAL (Read)
```````````````````
A list of the names of the input NDFs which are to be combined into a
mosaic. The NDF names should be separated by commas and may include
wildcards. The input NDFs are accessed only for reading.



LISTIN = _LOGICAL (Read)
````````````````````````
If a TRUE value is given for this parameter (the default), then the
names of all the NDFs supplied as input will be listed (and will be
recorded in the logfile if this is enabled). Otherwise, this listing
will be omitted. [TRUE]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter, then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP, then the
value specified there will be used. Otherwise, the default is
"CCDPACK.LOG". [CCDPACK.LOG]



LOGTO = LITERAL (Read)
``````````````````````
Every CCDPACK application has the ability to log its output for future
reference as well as for display on the terminal. This parameter
controls this process, and may be set to any unique abbreviation of
the following:

+ TERMINAL -- Send output to the terminal only
+ LOGFILE -- Send output to the logfile only (see the LOGFILE
parameter)
+ BOTH -- Send output to both the terminal and the logfile
+ NEITHER -- Produce no output at all

If the logging system has been initialised using CCDSETUP, then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



MAPVAR = _LOGICAL (Read)
````````````````````````
The value of this parameter specifies whether statistical error
(variance) information contained in the input NDFs should be used to
weight the input image pixels as they are drizzled on to the output
NDF (see the discussion of the drizzling algorithm). If MAPVAR is set
to .TRUE. then the ratio of the inverse variance of the input pixel
and the the mean inverse variance of the reference frame (or first
input NDF if no reference frame is provided) will be used to weight
each pixel as it drizzled onto the output image.
If weighting of the input pixels by the mean inverse variance of the
entire input image (rather than the pixels own variance) is required
MAPVAR should be set to .FALSE. and USEVAR should be set to .TRUE.
(this is the default condition). [FALSE]



MULTI = _DOUBLE (Read)
``````````````````````
The linear scaling between the size of the input and output pixels,
i.e. for a MULTI of 2.0 then each side of the input pixel is twice
that of the sub-sampling output pixel. For large values of MULTI,
PIXFRAC must also be larger (e.g. for a MULTI of 4.0 a PIXFRAC of 0.7
is unacceptably small for simgle image drizzling, however for a MULTI
of 3.0 a PIXFRAC of 0.7 produces acceptable output images). [1.5]



OUT = NDF (Write)
`````````````````
Name of the NDF to contain the output mosaic.



PIXFRAC = _DOUBLE (Read)
````````````````````````
The linear "drop" size, this being the ratio of the linear size of the
drizzled drop to that of the input pixel. Interlacing is equivalent to
setting PIXFRAC=0.0, while shift-and-add is equivalent to setting
PIXFRAC=1.0. For low values of PIXFRAC the MULTI parameter must also
be set correspondingly low. [0.9]



PRESERVE = _LOGICAL (Read)
``````````````````````````
If a TRUE value is given for this parameter (the default), then the
data type of the output mosaic NDF will be derived from that of the
input NDF with the highest precision, so that the input data type will
be "preserved" in the output NDF. Alternatively, if a FALSE value is
given, then the output NDF will be given an appropriate floating point
data type.
When using integer input data, the former option is useful for
minimising the storage space required for large mosaics, while the
latter typically permits a wider output dynamic range when necessary.
A wide dynamic range is particularly important if a large range of
scale factor corrections are being applied (as when combining images
with a wide range of exposure times).
If a global value has been set up for this parameter using CCDSETUP,
then that value will be used. [TRUE]



REF = NDF (Read)
````````````````
If the input NDFs being drizzled onto the output NDF are being
weighted by the inverse of their mean variance (see the USEVAR
parameter) then by default the first NDF frame in the input list (IN)
will be used as a reference frame. However, if an NDF is given via the
REF parameter (so as to over-ride its default null value), then the
weighting will instead be relative to the "reference NDF" supplied via
this parameter.
If scale-factor, zero-point corrections (see the SCALE and ZERO
parameters respectively) have not been specified via a sequential file
listing (see the CORRECT parameter) then if an NDF is given via the
REF parameter the program will attempt to normalise the input NDFs to
the "reference NDF" supplied.
This provides a means of retaining the calibration of a set of data,
even when corrections are being applied, by nominating a reference NDF
which is to remain unchanged. It also allows the output mosaic to be
normalised to any externally-calibrated NDF with which it overlaps,
and hence allows a calibration to be transferred from one set of data
to another.
If the NDF supplied via the REF parameter is one of those supplied as
input via the IN parameter, then this serves to identify which of the
input NDFs should be used as a reference, to which the others will be
adjusted. In this case, the scale-factor, zero-point corrections
and/or weightings applied to the nominated input NDF will be set to
one, zero and one respectively, and the corrections for the others
will be adjusted accordingly.
Alternatively, if the reference NDF does not appear as one of the
input NDFs, then it will be included as an additional set of data in
the inter-comparisons made between overlapping NDFs and will be used
to normalise the corrections obtained (so that the output mosaic is
normalised to it). However, it will not itself contribute to the
output mosaic in this case. [!]



SCALE = _LOGICAL (Read)
```````````````````````
This parameter specifies whether DRIZZLE should attempt to adjust the
input data values by applying scale-factor (i.e. multiplicative)
corrections before combining them into a mosaic. This would be
appropriate, for instance, if a series of images had been obtained
with differing exposure times; to combine them without correction
would yield a mosaic with discontinuities at the image edges where the
data values differ.
If SCALE is set to TRUE, then DRIZZLE will ask the user for a
sequential file containing the corrections for each image (see the
CORRECT parameter). If none is supplied the program will attempt to
find its own corrections.
DRIZZLE will inter-compare the NDFs supplied as input and will
estimate the relative scale-factor between selected pairs of input
data arrays where they overlap. From this information, a global set of
multiplicative corrections will be derived which make the input data
as mutually consistent as possible. These corrections will be applied
to the input data before drizzling them onto the output frame.
Calculation of scale-factor corrections may also be combined with the
use of zero-point corrections (see the ZERO parameter). By default, no
scale-factor corrections are applied. [FALSE]



TITLE = LITERAL (Read)
``````````````````````
Title for the output mosaic NDF. [Output from DRIZZLE]



USEVAR = _LOGICAL (Read)
````````````````````````
The value of this parameter specifies whether statistical error
(variance) information contained in the input NDFs should be used to
weight the input image pixels as they are drizzled on to the output
NDF (see the discussion of the drizzling algorithm). If USEVAR is set
to TRUE then the ratio of the mean inverse variance of the input image
and the mean inverse variance of the reference frame (or first input
NDF if no reference frame is provided) will be used as a weighting for
the image.
If weighting of the input image by the inverse variance map (rather
than the mean) then the MAPVAR parameter whould be used. [TRUE]



ZERO = _LOGICAL (Read)
``````````````````````
This parameter specifies whether DRIZZLE should attempt to adjust the
input data values by applying zero-point (i.e. additive) corrections
before combining them into a mosaic. This would be appropriate, for
instance, if a series of images had been obtained with differing
background (sky) values; to combine them without correction would
yield a mosaic with discontinuities at the image edges where the data
values differ.
If ZERO is set to TRUE, then DRIZZLE will ask the user for a
sequential file containing the corrections for each image (see the
CORRECT parameter). If none is supplied the program will attempt to
calculate its own corrections.
DRIZZLE will inter-compare the NDFs supplied as input and will
estimate the relative zero-point difference between selected pairs of
input data arrays where they overlap. From this information, a global
set of additive corrections will be derived which make the input data
as mutually consistent as possible. These corrections will be applied
to the input data before drizzling them onto the output frame.
Calculation of zero-point corrections may also be combined with the
use of scale-factor corrections (see the SCALE parameter). By default,
no zero-point corrections are applied. [FALSE]



{enter_further_parameters_here}
```````````````````````````````




Examples
~~~~~~~~
drizzle * out pixfrac=0.7
Drizzles a set of NDFs matching the wild-card "*" into a mosaic called
"out". The drop size of the input pixel is set to 0.7, i.e. it is
scaled to 70% of its orginal size before being drizzled onto the
output grid.
drizzle in=img* out=combined scale=true zero=true ref=! multi=4.0
Drizzles a set of NDFs matching the wild-card "img*" into a mosaic
called "combined". Both scaling and zero-point corrections are enabled
(the program will request a correction file), however no reference
image has been supplied (the program will use the first NDF supplied
in the input list). The multiplicative scaling factor between input
and output images is set to 4, i.e. the input pixel is 4 times larger
than the output pixel and contains 16 output pixels.
{enter_further_examples_here}




Notes
~~~~~
The file containing scale and zero-point corrections (see the CORRECT
parameter) must contain one line per frame having the following
information
INDEX SCALE ZERO
Where the fields have the following meaning:
INDEX = the index number of the frame, this must be the same as its
order number in the input list (see the IN parameter) SCALE = the
multiplicative scaling factor for the NDF ZERO = the zero-point
correction for the NDF
Comment lines may be added, but must be prefixed with a "#" character.


Algorithms Used
~~~~~~~~~~~~~~~
Taken from Fruchter et al., "A package for the reduction of dithered
undersampled images", in Casertano et al. (eds), HST Calibration
Workshop, STSCI, 1997, pp. 518-528
"The drizzle algorithm is conceptually straightforward. Pixels in the
original input images are mapped into pixels in the subsampled output
image, taking into account shifts and rotations between the images and
the optical distortion of the camera. However, in order to avoid
convolving the image with the larger pixel `footprint' of the camera,
we allow the user to shrink the pixel before it is averaged into the
output image.
The new shrunken pixels, or `drops', rain down upon the subsampled
output. In the case of the Hubble Deep Field (HDF), the drops used had
linear dimensions one-half that of the input pixel -- slightly larger
than the dimensions of the output subsampled pixels. The value of an
input pixel is averaged into the output pixel with a weight
proportional to the area of overlap between the `drop' and the output
pixel. Note that, if the drop size if sufficently small, not all
output pixels have data added to them from each input image. One must
therefore choose a drop size that is small enough to avoid degrading
the image, but large enough so that after all images are `dripped' the
coverage is fairly uniform.
The drop pize if controlled by a user-adjustable parameter called
PIXFRAC, which is simply the ratio of the linear size of the drop to
the input pixel (before any adjustment due to geometric distortion of
the camera). Thus interlacing is equivalent to setting PIXFRAC=0.0,
while shift-and-add is equivalent to PIXFRAC=1.0.
When a drop with value i_{xy} and a user-defined weight w_{xy} is
added to an image with pixel value I_{xy}, weight W_{xy}, and
fractional pixel overlap 0 < a_{xy} < 1, the resulting value the image
I'_{xy} and weight W'_{xy} is
W'_{xy} = a_{xy}w_[xy} + W_{xy}
I'_{xy} = a_{xy}i_{xy}w_{xy} + I_{xy}W_{xy}

+ -------------------------------- W'_{xy}

This algorithm has a number of advantages over standard linear
reconstruction methods presently used. Since the area of the pixels
scales with the Jacobian of the geometric distortion, drizzle
preserves both surface and absolute photometry. Therefore flux can be
measured using an aperture whose size is independent of position on
the chip. As the method anticipates that a given output pixel may
receive no information from a given input pixel, missing data (due for
instance to cosmic rays or detector defects) do not cause a
substantial problem, so long as there are enough dithered images to
fill in the gaps caused by these zero-weight input pixels. Finally the
linear weighting scheme is statistically optimum when inverse variance
maps are used as weights."


Pitfalls
~~~~~~~~
The format of the file containing scale and zero-point corrections
must be correct or the A-task will abort operations.


Copyright
~~~~~~~~~
Copyright (C) 1992 Science & Engineering Research Council Copyright
(C) 1998-1999 Central Laboratory of the Research Councils


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


+ All non-complex numeric data types are supported.
+ Bad pixels are supported.
+ The algorithm is restricted to handling 2D NDFs only.




