

POLSTACK
========


Purpose
~~~~~~~
Stack a set of intensity images


Description
~~~~~~~~~~~
This application combines a set of intensity images into a smaller
number of similar intensity images (it may also be used to combine
intensity cubes containing spectropolarimetry data). The input images
must all be aligned pixel-for-pixel. Each output image corresponds to
a range of analysis angle, and is formed by stacking together the
input images which have analysis angles within the range of the output
image. The variance component of each output image is set to hold the
standard error of the input images which contribute to the output
image. The output images may, for instance, be processed by POLCAL. In
addition, a 3D (or 4D if processing spectropolarimetry data) stack may
be created containing all the output images in a single data array -
see parameter STACK.
The same reference direction in used for all output images, and is
equal to the reference direction in the first input image. For each
input image, the anti-clockwise angle from this reference direction to
the effective analyser position is found. These analysis angles are
then sorted into bins of size given by parameter BIN. The first bin
extends from the analysis angle given by parameter ORIGIN (typically
zero) to the value (ORIGIN+BIN). The second bin extends from
(ORIGIN+BIN) to (ORIGIN+2*BIN), etc. If parameter TWOPI is FALSE, the
number of bins used is chosen so that they cover a range of ORIGIN to
(180+ORIGIN) degrees, and input images with analysis angles outside
this range are mapped into the range by subtracting (or adding) a
multiple of 180 degrees. If parameter TWOPI is TRUE, the number of
bins used is chosen so that they cover a range of ORIGIN to
(360+ORIGIN) degrees, and input images with analysis angles outside
this range are mapped into the range by subtracting (or adding) a
multiple of 360 degrees.
An output image is produced for each bin containing more than the
minimum required number of images specified by parameter MININ. The
output DATA value at each pixel is the mean of the corresponding
pixels in the input images which fall within the range of analysis
angles covered by the output image. A VARIANCE component is added to
the output image in which each pixel contains the standard error of
the corresponding input pixels. If there are less than 2 good input
pixel values, then the VARIANCE value is set bad.
Each output image contains a POLPACK extension in which the ANLANG
value (which specifies the analysis angle) is set to the mean of the
analysis angles for the corresponding input images. This mean value
refers to the output reference direction which is inherited from the
first input NDF.


Usage
~~~~~


::

    
       polstack in out [bin]
       



ADAM parameters
~~~~~~~~~~~~~~~



BIN = _REAL (Read)
``````````````````
The size of each analysis angle bin, in degrees. The run-time default
is the current value, or 10 degrees if there is no current value. []



MSG_FILTER = _CHAR (Read)
`````````````````````````
Controls the amount of information displayed on the screen while the
program is executing. A value of QUIET suppresses all information. A
value of NORM results in a summary of each output image being
displayed. A value of DEBUG additionally gives details of the input
images, and further details of each output image. [NORM]



IN = NDF (Read)
```````````````
A group specifying the names of the input intensity images or cubes.
This may take the form of a comma separated list, or any of the other
forms described in the help on "Group Expressions". These images must
be aligned pixel-for-pixel.



MININ = _INTEGER (Read)
```````````````````````
The minimum number of input images required to create an output image.
If any bin contains fewer than this many input images, no output image
will be created for the bin. The run-time default is the current
value, or 3 if there is no current value. []



ORIGIN = _REAL (Read)
`````````````````````
The analysis angle at the start of the first bin, in degrees. The run-
time default is the current value, or 0.0 if there is no current
value. []



OUT = NDF (Read)
````````````````
A group specifying the names of the output intensity images or cubes.
If the supplied string includes an asterisk (*) it is replaced by an
integer sequence number ranging from 1 to the number of output images.
The sequence number increases monotonically with analyser position.



STACK = NDF (Write)
```````````````````
An optional 3-dimensional (or 4-dimensional when dealing with
spectropolarimetry data) output cube. If created, each plane (or cube)
contains a copy of the output image (or cube) with the same sequence
number (see parameter OUT). The analyser position corresponding to
each plane is stored in the Axis structure for the last axis. No
POLPACK extension is created. The stack is not created if a null (!)
value is supplied. [!]



TWOPI = _LOGICAL (Read)
```````````````````````
If TRUE, then the range of analysis angles covered by the bins is 360
degrees, instead of 180 degrees. [FALSE]



Examples
~~~~~~~~
polstack "*_A" "bin*" 10
The intensity images specified by "*_A" are binned into a set of
intensity images each covering a range of 10 degrees of analysis
angle. These output images are called "bin1", "bin2", etc.



Notes
~~~~~


+ Any transmission (T) or efficiency (EPS) values in the POLPACK
extensions of the input images are ignored. The output images will not
contain any T or EPS values and so default values of 1.0 will be used
for both when POLCAL is run.
+ Any FILTER or IMGID values in the POLPACK extensions of the input
images are ignored. The output images will not contain any FILTER or
IMGID values.
+ Any VARIANCE components in the input images are ignored.




Copyright
~~~~~~~~~
Copyright (C) 1999, 2001 Central Laboratory of the Research Councils
Copyright (C) 2009 Science & Technology Facilities Council. All Rights
Reserved.


