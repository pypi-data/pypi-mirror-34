

ARCIDENT
========


Purpose
~~~~~~~
Auto-identify located features


Description
~~~~~~~~~~~
This routine identifies located features in a set of spectra. Auto-
identification is done from scratch (without prior identification of
any features) with the algorithm by Mills (1992).
The input data must be a base NDF. They can be a single spectrum or a
set of spectra. Examples for the latter are a long slit spectrum, a
set of extracted fibre spectra, or a collapsed echellogram (a set of
extracted orders from an echelle spectrograph). It is necessary that
the spectroscopic axis be the first axis in the data set. It does not
matter how many further axes there are, the data will be treated as a
linear set of rows with each row a spectrum.
The features for which an identification should be attempted must have
been located. That is, they must be components of type 'Gauss',
'triangle', 'Gauss feature' or 'triangle feature' in the results
structure of the Specdre Extension. Each of these components must have
at least a 'centre' and 'peak' parameter. The centres (feature
locations) must be a strictly monotonically increasing list. Their
variances must be available. The locations (centre parameters) must be
in terms of NDF pixel coordinates. The peaks must be positive. They
are used as a measure of the importance of a feature.
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
If this is not the case then it is still possible to work on a
collapsed echellogram: You can set ECHELLE false and thus use the full
WRANGE for each row, but you must adjust DRANGE to be a more
reasonable guess of the dispersion.
Identification is done by comparison with a feature data base
according to Mills (1992). The feature data base should to some degree
match the observation. Its spectral extent should be wider than that
of the observation. But it should not contain a significant number of
features that are not located. This is because the automatic
identification algorithm uses relative distances between neighbouring
features. If most neighbours in the list of laboratory values are not
detected in the actual arc observation, then the algorithm may fail to
find a solution or may return the wrong solution.
This routine works on each row (spectrum) in turn. It establishes
information about relative distances between neighbouring located
features and compares this with a feature data base. This serves to
identify at least a specified number of features. An auto-
identification should always be checked in the process of fitting a
polynomial dispersion curve. All located features are retained by this
routine, so that further identifications can be added or some
identifications can be cancelled.
The result of this routine is a list of feature identifications. All
located features are retained, though some will have not been
identified. The locations and identifications (pixel coordinates and
laboratory values) are stored in the results structure of the Specdre
Extension of the input data. This replaces the pre-existing results
extension. The locations are strictly monotonically increasing, as are
in all probability the identifications.
The new results structure provides for as many component as the old
one had components of any recognised type. Each component has on
output the type 'arc feature'. It has two parameters 'centre' and
'laboratory value'. Located but unidentified features will have bad
values as laboratory values. The variances of laboratory values are
set to zero.
Mills's (1992) algorithm performs only an initial line identification.
It is important to verify the returned values by fitting a wavelength
or frequency scale (e.g. polynomial or spline fit), and to reject any
out-liers. The algorithm should be given the positions of all
conceivable features in the spectra. It does not use the fainter ones
unless it is unable to identify using only the brightest, but you will
get more robust behaviour if you always provide all possible candidate
lines for potential identification. The algorithm should not be fed
severely blended line positions as the chance of incorrect
identifications will be significantly higher (this is the exception to
the rule above).
The speed of the algorithm varies approximately linearly with
wavelength/frequency range and also with dispersion range so the
better constraints you provide the faster it will run. The algorithm
takes your constraints as hard limits and it is usually more robust to
accept a slightly longer runtime by relaxing the ranges a little.
If the algorithm runs and keeps looping increasing its set of
neighbours, then the most likely causes are as follows:

+ wavelength/frequency scale does not increase with increasing x (set
the CHKRVS parameter true and try again).
+ WRANGE or DRANGE are too small (increase them both by a factor of 2
  and try again).




Usage
~~~~~


::

    
       arcident in out fdb wrange=?
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, the routine will issue only error messages and no
informational messages. [YES]



