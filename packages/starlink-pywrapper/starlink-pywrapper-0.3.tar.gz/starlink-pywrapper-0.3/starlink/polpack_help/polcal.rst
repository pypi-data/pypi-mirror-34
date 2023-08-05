

POLCAL
======


Purpose
~~~~~~~
Converts a set of analysed intensity images into a cube holding Stokes
vectors


Description
~~~~~~~~~~~
This application converts a set of input NDFs holding analysed
intensity, into an output NDF holding a Stokes vector at every pixel
in the supplied input NDFs. If the input NDFs are 2-dimensional
images, the output NDF will be 3-dimensional. If the input NDFs are
3-dimensional cubes (spectropolarimetry data for instance), the output
NDF will be 4-dimensional.
Either dual or single beam data can be processed, with an appropriate
algorithm being used in each case. There is also an option to process
dual-beam data using the single beam algorithm (see parameter
DUALBEAM).
All the input images should be aligned pixel-for-pixel, and should
have had the sky background removed. O and E ray images in dual-beam
data should have been extracted into separate images. If the input
arrays are 3D, the first two pixels axes must be the spatial axes, and
all planes within each input cube must be spatially aligned.
Corresponding 2D planes within 3D input cubes are processed
independently of each other, using the same algorithm used for 2D
input images.
The final axis in the output array corresponds to Stokes parameter and
has bounds 1:3 (this will be axis 3 if the inputs are 2D or axis 4 if
the inputs are 3D). Axis values 1, 2 and 3 correspond to I, Q and U
respectively. Currently, circular polarimetry can only be performed by
the dual-beam algorithm, in which case the final axis of the output
has bounds 1:2, corresponding to I and V values (see parameter PMODE).


Usage
~~~~~


::

    
       polcal in out
       



ADAM parameters
~~~~~~~~~~~~~~~



DEZERO = _LOGICAL (Read)
````````````````````````
This parameter is only accessed by the single-beam algorithm when
parameter WEIGHTS is set to 3. If TRUE, a constant value is added to
the data values read from each input data array to correct for any
differences in zero points. The constant value used for each input
array is chosen so that the residuals between the input array and the
corresponding intensity values implied by the Stokes vectors produced
on the previous iteration, have a mean value of zero. Set MSG_FILTER
to DEBUG or ALL to see the values used. Selecting the DEZERO option
can reduce the variances in the output cube, but usually slows down
convergence of the iterative procedure. Thus you may have to give a
larger value for parameter MAXIT, resulting in significantly longer
run time. [FALSE]



DUALBEAM = _LOGICAL (Read)
``````````````````````````
If TRUE, then the input images are processed as dual-beam data. If
FALSE they are processed as single-beam data. If a null (!) value is
supplied, the dual-beam algorithm is used if all the input images
contain a legal value for the RAY item in the POLPACK extension (i.e.
either "E" or "O"). Otherwise, the single-beam algorithm is used. It
is possible to process dual-beam data using the single-beam algorithm,
so DUALBEAM may be set to FALSE even if the input images hold dual-
beam data. However, the opposite is not true; the application will
abort if DUALBEAM is set TRUE and any of the input images contain
single-beam data. [!]



ETOL = _REAL (Read)
```````````````````
This parameter is only accessed by the dual-beam algorithm. The E
factors are found using an iterative procedure in which the supplied
intensity images are corrected using the current estimates of the E
factors, and new estimates are then calculated on the basis of these
corrected images. This procedure continues until the change in
E-factor produced by an iteration is less than the value supplied for
ETOL, or the maximum number of iterations specified by parameter MAXIT
is reached. [0.01]



MSG_FILTER = _CHAR (Read)
`````````````````````````
Specifies the amount of information to display on the screen. QUIET
suppresses all output. A value of NORM produces minimal output
describing such things as warnings and the E and F factors adopted (in
dual-beam mode). A value of VERBOSE produces more verbose output
including details of each iteration in the iterative processes used by
both dual and single-beam modes. A value of DEBUG produces additional
details about each individual input image in single-beam mode. [NORM]



