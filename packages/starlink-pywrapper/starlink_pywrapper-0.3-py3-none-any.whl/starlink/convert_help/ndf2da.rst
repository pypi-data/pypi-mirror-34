

NDF2DA
======


Purpose
~~~~~~~
Converts an NDF to a direct-access unformatted file


Description
~~~~~~~~~~~
This application converts an NDF to a direct-access unformatted file,
which is equivalent to fixed-length records, or a data stream suitable
for reading by C routines. Only one of the array components may be
copied to the output file.


Usage
~~~~~


::

    
       ndf2da in out [comp] [noperec]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The NDF component to be copied. It may be "Data", "Quality" or
"Variance". ["Data"]



IN = NDF (Read)
```````````````
Input NDF data structure. The suggested default is the current NDF if
one exists, otherwise it is the current value.



NOPEREC = _INTEGER (Read)
`````````````````````````
The number of data values per record of the output file. It must be
positive. The suggested default is the current value. [The first
dimension of the NDF]



OUT = FILENAME (Write)
``````````````````````
Name of the output direct-access unformatted file.



Examples
~~~~~~~~
ndf2da cluster cluster.dat
This copies the data array of the NDF called cluster to a direct-
access unformatted file called cluster.dat. The number of data values
per record is equal to the size of the first dimension of the NDF.
ndf2da cluster cluster.dat v
This copies the variance of the NDF called cluster to a direct-access
unformatted file called cluster.dat. The number of variance values per
record is equal to the size of the first dimension of the NDF.
ndf2da cluster cluster.dat noperec=12
This copies the data array of the NDF called cluster to a direct-
access unformatted file called {\tt cluster.dat}. There are twelve
data values per record in cluster.dat.



Notes
~~~~~
The details of the conversion are as follows:

+ the NDF array as selected by COMP is written to the unformatted file
in records.
+ all other NDF components are lost.




Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: DA2NDF.


Copyright
~~~~~~~~~
Copyright (C) 1996, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2011-2012 Science & Technology Facilities Council. All
Rights Reserved.


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


