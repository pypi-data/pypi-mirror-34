

NDFCOMPARE
==========


Purpose
~~~~~~~
Compares a pair of NDFs for equivalence


Description
~~~~~~~~~~~
This application compares two supplied NDFs, and sets the Parameter
SIMILAR to "FALSE" if they are significantly different in any way, and
to "TRUE" if they are not significantly different.
If they are not similar, a textual description of the differences is
written to standard output, and to any file specified by Parameter
REPORT.
The two NDFS are compared in the following ways. Each test has an
integer identifier, and the list of tests to be used can be controlled
by Parameters DOTESTS and SKIPTESTS. Tests that are not included by
default are indicated by the test number being in square brackets.
Some tests have parameters that control the exact nature of the test.
These are listed in parentheses at the end of the description test
listed below.
1 - The number of pixel axes are compared. 2 - The pixel bounds are
compared. 3 - The list of co-ordinate systems in the WCS FrameSet are
compared. 4 - The presence or absence of NDF components are compared
(COMP). 5 - The sky positions of a grid of pixels are compared
(ACCPOS). 6 - The data units strings are compared (WHITE). 7 - The
label strings are compared (CASE,WHITE). 8 - The title strings are
compared (CASE,WHITE). 9 - The data types are compared. 10 - The lists
of NDF extensions are compared. 11 - The number of bad DATA values are
compared (NBAD). 12 - The number of bad VARIANCE values are compared
(NBAD). 13 - The pixel DATA values are compared (ACCDAT). 14 - The
pixel VARIANCE values (if any) are compared (ACCVAR). 15 - The pixel
QUALITY values (if any) are compared (NBAD). 16 - The QUALITY names
(if any) are compared. [17] - The lists of root ancestor NDFs that
were used to create each NDF are compared.


Usage
~~~~~


::

    
       ndfcompare in1 in2 [report]
       



ADAM parameters
~~~~~~~~~~~~~~~



ACCDAT = LITERAL (Read)
```````````````````````
The maximum difference allowed between two pixel data values for them
to be considered equivalent. The supplied string should contain a
numerical value followed by a single character (case insensitive) from
the list below indicating how the numerical value is to be used.


+ "V" --- The numerical value is a signal-to-noise value. The absolute
difference in pixel data value is divided by the square root of the
smaller of the two variances associated with the pixels (one from each
input NDF). If the resulting ratio is smaller than the ACCDAT value,
then the two pixel data values are considered to be equivalent. An
error is reported if either NDF does not have a VARIANCE component.
+ "R" --- The numerical value is a relative error. The absolute
difference between the two pixel data values is divided by the
absolute mean of the two data values. If the resulting ratio is
smaller than the ACCDAT value, then the two pixel data values are
considered to be equivalent. To avoid problems with pixels where the
mean is close to zero, a lower limit equal to the RMS of the data
values is placed on the mean value used in the above ratio.
+ "A" --- The numerical value is an absolute error. If the absolute
  difference in pixel data value is smaller than the ACCDAT value, then
  the two pixel data values are considered to be equivalent.

If no character is included in the ACCDAT string, "R" is assumed.
["1E-6 R"]



ACCPOS = _DOUBLE (Read)
```````````````````````
The maximum difference allowed between two axis values for them to be
considered equivalent, in units of pixels on the corresponding pixel
axes. [0.2]



ACCVAR = LITERAL (Read)
```````````````````````
The maximum difference allowed between two pixel variance values for
them to be considered equivalent. The supplied string should contain a
numerical value followed by a single character (case insensitive) from
the list below indicating how the numerical value is to be used.


+ "R" --- The numerical value is a relative error. The absolute
difference in variance value is divided by the absolute mean of the
two variance values. If the resulting ratio is smaller than the ACCVAR
value, then the two pixel variances are considered to be equivalent.
+ "A" --- The numerical value is an absolute error. If the absolute
  difference in variance values is smaller than the ACCVAR value, then
  the two pixel variances are considered to be equivalent.

If no character is included in the ACCVAR string, "R" is assumed.
["1E-6 R"]



CASE = _LOGICAL (Read)
``````````````````````
If TRUE, then string comparisons are case sensitive. Otherwise they
are case insensitive. [TRUE]



COMP = _LITERAL (Read)
``````````````````````
A comma separated list of the NDF components to include in the test.
If a null (!) value is supplied, all NDF components are included. [!]



DOTESTS() = _INTEGER (Read)
```````````````````````````
An initial list of indices for the tests to be performed, or null (!)
if all tests are to be included in the initial list. This initial list
is modified by excluding any tests specified by Parameter SKIPTESTS.
[!]



IN1 = NDF (Read)
````````````````
The first NDF.



IN2 = NDF (Read)
````````````````
The second NDF.



NBAD = LITERAL (Read)
`````````````````````
The maximum difference allowed between the number of bad values in
each NDF. The same value is used for both DATA and VARIANCE arrays. It
is also used as the maximum number of pixel that can have different
QUALITY values. The supplied string should contain a numerical value
followed by a single character (case insensitive) from the list below
indicating how the numerical value is to be used.


+ "R" --- The numerical value is a relative error. The absolute
difference in the number of bad values is divided by the mean number
of bad values in both NDFs (for the QUALITY array, the total number of
pixels in the NDF is used as the denominator in this ratio). If the
resulting ratio is smaller than the NBAD value, then the two NDFs are
considered to be equivalent for the purposes of this test.
+ "A" --- The numerical value is an absolute error. If the absolute
  difference in the number of bad values is smaller than the NBAD value,
  then the two NDFs are considered to be equivalent for the purposes of
  this test.

If no character is included in the NBAD string, "R" is assumed.
["0.001 R"]



REPORT = LITERAL (Read)
```````````````````````
The name of a text file to create in which details of the differences
found between the two NDFs will be store. [!]



SKIPTESTS() = _INTEGER (Read)
`````````````````````````````
A list of indices for tests that are to removed from the initial list
of tests specified by Parameter DOTESTS. If a null (!) value is
supplied, the initial list is left unchanged. [15]



SIMILAR = _LOGICAL (Write)
``````````````````````````
Set to FALSE on exit if any of the used tests indicate that the two
NDFs differ.



WHITE = _LOGICAL (Read)
```````````````````````
If TRUE, then trailing or leading white space is ignored when
comparing strings. [FALSE]



Copyright
~~~~~~~~~
Copyright (C) 2015 East Asian Observatory. All Rights Reserved.


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