ECHELLE = _LOGICAL (Read)
`````````````````````````
If false, the given WRANGE is used for each row, assuming the rows are
similar spectra (long slit or fibre). If true, a collapsed echellogram
is assumed. In that case each row is an extracted order with different
wavelength/frequency range. This routine will divide the given WRANGE
into as many sub-ranges as there are rows (orders) in the given input.
[NO]



IN = NDF (Read)
```````````````
The spectrum or set of spectra in which located features are to be
identified. This must be a base NDF, the spectroscopic axis must be
the first axis. No spectroscopic values or widths must exist in the
Specdre Extension. The pixel centres along the first axis must be NDF
pixel coordinates. The input NDF must have a results structure in its
Specdre Extension, and the results must contain a number of line
components with strictly monotonically increasing position (centre).



OUT = NDF (Read)
````````````````
The output NDF is a copy of the input, except that the results
structure holds feature identifications rather than locations ('peak'
parameters will have been replaced with 'laboratory value'
parameters).



FDB = NDF (Read)
````````````````
The feature data base. The actual data base is a set of primitive
arrays in an extension to this NDF called ECHELLE. A feature data base
can be generated from a list of wavelengths or frequencies with
ARCGENDB.



WRANGE( 2 ) = _REAL (Read)
``````````````````````````
The approximate range of wavelengths or frequencies. The narrower this
range the faster is the identification algorithm. But if in doubt give
a wider range.



DRANGE( 2 ) = _REAL (Read)
``````````````````````````
The range into which the dispersion in pixels per wavelength or per
frequency falls. The narrower this range the faster is the
identification algorithm. But if in doubt give a wider range.



STRENGTH = _REAL (Read)
```````````````````````
This specifies the maximum ratio between the strength of features that
are to be used initially for identification. If the strongest feature
has peak 1000, then the weakest feature used initially has peak
greater than 1000/STRENGTH. [50.0]



THRESH = _REAL (Read)
`````````````````````
This specifies the maximum difference between the ratios of neighbour
distances as observed and as found in the feature data base. The
difference is evaluated as ABS(1 - ABS(obs/ref)) <? THRESH. Values
much larger than 0.1 are likely to generate a lot of coincidence
matches; values less than 0.01 may well miss 'good' matches in less-
than-ideal data. You may need to relax this parameter if your arc
spectra are very distorted (non-linear dispersion). [0.03]



MAXLOC = _INTEGER (Read)
````````````````````````
This specifies the maximum number of features to be used when
generating ratios for initial identification. In general, a good
solution can be found using only the strongest 8 to 16 features. The
program slowly increases the number of features it uses until an
adequate solution if found. However, there may be a large numbers of
weak features present which are not in the reference database. This
parameter allows the setting of an absolute maximum on the number of
features (per row) which are to be considered. If less than MAXLOC
features are located in a given row, then the number of identified
features is used instead for that row. [30]



MINIDS = _INTEGER (Read)
````````````````````````
The minimum number of features that must be identified for the
algorithm to be successful. If fewer than MINIDS features are located
in a given row, then a smaller number is used instead for that row.
[9]



NEIGHB( 2 ) = _INTEGER (Read)
`````````````````````````````
NEIGHB(1) specifies the starting number of neighbouring features (on
each side) to examine when generating ratios for matching. (These are
neighbours in the observed spectra, not in the feature data base.)
Increasing this will lead to exponential increases in CPU time, so it
should be used with caution when all else fails. The default value is
3. Higher values are tried automatically by the program if no solution
can be found. The number of neighbours considered is increased until
it reaches the maximum of NEIGHB(2), when the program gives up. [3,6]



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.


References
~~~~~~~~~~
Mills, D., 1992, Automatic ARC wavelength calibration, in P.J.
Grosbol, R.C.E. de Ruijsscher (eds), 4th ESO/ST-ECF Data Analysis
Workshop, Garching, 13 - 14 May 1992, ESO Conference and Workshop
Proceedings No. 41, Garching bei Muenchen, 1992


