

MEDIAN
======


Purpose
~~~~~~~
Smooths a 2-dimensional data array using a weighted median filter


Description
~~~~~~~~~~~
This task filters the 2-dimensional data array in the input NDF
structure with a Weighted Median Filter (WMF) in a 3-by-3-pixel kernel
to create a new NDF. There are a number of predefined weighting
functions and parameters that permit other symmetric weighting
functions. See parameter MODE and the topic "User-defined Weighting
Functions".
A threshold for replacement of a value by the median can be set. If
the absolute value of the difference between the actual value and the
median is less than the threshold, the replacement will not occur. The
array boundary is dealt by either pixel replication or a reflection
about the edge pixels of the array.
The WMF can be repeated iteratively a specified number of times, or it
can be left to iterate continuously until convergence is achieved and
no further changes are made to the data. In the latter case a damping
algorithm is used if the number of iterations exceeds some critical
value, which prevents the result oscillating between two solutions
(which can sometimes happen). When damping is switched on data values
are replaced not by the median value, but by a value midway between
the original and the median.
Bad pixels are not included in the calculation of the median. There is
a defined threshold which specifies minimum-allowable median position
as a fraction of the median position when there are no bad pixels. For
neighbourhoods with too many bad pixels, and so the median position is
too small, the resulting output pixel is bad.


Usage
~~~~~


::

    
       median in out [mode] [diff] [bound] [numit] corner side centre
       



ADAM parameters
~~~~~~~~~~~~~~~



BOUND = LITERAL (Read)
``````````````````````
Determines the type of padding required at the array edges before the
filtering starts. The alternatives are described below.
"Replication" - The values at the edge of the data array are
replicated into the padded area. For example, with STEP=2 one corner
of the original and padded arrays would appear as follows: 1 1 1 1 1 1
1 1 1 1 1 1 1 1 corner of 1 1 1 1 1 corresponding 1 1 1 1 1 1 1
original 1 2 2 2 2 corner of 1 1 1 2 2 2 2 array: 1 2 3 3 3 padded
array: 1 1 1 2 3 3 3 1 2 3 4 4 1 1 1 2 3 4 4 1 2 3 4 5 1 1 1 2 3 4 5
"Reflection" - The values near the edge of the data array are
reflected about the array's edge pixels. For example, with STEP=2 one
corner of the original and padded arrays would appear as follows: 3 2
1 2 3 3 3 2 2 1 2 2 2 2 corner of 1 1 1 1 1 corresponding 1 1 1 1 1 1
1 original 1 2 2 2 2 corner of 2 2 1 2 2 2 2 array: 1 2 3 3 3 padded
array: 3 2 1 2 3 3 3 1 2 3 4 4 3 2 1 2 3 4 4 1 2 3 4 5 3 2 1 2 3 4 5
["Replication"]



CENTRE = _INTEGER (Read)
````````````````````````
Central value for weighting function, required if MODE = -1. It must
be an odd value in the range 1 to 21. [1]



CORNER = _INTEGER (Read)
````````````````````````
Corner value for weighting function, required if MODE = -1. It must be
in the range 0 to 10. [1]



DIFF = _DOUBLE (Read)
`````````````````````
Replacement of a value by the median occurs if the absolute difference
of the value and the median is greater than DIFF. [0.0]



IN = NDF (Read)
```````````````
NDF structure containing the 2-dimensional data array to be filtered.



ITERATE = LITERAL (Read)
````````````````````````
Determines the type of iteration used. The alternatives are described
below.
"Specified" - You specify the number of iterations at each step size
in the parameter NUMIT.
"Continuous" - The filter iterates continuously until convergence is
achieved and the array is no longer changed by the filter. A damping
algorithm comes into play after MAXIT iterations, and the filter will
give up altogether after MAXIT * 1.5 iterations (rounded up to the
next highest integer).
"Continuous" mode is recommended only for images which are
substantially smooth to start with (such as a sky background frame
from a measuring machine). Complex images may take many iterations,
and a great deal of time, to converge. ["Specified"]



MAXIT = _INTEGER (Read)
```````````````````````
The maximum number of iterations of the filter before the damping
algorithm comes into play, when ITERATE = "Continuous". It must lie in
the range 1 to 30. [10]



MEDTHR = _REAL (Read)
`````````````````````
Minimum-allowable actual median position as a fraction of the median
position when there are no bad pixels, for the computation of the
median at a given pixel. [0.8]



