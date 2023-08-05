

NDFECHO
=======


Purpose
~~~~~~~
Displays a group of NDF names


Description
~~~~~~~~~~~
This application lists the names of the supplied NDFs to the screen,
optionally filtering them using a regular expression. Its primary use
is within scripts that need to process groups of NDFs. Instead of the
full name, a required component of the name may be displayed instead
(see Parameter SHOW).
Two modes are available.


+ If the NDFs are specified via the NDF parameter, then the NDFs must
exist and be accessible (an error is reported otherwise). The NDF
names obtained can then be modified by supplying a suitable GRP
modification expression such as "*_A" for Parameter MOD.
+ To list NDFs that may not exist, supply a null (!) value for
  Parameter NDF and the main group expression to Parameter MOD.




Usage
~~~~~


::

    
       ndfecho ndf [mod] [first] [last] [show]
       



ADAM parameters
~~~~~~~~~~~~~~~



ABSPATH = _LOGICAL (Read)
`````````````````````````
If TRUE, any relative NDF paths are converted to absolute, using the
current working directory. [FALSE]



EXISTS = _LOGICAL (Read)
````````````````````````
If TRUE, then only display paths for NDFs specified by parameter MOD
that actually exist and are accessible. [FALSE]



FIRST = _INTEGER (Read)
```````````````````````
The index of the first NDF to be tested. A null (!) value causes the
first NDF to be used (Index 1). [!]



LAST = _INTEGER (Read)
``````````````````````
The index of the last NDF to be tested. If a non-null value is
supplied for FIRST, then the run-time default for LAST is equal to the
supplied FIRST value (so that only a single NDF will be tested). If a
null value is supplied for FIRST, then the run-time default for LAST
is the last NDF in the supplied group. []



LOGFILE = FILENAME (Write)
``````````````````````````
The name of a text file in which to store the listed NDF names. If a
null (!) value is supplied, no log file is created. [!]



MOD = LITERAL (Read)
````````````````````
An optional GRP modification expression that will be used to modify
any names obtained via the Parameter NDF. For instance, if MOD is
"*_A" then the supplied NDF names will be modified by appending "_A"
to them. No modification occurs if a null (!) value is supplied.
If a null value is supplied for Parameter NDF then the value supplied
for Parameter MOD should not include an asterisk, since there are no
names to be modified. Instead, the MOD value should specify an
explicit group of NDF names that do not need to exist.
The list can be filtered to remove any NDFs that do not exist (see
parameter EXISTS). [!]



NDF = NDF (Read)
````````````````
A group of existing NDFs, or null (!). This should be given as a
comma-separated list, in which each list element can be one of the
following options:


+ An NDF name, optionally containing wild-cards and/or regular
expressions ("*", "?", "[a-z]" etc.).
+ The name of a text file, preceded by an up-arrow character "^". Each
  line in the text file should contain a comma-separated list of
  elements, each of which can in turn be an NDF name (with optional
  wild-cards, etc.), or another file specification (preceded by an up-
  arrow). Comments can be included in the file by commencing lines with
  a hash character "#".

If the value supplied for this parameter ends with a hyphen, then you
are re-prompted for further input until a value is given which does
not end with a hyphen. All the NDFs given in this way are concatenated
into a single group.
If a null (!) value is supplied, then the displayed list of NDFs is
determined by the value supplied for the MOD parameter.



NMATCH = _INTEGER (Write)
`````````````````````````
An output parameter to which is written the number of NDFs between
FIRST and LAST that match the pattern supplied by Parameter PATTERN.



PATTERN = LITERAL (Read)
````````````````````````
Specifies a pattern matching template using the syntax described below
in "Pattern Matching Syntax". Each NDF is displayed only if a match is
found between this pattern and the item specified by Parameter SHOW. A
null (!) value causes all NDFs to be displayed. [!]



SHOW = LITERAL (Read)
`````````````````````
Specifies the information to be displayed about each NDF. The options
are as follows.


+ "Base" -- The base file name.
+ "Dir" -- The directory path (if any).
+ "Fspec" -- The directory, base name and file type concatenated to
form a full file specification.
+ "Ftype" -- The file type (usually ".sdf" but may not be if any
foreign NDFs are supplied).
+ "HDSpath" -- The HDS path within the container file (if any).
+ "Path" -- The full name of the NDF as supplied by the user.
+ "Slice" -- The NDF slice specification (if any).

Items that do not match the pattern specified by Parameter PATTERN are
not displayed. ["Path"]



SIZE = _INTEGER (Write)
```````````````````````
An output parameter to which is written the total number of NDFs in
the specified group.



VALUE = LITERAL (Write)
```````````````````````
An output parameter to which is written information about the first
NDF that matches the pattern specified by Parameter PATTERN. The
information to write is specified by the SHOW parameter.



Examples
~~~~~~~~
ndfecho mycont
Report the full path of all the NDFs within the HDS container file
"mycont.sdf". The NDFs must all exist.
ndfecho ^files.lis first=4 show=base
This reports the file base name for just the fourth NDF in the list
specified within the text file "files.lis". The NDFs must all exist.
ndfecho ^files.lis *_a logfile=log.lis
This reports the names of the NDFs listed in text file files.lis, but
appending "_a" to the end of each name. The NDFs must all exist. The
listed NDF names are written to a new text file called "log.lis".
ndfecho in=! mod={^base}|_a|_b|
This reports the names of the NDFs listed in text file "base", but
replacing "_a" with "_b" in their names. The NDFs need not exist since
they are completely specified by Parameter MOD and not by Parameter
NDF.



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
can be matched by preceding them with a backslash (\) in which case
their special significance is ignored (note, this does not apply to
the characters in the set dDsSwW).
Note, minus signs ("-") within brackets have no special significance,
so ranges of characters must be specified explicitly.
The following quantifiers are allowed.
"*" -- Matches zero or more of the preceding atom, choosing the
largest possible number that gives a match. "*?" -- Matches zero or
more of the preceding atom, choosing the smallest possible number that
gives a match. "+" -- Matches one or more of the preceding atom,
choosing the largest possible number that gives a match. "+?" --
Matches one or more of the preceding atom, choosing the smallest
possible number that gives a match. "?" -- Matches zero or one of the
preceding atom. "{n}" -- Matches exactly "n" occurrences of the
preceding atom.
The following constraints are allowed.
"^" -- Matches the start of the test string. "$" -- Matches the end of
the test string.
Multiple templates can be concatenated, using the "|" character to
separate them. The test string is compared against each one in turn
until a match is found.


Copyright
~~~~~~~~~
Copyright (C) 2012 Science & Technology Facilities Council. All Rights
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


