

FOURIER
=======


Purpose
~~~~~~~
Performs forward and inverse Fourier transforms of 1- or 2-dimensional
NDFs


Description
~~~~~~~~~~~
This application performs forward or reverse Fast Fourier Transforms
(FFTs) of 1- or 2-dimensional NDFs. The output in the forward
transformation (from the space domain to the Fourier) can be produced
in Hermitian form in a single NDF, or as two NDFs giving the real and
imaginary parts of the complex transform, or as two NDFs giving the
power and phase of the complex transform. Any combination of these may
also be produced. The inverse procedure accepts any of these NDFs and
produces a purely real output NDF.
Any bad pixels in the input NDF may be replaced by a constant value.
Input NDFs need neither be square, nor be a power of 2 in size in
either dimension; their shape is arbitrary.
The Hermitian transform is a single image in which each quadrant
consists of a linear combination of the real and imaginary parts of
the transform. This form is useful if you just want to multiply the
Fourier transform by some known purely real mask and then invert it to
get a filtered image. However, if you want to multiply the Fourier
transform by a complex mask (e.g. the Fourier transform of another
NDF), or do any other operation involving combining complex values,
then the Hermitian NDF must be untangled into separate real and
imaginary parts.
There is an option to swap the quadrants of the input NDF around
before performing a forward FFT. This is useful if you want to perform
convolutions with the FFTs, since the point-spread function (PSF)
image can be created with the PSF centre at the array centre, rather
than at pixel (1,1) as is usually required.


Usage
~~~~~


::

    
       fourier in hermout
       



ADAM parameters
~~~~~~~~~~~~~~~



FILLVAL = LITERAL (Read)
````````````````````````
A value to replace bad pixels before performing the transform. The
input image is also padded with this value if necessary to form an
image of acceptable size. A value of "Mean" will cause the mean value
in the array to be used. [0.0]



HERMIN = NDF (Read)
```````````````````
Hermitian frequency-domain input NDF containing the complex transform.
If null is entered no Hermitian NDF is read and then the application
should be supplied either separate real and imaginary NDFs, or the
power and phase NDFs. Prompting will not occur if one of the other
(inverse) input NDFs has been given on the command line, but not
HERMIN as well. This parameter is only relevant for an inverse
transformation.



HERMOUT = NDF (Write)
`````````````````````
Hermitian output NDF from a forward transform. If a null value is
given then this NDF is not produced.



