

POLIMP
======


Purpose
~~~~~~~
Copies FITS keyword values into the POLPACK extension


Description
~~~~~~~~~~~
This application should be used to prepare data files prior to
processing them with POLPACK. It records the values of various items
of information required by POLPACK (half-wave plate position, filter,
etc). These values can either be supplied explicitly or can be copied
("imported") from FITS keywords stored in the files. Such keywords
may, for instance, be provided by the instrument/telescope control
systems. The specified values are stored in the POLPACK extensions of
the supplied data files for use
The import is controlled by a "table" which specifies how FITS keyword
values should be used to create the corresponding POLPACK extension
items. Each extension item may be assigned a specified constant value,
the value of a specified FITS keyword, or the value of an arbitrary
function of several FITS keywords.
During the processing of data, POLPACK adds items to the POLPACK
extension to indicate the state of the processing which has been
applied to the data. This routine also allows values to be assigned to
these extra extension items and thus can be used to import partially
processed data. POLIMP can be used in conjunction with POLEXP to allow
data to be moved backwards and forwards between POLPACK and other non-
NDF based packages.


Usage
~~~~~


::

    
       polimp in table
       



ADAM parameters
~~~~~~~~~~~~~~~



ABORT = _LOGICAL (Read)
```````````````````````
If TRUE, then the application aborts immediately if an error occurs
whilst processing any of the input data files. If FALSE, any such
errors are annulled, and the application continues to process any
remaining data files. The run time default is TRUE if only a single
data file is being processed, and FALSE otherwise. []



IN = NDF (Read)
```````````````
A group of data files. This may take the form of a comma separated
list of file names, or any of the other forms described in the help on
"Group Expressions".



