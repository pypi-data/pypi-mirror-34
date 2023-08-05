

FINDOFF
=======


Purpose
~~~~~~~
Performs pattern-matching between position lists related by simple
offsets


Description
~~~~~~~~~~~
This routine is designed to determine which positions in many
unaligned and unlabelled lists match, subject to the condition that
the transformations between the lists are well modelled by simple
translations. Although the position lists are written in pixel
coordinates, the objects can be related by translations in the Current
coordinate system of the associated NDFs.
The results from this routine are labelled position lists (one for
each input list) which may be used to complete image registration
using the REGISTER routine. The estimated offsets are reported, but
REGISTER should be used to get accurate values.


Usage
~~~~~


::

    
       findoff inlist error outlist
       



ADAM parameters
~~~~~~~~~~~~~~~



COMPLETE = _DOUBLE (Read)
`````````````````````````
A completeness threshold for rejecting matched position list pairs. A
completeness factor is estimated by counting the number of objects in
the overlap region of two lists, taking the minimum of these two
values (this adjusts for incompleteness due to a different object
detection threshold) and comparing this with the number of objects
actually matched. Ideally a completeness of 1 should be found, the
lower this value the lower the quality of the match. [0.5]



ERROR = _DOUBLE (Read)
``````````````````````
The error, in pixels, in the X and Y positions. This value is used to
determine which positions match within an error box (SLOW) or as a bin
size (FAST). An inaccurate value may result in excessive false or null
matches. [1.0]



FAILSAFE = _LOGICAL (Read)
``````````````````````````
If FAST is TRUE then this parameter indicates whether the SLOW
algorithm is to be used when FAST fails. [TRUE]



FAST = _LOGICAL (Read)
``````````````````````
If TRUE then the FAST matching algorithm is used, otherwise just the
SLOW algorithm is used. [TRUE]



INLIST = LITERAL (Read)
```````````````````````
This parameter is used to access the names of the lists which contain
the positions and, if NDFNAMES is TRUE, the names of the associated
NDFs. If NDFNAMES is TRUE the names of the position lists are assumed
to be stored in the extension of the NDFs (in the CCDPACK extension
item CURRENT_LIST) and the names of the NDFs themselves should be
given in response (and may include wildcards).
If NDFNAMES is FALSE then the actual names of the position lists
should be given. These may not use wildcards but may be specified
using indirection (other CCDPACK position list processing routines
will write the names of their results file into files suitable for use
in this manner) the indirection character is "^".



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



MAXDISP = _DOUBLE (Read)
````````````````````````
This parameter gives the maximum acceptable displacement (in pixels)
between the original alignment of the NDFs and the alignment in which
the objects are matched. If frames have to be displaced more than this
value to obtain a match, the match is rejected. This will be of use
when USEWCS is set and the NDFs are already fairly well aligned in
their Current coordinate systems. It should be set to the maximum
expected inaccuracy in that alignment. If null, arbitrarily large
displacements are allowed, although note that a similar restriction is
effectively imposed by setting the RESTRICT parameter. [!]



MINMATCH = _INTEGER (Read)
``````````````````````````
This parameter specifies the minimum number of positions which must be
matched for a comparison of two lists to be deemed successful. Small
values (especially less than 3) of this parameter can lead to a high
probability of false matches, and are only advisable for very sparsely
populated lists and/or small values of the MAXDISP parameter
(presumably in conjunction with USEWCS). [3]



MINSEP = _DOUBLE (Read)
```````````````````````
Positions which are very close may cause false matches by being within
the error box of other positions. The value of this parameter controls
how close (in pixels) objects may be before they are both rejected
(this occurs before pattern-matching). [Dynamic -- 5.0*ERROR]



NAMELIST = LITERAL (Read)
`````````````````````````
The name of a file to contain the names of the output position lists.
The names written to this file are those generated using the
expression given to the OUTLIST parameter. This file may be used in an
indirection expression to input all the position lists output from
this routine into another routine (say REGISTER), if the associating
position lists with NDFs option is not being used. [FINDOFF.LIS]



NDFNAMES = _LOGICAL (Read)
``````````````````````````
If TRUE then the routine will assume that the names of the position
lists are stored in the NDF CCDPACK extensions under the item
"CURRENT_LIST". The names will be present in the extension if the
positions were located using a CCDPACK application (such as FINDOBJ).
Using this facility allows the transparent propagation of position
lists through processing chains.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [TRUE]



