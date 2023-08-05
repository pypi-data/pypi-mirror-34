

WCSATTRIB
=========


Purpose
~~~~~~~
Manages attribute values associated with the WCS component of an NDF


Description
~~~~~~~~~~~
This application can be used to manage the values of attributes
associated with the current co-ordinate Frame of an NDF (title, axis
labels, axis units, etc.).
Each attribute has a name, a value, and a state. This application
accesses all attribute values as character strings, converting to and
from other data types as necessary. The attribute state is a Boolean
flag (i.e. TRUE or FALSE) indicating whether or not a value has been
assigned to the attribute. If no value has been assigned to an
attribute, then it adopts a default value until an explicit value is
assigned to it. An attribute value can be cleared, causing the
attribute to revert to its default value.
The operation performed by this application is controlled by parameter
MODE, and can be:


+ display the value of an attribute;
+ set a new value for a single attribute;
+ set new values for a list of attributes;
+ clear an attribute value; and
+ test the state of an attribute.

Note, the attributes of the PIXEL, FRACTION, GRID and AXIS Frames are
managed internally by the NDF library. They may be examined using this
application, but an error is reported if any attempt is made to change
them. The exception to this is that the DOMAIN attribute may be
changed, resulting in a copy of the Frame being added to the WCS
component of the NDF with the new Domain name. The AXIS Frame is
derived from the AXIS structures within the NDF, so the AXLABEL and
AXUNITS commands may be used to change the axis label and units string
respectively for the AXIS Frame.


Usage
~~~~~


::

    
       wcsattrib ndf mode name newval
       



ADAM parameters
~~~~~~~~~~~~~~~



MODE = LITERAL (Read)
`````````````````````
The operation to be performed on the attribute specified by parameter
NAME. It can be one of the following.


+ "Get" -- The current value of the attribute is displayed on the
screen and written to output parameter VALUE. If the attribute has not
yet been assigned a value (or has been cleared), then the default
value will be displayed.
+ "MSet" -- Assigns new values to multiple attributes. The attribute
names and values are obtained using parameter SETTING.
+ "Set" -- Assigns a new value, given by parameter NEWVAL, to the
attribute.
+ "Test" -- Displays "TRUE" if the attribute has been assigned a
value, and "FALSE" otherwise (in which case the attribute will adopt
its default value). This flag is written to the output parameter
STATE.
+ "Clear" -- Clears the current attribute value, causing it to revert
  to its default value.

The initial suggested default is "Get".



NAME = LITERAL (Read)
`````````````````````
The attribute name. Not used if MODE is "MSet".



NDF = NDF (Read and Write)
``````````````````````````
The NDF to be modified or read. When MODE="Get", the access is Read
only.



NEWVAL = LITERAL (Read)
```````````````````````
The new value to assign to the attribute. It is only used if MODE is
"Set".



REMAP = _LOGICAL (Read)
```````````````````````
Only accessed if MODE is "Set" or "clear". If REMAP is TRUE, then the
Mappings which connect the current Frame to the other Frames within
the WCS FrameSet will be modified (if necessary) to maintain the
FrameSet integrity. For instance, if the current Frame of the NDF
represents FK5 RA and DEC, and you change System from "FK5" to
"Galactic", then the Mappings which connect the SKY Frame to the other
Frames (e.g. PIXEL, AXIS) will be modified so that each pixel
corresponds to the correct Galactic co-ordinates. If REMAP is FALSE,
then the Mappings will not be changed. This can be useful if the
FrameSet has incorrect attribute values for some reason, which need to
be corrected without altering the Mappings to take account of the
change. [TRUE]



SETTING = LITERAL (Read)
````````````````````````
Only accessed if MODE is set to "MSet". It should hold a comma-
separated list of "<attribute>=<value>" strings, where <attribute> is
the name of an attribute and <value> is the value to assign to the
attribute.



STATE = _LOGICAL (Write)
````````````````````````
On exit, this holds the state of the attribute on entry to this
application. It is not used if MODE is "MSet".



VALUE = LITERAL (Write)
```````````````````````
On exit, this holds the value of the attribute on entry to this
application. It is not used if MODE is "MSet".



Examples
~~~~~~~~
wcsattrib my_spec set System freq
This sets the System attribute of the current co-ordinate Frame in the
NDF called my_Spec so that the Frame represents frequency (this
assumes the current Frame is a SpecFrame). The Mappings between the
current Frame and the other Frames are modified to take account of the
change of system.
wcsattrib my_spec mset setting='unit(1)=km/s,system(1)=vrad'
This sets new values of "km/s" and "vrad" simultaneously for the Unit
and System attributes for the first axis of the NDF called my_spec.
wcsattrib ngc5128 set title "Polarization map of Centaurus-A"
This sets the Title attribute of the current co-ordinate Frame in the
NDF called ngc5128 to the string "Polarization map of Centaurus-A".
wcsattrib my_data set domain saved_pixel
This sets the Domain attribute of the current co-ordinate Frame in the
NDF called my_data to the string SAVED_PIXEL.
wcsattrib my_data set format(1) "%10.5G"
This sets the Format attribute for axis 1 in the current co-ordinate
Frame in the NDF called my_data, so that axis values are formatted as
floating-point values using a minimum field width of ten characters,
and displaying five significant figures. An exponent is used if
necessary.
wcsattrib ngc5128 set format(2) bdms.2
This sets the Format attribute for axis 2 in the current co-ordinate
Frame in the NDF called ngc5128, so that axis values are formatted as
separate degrees, minutes and seconds fields, separated by blanks. The
seconds field has two decimal places. This assumes the current co-
ordinate Frame in the NDF is a celestial co-ordinate Frame.
wcsattrib my_data get label(1)
This displays the label associated with the first axis of the current
co-ordinate Frame in the NDF called my_data. A default label is
displayed if no value has been set for this attribute.
wcsattrib my_data test label(1)
This displays "TRUE" if a value has been set for the Label attribute
for the first axis of the current co-ordinate Frame in the NDF called
my_data, and "FALSE" otherwise.
wcsattrib my_data clear label(1)
This clears the Label attribute for the first axis of the current co-
ordinate Frame in the NDF called my_data. It reverts to its default
value.
wcsattrib my_data set equinox J2000 remap=no
This assumes that the Equinox attribute for the current co-ordinate
Frame within NDF "my_data" has been set to some incorrect value, which
needs to be corrected to "J2000". The REMAP parameter is set false,
which prevents the inter-Frame Mappings from being altered to take
account of the new Equinox value. This means that each pixel in the
NDF will retain its original RA and DEC values (but they will now be
interpreted as J2000). If REMAP had been left at its default value of
TRUE, then the RA and DEC associated with each pixel would have been
modified in order to precess them from the original (incorrect)
equinox to J2000.



Notes
~~~~~


+ An error is reported if an attempt is made to set or clear the Base
Frame in the WCS component.
+ The Domain names GRID, FRACTION, AXIS and PIXEL are reserved for use
  by the NDF library and an error will be reported if an attempt is made
  to assign one of these values to any Frame.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: NDFTRACE, WCSFRAME, WCSREMOVE, WCSCOPY, WCSADD, AXLABEL,
AXUNITS.


Copyright
~~~~~~~~~
Copyright (C) 1998, 2001, 2003 Central Laboratory of the Research
Councils. All Rights Reserved. Copyright (C) 2006 Particle Physics &
Astronomy Research Council. Copyright (C) 2007 Science & Technology
Facilities Council. All Rights Reserved.


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


