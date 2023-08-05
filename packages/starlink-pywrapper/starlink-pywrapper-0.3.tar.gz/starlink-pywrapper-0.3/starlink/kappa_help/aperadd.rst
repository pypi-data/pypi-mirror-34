

APERADD
=======


Purpose
~~~~~~~
Integrates pixel values within an aperture of an NDF


Description
~~~~~~~~~~~
This routine displays statistics for pixels that lie within a
specified aperture of an NDF. The aperture can either be circular
(specified by Parameters CENTRE and DIAM), or arbitrary (specified by
Parameter ARDFILE). If the aperture is specified using Parameters
CENTRE and DIAM, then it must be either one- or two-dimensional.
The following statistics are displayed:


+ The total number of pixels within the aperture
+ The number of good pixels within the aperture
+ The total data sum within the aperture
+ The standard deviation on the total data sum (that is, the square
root of the sum of the individual pixel variances)
+ The mean pixel value within the aperture
+ The standard deviation on the mean pixel value (that is, the
standard deviation on the total data sum divided by the number of
values)
+ The standard deviation of the pixel values within the aperture

If individual pixel variances are not available within the input NDF
(i.e. if it has no VARIANCE component), then each pixel is assumed to
have a constant variance equal to the variance of the pixel values
within the aperture. There is an option to weight pixels so that
pixels with larger variances are given less weight (see Parameter
WEIGHT). The statistics are displayed on the screen and written to
output parameters. They may also be written to a log file.
A pixel is included if its centre is within the aperture, and is not
included otherwise. This simple approach may not be suitable for
accurate aperture photometry, especially where the aperture diameter
is less than about ten times the pixel size. A specialist photometry
package should be used if accuracy, rather than speed, is paramount.


Usage
~~~~~


::

    
       aperadd ndf centre diam
       



ADAM parameters
~~~~~~~~~~~~~~~



ARDFILE = FILENAME (Read)
`````````````````````````
The name of an ARD file containing a description of the aperture. This
allows apertures of almost any shape to be used. If a null (!) value
is supplied then the aperture is assumed to be circular with centre
and diameter given by Parameters CENTRE and DIAM. ARD files can be
created either "by hand" using an editor, or using a specialist
application should as KAPPA:ARDGEN.
The co-ordinate system in which positions within the ARD file are
given should be indicated by including suitable COFRAME or WCS
statements within the file (see SUN/183), but will default to pixel
co-ordinates in the absence of any such statements. For instance,
starting the file with a line containing the text
"COFRAME(SKY,System=FK5)" would indicate that positions are specified
in RA/DEC (FK5,J2000). The statement "COFRAME(PIXEL)" indicates
explicitly that positions are specified in pixel co-ordinates. [!]



CENTRE = LITERAL (Read)
```````````````````````
The co-ordinates of the centre of the circular aperture. Only used if
Parameter ARDFILE is set to null. The position must be given in the
current co-ordinate Frame of the NDF (supplying a colon ":" will
display details of the current co-ordinate Frame). The position should
be supplied as a list of formatted axis values separated by spaces or
commas. See also Parameter USEAXIS. The current co-ordinate Frame can
be changed using KAPPA:WCSFRAME.



DIAM = LITERAL (Read)
`````````````````````
The diameter of the circular aperture. Only used if Parameter ARDFILE
is set to null. If the current co-ordinate Frame of the NDF is a SKY
Frame (e.g. RA and DEC), then the value should be supplied as an
increment of celestial latitude (e.g. DEC). Thus, "10.2" means 10.2
degrees, "0:30" would mean 30 arcminutes, and "0:0:1" would mean 1
arcsecond. If the current co-ordinate Frame is not a SKY Frame, then
the diameter should be specified as an increment along axis 1 of the
current co-ordinate Frame. Thus, if the current Frame is PIXEL, the
value should be given simply as a number of pixels.



LOGFILE = FILENAME (Read)
`````````````````````````
Name of the text file to log the results. If null, there will be no
logging. Note this is intended for the human reader and is not
intended for passing to other applications. [!]



MASK = NDF (Write)
``````````````````
An output NDF containing the pixel mask used to evaluate the reported
statistics. The NDF will contain a positive integer value for pixels
that are included in the statistics, and bad values for all other
pixels. The pixel bounds of the NDF will be the smallest needed to
encompass all used pixels. [!]



MEAN = _DOUBLE (Write)
``````````````````````
The mean of the pixel values within the aperture.



