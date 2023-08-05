

SETSKY
======


Purpose
~~~~~~~
Stores new WCS information within an NDF


Description
~~~~~~~~~~~
This application adds WCS information describing a celestial sky co-
ordinate system to a two-dimensional NDF. This information can be
stored either in the form of a standard NDF WCS component, or in the
form of an "IRAS90 astrometry structure" (see parameter IRAS90).
The astrometry is determined either by you supplying explicit values
for certain projection parameters, or by you providing the sky and
corresponding image co-ordinates for a set of positions (see parameter
POSITIONS). In the latter case, the projection parameters are
determined automatically by searching through parameter space in order
to minimise the sum of the squared residuals between the supplied
pixel co-ordinates and the transformed sky co-ordinates. You may force
particular projection parameters to take certain values by assigning
an explicit value to the corresponding application parameter listed
below. The individual residuals at each position can be written out to
a logfile so that you can identify any aberrant points. The RMS
residual (in pixels) implied by the best-fitting parameters is
displayed.


Usage
~~~~~


::

    
       setsky ndf positions coords epoch [projtype] [lon] [lat]
              [refcode] [pixelsize] [orient] [tilt] [logfile]
       



ADAM parameters
~~~~~~~~~~~~~~~



COORDS = LITERAL (Read)
```````````````````````
The sky co-ordinate system to use. Valid values include "Ecliptic"
(IAU 1980), "Equatorial" (FK4 and FK5), and "Galactic" (IAU 1958).
Ecliptic and equatorial co-ordinates are referred to the mean equinox
of a given epoch. This epoch is specified by appending it to the
system name, in parentheses, for example, "Equatorial(1994.5)". The
epoch may be preceded by a single character, "B" or "J", indicating
that the epoch is Besselian or Julian respectively. If this letter is
missing, a Besselian epoch is assumed if the epoch is less than
1984.0, and a Julian epoch is assumed otherwise.



EPOCH = DOUBLE PRECISION (Read)
```````````````````````````````
The Julian epoch at which the observation was made (e.g. "1994.0").



IRAS90 = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, then the WCS information will be stored
in the form of an IRAS90 astrometry structure. This is the form used
by the IRAS90 package (see SUN/163). In this case, any existing IRAS90
astrometry structure will be over-written. See the "Notes:" section
below for warnings about using this form.
If a FALSE value is supplied, then the WCS information will be stored
in the form of a standard NDF WCS component which will be recognized,
used and updated correctly by most other Starlink software.
If a null value (!) is supplied, then a TRUE value will be used if the
supplied NDF already has an IRAS90 extension. Otherwise a FALSE value
will be used. [!]



LAT = LITERAL (Read)
````````````````````
The latitude of the reference point, in the co-ordinate system
specified by parameter COORDS. For example, if COORDS is "Equatorial",
LAT is the Declination. See SUN/163, Section 4.7.2 for full details of
the allowed syntax for specifying this position. For convenience here
are some examples how you may specify the Declination -45 degrees, 12
arcminutes: "-45 12 00", "-45 12", "-45d 12m", "-45.2d", "-451200",
"-0.78888r". The last of these is a radians value. A null value causes
the latitude of the reference point to be estimated automatically from
the data supplied for parameter POSITIONS. [!]



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the text file to log the final projection parameter values and
the residual at each supplied position. If null, there will be no
logging. This parameter is ignored if a null value is given to
parameter POSITIONS. [!]



LON= LITERAL (Read)
```````````````````
The longitude of the reference point, in the co-ordinate system
specified by parameter COORDS. For example, if COORDS is "Equatorial",
LON is the Right Ascension. See SUN/163, Section 4.7.2 for full
details of the allowed syntax for specifying this position. For
convenience here are some examples how you may specify the Right
Ascension 11 hours, 34 minutes, and 56.2 seconds: "11 34 56.2", "11h
34m 56.2s", "11 34.9366", "11.58228", "113456.2". See parameter LAT
for examples of specifying a non-equatorial longitude. A null value
causes the longitude of the reference point to be estimated
automatically from the data supplied for parameter POSITIONS. [!]



NDF = NDF (Read and Write)
``````````````````````````
The NDF in which to store the WCS information.



ORIENT = LITERAL (Read)
```````````````````````
The position angle of the NDF's y axis on the celestial sphere,
measured from north through east. North is defined as the direction of
increasing sky latitude, and east is the direction of increasing sky
longitude. Values are constrained to the range 0 to two-pi radians. A
null value causes the position angle to be estimated automatically
from the data supplied for parameter POSITIONS. [!]



PIXELREF( 2 ) = REAL (Read)
```````````````````````````
The pixel co-ordinates of the reference pixel (x then y). This
parameter is ignored unless REFCODE = "Pixel". Remember that the
centre of a pixel at indices i,j is (i-0.5,j-0.5). A null value causes
the pixel co-ordinates of the reference point to be estimated
automatically from the data supplied for parameter POSITIONS. [!]



PIXELSIZE( 2 ) = _REAL (Read)
`````````````````````````````
The x and y pixel sizes at the reference position. If only one value
is given, the pixel is deemed to be square. Values may be given in a
variety of units (see parameter LAT). For example, 0.54 arcseconds
could be specified as "0.54s" or "0.009m" or "2.618E-6r". A null value
causes the pixel dimensions to be estimated automatically from the
data supplied for parameter POSITIONS. [!]



POSITIONS = LITERAL (Read)
``````````````````````````
A list of sky co-ordinates and corresponding image co-ordinates for
the set of positions which are to be used to determine the astrometry.
If a null value is given then the astrometry is determined by the
explicit values you supply for each of the other parameters. Each
position is defined by four values, the sky longitude (in the same
format as for parameter LON), the sky latitude (in the same format as
for parameter LAT), the image pixel x co-ordinate and the image pixel
y co-ordinate (both decimal values). These should be supplied (in the
order stated) for each position. These values are given in the form of
a `group expression' (see SUN/150). This means that values can be
either typed in directly or supplied in a text file. If typed in
directly, the items in the list should be separated by commas, and you
are re-prompted for further values if the last supplied value ends in
a minus sign. If conveyed in a text file, they should again be
separated by commas, but can be split across lines. The name of the
text file is given in response to the prompt, preceded by an `up
arrow' symbol (^).



PROJTYPE = LITERAL (Read)
`````````````````````````
The type of projection to use. The options are: "Aitoff" - Aitoff
equal-area, "Gnomonic" - Gnomonic (i.e. tangent plane), "Lambert" -
Lambert normal equivalent cylindrical, "Orthographic" - Orthographic.
The following synonyms are also recognised: "All_sky" - Aitoff,
"Cylindrical" - Lambert, "Tangent_plane" - Gnomonic.
See SUN/163 for descriptions of these projections. A null value causes
the projection to be determined automatically from the data supplied
for parameter POSITIONS. [!]



REFCODE = LITERAL (Read)
````````````````````````
The code for the reference pixel. If it has value "Pixel" this
requests that pixel co-ordinates for the reference point be obtained
through parameter PIXELREF. The other options are locations specified
by two characters, the first corresponding to the vertical position
and the second the horizontal. For the vertical, valid positions are
T(op), B(ottom), or C(entre); and for the horizontal the options are
L(eft), R(ight), or C(entre). Thus REFCODE = "CC" means the reference
position is at the centre of the NDF image, and "BL" specifies that
the reference position is at the centre of the bottom-left pixel in
the image. A null value causes the pixel co-ordinates of the reference
point to be estimated automatically from the data supplied for
parameter POSITIONS. [!]



TILT = LITERAL (Read)
`````````````````````
The angle through which the celestial sphere is to be rotated prior to
doing the projection. The axis of rotation is a radius passing through
the reference point. The rotation is in an anti-clockwise sense when
looking from the reference point towards the centre of the celestial
sphere. In common circumstances this can be set to zero. Values may be
given in a variety of units (see parameter LAT). Values are
constrained to the range 0 to two-pi radians. A null value causes the
latitude of the reference point to be estimated automatically from the
data supplied for parameter POSITIONS. ["0.0"]



