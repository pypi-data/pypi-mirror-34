

PSF
===


Purpose
~~~~~~~
Determines the parameters of a model star profile by fitting star
images in a two-dimensional NDF


Description
~~~~~~~~~~~
This application finds a set of parameters to describe a model
Gaussian star image. It can be used for profile-fitting stellar
photometry, to evaluate correction terms to aperture photometry, or
for filtering.
The model has a radial profile:
D = A exp(-0.5 * (r/sigma) ** gamma )
where r is calculated from the true radial distance from the star
centre allowing for image ellipticity, sigma is the Gaussian precision
constant or profile width. The application combines a number of star
images you specify and determines a mean seeing-disc size, radial
fall-off parameter (gamma), axis ratio, and orientation of a model
star image.
A table, giving details of the seeing and ellipticity of each star
image used can be reported to an output text file. This table
indicates if any star could not be used. Reasons for rejecting stars
are too-many bad pixels present in the image, the star is too close to
the edge of the data array, the `star' is a poor fit to model or it
could not be located.
An optional plot of the mean profile and the fitted function may be
produced. The two-dimensional point-spread function may be stored in
an NDF for later use, as may the one-dimensional fitted profile.


Usage
~~~~~


::

    
       psf in incat [device] [out] [cut] [range] [isize] [poscols]
       



ADAM parameters
~~~~~~~~~~~~~~~



AMP1 = _REAL (Write)
````````````````````
The fitted peak amplitude of the first usable star, in the data units
of the input NDF.



AXES = _LOGICAL (Read)
``````````````````````
TRUE if labelled and annotated axes are to be drawn around the plot.
The width of the margins left for the annotation may be controlled
using Parameter MARGIN. The appearance of the axes (colours, fonts,
etc) can be controlled using the Parameter STYLE. The dynamic default
is TRUE if CLEAR is TRUE, and FALSE otherwise. []



AXISR = _REAL (Write)
`````````````````````
The axis ratio of the star images: the ratio of the major axis length
to that of the minor axis.



CENTRE = LITERAL (Write)
````````````````````````
The formatted co-ordinates of the first fitted star position, in the
current Frame of the NDF.



CLEAR = _LOGICAL (Read)
```````````````````````
If TRUE the current picture is cleared before the plot is drawn. If
CLEAR is FALSE not only is the existing plot retained, but also an
attempt is made to align the new picture with the existing picture.
Thus you can generate a composite plot within a single set of axes,
say using different colours or modes to distinguish data from
different datasets. [TRUE]



COFILE = FILENAME (Read)
````````````````````````
Name of a text file containing the co-ordinates of the stars to be
used. It is only accessed if Parameter INCAT is given a null (!)
value. Each line should contain the formatted axis values for a single
position, in the current Frame of the NDF. Columns can be separated by
spaces, tabs or commas. The file may contain comment lines with the
first character # or !. Other columns may be included in the file, in
which case the columns holding the required co-ordinates should be
specified using Parameter POSCOLS.



CUT = _REAL (Read)
``````````````````
This parameter controls the size of the output NDF. If it is null, !,
the dimension of the square NDF will be the size of the region used to
calculate the radial profile, which usually is given by RANGE * width
in pixels * AXISR, unless truncated. If CUT has a value it is the
threshold which must be included in the PSF NDF, and it is given as
the fraction of the peak amplitude of the PSF. For example, if CUT=0.5
the NDF would contain the point-spread function to half maximum. CUT
must be greater than 0 and less than 1. The suggested default is
0.0001. [!]



DEVICE = DEVICE (Read)
``````````````````````
The graphics workstation on which to produce a plot of the mean radial
profile of the stars and the fitted function. A null (!) name
indicates that no plot is required. [current graphics device]



FWHM = _REAL (Write)
````````````````````
The seeing-disc size: the full width at half maximum across the minor
axis of the stars. It is in units defined by the current Frame of the
NDF. For instance, a value in arcseconds will be reported if the
current Frame is a SKY Frame, but pixels will be used if it is a PIXEL
Frame.



GAMMA = _REAL (Write)
`````````````````````
The radial fall-off parameter of the star images. See the description
for more details. A gamma of two would be a Gaussian.



GAUSS = _LOGICAL (Read)
```````````````````````
If TRUE, the gamma coefficient is fixed to be 2; in other words the
best-fitting two-dimensional Gaussian is evaluated. If FALSE, gamma is
a free parameter of the fit, and the derived value is returned in
Parameter GAMMA. [FALSE]



IN = NDF (Read)
```````````````
The NDF containing the star images to be fitted.



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a positions list (such as produced by
applications CURSOR, LISTMAKE, etc.) giving the star positions to use.
If a null (!) value is supplied Parameter COFILE will be used to get
the star positions from a simple text file.



ISIZE = _INTEGER (Read)
```````````````````````
The side of the square area to be used when forming the marginal
profiles for a star image, given as a number of pixels. It should be
sufficiently large to contain the entire star image. It should be an
odd number and must lie in the range from 3 to 101. [15]



LOGFILE = FILENAME (Read)
`````````````````````````
Text file to contain the table of parameters for each star. A null (!)
name indicates that no log file is required. [!]



