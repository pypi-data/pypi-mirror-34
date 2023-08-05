

SPECPLOT
========


Purpose
~~~~~~~
Plot a spectrum


Description
~~~~~~~~~~~
This routine plots a spectrum (or any one-dimensional NDF section) in
the current (AGI) picture of the graphics device.
The plot can basically be an overlay over the most recent data picture
inside the current picture, or a new plot inside the current picture.
(The current picture after SPECPLOT is the same as before.)
The screen contents of the current picture can be erased or not.
The plot location and size is governed by the outer and the inner box.
The inner box is the area where data are plotted, the outer box
contains the inner box and the plot labels.
In the overlay case the inner box and its world coordinates are
identified with the most recent data picture inside the current
picture. No labelling is done in the overlay case, so the outer box
has no meaning in this case.
In the case of a new plot, the outer box will be identified with the
current picture, although the plot labels are allowed to extend beyond
this area. Depending on the choice of labelling, a sensible location
for the inner box is offered. After the inner box is specified, its
world coordinates are enquired. The prompt values correspond to the
extreme values found in the data. The location and world coordinates
of the inner box are saved as a data picture in the AGI data base.
The labelling consists of axes, axis ticks, numeric labels at the
major ticks, and text labels. The axes are counted from bottom
clockwise. Each axis can be drawn or not. Each drawn axis can have
ticks or not. Each axis can have numeric labels or not. The left and
right axes can have either horizontal (orthogonal) or vertical
(parallel) numeric labels. Each axis can have a text label or not.
The kind of labelling is controlled by several 4-character strings.
Each character is the switch for axis 1, 2, 3, 4 respectively. "0"
turns an option off for that axis, "+" turns it on. For the ticks and
for numeric labels of axes 2 and 4, "-" is also allowed. It yields
inward ticks and vertical numeric labels.
The data can be plotted as a set of markers, as a line-style polygon
connecting the data points, or as a bin-style polygon. In addition
error bars or pixel width bars can be plotted. Each of the options can
be selected independent of the others, i.e. several (or all) options
can be selected at the same time. If no variance information is
available, error bars are de-selected automatically. Bad data are
omitted from the plot. If error bars are selected, bad variances cause
the corresponding data also to be omitted.
The attributes of the plot can be selected. These are

+ colour
+ line thickness
+ character height (equivalent to marker size)
+ simple or roman font
+ dash pattern for polygon connections

Most parameters default to the last used value.


Usage
~~~~~


::

    
       specplot in overlay=? bottom=? left=? top=? right=?
          labspc=? world=?
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, the routine will issue only error messages and no
informational messages. [TRUE]



CLEAR = _LOGICAL (Read)
```````````````````````
If true, the part of the graphics device corresponding to the current
(AGI) picture is erased before the plot is drawn. [FALSE]



OVERLAY = _LOGICAL (Read)
`````````````````````````
If true, the plot will be an overlay on the most recent (AGI) data
picture within the current (AGI) picture. If false, the plot will be
user-defined, but the inner box is restricted to the current (AGI)
picture.



IN = NDF (Read)
```````````````
The input NDF.



LIN = _LOGICAL (Read)
`````````````````````
If true, the data points will be connected by a line-style polygon.
[TRUE]



BIN = _LOGICAL (Read)
`````````````````````
If true, the data points will be connected by a bin-style (or
histogram-style) polygon. [FALSE]



MARK = _INTEGER (Read)
``````````````````````
This parameter determines the kind of marker to be drawn at each data
point [0]:

+ 0: No markers drawn,
+ 1: Diagonal cross,
+ 2: Asterisk,
+ 3: Open circle,
+ 4: Open square,
+ 5: Filled circle,
+ 6: Filled square.





ERROR = _LOGICAL (Read)
```````````````````````
If true and variance information available, error bars will be drawn.
[FALSE]



WIDTH = _LOGICAL (Read)
```````````````````````
If true, the pixel width will be indicated by horizontal bars. [FALSE]



ROMAN = _LOGICAL (Read)
```````````````````````
If true, PGPLOT's roman font is used for drawing text. If false, the
normal (single-stroke) font is used. [FALSE]



