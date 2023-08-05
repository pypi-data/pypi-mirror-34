

IDICURS
=======


Purpose
~~~~~~~
Views and writes position lists interactively


Description
~~~~~~~~~~~
This program displays an image or Set of images on the screen and
provides a graphical user interface for marking points on it. Points
can be read in from a position list file at the start (if READLIST is
true) or written out to a position list file at the end (if WRITELIST
is true) or both. If OVERWRITE is true then a position list file can
be viewed and edited in place.
The graphical interface used for marking features on the image should
be fairly self-explanatory. The image can be scrolled using the
scrollbars, the window can be resized, and there are controls for
zooming the image in or out, changing the style of display, and
altering the percentile cutoff limits which control the mapping of
pixel value to displayed colour. The position of the cursor is
reported below the display using the coordinates of the selected
coordinate frame for information, but the position list written out is
always written in Pixel coordinates, since that is how all CCDPACK
applications expect to find it written. Points are marked on the image
by clicking mouse button 1 (usually the left one) and may be removed
using mouse button 3 (usually the right one). When you have marked all
the points that you wish to, click the 'Done' button.


Usage
~~~~~


::

    
       idicurs in
       



ADAM parameters
~~~~~~~~~~~~~~~



CENTROID = _LOGICAL (Read and Write)
````````````````````````````````````
This parameter controls whether points marked on the image are to be
centroided. If true, then when you click on the image to add a new
point IDICURS will attempt to find a centroidable object near to where
the click was made and add the point there. If no centroidable feature
can be found nearby, you will not be allowed to add a point. Note that
the centroiding routine is capable of identifying spurious objects in
noise, but where a genuine feature is nearby this should find its
centre.
Having centroiding turned on does not guarantee that all points on the
image have been centroided, it only affects points added by clicking
on the image. In particular any points read from the INLIST file will
not be automatically centroided.
This parameter only gives the initial centroiding state - centroiding
can be turned on and off interactively while the program is running.



IN = LITERAL (Read)
```````````````````
Gives the name of the NDFs to display and get coordinates from. If
multiple NDFs are specified using wildcards or separating their names
with commas, the program will run on each one in turn, or on each Set
in turn if applicable (see the USESET parameter).



INEXT = _LOGICAL (Read)
```````````````````````
If the READLIST parameter is true, then this parameter determines
where the input position list comes from. If it is true, then the
position list currently associated with the NDF will be used. If it is
false, then the input position list names will be obtained from the
INLIST parameter. [FALSE]



INLIST = FILENAME (Read)
````````````````````````
If the READLIST parameter is true, and the INEXT parameter is false,
then this parameter gives the names of the files in which the input
position list is stored. This parameter may use modifications of the
input NDF name.



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



MARKSTYLE = LITERAL (Read and Write)
````````````````````````````````````
A string indicating how markers are initially to be plotted on the
image. It consists of a comma-separated list of "attribute=value" type
strings. The available attributes are:

+ colour -- Colour of the marker in Xwindows format.
+ size -- Approximate height of the marker in pixels.
+ thickness -- Approximate thickness of lines in pixels.
+ shape -- One of Plus, Cross, Circle, Square, Diamond.
+ showindex -- 1 to show index numbers, 0 not to do so.

This parameter only gives the initial marker type; it can be changed
interactively while the program is running. If specifying this value
on the command line, it is not necessary to give values for all the
attributes; missing ones will be given sensible defaults.
["showindex=1"]



MAXCANV = _INTEGER (Read and Write)
```````````````````````````````````
A value in pixels for the maximum initial X or Y dimension of the
region in which the image is displayed. Note this is the scrolled
region, and may be much bigger than the sizes given by WINX and WINY,
which limit the size of the window on the X display. It can be
overridden during operation by zooming in and out using the GUI
controls, but it is intended to limit the size for the case when ZOOM
is large (perhaps because the last image was quite small) and a large
image is going to be displayed, which otherwise might lead to the
program attempting to display an enormous viewing region. If set to
zero, then no limit is in effect. [1280]



READLIST = _LOGICAL (Read)
``````````````````````````
If this parameter is true, then the program will start up with with
some positions already marked (where the points come from depends on
the INEXT and INLIST parameters). If it is false, the program will
start up with no points initially plotted. [FALSE]



OUTLIST = FILENAME (Write)
``````````````````````````
If WRITELIST is true, and OVERWRITE is false, then this parameter
determines the names of the files to use to write the position lists
into. It can be given as a comma-separated list with the same number
of filenames as there are IN files, but wildcards can also be used to
act as modifications of the input NDF names.
This parameter is ignored if WRITELIST is false or READLIST and
OVERWRITE are true.



OVERWRITE = _LOGICAL (Read)
```````````````````````````
If READLIST and WRITELIST are both true, then setting OVERWRITE to
true causes the input position list file to be used as the output
position list file as well. Thus, setting this parameter to true
allows position list files to be edited in place. [FALSE]



