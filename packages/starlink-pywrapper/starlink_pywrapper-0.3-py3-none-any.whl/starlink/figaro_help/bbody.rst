

BBODY
=====


Purpose
~~~~~~~
Calculate a black body spectrum


Description
~~~~~~~~~~~
This routine calculates for a given (vacuum) wavelength or frequency
axis the intensity of a black body at given temperature. The intensity
is the energy per unit time, per unit area, per unit solid angle, and
per unit frequency (and for all polarisations):
2 h nu^3 1 B_nu = ---------- ------------------ c^2 exp(h nu/kT) - 1
where c is the velocity of light, and h and k are the Planck and
Boltzmann constants.


Usage
~~~~~


::

    
       bbody temp in=? xstart=? xstep=? xend=? xlabel=? xunit=? out=?
       



ADAM parameters
~~~~~~~~~~~~~~~



LOGAR = LOGICAL (Read)
``````````````````````
True if the common logarithm of intensity is to be written rather than
the intensity itself. [NO]



TEMP = REAL (Read)
``````````````````
The black body temperature in Kelvin.



ERRTEMP = REAL (Read)
`````````````````````
The error in the black body temperature in Kelvin.



IN = NDF (Read)
```````````````
The file holding axis data to be used. Enter the null value (!) to
read axis data parameters from keyboard.



XSTART = REAL (Read)
````````````````````
The spectroscopic value (pixel centre) for the first output pixel.



XSTEP = REAL (Read)
```````````````````
The spectroscopic step (pixel distance) for the output pixels.



XEND = REAL (Read)
``````````````````
The spectroscopic value (pixel centre) for the last output pixel.



XLABEL = CHARACTER (Read)
`````````````````````````
The label for the spectroscopic axis. Allowed values are "wavelength"
and "frequency". [wavelength]



XUNIT = CHARACTER (Read)
````````````````````````
The unit for the spectroscopic axis. If the label is "wavelength" then
the unit can basically be "m" for metre, "um" or "micron" for
micrometre, or "Angstrom" for Angstroem. If the label is "frequency"
then the unit must be basically "Hz" for Hertz. Any of these units may
be preceded by a power of ten, so it could be "10**1*Angstrom" if you
want to use nanometre as unit, or "10**-9*m" to the same effect. The
power must be an integer. You can achieve a logarithmic axis by
specifying something like "log10(10**-3*micron)". In this example the
axis values will be the common logarithms of the wavelength in
nanometres.



OUT = NDF (Read)
````````````````
The output file.



Examples
~~~~~~~~
bbody 5500 in=in out=out
This calculates the black-body spectrum for 5500 K. The spectrum is
written to file OUT. The routine tries to find all necessary
information for the 1st (and only) axis in OUT from the spectroscopic
axis of the file IN. Since LOGAR is left at its default value of
FALSE, the data are intensity in Jy/sr.
bbody 2.7 logar=true in=! xstart=0 xstep=0.05 xend=6

xlabel=wavelength xunit=log(micron) out=out
This calculates the black-body spectrum for 2.7 K. The spectrum is
written to OUT. No input file is specified. The axis contains the
logarithms of wavelengths in micron, which run from 0 (1 micron) to 6
(1 metre). Since LOGAR=TRUE, the data are the logarithms of intensity
in Jy/sr.
bbody 1e6 logar=true in=! xstart=-1 xstep=0.05 xend=2

xlabel=frequency xunit=log10(10**15*Hz) out=out
This calculates the black-body spectrum for 1 million K. This time the
axis is logarithms of frequency, the units used are 10^15 Hz. The
frequency range covered is from 10^14 Hz to 10^17 Hz.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.


References
~~~~~~~~~~
Lang, K.R., 1980, Astrophysical Formulae, Springer, Heidelberg,
Berlin, New York, p. 21


