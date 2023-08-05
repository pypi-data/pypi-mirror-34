

XTRACT
======


Purpose
~~~~~~~
Average an N-dimensional cube into an (N-M)-dimensional one


Description
~~~~~~~~~~~
This routine reduces the number of axes of a data set by averaging
pixels along some axes while retaining other axes. A simple and common
example is averaging all or a certain range of rows (or columns) of an
image to create a single row, e.g. an averaged spectrum from a 2-D
slit spectrum. Input pixels with bad or zero variance are treated as
bad, i.e. disregarded in the averaging (unless NOVAR is true).


Usage
~~~~~


::

    
       xtract in colaps out
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, the routine will issue only error messages and no
informational messages. [YES]



VARUSE = _LOGICAL (Read)
````````````````````````
If false, data variance in the input is ignored and output variance is
calculated from the scatter of averaged values. If true, data variance
in the input is used to weight mean values and to calculate output
variance. [YES]



IN = NDF (Read)
```````````````
Input file.



COLAPS( 7 ) = _INTEGER (Read)
`````````````````````````````
For each axis in IN a 0 indicates that the axis is to be retained in
OUT, a 1 indicates that along that axis pixels from IN are to be
averaged.



OUT = NDF (Read)
````````````````
Output file, containing the extracted data set.



Examples
~~~~~~~~
xtract cube(-30.:30.,1.5:2.5,10:20) [0,0,1] xyplane
This first takes a subset from the 3-D data cube extending from -30 to
+30, 1.5 to 2.5, 10 to 20 along the 1st, 2nd, 3rd axes respectively.
(Coordinates are used along the 1st and 2nd axes, pixel indices along
the 3rd.) From that sub-cube all the x-y-planes are averaged to create
a 2-D image. (E.g. this averages the channel maps between 10 and 20
into an integrated map.)
xtract cube(-30.:30.,1.5:2.5,10:20) [1,1,0] spectrum
This averages each x-y-plane into a single point of the output row.
The subset used is the same as above. (E.g. this averages the cube of
channel maps into a mean spectrum.)
xtract image(-30.:30.,1.5:2.5) [0,1] spectrum info=no varuse=no
This averages all rows between 1.5 and 2.5 into a spectrum. The
spectrum extends from -30 to +30. Informational messages are
suppressed, and data variances in the image are ignored. The variances
in the spectrum are calculated from the row-to-row scatter in each
column.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7. However, no
extraction is performed on NDFs in the input Specdre Extension. If the
spectroscopic axis is retained, then the scalar components in the
Extension are propagated. If the spectroscopic axis is collapsed, the
Extension is not propagated at all.


