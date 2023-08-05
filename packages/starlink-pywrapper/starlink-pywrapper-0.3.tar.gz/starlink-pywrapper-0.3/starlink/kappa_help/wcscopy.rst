

WCSCOPY
=======


Purpose
~~~~~~~
Copies WCS information from one NDF to another


Description
~~~~~~~~~~~
This application copies the WCS component from one NDF to another,
optionally modifying it to take account of a linear mapping between
the pixel co-ordinates in the two NDFs. It can be used, for instance,
to rectify the loss of WCS information produced by older applications
which do not propagate the WCS component.


Usage
~~~~~


::

    
       wcscopy ndf like [tr] [confirm]
       



ADAM parameters
~~~~~~~~~~~~~~~



CONFIRM = _LOGICAL (Read)
`````````````````````````
If TRUE, the user is asked for confirmation before replacing any
existing WCS component within the input NDF. No confirmation is
required if the there is no WCS component in the input NDF. [TRUE]



LIKE = NDF (Read)
`````````````````
The reference NDF data structure from which WCS information is to be
copied.



NDF = NDF (Read and Write)
``````````````````````````
The input NDF data structure in which the WCS information is to be
stored. Any existing WCS component is over-written (see parameter
CONFIRM).



OK = _LOGICAL (Read)
````````````````````
This parameter is used to get a confirmation that an existing WCS
component within the input NDF can be over-written.



TR( ) = _DOUBLE (Read)
``````````````````````
The values of this parameter are the coefficients of a linear
transformation from pixel co-ordinates in the reference NDF given for
parameter LIKE, to pixel co-ordinates in the input NDF given for
parameter NDF. For instance, if a feature has pixel co-ordinates
(X,Y,Z,...) in the reference NDF, and pixel co-ordinates (U,V,W,...)
in the input NDF, then the following transformations would be used,
depending on how many axes each NDF has:


+ 1-dimensional:

U = TR(1) + TR(2)*X


+ 2-dimensional:

U = TR(1) + TR(2)*X + TR(3)*Y
V = TR(4) + TR(5)*X + TR(6)*Y


+ 3-dimensional:

U = TR(1) + TR(2)*X + TR(3)*Y + TR(4)*Z
V = TR(5) + TR(6)*X + TR(7)*Y + TR(8)*Z
W = TR(9) + TR(10)*X + TR(11)*Y + TR(12)*Z
If a null value (!) is given it is assumed that the pixel co-ordinates
of a given feature are identical in the two NDFs. [!]



Examples
~~~~~~~~
wcscopy m51_sim m51
This copies the WCS component from the NDF called m51 to the NDF
called m51_sim, which may hold the results of a numerical simulation
for instance. It is assumed that the two NDFs are aligned (i.e. the
pixel co-ordinates of any feature are the same in both NDFs).
wcscopy m51_sqorst m51 [125,0.5,0.0,125,0.0,0.5]
This example assumes that an application similar to SQORST has
previously been used to change the size of a 2-dimensional NDF called
m51, producing a new NDF called m51_sqorst. It is assumed that this
SQORST-like application does not propagate WCS and also resets the
pixel origin to [1,1]. In fact, this is what KAPPA:SQORST actually
did, prior to version 1.0. This example shows how WCSCOPY can be used
to rectify this by copying the WCS component from the original NDF m51
to the squashed NDF m51_sqorst, modifying it in the process to take
account of both the squashing and the resetting of the pixel origin
produced by SQORST. To do this, you need to work out the
transformation in pixel co-ordinates produced by SQORST, and specify
this when running WCSCOPY using the TR parameter. Let's assume the
first axis of NDF m51 has pixel-index bounds of I1:I2 (these values
can be found using NDFTRACE). If the first axis in the squashed NDF
m51_sqorst spans M pixels (where M is the value assigned to SQORST
parameter XDIM), then it will have pixel-index bounds of 1:M. Note,
the lower bound is 1 since the pixel origin has been reset by SQORST.
The squashing factor for the first axis is then:
FX = M/(I2 - I1 + 1)
and the shift in the pixel origin is:
SX = FX*( 1 - I1 )
Likewise, if the bounds of the second axis in m51 are J1:J2, and
SQORST parameter YDIM is set to N, then the squashing factor for the
second axis is:
FY = N/(J2 - J1 + 1)
and the shift in the pixel origin is:
SY = FY*( 1 - J1 )
You would then use the following values for parameter TR when running
WCSCOPY:
TR = [SX, FX, 0.0, SY, 0.0, FY]
Note, the zero terms indicate that the axes are independent (i.e.
there is no rotation of the image). The numerical values in the
example are for an image with pixel-index bounds of 52:251 on both
axes which was squashed by SQORST to produce an image with 100 pixels
on each axis.



Notes
~~~~~


+ An error is reported if the transformation supplied using parameter
TR is singular.
+ The pixel with pixel index I spans a range of pixel co-ordinate from
(I - 1.0) to (I).
+ The pixel indices of the bottom left pixel in an NDF is called the
  "pixel origin" of the NDF, and can take any value. The pixel origin
  can be examined using application NDFTRACE and set using application
  SETORIGIN. WCSCOPY takes account of the pixel origins in the two NDFs
  when modifying the WCS component. Thus, if a null value is given for
  parameter TR, the supplied WCS component may still be modified if the
  two NDFs have different pixel origins.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFTRACE, WCSFRAME, WCSREMOVE, WCSADD, WCSATTRIB


Copyright
~~~~~~~~~
Copyright (C) 1998 Central Laboratory of the Research Councils. All
Rights Reserved.


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


