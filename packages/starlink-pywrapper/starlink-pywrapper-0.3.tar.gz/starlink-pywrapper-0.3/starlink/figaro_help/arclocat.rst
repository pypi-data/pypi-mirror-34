

ARCLOCAT
========


Purpose
~~~~~~~
Locate line features in a set of spectra


Description
~~~~~~~~~~~
This routine locates narrow features in a set of spectra. Features can
be located from scratch automatically. In a different mode, feature
locations can be added or deleted in a graphical dialogue. The feature
location and peak are determined by a Gauss or triangle line fit.
The input data must be a base NDF. They can be a single spectrum or a
set of spectra. Examples for the latter are a long slit spectrum, a
set of extracted fibre spectra, or a collapsed echellogram (a set of
extracted orders from an echelle spectrograph). It is necessary that
the spectroscopic axis be the first axis in the data set. It does not
matter how many further axes there are, the data will be treated as a
set of rows with each row a spectrum.
The coverage in spectroscopic values of all spectra (rows) should
either be similar (long slit or fibres) or roughly adjacent
(echellogram). There must not yet be any spectroscopic value
information: There must be no array of spectroscopic values or widths
in the Specdre Extension. The pixel centre array for the spectroscopic
axis (i.e. the first axis) must be NDF pixel coordinates (usually 0.5,
1.5, ...). The data must be arranged such that spectroscopic values
increase left to right. In the case of rows with adjacent coverage
spectroscopic values must also increase with row number. In a
collapsed echellogram this usually means that for wavelength
calibration the order number must decrease with increasing row number.
In automatic mode this routine works on each row (spectrum) in turn.
It scans through the spectrum and looks for pixels that exceed the
local background level by at least the given threshold value. When
such a pixel is spotted, a single-component line fit is tried no the
local profile. The local profile is centred on the pixel suspected to
be part of an emission feature. It includes 1.5 times the guessed FWHM
on either side and a further 5 baseline pixels on either side. A local
linear baseline is subtracted prior to the line fit. In order for the
feature to be entered into the list of located features, the fit must
succeed, the fitted peak must exceed the threshold, and the fitted
peak must exceed the absolute difference of background levels between
the left and right.
When run with graphics dialogue this routine works on any choice of
rows. It uses a pre-existing list of located features to which can be
added or from which features can be deleted. Graphics dialogue can
also be used to just check the locations. The graph displays the
spectrum currently worked on in bin-style. The current list of located
features is indicated by dashed vertical lines. The options in the
graphical dialogue are: R - Choose different row to work on X - X-zoom
2x on cursor Y - Y-zoom 2x on cursor W - Unzoom to show whole row N -
Pan left/right by 75% of current x range A - Add the feature under
cursor to list (subject to line fit) S - Add the cursor position as
feature to list D - Delete the feature nearest cursor from list Q -
Quit, preserving the updated list of located features ? - Help
The difference between the A and S options is that A tries a line fit
to the local profile around the cursor, while S accepts the cursor x
position as exact centre and the cursor y position as exact peak of a
new feature; (the variance of the centre is set to 0.25, the variance
of the peak to the bad value).
The result of this routine is a list of Gauss or triangle features.
Their locations in NDF pixel coordinates and their peak values are
stored in the results structure of the Specdre Extension of the input
data. If run in automatic mode, this routine will replace any
previously existing results structure. If run with graphics dialogue,
this routine will try to work with a pre-existing list of located
features. But if the pre-existing results structure does not conform
to the required format, then a new results structure is created.
The list of located features (for each row) is always sorted such that
the locations are strictly monotonically increasing.
The results structure provides for a certain number of components.
These have component type 'Gauss feature' or 'triangle feature'. Each
component has two parameters 'centre' and 'peak'. The number of
components is determined when the results structure is created, it is
derived from the approximate width of features and the number of
pixels in each spectrum.


Usage
~~~~~


::

    
       arclocat in fwhm thresh
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If true, messages about the progress of auto-locating features are
issued. [YES]



DIALOG = _CHAR (Read)
`````````````````````
If this is 'Y', 'T' or 'G', then no auto-locating takes place and the
graphics dialogue is entered. If this is 'N' or 'F' then the dialogue
is not entered and auto-locating is done instead. The string is case-
insensitive. ['G']



MODE = _CHAR (Read)
```````````````````
This can be 'Gauss' or 'triangle' and chooses the line profile to be
fitted. This string is case-insensitive and can be abbreviated to one
character. ['Gauss']



IN = NDF (Read)
```````````````
The spectrum or set of spectra in which emission features are to be
located. This must be a base NDF, the spectroscopic axis must be the
first axis. No spectroscopic values or widths must exist in the
Specdre Extension. The pixel centres along the first axis must be NDF
pixel coordinates. Update access is necessary, the results structure
in the Specdre Extension will be modified, possibly re-created.



FWHM = _REAL (Read)
```````````````````
The guessed full width at half maximum of the features to be located.
This is used to estimate the maximum number of features that might be
located, to locate baseline ranges next to suspected features, and as
a guess for the line fit.



THRESH = _REAL (Read)
`````````````````````
The threshold. While scanning a pixel must exceed this threshold to
initiate a line fit. The fitted peak also must exceed the threshold in
order that the feature location be accepted. This parameter is
significant only for automatic location of features.



DEVICE = GRAPHICS (Read)
````````````````````````
The graphics device to be used. This is unused if DIALOG is false.



ROWNUM = _INTEGER (Read)
````````````````````````
In graphics dialogue this parameter is used to switch to a different
row (spectrum).



Examples
~~~~~~~~
arclocat in 4. 20. mode=triangle dialog=f
This will scan through (all rows of) the NDF called "in". It looks out
for features of 4 pixels full width at half maximum and with a peak
value of at least 20 above the local background. The features are
fitted as triangles. The search is automatic. Thus a new results
structure in the input NDF's Specdre Extension is created with the
locations (centres) and peaks of located features.
arclocat in 4. mode=Gauss dialog=g rownum=5
This will use the graphic dialogue. Starting with the fifth row the
user can use the mouse cursor to choose features that are to be
deleted from or added to the list of located features. This can be
used to improve on an automatic run, or when no features have been
located so far. If you try to add a feature to the list, a Gauss fit
is tried in the vicinity of the cursor-selected position.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.
This routine works in situ and modifies the input file.


