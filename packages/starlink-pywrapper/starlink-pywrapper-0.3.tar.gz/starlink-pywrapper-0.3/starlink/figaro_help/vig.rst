

VIG
===


Purpose
~~~~~~~
Correct for vignetting


Description
~~~~~~~~~~~
This routine accepts a sky or flat field IMAGE obtained at the same
filter for imaging , or at the same grating angle as a series of
spectra which need to be corrected for vignetting in 2D. Two
orthogonal one dimensional cuts through the 2D IMAGE are formed and
fitted with Chebyshev polynomials to form flattening functions on the
respective axes. The correction applied to the data is formed from the
product of the terms of each of these two series. Because the
correction IMAGES may include unwanted signals, such as sky lines the
users can specify regions of the data which may be excluded from the
fits. In practice rather actaully restructure the template cuts formed
in the two directions,by deleteing these data this is achieved by
ascribing them a very low weight in the fitting process. At the
current time it has been found that a wright of 1E-6 is an effective
way of elimanting such points.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) Name of image for input OLD = LOGICAL (Read) old
coefficients are to be used for correction OUTPUT = FILE (Write)
OUTput Name of output file OUTPUT is the name of the resulting image.
If OUTPUT is the same as INPUT the data in the input file will be
modified in situ.Otherwise a new file will be created. YSTART =
INTEGER (Read) start value to extract in channel direction The data
between the limits ystart and yend is extracted and the resultant
spectrum is used to find the vignetting in the channel direction. YEND
= INTEGER (Read) end value to extract in channel direction The data
between the limits ystart and yend is extracted and the resultant
spectrum is used to find the vignetting in the channel direction.
XSTART = INTEGER (Read) start value to extract in x-sect direction The
data between the limits xstart and xend is extracted and the resultant
spectrum is used to find the vignetting in the cross-section
direction. XEND = INTEGER (Read) end value to extract in x-sect
direction The data between the limits xstart and xend is extracted and
the resultant spectrum is used to find the vignetting in the cross-
section direction.


