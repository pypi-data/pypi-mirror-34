

R2CMPLX
=======


Purpose
~~~~~~~
Creates a complex data structure from a real data array


Description
~~~~~~~~~~~
Creates a complex data structure from a real data structure. RCMPLX
sets the imaginary part of the complex data to zero. It can be set
subsequently using the I2CMPLX command.
The output data follows the input in structure, except that the data
array is of type DOUBLE. A zero-filled imaginary data array is also
created. Any axis structures are retained.


Usage
~~~~~


::

    
       r2cmplx rdata cdata
       



ADAM parameters
~~~~~~~~~~~~~~~



RDATA = FILE (Read)
```````````````````
RDATA is the name of an existing file that contains a data array that
is to become the real part of the complex data structure that is
created by R2CMPLX.



CDATA = FILE (Write)
````````````````````
CDATA is the name of the complex data structure to be created. Its
real part will come from the structure specified as RDATA, and its
imaginary part will be set to zero. If CDATA is the same as RDATA,
RDATA will be transformed into a complex structure; otherwise, a new
file is created.



