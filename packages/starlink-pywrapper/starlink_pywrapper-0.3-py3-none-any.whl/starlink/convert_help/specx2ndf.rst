

SPECX2NDF
=========


Purpose
~~~~~~~
Converts a SPECX map into a simple data cube, or SPECX data files to
individual spectra


Description
~~~~~~~~~~~
This application converts a SPECX map file into a simple data cube
formatted as a standard NDF. It works on map files in Version 4.2 or
later of the SPECX format. It can optionally write a schematic of the
map grid to a text file.
In addition, it will also convert an HDS container file containing an
array of one-dimensional NDFs holding SPECX spectra into a similar
container file holding individual, scalar NDFs each holding a single
spectrum from the supplied array.
In both cases, WCS components are added to the output NDFs describing
the spectral and spatial axes.
A VARIANCE component is added to the output NDF that has a constant
value derived from the Tsys value, integration time, and channel
spacing in the input.


Usage
~~~~~


::

    
       specx2ndf in out [gridfile] [system] [telescope] [latitude] [longitude]
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = _LOGICAL (Read)
``````````````````````
AXIS structures will be added to the output NDF if and only if AXIS is
set TRUE. [FALSE]



GRIDFILE = LITERAL (Read)
`````````````````````````
The name of a text file to which a schematic of the SPECX map will be
written. This schematic shows those positions in the map grid where
spectra were observed. To indicate that a file containing the
schematic is not to be written reply with an exclamation mark ("!").
See Section 'Schematic of the map grid' (below) for further details.
[!]



IN = NDF (Read)
```````````````
The name of the input SPECX map, or container file. The file extension
('.sdf') should not be included since it is appended automatically by
the application.



LATITUDE = LITERAL (Read)
`````````````````````````
The geodetic (geographic) latitude of the telescope where the
observation was made. The value should be specified in sexagesimal
degrees, with a colon (':') to separate the degrees, minutes and
seconds and no embedded spaces. Values in the northern hemisphere are
positive. The default corresponds to the latitude of the JCMT.
["19:49:33"]



LONGITUDE = LITERAL (Read)
``````````````````````````
The geodetic (geographic) longitude of the telescope where the
observation was made. The value should be specified in sexagesimal
degrees, with a colon (':') to separate the degrees, minutes and
seconds and no embedded spaces. Following the usual geographic
convention longitudes west of Greenwich are positive. The default
corresponds to the longitude of the JCMT. ["155:28:47"]



OUT = NDF (Write)
`````````````````
The name of the output NDF containing the data cube or spectra written
by the application. The file extension ('.sdf') should not be included
since it is appended automatically by the application.



