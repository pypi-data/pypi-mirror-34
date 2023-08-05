

SETUNITS
========


Purpose
~~~~~~~
Sets a new units value for an NDF data structure


Description
~~~~~~~~~~~
This routine sets a new value for the UNITS component of an existing
NDF data structure. The NDF is accessed in update mode and any pre-
existing UNITS component is over-written with a new value.
Alternatively, if a `null' value (!) is given for the UNITS parameter,
then the NDF's UNITS component will be erased.
There is also an option to modify the pixel values within the NDF to
reflect the change in units (see parameter MODIFY).


Usage
~~~~~


::

    
       setunits ndf units
       



ADAM parameters
~~~~~~~~~~~~~~~



NDF = NDF (Read and Write)
``````````````````````````
The NDF data structure whose UNITS component is to be modified.



MODIFY = _LOGICAL (Read)
````````````````````````
If a TRUE value is supplied, then the pixel values in the DATA and
VARIANCE components of the NDF will be modified to reflect the change
in units. For this to be possible, both the original Units value in
the NDF and the new Units value must both correspond to the format for
units strings described in the FITS WCS standard (see "Representations
of world coordinates in FITS", Greisen & Calabretta, 2002, A&A -
available at http://www.aoc.nrao.edu/~egreisen/wcs_AA.ps.gz) If either
of the two units strings are not of this form, or if it is not
possible to find a transformation between them (for instance, because
they represent different quantities), an error is reported. [FALSE]



UNITS = LITERAL (Read)
``````````````````````
The value to be assigned to the NDF's UNITS component (e.g.
"J/(m**2*Angstrom*s)" or "count/s"). This value may later be used by
other applications for labelling graphs and other forms of display
where the NDF's data values are shown. The suggested default is the
current value.



Examples
~~~~~~~~
setunits ngc1342 "count/s"
Sets the UNITS component of the NDF structure ngc1342 to have the
value "count/s". The pixel values are not changed.
setunits ndf=spect units="J/(m**2*Angstrom*s)"
Sets the UNITS component of the NDF structure spect to have the value
"J/(m**2*Angstrom*s)". The pixel values are not changed.
setunits datafile units=!
By specifying a null value (!), this example erases any previous value
of the UNITS component in the NDF structure datafile. The pixel values
are not changed.
setunits ndf=spect units="MJy" modify
Sets the UNITS component of the NDF structure spect to have the value
"MJy". If possible, the pixel values are changed from their old units
to the new units. For instance, if the UNITS component of the NDF was
original "J/(m**2*s*GHz)", the DATA values will be multiplied by
1.0E11, and the variance values by 1.0E22. However, if the original
units component was (say) "K" (Kelvin) then an error would be reported
since there is no direct conversion from Kelvin to MegaJansky.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: AXUNITS, SETLABEL, SETTITLE.


Copyright
~~~~~~~~~
Copyright (C) 1990 Science & Engineering Research Council. Copyright
(C) 1995, 2003-2004 Central Laboratory of the Research Councils. All
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