HM_TITLE = LITERAL (Read)
`````````````````````````
Title for the Hermitian Fourier-transform output NDF. A null (!) value
means using the title of the input NDF. ["KAPPA - Fourier -
Hermitian"]



IM_TITLE = LITERAL (Read)
`````````````````````````
Title for the frequency-domain imaginary output NDF. A null (!) value
means using the title of the input NDF. ["KAPPA - Fourier -
Imaginary"]



IMAGIN = NDF (Read)
```````````````````
Input frequency-domain NDF containing the real part of the complex
transform. If a null is given then an image of zeros is assumed unless
a null is also given for REALIN, in which case the input is requested
in power and phase form. This parameter is only available if HERMIN is
not used. One way to achieve that is to supply IMAGIN, but not HERMIN,
on the command line. This parameter is only relevant for an inverse
transformation.



IMAGOUT = NDF (Write)
`````````````````````
Frequency-domain output NDF containing the imaginary part of the
complex Fourier transform. If a null value is given then this NDF is
not produced. [!]



IN = NDF (Read)
```````````````
Real (space-domain) input NDF for a forward transformation. There are
no restrictions on the size or shape of the input NDF, although the it
may have to be padded or trimmed before being transformed. This
parameter is only used if a forward transformation was requested.



INVERSE = _LOGICAL (Read)
`````````````````````````
If TRUE, then the inverse transform---frequency domain to space domain
---is required, otherwise a transform from the space to the frequency
domain is undertaken. [FALSE]



OUT = NDF (Write)
`````````````````
Real space-domain output NDF. This parameter is only used if an
inverse transformation is requested.



PH_TITLE = LITERAL (Read)
`````````````````````````
Title for the frequency-domain phase output NDF. A null (!) value
means using the title of the input NDF. ["KAPPA - Fourier - Phase"]



PHASEIN = NDF (Read)
````````````````````
Input frequency-domain NDF containing the phase of the complex
transform. If a null is given then an image of zeros is assumed unless
a null is also given for PHASEIN, in which case the application quits.
This parameter is only available if HERMIN, REALIN and IMAGIN are all
not used. One way to achieve that is to supply PHASEIN, but none of
the aforementioned parameters, on the command line. This parameter is
only relevant for an inverse transformation.



PHASEOUT = NDF (Write)
``````````````````````
Frequency-domain output NDF containing the phase of the complex
Fourier transform. If a null value is given then this NDF is not
produced. [!]



POWERIN = NDF (Read)
````````````````````
Input frequency-domain NDF containing the modulus of the complex
transform. Note, this should be the square root of the power rather
than the power itself. If a null is given then an image of zeros is
assumed unless a null is also given for PHASEIN, in which case the
application quits. This parameter is only available if HERMIN, REALIN
and IMAGIN are all not used. One way to achieve that is to supply
POWERIN, but none of the aforementioned parameters, on the command
line. This parameter is only relevant for an inverse transformation.



POWEROUT = NDF (Write)
``````````````````````
Frequency-domain output NDF containing the modulus of the complex
Fourier transform. Note, this is the square root of the power rather
than the power itself. If a null value is given then this NDF is not
produced. [!]



PW_TITLE = LITERAL (Read)
`````````````````````````
Title for the frequency-domain power output NDF. A null (!) value
means using the title of the input NDF. ["KAPPA - Fourier - Power"]



REALIN = NDF (Read)
```````````````````
Input frequency-domain NDF containing the real part of the complex
transform. If a null is given then an image of zeros is assumed unless
a null is also given for IMAGIN, in which case the input is requested
in power and phase form. This parameter is only available if HERMIN is
not used. One way to achieve that is to supply REALIN, but not HERMIN,
on the command line. This parameter is only relevant for an inverse
transformation.



REALOUT = NDF (Write)
`````````````````````
Frequency-domain output NDF containing the real part of the complex
Fourier transform. If a null value is given then this NDF is not
produced. [!]



RL_TITLE = LITERAL (Read)
`````````````````````````
Title for the frequency-domain real output NDF. A null (!) value means
using the title of the input NDF. ["KAPPA - Fourier - Real"]



SHIFT = _LOGICAL (Read)
```````````````````````
If TRUE, the transform origin is to be located at the array's centre.
This is implemented by swapping bottom-left and top-right, and bottom-
right and top-left array quadrants, before doing the transform. This
results in the transformation effectively being done about pixel x =
INT(NAXIS1/2)+1 and y = INT(NAXIS2/2)+1, where NAXISn are the padded
or trimmed dimensions of the NDF. [FALSE]



TRIM = LOGICAL (Read)
`````````````````````
If TRUE, when the input array dimension cannot be processed by the
transform, the output arrays will be trimmed rather than padded with
the fill value. [FALSE]



TITLE = LITERAL (Read)
``````````````````````
Title for the real space-domain output NDF. A null (!) value means
using the title of the input NDF. ["KAPPA - Fourier"]



Examples
~~~~~~~~
fourier galaxy ft_gal
Makes an Hermitian Fourier transform stored in an NDF called ft_gal
from the 2-d NDF called galaxy.
fourier hermin=ft_gal out=galaxy inverse
Takes an Hermitian Fourier transform stored in an NDF called ft_gal
and performs the inverse transformation to yield a normal (spatial
domain) image in NDF galaxy.
fourier in=galaxy powerout=galpow hermout=ft_gal fillval=mean
Makes an Hermitian Fourier transform stored in an NDF called ft_gal
from the 2-d NDF called galaxy. Any bad values in galaxy are replaced
by the mean data value of galaxy. In addition the power of the
transform is written to an NDF called galpow.
fourier realin=real_gal out=galaxy inverse
Takes the real component of a Fourier transform stored in an NDF
called real_gal and performs the inverse transformation to yield a
normal image in NDF galaxy.



Notes
~~~~~


+ See the NAG documentation, Chapter C06, and/or KAPPA routine
  KPG1_HMLTX.GEN for more details of Hermitian Fourier transforms.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CONVOLVE, LUCY, MEM2D, WIENER; Figaro: BFFT, CMPLX*, COSBELL,
FFT, *2CMPLX.


Copyright
~~~~~~~~~
Copyright (C) 1988, 1990-1992 Science & Engineering Research Council.
Copyright (C) 1995, 1998, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2005 Particle Physics & Astronomy Research
Council. All Rights Reserved.


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


+ AXIS, VARIANCE and QUALITY are not propagated from the input to
  output NDFs, but the LABEL, TITLE, HISTORY components and all
  extensions are. Arithmetic is performed using single- or double-
  precision floating point, as appropriate for the type of the data
  array.