HEIGHT = _REAL (Read)
`````````````````````
The height of the characters. This also affects the size of the
markers. Markers are about half the size of characters. The height is
measured in units of PGPLOT default text heights, which is
approximately 1/40 of the height of the (AGI) base picture (i.e. 1/40
the height of the workstation window, screen or paper). [1.]



COLOUR = _INTEGER (Read)
````````````````````````
The PGPLOT colour index to be used for the plot. This can be formally
between 0 and 255, but not all devices support all colours. The
default colour representation is:

+ 0: Background, - 1: Foreground (default),
+ 2: Red, - 3: Green,
+ 4: Blue, - 5: Cyan,
+ 6: Magenta, - 7: Yellow,
+ 8: Orange, - 9: Green/Yellow,
+ 10: Green/Cyan, - 11: Blue/Cyan,
+ 12: Blue/Magenta, - 13: Red/Magenta,
+ 14: Dark grey, - 15: Light grey.





THICK = _INTEGER (Read)
```````````````````````
The PGPLOT line thickness. Can be between 1 and 21. [1]



DASH = _INTEGER (Read)
``````````````````````
The PGPLOT dash pattern [1]:

+ 1: Full line,
+ 2: Long dash,
+ 3: Dash-dot-dash-dot,
+ 4: Dotted,
+ 5: Dash-dot-dot-dot.





AXES = _CHAR (Read)
```````````````````
Array of switches to turn on or off the drawing of either of the four
box sides. The sides are counted from bottom clockwise: bottom, left,
top, right. Any switch can be "0" or "+". E.g. '00++' would switch off
the bottom and left axes and switch on the top and right axes.
['++++']



TICK = _CHAR (Read)
```````````````````
Array of switches to turn on or off the drawing of ticks along either
axis. Ticks are drawn only if the corresponding axis is also drawn.
The sides are counted from bottom clockwise: bottom, left, top, right.
Any switch can be "0", "+" or "-". E.g. '00+-' would switch off the
bottom and left ticks and switch on the top and right ticks. The top
axis would have ticks outward, the right axis would have ticks inward.
['----']



NUML = _CHAR (Read)
```````````````````
Array of switches to turn on or off the drawing of numeric labels
along either axis. The sides are counted from bottom clockwise:
bottom, left, top, right. Any switch can be "0" or "+"; the second and
fourth switch can also be "-". E.g. '0+0-' would switch off the bottom
and top labels and switch on the left and right labels. The left axis
would have labels horizontal (orthogonal), the right axis would have
labels vertical (parallel). ['++00']



TEXT = _CHAR (Read)
```````````````````
Array of switches to turn on or off the drawing of text labels along
either axis. The sides are counted from bottom clockwise: bottom,
left, top, right. Any switch can be "0" or "+". E.g. '0++0' would
switch off the bottom and right labels and switch on the left and top
labels. ['+++0']



NORTHO = _REAL (Read)
`````````````````````
If orthogonal numeric labels have been selected, you must specify how
much space there must be between the axis and the text label, i.e. how
long the longest numeric label along the left or right axis will be.
The unit is character heights. [1]



MAJOR( 2 ) = _REAL (Read)
`````````````````````````
The distance in world coordinates between major tick marks. The first
element is for the horizontal direction, the second for the vertical
direction. This is also the distance along the axis between numeric
labels. Values of 0 cause PGPLOT to choose the major tick interval
automatically. [0.,0.]



MINOR( 2 ) = _INTEGER (Read)
````````````````````````````
The number of minor tick intervals per major tick interval. The first
element is for the horizontal direction, the second for the vertical
direction. Values of 0 for MINOR or MAJOR cause PGPLOT to choose the
minor tick interval automatically. [0,0]



