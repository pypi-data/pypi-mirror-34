

CENTROID
========


Purpose
~~~~~~~
Finds the centroids of star-like features in an NDF


Description
~~~~~~~~~~~
This routine takes an NDF and returns the co-ordinates of the
centroids of features in its data array given approximate initial co-
ordinates. A feature is a set of connected pixels which are above or
below the surrounding background region. For example, a feature could
be a star or galaxy on the sky, although the applications is not
restricted to two-dimensional NDFs.
Four methods are available for obtaining the initial positions,
selected using Parameter MODE:


+ from the parameter system (see Parameter INIT);
+ using a graphics cursor to indicate the feature in a previously
displayed data array (see Parameter DEVICE);
+ from a specified positions list (see Parameter INCAT); or
+ from a simple text file containing a list of co-ordinates (see
  Parameter COIN).

In the first two modes the application loops, asking for new feature
co-ordinates until it is told to quit or encounters an error.
The results may optionally be written to an output positions list
which can be used to pass the positions on to another application (see
Parameter OUTCAT), or to a log file geared more towards human readers,
including details of the input parameters (see Parameter LOGFILE).
The uncertainty in the centroid positions may be estimated if variance
values are available within the supplied NDF (see Parameter CERROR).


Usage
~~~~~


::

    
       centroid ndf [mode] { init   [search] [maxiter] [maxshift] [toler]
                           { coin=?
                           { incat=?
                         mode
       



ADAM parameters
~~~~~~~~~~~~~~~



CATFRAME = LITERAL (Read)
`````````````````````````
A string determining the co-ordinate Frame in which positions are to
be stored in the output catalogue associated with Parameter OUTCAT.
The string supplied for CATFRAME can be one of the following options.


+ A Domain name such as SKY, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame.
+ An IRAS90 Sky Co-ordinate System (SCS) values such as EQUAT(J2000)
  (see SUN/163).

If a null (!) value is supplied, the positions will be stored in the
current Frame. [!]



CATEPOCH = DOUBLE PRECISION (Read)
``````````````````````````````````
The epoch at which the sky positions stored in the output catalogue
were determined. It will only be accessed if an epoch value is needed
to qualify the co-ordinate Frame specified by COLFRAME. If required,
it should be given as a decimal years value, with or without decimal
places ("1996.8" for example). Such values are interpreted as a
Besselian epoch if less than 1984.0 and as a Julian epoch otherwise.



CENTRE = LITERAL (Write)
````````````````````````
The formatted co-ordinates of the last centroid position, in the
current Frame of the NDF.



CERROR = _LOGICAL (Read)
````````````````````````
If TRUE, errors in the centroided position will be calculated. The
input NDF must contain a VARIANCE component in order to compute
errors. [FALSE]



COIN = FILENAME (Read)
``````````````````````
Name of a text file containing the initial guesses at the co-ordinates
of features to be centroided. It is only accessed if Parameter MODE is
given the value "File". Each line should contain the formatted axis
values for a single position, in the current Frame of the NDF. Axis
values can be separated by spaces, tabs or commas. The file may
contain comment lines with the first character # or !.



DESCRIBE = LOGICAL (Read)
`````````````````````````
If TRUE, a detailed description of the co-ordinate Frame in which the
centroided positions will be reported is displayed before the
positions themselves. [current value]



DEVICE = DEVICE (Read)
``````````````````````
The graphics device which is to be used to give the initial guesses at
the centroid positions. It is only accessed if Parameter MODE is given
the value "Cursor". [Current graphics device]



ERROR = LITERAL (Write)
```````````````````````
The errors associated with the position written to Parameter CENTRE.



GUESS = _LOGICAL (Read)
```````````````````````
If TRUE, then the supplied guesses for the centroid positions will be
included in the screen and log file output, together with the accurate
positions. [current value]



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a positions list giving the initial guesses at
the centroid positions, such as produced by applications CURSOR,
LISTMAKE, etc. It is only accessed if Parameter MODE is given the
value "Catalogue".



INIT = LITERAL (Read)
`````````````````````
An initial guess at the co-ordinates of the next feature to be
centroided, in the current co-ordinate Frame of the NDF (supplying a
colon ":" will display details of the current co-ordinate Frame). The
position should be supplied as a list of formatted axis values
separated by spaces or commas. INIT is only accessed if Parameter MODE
is given the value "Interface". If the initial co-ordinates are
supplied on the command line only one centroid will be found;
otherwise the application will ask for further guesses, which may be
terminated by supplying the null value (!).



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the text file to log the results. If null, there will be no
logging. Note this is intended for the human reader and is not
intended for passing to other applications. [!]



MARK = LITERAL (Read)
`````````````````````
Only accessed if Parameter MODE is given the value "Cursor". It
indicates which positions are to be marked on the screen using the
marker type given by Parameter MARKER. It can take any of the
following values.


+ "Initial" -- The position of the cursor when the mouse button is
pressed is marked.
+ "Centroid" -- The corresponding centroid position is marked.
+ "None" -- No positions are marked.

[current value]



MARKER = INTEGER (Read)
```````````````````````
This parameter is only accessed if Parameter MARK is set TRUE. It
specifies the type of marker with which each cursor position should be
marked, and should be given as an integer PGPLOT marker type. For
instance, 0 gives a box, 1 gives a dot, 2 gives a cross, 3 gives an
asterisk, 7 gives a triangle. The value must be larger than or equal
to -31. [current value]



MAXITER = _INTEGER (Read)
`````````````````````````
Maximum number of iterations to be used in the search. It must be in
the range 1--9. The dynamic default is 3. [9]



MAXSHIFT() = _REAL (Read)
`````````````````````````
Maximum shift in each dimension allowed between the guess and output
positions in pixels. Each must lie in the range 0.0--26.0. If only a
single value is given, then it will be duplicated to all dimensions.
The dynamic default is half of SEARCH + 1. [9.0]



MODE = LITERAL (Read)
`````````````````````
The mode in which the initial co-ordinates are to be obtained. The
supplied string can be one of the following values.


+ "Interface" -- positions are obtained using Parameter INIT.
+ "Cursor" -- positions are obtained using the graphics cursor of the
device specified by Parameter DEVICE.
+ "Catalogue" -- positions are obtained from a positions list using
Parameter INCAT.
+ "File" -- positions are obtained from a text file using Parameter
  COIN.

[current value]



NDF = NDF (Read)
````````````````
The NDF structure containing the data array to be analysed. In cursor
mode (see Parameter MODE), the run-time default is the displayed data,
as recorded in the graphics database. In other modes, there is no run-
time default and the user must supply a value. []



NSIM = _INTEGER (Read)
``````````````````````
The number of simulations or realisations using the variance
information in order to estimate the error in the centroid position.
The uncertainty in the centroid error decreases as one over the square
root of NSIM. The range of acceptable values is 3--10000. [100]



OUTCAT = FILENAME (Write)
`````````````````````````
The output catalogue in which to store the centroided positions. If a
null value (!) is supplied, no output catalogue is produced. See also
Parameter CATFRAME. [!]



PLOTSTYLE = GROUP (Read)
````````````````````````
A group of attribute settings describing the style to use when drawing
the graphics markers specified by Parameter MARK.
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
error is reported). [current value]



POSITIVE = _LOGICAL (Read)
``````````````````````````
TRUE, if array features are positive above the background. [TRUE]



SEARCH() = _INTEGER (Read)
``````````````````````````
Size in pixels of the search box to be used. If only a single value is
given, then it will be duplicated to all dimensions so that a square,
cube or hypercube region is searched. Each value must be odd and lie
in the range 3--51. [9]



TITLE = LITERAL (Read)
``````````````````````
A title to store with the output catalogue specified by Parameter
OUTCAT, and to display before the centroid positions are listed. If a
null (!) value is supplied, the title is taken from any input
catalogue specified by Parameter INCAT, or is a fixed string including
the name of the NDF. [!]



TOLER = _REAL (Read)
````````````````````
Accuracy in pixels required in centroiding. Iterations will stop when
the shift between successive centroid positions is less than the
accuracy. The accuracy must lie in the range 0.0--2.0. [0.05]



XCEN = LITERAL (Write)
``````````````````````
The formatted X co-ordinate of the last centroid position, in the
current co-ordinate Frame of the NDF.



XERR = LITERAL (Write)
``````````````````````
The error associated with the value written to Parameter XCEN.



YCEN = LITERAL (Write)
``````````````````````
The formatted Y co-ordinate of the last centroid position, in the
current co-ordinate Frame of the NDF.



YERR = LITERAL (Write)
``````````````````````
The error associated with the value written to Parameter YCEN.



Examples
~~~~~~~~
centroid cluster cu
This finds the centroids in the NDF called cluster via the graphics
cursor on the current graphics device.
centroid cluster cu search=21 mark=ce plotstyle='colour=red'
This finds the centroids in the NDF called cluster via the graphics
cursor on the current graphics device. The search box for the centroid
is 21 pixels in each dimension. The centroid positions are marked
using a red symbol.
centroid cluster i "21.7,5007.1"
This finds the centroid of the object in the two-dimensional NDF
called cluster around the current Frame co-ordinate (21.7,5007.1).
centroid arp244(6,,) i "40,30" toler=0.01
This finds the two-dimensional centroid of the feature near pixel
(6,40,30) in the three-dimensional NDF called arp244 (assuming the
current co-ordinate Frame of the NDF is PIXEL). The centroid must be
found to 0.01 pixels.
centroid cluster cu xcen=(xp) ycen=(yp)
This finds the centroid of an object in the two-dimensional NDF called
cluster using a graphics cursor, and writes the centroid co-ordinates
to ICL variables XP and YP for use in other applications.
centroid cluster mode=file coin=objects.dat logfile=centroids.log
This finds the centroids in the NDF called cluster. The initial
positions are given in the text file objects.dat in the current co-
ordinate Frame. A log of the input parameter values, initial and
centroid positions is written to the text file centroids.log.
centroid cluster mode=cat incat=a outcat=b catframe=ecl
This example reads the initial guess positions from the positions list
in file a.FIT, and writes the accurate centroid positions to positions
list file b.FIT, storing the output positions in ecliptic co-
ordinates. The input file may, for instance, have been created using
the application CURSOR.



Notes
~~~~~


+ All positions are supplied and reported in the current co-ordinate
Frame of the NDF. A description of the co-ordinate Frame being used is
given if Parameter DESCRIBE is set to a TRUE value. Application
WCSFRAME can be used to change the current co-ordinate Frame of the
NDF before running this application if required.
+ In Cursor or Interface mode, only the first 200 supplied positions
will be stored in the output catalogue. Any further positions will be
displayed on the screen but not stored in the output catalogue.
+ The centroid positions are not displayed on the screen when the
  message filter environment variable MSG_FILTER is set to QUIET. The
  creation of output parameters and files is unaffected by MSG_FILTER.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PSF, CURSOR, LISTSHOW, LISTMAKE.


Estimation of Centroid Positions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each centroid position is obtained by projecting the data values
within a search box centred on the supplied position, on to each axis
in turn. This forms a set of profiles for the feature, one for each
axis. An estimate of the background at each point in these profiles is
made and subtracted from the profile. This flattens the profile
backgrounds, removing any slope in the data. Once the profiles have
been flattened in this way, and estimate of the background noise in
each is made. The centroid of the feature is then found using only the
data above the noise level.
Successive estimates of the centroid position are made by using the
previous estimate of the centroid as the initial position for another
estimation. This loop is repeated up to a maximum number of
iterations, though it normally terminates when a desired accuracy has
been achieved.
The achieved accuracy is affected by noise, and the presence of non-
Gaussian or overlapping features, but typically an accuracy better
than 0.1 pixel is readily attainable for stars. The error in the
centroid position may be estimated by a Monte-Carlo method using the
data variance to generate realisations of the data about the feature
(see Parameter CERROR). Each realisation is processed identically to
the actual data, and statistics are formed to derive the standard
deviations.


Copyright
~~~~~~~~~
Copyright (C) 1991, 1992, 1998-2001 Central Laboratory of the Research
Councils Copyright (C) 2004-2006 Particle Physics and Astronomy
Research Council. Copyright (C) 2009-2010 Science and Technology
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


+ The processing of bad pixels and all non-complex numeric types is
  supported.




