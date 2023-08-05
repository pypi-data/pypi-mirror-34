

MOVIE
=====


Purpose
~~~~~~~
Browse through slices of a cube


Description
~~~~~~~~~~~
This routine takes a three-dimensional NDF and displays its two-
dimensional slices sequentially on a grey or colour graphics device.
The colour table of the display is unaltered so that a previously
loaded colour table will be used. Bad values will be displayed in the
display background colour, which in general is distinct from the
colour for the lowest (or highest) data value.
This routine is quite primitive. It does not use axis data or
spectroscopic values from the Specdre Extension. Pixels and slices in
the cube are addressed by their NDF pixel indices, which are integer
numbers, usually starting at 1.
The routine also does not pay much attention to the precise timing of
the display. The following list gives activities that the routine
spends time on and how the user can exert some control over the
timing.


+ Before a frame can be displayed it must be extracted from the cube.
The time taken for this depends greatly on whether the frame counting
axis is the first or last axis. Taking slices is fastest if AXIS=3 and
can be very slow if AXIS=1, so it may be useful to re-arrange the axes
of a cube that will be viewed often with the same frame-counting axis.
Another way to reduce the time for taking slices from the cube is to
use as small a cube as possible: If it is a-priori known that only a
certain range of frames will be looked at, or that only a certain part
of all frames is interesting, then the input cube can be given as an
appropriate subset of the actual disk file.
+ Also before a frame can be displayed it must be converted according
to the colour capabilites of the display.
+ Each frame needs to be extracted and converted only once and can be
viewed several times, converted frames are kept in a workspace until
the routine exits.
+ In the sequence displays each frame is converted and displayed
before the routine goes on to the next frame.
+ When a specific frame is requested it is extracted, converted and
displayed (unless it has been viewed before).
+ When the next or previous frame relative to the displayed one is
requested, it is extracted and converted if necessary. Then it is
displayed. In anticipation of another request of the same type the
next or previous frame is extracted and converted immediately.
+ Even if a frame has been converted before, it takes some time to
resample it from cube pixels to display pixels. This time can be
minimised by choosing the fast mode, where a cube pixel is only one
display pixel.
+ Disruptions occur in the display of a sequence of frames due to the
unpredictable need for the machine to page memory.
+ Display may be over a network and bandwidth has to be shared with
  other users. This too causes disruptions of frame sequences.

In summary, it may be best to


+ put on your spectacles and settle for the fast (and tiny) display,
+ decide which part of the cube is interesting and specify only that
sub-cube as input,
+ begin the forward sequence to convert the whole input sub-cube,
+ have a cup of tea if AXIS=3 and the cube is not small,
+ use the options 'I', 'P', 'N' to look at individual frames in your
  own time.

It is not possible to write the cube as converted for display. Such a
cube would be of limited use, since it might contain only part of the
input cube and since its scaling depends on the colour capabilities of
the display used.


Usage
~~~~~


::

    
       movie in axis low=? high=?
       



ADAM parameters
~~~~~~~~~~~~~~~



DIALOG = _CHAR (Read)
`````````````````````
The dialogue mode. If false ('F' or 'N') all frames of the cube will
be displayed once in forward order. If true ('T' or 'Y') the routine
will not display anything initially, but repeatedly ask for a menu
option via the MENU parameter. 'G' for graphic is also permitted, but
has the same meaning as 'T'. ['F']



INFO = _LOGICAL (Read)
``````````````````````
If true, informational messages are given. Such as, which frame is
currently displayed. [YES]



MODE = _CHAR (Read)
```````````````````
'Fast', 'Fill', or 'Square' for (i) a tiny but quick display, (ii) to
use the whole display area available, (iii) the biggest display with
square pixels that is possible in the area available. The mode can be
abbreviated to two characters and is case-insensitive. ['Fast']



IN = NDF (Read)
```````````````
The input NDF. It must be three-dimensional - not counting degenerate
axes.



DEVICE = GRAPHICS (Read)
````````````````````````
The graphics display device. It must be a screen device, not a printer
device.



AXIS = _INTEGER (Read)
``````````````````````
The number of the movie axis. Of the three axes in the input cube this
is the one not visible in the display. This is the axis to count the
frames of the movie. [3]



LOW = _REAL (Read)
``````````````````
The minimum data value from the cube to be displayed. Values less than
this are displayed in the same colour.



HIGH = _REAL (Read)
```````````````````
The maximum data value from the cube to be displayed. Values greater
than this are displayed in the same colour.



MENU = _CHAR (Read)
```````````````````
The application will ask repeatedly for the menu option, until 'Q' is
chosen. These options are also available from the keyboard if dialogue
is graphic. ['F']

+ F: Display each frame in forward order.
+ B: Display each frame in backward order.
+ I: Ask for FRAME parameter and display specified frame.
+ P: Display previous frame.
+ N: Display next frame.
+ Q: Quit.
+ ?: Help.





FRAME = _INTEGER (Read)
```````````````````````
The frame number to be displayed next. Note that frames are counted in
NDF pixel indices, i.e. from the NDF's lower bound to its upper bound.



