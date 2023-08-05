

CCDALIGN
========


Purpose
~~~~~~~
Aligns images graphically by interactive object selection


Description
~~~~~~~~~~~
This program aids the registration of NDFs which may not be related by
simple offsets (see FINDOFF and PAIRNDF if they are). It also has the
capability of dealing with groups of NDFs which are almost registered
(frames which have not been moved on the sky) saving effort in re-
identification of image features.
The basic method used is to supply a list of NDFs and an optional
reference NDF. The first NDF or the reference NDF is initially
displayed and you are invited to mark the positions of centroidable
image features on it using a graphical interface. This window then
remains on the screen for reference while you identify the same
features on each of the other images in the same way.
After centroiding you are then given the option to stop. If you decide
to, then you will have labelled position lists to use in the other
CCDPACK routines (the labelled positions will be called NDF_NAME.acc).
If you choose the option to continue then a full registration of the
NDFs will be attempted. This may only be performed for 'linear'
transformations.
After choosing a transformation type the procedure will then go on to
calculate a transformation set between all the NDFs; this is used
(with the extended reference set from REGISTER) to approximate the
position of all possible image features, which are then located by
centroiding and a final registration of all NDFs is performed. The
resultant NDFs then have associated lists of labelled positions, and
attached coordinate systems which may be used to transform other
position lists or when resampling the data.
If the EXTRAS parameter is true you may also enter, for each of the
original images, a group of images which is almost registered with it
(within the capabilities of centroiding, i.e. a few pixels). In this
way similar registration processes can be performed on many almost-
aligned images without additional work from the user.
The graphical interface used for marking features on the image should
be fairly self-explanatory. The image can be scrolled using the
scrollbars, the window can be resized, and there are controls for
zooming the image in or out, changing the style of display and
altering the percentile cutoff limits. The displayed index numbers of
any identified features on each image must match those on the
reference image (though it is not necessary to identify all of the
features from the reference image on each one), and there is also a
control for selecting the number of the next point to mark. Points are
added by clicking mouse button 1 (usually the left one) and may be
removed by clicking mouse button 3 (usually the right one). It is
possible to edit the points marked on the reference image while you
are marking points on the other images. When you have selected all the
points you wish to on a given image, click the 'Done' button and you
will be presented with the next one.


Usage
~~~~~


::

    
       ccdalign in
       



ADAM parameters
~~~~~~~~~~~~~~~



CONTINUE = _LOGICAL (Read)
``````````````````````````
If TRUE then this command will proceed to also work out the
registrations of your images. Note that this is only possible if you
are intending to use linear transformations (this is the usual case).
[FALSE]



EXTRAS = _LOGICAL (Read)
````````````````````````
If this parameter is true, then for each NDF (or Set of NDFs, if
USESET is true) from the IN list you will be prompted to enter a group
of corresponding names which represent more files of the same type
pointing at (almost) the same sky position as the one in the IN list.
CCDALIGN will then centroid the marked objects in all the images in
the same group so that multiple similar registrations can be done at
the same time. [FALSE]



FITTYPE = _INTEGER (Read)
`````````````````````````
The type of fit which should be used when determining the
transformation between the input positions lists. This may take the
values

+ 1 -- shift of origin
+ 2 -- shift of origin and rotation
+ 3 -- shift of origin and magnification
+ 4 -- shift of origin, rotation and magnification (solid body)
+ 5 -- a full six parameter fit
+ 6 -- self defined function

[5]



IN = LITERAL (Read)
```````````````````
A list of the NDFs to be displayed in the GUI for interactive marking
of features. The names should be separated by commas and may include
wildcards.



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the CCDPACK logfile. If a null (!) value is given for this
parameter then no logfile will be written, regardless of the value of
the LOGTO parameter.
If the logging system has been initialised using CCDSETUP then the
value specified there will be used. Otherwise, the default is
'CCDPACK.LOG'. [CCDPACK.LOG]



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
value specified there will be used. Otherwise, the default is 'BOTH'.
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

This parameter only gives the initial marker type; it can be changed
interactively while the program is running. If specifying this value
on the command line, it is not necessary to give values for all the
attributes; missing ones will be given sensible defaults. [""]



MAXCANV = INTEGER (Read and Write)
``````````````````````````````````
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



