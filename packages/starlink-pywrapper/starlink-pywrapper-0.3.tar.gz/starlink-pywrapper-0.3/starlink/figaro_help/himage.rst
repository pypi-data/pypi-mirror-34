

HIMAGE
======


Purpose
~~~~~~~
Create greyscale plot of image


Description
~~~~~~~~~~~
Handles an 'HIMAGE' command, producing an image on any suitable
device. Originally based on the routine IMAGE.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) The name of the first image to be displayed.
YSTART = REAL (Read) The first Y value to be displayed. YEND = REAL
(Read) The last Y value to be displayed. XSTART = REAL (Read) The
first X value to be displayed. XEND = REAL (Read) The last X value to
be displayed. X and Y are the horizontal and vertical directions

+ as displayed on the Grinnell - respectively. The first value for
  each is 1. LOW = REAL (Read) The minimum count level for the display,
  for the first image. HIGH = REAL (Read) The maximum count level for
  the display, for the first image. PLOTDEV = CHARACTER (Read) The name
  of the plotting device ASPECT = REAL (Read) The apect ratio of the
  plot SHRINK = LOGICAL (Read) If to shrink image to leave margin all
  round LOG = LOGICAL (Read) To take logarithms of the image to display
  it




Subroutines/functions referenced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CNF_PVAL : Full pointer to dynamically allocated memory GR_FOTOR :
Plot greyscale image
DSA_AXIS_RANGE : Get range along axis to use DSA_CLOSE : Close DSA
DSA_DATA_SIZE : Get size of main data array DSA_FREE_WORKSPACE : Free
workspace DSA_GET_WORK_ARRAY : Get workspace DSA_INPUT : Open input
data file DSA_MAP_DATA : Map main data array DSA_OBJECT_NAME : Get
name of object DSA_OPEN : Open DSA CHR_LEN : Get non-blank length of
character string PAR_RDCHAR : Read character string parameter
PAR_RDKEY : Read key parameter PAR_RDVAL : Read value parameter
PAR_WRUSER : Write character string to user
KS / CIT 18th April 1984