NAMELIST = LITERAL (Read)
`````````````````````````
The name of a file to create containing a list of the successfully
processed data files. This file can be used when specifying the input
data files for subsequent applications. No file is created if a null
(!) value is given. [!]



TABLE = LITERAL (Read)
``````````````````````
The name of the file containing the table describing how FITS keyword
values are to be translated into POLPACK extension items. If a null
value (!) is supplied, then the following default table is used which
corresponds to the FITS keywords written by POLEXP:
ANGROT? PPCKANGR ANLANG? PPCKANLA EPS? PPCKEPS FILTER? PPCKFILT IMGID?
PPCKIMID RAY? PPCKRAY STOKES? PPCKSTOK T? PPCKT WPLATE? PPCKWPLT
VERSION? PPCKVERS
See the topic "Table Format" for information on how to create
translation tables.
Note, the ANGROT value is not stored explicitly as a separate item in
the POLPACK extension. Instead, it is used to create a new co-ordinate
Frame (with domain POLANAL) in the NDF's WCS information. [!]



Examples
~~~~~~~~
polimp in='*' table=mytable.dat
This example processes all the data files in the current directory
using the import control table mytable.dat.
polimp in=^names.lis
This example processes the data files listed in the text file
"names.lis" using the default control table appropriate for partially
processed data which has previously been exported using POLEXP.



Notes
~~~~~


+ Any existing values in the POLPACK extension are deleted before
processing the supplied control table.
+ A new Frame is added to the WCS component of each NDF and is given
  the Domain "POLANAL". This Frame is formed by rotating the grid co-
  ordinate Frame so that the first axis is parallel to the analyser
  axis. The angle of rotation is given by the ANGROT value and defaults
  to zero if ANGROT is not specified in the control table. As of POLPACK
  V2.0, the ANGROT value is no longer stored explicitly in the POLPACK
  extension; its value is deduced from the POLANAL Frame in the WCS
  component.




Table Format
~~~~~~~~~~~~
The import control (translation) table is an ordinary text file which
contains instructions on how to assign values to the components of the
POLPACK extension. Constant values specified in the file may be used,
or the values may be derived from the values of FITS keywords stored
in the FITS extension.
In its most simple format each line in a FITS control table contains
the name of a POLPACK extension item, followed by a constant value or
FITS keyword. This causes the value of the specified FITS keyword or
constant, to be assigned to the specified extension item. Some
examples:
WPLATE HWP
This copies the value of the FITS keyword HWP from the FITS extension
to the WPLATE component in the POLPACK extension.
WPLATE 45.0
This assigns the value 45.0 to the WPLATE component of the POLPACK
extension.
IMGID "M51_PLATEB"
This assigns the value M51_PLATE to the IMGID component of the POLPACK
extension. Note, textual constants must be enclosed within quotes.
In addition to using the values of FITS keywords directly, it is also
possible to use arbitrary functions of one or more keywords. To do
this, each keyword used in the function must first be "declared" so
that a data type may be associated with it. This is done by including
lines with the following form in the control table prior to the
function reference:
Data-type FITS-keyword
Here "Data-type" must be one of _INTEGER, _REAL, _DOUBLE, _WORD,
_BYTE, _CHAR. So for instance if you wanted to assign a value to the
WPLATE extension item, the orientation of the half-wave plate in
degrees, from the FITS keyword HWP which gives the required value in
radians, you could use this sequence of commands:
_REAL HWP WPLATE 57.29578*HWP
The function may use any of the usual Fortran operators; +, -, *, /,
** and built-in functions (SIN, COS, TAN, LOG, etc). See SUN/61
(appendix A) for complete details.
Characters strings cannot be manipulated by these functions so two
special formats for translating their values are provided. The first
form allows for the concatenation of keywords and the second the
translation from a known word to another (which is usually one of the
POLPACK special names). The concatenation form looks like:
IMGID OBSNUM//IDATE
Which results in the IMGID extension item being set to the
concatenation of the values of the FITS keywords OBSNUM and IDATE (you
can concatentate more than two values). Note, conversion of numeric
values to character strings occurs automatically.
In the second special form, the name of the destination extension item
is given as usual followed by a FITS-keyword which supplies the string
to be translated. This is then followed by statements which translate
an "input" string into an "output" string. So for instance if you were
doing circular polarimetry, and wanted to translate quarter waveplate
positions to the equivalent strings recognised by POLPACK you might
use something like:
WPLATE POLPLATE 48.0=0.0 - 138.0=45.0
This compares the value of the FITS keyword POLPLATE with the strings
on the left hand sides of the equals signs ("48.0" and "138.0"). If a
match is found, it assigns the value from the right hand side of the
equals sign ("0.0" or "45.0") to the WPLATE component in the POLPACK
extension. An error is reported if no match is found. The "-" sign at
the end of the first line indicates that the list continues on the
next line. If the strings being compared both represent numerical
values, the comparison will be performed between their numerical
values. This means, for instance, that all the following strings will
be considered equal "45.0", "45", "45D0", "+45.0E0". If either of the
strings are not numerical, then the comparison is performed between
their textual values (case insensitive).
Here is a more complicated example:
FILTER NAME //" - "//MYFILT "U band"=U "V band"=V "B band"=B
This concatenates the value of the FITS keyword NAME, the string " -
", and the value of the sub-expression:
MYFILT "U band"=U "V band"=V "B band"=B
and assigns the resulting string to the FILTER extension item. Note,
parentheses may be used to indicate a different order of precedence.
For instance, this example:
FILTER (NAME //" - "//MYFILT) "U band"=U "V band"=V "B band"=B
performs the checks for "U band", etc, on the total concatenated
string, rather than on the value of keyword MYFITS. The two strings
included in a replacement specification may themselves be enclosed
within parentheses in which case they may be any complex character
expression involing literal strings, concatentation operators and
nested replacement specifications.
If a control table contains more than one line for an extension item,
then each line is processed in turn, replacing any value established
by earlier lines. Thus the final value of the extension item will be
given by the last line in the table refering to the extension item.
If it is not known in advance if the FITS extension will contain the
keyword values needed to assign a value to a particular POLPACK
extension item, then a question mark may be appended to the name of
the POLPACK extension item. If the required FITS keyword values cannot
be found, then the error messages which would normally be issued are
suppressed, and any remaining lines in the control table are processed
as normal. If no value has been assigned to the item when the entire
table has been processed, then the item will be set to its default
value if it has one, or left undefined otherwise (see below). For
instance:
RAY? OLDRAY RAY? PPCKRAY
causes the POLPACK extension item RAY to be assigned the value of the
FITS keyword PPCKRAY if the keyword has a value in the FITS extension.
If not, then the FITS keyword OLDRAY is used instead. If this does not
exist either, then RAY is left undefined.
Logical data types are restricted to a single keyword whose value must
be "YES", "TRUE", "T", "Y" for TRUE or "NO", "FALSE", "N", "F".
Fields in the table may be separated by commas if desired, instead of
spaces. Comments may be placed anywhere and should start with the
characters "#" or "!". Continuation onto a new line is indicated by
use of "-".


Copyright
~~~~~~~~~
Copyright (C) 1998 Central Laboratory of the Research Councils


