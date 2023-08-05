

RAWREWRTSC2WCS
==============


Purpose
~~~~~~~
Fix broken WCS in raw SCUBA-2 file by re-writing it


Description
~~~~~~~~~~~
Some SCUBA-2 files end up with corrupt WCS extensions. It is possible
to recreate the WCS by looking at the JCMTSTATE and FITS header. The
new WCS is written to the file, replacing the original.


ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read)
````````````````
Input files to be fixed.



Notes
~~~~~


+ Supports SCUBA-2 raw data files
+ Currently it will be necessary to remove the corrupt .WCS data using
  KAPPA ERASE before running this command.




Copyright
~~~~~~~~~
Copyright (C) 2011 Science and Technology Facilities Council. All
Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA


