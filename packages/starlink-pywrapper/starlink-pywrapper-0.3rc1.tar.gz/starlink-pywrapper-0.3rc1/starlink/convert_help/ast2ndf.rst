

AST2NDF
=======


Purpose
~~~~~~~
Converts an Asterix data cube into a simple NDF


Description
~~~~~~~~~~~
This application converts an Asterix data cube into a standard NDF.
See Section 'Notes' (below) for details of the conversion.


Usage
~~~~~


::

    
       ast2ndf in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The name of the input Asterix data cube. The file extension ('.sdf')
should not be included since it is appended automatically by the
application.



OUT = NDF (Write)
`````````````````
The name of the output NDF containing the data cube written by the
application. The file extension ('.sdf') should not be included since
it is appended automatically by the application.



Examples
~~~~~~~~
ast2ndf ast_cube ndf_cube
This example generates data cube NDF ndf_cube (in file ndf_cube.sdf)
from Asterix cube ast_cube (in file ast_cube.sdf).



Notes
~~~~~
This application accepts data in the format used by the Asterix
package (see SUN/98). These data are cubes, with two axes comprising a
regular grid of positions on the sky and the third corresponding to
energy or wavelength. The data are Starlink HDS files which are very
similar in format to a standard NDF. The following points apply.


+ The Asterix QUALITY array is non-standard. There is no QUALITY
component in the output NDF. Instead 'bad' or 'null' values are used
to indicate missing or suspect values.
+ The VARIANCE component is copied if it is present.
+ The non-standard Asterix axis components are replaced with standard
ones.
+ The order of the axes is rearranged.




References
~~~~~~~~~~
D.J. Allan and R.J. Vallance, 1995, in SUN/98: 'ASTERIX -- X-ray Data
Processing System', Starlink.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA:AXCONV


Copyright
~~~~~~~~~
Copyright (C) 1997-1998, 2004 Central Laboratory of the Research
Councils. All Rights Reserved.


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


