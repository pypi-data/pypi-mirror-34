

KSTEST
======


Purpose
~~~~~~~
Compares data sets using the Kolmogorov-Smirnov test


Description
~~~~~~~~~~~
This routine reads in a data array and performs a two sided
Kolmogorov-Smirnov test on the vectorised data. It does this in two
ways:
1) If only one dataset is to be tested the data array is divided into
subsamples. First it compares subsample 1 with subsample 2, if they
are thought to be from the same sample they are concatenated. This
enlarged sample is then compared with subsample 3 etc., concatenating
if consistent, until no more subsamples remain.
2) If more than one dataset is specified, the datasets are compared to
the reference dataset in turn. If the probability the two are from the
same sample is greater than the specified confidence level, the
datasets are concatenated, and the next sample is tested against this
enlarged reference dataset.
The probability and maximum separation of the cumulative distribution
function is displayed for each comparison (at the normal reporting
level). The mean value of the consistent data and its error are also
reported. In all cases the consistent data can be output to a new
dataset. The statistics and probabilities are written to results
parameters.


Usage
~~~~~


::

    
       kstest in out [limit]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMP = LITERAL (Read)
`````````````````````
The name of the NDF array component to be tested for consistency:
"Data", "Error", "Quality" or "Variance" (where "Error" is the
alternative to "Variance" and causes the square root of the variance
values to be taken before performing the comparisons). If "Quality" is
specified, then the quality values are treated as numerical values (in
the range 0 to 255). ["Data"]



DIST() = _REAL (Write)
``````````````````````
Maximum separation found in the cumulative distributions for each
comparison subsample. Note that it excludes the reference dataset.



ERRMEAN = _DOUBLE (Write)
`````````````````````````
Error in the mean value of the consistent data.



FILES() = LITERAL (Write)
`````````````````````````
The names of the datasets intercompared. The first is the reference
dataset.



LIMIT = _REAL (Read)
````````````````````
Confidence level at which samples are thought to be consistent. This
must lie in the range 0 to 1. [0.05]



IN = LITERAL (Read)
```````````````````
The names of the NDFs to be tested. If just one dataset is supplied,
it is divided into subsamples, which are compared (see parameter
NSAMPLE). When more than one dataset is provided, the first becomes
the reference dataset to which all the remainder are compared.
It may be a list of NDF names or direction specifications separated by
commas. If a list is supplied on the command line, the list must be
enclosed in double quotes. NDF names may include the regular
expressions ("*", "?", "[a-z]" etc.). Indirection may occur through
text files (nested up to seven deep). The indirection character is
"^". If extra prompt lines are required, append the continuation
character "-" to the end of the line. Comments in the indirection file
begin with the character "#".



MEAN = _DOUBLE (Write)
``````````````````````
Mean value of the consistent data.



NKEPT = _INTEGER (Write)
````````````````````````
Number of consistent data.



NSAMPLE = _INTEGER (Read)
`````````````````````````
The number of the subsamples into which to divide the reference
dataset. This parameter is only requested when a single NDF is to be
analysed, i.e. when only one dataset name is supplied via parameter
IN. The allowed range is 2 to 20. [3]



OUT = NDF (Write)
`````````````````
Output 1-dimensional NDF to which the consistent data is written. A
null value (!)---the suggested default---prevents creation of this
output dataset.



PROB() = _REAL (Write)
``````````````````````
Probability that each comparison subsample is drawn from the same
sample. Note that this excludes the reference sample.



SIGMA = _DOUBLE (Write)
```````````````````````
Standard deviation of the consistent data.



Examples
~~~~~~~~
kstest arlac accept
This tests the NDF called arlac for self-consistency at the 95%
confidence level using three subsamples. No output dataset is created.
The following applies to all the examples. If the reference dataset
and a comparison subsample are consistent, the two merge to form an
expanded reference dataset, which is then used for the next
comparison. Details of the comparisons are presented.
kstest arlac arlac_filt 0.10 nsample=10
As above except data are retained if they exceed the 90% probability
level, the comparisons are made with ten subsamples, and the
consistent data are written to the one-dimensional NDF called
arlac_filt.
kstest in="ref,obs*" comp=v out=master
This compares the variance in the NDF called ref with that in a series
of other NDFs whose names begin "obs". The variance consistent with
the reference dataset are written to the data array in the NDF called
master. To be consistent, they must be the same at 95% probability.
kstest "ref,^96lc.lis,obs*" master comp=v
As the previous example, except the comparison files include those
listed in the text file 96lc.lis.



Notes
~~~~~


+ The COMP array MUST exist in each NDF to be compared. The COMP array
becomes the data array in the output dataset. When COMP="Data", the
variance values corresponding to consistent data are propagated to the
output dataset.
+ Pixel bounds are ignored for the comparisons.
+ The internal comparison of a single dataset follows the method
outlined in Hughes D., 1993, JCMT-UKIRT Newsletter, #4, p32.
+ The maximum number of files is 20.




Copyright
~~~~~~~~~
Copyright (C) 1996-1998, 2004 Central Laboratory of the Research
Councils. All Rights Reserved.


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


+ This routine correctly processes DATA, VARIANCE, HISTORY, LABEL,
TITLE, and UNITS components, and propagates all extensions. AXIS
information is lost. Propagation is from the reference dataset.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All numeric data types are supported, however, processing uses the
  _REAL data type, and the output dataset has this type.




