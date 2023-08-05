

FIBSEP
======


Purpose
~~~~~~~
Isolate output from different fibres


Description
~~~~~~~~~~~
Handles an 'FIBSEP' command, producing an image on any suitable
device. The user can then select fibres at either end (in the Y
direction), and give a number. The program then will locate the fibre
spectra in between. This assumes that a correction has been made
previously for S-distortion. Originally based on the routine IMAGE.


Parameters
~~~~~~~~~~
IMAGE = FILE (Read) The name of the input image YSTART = REAL (Read)
The first Y value to be displayed. YEND = REAL (Read) The last Y value
to be displayed. XSTART = REAL (Read) The first X value to be
displayed. XEND = REAL (Read) The last X value to be displayed. X and
Y are the horizontal and vertical directions

+ as displayed - respectively. The first value for each is 1. LOW =
  REAL (Read) The minimum count level for the display, for the first
  image. HIGH = REAL (Read) The maximum count level for the display, for
  the first image. PLOTDEV = CHARACTER (Read) The name of the plotting
  device OUTPUT = FILE (Write) The name of the output image LOG =
  LOGICAL (Read) To take logarithms of the image to display it




