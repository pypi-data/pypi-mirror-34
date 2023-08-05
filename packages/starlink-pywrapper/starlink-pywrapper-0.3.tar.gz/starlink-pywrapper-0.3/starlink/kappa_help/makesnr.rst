

MAKESNR
=======


Purpose
~~~~~~~
Creates a signal-to-noise array from an NDF with defined variances


Description
~~~~~~~~~~~
This application creates a new NDF from an existing NDF by dividing
the DATA component of the input NDF by the square root of its VARIANCE
component. The DATA array in the output NDF thus measures the signal
to noise ratio in the input NDF.
Anomalously small variance values in the input can cause very large
spurious values in the output signal to noise array. To avoid this,
pixels that have a variance value below a given threshold are set bad
in the output NDF.


Usage
~~~~~


::

    
       makesnr in out [minvar]
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input NDF. An error is reported if this NDF does not have a
VARIANCE component.



MINVAR = _REAL (Read)
`````````````````````
The minimum variance value to be used. Input pixels that have variance
values smaller than this value will be set bad in the output. The
suggested default is determined by first forming a histogram of the
logarithm of the input variance values. The highest peak is then found
in this histogram. The algorithm then moves down from this peak
towards lower variance values until the histogram has dropped to a
value equal to the square root of the peak value, or a significant
minimum is encountered in the histogram. The corresponding variance
value is used as the suggested default. []



OUT = NDF (Write)
`````````````````
The output signal to noise NDF. The VARIANCE component of this NDF
will be filled with the value 1.0 (except that bad DATA values will
also have bad VARIANCE values).



Copyright
~~~~~~~~~
Copyright (C) 2006 Particle Physics & Astronomy Research Council. All
Rights Reserved.


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


