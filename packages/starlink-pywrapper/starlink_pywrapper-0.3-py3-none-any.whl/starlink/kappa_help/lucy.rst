

LUCY
====


Purpose
~~~~~~~
Performs a Richardson-Lucy deconvolution of a 1- or 2-dimensional
array


Description
~~~~~~~~~~~
This application deconvolves the supplied 1- or 2-dimensional array
using the Richardson-Lucy (R-L) algorithm. It takes an array holding
observed data and another holding a Point-Spread Function (PSF) as
input and produces an output array with higher resolution. The
algorithm is iterative, each iteration producing a new estimate of the
restored array which (usually) fits the observed data more closely
than the previous estimate (in the sense that simulated data generated
from the restored array is closer to the observed data). The closeness
of the fit is indicated after each iteration by a normalised chi-
squared value (i.e. the chi-squared per pixel). The algorithm
terminates when the normalised chi-squared given by parameter AIM is
reached, or the maximum number of iterations given by parameter NITER
have been performed. The current estimate of the restored array is
then written to the output NDF.
Before the first iteration, the restored array is initialised either
to the array given by parameter START, or, if no array is given, to
the difference between the mean value in the input data array and the
mean value in the background (specified by parameters BACK and
BACKVAL). Simulated data is then created from this trial array by
smoothing it with the supplied PSF, and then adding the background on.
The chi-squared value describing the deviation of this simulated data
from the observed data is then found and displayed. If the required
chi-squared is not reached by this simulated data, the first iteration
commences, which consists of creating a new version of the restored
array and then creating new simulated data from this new restored
array (the corresponding chi-squared value is displayed). Repeated
iterations are performed until the required chi-squared is reached, or
the iteration limit is reached. The new version of the restored array
is created as follows.
1 - A correction factor is found for each data value. This is the
ratio of the observed data value to the simulated data value. An
option exists to use the Snyder modification as used by the LUCY
program in the STSDAS package within IRAF. With this option selected,
the variance of the observed data value is added to both the numerator
and the denominator when finding the correction factors.
2 - These correction factors are mapped into an array by smoothing the
array of correction factors with the transposed PSF.
3 - The current version of the restored array is multiplied by this
correction factor array to produce the new version of the restored
array.
For further background to the algorithm, see L. B. Lucy, Astron.J.
1974, Vol 79, No. 6.


Usage
~~~~~


::

    
       lucy in psf out [aim]
       



ADAM parameters
~~~~~~~~~~~~~~~



AIM = _REAL (Read)
``````````````````
The chi-squared value at which the algorithm should terminate. Smaller
values of AIM will result in higher apparent resolution in the output
array but will also cause noise in the observed data to be interpreted
as real structure. Small values will require larger number of
iterations, so NITER may need to be given a larger value. Very-small
values may be completely un-achievable, indicated by chi-squared not
decreasing (or sometimes increasing) between iterations. Larger values
will result in smoother output arrays with less noise. [1.0]



BACK = NDF (Read)
`````````````````
An NDF holding the background value for each observed data value. If a
null value is supplied, a constant background value given by parameter
BACKVAL is used. [!]



BACKVAL = _REAL (Read)
``````````````````````
The constant background value to use if BACK is given a null value.
[0.0]



CHIFAC = _REAL (Read)
`````````````````````
The normalised chi-squared value which is used to determine if the
algorithm should terminate is the mean of the following expression
(the mean is taken over the entire input array, the margins used to
pad the input array are excluded):
( D - S )**2 / ( CHIFAC*S - V )
where D is the observed data value, S is the simulated data value
based on the current version of the restored array, V is the variance
of the error associated with D, and CHIFAC is the value of parameter
CHIFAC. Using 0 for CHIFAC results in the standard expression for chi-
squared. However, the algorithm sometimes has difficulty fitting
bright features and so may not reach the required normalised chi-
squared value. Setting CHIFAC to 1 (as is done by the LUCY program in
the STSDAS package within IRAF) causes larger data values to be given
less weight in the chi-squared calculation, and so encourages lower
chi-squared values. [1.0]



IN= NDF (Read)
``````````````
The input NDF containing the observed data.



NITER = _INTEGER (Read)
```````````````````````
The maximum number of iterations to perform. [50]



OUT = NDF (Write)
`````````````````
The restored output array. The background specified by parameters BACK
and BACKVAL will have been removed from this array. The output is the
same size as the input. There is no VARIANCE component in the output,
but any QUALITY values are propagated from the input to the output.



