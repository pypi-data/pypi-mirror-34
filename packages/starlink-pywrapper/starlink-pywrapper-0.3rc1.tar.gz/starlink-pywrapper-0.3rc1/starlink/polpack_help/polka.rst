

POLKA
=====


Purpose
~~~~~~~
Creates Stokes vectors from a set of 2-dimensional intensity frames


Description
~~~~~~~~~~~
This application converts a set of 2D intensity frames into a 3D cube
containing a Stokes vector for every measured pixel on the sky. It may
also be used as an image alignment tool for non-polarimetric data (see
parameter POL). It cannot be used with 3D intensity frames (e.g.
spectropolarimetry data).
The main processes applied to the data are:
1) Extraction of the required sub-regions from each input frame.
2) Alignment of all extracted sub-regions using stars within the
field.
3) Sky subtraction within each aligned sub-region.
4) Calculation of a Stokes vector for each pixel. This step may be
omitted if required by supplying a null value for parameter OUT_S.
The inputs to this application are a set of intensity frames which
have been corrected to remove any instrumental effects introduced by
the detector (such as de-biassing, flat-fielding, etc). Output Stokes
vectors can only be produced if all input frames contain a POLPACK
extension (see application POLIMP). In dual-beam mode, each input
frame contains two images of the sky (the O and E ray images). In
single-beam mode, each input frame contains only a single image of the
sky.
The outputs from this application consist of the aligned, sky-
subtracted intensity images, and the cube holding the Stokes vectors.
In dual beam mode two output intensity frames are created for each
input frame, one containing the O ray image, and the other containing
the E ray image. In single-beam mode one output intensity frame is
created for each input frame, holding the usable area of the
corresponding input frame. The user may choose not to create any or
all of these outputs. For instance, the Stokes vectors may be produced
without retaining the aligned intensity images (see parameters OUT_S,
OUT_E, OUT_O and OUT).
Use of this application divides into two stages. In the first stage, a
Graphical User Interface (GUI) is used to obtain all the information
required to produce the output data files from the user. This includes
identifying stars, masks and sky regions on each of the supplied input
images. This is the labour-intensive bit. Once this has been completed
your satisfaction, the second stage is entered in which the output
data files are created. Once initiated, no further interaction on your
part is required. This is the computationally intensive bit. The GUI
makes use of various applications from POLPACK, KAPPA and CCDPACK to
perform all these tasks. Note, if the find the image display area too
small for comfort you can make it bigger using the DPI parameter
described below.
A step-by-step tutorial on the use of the GUI is available within the
"Help" menu at the right hand end of the menu bar (see also the
STARTHELP parameter).
Various options controlling the behaviour of the GUI can be set on the
command line by assigning values to the parameters listed below.
Alternatively, most of them can be set using the "Options" menu in the
menu bar at the top of the GUI. If not supplied on the command line,
these parameters usually adopt the values they had on the previous
invocation of POLKA. The values shown in square brackets in the
parameter descriptions below are the initial default values.


Usage
~~~~~


::

    
       polka in out_s
       



ADAM parameters
~~~~~~~~~~~~~~~



BADCOL = LITERAL (Update)
`````````````````````````
The colour with which to represent missing data in the image display.
This should be one of RED, BLUE, GREEN, CYAN, MAGENTA, YELLOW, BLACK.
Any unambiguous abbreviation can be supplied, and the value is case-
insensitive. [CYAN]



CURCOL = LITERAL (Update)
`````````````````````````
The colour with which to mark the objects (i.e. image features and
masks) currently being entered by the user. This should be one of RED,
BLUE, GREEN, CYAN, MAGENTA, YELLOW, BLACK. Any unambiguous
abbreviation can be supplied, and the value is case-insensitive. [RED]



DPI = _INTEGER (Read)
`````````````````````
The dots per inch on the display screen. Some X servers fail to supply
the correct value, resulting in the GUI being unpleasantly small or
large. For this reason, an explicit value may be supplied using this
parameter. If a null (!) value is supplied, then the DPI value
returned by the X server is used. This parameter may also be used to
adjust the size of the GUI to the user's preference, even if the DPI
value returned by the X server is correct. Note, this value cannot be
set from the GUI's "Options" menu. [!]



DUALBEAM = _LOGICAL (Read)
``````````````````````````
If a TRUE value is supplied, then POLKA will operate in dual-beam
mode, producing two output images for each input image. Otherwise, it
will operate in single-beam mode, with one output image being produced
for each input image. In single-beam mode, the output image is
notionally referred to as the "O-ray" image, and all the GUI controls
related to the E-ray areas are disabled. This parameter is only used
when processing polarimeter data (see parameter POL). It's value
cannot be set from the "Options" menu within the GUI. [TRUE]



FITTYPE = _INTEGER (Update)
```````````````````````````
The type of mapping which should be used between images. This may take
any of the following values:
1 - Shift of origin.
2 - Shift of origin and rotation.
3 - Shift of origin and magnification.
4 - Shift of origin, rotation and magnification.
Only mapping types 1 and 3 are available when processing dual-beam
polarimeter data. Mapping types 2 and 4 are also available when
processing single-beam data. [1]



