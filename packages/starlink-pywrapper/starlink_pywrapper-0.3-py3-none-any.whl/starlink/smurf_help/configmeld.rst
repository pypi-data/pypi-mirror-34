

CONFIGMELD
==========


Purpose
~~~~~~~
Compare two MAKEMAP configs using a visual file comparison tool


Description
~~~~~~~~~~~
This script uses a visual file comparison tool such as "meld", to
display two sets of configuration parameters, highlighting the
differences between them. Each config may be supplied directly, as is
done when running MAKEMAP, or can be read from the History component
of an NDF that was created by MAKEMAP.


Usage
~~~~~


::

    
       configmeld config1 config2 waveband defaults tool
       



ADAM parameters
~~~~~~~~~~~~~~~



CONFIG1 = LITERAL (Read)
````````````````````````
The first configuration. This can be a normal config such as is
supplied for the CONFIG parameter of MAKEMAP, or an NDF created by
MAKEMAP.



CONFIG2 = LITERAL (Read)
````````````````````````
The first configuration. This can be a normal config such as is
supplied for the CONFIG parameter of MAKEMAP, or an NDF created by
MAKEMAP. If a value is supplied for PARAM, then CONFIG2 defaults to
null (!). []



WAVEBAND = LITERAL (Read)
`````````````````````````
This parameter is not used if either CONFIG1 or CONFIG2 is an NDF
created by MAKEMAP. It should be one of "450" or "850". It specifies
which value should be displayed for configuration parameters that have
separate values for 450 and 850 um. If either CONFIG1 or CONFIG2 is an
NDF created by MAKEMAP, then the wavebands to use are determined from
the headers in the NDFs.



DEFAULTS = _LOGICAL (Read)
``````````````````````````
If TRUE, then each supplied configuration (CONFIG1 and CONFIG2) is
extended to include default values are any MAKEMAP parameters that it
does not specify. These defaults are read from file
"$SMURF_DIR/smurf_makemap.def". [TRUE]



PARAM = LITERAL (Read)
``````````````````````
If supplied, then the value used for the specified parameter is
displayed on standard output, and no visual comparison is displayed.
Separate values are displayed for CONFIG1 and (if supplied) CONFIG2.
[!]



TOOL = LITERAL (Read)
`````````````````````
Gives the name of the file comparison tool to use. The named command
should be available on the current PATH. It should take the names of
two files to compare as command line arguments. If null (!) is
supplied, the first available tool in the following list is used:


+ meld: www.meldmerge.org
+ opendiff: developer.apple.com
+ diffmerge: www.sourcegear.com/diffmerge
+ kdiff3: kdiff3.sourceforge.net
+ tkdiff: sourceforge.net/projects/tkdiff
+ diffuse: diffuse.sourceforge.net

[!]



Copyright
~~~~~~~~~
Copyright (C) 2013 Science & Technology Facilities Council. All Rights
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


