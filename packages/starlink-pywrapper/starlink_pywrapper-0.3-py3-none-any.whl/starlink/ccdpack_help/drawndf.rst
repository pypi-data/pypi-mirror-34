

DRAWNDF
=======


Purpose
~~~~~~~
Draws aligned images or outlines on a graphics display


Description
~~~~~~~~~~~
This routine displays on a graphics device the positions of a group of
NDFs in their Current attached coordinate system. This will show their
relative positions in their current coordinates, and so can, for
instance, be used to check that alignment looks correct prior to
resampling and combining into a mosaic. Depending on the CLEAR
parameter it will either clear the display device and set the plotting
area to the right size to fit in all the images, or leave the display
intact and plot those parts of images which fit on the existing area.
Depending on the LINES and IMAGE parameters, an outline showing the
extent of each NDF can be plotted, or the pixels of the NDF plotted
resampled into the given coordinate system, or both. Each outline or
pixel block shows the extent of the data array of the corresponding
NDF, and is therefore basically rectangular in shape, though it may be
distorted if the mapping between pixel and Current coordinates is
nonlinear. The origin (minimum X,Y pixel value) of each boundary can
be marked and the image labelled with its name and/or index number.
Optionally (according to the TRIM parameter), the display may be
restricted to the useful extent of the image, enabling overscan
regions or bias strips to be ignored.
If the LINES parameter is true, the position of each NDF's data array
will be indicated by a (perhaps distorted) rectangle drawn on the
device. If the IMAGE parameter is true, then the image's pixels will
be plotted as well as its position. The colour levels in this case are
determined by the PERCENTILES argument applied separately to each
plotted frame, and overlapping images will simply be drawn on top of
each other - no averaging or scaling is performed. If the IMAGES
parameter is false, the program does not need to examine the data
pixels at all, so it can run much faster.
The results are only likely to be sensible if the Current coordinate
system of all the NDFs is one in which they are all (more or less)
aligned. If the Current attached coordinate systems of all do not all
have the same Domain (name), a warning will be issued, but plotting
will proceed.
DRAWNDF uses the AGI graphics database in a way which is compatible
with KAPPA applications; if the CLEAR parameter is set to false (only
possible when IMAGE is also false) then it will attempt to align the
plotted outlines with suitably registered graphics which are already
on the graphics device; in this case outlines or parts of outlines
lying outside the existing graphics window remain unplotted. So, for
instance, it is easy to overlay the outlines of a set of NDFs on a
mosaic image which has been constructed using those NDFs, or to see
how an undisplayed set of NDFs would map onto one already displayed,
either by a previous invocation of DRAWNDF or by a KAPPA program such
as DISPLAY or CONTOUR.
This routine is designed for use on two-dimensional NDFs; if the NDFs
presented have more than two dimensions, any higher ones will be
ignored.


Usage
~~~~~


::

    
       drawndf in [device]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXES = _LOGICAL (Read)
``````````````````````
True if labelled and annotated axes are to be drawn around the
plotting surface, showing the common Current coordinate system of the
images. The appearance of the axes can be controlled using the STYLE
parameter. AXES has a dynamic default; it defaults to the same value
as the CLEAR parameter. [dynamic]



CLEAR = _LOGICAL (Read)
```````````````````````
If CLEAR is set to true, the graphics device will be cleared before
the plot is made.
If you want the outlines to be drawn over the top of an existing DATA
picture, for instance one displayed with KAPPA's DISPLAY application,
then set CLEAR to false. If possible, alignment will occur within the
Current coordinate system of the NDF. If this is not possible, an
attempt is made in SKY, PIXEL or GRID domains. If the image cannot be
aligned in any suitable domain, then DRAWNDF will terminate with an
error. If CLEAR is set to FALSE, then there must already be a picture
displayed on the graphics device.
The CLEAR parameter is ignored (and the device cleared anyway) if
IMAGE is true. [TRUE]



DEVICE = DEVICE (Read)
``````````````````````
The name of the device on which to make the plot. [Current display
device]



EXTENT( 4 ) = _INTEGER (Read)
`````````````````````````````
The extent of the useful CCD area. This should be given in pixel index
values (see notes). The extent is restricted to that of the CCD frame,
so no padding of the data can occur. If values outside of those
permissable are given then they are modified to lie within the CCD
frame. The values should be given in the order XMIN,XMAX,YMIN,YMAX.
If the TRIM parameter is set true, then only the area defined by these
values is drawn. If TRIM is false, this parameter is ignored.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. If USESET is true then a value specific to
the Set Index of each image will be sought.



IN = LITERAL (Read)
```````````````````
A list of the NDFs to be displayed.



IMAGE = _LOGICAL (Read)
```````````````````````
If true, the pixels of the each image will be plotted. In this case
any existing plot on the graphics device is always cleared, regardless
of the value of the CLEAR parameter. Note that DRAWNDF does not need
to examine the NDF pixels at all unless this option is true, so
setting it can make the program run much more slowly. [FALSE]



