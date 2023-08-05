

NUMB
====


Purpose
~~~~~~~
Counts the number of elements of an NDF with values or absolute values
above or below a threshold


Description
~~~~~~~~~~~
This routine counts and reports the number of elements of an array
within an input NDF structure that have a value or absolute value
greater or less than a specified threshold. This statistic is also
shown as a percentage of the total number of array elements.


Usage
~~~~~


::

    
       numb in value [comp]
       



ADAM parameters
~~~~~~~~~~~~~~~



ABS = _LOGICAL (Read)
`````````````````````
If ABS is TRUE, the criterion is a comparison of the absolute value
with the threshold; if FALSE, the criterion is a comparison of the
actual value with the threshold. The current value is the suggested
default. [FALSE]



ABOVE = _LOGICAL (Read)
```````````````````````
If ABOVE is TRUE the criterion tests whether values are greater than
the threshold; if FALSE the criterion tests whether values are less
than the threshold. The current value of ABOVE is the suggested
default. [TRUE]



COMP = LITERAL (Read)
`````````````````````
The components whose flagged values are to be substituted. It may be
"Data", "Error", "Variance", or "Quality". If "Quality" is specified,
then the quality values are treated as numerical values in the range 0
to 255. ["Data"]



IN = NDF (Read)
```````````````
Input NDF structure containing the array to be tested.



NUMBER = _INTEGER (Write)
`````````````````````````
The number of elements that satisfied the criterion.



VALUE = _DOUBLE (Read)
``````````````````````
Threshold against which the values of the array elements will be
tested. It must lie in within the minimum and maximum values of the
data type of the array being processed, unless ABS = TRUE or the
component is the variance or quality array, in which case the minimum
is zero. The suggested default is the current value.



Examples
~~~~~~~~
numb image 100
This counts the number of elements in the data array of the NDF called
image that exceed 100.
numb spectrum 100 noabove
This counts the number of elements in the data array of the NDF called
spectrum that are less than 100.
numb cube 100 abs
This counts the number of elements in the data array of the NDF called
cube whose absolute values exceed 100.
numb image -100 number=(count)
This counts the number of elements in the data array of the NDF called
image that exceed -100 and write the number to ICL variable COUNT.
numb image 200 v
This counts the number of elements in the variance array of the NDF
called image that exceed 200.



Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995, 2004 Central Laboratory of the Research Councils. Copyright
(C) 2012 Science & Technology Facilities Council. All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the DATA, QUALITY, TITLE, and
VARIANCE components of an NDF data structure.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ Any number of NDF dimensions is supported.




