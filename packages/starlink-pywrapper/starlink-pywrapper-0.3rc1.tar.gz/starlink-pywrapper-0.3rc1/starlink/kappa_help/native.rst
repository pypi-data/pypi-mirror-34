

NATIVE
======


Purpose
~~~~~~~
Converts an HDS object to native machine data representation


Description
~~~~~~~~~~~
This application converts an HDS object (or structure) so that all
primitive data values within it are represented using the appropriate
native data representation for the machine in use (this includes the
appropriate number format and byte ordering). This may typically be
required after moving HDS files from another machine which uses a
different number format and/or byte order, and will minimise the
subsequent access time on the new machine. Conversion is performed by
modifying the data in situ. No separate output file is produced.
This application can also be used to replace any IEEE floating point
NaN or Inf values in an HDS object with the appropriate Starlink bad
value. This conversion is performed even if the data values within the
object are already represented using the appropriate native data
representation for the machine in use.


Usage
~~~~~


::

    
       native object
       



ADAM parameters
~~~~~~~~~~~~~~~



OBJECT = UNIVERSAL (Read and Write)
```````````````````````````````````
The HDS structure to be converted; either an entire container file or
a particular object or structure within the file may be specified. If
a structure is given, all components (and sub-components, etc.) within
it will also be converted.



Examples
~~~~~~~~
native myfile
Converts all the primitive data in the HDS container file myfile to be
held using the appropriate native machine representation for faster
subsequent access.
native yourfile.data_array
Converts just the DATA_ARRAY component (and its contents, if a
structure) in the container file yourfile to the appropriate native
machine data representation. Other file contents remain unchanged.



Copyright
~~~~~~~~~
Copyright (C) 2009 Science and Technology Facilities Council.
Copyright (C) 1992 Science & Engineering Research Council. Copyright
(C) 1995, 1998 Central Laboratory of the Research Councils. All Rights
Reserved.


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