HELPAREA = _LOGICAL (Update)
````````````````````````````
If a TRUE value is supplied, then dynamic help information will be
displayed in a box at the bottom of the GUI. This information is
continuously updated to describe the control or area currently under
the mouse pointer. [TRUE]



IN = NDF (Read)
```````````````
A group of 2-d input intensity frames. This may take the form of a
comma separated list of file names, or any of the other forms
described in the help on "Group Expressions". Note, the input frames
cannot be specified within the GUI. See also parameter REFIN.



LOGFILE = LITERAL (Read)
````````````````````````
The name of a log file to which will be written all the messages
generated by the applications activated by the GUI. If "stdout" is
supplied, then the messages will be directed to standard output
(usually the screen). If a null (!) value is supplied, then no log
file will be created. Note, this parameter cannot be set from the
GUI's "Options" menu. [!]



OEFITTYPE = _INTEGER (Update)
`````````````````````````````
The type of mapping which should be used between O and E rays. See
parameter FITTYPE for a description of the allowed values. This
parameter is only accessed when processing polarimeter data (see
parameter POL). [1]



OUT = LITERAL (Write)
`````````````````````
A group specifying the names of the output intensity images to create
in single-beam mode, or when processing non-polarimeter data (see
parameters DUALBEAM and POL). The specified names should correspond
one-for-one to the input images. See the help on "Group Expressions"
for information on the allowed formats for this list. Any asterisk
within the supplied string is replaced in turn by each of the input
image names. If a null (!) value is given, then the intensity images
are not saved. Note, the output images cannot be specified within the
GUI.



OUT_E = LITERAL (Write)
```````````````````````
A group specifying the names of the E-ray output intensity images to
create in dual-beam mode (see parameter DUALBEAM). These should
correspond one-for-one to the input images. See the help on "Group
Expressions" for information on the allowed formats for this list. Any
asterisk within the supplied string is replaced in turn by each of the
input image names. If a null (!) value is given, then the E-ray
intensity images are not saved. Note, the output images cannot be
specified within the GUI.



OUT_O = LITERAL (Write)
```````````````````````
A group specifying the names of the O-ray output intensity images to
create in dual-beam mode (see parameter DUALBEAM). These should
correspond one-for-one to the input images. See the help on "Group
Expressions" for information on the allowed formats for this list. Any
asterisk within the supplied string is replaced in turn by each of the
input image names. If a null (!) value is given, then the E-ray
intensity images are not saved. Note, the output images cannot be
specified within the GUI.



OUT_S = NDF (Write)
```````````````````
The name of the output cube to hold the Stokes parameters calculated
from the input images. If a null value is given then no Stokes
parameters are calculated. Note, the output cube cannot be specified
within the GUI. This parameter is only accessed when processing
polarimeter data (see parameter POL).



PERCENTILES( 2 ) = _REAL (Update)
`````````````````````````````````
The percentiles that define the scaling limits for the displayed
images. For example, [25,75] would scale between the quartile values.
[5,95]



PMODE = LITERAL (Read)
``````````````````````
The type of polarization being measured; Linear or Circular. This
parameter is only accessed if an output cube holding Stokes parameters
is being created (i.e. if OUT_S is not given a null (!) value).
[Linear]



POL = _LOGICAL (Read)
`````````````````````
Indicates the nature of the input Frames. Input frames containing non-
polarimeter data may be aligned and sky subtracted using POLKA if
parameter POL is assigned a FALSE value. This indicates that the input
intensity frames are not to be treated as polarimeter data. In this
case, Stokes vectors may not be produced (see parameter OUT_S). The
use of the GUI is the same as in single-beam mode (see parameter
DUALBEAM). [TRUE]



PSFSIZE = _INTEGER (Update)
```````````````````````````
This value controls the centroiding process which is used to find
accurate centres for the features identified using the mouse. It
should be set roughly to the width (in pixels) of the features which
are to be used to align the images. If the accurate positions wander
too far from the original position, then a smaller value should be
supplied. If it is set to zero, then no centroiding is performed, and
the raw feature positions are used as supplied. [3]



REFIN = NDF (Read)
``````````````````
An intensity frame defining the reference co-ordinate system. The
images specified by parameter IN will be aligned with this image. If a
null (!) value is supplied, the first image in the group supplied for
parameter IN is used as the reference image. If the reference image is
specified using paremeter IN, it will be processed like the other
images. If the reference image is specified using parameter REFIN, it
will not be processed. No aligned, extracted images will be created
from it, and it will not be included in the calculation of the Stokes
parameters. [!]



REFCOL = LITERAL (Update)
`````````````````````````
The colour with which to mark the reference objects (i.e. image
features or masks). This should be one of RED, BLUE, GREEN, CYAN,
MAGENTA, YELLOW, BLACK. Any unambiguous abbreviation can be supplied,
and the value is case-insensitive. [GREEN]



SELCOL = LITERAL (Update)
`````````````````````````
The colour with which to mark the selected area of the image (if any).
This should be one of RED, BLUE, GREEN, CYAN, MAGENTA, YELLOW, BLACK.
Any unambiguous abbreviation can be supplied, and the value is case-
insensitive. [RED]



SKYFRAMES = NDF (Read)
``````````````````````
A group specifying the sky frames to use. These frames are subtracted
from the supplied object frames before the output images are created.
If only one sky frame is supplied, then it is used for all the object
frames. Otherwise, the number of sky frames must equal the number of
object frames supplied using parameter IN, and must be given in the
same order. If a null value (!) is given for SKYFRAMES, then the sky
background to be subtracted from each output image is determined by
fitting a surface to sky areas identified by the user within the
supplied object frames. [!]



SKYPAR = _INTEGER (Update)
``````````````````````````
If no sky frames are supplied using parameter SKYFRAMES, then the sky
in each output image will be fitted using a polynomial surface. The
order of the fit on each axis is given by this parameter (SKYPAR). A
value of 0 will result in a flat surface (i.e. a constant value) being
used, 1 will result in a linear surface, 2 in a quadratic surface,
etc. The supplied value must be in the range 0 to 14. [0]



SKYOFF = _LOGICAL (Update)
``````````````````````````
If a TRUE value is supplied, then the sky background is removed from
each output image. Otherwise, no sky background is removed. The method
used to estimate the sky background is determined by the SKYFRAMES
parameter. [TRUE]



STARTHELP = _LOGICAL (Read)
```````````````````````````
If a TRUE value is supplied, then a hyper-text browser will be created
with the GUI, displaying the tutorial page of the POLKA on-line help
documentation. Otherwise, the browser is only created if the user
accesses the on-line help information explicitly from within the GUI
by using the "Help" menu or the F1 key on the keyboard. [TRUE]



STATUSAREA = _LOGICAL (Update)
``````````````````````````````
If a TRUE value is supplied, then information describing the currently
displayed image, current options values, etc, will be displayed in a
box underneath the displayed image. The contents of this box can be
selected using the "Options" menu in the GUI. [TRUE]



VIEW = LITERAL (Update)
```````````````````````
This controls how images are placed within the image display area of
the GUI when a new image is selected using the "Images" menu. It may
take one of the following values:

+ ZOOMED -- The new image is displayed with the current zoom factor
and image centre.
+ UNZOOMED -- The zoom factor and image centre are reset so that the
  new image just fills the image display area in at least one dimension.
  [ZOOMED]





XHAIR = _LOGICAL (Update)
`````````````````````````
If a TRUE value is supplied, then a cross hair will be used instead of
a pointer while the mouse is over the image display area. [TRUE]



XHAIRCOL = LITERAL (Update)
```````````````````````````
The colour with which to draw the cross-hair (if required). This
should be one of RED, BLUE, GREEN, CYAN, MAGENTA, YELLOW, BLACK. Any
unambiguous abbreviation can be supplied, and the value is case-
insensitive. [YELLOW]



Examples
~~~~~~~~
polka 'im1,im2,im3,im4' cube out_o=! out_e=!
This example aligns and extracts the O and E ray areas from the four
images 'im1' to 'im4', subtracts a sky background from each (estimated
from areas within the object frames), and stores the corresponding
Stokes vectors in 'cube'. The aligned intensity images are not saved.
polka ^in.lis out=^out.lis out_s=! dualbeam=no skyframes=^sky.lis
reset
This example uses single-beam mode. It reads the names of input images
from the text file 'in.lis', subtracts the sky frames read from the
text file 'sky.lis', aligns them and stores them in the images named
in the text file 'out.lis'. All other parameters are reset to their
initial default values listed in the parameter descriptions above. No
Stokes vectors are produced.



Notes
~~~~~


+ If present, WCS information is copied from each input NDF to the
corresponding output NDFs.
+ The following components are added to the POLPACK extension in the
output intensity images (the extension is first created if it does not
already exist):
+ RAY -- A string identifying which of the two rays the image
contains. This will be either "O" or "E". This is only written in
dual-beam mode (see parameter DUALBEAM).
+ IMGID -- An string identifier for the input image from which the
output image was derived. If the input image already contains a
POLPACK extension with a IMGID value, then the IMGID value is copied
unchanged to the corresponding output images. Otherwise, the name of
the input image (without a directory path) is used.
+ The following components are added to the POLPACK extension in the
output cube holding Stokes parameter (the extension is first created
if it does not already exist):
+ STOKES -- A string containing one character for each plane in the
data cube. Each character identifies the quantity stored in the
corresponding plane of the data array, and will be one of I, Q, U or
V.
+ Intermediate files created during the execution of POLKA are stored
  in a separate directory created each time POLKA is run, and deleted
  when POLKA exits. The directory will have a name of the form
  "polka_temp_<nnn>" where <nnn> is some number. This directory will be
  created within the directory specified by the HDS_SCRATCH environment
  variable. If HDS_SCRATCH is not defined then it will be created within
  the current directory.




Copyright
~~~~~~~~~
Copyright (C) 1999-2007 Central Laboratory of the Research Councils


