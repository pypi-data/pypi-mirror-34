

QUCOVAR
=======


Purpose
~~~~~~~
Find co-variance of Q and U from a POL2 observation


Description
~~~~~~~~~~~
Calculates the co-variance of Q and U in each map pixel for a POL2
observation. For a single pixel, the returned co-variance is:
sum( W_i*RQ_i*RU_i )/(N*sum( W_i ))
where:


+ RQ_I is the ith residual from the Q map, and RU_I is the ith
residual from the U map. A residual is the bolometer Q or U sample
minus the Q or U map pixel value (the pixel value is the weighted mean
of the Q or U sample values that fall in the pixel). These residuals
can be dumped by makemap when the Q and U maps are created.
+ W_i is the weight for the ith sample. It is the geometric mean of
  the weights associated with RQ_i and RU_i. These can also be dumped by
  makemap, but are created initially by calcuq as the residual of the
  fitting process for each sample.

The input NDFs should be created by running makemap twice on the
CALCQU output for a single POL2 observation - once to create a Q map
and once to create a U map. On each invocation of makemap, the config
should include "exportndf=(res,qua,noi,lut)". This will causes two
extra NDFs to be created by each invocation of makemap with suffixes
"QT_con_lut", "QT_con_res", "UT_con_lut" and "UT_con_res". These
should be supplied as input to this command.


ADAM parameters
~~~~~~~~~~~~~~~



QLUT = NDF (Read)
`````````````````
3-D NDF holding Q LUT model (suffix "QT_con_lut").



QRES = NDF (Read)
`````````````````
3-D NDF holding Q residuals time-series (suffix "QT_con_res").



ULUT = NDF (Read)
`````````````````
3-D NDF holding U LUT model (suffix "UT_con_lut").



URES = NDF (Read)
`````````````````
3-D NDF holding U residuals time-series (suffix "UT_con_res").



MSG_FILTER = _CHAR (Read)
`````````````````````````
Control the verbosity of the application. Values can be NONE (no
messages), QUIET (minimal messages), NORMAL, VERBOSE, DEBUG or ALL.
[NORMAL]



OUT = NDF (Write)
`````````````````
The output NDF - a 2-dimensional map holding the QU co-variance at
each pixel.



REF = NDF (Read)
````````````````
2-D NDF holding a Q or U map made from the same POL2 observation. This
acts as a template to define the shape, size and WCS of the output
NDF.



Copyright
~~~~~~~~~
Copyright (C) 2016 East Asian Observatory. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA


