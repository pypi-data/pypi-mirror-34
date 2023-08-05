

POLROTREF
=========


Purpose
~~~~~~~
Rotate the reference direction in a pair of Q and U images


Description
~~~~~~~~~~~
This application creates a new pair of Q and U images from a supplied
pair of Q and U images, by changing the polarimetric reference
direction. The required direction can either be inherited from another
NDF (see parameter LIKE) or specified as a specified axis within a
specified coordinate Frame (see parameters AXIS and FRAME). It is
assumed that the supplied Q and U images are aligned in pixel
coordinates, and have the same reference direction.


Usage
~~~~~


::

    
       polrotref qin uin qout uout like
       



ADAM parameters
~~~~~~~~~~~~~~~



AXIS = _INTEGER (Read)
``````````````````````
Parameter AXIS is used only if a null value is supplied for parameter
LIKE, in which case AXIS is the index of the axis within the
coordinate frame specified by parameter FRAME that is to be used as
the reference direction in the output NDFs. The first axis has index
1. [2]



FRAME = LITERAL (Read)
``````````````````````
A string specifying the co-ordinate Frame to which parameter AXIS
refers. If a null parameter value is supplied, then the current Frame
within the NDF specified by parameter QIN is used. The string can be
one of the following:


+ A domain name such as SKY, SPECTRUM, AXIS, PIXEL, etc.
+ An integer value giving the index of the required Frame within the
WCS component.
+ A "Sky Co-ordinate System" (SCS) value such as EQUAT(J2000) (see
  section "Sky Co-ordinate Systems" in SUN/95). Using an SCS value is
  equivalent to specifying "SKY" for this parameter and then setting the
  System attribute (to "FK5", "Galactic", etc.) using KAPPA command
  WCSATTRIB. ["PIXEL"]





LIKE = NDF (Read)
`````````````````
A 2D Q or U NDF that defines the new reference direction. The supplied
NDF should have a Frame with Domain "POLANAL" in its WCS component.
The supplied Q and U images are modified so that they use the same
reference direction as the supplied NDF. If null (!) is supplied, the
rotation is defined by parametrer AXIS. [!]



QIN = NDF (Read)
````````````````
The 2D input Q image. The WCS component of this NDF must contain a
POLANAL Frame.



QOUT = NDF (Write)
``````````````````
The 2D output Q image.



UIN = NDF (Read)
````````````````
The 2D input U image. The WCS component of this NDF must contain a
POLANAL Frame.



UOUT = NDF (Write)
``````````````````
The 2D output U image.



Notes
~~~~~


+ It is assumed that the supplied Q and U images are aligned in pixel
coordinates, and have the same reference direction.
+ The supplied Q and U arrays are mapped as double precision values.
+ Variance arrays are rotated in the same was as Data arrays.
+ Quality arrays are copied unchanged from input to output.
+ The reference direction is defined as being constant within the
  POLANAL Frame. It will not be constant within another Frame if the
  transformation from POLANAL to that Frame is non-linear.




Copyright
~~~~~~~~~
Copyright (C) 2012 Science and Technology Facilities Council.
Copyright (C) 2015 East Asian Observatory. All Rights Reserved.


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


