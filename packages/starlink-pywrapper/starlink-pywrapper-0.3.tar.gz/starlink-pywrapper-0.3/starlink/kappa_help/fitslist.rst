

FITSLIST
========


Purpose
~~~~~~~
Lists the FITS extension of an NDF


Description
~~~~~~~~~~~
This application lists the FITS header stored in an NDF FITS
extension. The list may either be reported directly to you, or written
to a text file. The displayed list of headers can be augmented, if
required, by the inclusion of FITS headers representing the current
World Coordinate System defined by the WCS component in the NDF (see
Parameter ENCODING).


Usage
~~~~~


::

    
       fitslist in [logfile]
       



ADAM parameters
~~~~~~~~~~~~~~~



ENCODING = LITERAL (Read)
`````````````````````````
If a non-null value is supplied, the NDF WCS component is used to
generate a set of FITS headers describing the WCS, and these headers
are added into the displayed list of headers (any WCS headers
inherited from the FITS extension are first removed). The value
supplied for ENCODING controls the FITS keywords that will be used to
represent the WCS. The value supplied should be one of the encodings
listed in the "World Co-ordinate Systems" section below. An error is
reported if the WCS cannot be represented using the supplied encoding.
A trailing minus sign appended to the encoding indicates that only the
WCS headers should be displayed (that is, the contents of the FITS
extension are not displayed if the encoding ends with a minus sign).
Also see the FULLWCS parameter. [!]



FULLWCS = _LOGICAL (Read)
`````````````````````````
Only accessed if ENCODING is non-null. If TRUE, then all co-ordinate
frames in the WCS component are written out. Otherwise, only the
current Frame is written out. [FALSE]



IN = NDF (Read)
```````````````
The NDF whose FITS extension is to be listed.



LOGFILE = FILENAME (Read)
`````````````````````````
The name of the text file to store a list of the FITS extension. If it
is null (!) the list of the FITS extension is reported directly to
you. [!]



Examples
~~~~~~~~
fitslist saturn
The contents of the FITS extension in NDF saturn are reported to you.
fitslist saturn fullwcs encoding=fits-wcs
As above but it also lists the standard FITS world-co-ordinate headers
derived from saturn's WCS component, provided such information exists.
fitslist saturn fullwcs encoding=fits-wcs-
As the previous example except that it only lists the standard FITS
world-co-ordinate headers derived from saturn's WCS component. The
headers in the FITS extension are not listed.
fitslist ngc205 logfile=ngcfits.lis
The contents of the FITS extension in NDF ngc205 are written to the
text file ngcfits.lis.



Notes
~~~~~


+ If the NDF does not have a FITS extension the application will exit
  unless the value supplied for ENCODING ends with a minus sign.




World Co-ordinate Systems
~~~~~~~~~~~~~~~~~~~~~~~~~
The ENCODING parameter can take any of the following values.
"FITS-IRAF" --- This uses keywords CRVALi CRPIXi, CDi_j, and the
system commonly used by IRAF. It is described in the document "World
Coordinate Systems Representations Within the FITS Format" by R.J.
Hanisch and D.G. Wells, 1988, available by ftp from fits.cv.nrao.edu
/fits/documents/wcs/wcs88.ps.Z.
"FITS-WCS" --- This is the FITS standard WCS encoding scheme described
in the paper "Representation of celestial coordinates in FITS"
(http://www.atnf.csiro.au/people/mcalabre/WCS/). It is very similar to
"FITS-IRAF" but supports a wider range of projections and co-ordinate
systems.
"FITS-WCS(CD)" --- This is the same as "FITS-WCS" except that the
scaling and rotation of the data array is described by a CD matrix
instead of a PC matrix with associated CDELT values.
"FITS-PC" --- This uses keywords CRVALi, CDELTi, CRPIXi, PCiiijjj,
etc., as described in a previous (now superseded) draft of the above
FITS world co-ordinate system paper by E.W.Greisen and M.Calabretta.
"FITS-AIPS" --- This uses conventions described in the document "Non-
linear Coordinate Systems in AIPS" by Eric W. Greisen (revised 9th
September, 1994), available by ftp from fits.cv.nrao.edu
/fits/documents/wcs/aips27.ps.Z. It is currently employed by the AIPS
data-analysis facility (amongst others), so its use will facilitate
data exchange with AIPS. This encoding uses CROTAi and CDELTi keywords
to describe axis rotation and scaling.
"FITS-AIPS++" --- This is an extension to FITS-AIPS which allows the
use of a wider range of celestial projections, as used by the AIPS++
project.
"FITS-CLASS" --- This uses the conventions of the CLASS project. CLASS
is a software package for reducing single-dish radio and sub-mm
spectroscopic data. It supports double-sideband spectra. See
http://www.iram.fr/IRAMFR/GILDAS/doc/html/class-html/class.html.
"DSS" --- This is the system used by the Digital Sky Survey, and uses
keywords AMDXn, AMDYn, PLTRAH, etc.
"NATIVE" --- This is the native system used by the AST library (see
SUN/210) and provides a loss-free method for transferring WCS
information between AST-based application. It allows more complicated
WCS information to be stored and retrieved than any of the other
encodings.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSEDIT, FITSHEAD; Figaro: FITSKEYS.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 2004 Central Laboratory of the Research Councils. Copyright (C)
2006 Particle Physics & Astronomy Research Council. Copyright (C) 2009
Science & Technology Facilities Council. All Rights Reserved.


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


