

SEGMENT
=======


Purpose
~~~~~~~
Copies polygonal segments from one NDF into another


Description
~~~~~~~~~~~
This routine copies one or more polygonal segments from the first
input NDF (Parameter IN1), and pastes them into the second input NDF
(Parameter IN2) at the same pixel co-ordinates. The resulting mosaic
is stored in the output NDF (see OUT). Either input NDF may be
supplied as null ("!") in which case the corresponding areas of the
output NDF are filled with bad values. For instance, supplying a null
value for IN2 allows segments to be cut from IN1 and pasted on to a
background of bad values. Supplying a null value for IN1 allows
"holes" to be cut out of IN2 and filled with bad values.
Each polygonal segment is specified by giving the positions of its
vertices. This may be done using a graphics cursor, by supplying a
positions list or text file containing the positions, or by supplying
the positions in response to a parameter prompt. The choice is made by
Parameter MODE.
This application may also be used to cut and paste cylinders with
polygonal cross-sections from NDFs with more than two dimensions. See
the Notes section below for further details.


Usage
~~~~~


::

    
       segment in1 in2 out { coords=?
                           { incat1-incat20=?
                           { poly1-poly20=?
                           mode
       



ADAM parameters
~~~~~~~~~~~~~~~



COORDS = LITERAL (Read)
```````````````````````
The co-ordinates of a single vertex for the current polygon. If
Parameter MODE is set to "Interface", this parameter is accessed
repeatedly to obtain the co-ordinates of all vertices in the polygon.
A null value should be given when the final vertex has been specified.
Each position should be supplied within the current co-ordinate Frame
of the output NDF (see Parameter OUT). Supplying a colon ":" will
display details of the required co-ordinate Frame. No more than two
formatted axis values (separated by a comma or space) may be supplied.
If the co-ordinate Frame being used has more than two axes, then the
two axes to use must be specified using Parameter USEAXIS.



DEVICE = DEVICE (Read)
``````````````````````
The name of the graphics device on which an image is displayed. Only
used if Parameter MODE is given the value "Cursor". Any graphics
specified by Parameter PLOT will be produced on this device. This
device must support cursor interaction. [Current graphics device]



IN1 = NDF (Read)
````````````````
The input NDF containing the data to be copied to the inside of the
supplied polygonal segments. If a null value is supplied, the inside
of the polygonal segments will be filled with bad values.



IN2 = NDF (Read)
````````````````
The input NDF containing the data to be copied to the outside of the
supplied polygonal segments. If a null value is supplied, the outside
of the polygonal segments will be filled with bad values.



INCAT1-INCAT20 = FILENAME (Read)
````````````````````````````````
If MODE is "Catalogue", each of the Parameters INCAT1 to INCAT20 are
used to access catalogues containing the co-ordinates of the vertices
of a single polygon. Suitable catalogues may be created using CURSOR,
LISTMAKE, etc. If a value is assigned to INCAT1 on the command line,
you are not prompted for any of the remaining parameters in this
group; additional polygon catalogues must also be supplied on the
command line. Otherwise, you are prompted for INCAT1, then INCAT2,
etc. until a null value is given or INCAT20 is reached.
The positions in each catalogue are mapped into the pixel co-ordinate
Frame of the output NDF by aligning the WCS information stored in the
catalogue with the WCS information in the output NDF. A message
indicating the Frame in which the positions were aligned with the
output NDF is displayed.



LOGFILE = FILENAME (Write)
``````````````````````````
The name of a text file in which the co-ordinates of the polygon
vertices are to be stored. A null value (!) means that no file is
created. [!]



MARKER = INTEGER (Read)
```````````````````````
This parameter is only accessed if Parameter PLOT is set to "Chain" or
"Mark". It specifies the type of marker with which each cursor
position should be marked, and should be given as an integer PGPLOT
marker type. For instance, 0 gives a box, 1 gives a dot, 2 gives a
cross, 3 gives an asterisk, 7 gives a triangle. The value must be
larger than or equal to -31. [current value]



MODE = LITERAL (Read)
`````````````````````
The mode in which the co-ordinates of each polygon vertex are to be
obtained. The supplied string can be one of the following selection.


+ "Interface" -- positions are obtained using Parameter COORDS. These
positions must be supplied in the current co-ordinate Frame of the
output NDF (see Parameter OUT).
+ "Cursor" -- positions are obtained using the graphics cursor of the
device specified by Parameter DEVICE. The WCS information stored with
the picture in the graphics database is used to map the supplied
cursor positions into the pixel co-ordinate Frame of the output NDF. A
message is displayed indicating the co-ordinate Frame in which the
picture and the output NDF were aligned.
+ "Catalogue" -- positions are obtained from positions lists using
Parameters INCAT1 to INCAT20. Each catalogue defines a single polygon.
The WCS information in each catalogue is used to map the positions in
the catalogue into the pixel co-ordinate Frame of the output NDF. A
message is displayed for each catalogue indicating the co-ordinate
Frame in which the catalogue and the output NDF were aligned.
+ "File" -- positions are obtained from text files using Parameters
  POLY1 to POLY20. Each file defines a single polygon. Each line in a
  file must contain two formatted axis values in the current co-ordinate
  Frame of the output NDF (see Parameter OUT), separated by white space
  or a comma.

[current value]



MAXPOLY = _INTEGER (Read)
`````````````````````````
The maximum number of polygons which can be used. For instance, this
can be set to 1 to ensure that no more than one polygon is used (this
sort of thing can be useful when writing procedures or scripts). A
null value causes no limit to be imposed (unless MODE="File" or
"Catalogue" in which case a limit of 20 is imposed). [!]



MINPOLY = _INTEGER (Read)
`````````````````````````
The minimum number of polygons which can be used. For instance, this
can be set to 2 to ensure that at least 2 polygons are used. The
supplied value must be less than or equal to the value given for
MAXPOLY and must be greater than zero. [1]



OUT = NDF (Write)
`````````````````
The output NDF. If only one input NDF is supplied (that is, if one of
IN1 and IN2 is assigned a null value), then the output NDF has the
same shape and size as the supplied input NDF. Also ancillary data
such as WCS information is propagated from the supplied input NDF. In
particular, this means that the current co-ordinate Frame of the
output NDF (in which vertex positions should be supplied if MODE is
"File" or "Interface") is inherited from the input NDF. If two input
NDFs are supplied, then the shape and size of the output NDF
corresponds to the area of overlap between the two input NDFs (in
pixel space), and the WCS information and current Frame are inherited
from the NDF associated with Parameter IN1.



PLOT = LITERAL (Read)
`````````````````````
The type of graphics to be used to mark the position of each selected
vertex. It is only used if Parameter MODE is given the value "Cursor".
The appearance of these graphics (colour, size, etc ) is controlled by
the STYLE parameter. PLOT can take any of the following values.


+ "None" -- No graphics are produced.
+ "Mark" -- Each position is marked with a marker of type specified by
Parameter MARKER.
+ "Poly" -- Causes each position to be joined by a line to the
previous position. Each polygon is closed by joining the last position
to the first.
+ "Chain" -- This is a combination of "Mark" and "Poly". Each position
  is marked by a marker and joined by a line to the previous position.
  Parameter MARKER is used to specify the marker to use. [current value]





POLY1-POLY20 = FILENAME (Read)
``````````````````````````````
If MODE is "File", each of the Parameters POLY1 to POLY20 are used to
access text files containing the co-ordinates of the vertices of a
single polygon. If a value is assigned to POLY1 on the command line,
you are not prompted for any of the remaining parameters in this
group; additional polygon files must also be supplied on the command
line. Otherwise, you are prompted for POLY1, then POLY2, etc. until a
null value is given or POLY20 is reached.
Each position should be supplied within the current co-ordinate Frame
of the output NDF (see Parameter OUT). No more than two formatted axis
values (separated by a comma or space) may be supplied on each line.
If the co-ordinate Frame being used has more than two axes, then the
two axes to use must be specified using Parameter USEAXIS.



QUALITY = _LOGICAL (Read)
`````````````````````````
If a TRUE value is supplied for Parameter QUALITY then quality
information is copied from the input NDFs to the output NDFs.
Otherwise, the quality information is not copied. This parameter is
only accessed if all supplied input NDFs have defined QUALITY
components. If any of the supplied input NDFs do not have defined
QUALITY components, then no quality is copied. Note, if a null input
NDF is given then the corresponding output QUALITY values are set to
zero. [TRUE]



STYLE = GROUP (Read)
````````````````````
A group of attribute settings describing the style to use when drawing
the graphics specified by Parameter PLOT.
A comma-separated list of strings should be given in which each string
is either an attribute setting, or the name of a text file preceded by
an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner. Attribute settings are applied in the order in which they
occur within the list, with later settings overriding any earlier
settings given for the same attribute.
Each individual attribute setting should be of the form:
<name>=<value>
where <name> is the name of a plotting attribute, and <value> is the
value to assign to the attribute. Default values will be used for any
unspecified attributes. All attributes will be defaulted if a null
value (!)---the initial default---is supplied. To apply changes of
style to only the current invocation, begin these attributes with a
plus sign. A mixture of persistent and temporary style changes is
achieved by listing all the persistent attributes followed by a plus
sign then the list of temporary attributes.
See section "Plotting Attributes" in SUN/95 for a description of the
available attributes. Any unrecognised attributes are ignored (no
error is reported).
The appearance of the lines forming the edges of each polygon is
controlled by the attributes Colour(Curves), Width(Curves), etc.
(either of the synonyms Lines and Edges may be used in place of
Curves). The appearance of the vertex markers is controlled by the
attributes Colour(Markers), Size(Markers), etc. (the synonyms Vertices
may be used in place of Markers). [current value]



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the
output NDF has more than two axes. A group of two strings should be
supplied specifying the two axes spanning the plane in which the
supplied polygons are defined. Each axis can be specified using one of
the following options.


+ An integer index of an axis within the current Frame of the output
NDF (in the range 1 to the number of axes in the current Frame).
+ An axis symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the first two significant NDF pixel axes are used. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
If a TRUE value is supplied for Parameter VARIANCE then variance
information is copied from the input NDFs to the output NDFs.
Otherwise, the variance information is not copied. This parameter is
only accessed if all supplied input NDFs have defined VARIANCE
components. If any of the supplied input NDFs do not have defined
VARIANCE components, then no variances are copied. Note, if a null
input NDF is given then the corresponding output variance values are
set bad. [TRUE]



Examples
~~~~~~~~
segment in1=m51a in2=m51b out=m51_comp incat1=coords mode=cat
Copies a region of the NDF m51a to the corresponding position in the
output NDF m51_comp. The region is defined by the list of vertex co-
ordinates held in catalogue coords.FIT. All pixels in the output NDF
which fall outside this region are given the corresponding pixel
values from NDF m51b.
segment in1=m51a out=m51_cut mode=cursor plot=poly accept
Copies a region of the NDF m51a to the corresponding position in the
output NDF m51_cut. The region is defined by selecting vertices using
a graphics cursor. The image m51a should previously have been
displayed. Each vertex is joined to the previous vertex by a line on
the graphics device. The ACCEPT keyword causes the suggested null
default value for IN2 to be accepted. This means that all pixels
outside the region identified using the cursor will be set bad in the
output NDF.



Notes
~~~~~


+ Supplied positions are mapped into the pixel co-ordinate Frame of
the output NDF before being used. This means that the two input NDFs
(if supplied) must be aligned in pixel space before using this
application.
+ The routine can handle NDFs of arbitrary dimensionality. If either
  input has three or more dimensions then all planes in the NDF pixel
  arrays are processed in the same way, that is the same polygonal
  regions are extracted from each plane and copied to the corresponding
  plane of the output NDF. The plane containing the polygons must be
  defined using Parameter USEAXIS. This plane is a plane within the
  current co-ordinate Frame of the output NDF (which is inherited from
  the first supplied input NDF). This scheme will only work correctly if
  the selected plane in the current co-ordinate Frame is parallel to one
  of the planes of the pixel array.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: ARDMASK, ERRCLIP, FILLBAD, FFCLEAN, PASTE, REGIONMASK,
SETMAGIC, THRESH.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995, 1997-1998, 2000, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2010 Science & Facilities Research Council.
All Rights Reserved.


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


+ This routine will propagate VARIANCE component values so long as all
supplied input NDFs have defined VARIANCE components, and Parameter
VARIANCE is not FALSE.
+ This routine will propagate QUALITY component values so long as all
supplied input NDFs have defined QUALITY components, and Parameter
QUALITY is not FALSE.
+ The UNITS, AXIS, LABEL, TITLE, WCS and HISTORY components are
propagated from the first supplied input NDF, together with all
extensions.
+ All non-complex numeric types are supported. The following data
  types are processed directly: _WORD, _INTEGER, _REAL, _DOUBLE.




