

ASTSWITCHMAP
============


Purpose
~~~~~~~
Create a SwitchMap


Description
~~~~~~~~~~~
This application creates a new SwitchMap and optionally initialises
its attributes. An option is provided to create a SwitchMap from an
output file created by FIGARO:IARC (see parameter IARCFILE).
A SwitchMap is a Mapping which represents a set of alternate Mappings,
each of which is used to transform positions within a particular
region of the input or output coordinate system of the SwitchMap.
A SwitchMap can encapsulate any number of Mappings, but they must all
have the same number of inputs (Nin attribute value) and the same
number of outputs (Nout attribute value). The SwitchMap itself
inherits these same values for its Nin and Nout attributes. Each of
these Mappings represents a "route" through the switch, and are
referred to as "route" Mappings below. Each route Mapping transforms
positions between the input and output coordinate space of the entire
SwitchMap, but only one Mapping will be used to transform any given
position. The selection of the appropriate route Mapping to use with
any given input position is made by another Mapping, called the
"selector" Mapping. Each SwitchMap encapsulates two selector Mappings
in addition to its route Mappings; one for use with the SwitchMap's
forward transformation (called the "forward selector Mapping"), and
one for use with the SwitchMap's inverse transformation (called the
"inverse selector Mapping"). The forward selector Mapping must have
the same number of inputs as the route Mappings, but should have only
one output. Likewise, the inverse selector Mapping must have the same
number of outputs as the route Mappings, but should have only one
input.
When the SwitchMap is used to transform a position in the forward
direction (from input to output), each supplied input position is
first transformed by the forward transformation of the forward
selector Mapping. This produces a single output value for each input
position referred to as the selector value. The nearest integer to the
selector value is found, and is used to index the array of route
Mappings (the first supplied route Mapping has index 1, the second
route Mapping has index 2, etc). If the nearest integer to the
selector value is less than 1 or greater than the number of route
Mappings, then the SwitchMap output position is set to a value of
AST__BAD on every axis. Otherwise, the forward transformation of the
selected route Mapping is used to transform the supplied input
position to produce the SwitchMap output position.
When the SwitchMap is used to transform a position in the inverse
direction (from "output" to "input"), each supplied "output" position
is first transformed by the inverse transformation of the inverse
selector Mapping. This produces a selector value for each "output"
position. Again, the nearest integer to the selector value is found,
and is used to index the array of route Mappings. If this selector
index value is within the bounds of the array of route Mappings, then
the inverse transformation of the selected route Mapping is used to
transform the supplied "output" position to produce the SwitchMap
"input" position. If the selector index value is outside the bounds of
the array of route Mappings, then the SwitchMap "input" position is
set to a value of AST__BAD on every axis.
In practice, appropriate selector Mappings should be chosen to
associate a different route Mapping with each region of coordinate
space. Note that the SelectorMap class of Mapping is particularly
appropriate for this purpose.
If a compound Mapping contains a SwitchMap in series with its own
inverse, the combination of the two adjacent SwitchMaps will be
replaced by a UnitMap when the compound Mapping is simplified using
astsimplify.


Usage
~~~~~


::

    
       astswitchmap fsmap ismap route1 route2 options result
       



ADAM parameters
~~~~~~~~~~~~~~~



FMT = LITERAL (Read)
````````````````````
The format in which to store output objects. Can be "AST", "XML",
"STCS", or any FitsChan encoding such as FITS-WCS. Only used if the
output object is written to a text file. An error is reported if the
output object cannot be written using the requested format. ["AST"]



FSMAP = LITERAL (Read)
``````````````````````
An NDF or text file holding the forward selector Mapping. If an NDF is
supplied, the Mapping from the Base Frame to the Current Frame of its
WCS FrameSet will be used. The supplied Mapping must have a defined
forward transformation, but need not have a defined inverse
transformation. It must have one output, and the number of inputs must
match the number of inputs of each of the supplied route Mappings. A
null (!) value may be supplied, in which case the SwitchMap will have
an undefined forward Mapping. This parameter is only used if a null
value is supplied for IARCFILE.



IARCFILE = LITERAL (Read)
`````````````````````````
The name of a text file containing the coefficients of the polynomial
fit produced by the FIGARO:IARC command. If a null value (!) is
supplied, the parameters ISMAP, FSMAP and ROUTEMAP1, etc, are used
instead to determine the nature of the required SwitchMap. Otherwise,
the returned SwitchMap will have two inputs and 1 output. The inputs
are channel number and row number (in that order), and the one output
is wavelength in Angstroms. [!]



ISMAP = LITERAL (Read)
``````````````````````
An NDF or text file holding the inverse selector Mapping. If an NDF is
supplied, the Mapping from the Base Frame to the Current Frame of its
WCS FrameSet will be used. The supplied Mapping must have a defined
inverse transformation, but need not have a defined forward
transformation. It must have one input, and the number of outputs must
match the number of outputs of each of the supplied route Mappings. A
null (!) value may be supplied, in which case the SwitchMap will have
an undefined inverse Mapping. This parameter is only used if a null
value is supplied for IARCFILE.



ROUTEMAP1-ROUTEMAP25 = LITERAL (Given)
``````````````````````````````````````
A set of 25 parameters associated with the NDFs or text files holding
the route Mappings. If an NDF is supplied, the Mapping from the Base
Frame to the Current Frame of its WCS FrameSet will be used. All the
supplied route Mappings must have common values for the Nin and Nout
attributes, and these values define the number of inputs and outputs
of the SwitchMap. There can be no missing Mappings; if ROUTEMAP3 is to
be processed then ROUTEMAP1 and ROUTEMAP2 must also be supplied. A
null value (!) should be supplied to indicate that there are no
further Mappings. ROUTEMAP3 to ROUTEMAP25 default to null (!). At
least one Mapping must be supplied. These parameters are only used if
a null value is supplied for IARCFILE.



OPTIONS = LITERAL (Read)
````````````````````````
A string containing an optional comma-separated list of attribute
assignments to be used for initialising the new SwitchMap.



RESULT = LITERAL (Read)
```````````````````````
A text file to receive the new SwitchMap.



Copyright
~~~~~~~~~
Copyright (C) 2006 Particle Physics & Astronomy Research Council. All
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


