

PLUCK
=====


Purpose
~~~~~~~
Plucks slices from an NDF at arbitrary positions


Description
~~~~~~~~~~~
This application's function is to extract data at scientifically
relevant points such as the spatial location of a source or wavelength
of a spectral feature, rather than at data sampling points (for which
NDFCOPY is appropriate). This is achieved by the extraction of
interpolated slices from an NDF. A slice is located at a supplied set
of co-ordinates in the current WCS Frame for some but not all axes,
and it possesses one fewer significant dimension per supplied co-
ordinate. The slices run parallel to pixel axes of the NDF.
The interpolation uses one of a selection of resampling methods to
effect the non-integer shifts along the fixed axes, applied to each
output element along the retained axes (see the METHOD, PARAMS, and
TOL parameters).
Three routes are available for obtaining the fixed positions, selected
using parameter MODE:


+ from the parameter system (see parameter POS);
+ from a specified positions list (see parameter INCAT); or
+ from a simple text file containing a list of co-ordinates (see
  parameter COIN).

In the first mode the application loops, asking for new extraction co-
ordinates until it is told to quit or encounters an error. However
there is no looping if the position has been supplied on the command
line.
Each extracted dataset is written to a new NDF, which however, may
reside in a single container file (see the CONTAINER parameter).


Usage
~~~~~