MORE = LITERAL (Read)
`````````````````````
If EXTRAS is true, this parameter is used to get a list of images
corresponding to each one which is named by the IN parameter. These
lists are always got interactively; MORE values cannot be given on the
command line. For any given response the null value (!) may be
supplied, indicating that there are no similarly aligned images. If
the original image is included again in the supplied MORE value, it
will be ignored, since it already forms part of the group being
considered. [!]



PERCENTILES( 2 ) = _DOUBLE (Read)
`````````````````````````````````
The initial low and high percentiles of the data range to use when
displaying the images; any pixels with a value lower than the first
element will have the same colour, and any with a value higher than
the second will have the same colour. Must be in the range 0 <=
PERCENTILES( 1 ) <= PERCENTILES( 2 ) <= 100. This can be changed from
within the GUI. [2,98]



REFNDF = LITERAL (Read)
```````````````````````
The name of an additional reference image (or Set); this is the first
image displayed and the one which will be visible while you are
marking points on all the others. If the null value (!) is supplied
then no additional reference image will be used, and the first one in
the IN list will be the first displayed. [!]



USESET = _LOGICAL (Read)
````````````````````````
This parameter determines whether Set header information will be used.
If USESET is true, then CCDALIGN will try to group images according to
their Set Name attribute before displaying them, rather than treating
them one by one. All images in the IN list which share the same (non-
blank) Set Name attribute, and which have a CCD_SET attached
coordinate system, will be shown together as a single image in the
viewer for object marking, plotted in their CCD_SET coordinates.
If USESET is false, then regardless of Set headers, each individual
NDF will be displayed for marking separately. If the input images have
no Set headers, or if they have no CCD_SET coordinates in their WCS
components, the value of this parameter will make no difference.
If a global value for this parameter has been set using CCDSETUP than
that value will be used. [FALSE]



WINX = INTEGER (Read and Write)
```````````````````````````````
The width in pixels of the window to display the image and associated
controls in. If the image is larger than the area allocated for
display, it can be scrolled around within the window. The window can
be resized in the normal way using the window manager while the
program is running. [450]



WINY = INTEGER (Read and Write)
```````````````````````````````
The height in pixels of the window to display the image and associated
controls in. If the image is larger than the area allocated for
display, it can be scrolled around within the window. The window can
be resized in the normal way using the window manager while the
program is running. [600]



ZOOM = DOUBLE (Read and Write)
``````````````````````````````
A factor giving the initial level to zoom in to the image displayed,
that is the number of screen pixels to use for one image pixel. It
will be rounded to one of the values ... 3, 2, 1, 1/2, 1/3 .... The
zoom can be changed interactively from within the program. The initial
value may be limited by MAXCANV. [1]



Examples
~~~~~~~~
ccdalign * continue=no
This will display all the images in the current directory and invite
you to mark corresponding image features on each one in turn. When you
have done this, the centroids will be calculated and you will be left
with a position list with the extension `.acc' associated with each
one.
ccdalign "x1008,x1009,x1010" refndf=xmos extras=yes continue
Here the EXTRAS parameter is true, so for each of the named images you
will be prompted for a list of other images which were taken pointing
in the same direction. The file `xmos' is being used as the reference
image, so that will be presented first for marking features. When you
have marked features on all four images, the program will go on to
match them all up and produce a global registration, attaching a new
coordinate system in which they are all registered to each file.



Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
All parameters retain their current value as default. The 'current'
value is the value assigned on the last run of the application. If the
application has not been run then the 'intrinsic' defaults, as shown
in the parameter help, apply.
Certain parameters (LOGTO, LOGFILE and USESET) have global values.
These global values will always take precedence, except when an
assignment is made on the command line. Global values may be set and
reset using the CCDSETUP and CCDCLEAR commands.
Some of the parameters (MAXCANV, PERCENTILES, WINX, WINY, ZOOM,
MARKSTYLE) give initial values for quantities which can be modified
while the program is running. Although these may be specified on the
command line, it is normally easier to start the program up and modify
them using the graphical user interface. If the program exits
normally, their values at the end of the run will be used as defaults
next time the program starts up.


Copyright
~~~~~~~~~
Copyright (C) 1997-2001 Central Laboratory of the Research Councils.
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