LABNAME = _LOGICAL (Read)
`````````````````````````
If true, each plotted outline is labelled with the name of the NDF.
Label positioning is determined by the LABPOS parameter. [TRUE]



LABNUM = _LOGICAL (Read)
````````````````````````
If true, each plotted outline is labelled with the number of the NDF
(i.e. the first on in the IN list is 1, the second is 2, etc). If both
this and the LABNAME parameter are true, the label will contain both
the number and the name. Label positioning is determined by the LABPOS
parameter. [FALSE]



LABOPAQUE = _LOGICAL (Read)
```````````````````````````
If true, the label text indicated by the LABNUM and LABNAME parameters
will be written on an opaque rectangle of background colour obscuring
the picture below. If false, the text will be plotted directly on the
picture, which may be hard to read. [TRUE]



LABPOS = LITERAL (Read)
```````````````````````
A two-character string identifying the positioning of the text label
(only used if at least one of LABNAME or LABNUM is true). The first
letter indicates the side-to-side position and the second indicates
the up-and-down position in the pixel coordinates of each NDF. Each
letter must be "N", "C" or "F", for Near to the origin, Central or Far
from the origin. Normally (unless LABUP is true) the text will be
written parallel or antiparallel to the X pixel direction for each
NDF, with one edge anchored as per the value of LABPOS in such a way
that the text sits inside the outline (if it will fit).
Only the first two characters are significant.
LABPOS normally defaults to "NN", indicating the label written next to
the origin, but if LABUP is set TRUE, then it defaults to "CC". [NN]



LABUP = _LOGICAL (Read)
```````````````````````
Normally this parameter is FALSE, and each text label (as determined
by LABNAME and LABNUM) is written parallel or anti-parallel to the
pixel X axis of the corresponding NDF. If this parameter is set TRUE
however, text will be written upright, that is, horizontal on the
graphics device. In this case the positioning algorithm may fail to
place it inside the corresponding outline; it is generally not
advisable to set LABUP to TRUE unless the label is positioned in the
centre of the outline by setting LABPOS="CC". [FALSE]



LINES = _LOGICAL (Read)
```````````````````````
If true, the outline of each NDF is plotted. If false, no outlines are
plotted. [TRUE]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is
"CCDPACK.LOG". [CCDPACK.LOG]



LOGTO = LITERAL (Read)
``````````````````````
Every CCDPACK application has the ability to log its output for future
reference as well as for display on the terminal. This parameter
controls this process, and may be set to any unique abbreviation of
the following:

+ TERMINAL -- Send output to the terminal only
+ LOGFILE -- Send output to the logfile only (see the LOGFILE
parameter)
+ BOTH -- Send output to both the terminal and the logfile
+ NEITHER -- Produce no output at all

If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is "BOTH".
[BOTH]



ORIGIN = _LOGICAL (Read)
````````````````````````
If true, a marker is placed at the grid coordinate origin of each NDF
(the corner of the data region being considered which has the lowest X
and Y pixel coordinates). [TRUE]



PENROT = _LOGICAL (Read)
````````````````````````
If TRUE, each outline will be drawn with a different pen (colour).
Otherwise, they will all be drawn in the same pen. [FALSE]



PERCENTILES( 2 ) = _DOUBLE (Read)
`````````````````````````````````
If IMAGE is true, this gives the percentile limits between which each
image will be scaled when it is drawn. Any pixels with a value lower
than the first element will have the same colour, and any with a value
higher than the second will have the same colour. Must be in the range
0 <= PERCENTILES( 1 ) <= PERCENTILES( 2 ) <= 100.
Note that the percentile levels are calculated separately for each of
the NDFs in the IN list, so that the brightest pixel in each NDF will
be plotted in the same colour, even though their absolute values may
be quite different. [2,98]



STYLE = LITERAL (Read)
``````````````````````
A group of attribute settings describing the plotting style to use for
the outlines and annotated axes. This should be a string consisting of
comma-separated `attribute=value' items; as explained in the `Plotting
Styles and Attributes' section of SUN/95, except that colours may only
be specified by number, and not by name.
Some attributes which it may be useful to set are the following
(default values given in square brackets):

+ width(curves) -- the thickness of outlines drawn [1]
+ colour(curves) -- colour of the outlines (if PENROT is true, serves
as starting value) [1]
+ size(strings) -- font size of text labels [1]
+ colour(strings) -- colour of text labels [1]
+ colour(markers) -- colour of origin markers [1]
+ colour -- colour of everything plotted (including axes and axis
labels) [1]
+ grid -- whether to draw a grid (1=yes, 0=no) [0]
+ title -- title to draw above the plot [coords title]

[""]



TRIM = _LOGICAL (Read)
``````````````````````
If TRIM is true, then an attempt will be made to trim the data to its
useful area only; this may be used to exclude non-image areas such as
overscan regions. See the EXTENT parameter for details of how the
useful area is determined. [FALSE]