::

    
       pluck in axes out method [mode] { pos
                                       { coin=?
                                       { incat=?
                                      mode
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES( ) = _INTEGER (Read)
`````````````````````````
The WCS axis or axes to remain in the output NDF. The slice will
therefore contain an array comprising all the elements along these
axes. The maximum number of axes is one fewer than the number of WCS
axes in the NDF.
Each axis can be specified using one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If the axes of the current Frame are not parallel to the NDF
pixel axes, then the pixel axis which is most nearly parallel to the
specified current Frame axis will be used.



COIN = FILENAME (Read)
``````````````````````
Name of a text file containing the co-ordinates of slices to be
plucked. It is only accessed if parameter MODE is given the value
"File". Each line should contain the formatted axis values for a
single position, in the current Frame of the NDF. Axis values can be
separated by spaces, tabs or commas. The file may contain comment
lines with the first character # or !.



CONTAINER = _LOGICAL (Read)
```````````````````````````
If TRUE, each slice extracted is written as an NDF component of the
HDS container file specified by the OUT parameter. The nth component
will be named PLUCK_n. If set FALSE, each extraction is written to a
separate file. On-the-fly format conversion to foreign formats is not
possible when CONTAINER=TRUE. [FALSE]



DESCRIBE = _LOGICAL (Read)
``````````````````````````
If TRUE, a detailed description of the co-ordinate Frame in which the
fixed co-ordinates are to be supplied is displayed before the
positions themselves. It is ignored if MODE="Catalogue". [current
value]



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a positions list giving the co-ordinates of the
fixed positions, such as produced by applications CURSOR, LISTMAKE,
etc. It is only accessed if parameter MODE is given the value
"Catalogue". The catalogue should have a WCS Frame common with the
NDF, so that the NDF and catalogue FrameSets can be aligned.



MODE = LITERAL (Read)
`````````````````````
The mode in which the initial co-ordinates are to be obtained. The
supplied string can be one of the following values.


+ "Interface" -- positions are obtained using parameter POS.
+ "Catalogue" -- positions are obtained from a positions list using
parameter INCAT.
+ "File" -- positions are obtained from a text file using parameter
  COIN.

[current value]



IN = NDF (Read)
```````````````
The NDF structure containing the data to be extracted. It must have at
least two dimensions.



METHOD = LITERAL (Read)
```````````````````````
The method to use when sampling the input pixel values. For details of
these schemes, see the descriptions of routine AST_RESAMPLEx in
SUN/210. METHOD can take the following values.


+ "Linear" -- When resampling, the output pixel values are calculated
by linear interpolation in the input NDF among the two nearest pixel
values along each axis chosen by AXES. This method produces smoother
output NDFs than the nearest-neighbour scheme, but is marginally
slower.
+ "Sinc" -- Uses the sinc(pi*x) kernel, where x is the pixel offset
from the interpolation point, and sinc(z)=sin(z)/z. Use of this scheme
is not recommended.
+ "SincSinc" -- Uses the sinc(pi*x)sinc(k*pi*x) kernel. A valuable
general-purpose scheme, intermediate in its visual effect on NDFs
between the linear option and using the nearest neighbour.
+ "SincCos" -- Uses the sinc(pi*x)cos(k*pi*x) kernel. Gives similar
results to the "SincSinc" scheme.
+ "SincGauss" -- Uses the sinc(pi*x)exp(-k*x*x) kernel. Good results
can be obtained by matching the FWHM of the envelope function to the
point-spread function of the input data (see parameter PARAMS).
+ "Somb" -- Uses the somb(pi*x) kernel, where x is the pixel offset
from the interpolation point, and somb(z)=2*J1(z)/z (J1 is the first-
order Bessel function of the first kind. This scheme is similar to the
"Sinc" scheme.
+ "SombCos" -- Uses the somb(pi*x)cos(k*pi*x) kernel. This scheme is
similar to the "SincCos" scheme.
+ "BlockAve" -- Block averaging over all pixels in the surrounding
  N-dimensional cube.

All methods propagate variances from input to output, but the variance
estimates produced by interpolation schemes need to be treated with
care since the spatial smoothing produced by these methods introduces
correlations in the variance estimates. The initial default is
"SincSinc". [current value]



OUT = NDF (Write)
`````````````````
The name for the output NDF, or the name of the single container file
if CONTAINER=TRUE.



PARAMS( 2 ) = _DOUBLE (Read)
````````````````````````````
An optional array which consists of additional parameters required by
the Sinc, SincSinc, SincCos, SincGauss, Somb, SombCos, and Gauss
methods.
PARAMS(1) is required by all the above schemes. It is used to specify
how many pixels are to contribute to the interpolated result on either
side of the interpolation in each dimension. Typically, a value of 2
is appropriate and the minimum allowed value is 1 (i.e. one pixel on
each side). A value of zero or fewer indicates that a suitable number
of pixels should be calculated automatically. [0]
PARAMS(2) is required only by the SombCos, Gauss, SincSinc, SincCos,
and SincGauss schemes. For the SombCos, SincSinc, and SincCos schemes,
it specifies the number of pixels at which the envelope of the
function goes to zero. The minimum value is 1.0, and the run-time
default value is 2.0. For the Gauss and SincGauss scheme, it specifies
the full-width at half-maximum (FWHM) of the Gaussian envelope. The
minimum value is 0.1, and the run-time default is 1.0. On astronomical
images and spectra, good results are often obtained by approximately
matching the FWHM of the envelope function, given by PARAMS(2), to the
point-spread function of the input data. []



POS( ) = LITERAL (Read)
```````````````````````
An the co-ordinates of the next slice to be extracted, in the current
co-ordinate Frame of the NDF (supplying a colon ":" will display
details of the current co-ordinate Frame). The position should be
supplied as a list of formatted axis values separated by spaces or
commas. POS is only accessed if parameter MODE is given the value
"Interface". If the co-ordinates are supplied on the command line only
one slice will be extracted; otherwise the application will ask for
further positions which may be terminated by supplying the null value
(!).



TITLE = LITERAL (Read)
``````````````````````
A Title for every output NDF structure. A null value (!) propagates
the title from the input NDF to all output NDFs. [!]



TOL = _DOUBLE (Read)
````````````````````
The maximum tolerable geometrical distortion which may be introduced
as a result of approximating non-linear Mappings by a set of piece-
wise linear transforms. Both algorithms approximate non-linear co-
ordinate transformations in order to improve performance, and this
parameter controls how inaccurate the resulting approximation is
allowed to be, as a displacement in pixels of the input NDF. A value
of zero will ensure that no such approximation is done, at the expense
of increasing execution time. [0.05]



Examples
~~~~~~~~
pluck omc1 pos="5:35:13.7,-5:22:13.6" axes=FREQ
method=sincgauss params=[3,5] out=omc1_trap The NDF omc1 is a
spectral-imaging cube with (Right ascension, declination, frequency)
World Co-ordinate axes. This example extracts a spectrum at
RA=5h35m13.7s, Dec=-5d22m13.6 using the SincGauss interpolation
method. Three pixels either side of the point are used to interpolate,
the full-width half-maximum of the Gaussian is five pixels. The
resultant spectrum called omc1_trap, is still a cube, but its spatial
dimensions each only have one element.
pluck omc1 mode=cat incat=a axes=FREQ container out=omc1_spectra
This example reads the fixed positions from the positions list in file
a.FIT. The selected spectra are stored in an HDS container file called
omc1_spectra.sdf.
pluck omc1 mode=cat incat=a axes=SPEC container out=omc1_spectra
As the previous example, plucking spectra, this time by selecting the
generic spectral axis.
pluck omc1 pos=3.45732E11 axes="RA,Dec" method=lin out=peakplane
This example extracts a plane from omc1 at frequency 3.45732E11 Hz
using linear interpolation and stores it in NDF peakplane.



Notes
~~~~~


+ In Interface or File modes all positions should be supplied in the
current co-ordinate Frame of the NDF. A description of the co-ordinate
Frame being used is given if parameter DESCRIBE is set to a TRUE
value. Application WCSFRAME can be used to change the current co-
ordinate Frame of the NDF before running this application if required.
+ The output NDF has the same dimensionality as the input NDF,
although the axes with fixed co-ordinates (those not specified by the
AXES parameter) are degenerate, having bounds of 1:1. The retention of
these insignificant axes enables the co-ordinates of where the slice
originated to be recorded. Such fixed co-ordinates may be examined
with say NDFTRACE. NDFCOPY may be used to trim the degenerate axes if
their presence prevents some old non-KAPPA tasks from operating.
+ In Catalogue or File modes the table file need only contain columns
  supplying the fixed positions. In this case the co-ordinates along the
  retained axes are deemed to be independent, that is they do not affect
  the shifts required of the other axes. In practice this assumption
  only affects File mode, as catalogues made with CURSOR or LISTMAKE
  will contain WCS information.

In Interface mode representaive co-ordinates along retained axes are
the midpoints of the bounds of an array that would contain the
resampled copy of the whole input array.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFCOPY, REGRID.


Copyright
~~~~~~~~~
Copyright (C) 2007 Science & Technology Facilities Council. All Rights
Reserved.


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


+ The LABEL, UNITS, and HISTORY components, and all extensions are
propagated. TITLE is controlled by the TITLE parameter. DATA,
VARIANCE, AXIS, and WCS are propagated after appropriate modification.
The QUALITY component is not propagated.
+ The processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ The minimum number of dimensions in the input NDF is two.
+ Processing a group of input NDFs is not supported unless CONTAINER =
  TRUE or when only one output NDF is created per input file.




