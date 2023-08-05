

IRCAM2NDF
=========


Purpose
~~~~~~~
Converts an IRCAM data file to a series of NDFs


Description
~~~~~~~~~~~
This applications converts an HDS file in the IRCAM format listed in
IRCAM User Note 11 to one or more NDFs. See the Notes for a detailed
list of the rules of the conversion.


Usage
~~~~~


::

    
       ircam2ndf in prefix obs [config]
       



ADAM parameters
~~~~~~~~~~~~~~~



CONFIG = LITERAL (Read)
```````````````````````
The choice of data array to place in the NDF. It can have one of the
following configuration values: "STARE" --- the image of the object or
sky; "CHOP" --- the chopped image of the sky; "KTCSTARE" --- the
electronic pedestal or bias associated with the stare image of the
object or sky; "KTCCHOP" --- the electronic pedestal or bias
associated with the chopped image of the sky. Note that at the time of
writing chopping has not been implemented for IRCAM. For practical
purposes CONFIG="STARE" should be used. The suggested default is the
current value. ["STARE"]



FMTCNV = _LOGICAL (Read)
````````````````````````
This specifies whether or not format conversion may occur. If FMTCNV
is FALSE, the data type of the data array in the NDF will be the same
as that in the IRCAM file, and there is no scale factor and offset
applied. If FMTCNV is TRUE, whenever the IRCAM observation has non-
null scale and offset values, the observation data array will be
converted to type _REAL in the NDF, and the scale and offset applied
to the input data values to give the `true' data values. A null scale
factor is 1 and a null offset is 0. [FALSE]



IN = IRCAM (Read)
`````````````````
The name of the input IRCAM file to convert to NDFs. The suggested
value is the current value.



OBS() = LITERAL (Read)
``````````````````````
A list of the observation numbers to be converted into NDFs.
Observations are numbered consecutively from 1 up to the actual number
of observations in the IRCAM file. Single observations or a set of
adjacent observations may be specified, e.g. entering [4,6-9,12,14-16]
will read observations 4,6,7,8,9,12,14,15,16. (Note that the brackets
are required to distinguish this array of characters from a single
string including commas. The brackets are unnecessary when there is
only one item.)
If you wish to extract all the observations enter the wildcard *. 5-*
will read from 5 to the last observation. The processing will continue
until the last observation is converted. The suggested value is the
current value.



PREFIX = LITERAL (Read)
```````````````````````
The prefix of the output NDFs. The name of an NDF is the prefix
followed by the observation number. The suggested value is the current
value.



Examples
~~~~~~~~
ircam2ndf ircam_27aug89_1cl rhooph obs=*
This converts the IRCAM data file called ircam_27aug89_1cl into a
series of NDFs called rhooph1, rhooph2 etc. There is no format
conversion applied.
ircam2ndf ircam_27aug89_1cl rhooph [32,34-36] fmtcnv
This converts four observations in the IRCAM data file called
ircam_27aug89_1cl into NDFs called rhooph32, rhooph34, rhooph35,
rhooph36. The scale and offset are applied.
ircam2ndf in=ircam_04nov90_1c config="KTC" obs=5 prefix=bias
This converts the fifth observation in the IRCAM data file called
ircam_04nov90_1c into an NDF called bias5 containing the electronic
pedestal in its data array. There is no format conversion applied.



Notes
~~~~~


+ The rules for the conversion of the various components are as
follows:
_________________________________________________________________
IRCAM file NDF
+ ----------------------------------------------------------------
  .OBS.PHASEA.DATA_ARRAY -> .DATA_ARRAY when Parameter CONFIG="STARE"
  .OBS.PHASEB.DATA_ARRAY -> .DATA_ARRAY when Parameter CONFIG="CHOP"
  .OBS.KTCA.DATA_ARRAY -> .DATA_ARRAY when Parameter CONFIG="KTCSTARE"
  .OBS.KTCB.DATA_ARRAY -> .DATA_ARRAY when Parameter CONFIG="KTCCHOP"

.OBS.DATA_LABEL -> .LABEL .OBS.DATA_UNITS -> .UNITS .OBS.TITLE ->
.TITLE If .OBS.TITLE is a blank string, OBS.DATA_OBJECT is copied to
the NDF title instead.
.OBS.AXIS1_LABEL -> .AXIS(1).LABEL .OBS.AXIS2_LABEL -> .AXIS(2).LABEL
.OBS.AXIS1_UNITS -> .AXIS(1).UNITS .OBS.AXIS2_UNITS -> .AXIS(2).UNITS
.GENERAL.INSTRUMENT.PLATE_SCALE becomes the increment between the axis
centres, with co-ordinate (0.0,0.0) located at the image centre. The
NDF axis units both become "arcseconds".
.GENERAL -> .MORE.IRCAM.GENERAL .GENERAL.x -> .MORE.IRCAM.GENERAL.x
.GENERAL.x.y -> .MORE.IRCAM.GENERAL.x.y
.OBS.x -> .MORE.IRCAM.OBS.x This excludes the components of OBS
already listed above and DATA_BLANK.


+ The data types of the IRCAM GENERAL structures have not been
propagated to the NDF IRCAM extensions, because it would violate the
rules of SGP/38. In the IRCAM file these all have the same type
STRUCTURE. The new data types are as follows:
_________________________________________________________________
Extension Name Data type
+ ----------------------------------------------------------------
IRCAM.GENERAL IRCAM_GENERAL IRCAM.GENERAL.INSTRUMENT IRCAM_INSTRUM
IRCAM.GENERAL.ID IRCAM_ID IRCAM.GENERAL.TELESCOPE IRCAM_TELESCOPE
+ Upon completion the number of observations successfully converted to
  NDFs is reported.

Bad-pixel Handling: Elements of the data array equal to the IRCAM
component .OBS.DATA_BLANK are replaced by the standard bad value.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 2004 Central Laboratory of the Research Councils. Copyright (C)
2008 Science & Technology Facilities Council. All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ The data array in the NDF is in the primitive form.
+ The application aborts if the data array chosen by parameter CONFIG
  does not exist in the observation.




