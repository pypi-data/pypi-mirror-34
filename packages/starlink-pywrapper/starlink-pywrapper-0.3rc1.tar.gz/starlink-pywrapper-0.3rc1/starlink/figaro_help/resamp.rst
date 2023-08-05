

RESAMP
======


Purpose
~~~~~~~
Resample and average several spectra


Description
~~~~~~~~~~~
Depending on the operation mode this routine either

+ takes a list of one-dimensional NDFs as input, resamples them to a
common linear grid of axis values, and averages them into a single
one-dimensional NDF, or
+ takes a single N-dimensional NDF as input and resamples each row
  into a new row of a similar output NDF; resampling is along the first
  axis, all further axes are retained.

The resampling creates an interdependence between pixels of the output
NDF. Only limited information on this interdependence is stored in the
output and ignored by most applications. Data input to this routine is
assumed to have no such interdependence.
The resampling algorithm is reintegration (Meyerdierks, 1992a) and it
is applied to each input NDF separately. Any resampled data value is a
weighted sum of the input values. The weights are the normalised
overlaps between the output and input pixels. The resampled spectra
are averaged pixel by pixel.
If input variances are to be ignored it is assumed that the variance
is a global constant, i.e. equal in all pixels of all input NDFs. The
resampling may still result in different weights for different pixels.
In the averaging process the global input variance is calculated and
reported. The output variance will be derived on a pixel-by-pixel
basis from the data scatter in the averaging process.
In any input NDF, this routine recognises axis centres (pixel
positions), pixel widths, data values, and data variances. (This
routine also recognises the Specdre Extension and will use it where
relevant.) Any other information is propagated from the first input
NDF.
Labels and units are checked for consistency, but only a warning is
given. In interpreting the data all labels and units are assumed to be
the same as in the first input NDF.
All input NDFs must have a variance component (unless VARUSE is set
false). NDFs without variances are ignored. A warning to that effect
is issued. If VARUSE is set false, input NDFs may or may not have
variances, such information will be ignored at any rate.
The output NDF is based primarily on the first input NDF. There will
be no pixel widths, since the pixel positions are linear and the
pixels contiguous. The pixel positions, data values, and data
variances will be affected by the resampling process. The output
Specdre Extension will be based on the first input NDF or will be
created.
The vector of row sums of the covariance matrix (Meyerdierks, 1992a/b)
will be created in the Specdre Extension. This is an NDF structure
with only a data component of the same shape as the main data array.
If such a structure is found in one of the input NDFs, a warning is
issued but such information is ignored.


Usage
~~~~~


::

    
       resample mode inlist out start step end
       



ADAM parameters
~~~~~~~~~~~~~~~



MODE = _CHAR (Read)
```````````````````
The operating mode. This can be abbreviated to one character, is case-
insensitive and must be one of the following:

+ 'SPECTRA': Average several 1-D input NDFs into a single 1-D output
NDF. Resample before averaging.
+ 'CUBE': Accept only one - but N-D - input NDF. Resample each row
  (1-D subset extending along first axis) separately. Note that a single
  spectrum could be handled by both modes; it is more effective to treat
  it as a 1-D cube than as an N=1 average. ['Cube']





INFO = _LOGICAL (Read)
``````````````````````
If false, informational and warning messages are suppressed. [YES]



VARUSE = _LOGICAL (Read)
````````````````````````
If true, input NDFs without variance information are skipped. If
false, variance information in the input is ignored. [YES]



INLIST = LITERAL (Read)
```````````````````````
The group of input NDFs. In a complicated case this could be something
like
M_51(25:35,-23.0,-24.0),M101,^LISTFILE.LIS
This NDF group specification consists of

