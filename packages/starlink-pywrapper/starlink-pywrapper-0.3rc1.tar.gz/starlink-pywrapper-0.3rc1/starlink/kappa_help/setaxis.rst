

SETAXIS
=======


Purpose
~~~~~~~
Sets values for an axis array component within an NDF data structure


Description
~~~~~~~~~~~
This routine modifies the values of an axis array component or system
within an NDF data structure. There are a number of options (see
parameters LIKE and MODE). They permit the deletion of the axis
system, or an individual variance or width component; the replacement
of one or more individual values; assignment of the whole array using
Fortran-like mathematical expressions, or values in a text file, or to
pixel co-ordinates, or by copying from another NDF.
If an AXIS structure does not exist, a new one whose centres are pixel
co-ordinates is created before any modification.


Usage
~~~~~


::

    
       setaxis ndf dim mode [comp] { file=?
                                   { index=? newval=?
                                   { exprs=?
                                   mode
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The name of the NDF axis array component to be modified. The choices
are: "Centre", "Data", "Error", "Width" or "Variance". "Data" and
"Centre" are synonyms and selects the axis centres. "Variance" is the
variance of the axis centres, i.e. measures the uncertainty of the
axis-centre values. "Error" is the alternative to "Variance" and
causes the square of the supplied error values to be stored. "Width"
selects the axis width array. ["Data"]



DIM = _INTEGER (Read)
`````````````````````
The axis dimension for which the array component is to be modified.
There are separate arrays for each NDF dimension. The value must lie
between 1 and the number of dimensions of the NDF. This defaults to 1
for a 1-dimensional NDF. DIM is not accessed when COMP="Centre" and
MODE="Delete". The suggested default is the current value. []



EXPRS = LITERAL (Read)
``````````````````````
A Fortran-like arithmetic expression giving the value to be assigned
to each element of the axis array specified by parameter COMP. The
expression may just contain a constant for the axis widths or
variances, but the axis-centre values must vary. In the latter case
and whenever a constant value is not required, there are two tokens
available---INDEX and CENTRE---either or both of which may appear in
the expression. INDEX represents the pixel index of the corresponding
array element, and CENTRE represents the existing axis centres. Either
the CENTRE or the INDEX token must appear in the expression when
modifying the axis centres. All of the standard Fortran-77 intrinsic
functions are available for use in the expression, plus a few others
(see SUN/61 for details and an up-to-date list).
Here are some examples. Suppose the axis centres are being changed,
then EXPRS="INDEX-0.5" gives pixel co-ordinates, EXPRS="2.3 * INDEX +
10" would give a linear axis at offset 10 and an increment of 2.3 per
pixel, EXPRS="LOG(INDEX*5.2)" would give a logarithmic axis, and
EXPRS="CENTRE+10" would add ten to all the array centres. If
COMP="Width", EXPRS=0.96 would set all the widths to 0.96, and
EXPRS="SIND(INDEX-30)+2" would assign the widths to two plus the sine
of the pixel index with respect to index 30 measured in degrees.
EXPRS is only accessed when MODE="Expression".



FILE = FILENAME (Read)
``````````````````````
Name of the text file containing the free-format axis data. This
parameter is only accessed if MODE="File". The suggested default is
the current value.



INDEX = _INTEGER (Read)
```````````````````````
The pixel index of the array element to change. A null value (!)
terminates the loop during multiple replacements. This parameter is
only accessed when MODE="Edit". The suggested default is the current
value.



LIKE = NDF (Read)
`````````````````
A template NDF containing axis arrays. These arrays will be copied
into the NDF given by parameter NDF. All axes are copied. The other
parameters are only accessed if a null (!) value is supplied for LIKE.
If the NDF being modified extends beyond the edges of the template
NDF, then the template axis arrays will be extrapolated to cover the
entire NDF. This is done using linear extrapolation through the last
two extreme axis values. [!]



MODE = LITERAL (Read)
`````````````````````
The mode of the modification. It can be one of the following:
"Delete" - Deletes the array, unless COMP="Data" or "Centre" whereupon
the whole axis structure is deleted. "Edit" - Allows the modification
of individual elements within the array. "Expression" - Allows a
mathematical expression to define the array values. See parameter
EXPRS. "File" - The array values are read in from a free-format text
file. "Linear_WCS" - The axis centres are set to the least-squares
linear fit to the values of the selected axis in the current co-
ordinate Frame of the NDF. This is useful for exporting to packages
with limited FITS WCS compatibility and when the non-linearity is
small. "Linear_WCS" is only available when COMP="Data" or "Centre".
"Pixel" - The axis centres are set to pixel co-ordinates. This is only
available when COMP="Data" or "Centre". "WCS" - The axis centres are
set to the values of the selected axis in the current co-ordinate
Frame of the NDF. This is only available when COMP="Data" or "Centre".
MODE is only accessed if a null (!) value is supplied for parameter
LIKE. The suggested default is the current value.



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure in which an axis array component is to be
modified.



NEWVAL = LITERAL (Read)
```````````````````````
Value to substitute in the array element. The range of allowed values
depends on the data type of the array being modified. NEWVAL="Bad"
instructs that the bad value appropriate for the array data type be
substituted. Placing NEWVAL on the command line permits only one
element to be replaced. If there are multiple replacements, a null
value (!) terminates the loop. This parameter is only accessed when
MODE="Edit".



TYPE = LITERAL (Read)
`````````````````````
The data type of the modified axis array. TYPE can be either "_REAL"
or "_DOUBLE". It is only accessed for MODE="File", "Expression", or
"Pixel". If a null (!) value is supplied, the value used is the
current data type of the array component if it exists, otherwise it is
"_REAL". [!]



Examples
~~~~~~~~
setaxis ff mode=delete
This erases the axis structure from the NDF called ff.
setaxis ff like=hh
This creates axis structures in the NDF called ff by copying them from
the NDF called hh, extrapolating them as necessary to cover ff.
setaxis abell4 1 expr exprs="CENTRE + 0.1 * (INDEX-1)"
This modifies the axis centres along the first axis in the NDF called
abell4. The new centre values are spaced by 0.1 more per element than
previously.
setaxis cube 3 expr error exprs="25.3+0.2*MOD(INDEX,8)"
This modifies the axis errors along the third axis in the NDF called
cube. The new errors values are given by the expression
"25.3+0.2*MOD(INDEX,8)", in other words the noise has a constant term
(25.3), and a cyclic ramp component of frequency 8 pixels.
setaxis spectrum mode=file file=spaxis.dat
This assigns the axis centres along the first axis in the
1-dimensional NDF called spectrum. The new centre values are read from
the free-format text file called spaxis.dat.
setaxis ndf=plate3 dim=2 mode=pixel
This assigns pixel co-ordinates to the second axis's centres in the
NDF called plate3.
setaxis datafile 2 expression exprs="centre" type=_real
This modifies the data type of axis centres along the second dimension
of the NDF called datafile to be _REAL.
setaxis cube 2 edit index=3 newval=129.916
This assigns the value 129.916 to the axis centre at index 3 along the
second axis of the NDF called cube.
setaxis comp=width ndf=cube dim=1 mode=edit index=-16 newval=1E-05
This assigns the value 1.0E-05 to the axis width at index -16 along
the first axis of the NDF called cube.



Notes
~~~~~


+ An end-of-file error results when MODE="File" and the file does not
contain sufficient values to assign to the whole array. In this case
the axis array is unchanged. A warning is given if there are more
values in a file record than are needed to complete the axis array.
+ An invalid expression when MODE="Expression" results in an error and
the axis array is unchanged.
+ The chapter entitled "The Axis Coordinate System" in SUN/33
describes the NDF axis co-ordinate system and is recommended reading
especially if you are using axis widths.
+ There is no check, apart from constraints on parameter NEWVAL, that
  the variance is not negative and the widths are positive.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: AXCONV, AXLABEL, AXUNITS; Figaro: LXSET, LYSET.


File Format
~~~~~~~~~~~
The format is quite flexible. The number of axis-array values that may
appear on a line is variable; the values are separated by at least a
space, comma, tab or carriage return. A line can have up to 255
characters. In addition a record may have trailing comments designated
by a hash or exclamation mark. Here is an example file, though a more
regular format would be clearer for the human reader (say 10 values
per line with commenting).
# Axis Centres along second dimension

+ 3.4 -0.81 .1 3.3 4.52 5.6 9 10.5 12. 15.3 18.1 20.2 23 25.3 ! a
  comment 26.8,27.5 29. 30.76 32.1 32.4567 35.2 37. <EOF>




Copyright
~~~~~~~~~
Copyright (C) 1995, 2000-2001, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2008 Science and Technology Facilities
Council. All Rights Reserved.


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
Processing is in single- or double-precision floating point.