MODE = _INTEGER (Read)
``````````````````````
Determines type of weighting used, -1 allows you to define the
weighting, and 0 to 7 the predefined filters. The predefined modes
have the following weighting functions:
0: 1 1 1 1: 0 1 0 2: 1 0 1 3: 1 1 1 4: 0 1 0 1 1 1 1 1 1 0 1 0 1 3 1 1
3 1 1 1 1 0 1 0 1 0 1 1 1 1 0 1 0
5: 1 0 1 6: 1 2 1 7: 1 3 1 0 3 0 2 3 2 3 3 3 1 0 1 1 2 1 1 3 1
[0]



NUMIT = _INTEGER (Read)
```````````````````````
The specified number of iterations of the filter, when ITERATE =
"Specified". [1]



OUT = NDF (Write)
`````````````````
NDF structure to contain the 2-dimensional data array after filtering.



SIDE = _INTEGER (Read)
``````````````````````
Side value for weighting function, required if MODE = -1. It must be
in the range 0 to 10. [1]



STEP() = _INTEGER (Read)
````````````````````````
The spacings between the median filter elements to be used. The data
may be filtered at one particular spacing by specifying a single
value, such as STEP=4, or may be filtered at a whole series of
spacings in turn by specifying a list of values, such as
STEP=[4,3,2,1]. There is a limit of 32 values. [1]



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the NDF supplied for parameter IN to be used instead. [!]



Examples
~~~~~~~~
median a100 a100med
This applies an equally weighted median filter to the NDF called a100
and writes the result to the NDF a100med. It uses the default
settings, which are a single step size of one pixel, and a difference
threshold of 0.0. The task pads the array by replication to deals with
the edge pixels, and runs the filter once only.
median a100 a100med bound=ref
As in the previous example except that it uses reflection rather than
replication when padding the array.
median abc sabc mode=3 step=4 diff=1.0 numit=2
This applies a median filter to the NDF called abc with a 1 1 1 1 3 1
weighting mask (MODE=3), a step size of 4 pixels 1 1 1 (STEP=4) and a
difference threshold of 1.0 (DIFF=1.0). It runs the filter twice
(NUMIT=2) and writes the result to the NDF called sabc.
median abc sabc mode=3 step=[4,3,2,1] diff=1.0 numit=2
This applies a median filter as in the previous example, only this
time run the filter at step sizes of 4, 3, 2, and 1 pixels, in that
order (STEP=[4,3,2,1]). It runs the filter twice at each step size
(NUMIT=2). Note that the filter will be run a total of EIGHT times
(number of step sizes times the number of iterations).
median in=spotty step=[4,3,2,1] iterate=cont maxit=6 out=clean
This applies a median filter to the NDF called spotty with the default
settings for the mode and difference threshold. It runs the filter at
step sizes of 4, 3, 2, and 1 pixels, operating continuously at each
step size until the result converges (ITERATE=CONT). Damping will
begin after 6 iterations (MAXIT=6), and the filtering will stop
regardless after 10 iterations (1 + INT(1.5 * MAXIT)). Note that the
filter will run an indeterminate number of times, up to a maximum of
40 (number of step sizes * maximum number of iterations), and may take
a long time. The resultant data array are written to the NDF called
clean.



User-defined Weighting Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parameters CORNER, SIDE, and CENTRE allow other symmetric functions in
addition to those offered by MODE=0 to 7. A step size has to be
specified too; this determines the spacing of the elements of the
weighting function. The data can be filtered at one step size only, or
using a whole series of step sizes in sequence. The weighting function
has the form:
%CORNER . %SIDE . %CORNER . . . %SIDE . %CENTRE . %SIDE . . . %CORNER
. %SIDE . %CORNER
The . indicates that the weights are separated by the stepsize-minus-
one zeros.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: BLOCK, CONVOLVE, FFCLEAN, GAUSMOOTH; Figaro: ICONV3, ISMOOTH,
IXSMOOTH, MEDFILT.


Copyright
~~~~~~~~~
Copyright (C) 1983-1984, 1986-1989, 1991-1993 Science & Engineering
Research Council. Copyright (C) 1995, 1998, 2004 Central Laboratory of
the Research Councils. Copyright (C) 2012 Science & Technology
Facilities Council. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, LABEL, TITLE,
UNITS, WCS and HISTORY components of an NDF data structure and
propagates all extensions. VARIANCE is not used to weight the median
filter and is not propagated. QUALITY is also lost.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.




