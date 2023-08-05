

PROVREM
=======


Purpose
~~~~~~~
Removes selected provenance information from an NDF


Description
~~~~~~~~~~~
This application removes selected ancestors, either by hiding them, or
deleting them from the provenance information stored in a given NDF.
The `generation gap' caused by removing an ancestor is bridged by
assigning all the direct parents of the removed ancestor to each of
the direct children of the ancestor.
The ancestors to be removed can be specified either by giving their
indices (Parameter ANCESTOR), or by comparing each ancestor with a
supplied pattern matching template (Parameter PATTERN).
If an ancestor is hidden rather than deleted (see Parameter HIDE), the
ancestor is retained within the NDF, but a flag is set telling later
applications to ignore the ancestor (exactly how the flag is used will
depend on the particular application).


Usage
~~~~~


::

    
       provrem ndf pattern item
       



ADAM parameters
~~~~~~~~~~~~~~~



ANCESTOR = LITERAL (Read)
`````````````````````````
Specifies the indices of one or more ancestors that are to be removed.
If a null (!) value is supplied, the ancestors to be removed are
instead determined using the PATTERN parameter. Each supplied index
must be positive and refers to one of the NDFs listed in the ANCESTORS
table in the PROVENANCE extension of the NDF (including any hidden
ancestors). Note, if ancestor indices are determined using the
PROVSHOW command, then PROVSHOW should be run with the HIDE parameter
set to FALSE - otherwise incorrect ancestor indices may be determined,
resulting in the wrong ancestors being removed by PROVREM.
The maximum number of ancestors that can be removed is limited to 100
unless "ALL", "*" or "!" is specified. The supplied parameter value
can take any of the following forms.


+ "ALL" or "*" -- All ancestors.
+ "xx,yy,zz" -- A list of ancestor indices.
+ "xx:yy" -- Ancestor indices between xx and yy inclusively. When xx
is omitted, the range begins from 0; when yy is omitted, the range
ends with the maximum value it can take, that is the number of
ancestors described in the PROVENANCE extension.
+ Any reasonable combination of above values separated by commas. [!]





HIDE = _LOGICAL (Read)
``````````````````````
If TRUE, then the ancestors are not deleted, but instead have a flag
set indicating that they have been hidden. All information about
hidden ancestors is retained unchanged, and can be viewed using
PROVSHOW if the HIDE parameter is set FALSE when running PROVSHOW.
[FALSE]



ITEM = LITERAL (Read)
`````````````````````
Specifies the item of provenance information that is checked against
the pattern matching template specified for parameter PATTERN. It can
be "PATH", "CREATOR" or "DATE". ["PATH"]



NDF = NDF (Update)
``````````````````
The NDF data structure.



PATTERN = LITERAL (Read)
````````````````````````
Specifies a pattern matching template using the syntax described below
in "Pattern Matching Syntax". Each ancestor listed in the PROVENANCE
extension of the NDF is compared with this template, and each ancestor
that matches is removed. The item of provenance information to be
compared to the pattern is specified by Parameter ITEM.



REMOVE = _LOGICAL (Read)
````````````````````````
If TRUE, then the ancestors specified by Parameter PATTERN or
ANCESTORS are removed. Otherwise, these ancestors are retained and all
other ancestors are removed. [TRUE]



Examples
~~~~~~~~
provrem ff ancestor=1
This removes the first ancestor from the NDF called ff.
provrem ff ancestor=all
This erases all provenance information.
provrem ff pattern='_xb$|_yb$' hide=yes
This hides, but does not permanently delete, all ancestors that have
paths that end with "_xb" or "_yb". Note, provenance paths do not
include a trailing ".sdf" string.
provrem ff pattern='_ave'
This removes all ancestors that have paths that contain the string
"_ave" anywhere.
provrem ff pattern='_ave' remove=no
This removes all ancestors that have paths that do not contain the
string "_ave" anywhere.
provrem ff pattern='_d[^/]*$'
This removes all ancestors that have file base-names that begin with
"_d" . The pattern matches "_d" followed by any number of characters
that are not "/", followed by the end of the string.
provrem ff pattern='^m51|^m31'
This removes all ancestors that have paths that begin with "m51" or
"m31".



Pattern Matching Syntax
~~~~~~~~~~~~~~~~~~~~~~~
The syntax for the PATTERN parameter value is a minimal form of
regular expression. The following atoms are allowed.
"[chars]" -- Matches any of the characters within the brackets.
"[^chars]" -- Matches any character that is not within the brackets
(ignoring the initial "^" character). "." -- Matches any single
character. "\d" -- Matches a single digit. "\D" -- Matches anything
but a single digit. "\w" -- Matches any alphanumeric character, and
"_". "\W" -- Matches anything but alphanumeric characters, and "_".
"\s" -- Matches white space. "\S" -- Matches anything but white space.
Any other character that has no special significance within a regular
expression matches itself. Characters that have special significance
can be matched by preceeding them with a backslash (\) in which case
their special significance is ignored (note, this does not apply to
the characters in the set dDsSwW).
Note, minus signs ("-") within brackets have no special significance,
so ranges of characters must be specified explicitly.
The following quantifiers are allowed.
"*" -- Matches zero or more of the preceeding atom, choosing the
largest possible number that gives a match. "*?"-- Matches zero or
more of the preceeding atom, choosing the smallest possible number
that gives a match. "+" -- Matches one or more of the preceeding atom,
choosing the largest possible number that gives a match. "+?"--
Matches one or more of the preceeding atom, choosing the smallest
possible number that gives a match. "?" -- Matches zero or one of the
preceeding atom. "{n}" -- Matches exactly "n" occurrences of the
preceeding atom.
The following constraints are allowed.
"^" -- Matches the start of the test string. "$" -- Matches the end of
the test string.
Multiple templates can be concatenated, using the "|" character to
separate them. The test string is compared against each one in turn
until a match is found.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PROVADD, PROVMOD, PROVSHOW.


Copyright
~~~~~~~~~
Copyright (C) 2008-2009 Science & Technology Facilities Council. All
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


