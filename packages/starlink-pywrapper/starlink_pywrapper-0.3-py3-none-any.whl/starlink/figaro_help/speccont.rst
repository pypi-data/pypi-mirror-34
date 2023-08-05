

SPECCONT
========


Purpose
~~~~~~~
Contour a two-dimensional cut


Description
~~~~~~~~~~~
This routine displays a two-dimensional cut as a contour plot. The cut
can be an ordinary image, a long-slit spectrum, or any cut through a
spectroscopic data cube. The plot area is the current (AGI) picture of
the graphics device.
The plot can be an overlay over the most recent data picture inside
the current picture, or a new plot inside the current picture. (The
current picture after SPECCONT is the same as before.)
The screen contents of the current picture can be erased or not. If
the plot is not an overlay, then the space to be left for axis labels
as well as the exact labelling can be specified.
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
The attributes of the plot can be selected. These are

+ colour
+ line thickness
+ character height
+ simple or roman font
+ dash pattern

Most parameters default to the last used value.


Usage
~~~~~


::

    
       speccont in overlay=? world=? start=? step=? end=?
       



ADAM parameters
~~~~~~~~~~~~~~~



CLEAR = _LOGICAL (Read)
```````````````````````
If true the plot area will be cleared before plotting. [FALSE]



OVERLAY = _LOGICAL (Read)
`````````````````````````
If true then the last (AGI) data picture inside the current (AGI)
picture is used to define the plot area and its world coordinates.
Only that area will be cleared if CLEAR is true. No new labelling of
the plot will occur. [FALSE]



IN = NDF (Read)
```````````````
The input NDF. It must be two-dimensional - not counting degenerate
axes.



DEVICE = GRAPHICS (Read)
````````````````````````
The graphics display device.



FILL = _LOGICAL (Read)
``````````````````````
If false then the plot window will be adjusted to give the same plot
scale horizontally and vertically. If true, scaling is independent in
each direction and the plot will fill the area available. This
parameter is used only if OVERLAY is false. [FALSE]



ROMAN = _LOGICAL (Read)
```````````````````````
If true, PGPLOT's roman font is used for drawing text. If false, the
normal (single-stroke) font is used. [FALSE]



HEIGHT = _REAL (Read)
`````````````````````
The height of the characters measured in units of PGPLOT default text
height, which is approximately 1/40 of the height of the (AGI) base
picture (i.e. 1/40 the height of the workstation window, screen or
paper). HEIGHT will be used for labelling the plot box. The contour
labels are always half that size. [1.]



COLOUR = _INTEGER (Read)
````````````````````````
The PGPLOT colour index to be used for the plot. This can be formally
between 0 and 255, but not all devices support all colours. The
default colour representation is:

+ 0: Background,
+ 1: Foreground (default),
+ 2: Red,
+ 3: Green,
+ 4: Blue,
+ 5: Cyan,
+ 6: Magenta,
+ 7: Yellow,
+ 8: Orange,
+ 9: Green/Yellow,
+ 10: Green/Cyan,
+ 11: Blue/Cyan,
+ 12: Blue/Magenta,
+ 13: Red/Magenta,
+ 14: Dark grey,
+ 15: Light grey.





THICK = _INTEGER (Read)
```````````````````````
The PGPLOT line thickness. Can be between 1 and 21. [1]



DASH = _INTEGER (Read)
``````````````````````
The PGPLOT dash pattern:

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
Note that with the current plot software, ticks are drawn only if the
axis is drawn as well. ['----']



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
labels. ['++++']



MAJOR = _REAL (Read)
````````````````````
The distance in world coordinates between major tick marks. The first
element is for the horizontal direction, the second for the vertical
direction. This is also the distance along the axis between numeric
labels. Values of 0 cause PGPLOT to choose the major tick interval
automatically. [0.,0.]



MINOR = _INTEGER (Read)
```````````````````````
The number of minor tick intervals per major tick interval. The first
element is for the horizontal direction, the second for the vertical
direction. Values of 0 for MINOR or MAJOR cause PGPLOT to choose the
minor tick interval automatically. [0,0]



BOTTOM = _CHAR (Read)
`````````````````````
The text label for the bottom axis. Give null to construct the label
from the input NDF axis label and unit. Within the string, you can use
the following escape sequences:

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
The text label for the left axis. Give null to construct the label
from the input NDF axis label and unit. Within the string, you can use
the following escape sequences:

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
The text label for the top axis. Give null to use the title from the
input NDF. Within the string, you can use the following escape
sequences:

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
The text label for the right axis. Give null to construct the label
from the input NDF label and unit. Within the string, you can use the
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





LABSPC( 4 ) = _REAL (Read)
``````````````````````````
If the plot is not an overlay then this specifies the space left at
the bottom, left, top, and right between the plot window and the
current (AGI) picture. The space is measured as a fraction of the
current picture. Ticks and numeric labels are drawn outward from the
plot window, but text labels are drawn inward from the current
picture. The labelling space must be between zero and 0.5.
[0.1,0.1,0.05,0.05]



WORLD( 4 ) = _REAL (Read)
`````````````````````````
The world coordinates of the plot window. Give null to use the extent
of the input NDF instead. The four elements are the bounds on the
left, right, bottom, and top in that order. Left and right bound must
not be equal, neither must bottom and top. [!]



START = _REAL (Read)
````````````````````
The first contour level.



STEP = _REAL (Read)
```````````````````
The step between successive major contour levels. If zero is given
then only one contour at value START will be drawn. STEP can be
negative. In addition to the major contours, three minor contours will
be drawn between successive major contours. The major contours are
thick and labelled with the contour value. The minor contours are thin
and labelled with an arrow pointing counter-clockwise around a local
maximum.



END = _REAL (Read)
``````````````````
The last contour level. This may be adjusted slightly so as to comply
with START and STEP. If given equal to START then only one contour at
value START will be drawn. END can be smaller than START.



Examples
~~~~~~~~
speccont cube(,5,) start=2 step=2 end=10 accept
This takes the fifth xz-cut from the input cube. It draws contours at
values 2, 4, 6, 8, and 10.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.
This routine recognises and uses coordinate transformations in AGI
pictures.


