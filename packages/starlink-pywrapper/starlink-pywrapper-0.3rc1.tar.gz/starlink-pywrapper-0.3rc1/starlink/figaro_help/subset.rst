

SUBSET
======


Purpose
~~~~~~~
Take a subset of a data set


Description
~~~~~~~~~~~
Takes a rectangular subset of a data set. The given data set and the
resulting subset may have up to seven axes. Axes that become
degenerate by subsetting - i.e. along which only one pixel is chosen -
are deleted from the subset. Thus the subset may have smaller
dimensionality than the original.


Usage
~~~~~


::

    
       subset in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input file.



OUT = NDF (Read)
````````````````
The output file.



Examples
~~~~~~~~
subset in(1.5:2.5,10:12) out
This takes the data from IN and writes the subset to OUT. The subset
is specified as having 1st axis coordinates between 1.5 and 2.5 and
2nd axis pixel numbers between 10 and 12.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.