MARGIN( 4 ) = _REAL (Read)
``````````````````````````
The widths of the margins to leave for axis annotation, given as
fractions of the corresponding dimension of the current picture. Four
values may be given, in the order: bottom, right, top, left. If fewer
than four values are given, extra values are used equal to the first
supplied value. If these margins are too narrow, any axis annotation
may be clipped. If a null (!) value is supplied, the value used is
0.15 (for all edges) if either annotated axes or a key are produced,
and zero otherwise. [current value]



MARKER = INTEGER (Read)
```````````````````````
The PGPLOT marker type to use for the data values in the plot.
[current value]



MINOR = _LOGICAL (Read)
```````````````````````
If MINOR is TRUE the horizontal axis of the plot is annotated with
distance along the minor axis from the centre of the PSF. If MINOR is
FALSE, the distance along the major axis is used. [TRUE]



NORM = _LOGICAL (Read)
``````````````````````
If TRUE, the model PSF is normalized so that it has a peak value of
unity. Otherwise, its peak value is equal to the peak value of the fit
to the first usable star, in the data units of the input NDF. [TRUE]



ORIENT = _REAL (Write)
``````````````````````
The orientation of the major axis of the star images, in degrees. If
the current Frame of the NDF is a SKY Frame, this will be a position
angle (measured from north through east). Otherwise, it will be
measured from the positive direction of the first current Frame axis
("X") towards the second current Frame axis ("Y").



OUT = NDF (Write)
`````````````````
The NDF containing the fitted point-spread function evaluated at each
pixel. If null, !, is entered no output NDF will be created. The
dimensions of the array are controlled by Parameter CUT. The pixel
origin is chosen to align the model PSF with the fitted star in pixel
co-ordinates, thus allowing the NDF holding the model PSF to be
compared directly with the input NDF. A WCS component is stored in the
output NDF holding a copy of the input WCS component. An additional
Frame with Domain name OFFSET is added, and is made the current Frame.
This Frame measures the distance from the PSF centre in the units in
which the FWHM is reported. [!]



POSCOLS = _INTEGER (Read)
`````````````````````````
Column positions of the co-ordinates (x then y) in an input record of
the file specified by Parameter COFILE. The columns must be different
amongst themselves. If there is duplication new values will be
requested. Only accessed if INCAT is given a null (!) value. If a null
(!) value is supplied for POSCOLS, the values [1,2] will be used. [!]



PROFOUT = NDF (Write)
`````````````````````
The NDF containing the one-dimensional fitted profile as displayed in
the plot. If null, !, is entered no output NDF will be created. The
DATA component of this NDF holds the fitted PSF value at each radial
bin. The VARIANCE component holds the square of the residuals between
the fitted values and the binned values derived from the input NDF. An
AXIS component is included in the NDF containing the radial distance
as displayed in the plot. [!]



RANGE = _REAL (Read)
````````````````````
The number of image profile widths out to which the radial star
profile is to be fitted. (There is an upper limit of 100 pixels to the
radius at which data are actually used.) [4.0]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the plotting style to use
when drawing the annotated axes, data values, and the model profile.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings overriding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a plotting attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!)---the initial default---is supplied. To apply changes of
style to only the current invocation, begin these attributes with a
plus sign. A mixture of persistent and temporary style changes is
achieved by listing all the persistent attributes followed by a plus
sign then the list of temporary attributes.
See section "Plotting Attributes" in SUN/95 for a description of the
available attributes. Any unrecognised attributes are ignored (no
error is reported).
The appearance of the model curve is controlled by the attributes
Colour(Curves), Width(Curves), etc. (the synonym Line may be used in
place of Curves). The appearance of the markers representing the real
data is controlled by Colour(Markers), Width(Markers), etc. (the
synonym Symbols may be used in place of Markers). [current value]



TITLE = LITERAL (Read)
``````````````````````
The title for the NDF to contain the fitted point-spread function. If
null (!) is entered the NDF will not contain a title. ["KAPPA - PSF"]



TOTAL = _REAL (Write)
`````````````````````
The flux of the fitted function integrated to infinite radius. Its
unit is the product of the data unit of the input NDF and the square
of the radial unit, such as pixel or arcsec, for the current WCS
Frame, when NORM=FALSE. When NORM=TRUE, TOTAL is just measured in the
squared radial unit. Therefore, for direct comparison of total flux,
the same units must be used.



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has more than two axes. A group of two strings should be supplied
specifying the two axes which are to be used when determining
distances, reporting positions, etc. Each axis can be specified using
one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the two significant NDF pixel axes are used. [!]



XCEN = LITERAL (Write)
``````````````````````
The formatted X co-ordinate of the first fitted star position, in the
current co-ordinate Frame of the NDF.