Examples
~~~~~~~~
setsky m51 ^stars.lis ecl(j1994.0) 1994.0 logfile=m51.log
This creates a WCS component to a two-dimensional NDF called m51. The
values for parameters PROJTYPE, LON, LAT, PIXELREF, PIXELSIZE and
ORIENT are determined automatically so that they minimised the sum of
the squared residuals (in pixels) at each of the positions specified
in the file stars.lis. This file contains a line for each position,
each line containing an ecliptic longitude and latitude, followed by a
pair of image co-ordinates. These values should be separated by
commas. The ecliptic co-ordinates were determined at Julian epoch
1994.0, and are referred to the mean equinox at Julian epoch 1994.0.
The determined parameter values together with the residual at each
position are logged to file m51.log.
setsky m51 ^stars.lis ecl(j1994.0) 1994.0 orient=0 projtype=orth
This creates a WCS component within the two-dimensional NDF called
m51. The values for parameters PROJTYPE, LON, LAT, PIXELREF and
PIXELSIZE are determined automatically as in the previous example. In
this example however, an Orthographic projection is forced, and the
value zero is assigned to parameter ORIENT, resulting in north being
`upwards' in the image.
setsky virgo "!" eq(j2000.0) 1989.3 gn "12 29" "+12 30" bl 1.1s 0.0d
This creates a WCS component within the two-dimensional NDF called
virgo. It is a gnomonic projection in the equatorial system at Julian
epoch 2000.0. The bottom-left pixel of the image is located at Right
Ascension 12 hours 29 minutes, Declination +12 degrees 30 minutes. A
pixel at that position is square and has angular size of 1.1
arcseconds. The image was observed at epoch 1989.3. At the bottom-left
of the image, north is at the top, parallel to the y-axis of the
image.
setsky map "!" galactic(1950.0) 1993.8 aitoff 90 0 cc [0.5d,0.007r]
180.0d
This creates a WCS component within the two-dimensional NDF called
map. It is an Aitoff projection in the galactic system at Besselian
epoch 1950.0. The centre of the image is located at galactic longitude
90 degrees, latitude 0 degrees. A pixel at that position is
rectangular and has angular size of 0.5 degrees by 0.007 radians. The
image was made at epoch 1993.8. At the image centre, south is at the
top and is parallel to the y-axis of the image.
setsky zodiac "!" ec 1983.4 or 10.3 -5.6 Pixel 20m 0.3d
pixelref=[9.5,-11.2] IRAS90=YES
This creates an IRAS90 astrometry extension within the two-dimensional
NDF called zodiac. It is an orthographic projection in the Ecliptic
system at Besselian epoch 1950.0. The reference point at pixel co-
ordinates (9.5,-11.2) corresponds to ecliptic longitude 10.3 degrees,
latitude -5.6 degrees. A pixel at that position is square and has
angular size of 20 arcminutes. The image was observed at epoch 1983.4.
At the reference point the y-axis of the image points to 0.3 degrees
east of north.



Notes
~~~~~


+ The GAIA image display tool (SUN/214) provides various interactive
tools for storing new WCS information within an NDF.
+ This application was written to supply the limited range of WCS
functions required by the IRAS90 package. For instance, it does not
support the complete range or projections or sky co-ordinate systems
which may be represented by the more general NDF WCS component.
+ If WCS information is stored in the form of an IRAS90 astrometry
  structure (see parameter IRAS90), it will in general be invalidated by
  any subsequent KAPPA commands which modify the transformation between
  sky and pixel coordinates. For instance, if the image is moved using
  SLIDE (for example), then the IRAS90 astrometry structure will no
  longer correctly describe the sky co-ordinates associated with each
  pixel. For this reason (amongst others) it is better to set parameter
  IRAS90 to a false value.




Related Applications
~~~~~~~~~~~~~~~~~~~~
ASTROM; IRAS90: SKYALIGN, SKYBOX, SKYGRID, SKYLINE, SKYMARK, SKYPOS,
SKYWRITE.


Copyright
~~~~~~~~~
Copyright (C) 1994 Science & Engineering Research Council. Copyright
(C) 1995, 2001 Central Laboratory of the Research Councils. All Rights
Reserved.


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