SYSTEM = LITERAL (Read)
```````````````````````
Celestial co-ordinate system for output cube. SPECX files do not
record the co-ordinate system for any offsets. The recognised options
are as follows.
"AZ" -- azimuth and elevation "GA" -- galactic "RB" -- B1950 "RD" --
equatorial of date "RJ" -- J2000
SYSTEM needs to be used to set manually the correct co-ordinates for a
map file. ["RJ"]



TELESCOPE = LITERAL (Read)
``````````````````````````
The name of the telescope where the observation was made. This
parameter is used to look up the geodetic (geographical) latitude and
longitude of the telescope. See the documentation of subroutine
SLA_OBS in SUN/67 for a list of permitted values. Alternatively, if
you wish to explicitly enter the latitude and longitude enter
'COORDS'. The values are not case sensitive. ["JCMT"]



Examples
~~~~~~~~
specx2ndf specx_map specx_cube
This example generates an NDF data cube called specx_cube (in file
specx_cube.sdf) from the NDF SPECX map called specx_map (in file
specx_map.sdf). A text file containing a schematic of the map grid
will not be produced.
specx2ndf specx_map specx_cube gridfile=map.grid
This example generates an NDF data cube called specx_cube (in file
specx_cube.sdf) from the NDF SPECX map called specx_map (in file
specx_map.sdf). A text file containing a schematic of the map grid
will be written to file map.grid.



Input and Output Map Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SPECX map files are written by the SPECX package (see SUN/17) for
reducing spectra observed with heterodyne receivers operating in the
mm and sub-mm wavelength range of the electromagnetic spectrum. SPECX
is usually used to process observations obtained with the James Clerk
Maxwell Telescope (JCMT) in Hawaii.
A SPECX map file comprises a regular 'rectangular' two-dimensional
grid of map positions on the sky, with spectra observed at the grid
points. However, a spectrum is not necessarily available at every grid
position; at some positions a spectrum is not observed in order to
save observing time. For example, for a grid centred on a typical,
roughly circular, object spectra may be omitted for the positions at
the corners of the grid. SPECX map files are standard Starlink NDF HDS
structures. The principal array of the NDF is a two-dimensional array
of the grid positions. The value of each element is either a pointer
to the spectrum observed there (in practice the number of the spectrum
in the array where they are stored) or a value indicating that a
spectrum was not observed at this point. In effect the SPECX map
structure is an implementation of a sparse array.
SPECX2NDF expands a SPECX map file into a simple three-dimensional
data cube, again formatted as a standard NDF, in which the first and
second pixel axes corresponds to the spatial axes and the third axes
correspond to the spectral axis. The advantage of this approach is
that the converted file can be examined with standard applications,
such as those in KAPPA (see SUN/95) and easily imported into
visualisation packages, such as Data Explorer (DX, see SUN/203 and
SC/2). When the output data cube is created the columns corresponding
to the positions on the sky grid where spectra were not observed are
filled with 'bad' values (sometimes called 'magic' or 'null' values),
to indicate that valid data are not available at these positions. The
standard Starlink bad value is used. Because of the presence of these
bad values the expanded cube is usually larger than the original map
file.
The created NDF cube has a WCS component in which Axes 1 and 2 are RA
and DEC, and Axis 3 is frequency in units of GHz. The nature of these
axes can be changed if necessary by subsequent use of the WCSATTRIB
application within the KAPPA package. For compatibility with older
applications, AXIS structures may also be added to the output cube
(see parameter AXIS). Axes 1 and 2 are offsets from the central
position of the map, with units of seconds of arc, and Axis 3 is
frequency offset in GHz relative to the central frequency. The pixel
origin is placed at the source position on Axes 1 and 2, and the
central frequency on Axis 3.
SPECX2NDF reads map files in Version 4.2 or later of the SPECX data
format. If it is given a map file in an earlier version of the data
format it will terminate with an error message. Note, however, that
SPECX itself can read map files in earlier versions of the SPECX
format and convert them to Version 4.2.


Schematic of the Map Grid
~~~~~~~~~~~~~~~~~~~~~~~~~
SPECX2NDF has an optional facility to write a crude schematic of the
grid of points observed on the sky to an ASCII text file suitable for
printing or viewing on a terminal screen. This schematic can be useful
in interpreting displays of the data cube. It shows the positions on
the grid where spectra were observed. Each spectrum is numbered within
the SPECX map structure and the first nine are shown using the digits
one to nine. The remaining spectra are shown using an asterisk ('*').
You specify the name of the file to which the schematic is written.
The following is an example of a schematic:
Schematic map grid for CO21
+---------+ 9| | 8| 8765432 | 7|*******9 | 6|******** | 5|****1*** |
4|******** | 3|******** | 2|******** | 1| | +---------+ 123456789


Auxiliary Information
~~~~~~~~~~~~~~~~~~~~~
SPECX2NDF copies all the auxiliary information present in the original
map file to the output data cube. However, the arrays holding the
original spectra are not copied in order to save disk space.


Input and Output Spectra Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In addition to converting SPECX map files, this application can also
convert HDS files which hold an array of one-dimensional NDF
structures, each being a single spectrum extracted by SPECX. Since
arrays of NDFs are not easily accessed, this application extracts each
NDF from the array and creates a new scalar NDF holding the same data
within the output container file. The name of the new NDF is
"SPECTRUM<n>" where "<n>" is its index within the original array of
NDFs. Each new scalar NDF is actually three-dimensional and has the
format described above for an output cube (i.e. Axes 1 and 2 are RA
and DEC, and axis 3 is frequency). However, Pixel Axes 1 and 2 span
only a single pixel (the size of this single spatial pixel is assumed
to be half the size of the resolution of the JCMT at the central
frequency). Inclusion of three-dimensional WCS information allows the
individual spectra to be aligned on the sky (for instance using the
KAPPA WCSALIGN task).


Copyright
~~~~~~~~~
Copyright (C) 1997-1998, 2003-2004 Central Laboratory of the Research
Councils. Copyright (C) 2008, 2010-2012 Science & Technology
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