IN = NDF (Update)
`````````````````
A group specifying the names of the input intensity images or cubes.
This may take the form of a comma separated list, or any of the other
forms described in the help on "Group Expressions". Read access only
is required unless the SETVAR parameter is assigned a TRUE value.



MAXIT = _INTEGER (Read)
```````````````````````
This parameter is accessed by both single and dual-beam algorithm, but
is used slightly differently in each case.
In dual-beam mode, it specifies the maximum number of iterations to be
used when inter-comparing pairs of input images to determine their
relative scale-factor and/or zero-point. If the specified number of
iterations is exceeded without achieving the accuracy required by the
settings of the TOLS and TOLZ parameters, then a warning message will
be issued, but the results will still be used. The value given for
MAXIT must be at least one. The runtime default value is 30.
In single-beam mode, it specifies the maximum number of iterations to
be used when estimating input variances or rejecting aberrant input
values. The default value depends on the value supplied for parameter
WEIGHTS. If WEIGHTS indicates that estimates of the input variances
are to be made (i.e. if WEIGHTS has the value 2 or 3), then the
default value is 8. Otherwise, if variances in the input NDFs are to
be used (i.e. if WEIGHTS is 1), the default is zero. This is because
each iteration is a computationally expensive process, and so
iterations should only be performed if they are really necessary.
MAXIT is always fixed at zero if WEIGHTS is 4 (i.e. if all input data
are given constant weight). See also parameter TOLR. []



MINFRAC = _REAL (Read)
``````````````````````
This parameter is only accessed by the single-beam algorithm when
iteratively rejecting input values (i.e. if MAXIT is greater than
zero). It controls how much good input data is required to form a good
output pixel. It is given as a fraction in the range 0 to 1. The
minimum number of good input values required to form a good output
value at a particular pixel is equal to this fraction multiplied by
the number of input NDFs which have good values for the pixel. The
number is rounded to the nearest integer and limited to at least 3. If
MSG_FILTER is greater than NORM, then the percentage of output pixels
which fail this test is displayed. [0.0]



NSIGMA = _REAL (Read)
`````````````````````
This parameter is only accessed by the single-beam algorithm. It
specifies the threshold at which to reject input data values. If an
input data value differs from the data value implied by the current I,
Q and U values by more than NSIGMA standard deviations, then it will
not be included in the next calculation of I, Q and U. [3.0]



OUT = NDF (Read)
````````````````
The name of the output 3D or 4D cube holding the Stokes parameters.
The x-y plane of this cube covers the overlap region of the supplied
intensity images (but see parameter TRIMBAD). Pixel 1 on the final
axis contains the total intensity. The others contain either Q and U,
or V, depending on the value of parameter PMODE.



PMODE = LITERAL (Read)
``````````````````````
This parameter is only accessed by the dual-beam algorithm. It gives
the mode of operation; CIRCULAR for measuring circular polarization,
or LINEAR for measuring linear polarization. In circular mode, the
only legal values for the POLPACK extension item "WPLATE" are 0.0 and
45.0. Currently, the single-beam algorithm can only perform linear
polarimetry. [LINEAR]



SETVAR = _REAL (Read)
`````````````````````
This parameter is only accessed by the single-beam algorithm. If a
TRUE value is supplied for SETVAR, and if the variances in the input
images are being estimated (see parameter WEIGHTS), then the final
mean variance estimate found for each input image will be stored as a
constant value in the VARIANCE component of the input image. [FALSE]



