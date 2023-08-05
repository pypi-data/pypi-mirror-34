

IMPAZTEC
========


Purpose
~~~~~~~
Import AzTEC NetCDF files and produce SCUBA-2 ICD-compliant files


Description
~~~~~~~~~~~
Uses the NetCDF library to import raw AzTEC data files and save to NDF
files in a format approximating the SCUBA-2 ICD so that they may
subsequently be read by other SMURF routines to make maps.


ADAM parameters
~~~~~~~~~~~~~~~



IN = _CHAR (Read)
`````````````````
Name of the input NetCDF file to be converted. This name should
include the .nc extension.



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = _CHAR (Read)
``````````````````
Output NDF file.



Notes
~~~~~


+ No base coordinates were stored in netcdf files.
+ Time is presently inaccurate and requires an optimization routine to
calculate the time that makes Az/El and RA/Dec consistent.
+ This command is untested and probably does not work.




Related Applications
~~~~~~~~~~~~~~~~~~~~
SMURF: MAKEMAP


Copyright
~~~~~~~~~
Copyright (C) 2007-2008,2011 Science and Technology Facilities
Council. Copyright (C) 2005-2008 Univeristy of British Columbia.
Copyright (C) 2005-2007 Particle Physics and Astronomy Research
Council. Copyright (C) 2017 East Asian Observatory. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful,but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