+ one identified NDF from which a subset is to be taken,
+ one identified NDF,
+ an indirection to an ASCII file containing more NDF group
  specifications. That file may have comment lines and in-line comments,
  which are recognised as beginning with a hash (#).





OUT = NDF (Read)
````````````````
The output NDF.



START = _DOUBLE (Read)
``````````````````````
The first pixel position in the output NDF. The prompt value is
derived from the first valid input NDF.



STEP = _DOUBLE (Read)
`````````````````````
The pixel position increment in the output NDF. The prompt value is
derived as the average increment in the first valid input NDF.



END = _DOUBLE (Read)
````````````````````
The last pixel position in the output NDF. The prompt value is derived
from the first valid input NDF.



Examples
~~~~~~~~
resample spectra ^inlist out 3.5 0.0254902 10.0
The names of input NDFs are read from an ASCII list file called
INLIST. The result will be stored in OUT which has 256 pixels covering
the coordinates from 3.5 to 10.0
resample spectra ^inlist out varuse=false accept
The names of input NDFs are read from an ASCII list file called
INLIST. The input NDFs either have no variance, or their variance
information is to be ignored. The output will be in OUT. The start and
end pixel positions for OUT are the same as in the first input NDF.
OUT also has the same number of pixels. The pixel spacings are
constant in OUT while they may not be in the input NDF.
resample cube ^inlist out 3.5 0.0254902 10.0
INLIST contains only one NDF probably with more than one dimension.
OUT will have the same dimensions except the first, which is the
resampled one.



Notes
~~~~~
The axis normalisation flag is ignored.
This routine recognises the Specdre Extension v. 0.7.


Pitfalls
~~~~~~~~
This routine uses pixel widths. If there is no width array in the
input NDF, the widths default as described in SUN/33. This may have
undesired effects on resampling spectra that cover several non-
adjacent coordinate ranges and where the missing ranges are not
covered by bad pixels. Such spectra have highly non-linear pixel
positions and the default pixel widths will not be as desired. To
illustrate this consider the following spectrum with four pixels, the
intended extents of the pixels and the defaulted extents:
x x x x
|1111111|2222222| |3333333|4444444|
|1111111| |333333333333333333333333333333333|
|222222222222222222222222222222222| |4444444|
Since this routine uses the overlap between input and output pixels as
weights for resampling, non-bad pixels next to such a gap in data will
affect too many output pixels with too much weight. Users should be
aware that spectra as illustrated here are somewhat pathologic and
that they should be given an explicit width array.
The routine accesses one input NDF at a time and needs not hold all
input NDFs at the same time. However, The routine needs temporary
workspace. If KMAX is the number of pixels in an input NDF and LMAX
the number of output pixels, the routine needs

+ one vector of length LMAX,
+ one matrix of size KMAX by LMAX,
+ two matrices of size LMAX by LMAX.

These workspaces are usually of type _REAL. All (!) are of type
_DOUBLE if the first valid input NDF has type _DOUBLE for either of
the following:

+ pixel position,
+ pixel width,
+ data value,
+ data variance.

In addition one integer vector of length LMAX is needed.
There is an oddity about this routine if only one input NDF is used
and its variance array is used and some or all variance values are
zero. In this case the output will formally still be an average of
input NDFs using 1/variance as weights. Data with zero variance cannot
be weighted and are regarded as bad. If this is a problem, users can
set VARUSE false to ignore all the input variances. (Note that zero
variances always cause that pixel to be ignored by this routine. But
where it really calculates an average of two or more spectra, this is
considered proper procedure.)


Timing
~~~~~~
The time used by this routine is about proportional to the number of
input NDFs. It is proportional to the square of the number of output
pixels. Timing can be optimized, if the input NDFs cover about the
same coordinate range as the output NDF rather than include a lot of
data irrelevant for the output.


References
~~~~~~~~~~
Meyerdierks, H., 1992a, Covariance in resampling and model fitting,
Starlink, Spectroscopy Special Interest Group
Meyerdierks, H., 1992b, Fitting resampled spectra, in P.J. Grosbol,
R.C.E. de Ruijsscher (eds), 4th ESO/ST-ECF Data Analysis Workshop,
Garching, 13 - 14 May 1992, ESO Conference and Workshop Proceedings
No. 41, Garching bei Muenchen, 1992


