

FLAIRCOMP
=========


Purpose
~~~~~~~
Compresses a FLAIR frame to give a weight vector


Description
~~~~~~~~~~~
This application takes a FLAIR frame stored in an NDF and compresses
it along the y axis, normalises the compressed array by its mean
value, and then finds the minima in the values and set these to the
bad value. Thus it provides the weights for an optimal extraction. It
reports the number of fibres found in the NDF.
This assumes stability (x positions of the fibres do not move), and
vertical orientation of the fibres. These are satisfied by FLAIR
(Parker, private communication).


Usage
~~~~~


::

    
       flaircomp in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = NDF (Read)
```````````````
The input two-dimensional NDF. This should be the co-added arc or sky
flat-field frames, so that the compressed array gives the instrumental
response of the detector system.



OUT = NDF (Write)
`````````````````
The vector of weights to use during optimal extraction.



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null (!) propagates the title
from input NDF to the output. [!]



