

FILLBAD
=======


Purpose
~~~~~~~
Removes regions of bad values from an NDF


Description
~~~~~~~~~~~
This application replaces bad values in a NDF with a smooth function
which matches the surrounding data. It can fill arbitrarily shaped
regions of bad values within n-dimensional arrays.
It forms a smooth replacement function for the regions of bad values
by forming successive approximations to a solution of Laplace's
equation, with the surrounding valid data providing the boundary
conditions.


Usage
~~~~~


::

    
       fillbad in out [niter] [size]
       



ADAM parameters
~~~~~~~~~~~~~~~



BLOCK = _INTEGER (Read)
```````````````````````
The maximum number of pixels along either dimension when the array is
divided into blocks for processing. It is ignored unless MEMORY=TRUE.
This must be at least 256. [512]



CNGMAX = _DOUBLE (Write)
````````````````````````
The maximum absolute change in output values which occurred in the
final iteration.



CNGRMS = _DOUBLE (Write)
````````````````````````
The root-mean-squared change in output values which occurred in the
last iteration.



IN = NDF (Read)
```````````````
The NDF containing the input image with bad values.



MEMORY = _LOGICAL (Read)
````````````````````````
If this is FALSE, the whole array is processed at the same time. If it
is TRUE, the array is divided into chunks whose maximum dimension
along an axis is given by parameter BLOCK. [FALSE]



NITER = INTEGER (Given)
```````````````````````
The number of iterations of the relaxation algorithm. This value
cannot be less than two, since this is the minimum number required to
ensure that all bad values are assigned a replacement value. The more
iterations used, the finer the detail in the replacement function and
the closer it will match the surrounding good data. [2]



OUT = NDF (Write)
`````````````````
The NDF to contain the image free of bad values.



SIZE( ) = _REAL (Read)
``````````````````````
The initial scale lengths in pixels to be used in the first iteration,
along each axis. If fewer values are supplied than pixel axes in the
NDF, the last value given is repeated for the remaining axes. The size
0 means no fitting across a dimension. For instance, [0,0,5] would be
appropriate if the spectra along the third dimension of a cube are
independent, and the replacement values are to be derived only within
each spectrum.
For maximum efficiency, a scale length should normally have a value
about half the `size' of the largest invalid region to be replaced.
(See the Notes section for more details.) [5.0]



TITLE = LITERAL (Read)
``````````````````````
The title of the output NDF. A null (!) value means using the title of
the input NDF. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
If VARIANCE is TRUE, variance information is to be propagated; any bad
values therein are filled. Also the variance is used to weight the
calculation of the replacement data values. If VARIANCE is FALSE,
there will be no variance processing thus requiring two less arrays in
memory. This parameter is only accessed if the input NDF contains a
VARIANCE component. [TRUE]



Examples
~~~~~~~~
fillbad aa bb
The NDF called aa has its bad pixels replaced by good values derived
from the surrounding good pixel values using two iterations of a
relaxation algorithm. The initial scale length is 5 pixels. The
resultant NDF is called bb.
fillbad aa bb 6 20 title="Cleaned image"
As above except the initial scale length is 20 pixels, 5 iterations
will be performed, and the output title is "Cleaned image" instead of
the title of NDF aa.
fillbad aa bb memory novariance
As in the first example except that processing is performed with
blocks up to 512 by 512 pixels to reduce the memory requirements, and
no variance information will be used or propagated.
fillbad in=speccube out=speccube_fill size=[0,0,128] iter=5
Suppose NDF speccube is a spectral imaging cube with the spectral axis
third. This example replaces the bad pixels by valid values derived
from the surrounding good pixel values within each spectrm, using an
initial scale length of 128 channels, iterating five times. The filled
NDF is called speccube_fill.
fillbad in=speccube out=speccube_fill size=[5,5,128] iter=5
As the previous example, but now the relaxation occurs along the
spatial axes too, initially with a scale length of five pixels.



Notes
~~~~~


+ The algorithm is based on the relaxation method of repeatedly
  replacing each bad pixel with the mean of its two nearest neighbours
  along each pixel axis. Such a method converges to the required
  solution, but information about the good regions only propagates at a
  rate of about one pixel per iteration into the bad regions, resulting
  in slow convergence if large areas are to be filled.

This application speeds convergence to an acceptable function by
forming the replacement mean from all the pixels in the same axis
(such as a row or a column), using a weight which decreases
exponentially with distance and goes to zero after the first good
pixel is encountered in any direction. If there is variance
information, this is included in the weighting so as to give more
weight to surrounding values with lower variance. The scale length of
the exponential weight is initially set large, to allow rapid
propagation of an approximate `smooth' solution into the bad regions
---an initially acceptable solution is thus rapidly obtained (often in
the first one or two iterations). The scale length is subsequently
reduced by a factor of 2 whenever the maximum absolute change
occurring in an iteration has decreased by a factor of 4 since the
current scale length was first used. In this way, later iterations
introduce progressively finer detail into the solution. Since this
fine detail occurs predominantly close to the `crinkly' edges of the
bad regions, the slower propagation of the solution in the later
iterations is then less important.
When there is variance processing the output variance is reassigned if
either the input variance or data value was bad. Where the input value
is good but its associated variance is bad, the calculation proceeds
as if the data value were bad, except that only the variance is
substituted in the output. The new variance is approximated as twice
the inverse of the sum of the weights.

+ The price of the above efficiency means that considerable workspace
is required, typically two or three times the size of the input image,
but even larger for the one and two-byte integer types. If memory is
at a premium, there is an option to process in blocks (cf. parameter
MEMORY). However, this may not give as good results as processing the
array in full, especially when the bad-pixel regions span blocks.
+ The value of the parameter SIZE is not critical and the default
value will normally prove effective. It primarily affects the
efficiency of the algorithm on various size scales. If the smoothing
scale is set to a large value, large scale variations in the
replacement function are rapidly found, while smaller scale variations
may require many iterations. Conversely, a small value will rapidly
produce the small scale variations but not the larger scale ones. The
aim is to select an initial value SIZE such that during the course of
a few iterations, the range of size scales in the replacement function
are all used. In practice this means that the value of SIZE should be
about half the size of the largest scale variations expected. Unless
the valid pixels are very sparse, this is usually determined by the
`size' of the largest invalid region to be replaced.
+ An error results if the input NDF has no bad values to replace.
+ The progress of the iterations is reported at the normal reporting
  level. The format of the output is slightly different if the scale
  lengths vary with pixel axis; an extra axis column is included.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CHPIX, GLITCH, MEDIAN, ZAPLIN; Figaro: BCLEAN, COSREJ, CLEAN,
ISEDIT, MEDFILT, MEDSKY, REMBAD, TIPPEX.


Timing
~~~~~~
The time taken increases in proportion to the value of NITER.
Adjusting the SIZE parameter to correspond to the largest regions of
bad values will reduce the processing time. See the Notes section.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1998-1999, 2001, 2004 Central Laboratory of the
Research Councils. All Rights Reserved.


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
supported. The output bad-pixel flag is set to indicate no bad values
in the data and variance arrays.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single- or double-precision floating point as
  appropriate.




