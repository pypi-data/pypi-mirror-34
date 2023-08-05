

CONFIGECHO
==========


Purpose
~~~~~~~
Displays one or more configuration parameters


Description
~~~~~~~~~~~
This application displays the name and value of one or all
configuration parameters, specified using Parameters CONFIG or NDF. If
a single parameter is displayed, its value is also written to an
output parameter. If the parameter value is not specified by the
CONFIG, NDF or DEFAULTS parameter, then the value supplied for DEFVAL
is displayed.
If an input NDF is supplied then configuration parameters are read
from its history (see Parameters NDF and APPLICATION).
If values are supplied for both CONFIG and NDF, then the differences
between the two sets of configuration parameters are displayed (see
Parameter NDF).


Usage
~~~~~


::

    
       configecho name config [defaults] [select] [defval]
       



ADAM parameters
~~~~~~~~~~~~~~~



APPLICATION = LITERAL (Read)
````````````````````````````
When reading configuration parameters from the history of an NDF, this
parameter specifies the name of the application to find in the
history. There must be a history component corresponding to the value
of this parameter, and it must include a CONFIG group. [current value]



CONFIG = GROUP (Read)
`````````````````````
Specifies values for the configuration parameters. If the string "def"
(case-insensitive) or a null (!) value is supplied, the configuration
parameters are obtained using Parameter NDF. If a null value is also
supplied for NDF, a set of default configuration parameter values will
be used, as specified by Parameter DEFAULTS.
The supplied value should be either a comma-separated list of strings
or the name of a text file preceded by an up-arrow character "^",
containing one or more comma-separated lists of strings. Each string
is either a "keyword=value" setting, or the name of a text file
preceded by an up-arrow character "^". Such text files should contain
further comma-separated lists which will be read and interpreted in
the same manner (any blank lines or lines beginning with "#" are
ignored). Within a text file, newlines can be used as delimiters, as
well as commas. Settings are applied in the order in which they occur
within the list, with later settings overriding any earlier settings
given for the same keyword.
Each individual setting should be of the form "<keyword>=<value>". If
a non-null value is supplied for Parameter DEFAULTS, an error will be
reported if CONFIG includes values for any parameters that are not
included in DEFAULTS.



DEFAULTS = LITERAL (Read)
`````````````````````````
The path to a file containing the default value for every allowed
configuration parameter. If null (!) is supplied, no defaults will be
supplied for parameters that are not specified by CONFIG, and no tests
will be performed on the validity of paramter names supplied by
CONFIG. [!]



DEFVAL = LITERAL (Read)
```````````````````````
The value to return if no value can be obtained for the named
parameter, or if the value is "<undef>". [<***>]



LOGFILE = LITERAL (Read)
````````````````````````
The name of a text file in which to store the displayed configuration
parameters. [!]



NAME = LITERAL (Read)
`````````````````````
The name of the configuration parameter to display. If set to null
(!), then all parameters defined in the configuration are displayed.



NDF = NDF (Read)
````````````````
An NDF file containing history entries which include configuration
parameters. If not null (!) the history of the NDF will be searched
for a component corresponding to the Parameter APPLICATION. The
Parameter CONFIG is then optional, but if it too is not null (!) then
the output will show the differences between the configuration stored
in the NDF history and the given configuration: new parameters and
those different from the reference configuration (given by Parameter
CONFIG) are prefixed with "+" and those which are the same as the
reference configuration are prefixed with "-". [!]



SELECT = GROUP (Read)
`````````````````````
A group that specifies any alternative prefixes that can be included
at the start of any parameter name. For instance, if this group
contains the two entries "450=1" and "850=0", then either CONFIG or
DEFAULTS can specify two values for any single parameter -- one for
the parameter prefixed by "450." and another for the parameter
prefixed by "850.". Thus, for instance, if DEFAULTS defines a
parameter called "filter", it could include "450.filter=300" and
"850.filter=600". The CONFIG parameter could then either set the
filter parameter for a specific prefix (as in "450.filter=234"); or it
could leave the prefix unspecified, in which case the prefix used is
the first one with a non-zero value in SELECT (450 in the case of this
example - 850 has a value zero in SELECT). Thus the names of the items
in SELECT define the set of allowed alternative prefixes, and the
values indicate which one of these alternatives is to be used (the
first one with non-zero value). [!]



SORT = _LOGICAL (Read)
``````````````````````
If TRUE then sort the listed parameters in to alphabetical order.
Otherwise, retain the order they have in the supplied configuration.
Only used if a null (!) value is supplied for Parameter NAME. [FALSE]



VALUE = LITERAL (Write)
```````````````````````
The value of the configuration parameter, or "<***>" if the parameter
has no value in CONFIG and DEFAULTS.



Examples
~~~~~~~~
configecho m81 ^myconf
Report the value of configuration parameter "m81" defined within the
file "myconf". If the file does not contain a value for "m81", then
"<***>" is displayed.
configecho type ^myconf select="m57=0,m31=1,m103=0"
Report the value of configuration parameter "type" defined within the
file "myconf". If the file does not contain a value for "type", then
the value of "m31.type" will be reported instead. If neither is
present, then "<***>" is displayed.
configecho flt.filt_edge_largescale \
config=^/star/share/smurf/dimmconfig.lis \
defaults=/star/bin/smurf/smurf_makemap.def \ select="450=1,850=0"
Report the value of configuration parameter "flt.filt_edge_largescale"
defined within the file "/star/share/smurf/dimmconfig.lis", using
defaults from the file "/star/bin/smurf/smurf_makemap.def". If
dimmconfig.lis does not contain a value for "flt.filt_edge_largescale"
then it is searched for "450.flt.filt_edge_largescale" instead. An
error is reported if dimmconfig.lis contains values for any items that
are not defined in smurf_makemap.def.
configecho ndf=omc1 config=^/star/share/smurf/dimmconfig.lis \
defaults=/star/bin/smurf/smurf_makemap.def \ application=makemap
name=! sort select="450=0,850=1" Show how the configuration used to
generate the 850um map of OMC1 differs from the basic dimmconfig.lis
file.



Copyright
~~~~~~~~~
Copyright (C) 2012-3 Science & Technology Facilities Council. All
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


