

SPECGRID
========


Purpose
~~~~~~~
Plot spectra on position grid


Description
~~~~~~~~~~~
This routine takes an NDF and displays all the spectra (rows) in it.
Each spectrum occupies a cell in the plot which is positioned
according to its coordinates. The coordinates for each spectrum are
normally stored in the Specdre Extension, but for an NDF of at least
three dimensions the first two non-spectroscopic axes can be used
instead. The plot area is the current (AGI) picture of the graphics
device.
The plot can be an overlay in coordinate space to a previous plot, or
a new plot. A plot can be combined from spectra in different NDFs, or
it can overlay spectra on an image of the same or a similar region in
coordinate space.
The previous contents of the plot area can be erased or not. If the
plot is not an overlay, then the space to be left for axis labels as
well as the exact labelling can be specified.
The labelling (in coordinate space) consists of axes, axis ticks,
numeric labels at the major ticks, and text labels. The axes are
counted from bottom clockwise. Each axis can be drawn or not. Each
drawn axis can have ticks or not. Each axis can have numeric labels or
not. The left and right axes can have either horizontal (orthogonal)
or vertical (parallel) numeric labels. Each axis can have a text label
or not.
The kind of labelling is controlled by several 4-character strings.
Each character is the switch for axis 1, 2, 3, 4 respectively. "0"
turns an option off for that axis, "+" turns it on. For the ticks and
for numeric labels of axes 2 and 4, "-" is also allowed. It yields
inward ticks and vertical numeric labels.
Labelling in spectroscopic space (e.g. wavelength-intensity space) is
optional. It is in the form of an empty spectrum cell at a specified
position in coordinate space. This legend cell is labelled with the
ranges in spectroscopic space that is covered by each cell. It also
has text labels to indicate what quantities are displayed.
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

    
       specgrid in overlay=? bottom=? left=? top=? right=?
          labspc=? cworld=? legend=? sworld=? xlegend=? ylegend=?
       



ADAM parameters
~~~~~~~~~~~~~~~



CLEAR = _LOGICAL (Read)
```````````````````````
If true the plot area will be cleared before plotting. When plotting
to a printer file, set this false. Otherwise the output may be
preceded by an empty page. [FALSE]



OVERLAY = _LOGICAL (Read)
`````````````````````````
If true then the last (AGI) data picture inside the current (AGI)
picture is used to define the plot area and its world coordinates.
Only that area will be cleared if CLEAR is true. No new labelling of
the plot will occur. [FALSE]



IN = NDF (Read)
```````````````
The input NDF. If it does not have explicit components COORD1 and
COORD2 in its Specdre Extension, then the NDF must have at least three
dimensions (one spectroscopic and two positional axes). In any case,
the spectroscopic axis must be the first non-degenerate axis.



DEVICE = GRAPHICS (Read)
````````````````````````
The graphics display device.



LIN = _LOGICAL (Read)
`````````````````````
If true, the spectral data points will be connected by a line-style
polygon. [TRUE]



BIN = _LOGICAL (Read)
`````````````````````
If true, the spectral data points will be connected by a bin-style (or
histogram-style) polygon. [FALSE]



MARK = _INTEGER (Read)
``````````````````````
This parameter determines the kind of marker to be drawn at each
spectral data point [0]:

+ 0: No markers drawn,
+ 1: Diagonal cross,
+ 2: Asterisk,
+ 3: Open circle,
+ 4: Open square,
+ 5: Filled circle,
+ 6: Filled square.





ERROR = _LOGICAL (Read)
```````````````````````
If true and variance information available, error bars will be drawn
for each spectral data point. [FALSE]



WIDTH = _LOGICAL (Read)
```````````````````````
If true, the pixel width will be indicated by horizontal bars for each
spectral data point. [FALSE]



FRAME = _LOGICAL (Read)
```````````````````````
If true, each spectral cell gets a plain box drawn around it. [T]



FILL = _LOGICAL (Read)
``````````````````````
If false then the plot window will be adjusted to give the same plot
scale horizontally and vertically. If true, scaling is independent in
each direction and the plot will fill the area available. This
parameter is used only if OVERLAY is false. [F]



