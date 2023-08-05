

BEAMFIT
=======


Purpose
~~~~~~~
Fits beam features in a two-dimensional NDF


Description
~~~~~~~~~~~
This fits generalised Gaussians (cf. PSF) to beam features within the
data array of a two-dimensional NDF given approximate initial co-
ordinates. It uses an unconstrained least-squares minimisation
involving the residuals and a modified Levenberg-Marquardt algorithm.
The beam feature is a set of connected pixels which are either above
or below the surrounding background region. The errors in the fitted
coefficients are also calculated.
You may apply various constraints. These are either fixed, or
relative. Fixed values include the FWHM, background level, or the
shape exponent that defaults to 2 thus fits a normal distribution.
Relative constraints define the properties of secondary beam features
with respect to the primary (first given) feature, and can specify
amplitude ratios, and beam separations in Cartesian or polar co-
ordinates.
Four methods are available for obtaining the initial positions,
selected using Parameter MODE:


+ from the parameter system (see Parameters POS, POS2--POS5);
+ using a graphics cursor to indicate the feature in a previously
displayed data array (see Parameter DEVICE);
+ from a specified positions list (see Parameter INCAT); or
+ from a simple text file containing a list of co-ordinates (see
  Parameter COIN).

In the first two modes the application loops, asking for new feature
co-ordinates until it is told to quit or encounters an error or the
maximum number of features is reached. The last is five, unless
Parameters POS2---POS5 define the location of the secondary beams and
then only the primary beam's position is demanded.
BEAMFIT both reports and stores in parameters its results. These are
fit coefficients and their errors, the offsets and position angles of
the secondary beam features with respect to the primary beam, and the
offset of the primary beam from a reference position. Also a listing
of the fit results may be written to a log file geared more towards
human readers, including details of the input parameters (see
Parameter LOGFILE).


Usage
~~~~~


