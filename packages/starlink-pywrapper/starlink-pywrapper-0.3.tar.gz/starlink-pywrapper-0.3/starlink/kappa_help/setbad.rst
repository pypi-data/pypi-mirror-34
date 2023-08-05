

SETBAD
======


Purpose
~~~~~~~
Sets new bad-pixel flag values for an NDF


Description
~~~~~~~~~~~
This application sets new logical values for the bad-pixel flags
associated with an NDF's data and/or variance arrays. It may either be
used to test whether bad pixels are actually present in these arrays
and to set their bad-pixel flags accordingly, or to set explicit TRUE
or FALSE values for these flags.


Usage
~~~~~


::

    
       setbad ndf [value]
       



ADAM parameters
~~~~~~~~~~~~~~~



DATA = _LOGICAL (Read)
``````````````````````
This parameter controls whether the NDF's data array is processed. If
a TRUE value is supplied (the default), then it will be processed.
Otherwise it will not be processed, so that the variance array (if
present) may be considered on its own. The DATA and VARIANCE
parameters should not both be set to FALSE. [TRUE]



MODIFY = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied for this parameter (the default), then the
NDF's bad-pixel flags will be permanently modified if necessary. If a
FALSE value is supplied, then no modifications will be made. This
latter mode allows the routine to be used to check for the presence of
bad pixels without changing the current state of an NDF's bad-pixel
flags. It also allows the routine to be used on NDFs for which write
access is not available. [TRUE]



NDF = NDF (Read and Write)
``````````````````````````
The NDF in which bad pixels are to be checked for, and/or whose bad-
pixel flags are to be modified. (Note that setting the MODIFY
parameter to FALSE makes it possible to check for bad pixels without
permanently modifying the NDF.)



VALUE = _LOGICAL (Read)
```````````````````````
If a null (!) value is supplied for this parameter (the default), then
the routine will check to see whether any bad pixels are present. This
will only involve testing the value of each pixel if the bad-pixel
flag value is initially TRUE, in which case it will be reset to FALSE
if no bad pixels are found. If the bad-pixel flag is initially FALSE,
then it will remain unchanged.
If a logical (TRUE or FALSE) value is supplied for this parameter,
then it indicates the new bad-pixel flag value which is to be set.
Setting a TRUE value indicates to later applications that there may be
bad pixels present in the NDF, for which checks must be made.
Conversely, setting a FALSE value indicates that there are definitely
no bad pixels present, in which case later applications need not check
for them and should interpret the pixel values in the NDF literally.
The VALUE parameter is not used (a null value is assumed) if the
MODIFY parameter is set to FALSE indicating that the NDF is not to be
permanently modified. [!]



VARIANCE = _LOGICAL (Read)
``````````````````````````
This parameter controls whether the NDF's variance array is processed.
If a TRUE value is supplied (the default), then it will be processed.
Otherwise it will not be processed, so that the data array may be
considered on its own. The DATA and VARIANCE parameters should not
both be set to FALSE. [TRUE]



Examples
~~~~~~~~
setbad ngc1097
Checks the data and variance arrays (if present) in the NDF called
ngc1097 for the presence of bad pixels. If the initial bad-pixel flag
values indicate that bad pixels may be present, but none are found,
then the bad-pixel flags will be reset to FALSE. The action taken will
be reported.
setbad ndf=ngc1368 nomodify
Performs the same checks as described above, this time on the NDF
called ngc1368. The presence or absence of bad pixels is reported, but
the NDF is not modified.
setbad myfile nodata
Checks the variance array (if present) in the NDF called myfile for
the presence of bad pixels, and modifies its bad-pixel flag
accordingly. Specifying "nodata" inhibits processing of the data
array, whose bad-pixel flag is left unchanged.
setbad halpha false
Sets the bad-pixel flag for the NDF called halpha to FALSE. Any pixel
values which might previously have been regarded as bad will
subsequently be interpreted literally as valid pixels.
setbad hbeta true
Sets the bad-pixel flags for the NDF called hbeta to be TRUE. If any
pixels have the special "bad" value, then they will subsequently be
regarded as invalid pixels. Note that if this is followed by a further
command such as "setbad hbeta", then an actual check will be made to
see whether any pixels have this special value. The bad-pixel flags
will be returned to FALSE if they do not.



Bad-Pixel Flag Values
~~~~~~~~~~~~~~~~~~~~~
If a bad-pixel flag is TRUE, it indicates that the associated NDF
array may contain the special "bad" value and that affected pixels are
to be regarded as invalid. Subsequent applications will need to check
for such pixels and, if found, take account of them.
Conversely, if a bad-pixel flag value is FALSE, it indicates that
there are no bad pixels present. In this case, any special "bad"
values appearing in the array are to be interpreted literally as valid
pixel values.


Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NOMAGIC, SETMAGIC.


Quality Components
~~~~~~~~~~~~~~~~~~
Bad pixels may also be introduced into an NDF's data and variance
arrays implicitly through the presence of an associated NDF quality
component. This application will not take account of such a component,
nor will it modify it.
However, if either of the NDF's data or variance arrays do not contain
any bad pixels themselves, a check will be made to see whether a
quality component is present. If it is (and its associated bad-bits
mask is non-zero), then a warning message will be issued indicating
that bad pixels may be introduced via this quality component. If
required, these bad pixels may be eliminated either by setting the
bad-bits mask to zero or by erasing the quality component.


Copyright
~~~~~~~~~
Copyright (C) 1991 Science & Engineering Research Council. Copyright
(C) 1995 Central Laboratory of the Research Councils. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