PSF = NDF (Read)
````````````````
An NDF holding an estimate of the Point-Spread Function (PSF) of the
input array. This could, for instance, be produced using the KAPPA
application `PSF'. There should be no bad pixels in the PSF otherwise
an error will be reported. The PSF can be centred anywhere within the
array, but the location of the centre must be specified using
parameters XCENTRE and YCENTRE. The PSF is assumed to have the value
zero outside the supplied NDF.



SIGMA = _REAL (Read)
````````````````````
The standard deviation of the noise in the observed data. This is only
used if parameter VARIANCE is given the value FALSE. If a null (!)
value is supplied, the value used is an estimate of the noise based on
the difference between adjacent pixel values in the observed data. [!]



START = NDF (Read)
``````````````````
An NDF containing an initial guess at the restored array. This could,
for instance, be the output from a previous run of LUCY, in which case
the deconvolution would continue from the point it had previously
reached. If a null value is given, then the restored array is
initialised to a constant value equal to the difference between the
mean observed data value and the mean background value. [!]



SNYDER = _LOGICAL (Read)
````````````````````````
If TRUE then the variance of the observed data sample is added to both
the numerator and denominator when evaluating the correction factor
for each data sample. This is the modified form of the R-L algorithm
used by the LUCY program in the STSDAS package within IRAF. [TRUE]



THRESH = _REAL (Read)
`````````````````````
The fraction of the PSF peak amplitude at which the extents of the PSF
are determined. These extents are used to determine the size of the
margins used to pad the supplied input array. Lower values of THRESH
will result in larger margins being used. THRESH must be positive and
less than 0.5. [0.0625]



TITLE = LITERAL (Read)
``````````````````````
A title for the output NDF. A null (!) value means using the title of
the input NDF. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
If TRUE, then the variance of each input data sample will be obtained
from the VARIANCE component of the input NDF. An error is reported if
this option is selected and the NDF has no VARIANCE component. If
FALSE, then a constant variance equal to the square of the value given
for parameter SIGMA is used for all data samples. If a null (!) value
is supplied, the value used is TRUE if the input NDF has a VARIANCE
component, and FALSE otherwise. [!]



WLIM = _REAL (Read)
```````````````````
If the input array contains bad pixels, then this parameter may be
used to determine the number of good data values which must contribute
to an output pixel before a valid value is stored in the restored
array. It can be used, for example, to prevent output pixels from
being generated in regions where there are relatively few good data
values to contribute to the restored result. It can also be used to
`fill in' small areas (i.e. smaller than the PSF) of bad pixels.
The numerical value given for WLIM specifies the minimum total weight
associated with the good pixels in a smoothing box required to
generate a good output pixel (weights for each pixel are defined by
the normalised PSF). If this specified minimum weight is not present,
then a bad output pixel will result, otherwise a smoothed output value
will be calculated. The value of this parameter should lie between 0.0
and 1.0. WLIM=0 causes a good output value to be created even if there
is only one good input value, whereas WLIM=1 causes a good output
value to be created only if all input values are good. Values less
than 0.5 will tend to reduce the number of bad pixels, whereas values
larger than 0.5 will tend to increase the number of bad pixels.
This threshold is applied each time a smoothing operation is
performed. Many smoothing operations are typically performed in a run
of LUCY, and if WLIM is larger than 0.5 the effects of bad pixels will
propagate further through the array at each iteration. After several
iterations this could result in there being no good data left. An
error is reported if this happens. [0.001]



XCENTRE = _INTEGER (Read)
`````````````````````````
The x pixel index of the centre of the PSF within the supplied PSF
array. If a null (!) value is supplied, the value used is the middle
pixel (rounded down if there are an even number of pixels per line).
[!]



YCENTRE = _INTEGER (Read)
`````````````````````````
The y pixel index of the centre of the PSF within the supplied PSF
array. If a null (!) value is supplied, the value used is the middle
line (rounded down if there are an even number of lines). [!]



Examples
~~~~~~~~
lucy m51 star m51_hires
This example deconvolves the array in the NDF called m51, putting the
resulting array in the NDF called m51_hires. The PSF is defined by the
array in NDF star (the centre of the PSF is assumed to be at the
central pixel). The deconvolution terminates when a normalised chi-
squared value of 1.0 is reached.
lucy m51 star m51_hires 0.5 niter=60
This example performs the same function as the previous example,
except that the deconvolution terminates when a normalised chi-squared
value of 0.5 is reached, giving higher apparent resolution at the
expense of extra spurious noise-based structure. The maximum number of
iterations is increased to 60 to give the algorithm greater
opportunity to reach the reduced chi-squared value.
lucy m51 star m51_hires2 0.1 start=m51_hires
This example continues the deconvolution started by the previous
example in order to achieve a normalised chi-squared of 0.1. The
output array from the previous example is used to initialise the
restored array.



Notes
~~~~~


+ The convolutions required by the R-L algorithm are performed by the
multiplication of Fourier transforms. The supplied input array is
extended by a margin along each edge to avoid problems of wrap-around
between opposite edges of the array. The width of this margin is about
equal to the width of the significant part of the PSF (as determined
by parameter THRESH). The application displays the width of these
margins. The margins are filled by replicating the edge pixels from
the supplied input NDFs.
+ The R-L algorithm works best for arrays which have zero background.
  Non-zero backgrounds cause dark rings to appear around bright, compact
  sources. To avoid this a background array should be created before
  running LUCY and assigned to the parameter BACK. The SEGMENT and
  SURFIT applications within KAPPA can be used to create such a
  background array.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FOURIER, MEM2D, WIENER.


Copyright
~~~~~~~~~
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDF and
propagates all extensions.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using single-precision floating point.




