

FITSIMP
=======


Purpose
~~~~~~~
Imports FITS information into an NDF extension


Description
~~~~~~~~~~~
This application extracts the values of FITS keywords from a FITS
extension in an NDF and uses them to construct another NDF extension.
The list of new extension components required, their data types and
the names of the FITS keywords from which to derive their values are
specified in a "keyword translation table" held in a separate text
file.


Usage
~~~~~


::

    
       fitsimp ndf table xname xtype
       



ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read and Write)
``````````````````````````
The NDF in which the new extension is to be created.



TABLE = FILENAME (Read)
```````````````````````
The text file containing the keyword translation table. The format of
this file is described under "Table Format".



XNAME = LITERAL (Read)
``````````````````````
The name of the NDF extension which is to receive the values read from
the FITS extension. If this extension does not already exist, then it
will be created. Otherwise, it should be a scalar structure extension
within which new components may be created (existing components of the
same name will be over-written). Extension names may contain up to 15
alpha-numeric characters, beginning with an alphabetic character.



XTYPE = LITERAL (Read)
``````````````````````
The HDS data type of the output extension. This value will only be
required if the extension does not initially exist and must be
created. New extensions will be created as scalar structures.



Examples
~~~~~~~~
fitsimp datafile fitstable ccdinfo ccd_ext
Creates a new extension called CCDINFO (with a data type of CCD_EXT)
in the NDF structure called datafile. Keyword values are read from the
NDF's FITS extension and written into the new extension as separate
components under control of a keyword translation table held in the
file fitstable.
fitsimp ndf=n1429 table=std_table xname=std_extn
FITS keyword values are read from the FITS extension in the NDF
structure n1429 and written into the pre-existing extension STD_EXTN
under control of the translation table std_table. Components which
already exist within the extension may be over-written by this
process.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSHEAD, FITSLIST, FITSDIN, FITSIN; CONVERT: FITS2NDF; Figaro:
RDFITS.


Table Format
~~~~~~~~~~~~
The keyword translation table should be held in a text file, with one
extension component specified per line. Each line should contain 3
fields, separated by spaces and/or tabs, as follows.


+ Field 1: The name of the component in the output extension for which
a value is to be obtained.
+ Field 2: The data type of the output component, to which the keyword
value will be converted (one of _INTEGER, _REAL, _DOUBLE, _LOGICAL or
_CHAR).
+ Field 3: The name of the FITS keyword from which the value is to be
  obtained. Hierarchical keywords are permissible; the format is
  concatenated keywords joined with full stops and no spaces, e.g.
  HIERARCH.ESO.NTT.HUMIDITY, ING.DETHEAD.

Comments may appear at any point in the table and should begin with an
exclamation mark. The remainder of the line will then be ignored.


Timing
~~~~~~
Approximately proportional to the number of FITS keywords to be
translated.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 2004 Central Laboratory of the Research Councils. All Rights
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