NDF = NDF (Read)
````````````````
The input NDF.



NGOOD = _INTEGER (Write)
````````````````````````
The number of good pixels within the aperture.



NUMPIX = _INTEGER (Write)
`````````````````````````
The total number of pixels within the aperture.



SIGMA = _DOUBLE (Write)
```````````````````````
The standard deviation of the pixel values within the aperture.



SIGMEAN = _DOUBLE (Write)
`````````````````````````
The standard deviation on the mean pixel value. If variances are
available this is the RMS value of the standard deviations associated
with each included pixel value. If variances are not available, it is
the standard deviation of the pixel values divided by the square root
of the number of good pixels in the aperture.



SIGTOTAL = _DOUBLE (Write)
``````````````````````````
The standard deviation on the total data sum. Only created if
variances are available this is the RMS value of the standard
deviations associated with each included pixel value. If variances are
not available, it is the standard deviation of the pixel values
divided by the square root of the number of good pixels in the
aperture.



TOTAL = _DOUBLE (Write)
```````````````````````
The total of the pixel values within the aperture.



USEAXIS = GROUP (Read)
``````````````````````
USEAXIS is only accessed if the current co-ordinate Frame of the NDF
has too many axes. A group of strings should be supplied specifying
the axes which are to be used when specifying the aperture using
Parameters ARDFILE, CENTRE and DIAM. Each axis can be specified using
one of the following options.


+ Its integer index within the current Frame of the input NDF (in the
range 1 to the number of axes in the current Frame).
+ Its symbol string such as "RA" or "VRAD".
+ A generic option where "SPEC" requests the spectral axis, "TIME"
  selects the time axis, "SKYLON" and "SKYLAT" picks the sky longitude
  and latitude axes respectively. Only those axis domains present are
  available as options.

A list of acceptable values is displayed if an illegal value is
supplied. If a null (!) value is supplied, the axes with the same
indices as the two used pixel axes within the NDF are used. [!]



WEIGHT = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, and the input NDF has a VARIANCE
component, then pixels with larger variances will be given smaller
weight in the statistics. The weight associated with each pixel is
proportional to the reciprocal of its variance. The constant of
proportionality is chosen so that the mean weight is unity. The pixel
value and pixel variance are multiplied by the pixels weight before
being used to calculate the statistics. The calculation of the
statistics remains unchanged in all other respects. [FALSE]



Examples
~~~~~~~~
aperadd neb1 "13.5,201.3" 20
This calculates the statistics of the pixels within a circular
aperture of NDF neb1. Assuming the current co-ordinate Frame of neb1
is PIXEL, the aperture is centred at pixel co-ordinates (13.5, 201.3)
and has a diameter of 20 pixels.
aperadd neb1 "15:23:43.2 -22:23:34.2" "10:0"
This also calculates the statistics of the pixels within a circular
aperture of NDF neb1. Assuming the current co-ordinate Frame of neb1
is a SKY Frame describing RA and DEC, the aperture is centred at RA
15:23:43.2 and DEC -22:23:34.2, and has a diameter of 10 arcminutes.
aperadd ndf=neb1 ardfile=outline.dat logfile=obj1
This calculates the statistics of the pixels within an aperture of NDF
neb1 described within the file "outline.dat". The file contains an ARD
description of the required aperture. The results are written to the
log file "obj1".



Notes
~~~~~


+ The statistics are not displayed on the screen when the message
  filter environment variable MSG_FILTER is set to QUIET. The creation
  of output parameters and the log file is unaffected by MSG_FILTER.




ASCII-region-definition Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ARD file may be created by ARDGEN or written manually. In the
latter case consult SUN/183 for full details of the ARD descriptors
and syntax; however, much may be learnt from looking at the ARD files
created by ARDGEN and the ARDGEN documentation. There is also a
summary with examples in the main body of SUN/95.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: STATS, MSTATS, ARDGEN, ARDMASK, ARDPLOT, WCSFRAME.


Copyright
~~~~~~~~~
Copyright (C) 2001, 2003-2004 Central Laboratory of the Research
Councils. Copyright (C) 2009, 2012 Science and Technology Facilities
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


+ This routine correctly processes the WCS, AXIS, DATA, and VARIANCE
components of an NDF data structure.
+ Processing of bad pixels and automatic quality masking are
supported.
+ Bad pixels and automatic quality masking are supported.
+ All non-complex numeric data types can be handled.