::

    
       beamfit ndf [mode] { incat=?
                          { [beams]
                          { coin=?
                          { [beams] pos pos2-pos5=?
                          mode
       



ADAM parameters
~~~~~~~~~~~~~~~



AMP( 2 * BEAMS ) = _DOUBLE (Write)
``````````````````````````````````
The amplitude and its error for each beam.



AMPRATIO( ) = _REAL (Read)
``````````````````````````
If number of beam positions given by BEAMS is more than one, this
specifies the ratio of the amplitude of the secondary beams to the
primary. Thus you should supply one fewer value than the number of
beams. If you give fewer than that the last ratio is copied to the
missing values. The ratios would normally be negative, usually -1 or
-0.5. AMPRATIO is ignored when there is only one beam feature to fit.
[!]



BACK( 2 * BEAMS ) = _DOUBLE (Write)
```````````````````````````````````
The background level and its error at each beam position.



BEAMS = _INTEGER (Read)
```````````````````````
The number of beam positions to fit. This will normally be 1, unless a
chopped observation is supplied, when there may be two or three beam
positions. This parameter is ignored for "File" and "Catalogue" modes,
where the number comes from the number of beam positions read from the
files; and for "Interface" mode when the beam positions POS, POS2,
etc. are supplied in full on the command line without BEAMS. In all
modes there is a maximum of five positions, which for "File" or
"Catalogue" modes will be the first five. [1]



CENTRE( 2 * BEAMS ) = LITERAL (Write)
`````````````````````````````````````
The formatted co-ordinates and their errors of each beam in the
current co-ordinate Frame of the NDF.



CIRCULAR = _LOGICAL (Read)
``````````````````````````
If set TRUE only circular beams will be fit. [FALSE]



COIN = FILENAME (Read)
``````````````````````
Name of a text file containing the initial guesses at the co-ordinates
of beams to be fitted. It is only accessed if Parameter MODE is given
the value "File". Each line should contain the formatted axis values
for a single position, in the current Frame of the NDF. Axis values
can be separated by spaces, tabs or commas. The file may contain
comment lines with the first character # or !.



DESCRIBE = _LOGICAL (Read)
``````````````````````````
If TRUE, a detailed description of the co-ordinate Frame in which the
beam positions will be reported is displayed before the positions
themselves. [current value]



DEVICE = DEVICE (Read)
``````````````````````
The graphics device which is to be used to give the initial guesses at
the beam positions. Only accessed if Parameter MODE is given the value
"Cursor". [Current graphics device]



FIXAMP = _DOUBLE (Read)
```````````````````````
This specifies the fixed amplitude of the first beam. Secondary
sources arising from chopped data use FIXAMP multiplied by the
AMPRATIO. A null value indicates that the amplitude should be fitted.
[!]



FITAREA() = _INTEGER (Read)
```````````````````````````
Size in pixels of the fitting area to be used. This should fully
encompass the beam and also include some background signal. If only a
single value is given, then it will be duplicated to all dimensions so
that a square region is fitted. Each value must be at least 9. A null
value requests that the full data array is used. [!]



FIXBACK = _DOUBLE (Read)
````````````````````````
If a non-null value is supplied then the model fit will use that value
as the constant background level otherwise the background is a free
parameter of the fit. [!]



FIXFWHM = _LOGICAL (Read)
`````````````````````````
If this is set TRUE then the model fit will use the full-width half-
maximum values for the beams supplied through Parameter FWHM. FALSE
demands that the FWHM values are free parameters of the fit. [FALSE]



FIXPOS = _LOGICAL (Read)
````````````````````````
If TRUE, the supplied position of each beam is used and the centre co-
ordinates of the beam features are not fit. FALSE causes the initial
estimate of the location of each beam to come from the source selected
by Parameter MODE, and all these locations are part of the fitting
process (however note the exception when FIXSEP = TRUE. It is
advisable not to use this option in the inaccurate "Cursor" mode.
[FALSE]



FIXSEP = _LOGICAL (Read)
````````````````````````
If TRUE, the separations of secondary beams from the primary beam are
fixed, and this takes precedence over Parameter FIXPOS. If FALSE, the
beam separations are free to be fitted (although it is actually the
centres being fit). It is advisable not to use this option in the
inaccurate "Cursor" mode. [FALSE]



FWHM = LITERAL (Read)
`````````````````````
The initial full-width half-maximum (FWHM) values for each beam. These
become fixed values if FIXFWHM is set TRUE.
A number of options are available.

+ A single value gives the same circular FWHM for all beams.
+ When Parameter CIRCULAR is TRUE, supply a list of values one for
each of the number of beams. These should be supplied in the same
order as the corresponding beam positions.
+ A pair of values sets the major- and minor-axis values for all
beams, provided Parameter CIRCULAR is FALSE.
+ Major- and minor-axis pairs, whose order should match that of the
  corresponding beams. Again CIRCULAR should be FALSE. Multiple values
  are separated by commas. An error is issued should none of these
  options be offered.

If the current co-ordinate Frame of the NDF is a SKY Frame (e.g. right
ascension and declination), then each value should be supplied as an
increment of celestial latitude (e.g. declination). Thus, "5.7" means
5.7 arcseconds, "20:0" would mean 20 arcminutes, and "1:0:0" would
mean 1 degree. If the current co-ordinate Frame is not a SKY Frame,
then the widths should be specified as an increment along Axis 1 of
the current co-ordinate Frame. Thus, if the Current Frame is PIXEL,
the value should be given simply as a number of pixels.
Null requests that BEAMFIT itself estimates the initial FWHM values.
[!]



GAMMA( 2 ) = _DOUBLE (Write)
````````````````````````````
The shape exponent and its error for each beam.



GAUSS = _LOGICAL (Read)
```````````````````````
If TRUE, the shape exponent is fixed to be 2; in other words the beams
are modelled as two-dimensional normal distributions. If FALSE, the
shape exponent is a free parameter in each fit. [TRUE]



INCAT = FILENAME (Read)
```````````````````````
A catalogue containing a positions list giving the initial guesses at
the beam positions, such as produced by applications CURSOR, LISTMAKE,
etc. It is only accessed if Parameter MODE is given the value
"Catalogue".



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the text file to log the results. If null, there will be no
logging. Note this is intended for the human reader and is not
intended for passing to other applications. [!]



MAJFWHM( 2 ) = _DOUBLE (Write)
``````````````````````````````
The major-axis FWHM and its error, measured in the current co-ordinate
Frame of the NDF, for each beam. Note that the unit for sky co-
ordinate Frames is radians.



MARK = LITERAL (Read)
`````````````````````
Only accessed if Parameter MODE is given the value "Cursor". It
indicates which positions are to be marked on the screen using the
marker type given by Parameter MARKER. It can take any of the
following values.


+ "Initial" -- The position of the cursor when the mouse button is
pressed is marked.
+ "Fit" -- The corresponding fit position is marked.
+ "Ellipse" -- As "Fit" but it also plots an ellipse at the FWHM radii
and orientation.
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



MINFWHM( 2 ) = _DOUBLE (Write)
``````````````````````````````
The minor-axis FWHM and its error, measured in the current co-ordinate
Frame of the NDF, for each beam. Note that the unit for sky co-
ordinate Frames is radians.



MODE = LITERAL (Read)
`````````````````````
The mode in which the initial co-ordinates are to be obtained. The
supplied string can be one of the following values.


+ "Interface" -- positions are obtained using Parameters POS, POS2--
POS5.
+ "Cursor" -- positions are obtained using the graphics cursor of the
device specified by Parameter DEVICE.
+ "Catalogue" -- positions are obtained from a positions list using
Parameter INCAT.
+ "File" -- positions are obtained from a text file using Parameter
  COIN. [current value]





NDF = NDF (Read)
````````````````
The NDF structure containing the data array to be analysed. In cursor
mode (see Parameter MODE), the run-time default is the displayed data,
as recorded in the graphics database. In other modes, there is no run-
time default and the user must supply a value. []



OFFSET( ) = LITERAL (Write)
```````````````````````````
The formatted offset and its error of each secondary beam feature with
respect to the primary beam. They are measured in the current Frame of
the NDF along a latitude axis if that Frame is in the SKY Domain, or
the first axis otherwise. The number of values stored is twice the
number of beams. The array alternates an offset, then its
corresponding error, appearing in beam order starting with the first
secondary beam.



ORIENT( 2 * BEAMS ) = _DOUBLE (Write)
`````````````````````````````````````
The orientation and its error, measured in degrees for each beam. If
the current WCS frame is a SKY Frame, the angle is measured from North
through East. For other Frames the angle is from the X-axis through Y.



PA() = _REAL (Write)
````````````````````
The position angle and its errors of each secondary beam feature with
respect to the primary beam. They are measured in the current Frame of
the NDF from North through East if that is a SKY Domain, or
anticlockwise from the Y axis otherwise. The number of values stored
is twice the number of beams. The array alternates a position angle,
then its corresponding error, appearing in beam order starting with
the first secondary beam.



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



POLAR = _LOGICAL (Read)
```````````````````````
If TRUE, the co-ordinates supplied through POS2--POS5 are interpreted
in polar co-ordinates (offset, position angle) about the primary beam.
The radial co-ordinate is a distance measured in units of the latitude
axis if the current WCS Frame is a a SKY Domain, or the first axis for
other Frames. For a SKY current WCS Frame, position angle follows the
standard convention of North through East. For other Frames the angle
is measured from the second axis anticlockwise, e.g. for a PIXEL Frame
it would be from Y through negative X, not the standard X through Y.
If FALSE, the co-ordinates are the regular axis co-ordinates in the
current Frame.
POLAR is only accessed when there is more than one beam to fit. [TRUE]



POS = LITERAL (Read)
````````````````````
When MODE = "Interface" POS specifies the co-ordinates of the primary
beam position. This is either merely an initial guess for the fit, or
if Parameter FIXPOS is TRUE, it defines a fixed location. It is
specified in the current co-ordinate Frame of the NDF (supplying a
colon ":" will display details of the current co-ordinate Frame). A
position should be supplied as a list of formatted WCS axis values
separated by spaces or commas, and should lie within the bounds of the
NDF.
If the initial co-ordinates are supplied on the command line without
BEAMS the number of contiguous POS, POS2,... parameters specifies the
number of beams to be fit.



POS2-POS5 = LITERAL (Read)
``````````````````````````
When MODE = "Interface" these parameters specify the co-ordinates of
the secondary beam positions. These should lie within the bounds of
the NDF. For each parameter the supplied location may be merely an
initial guess for the fit, or if Parameter FIXPOS is TRUE, it defines
a fixed location, unless Parameter FIXSEP is TRUE, whereupon it
defines a fixed separation from the primary beam.
For POLAR = FALSE each distance should be given as a single literal
string containing a space- or comma-separated list of formatted axis
values measured in the current co-ordinate Frame of the NDF. The
allowed formats depends on the class of the current Frame. Supplying a
single colon ":" will display details of the current Frame, together
with an indication of the format required for each axis value, and a
new parameter value is then obtained.
If Parameter POLAR is TRUE, POS2--POS5 may be given as an offset
followed by a position angle. See Parameter POLAR for more details of
the sense of the angle and the offset co-ordinates.
The parameter name increments by 1 for each subsequent beam feature.
Thus POS2 applies to the first secondary beam (second position in
all), POS3 is for the second secondary beam, and so on. As the total
number of parameters required is one fewer than the value of Parameter
BEAMS, POS2--POS5 are only accessed when BEAMS exceeds 1.



REFOFF( 2 ) = LITERAL (Write)
`````````````````````````````
The formatted offset followed by its error of the primary beam's
location with respect to the reference position (see Parameter
REFPOS). The offset might be used to assess the optical alignment of
an instrument. The ofset and its error are measured in the current
Frame of the NDF along a latitude axis if that Frame is in the SKY
Domain, or the first axis otherwise. The error is derived entirely
from the uncertainities in the fitted position of the primary beam,
i.e. the reference position has no error attached to it. By definition
the error is zero when FIXPOS is TRUE.



REFPOS = LITERAL (Read)
```````````````````````
The reference position. This is often the desired position for the
beam. The offset of the primary beam with respect to this point is
reported and stored in Parameter REFOFF. It is only accessed if the
current WCS Frame in the NDF is not a SKY Domain containing a
reference position.
The co-ordinates are specified in the current WCS Frame of the NDF
(supplying a colon ":" will display details of the current co-ordinate
Frame). A position should be supplied either as a list of formatted
WCS axis values separated by spaces or commas. A null value (!)
requests that the centre of the supplied map is deemed to be the
reference position.



RESID = NDF (Write)
```````````````````
The map of the residuals (data minus model) of the fit. It inherits
the properties of the input NDF, except that its data type is _DOUBLE
or _REAL depending on the precision demanded by the type of IN, and no
variance is propagated. A null (!) value requests that no residual map
be created. [!]



RMS = _REAL (Write)
```````````````````
The primary beam position's root mean-squared deviation from the fit.



SUM = _DOUBLE (Write)
`````````````````````
The total data sum of the multi-Gaussian fit above the background. The
fit is evaluated at the centre of every pixel in the input NDF
(including bad-valued pixels). The fitted background level is then
removed from the fit value, and the sum of these is written to this
output parameter.



TITLE = LITERAL (Read)
``````````````````````
The title for the NDF to contain the residuals of the fit. If null (!)
is entered the NDF will not contain a title. ["KAPPA - BEAMFIT"]



VARIANCE = _LOGICAL (Read)
``````````````````````````
If TRUE, then any VARIANCE component present within the input NDF will
be used to weight the fit; the weight used for each data value is the
reciprocal of the variance. If set to FALSE or there is no VARIANCE
present, all points will be given equal weight. [FALSE]



Examples
~~~~~~~~
beamfit mars_3pos i 1 "5.0,-3.5"
This finds the Gaussian coefficients of the primary beam feature in
the NDF called mars_3pos, using the supplied co-ordinates (5.0,-3.5)
for the initial guess for the beam's centre. The co-ordinates are
measured in the NDF's current co-ordinate Frame. In this case they are
offsets in arcseconds.
beamfit ndf=mars_3pos mode=interface beams=1 pos="5.0,-3.5"
fixback=0.0 As above but now the background is fixed to be zero.
beamfit ndf=mars_3pos mode=interface beams=1 pos="5.0,-3.5"
fixfwhm fwhm=16.5 gauss=f As above but now the Gaussian is constrained
to have a FWHM of 16.5 arcseconds and be circular, but the shape
exponent is not constrained to be 2.
beamfit mars_3pos in beams=1 fwhm=16.5 fitarea=51 pos="5.,-3.5"
As above but now the fitted data is restricted to areas 51x51 pixels
about the initial guess positions. All the other examples use the full
array. Also the FWHM value is now just an initial guess.
beamfit mars_3pos int 3 "5.0,-3.5" ampratio=-0.5 resid=mars_res
As the first example except this finds the Gaussian coefficients of
the primary beam feature and two secondary features. The secondary
features have fixed amplitudes that are half that of the primary
feature and of the opposite polarity. The residuals after subtracting
the fit are stored in NDF mars_res. In all the other examples no
residual map is created.
beamfit mars_3pos int 2 "5.0,-3.5" pos2="60.0,90" fixpos
This finds the Gaussian coefficients of the primary beam feature and a
secondary feature in the NDF called mars_3pos. The supplied co-
ordinates (5.0,-3.5) define the centre, i.e. they are not fitted. Also
the secondary beam is fixed at 60 arcseconds towards the East
(position angle 90 degrees).
beamfit mars_3pos int 2 "5.0,-3.5" pos2="60.0,90" fixsep
As the previous example, except now the separation of the second
position is fixed at 60 arcseconds towards the East from the primary
beam, instead of being an absolute location.
beamfit mars_3pos int 2 "5.0,-3.5" pos2="-60.5,0.6" polar=f fixpos
As the last-but-one example, but now location of the secondary beam is
fixed at (-55.5,-2.9).
beamfit s450 int beams=2 fwhm="7.9,25" ampratio=0.06 circular
pos='"0:0:0,0:0:0"' nopolar pos2="0:0:0,0:0:0" This fits two
superimposed circular Gaussians in the NDF called s450, whose current
WCS is SKY. The beam second being fixed at 6 percent the strength of
the first, with initial widths of 7.9 and 25 arcseconds.
beamfit mode=cu beams=1
This finds the Gaussian coefficients of the primary beam feature of an
NDF, using the graphics cursor on the current graphics device to
indicate the approximate centre of the feature. The NDF being analysed
comes from the graphics database.
beamfit uranus cu 2 mark=ce plotstyle='colour=red' marker=3
This fits to two beam features in the NDF called uranus via the
graphics cursor on the current graphics device. The beam positions are
marked using a red asterisk.
beamfit uranus file 4 coin=features.dat logfile=uranus.log
This fits to the beam features in the NDF called uranus. The initial
positions are given in the text file features.dat in the current co-
ordinate Frame. Only the first four positions will be used. The last
three positions are in polar co-ordinates with respect to the primary
beam. A log of selected input parameter values, and the fitted
coefficients and errors is written to the text file uranus.log.
beamfit uranus mode=cat incat=uranus_beams polar=f
This example reads the initial guess positions from the positions list
in file uranus_beams.FIT. The number of beam features fit is the
number of positions in the catalogue subject to a maximum of five. The
input file may, for instance, have been created using the application
CURSOR.



Notes
~~~~~


+ All positions are supplied and reported in the current co-ordinate
Frame of the NDF. A description of the co-ordinate Frame being used is
given if Parameter DESCRIBE is set to a TRUE value. Application
WCSFRAME can be used to change the current co-ordinate Frame of the
NDF before running this application if required.
+ The uncertainty in the positions are estimated iteratively using the
curvature matrix derived from the Jacobian, itself determined by a
forward-difference approximation.
+ The fit parameters are not displayed on the screen when the message
filter environment variable MSG_FILTER is set to QUIET.
+ If the fitting fails there are specific error codes that can be
  tested and appropriate action taken in scripts: PDA__FICMX when it is
  impossible to derive fit errors, and KAP__LMFOJ when the fitted
  functions from the Levenberg-Marquardt minimisation are orthogonal to
  the Jacobian's columns (usually indicating that FITAREA is too small).




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PSF, CENTROID, CURSOR, LISTSHOW, LISTMAKE; ESP: GAUFIT; Figaro:
FITGAUSS.


Copyright
~~~~~~~~~
Copyright (C) 2007 Particle Physics & Astronomy Research Council.
Copyright (C) 2009, 2010, 2011, 2013, 2018 Science & Technology
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


+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled. Arithmetic is
  performed using double-precision floating point.