XLEFT = _REAL (Read)
````````````````````
The axis value to place at the left hand end of the horizontal axis of
the plot. If a null (!) value is supplied, a suitable default value
will be found and used. The value supplied may be greater than or less
than the value supplied for XRIGHT. [!]



XRIGHT = _REAL (Read)
`````````````````````
The axis value to place at the right hand end of the horizontal axis
of the plot. If a null (!) value is supplied, a suitable default value
will be found and used. The value supplied may be greater than or less
than the value supplied for XLEFT. [!]



YBOT = _REAL (Read)
```````````````````
The axis value to place at the bottom end of the vertical axis of the
plot. If a null (!) value is supplied, a suitable default value will
be found and used. The value supplied may be greater than or less than
the value supplied for YTOP. [!]



YCEN = LITERAL (Write)
``````````````````````
The formatted Y co-ordinate of the first fitted star position, in the
current co-ordinate Frame of the NDF.



YTOP = _REAL (Read)
```````````````````
The axis value to place at the top end of the vertical axis of the
plot. If a null (!) value is supplied, a suitable default value will
be found and used. The value supplied may be greater than or less than
the value supplied for YBOT. [!]



Examples
~~~~~~~~
psf ngc6405i starlist.FIT \
Derives the mean point-spread function for the stars images in the NDF
called ngc6405i that are situated near the co-ordinates given in the
positions list starlist.FIT. A plot of the profile is drawn on the
current graphics device.
psf ngc6405i starlist device=!
As above but there is no graphical output, and the file type of the
input positions list is defaulted.
psf ngc6405i cofile=starlist.dat gauss \
As the first example, except the psf is fitted to a two-dimensional
Gaussian, and the positions are given in a simple text file instead of
a positions list.
psf incat=starlist.FIT in=ngc6405i logfile=fit.log fwhm=(seeing) \
As the first example, but the results, including the fits to each
star, are written to the text file fit.log. The full-width half-
maximum is written to the ICL variable SEEING rather than the
parameter file.
psf ngc6405i starlist isize=31 style="'title=Point spread function'"
As the first example, but the area including a star image is 31 pixels
square, say because the seeing is poor or the pixels are smaller than
normal. The graph is titled "Point spread function".



Notes
~~~~~


+ Values for the FWHM seeing are given in arcseconds if the Current
co-ordinate Frame of the NDF is a SKY Frame.
+ The stars used to determine the mean image parameters should be
chosen to represent those whose magnitudes are to be found using a
stellar photometry application, and to be sufficiently bright,
uncrowded, and noise-free to allow an accurate fit to be made.
+ It is assumed that the image scale does not vary significantly
across the image.
+ The iterative method to calculate the fit is as follows.
+ Marginal profiles of each star image are formed in four directions:
at 0, 45, 90 and 135 degrees to the x axis. The profiles are cleaned
via an iterative modal filter that removes contamination such as
neighbouring stars; moving from the centre of the star, the filter
prevents each data point from exceeding the maximum of the two
previous data values.
+ A Gaussian curve and background is fitted to each profile
iteratively refining the parameters until parameters differ by less
than 0.1 per cent from the previous iteration. If convergence is not
met after fifteen iterations, each fit parameter is approximately the
average of its last pair of values. The initial background is the
lower quartile. Using the resulting four Gaussian centres, a mean
centre is found for each star. Iterations cease when the mean centroid
position shifts by less 0.001 from the previous iteration, or after
three iterations if the nominal tolerance is not achieved.
+ The four Gaussian widths of all the stars are combined modally,
using an amplitude-weighted average with rejection of erroneous data
(using a maximum-likelihood function for a statistical model in which
any of the centres has a constant probability of being corrupt). From
the average widths along the four profiles, the seeing-disc size, axis
ratio and axis inclination are calculated.
+ The data surrounding each star is then binned into isophotal zones
  which are elliptical annuli centred on the star---the ellipse
  parameters being those just calculated. The data in each zone is
  processed to remove erroneous points (using the aforementioned
  maximum-likelihood function) and to find an average value. A Gaussian
  profile is fitted to these average values and the derived amplitude is
  used to normalise the values to an amplitude of unity. The normalised
  values are put into bins together with the corresponding data from all
  other stars and these binned data represent a weighted average radial
  profile for the set of stars, with the image ellipticity removed.
  Finally a radial profile is fitted to these data, giving the radial
  profile parameter gamma and a final re-estimate of the seeing-disc
  size.




Related Applications
~~~~~~~~~~~~~~~~~~~~
PHOTOM; Starman.


Copyright
~~~~~~~~~
Copyright (C) 1990-1993 Science & Engineering Research Council.
Copyright (C) 1998-2001, 2004, 2006 Particle Physics & Astronomy
Research Council. Copyright (C) 2007, 2010, 2012 Science & Technology
Facilities Council. All Rights Reserved.


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


+ This routine correctly processes the AXIS, DATA, QUALITY, LABEL, WCS
and TITLE components of an NDF data structure.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. The output point-
  spread-function NDF has the same type as the input NDF.




