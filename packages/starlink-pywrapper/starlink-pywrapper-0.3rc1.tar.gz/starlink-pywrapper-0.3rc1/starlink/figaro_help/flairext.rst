

FLAIREXT
========


Purpose
~~~~~~~
Optimally extracts spectra from a FLAIR NDF to form a new NDF


Description
~~~~~~~~~~~
This application takes a FLAIR frame stored in an NDF with the
dispersion along the y axis, and extracts the individual spectra using
an optimal extraction. It stores the spectra in an output two-
dimensional NDF, configured such that the dispersion is along x axis,
and wavelength increases with pixel index, and each spectrum occupies
one line.
This assumes stability (x positions of the fibres do not move), and
vertical orientation of the fibres. These are satisfied by FLAIR
(Parker, private communication).


Usage
~~~~~


::

    
       flairext in profile out fibres
       



ADAM parameters
~~~~~~~~~~~~~~~



FIBRES = _INTEGER (Read)
````````````````````````
The number of fibres to extract. This must be in the range 1 to 92.
[92]



IN = NDF (Read)
```````````````
A list of the input two-dimensional NDFs containing FLAIR spectra to
be extracted.



PROFILE = NDF (Write)
`````````````````````
The vector of weights to use during optimal extraction, as derived
from FLAIRCOMP.



OUT = NDF (Write)
`````````````````
The list of the two-dimensional NDF containing the extracted FLAIR
spectra. There should be as many files in this list as for parameter
IN. The nth item in this list will be the extracted spectra for the
nth file in IN.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value (!) will cause the
title of the input NDF to be used. [!]