USEEXT = _LOGICAL (Read)
````````````````````````
If USEEXT and TRIM are both TRUE, then the value of the EXTENT
parameter will be sought from the CCDPACK extension of each NDF. This
method will only be successful if they have been put there using the
IMPORT or PRESENT programs. [TRUE]



USESET = _LOGICAL (Read)
````````````````````````
If the pen colour is being rotated because PENROT is true, USESET
determines whether a new colour is used for each individual NDF or
each Set. If TRIM is true, it allows Set-Index-specific values of the
EXTENT parameter to be used. This parameter is ignored if PENROT and
TRIM are false, and has no effect if the input NDFs have no Set header
information.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



Examples
~~~~~~~~
drawndf reg-data* clear
This will clear the current graphics device and plot on it labelled
outlines of all the `reg-data*' NDFs, as well as axes showing the
common coordinate system in which they all reside. The plotting area
will be made just large enough that all the outlines fit in. Prior to
running this, the Current attached coordinate system of all the reg-
data* NDFs should be one in which they are all aligned.
drawndf ccd* noclear
This will attempt to plot boundaries of all the `ccd*' NDFs aligned
with whatever is already plotted on the graphics device, for instance
the result of a KAPPA DISPLAY command or of a previous call of
DRAWNDF. Parts of the NDF outlines which fall outside the existing
plot area will not be visible. If this is attempted when there is no
existing picture on the graphics device it will fail with an error.
drawndf in="one,two,three" axes labname labnum penrot
style="size(strings)=2,width(curves)=3" This will draw outlines of the
NDFs `one', `two' and `three' in the current directory with labelled
axes, in triple-thick lines and with double-size text labels which
read `1: one', `2: two' and `3: three' respectively. The colour of
each outline and its associated text label will be different from the
others.
drawndf in=a* noclear nopenrot style="colour=2" nolabel nolabnum
All the NDFs beginning with `a' will be outlined in colour 2, with no
text labels or indication of the origin.
drawndf in=gc2112 nolines image percentiles=[20,90]
The graphics device will be cleared, and the named image resampled
into its Current attached coordinate system will be displayed. The
data will be scaled such that the brightest 10% of pixels are plotted
in the highest available colour and the dimmest 20% in the lowest.
drawndf "obs-[abc]" image lines labup labopaque=false
The files obs-a, obs-b and obs-c will be plotted; both the outlines
and the pixel data will be shown, and the name of each will be drawn
upright in the middle of each one, without an opaque background.



Notes
~~~~~


+ Resampling schemes: When the IMAGE parameter is true and image
pixels are plotted, the image data has to be resampled into the
Current coordinate system prior to being displayed on the graphics
device. DRAWNDF currently does this using a nearest-neighbour
resampling scheme if the display pixels are of comparable size or
larger than the image pixels, and a block averaging scheme if they are
much smaller (less than one third the size). Though slower, this
latter scheme has the advantage of averaging out noisy data.
+ Pixel indices: The EXTENT values supplied should be given as pixel
index values. These usually start at (1,1) for the pixel at the lower
left hand corner of the data-array component (this may not be true if
the NDFs have been sectioned, in which case the lower left hand pixel
will have pixel indices equal to the data component origin values).
Pixel indices are different from pixel coordinates in that they are
non-continuous, i.e. can only have integer values, and start at 1,1
not 0,0. To change from pixel coordinates add 0.5 and round to the
nearest integer.
+ Display: The IMAGE display mode is not particularly sophisticated.
  If you wish to view a single image in its pixel coordinate system, you
  may find KAPPA's DISPLAY program more versatile.




Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application. The intrinsic default
behaviour of the application may be restored by using the RESET
keyword on the command line.
Certain parameters (LOGTO, LOGFILE, USESET and EXTENT) have global
values. These global values will always take precedence, except when
an assignment is made on the command line, or in the case of EXTENT,
if USEEXT is true. If USESET is true, a global value for EXTENT
corresponding to the Set Index of each image will be sought. Global
values may be set and reset using the CCDSETUP and CCDCLEAR commands.
The DEVICE parameter also has a global association. This is not
controlled by the usual CCDPACK mechanisms, instead it works in co-
operation with KAPPA (SUN/95) image display/control routines.
If the parameter USEEXT is true then the EXTENT parameter will be
sought first from the input NDF extensions, and only got from its
global or command-line value if it is not present there.


Copyright
~~~~~~~~~
Copyright (C) 2000-2001 Central Laboratory of the Research Councils.
All Rights Reserved.


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
DRAWNDF's communication with the AGI database is compatible with most
of KAPPA's behaviour, but is slightly less capable; in particular it
will fail to align with pictures whose alignment has been stored using
TRANSFORM structures instead of MORE.AST extensions. This affects only
older applications.