PERCENTILES( 2 ) = _DOUBLE (Read and Write)
```````````````````````````````````````````
The initial values for the low and high percentiles of the data range
to use when displaying the images; any pixels with a value lower than
the first element will have the same colour, and any with a value
higher than the second will have the same colour. Must be in the range
0 <= PERCENTILES( 1 ) <= PERCENTILES( 2 ) <= 100. These values can be
changed interactively while the program runs. [2,98]



USESET = _LOGICAL (Read)
````````````````````````
This parameter determines whether Set header information should be
used or not. If USESET is true, IDICURS will try to group images
according to their Set Name attribute before displaying them, rather
than treating them one by one. All images which share the same (non-
blank) Set Name attribute, and which have a CCD_SET attached
coordinate system, will be shown together in the viewer resampled into
their CCD_SET coordinates.
If USESET is false, then regardless of Set headers, each individual
NDF will be displayed for marking separately.
If the input images have no Set headers, or if they have no CCD_SET
coordinates in their WCS components, the value of USESET will make no
difference.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



VERBOSE = _LOGICAL (Read)
`````````````````````````
If this parameter is true, then at the end of processing all the
positions will be written through the CCDPACK log system. [TRUE]



WINX = _INTEGER (Read and Write)
````````````````````````````````
The width in pixels of the window to display the image and associated
controls in. If the image is larger than the area allocated for
display, it can be scrolled around within the window. The window can
be resized in the normal way using the window manager while the
program is running. [450]



WINY = _INTEGER (Read and Write)
````````````````````````````````
The height in pixels of the window to display the image and associated
controls in. If the image is larger than the area allocated for
display, it can be scrolled around within the window. The window can
be resized in the normal way using the window manager while the
program is running. [600]



WRITELIST = _LOGICAL (Read)
```````````````````````````
This parameter determines whether an output position list file will be
written and associated with the input images.
If the program exits normally, there are points are marked on the
image, and WRITELIST is true, then the points will be written to a
position list file and that file will be associated with the image
file. The name of the position list file is determined by the OUTLIST
and OVERWRITE parameters. The positions will be written to the file
using the standard CCDPACK format as described in the Notes section.
If WRITELIST is false, then no position lists are written and no
changes are made to the image associated position lists. [FALSE]



ZOOM = _INTEGER (Read and Write)
````````````````````````````````
A factor giving the initial level to zoom in to the image displayed,
that is the number of screen pixels to use for one image pixel. It
will be rounded to one of the values ... 3, 2, 1, 1/2, 1/3 .... The
zoom can be changed interactively from within the program. The initial
value may be limited by MAXCANV. [1]



Examples
~~~~~~~~
idicurs mosaic mos.lis
This starts up the graphical user interface, allowing you to select a
number of points which will be written to the position list file
'mos.lis', which will be associated with the image file.
idicurs in=* out=*.pts percentiles=[10,90] useset=false
Each of the NDFs in the current directory will be displayed, and the
positions marked on it written to a list with the same name as the
image but the extension '.pts', which will be associated with the
image in question. The display will initially be scaled so that pixels
with a value higher than the 90th percentile will all be displayed as
the brightest colour and those with a value lower than the 10th
percentile as the dimmest colour, but this may be changed
interactively while the program is running. Since USESET is explicitly
set to false, each input NDF will be viewed and marked separately,
even if some they have Set headers and Set alignment coordinates,
idicurs in=gc6253 readlist inlist=found.lis outlist=out.lis
markstyle="colour=skyblue,showindex=0" The image gc6253 will be
displayed, with the points stored in the position list 'found.lis'
already plotted on it. These may be added to, moved and deleted, and
the resulting list will be written to the file out.lis. Points will
initially be marked using skyblue markers, and not labelled with index
numbers.
idicurs * readlist writelist inext overwrite
All the images in the current directory will be displayed, one after
the other, with the points which are in their currently associated
position lists already plotted. You can add and remove points, and the
modified position lists will be written back into the same files.



Notes
~~~~~


+ Position list formats.

CCDPACK supports data in two formats.
CCDPACK format - the first three columns are interpreted as the
following.


+ Column 1: an integer identifier
+ Column 2: the X position
+ Column 3: the Y position

The column one value must be an integer and is used to identify
positions which are the same but which have different locations on
different images. Values in any other (trailing) columns are usually
ignored.
EXTERNAL format - positions are specified using just an X and a Y
entry and no other entries.


+ Column 1: the X position
+ Column 2: the Y position

This format is used by KAPPA applications such as CURSOR.
Comments may be included in a file using the characters "#" and "!".
Columns may be separated by the use of commas or spaces.
Input position lists read when READLIST is true may be in either of
these formats. The output list named by the OUTLIST parameter will be
written in CCDPACK (3 column) format.
In all cases, the coordinates in position lists are pixel coordinates.


+ NDF extension items.

On normal exit, unless OUTLIST is set to null (!), the CURRENT_LIST
items in the CCDPACK extensions (.MORE.CCDPACK) of the input NDFs are
set to the name of the output list. These items will be used by other
CCDPACK position list processing routines to automatically access the
list.


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
Certain parameters (LOGTO, LOGFILE and USESET) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.
Some of the parameters (MAXCANV, PERCENTILES, WINX, WINY, ZOOM,
MARKSTYLE, CENTROID) give initial values for quantities which can be
modified while the program is running. Although these may be specified
on the command line, it is normally easier to start the program up and
modify them using the graphical user interface. If the program exits
normally, their values at the end of the run will be used as defaults
next time the program starts up.


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


