

PROVADD
=======


Purpose
~~~~~~~
Stores provenance information in an NDF


Description
~~~~~~~~~~~
This application modifies the provenance information stored in an NDF.
It records a second specified NDF as a direct parent of the first NDF.
If an NDF has more than one direct parent then this application should
be run multiple times, once for each parent.


Usage
~~~~~


::

    
       provadd ndf parent creator isroot moretext
       



ADAM parameters
~~~~~~~~~~~~~~~



CREATOR = LITERAL (Read)
````````````````````````
A text identifier for the software that created the main NDF (usually
the name of the calling application). The format of the identifier is
arbitrary, but the form "PACKAGE:COMMAND" is recommended. If a null
(!) value is supplied, no creator information is stored. [!]



ISROOT = _LOGICAL (Read)
````````````````````````
If TRUE, then the NDF given by parameter "PARENT" will be treated as a
root NDF. That is, any provenance information within PARENT describing
its own parents is ignored. If FALSE, then any provenance information
within PARENT is copied into the main NDF. PARENT is then only a root
NDF only if it contains no provenance information. [FALSE]



MORETEXT = GROUP (Read)
```````````````````````
A group of "keyword=value" strings that give additional information
about the parent NDF, and how it was used in the creation of the main
NDF. If supplied, this information is stored with the provenance in
the main NDF.
The supplied value should be either a comma-separated list of strings,
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated list of strings. Each string is
either a "keyword=value" setting, or the name of a text file preceded
by an up-arrow character "^". Such text files should contain further
comma-separated lists which will be read and interpreted in the same
manner (any blank lines or lines beginning with "#" are ignored).
Within a text file, newlines can be used as delimiters as well as
commas.
Each individual setting should be of the form:
<keyword>=<value>
where <keyword> is either a simple name, or a dot-delimited hierarchy
of names (e.g. "camera.settings.exp=1.0"). The <value> string should
not contain any commas. [!]



NDF = NDF (Read and Write)
``````````````````````````
The NDF which is to be modified.



PARENT = NDF (Read)
```````````````````
An NDF that is to be recorded as a direct parent of the NDF given by
parameter "NDF".



Examples
~~~~~~~~
provadd m51_ff ff
Records the fact that NDF "ff" was used in the creation of NDF
"m51_ff".



Notes
~~~~~
Provenance information is stored in an NDF extension called
PROVENANCE, and is propagated automatically by all KAPPA applications.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PROVMOD, PROVSHOW, HISCOM.


Copyright
~~~~~~~~~
Copyright (C) 2008-2014 Science & Technology Facilities Council. All
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