SKYSUP = _REAL (Read)
`````````````````````
This parameter is only accessed by the dual-beam algorithm. It is a
positive "sky noise suppression factor" used to control the effects of
sky noise when pairs of input images are inter-compared to determine
their relative scale-factor. It is intended to prevent the resulting
scale-factor estimate being biased by the many similar values present
in the "sky background" of typical astronomical data. SKYSUP controls
an algorithm which reduces the weight given to data where there is a
high density of points with the same value, in order to suppress this
effect.
A SKYSUP value of unity can often be effective, but a value set by the
approximate ratio of sky pixels to useful object pixels (i.e. those
containing non-sky signal) in a "typical" image will usually be
better. The precise value is not critical. A value of zero disables
the sky noise suppression algorithm completely. The default value for
SKYSUP is 10. This is normally reasonable for CCD frames of extended
objects such as galaxies, but a larger value, say 100, may give
slightly better results for star fields. [10]



SMBOX = _INTEGER (Read)
```````````````````````
This parameter is only accessed by the single-beam algorithm. It
specifies the size (in pixels) of the smoothing box to use when
estimating the variance of the input data. It is only accessed if
parameter WEIGHTS is given the value 2 or 3 (i.e. if input variances
are to be estimated from the spread of the input data values).
The error of a given input intensity value can be estimated in two
ways, by its deviation from the sine curve connecting analysed
intensity and analyser position, or from its deviation from its local
neighbours. The second method requires a spatial smoothing to be
performed, the size of which is specified by SMBOX. However, spatial
smoothing can introduce problems because it can cause spatial
structure in the image to be interpreted as noise, resulting in over-
estimates of the input variances. For this reason it is best to use a
small smoothing size. If you have data for many analyser positions
(say 8 or more) you could even set SMBOX to zero in order to prevent
any spatial smoothing being performed. In this case, the errors are
based purely on deviations from the expected sine curves. If you do
not have this many analyser positions, you should use some spatial
smoothing. For instance if you only had data for three analyser
positions (the minimum possible number), then the sine curves would
fit the supplied data exactly, no matter what the noise may be, and
would consequently give no information about the input variances. In
this case, a larger value of SMBOX (say 9) may be necessary. [3]



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. [Output from POLCAL]



TOLR = _INTEGER (Read)
``````````````````````
This parameter is only accessed by the single-beam algorithm. It
specifies the convergence criterion for the iterative process which
estimates the input variances, and rejects bad input values. If the
number of pixels rejected from any input NDF changes by more than TOLR
pixels between two successive iterations, then the process is assumed
not to have converged and another iteration will be performed unless
MAXIT iterations have already been performed. [0]



TOLS = _REAL (Read)
```````````````````
This parameter is only accessed by the dual-beam algorithm. It defines
the accuracy tolerance to be achieved when inter-comparing pairs of
input images to determine their relative scale-factor. The value given
for TOLS specifies the tolerable fractional error in the estimation of
the relative scale-factor between any pair of input NDFs. This value
must be positive. [0.001]



TOLZ = _REAL (Read)
```````````````````
This parameter is only accessed by the dual-beam algorithm. It defines
the accuracy tolerance to be achieved when inter-comparing pairs of
input images to determine their relative zero-points. The value given
for TOLZ specifies the tolerable absolute error in the estimation of
the relative zero-point between any pair of input images whose
relative scale-factor is unity. The value used is multiplied by the
relative scale-factor estimate (which reflects the fact that an image
with a larger data range can tolerate a larger error in estimating its
zero-point). The TOLS value supplied must be positive. [0.05]



TRIMBAD = _LOGICAL (Read)
`````````````````````````
If a TRUE value is supplied, the bounds of the output data are trimmed
to remove any margins of bad pixels round the data. [FALSE]



VARIANCE = _LOGICAL (Read)
``````````````````````````
This parameter should be set to a TRUE value if variances are to be
included in the output cube. A null (!) value results in variance
values being created if possible, but not otherwise. [!]



WEIGHTS = _INTEGER (Read)
`````````````````````````
This parameter is only accessed by the single-beam algorithm. It
indicates how the weight and variance associated with each input
intensity value should be chosen. It should be an integer in the range
1 to 4. These values select the following schemes:


+ 1 -- Use the variances supplied with the input images. The
reciprocal of these variances are used as weights. If any input images
do not have associated variances then a constant weight of 1.0 will be
used for all input images.
+ 2 -- Use the variances supplied with the input images. If any input
images do not have associated variances then estimates of the
variances are made for all input images based on the spread of data
values. The reciprocal of these variances are used as weights. An
error will be reported if parameter MAXIT is set to zero, thus
preventing the iterative estimation of input variances.
+ 3 -- Use estimates of the variances for all input images based on
the spread of data values. The reciprocal of these variances are used
as weights. Any variances supplied with the input images are ignored.
An error will be reported if parameter MAXIT is set to zero, thus
preventing the iterative estimation of input variances.
+ 4 -- Use a constant weight of 1.0 for all input images. Any
  variances supplied with the input images are ignored. The iterative
  rejection of bad input values controlled by parameter MAXIT and TOLR
  is not available in this mode.

The dual-beam algorithm always uses scheme 1. [1]



Examples
~~~~~~~~
polcal "*_O,*_E" stokes
This example uses all images in the current directory which have file
names ending with either "_O" or "_E", and stores the corresponding I,
Q and U values in the 3d cube "stokes". These images contain dual-beam
data (indicated by the presence of the RAY item in the POLPACK
extension), and so the dual-beam algorithm is used.
polcal "*_O,*_E" stokes nodualbeam
As above, but the data is processed as if it were single-beam data.



Notes
~~~~~


+ An item named STOKES is added to the POLPACK extension. It is a
character string identifying the quantity stored in each plane of the
cube. For linear polarimetry, it is set to "IQU", and for circular
polarimetry it is set to "IV".
+ The reference direction for the Stokes vectors and polarization
vectors in the output NDF will be north if the first input NDF has a
celestial co-ordinate Frame within its WCS information. Otherwise, the
reference direction will be the second pixel axis. The POLANAL Frame
in the WCS component of the output NDF is updated to describe the new
reference direction. Angles are always measured positive in the same
sense as rotation from the first image axis (X) to the second image
axis (Y) (this will be equivalent to rotation from north through east
if the image has conventional WCS information).
+ WCS and AXIS components are propagated from the first supplied input
  image to the output cube.




The Single-beam Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~
In single-beam mode, the I, Q and U values at each output pixel are
chosen to minimise the sum of the squared residuals between the
supplied intensity values and the intensity values implied by the I, Q
and U values (this is equivalent to fitting sine curves to the input
intensity values). Input intensity values are weighted according to
the scheme chosen using parameter WEIGHTS. The basic algorithm is
described by Sparks and Axon (submitted to P.A.S.P.).
Single-beam mode can take account of imperfections in the analyser.
The transmission (i.e. the overall throughput) and efficiency (i.e.
the ability to reject light polarized across the axis) of the analyser
are read from the POLPACK extension. If not found, values of 1.0 are
used for both. These values are appropriate for a perfect analyser. A
perfectly bad analyser (a piece of high quality glass for instance)
would have a transmission of 2.0 and an efficiency of zero. The
extension items named T and EPS hold the transmission and efficiency.
Single-beam mode can handle data taken by polarimeters containing a
number of fixed analysers, or a single rotating analyser, in addition
to the normal combination of fixed analyser and rotating half-wave
plate. The POLPACK extension in each input NDF should contain either a
WPLATE value (giving the angle between a fixed analyser and the half-
wave plate), or an ANLANG value (giving the angle between the rotating
or fixed analyser and the polarimeter reference direction). Only one
of these two extension items should be present. The WPLATE and ANLANG
items are free to take any value (i.e. they are not restricted to the
values 0.0, 22.5, 45.0 and 67.5 degrees as in the dual-beam
algorithm).
If the input intensity NDFs do not contain usable variances, then


