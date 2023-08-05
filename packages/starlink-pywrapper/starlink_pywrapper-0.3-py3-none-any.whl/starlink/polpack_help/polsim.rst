

POLSIM
======


Purpose
~~~~~~~
Produces intensity data corresponding to given Stokes vectors


Description
~~~~~~~~~~~
This application produces intensity data (either 2D images or 3D
cubes) corresponding to given Stokes vectors. A set of template input
intensity images or cubes are supplied which define the pixel
positions, analyser angles, efficiencies, transmissions, etc. The
pixel values supplied in these templates are ignored. A set of
corresponding output intensity images or cubes are created which
inherit the properties of the input NDFs. The pixel values in these
images are calculated using the supplied Stokes vectors, using the
analyser properties defined in the input images.


Usage
~~~~~


::

    
       polsim cube in out
       



ADAM parameters
~~~~~~~~~~~~~~~



CUBE = NDF (Read)
`````````````````
The name of the input NDF holding the Stokes parameters, such as
produced by POLCAL.



IN = NDF (Read)
```````````````
A group specifying the names of the input intensity NDFs. This may
take the form of a comma separated list, or any of the other forms
described in the help on "Group Expressions". These images must be
aligned pixel-for-pixel with the Stokes vectors given by CUBE.



OUT = NDF (Read)
````````````````
A group specifying the names of the output intensity NDFs.



Examples
~~~~~~~~
polsim cube "*_A" "*_sim"
A set of intensity images is created holding analysed intensities
derived from the Stokes vectors in file "cube". Each output image
inherits the pixel positions and analyser properties from a specified
input intensity image. All images in the current directory which have
file names ending with "_A" are used as the input template images, and
the output images containing simulated intensity values have the same
names, but with "_sim" appended.



Copyright
~~~~~~~~~
Copyright (C) 2009 Science & Technology Facilities Council. Copyright
(C) 1999, 2001 Central Laboratory of the Research Councils All Rights
Reserved.


