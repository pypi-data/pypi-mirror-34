

ARCDISP
=======


Purpose
~~~~~~~
Fit polynomial dispersion curve


Description
~~~~~~~~~~~
This routine fits a polynomial dispersion curve to a list of
identified arc features and transforms the NDF pixel coordinates to
spectroscopic values. Optionally you can use a graphical dialogue to
improve on the previous feature identification, until you like the
appearance of the dispersion curve.
The input data must be a base NDF. They can be a single spectrum or a
set of spectra. Examples for the latter are a long slit spectrum, a
set of extracted fibre spectra, or a collapsed echellogram (a set of
extracted orders from an echelle spectrograph). It is necessary that
the spectroscopic axis be the first axis in the data set. It does not
matter how many further axes there are, the data will be treated as a
linear set of rows with each row a spectrum.
The actual input is the results structure in the Specdre Extension.
This must be a set of components of type 'arc feature'. Each must have
two parameters 'centre' and 'laboratory value'. These must be
corresponding locations one expressed in NDF pixel coordinates, the
other in spectroscopic values (wavelength, frequency etc.). The
centres must be strictly monotonically increasing, their variances
must be available. Laboratory values may be bad values to signify
unidentified features.
In the graphical dialogue the results structure may be updated. The
locations remain unchanged; all located features form a fixed list of
potentially identified features. Identifications may be added, deleted
or modified. The user has to work on each row in turn (unless Quit is
chosen). When the user switches from one row to the next, the
dispersion curve for the finished row is applied and its spectroscopic
values in the Specdre Extension are set. When the last row is
finished, the application exits; the output of this routine is (i) an
updated list of identifications in the results structure of the
Specdre Extension and (ii) an array of spectroscopic values according
to the dispersion curves for each row, also in the Specdre Extension.
At any point the user can quit. In this case the array of
spectroscopic values is discarded, but the updated identifications are
retained. If run without dialogue, this routine simply performs the
polynomial fit of the dispersion curve for each row in turn and works
out the array of spectroscopic values. The list of identifications is
input only and remains unchanged. If for any row the fit cannot be
performed, then the spectroscopic values calculated so far are
discarded and the routine aborts.
There must not yet be any spectroscopic value information: There must
be no array of spectroscopic values or widths in the Specdre
Extension. The pixel centre array for the spectroscopic axis (i.e. the
first axis) must be NDF pixel coordinates (usually 0.5, 1.5, ...).
This routine works on each row (spectrum) in turn. It fits a
polynomial to the existing identifications. In the optional graphical
dialogue two plots are displayed and updated as necessary. The lower
panel is a plot of laboratory values (wavelength, frequency etc.)
versus pixel coordinate shows

+ all possible identifications from the feature data base as
horizontal lines,
+ all unidentified located features as vertical lines,
+ all identified located features as diagonal crosses,
+ the dispersion curve.

In the upper panel, a linear function is subtracted so that it
displays the higher-order components of the dispersion curve. Crosses
indicate the identified located features. Since the scale of this
upper panel is bigger, it can be used to spot outlying feature
identifications. In the dialogue you can R - Switch to next row,
accepting the current fit for this row X - X-zoom 2x on cursor Y -
Y-zoom 2x on cursor W - Unzoom to show whole row N - Pan by 75% of
current plot range A - Add ID for location nearest to cursor (from
FDB) S - Set ID for location nearest to cursor (from cursor y pos.) D
- Delete ID for feature nearest to cursor Q - Quit (preserves updated
IDs, discards applied fits for all rows) ? - Help
Whenever the list of identifications is changed, the dispersion curve
is fitted again and re-displayed. If there are too few identifications
for the order chosen, then the dialogue will display the maximum order
possible. But such an under-order fit cannot be accepted, the R option
will result in an error.
The Q option will always result in an error report, formally the
routine aborts. After all, it does not achieve the main goal of
applying individual dispersion curves to all rows.
On one hand the output of this routine may be an updated list of
identifications, which could in principle be used in a future run of
this routine. On the other hand this routine will always result in an
array of spectroscopic values. The existence of these spectroscopic
values prevents using this routine again. Before using this routine
again on the same input NDF you have to delete the SPECVALS component
in the Specdre Extension.
In order to facilitate repeated use of this routine on the same data,
it always uses the Specdre Extension to store spectroscopic values,
even if the data are one-dimensional and the first axis centre array
would suffice to hold that information. This leaves the first axis
centre array at NDF pixel coordinates, as necessary for re-use of this
routine.


Usage
~~~~~


::

    
       arcdisp in order
       



ADAM parameters
~~~~~~~~~~~~~~~



DIALOG = _CHAR (Read)
`````````````````````
If this is 'Y', 'T' or 'G', then the graphical dialogue is entered
before the polynomial dispersion curve for any row is accepted and
applied. If this is 'N' or 'F' then the dialogue is not entered and
separate dispersion curves are applied to all rows. The string is
case-insensitive. ['G']



IN = NDF (Read)
```````````````
The spectrum or set of spectra in which emission features are to be
located. This must be a base NDF, the spectroscopic axis must be the
first axis. No spectroscopic values or widths must exist in the
Specdre Extension. The pixel centres along the first axis must be NDF
pixel coordinates. Update access is necessary, the results structure
in the Specdre Extension may be modified, an array of spectroscopic
values will be created in the Specdre Extensions.



ORDER = _INTEGER (Read)
```````````````````````
The polynomial order of dispersion curves. This cannot be changed
during the graphical dialogue. Neither can it differ between rows. [2]



FDB = NDF (Read)
````````````````
The feature data base. Only the simple list of values FTR_WAVE is used
and only in graphics dialogue. It serves to find the identification
for an as yet unidentified - but located feature.



DEVICE = GRAPHICS (Read)
````````````````````````
The graphics device to be used. This is unused if DIALOG is false.



WRANGE( 2 ) = _REAL (Read)
``````````````````````````
In graphical dialogue this parameter is used repeatedly to get a range
of laboratory values. This is used for plotting as well as for finding
identifications in the feature data base.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.
This routine works in situ and modifies the input file.