BOTTOM = _CHAR (Read)
`````````````````````
The text label for the first axis. Within the string, you can use the
following escape sequences:

+ \fn Normal (single stroke) font,
+ \fr Roman font,
+ \fi Italic font,
+ \fs Script font,
+ \u Superscript (use only paired with \d),
+ \d Subscript (use only paired with \u),
+ \b Backspace,
+ \\ Backslash,
+ \A Danish umlaut (Angstroem),
+ \g Any greek letter.





LEFT = _CHAR (Read)
```````````````````
The text label for the second axis. Within the string, you can use the
following escape sequences:

+ \fn Normal (single stroke) font,
+ \fr Roman font,
+ \fi Italic font,
+ \fs Script font,
+ \u Superscript (use only paired with \d),
+ \d Subscript (use only paired with \u),
+ \b Backspace,
+ \\ Backslash,
+ \A Danish umlaut (Angstroem),
+ \g Any greek letter.





TOP = _CHAR (Read)
``````````````````
The text label for the third axis. Within the string, you can use the
following escape sequences:

+ \fn Normal (single stroke) font,
+ \fr Roman font,
+ \fi Italic font,
+ \fs Script font,
+ \u Superscript (use only paired with \d),
+ \d Subscript (use only paired with \u),
+ \b Backspace,
+ \\ Backslash,
+ \A Danish umlaut (Angstroem),
+ \g Any greek letter.





RIGHT = _CHAR (Read)
````````````````````
The text label for the fourth axis. Within the string, you can use the
following escape sequences:

+ \fn Normal (single stroke) font,
+ \fr Roman font,
+ \fi Italic font,
+ \fs Script font,
+ \u Superscript (use only paired with \d),
+ \d Subscript (use only paired with \u),
+ \b Backspace,
+ \\ Backslash,
+ \A Danish umlaut (Angstroem),
+ \g Any greek letter.





DEVICE = DEVICE (Read)
``````````````````````
The graphics device for the plot.



LABSPC( 4 ) = _REAL (Read)
``````````````````````````
The space between outer box (AGI current picture) and inner box
measured in units of character heights. The four numbers are for the
bottom, left, top, right labelling space in that order. The dynamic
default offered is based on the space requirements for the axis
labelling, and can in general be accepted.



WORLD( 4 ) = _REAL (Read)
`````````````````````````
The world coordinates that the left, right, bottom and top ends of the
inner box should correspond to. The dynamic default is based on the
coordinates of the first and last pixel of the selected subset and on
the extreme data values of the selected subset. Reverse axes can be
achieved by giving WORLD(1) > WORLD(2) and/or WORLD(3) > WORLD(4).



Examples
~~~~~~~~
specplot spectrum accept
This is the simplest way to plot a 1-D data set in its full length.
specplot imagerow(-100.:50.,15.) accept
This will take a 2-D data set IMAGEROW and plot part of the row
specified by the second coordinate being 15. The part of the row
plotted corresponds to the first coordinate being between -100 and
+50. Note that the decimal point forces use of axis data. Omitting the
period would force use of pixel numbers.
specplot imagecol(15.,-100.:50.) accept
This will take a 2-D data set IMAGEROW and plot part of the column
specified by the first coordinate being 15. The part of the row
plotted corresponds to the second coordinate being between -100 and
+50. Note that the decimal point forces use of axis data. Omitting the
period would force use of pixel numbers.
specplot spectrum lin=false bin=true accept
Replace direct connections between data points by bin-style
connections.
specplot spectrum mark=1 accept
Mark each data point by a diagonal cross.
specplot spectrum error=true width=true accept
Draw an error bar and a pixel width bar for each data point.
specplot spectrum roman=true height=1.5 colour=3 accept
Draw text with the roman font, draw text and makers 1.5 times their
normal size, and plot the whole thing in green colour.
specplot spectrum bottom=Weekday left="Traffic noise [dBA]" accept
Specify text labels on the command line instead of constructing them
from the file's axis and data info.
specplot spectrum overlay=true clear=false accept
The position and scale of the plot are determined by the previous plot
(which might have been produced by a different application).
specplot spectrum world=[0.,1.,-1.,1.] accept
Use plot limits different from the extreme data values.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.
This routine recognises and uses coordinate transformations in AGI
pictures.


