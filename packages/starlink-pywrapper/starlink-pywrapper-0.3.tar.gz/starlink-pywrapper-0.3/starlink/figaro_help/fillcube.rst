

FILLCUBE
========


Purpose
~~~~~~~
Copy one NDF into part of another


Description
~~~~~~~~~~~
This routine copies data, variance etc. from one NDF into another
existing NDF. By successive calls the output NDF can be filled with
data from a number of input NDFs. The target area in the output is
identified by matching axis data (not pixel indices). Data are copied
from input to output only if the input data value is not bad, apart
from that existing data in the output are overwritten.
This application is more akin to ASCIN than to GROW. The main
differences to ASCIN are that FILLCUBE updates an existing output and
that its input is an NDF rather than an ASCII table. Its main
advantage over GROW is that input and output may (actually must) have
the same dimensionality, but any dimensions or axis data can differ.
Also it is not necessary that target pixels form a contiguous subset
in the output: The input pixels could match, say, every second or
third output pixel. The disadvantages are that results and
spectroscopic values in the Specdre Extension are not handled, and
that the coordinates along each axis in input and output must be
linear.
For each input pixel, FILLCUBE looks for the output pixel that is
nearest in the space of axis data coordinates. Data are copied only if
the output pixel is hit close to its centre. However, if an axis is
degenerate (has only one pixel) in both input and output, then the
coordinates are assumed to match.
No indication is given as to how many input pixels did not match any
output pixel.


Usage
~~~~~


::

    
       fillcube in out
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
True if informational messages are to be issued.



TOL = _REAL (Read)
``````````````````
The tolerated fraction of the pixel size by which the input
coordinates may deviate from the output coordinates. If any one of the
axis values deviates more than TOL times the coordinate step, then the
input data are ignored and the output data left unchanged. [0.2]



IN = NDF (Read)
```````````````
The input NDF.



OUT = NDF (Read)
````````````````
The output NDF. This must already exist, update access is required.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7, although it is
largely ignored.
This routine works in situ on an existing output file.
Spectroscopic values must not exist in the Extension of either the
input or the output NDF: A unique coordinate axis is required for all
axes, including the spectroscopic one, in order to locate the target
pixels by matching coordinates between input and output. If this is
inconvenient, GROW may be a more suitable application for your
purpose.
Spectroscopic widths must not exist in the Extension of the output NDF
and are ignored in the input NDF: This information is likely to be
present only when spectroscopic values are present as well.
Covariance row sums must not exist in the Extension of the output NDF:
The validity of this information is difficult to assess when only
parts of spectra might be copied from one cube to another, and when
these parts are contiguous in the input but might not be in the
output. Input covariance row sums are ignored.
The results in the input Extension are ignored, and results must not
exist in the output Extension.


