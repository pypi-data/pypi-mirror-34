

FFCLEAN
=======


Purpose
~~~~~~~
Removes defects from a substantially flat one-, two- or three-
dimensional NDF


Description
~~~~~~~~~~~
This application cleans a one- or two-dimensional NDF by removing
defects smaller than a specified size. In addition, three-dimensional
NDFs can be cleaned by processing each row or plane within it using
the one- or two-dimensional algorithm (see parameter AXES).
The defects are flagged with the bad value. The defects are found by
looking for pixels that deviate from the data's smoothed version by
more than an arbitrary number of standard deviations from the local
mean, and that lie within a specified range of values. Therefore, the
spectrum or image must be substantially flat. The data variances
provide the local-noise estimate for the threshold, but if these are
not available a variance for the whole of the spectrum or image is
derived from the mean squared deviations of the original and smoothed
versions. The smoothed version of the image is obtained by block
averaging over a rectangular box. An iterative process progressively
removes the outliers from the image.


Usage
~~~~~


::

    
       ffclean in out clip box [thresh] [wlim]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES( 2 ) = _INTEGER (Read)
```````````````````````````
The indices of up to two axes that span the rows or planes that are to
be cleaned. If only one value is supplied, then the NDF is processed
as a set of one-dimensional spectra parallel to the specified pixel
axis. If two values are supplied, then the NDF is processed as a set
of two-dimensional images spanned by the given axes. Thus, a two-
dimensional NDF can be processed either as a single two-dimensional
image or as a set of one-dimensional spectra. Likewise, a three-
dimensional NDF can be processed either as a set of two-dimensional
images or a set of one-dimensional spectra. By default, a two-
dimensional NDF is processed as a single two-dimensional image, and a
three-dimensional NDF is processed as a set of one-dimensional spectra
(the spectral axis is chosen by examining the WCS component---pixel-
axis 1 is used if the current WCS frame does not contain a spectral
axis). []



BOX( 2 ) = _INTEGER (Read)
``````````````````````````
The x and y sizes (in pixels) of the rectangular box to be applied to
smooth the image. If only a single value is given, then it will be
duplicated so that a square filter is used except where the image is
one-dimensional for which the box size along the insignificant
dimension is set to 1. The values given will be rounded up to positive
odd integers if necessary.



CLIP( ) = _REAL (Read)
``````````````````````
The number of standard deviations for the rejection threshold of each
iteration. Pixels that deviate from their counterpart in the smoothed
image by more than CLIP times the noise are made bad. The number of
values given specifies the number of iterations. Values should lie in
the range 0.5--100. Up to one hundred values may be given. [3.0, 3.0,
3.0]



GENVAR = _LOGICAL (Read)
````````````````````````
If TRUE, the noise level implied by the deviations from the local mean
over the supplied box size are stored in the output VARIANCE
component. This noise level has a constant value over the whole NDF
(or over each section of the NDF if the NDF is being processed in
sections---see Parameter AXES). This constant noise level is also
displayed on the screen if the current message-reporting level is at
least NORMAL. If GENVAR is FALSE, then the output variances will be
copied from the input variances (if the input NDF has no variances,
then the output NDF will not have any variances either). [FALSE]



IN = NDF (Read)
```````````````
The one- or two-dimensional NDF containing the input image to be
cleaned.



OUT = NDF (Write)
`````````````````
The NDF to contain the cleaned image.



SIGMA = _DOUBLE (Write)
```````````````````````
The estimation of the RMS noise per pixel of the output image. If the
NDF is processed in sections (see parameter AXES), then the value
stored in this output parameter refers to the final section processed.



THRESH( 2 ) = _DOUBLE (Read)
````````````````````````````
The range between which data values must lie if cleaning is to occur.
Thus it is possible to clean the background without removing the cores
of images by a judicious choice of these thresholds. If null, !, is
given, then there is no limit on the data range. [!]



TITLE = LITERAL (Read)
``````````````````````
The title of the output NDF. A null (!) value means using the title of
the input NDF. [!]



WLIM = _REAL (Read)
```````````````````
If the input image contains bad pixels, then this parameter may be
used to determine the number of good pixels which must be present
within the smoothing box before a valid output pixel is generated. It
can be used, for example, to prevent output pixels from being
generated in regions where there are relatively few good pixels to
contribute to the smoothed result.
By default, a null (!) value is used for WLIM, which causes the
pattern of bad pixels to be propagated from the input image to the
output image unchanged. In this case, smoothed output values are only
calculated for those pixels which are not bad in the input image.
If a numerical value is given for WLIM, then it specifies the minimum
fraction of good pixels which must be present in the smoothing box in
order to generate a good output pixel. If this specified minimum
fraction of good input pixels is not present, then a bad output pixel
will result, otherwise a smoothed output value will be calculated. The
value of this parameter should lie between 0.0 and 1.0 (the actual
number used will be rounded up if necessary to correspond to at least
1 pixel). [!]



Examples
~~~~~~~~
ffclean dirty clean \
The NDF called dirty is filtered such that pixels that deviate by more
than three standard deviations from the smoothed version of dirty are
rejected. Three iterations are performed. Each pixel in the smoothed
image is the average of the neighbouring nine pixels. The filtered NDF
is called clean.
ffclean out=clean in=dirty thresh=[-100,200]
As above except only those pixels whose values lie between -100 and
200 can be cleaned.
ffclean poxy dazed [2.5,2.8] [5,5]
The two-dimensional NDF called poxy is filtered such that pixels that
deviate by more than 2.5 then 2.8 standard deviations from the
smoothed version of poxy are rejected. The smoothing is an average of
a 5-by-5-pixel neighbourhood. The filtered NDF is called dazed.



Notes
~~~~~


+ There are different facts reported, their verbosity depending on the
  current message-reporting level set by environment variable
  MSG_FILTER. When the filtering level is at least as verbose as NORMAL,
  the application will report the intermediate results after each
  iteration during processing. In addition, it will report the section
  of the input NDF currently being processed (but only if the NDF is
  being processed in sections---see Parameter AXES).




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CHPIX, FILLBAD, GLITCH, MEDIAN, MSTATS, ZAPLIN; Figaro: BCLEAN,
COSREJ, CLEAN, ISEDIT, MEDFILT, MEDSKY, TIPPEX.


Copyright
~~~~~~~~~
Copyright (C) 1981, 1990-1992 Science & Engineering Research Council.
Copyright (C) 1995, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2008, 2009 Science & Technology Facilities Council. All
Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of an NDF data
structure and propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single- or double-precision floating point as
  appropriate.




