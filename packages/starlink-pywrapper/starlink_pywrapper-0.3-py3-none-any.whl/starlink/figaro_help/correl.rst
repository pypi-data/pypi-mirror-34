

CORREL
======


Purpose
~~~~~~~
Correlate two or three data sets


Description
~~~~~~~~~~~
This routine correlates two or three data sets. Either pair is
subjected to a linear fit and the third data set is subjected to a
two-parameter linear fit (i.e. regarded as a linear function of the
first and second data sets). Each data set may be an NDF section. All
must have the same dimensions.


Usage
~~~~~


::

    
       correl inlist out logfil
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, the routine will issue only error messages and no
informational messages. [YES]



VARUSE = _LOGICAL (Read)
````````````````````````
If false, input variances are ignored. [YES]



INLIST = LITERAL (Read)
```````````````````````
The group of input NDFs. Two or three NDFs must be specified. A
complicated INLIST could look something like
M_51(25:35,-23.0,-24.0),M101,^LISTFILE.LIS
This example NDF group specification consists of

+ one identified NDF from which a subset is to be taken,
+ one identified NDF,
+ an indirection to an ASCII file containing more NDF group
  specifications. That file may have comment lines and in-line comments,
  which are recognised as beginning with a hash (#).





OUT = FILENAME (Read)
`````````````````````
The ASCII output file where the data points are written into a table.
A new file will be opened. No file will be opened, if "!" is entered.
The table in OUT is without any information else than the values from
the 1st, 2nd, 3rd data array and errors from the 1st, 2nd, 3rd
variance array in that order. [!]



LOGFIL = FILENAME (Read)
````````````````````````
The ASCII log file where fit results are written to. This will be
opened for append, if such a file exists.



