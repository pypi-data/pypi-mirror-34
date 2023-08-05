

PROVMOD
=======


Purpose
~~~~~~~
Modifies provenance information for an NDF


Description
~~~~~~~~~~~
This application modifies the provenance information stored in the
PROVENANCE extension of an NDF.


Usage
~~~~~


::

    
       provmod ndf ancestor path
       



ADAM parameters
~~~~~~~~~~~~~~~



ANCESTOR = LITERAL (Read)
`````````````````````````
Specifies the indices of one or more ancestors that are to be
modified. An index of zero refers to the supplied NDF itself. A
positive index refers to one of the NDFs listed in the ANCESTORS table
in the PROVENANCE extension of the NDF. The maximum number of
ancestors is limited to 100 unless "ALL" or "*" is specified. The
supplied parameter value can take any of the following forms.


+ "ALL" or "*" -- All ancestors.
+ "xx,yy,zz" -- A list of ancestor indices.
+ "xx:yy" -- Ancestor indices between xx and yy inclusively. When xx
is omitted, the range begins from 0; when yy is omitted, the range
ends with the maximum value it can take, that is the number of
ancestors described in the PROVENANCE extension.
+ Any reasonable combination of above values separated by commas.
  ["ALL"]





CREATOR = LITERAL (Read)
````````````````````````
If the supplied string includes no equals signs, then it is a new
value for the "CREATOR" string read from each of the ancestors being
modified. If the supplied string includes one or more equals signs,
then it specifies one or more substitutions to be performed on the
"CREATOR" string read from each of the ancestors being modified. See
"Substitution Syntax" below. If null (!) is supplied, the CREATOR item
is left unchanged. [!]



DATE = LITERAL (Read)
`````````````````````
If the supplied string includes no equals signs, then it is a new
value for the "DATE" string read from each of the ancestors being
modified. If the supplied string includes one or more equals signs,
then it specifies one or more substitutions to be performed on the
"DATE" string read from each of the ancestors being modified. See
"Substitution Syntax" below. If null (!) is supplied, the DATE item is
left unchanged. [!]



MORETEXT = GROUP (Read)
```````````````````````
This parameter is accessed only if a single ancestor is being modified
(see parameter ANCESTORS). It gives information to store in the MORE
component of the ancestor (any existing information is first removed).
If a null (!) value is supplied, then existing MORE component is left
unchanged.
The supplied value should be either a comma-separated list of strings
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



NDF = NDF (Update)
``````````````````
The NDF data structure.



PATH = LITERAL (Read)
`````````````````````
If the supplied string includes no equals signs, then it is a new
value for the "PATH" string read from each of the ancestors being
modified. If the supplied string includes one or more equals signs,
then it specifies one or more substitutions to be performed on the
"PATH" string read from each of the ancestors being modified. See
"Substitution Syntax" below. If null (!) is supplied, the PATH item is
left unchanged. [!]



Examples
~~~~~~~~
provmod ff path=/home/dsb/real-file.sdf
This modifies any ancestor within the NDF called ff by setting its
PATH to "/home/dsb/real-file.sdf".
provmod ff ancestor=3 moretext="obsidss=acsis_00026_20080322T055855_1"
This modifies ancestor Number 3 by storing a value of
"acsis_00026_20080322T055855_1" for key "obsidss" within the additonal
information for the ancestor. Any existing additional information is
removed.
provmod ff path='(_x)$=_y'
This modifies any ancestor within the NDF called ff that has a path
ending in "_x" by replacing the final "_x" with "_y".
provmod ff path='(_x)$=_y'
This modifies any ancestor within the NDF called ff that has a path
ending in "_x" by replacing the final "_x" with "_y".
provmod ff path='(.*)_(.*)=$2=$1'
This modifies any ancestor within the NDF called ff that has a path
consisting of two parts separated by an underscore by swapping the
parts. If there is more than one underscore in the ancestor path, then
the final underscore is used (because the initial quantifier ".*" is
greedy).
provmod ff path='(.*?)_(.*)=$2=$1'
This modifies any ancestor within the NDF called ff that has a path
consisting of two parts separated by an underscore by swapping the
parts. If there is more than one underscore in the ancestor path, then
the first underscore is used (because the initial quantifier ".*?" is
not greedy).



Substitution Syntax
~~~~~~~~~~~~~~~~~~~
The syntax for the CREATOR, DATE and PATH parameter values is a
minimal form of regular expression. The following atoms are allowed.
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
A template should use parentheses to enclose the sub-strings that are
to be replaced, and the set of corresponding replacement values should
be appended to the end of the string, separated by "=" characters. The
section of the test string that matches the first parenthesised
section in the template string will be replaced by the first
replacement string. The section of the test string that matches the
second parenthesised section in the template string will be replaced
by the second replacement string, and so on.
The replacement strings can include the tokens "$1", "$2", etc. The
section of the test string that matched the corresponding
parenthesised section in the template is used in place of the token.
See the "Examples" section above for how to use these facilities.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PROVADD, PROVREM, PROVSHOW.


Copyright
~~~~~~~~~
Copyright (C) 2008 Science & Technology Facilities Council. All Rights
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