ROMAN = _LOGICAL (Read)
```````````````````````
If true, PGPLOT's roman font is used for drawing text. If false, the
normal (single-stroke) font is used. [FALSE]



HEIGHT = _REAL (Read)
`````````````````````
The height of the characters measured in units of PGPLOT default text
height, which is approximately 1/40 of the height of the (AGI) base
picture (i.e. 1/40 the height of the workstation window, screen or
paper). HEIGHT will be used for labelling the plot box (coordinate
space). The legend cell labels are always half that size. [1.]



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
the following escape sequences [!]:

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
the following escape sequences [!]:

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
sequences [!]:

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
following escape sequences [!]:

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
This is a measure for the distance of the text labels from the
coordinate view port. The elements are for the bottom, left, top, and
right edge respectively. In the first instance the whole plot is
inside the current (AGI) picture and LABSPC specifies the fraction of
this view surface to be reserved for labelling. However, if FILL is
false, then the view port will shrink further either horizontally or
vertically to give equal plot scales. The labelling area will then
move inwards as well. The labelling space is measured as a fraction of
the current picture. The values must be between zero and 0.5.
[0.1,0.1,0.05,0.05]



CWORLD( 4 ) = _REAL (Read)
``````````````````````````
The world coordinates of the plot window. Give null to use the
coordinate extent of the input NDF instead. The elements are

+ 1: Left bound in coordinate space,
+ 2: Right bound in coordinate space,
+ 3: Bottom bound in coordinate space,
+ 4: Top bound in coordinate space, Left and right bound must not be
  equal, neither must bottom and top. [!]





LEGEND( 2 ) = _REAL (Read)
``````````````````````````
The coordinates of the legend cell. Each spectral cell has coordinates
according to the NDF's Specdre Extension (or positional axes). LEGEND
is in the same units the position of the empty cell that explains the
spectral and intensity coverage of all cells. Give null to avoid the
legend cell being drawn. [!]



CELLSZ( 2 ) = _REAL (Read)
``````````````````````````
The size of the spectral cells, specified in coordinate units. These
must be positive. [1.,1.]



SWORLD( 4 ) = _REAL (Read)
``````````````````````````
The world coordinates within the spectrum cells. Give null to use the
spectral extent and data range of the input NDF instead. The elements
are

+ 1: Left bound in spectroscopic space,
+ 2: Right bound in spectroscopic space,
+ 3: Bottom bound in spectroscopic space,
+ 4: Top bound in spectroscopic space. Left and right bound must not
  be equal, neither must bottom and top. [!]





XLEGEND = _CHAR (Read)
``````````````````````
The text label for the bottom axis of the legend cell. Give null to
construct the label from the input NDF axis label and unit. Within the
string, you can use the following escape sequences [!]:

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





YLEGEND = _CHAR (Read)
``````````````````````
The text label for the left axis of the legend cell. Give null to
construct the label from the input NDF label and unit. Within the
string, you can use the following escape sequences [!]:

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





Examples
~~~~~~~~
specgrid in accept
Let's assume the given NDF is three-dimensional and has neither a
Specdre Extension, nor any axis information. This implies that the
first axis is spectroscopic with pixel centres 0.5, 1.5, ..., NX-0.5.
The second and third axes will thus be used to position the plots of
the individual spectra horizontally and vertically. The positions will
also be (0.5,0.5), (1.5,0.5), ..., (NY-0.5,NZ-0.5). Each cell has the
default size of 1.0 by 1.0, thus neighbouring pixels in the Y-Z plane
of the NDF will be in adjacent cells on the plot. All cells use
internally the same scales for the spectroscopic value and the data
value. Since these are not specified in parameters, each cell goes
from 0.5 to NX-0.5 horizontally and from the minimum data value to the
maximum data value vertically. There will be no legend cell, since its
position was not given.



Notes
~~~~~
This routine recognises the Specdre Extension v. 1.1.
This routine recognises and uses coordinate transformations in AGI
pictures.