OUTLIST = FILENAME (Write)
``````````````````````````
A list of names specifying the result files. These contain labelled
positions which can be used in registration. The names of the lists
may use modifications of the input names (NDF names if available
otherwise the names of the position lists). So if you want to call the
output lists the same name as the input NDFs except to add a type use.
OUTLIST > *.find
If no NDF names are given (NDFNAMES is FALSE) then if you want to
change the extension of the files (from ".find" to ".off" in this
case) use
OUTLIST > *|find|off|
Or alternatively you can use an explicit list of names. These may use
indirection elements as well as names separated by commas.



OVERRIDE = _LOGICAL (Read)
``````````````````````````
This parameter controls whether to continue and create an incomplete
solution. Such solutions will result when only a subset of the input
position lists have been matched. If the associating position lists
with NDFs option has been chosen, an position list will still be
written for each input NDF, but for NDFs which were not matched the
output list will be empty (will consist only of comment lines).
Incomplete matching would ideally indicate that one, or more, of the
input lists are from positions not coincident with the others, in
which case it is perfectly legimate to proceed. However, it is equally
possible that they have too few positions and have consequently been
rejected. [TRUE]



RESTRICT = _LOGICAL (Read)
``````````````````````````
This parameter determines whether the Current coordinate system is
used to restrict the choice of objects to match with each other. If
set TRUE, then the only objects which are considered for matching are
those which would appear in the overlap of two frames given that they
are correctly aligned in their Current coordinate system. If it is set
FALSE, then all objects in both frames are considered for matching.
This parameter should therefore be set TRUE if the frames are quite
well aligned in their Current coordinate systems (especially in the
case that there are many objects and a small overlap), and FALSE if
they are not.
This parameter is ignored if USEWCS is FALSE. [FALSE]



