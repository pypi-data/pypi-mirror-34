

GOODVAR
=======


Purpose
~~~~~~~
Replace negative, zero and bad variance values


Description
~~~~~~~~~~~
This routine checks the variance component of an NDF for values that
are bad, negative, or zero and replaces them by values specified by
the user. The specified value can be the null value ("!") which is
translated into the bad value.


Usage
~~~~~


::

    
       goodvar in out bad neg zero
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF.



OUT = NDF (Read)
````````````````
The output NDF.



BAD = _REAL (Read)
``````````````````
The value which replaces bad values. Enter an exclamation mark to keep
bad values. Bad values in VARIANCE or ERRORS are not allowed by
Figaro. If DSA has to convert these arrays while mapping them,
floating overflows or square roots of negative numbers may occur, and
the application is liable to crash. [!]



NEG = _REAL (Read)
``````````````````
The value which replaces negative values. Enter an exclamation mark to
replace negative values with the bad value. Negative errors or
variances are nonsense. Negative variances often will cause an
application to crash because it takes the square root to calculate the
error. [!]



ZERO = _REAL (Read)
```````````````````
The value which replaces zeroes. Enter an exclamation mark to replace
zeroes with the bad value. Errors of zero sometimes are reasonable or
necessary for error propagation. In other instances they cause
problems, because statistical weights often are the reciprocal of the
variance. [!]