USECOMP = _LOGICAL (Read)
`````````````````````````
This parameter specifies whether the completeness value will be used
to weight the number of matches between a pair, when determining the
graph connecting all input datasets. Using a completeness weight
increases the chance of selecting high quality matches, but may reduce
the chance of selecting matches with the highest counts in favour of
those with lower counts. [TRUE]



USESET = _LOGICAL (Read)
````````````````````````
This parameter determines whether Set header information should be
used in the object matching. If USESET is true, FINDOFF will try to
group position lists according to the Set Name attribute of the NDF to
which they are attached. All lists coming from NDFs which share the
same (non-blank) Set Name attribute, and which have a CCD_SET
coordinate frame in their WCS component, will be grouped together and
treated by the program as a single position list. Thus no attempt is
made to match objects between members of the same Set; it is assumed
that the relative alignment within a Set is already known and has been
fixed.
If USESET is false, all Set header information is ignored. If NDFNAMES
is false, USESET will be ignored. If the input NDFs have no Set
headers, or if they have no CCD_SET frame in their WCS components, the
setting of USESET will make no difference.
If a global value for this parameter has been set using CCDSETUP then
that value will be used. [FALSE]



USEWCS = _LOGICAL (Read)
````````````````````````
This parameter specifies whether the coordinates in the position lists
should be transformed from Pixel coordinates into the Current
coordinate system of the associated NDF before use. If the Current
coordinates are related to pixel coordinates by a translation, the
setting of this parameter is usually unimportant (but see also the
RESTRICT parameter).
This parameter is ignored if NDFNAMES is false. [TRUE]



Examples
~~~~~~~~
findoff inlist='*' error=1 outlist='*.off'
In this example all the NDFs in the current directory are accessed and
their associated position lists are used. The NDFs are related by a
simple offset (translation) in their Current coordinate system,
although not necessarily their pixel coordinate system. The matched
position lists are named *.off. The method used is to try the FAST
algorithm, switching to SLOW if FAST fails. The completeness measure
is used when forming the spanning tree. Matches with completenesses
less than 0.5 and or with less than three positions, are rejected.
findoff fast nofailsafe
In this example the only the FAST algorithm is used.
findoff usecomp=false
In this example the completeness factor is derived but not used to
weight the edges of the spanning tree.
findoff error=8 minsep=100
In this example very fuzzy measurements (or small pixels) are being
used. The intrinsic error in the measurements is around 8 pixels and
positions within a box 100 pixels of each other are rejected.
findoff inlist='data*' outlist='*.off' restrict=true
This form would be used if the NDFs 'data*' are already approximately
aligned in their Current coordinates. Setting the RESTRICT parameter
then tells FINDOFF to consider only objects in the region which
overlaps in the Current coordinates of each pair of frames. This can
save a lot of time if there are many objects and a small overlap, but
will result in failure of the program if the NDFs are not
translationally aligned reasonably well in the first place.
findoff inlist='data*' outlist='*.off' restrict minmatch=2
maxdisp=20 minsep=30 In this example the NDFs are sparsely populated,
and a pair will be considered to match if as few as two matching
objects can be found. The NDFs have been initially aligned in their
Current coordinate systems to an accuracy of 20 or better. As an
additional safeguard, no objects within 30 units (in coordinates of
the Current frame) of each other in the same NDF are used for
matching.



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
positions. In the output position lists from one run of FINDOFF, lines
with the same column-1 value in different files represent the same
object. In the input position lists column-1 values are ignored. If
additional columns are present they must be numeric, and there must be
the same number of them in every line. These have no effect on the
calculations, but FINDOFF will propagate them to the corresponding
lines in the output list.
EXTERNAL format - positions are specified using just an X and a Y
entry and no other entries.


+ Column 1: the X position
+ Column 2: the Y position

This format is used by KAPPA applications such as CURSOR.
Comments may be included in a file using the characters "#" and "!".
Columns may be separated by the use of commas or spaces.
In all cases, the coordinates in position lists are pixel coordinates.


+ NDF extension items.

If NDFNAMEs is TRUE then the names of the input position lists will be
gotten from the item "CURRENT_LIST" of the CCDPACK extension of the
input NDFs. On exit this item will be updated to contain the name of
the appropriate output lists.


Behaviour of Parameters
~~~~~~~~~~~~~~~~~~~~~~~
Most parameters retain their current value as default. The "current"
value is the value assigned on the last run of the application. If the
application has not been run then the "intrinsic" defaults, as shown
in the parameter help, apply.
Retaining parameter values has the advantage of allowing you to define
the default behaviour of the application but does mean that additional
care needs to be taken when re-using the application after a break of
sometime. The intrinsic default behaviour of the application may be
restored by using the RESET keyword on the command line.
Certain parameters (LOGTO, LOGFILE, NDFNAMES and USESET) have global
values. These global values will always take precedence, except when
an assignment is made on the command line. Global values may be set
and reset using the CCDSETUP and CCDCLEAR commands.


Notes On Algorithms
~~~~~~~~~~~~~~~~~~~
The pattern-matching process uses two main algorithms, one which
matches all the point pair-offsets between any two input lists,
looking for the matches with the most common positions, and one which
uses a statistical method based on a histogram of the differences in
the offsets (where the peak in the histogram is assumed the most
likely difference). In each case an estimate of the positional error
must be given as it is used when deciding which positions match (given
an offset) or is used as the bin size when forming histograms.
Which algorithm you should use depends on the number of points your
position lists contain and the expected size of the overlaps between
the datasets. Obviously it is much easier to detect two lists with
most of their positions in common. With small overlaps a serious
concern is the likelihood of finding a `false' match. False matches
must be more likely the larger the datasets and the smaller the
overlap.
The first algorithm (referred to as SLOW) is more careful and is
capable of selecting out positions when small overlaps in the data are
present (although a level of false detections will always be present)
but the process is inherently slow (scaling as n**3log2(n)). The
second algorithm (referred to as FAST) is an n*n process so is much
quicker, but requires much better overlapping.
Because the FAST process takes so little CPU time it is better to try
this first (without the SLOW process as a backup), only use the SLOW
algorithm when you have small datasets and do not expect large areas
(numbers of positions) of overlap.
A third algorithm, referred to as SNGL, is used automatically if one
or both of the lists in a pair contains only a single object. In this
case object matching is trivial and, of course, may easily be in
error. SNGL can only be used if the MINMATCH parameter has been set to
1, which should be done with care. The SNGL algorithm may be useful if
there really is only one object, correctly identified, in all the
frames. If this is not the case, it should only be used when USEWCS is
true and MAXDISP is set to a low value, indicating that the alignment
of the NDFs in their Current coordinate systems is already fairly
accurate.
The global registration process works by forming a graph with each
position list at a node and with connecting edges of weight the number
of matched position-pairs. The edge weights may be modified by a
completeness factor which attempts to assess the quality of the match
(this is based on the ratio of the expected number of matches in the
overlap region to the actual number, random matches shouldn't return
good statistics when compared with genuine ones). This still leaves a
possibility of false matches disrupting any attempt to register the
datasets so a single "spanning tree" is chosen (this is a graph which
just visits each node the minimum number of times required to get
complete connectivity, no loops allowed) which has the highest
possible number of matched positions (rejecting edges with few matched
positions/low completenesses where possible). This gives a most likely
solution to the offsets between the position lists, rather than the
"best" solution which could well include false matches; compare this
solution with a median as opposed to a mean. The final registration is
then used to identify all the objects which are the same in all
datasets (using a relaxation method), resulting in labelled position
lists which are output for use by REGISTER.


Copyright
~~~~~~~~~
Copyright (C) 1992-1993 Science & Engineering Research Council.
Copyright (C) 1995-2002 Central Laboratory of the Research Copyright
(C) 2008 Science and Technology Facilities Council Councils. All
Rights Reserved.


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


