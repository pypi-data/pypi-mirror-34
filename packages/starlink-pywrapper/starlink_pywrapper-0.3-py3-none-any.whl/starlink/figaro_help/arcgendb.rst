

ARCGENDB
========


Purpose
~~~~~~~
Convert list of laboratory values to feature data base


Description
~~~~~~~~~~~
This routine converts an arc line list - i.e. an ASCII list of
laboratory wavelengths or frequencies of known features in an arc
spectrum - into a feature data base. That can be used for automatic
identification of features in an observed arc spectrum.
Since generating the feature data base may take some time, you may
want to do it once for any line lists you often use, and keep the
feature data bases. On the other hand, the feature data bases may be
rather big.
This routine reads a list of laboratory values (wavelengths or
frequencies). The list must be an unformatted ASCII file. From the
beginning of each line one value is read. If this fails, the line is
ignored. Comment lines can be inserted by prefixing them with "*", "!"
or "#". The value can be followed by any comment, but can be preceded
only by blanks. The list must be strictly monotonically increasing.
The list should to some degree match an expected observation. Its
spectral extent should be wider than that of an expected observation.
But it should not contain a significant number of features that are
usually not detected. This is because the automatic identification
algorithm uses relative distances between neighbouring features. If
most neighbours in the list of laboratory values are not detected in
the actual arc observation, then the algorithm may fail to find a
solution or may return the wrong solution.
The given list is converted to a feature data base according to Mills
(1992). The data base contains information about the distances between
neighbours of features. The scope of the feature data base is the
number of neighbours about which information is stored. The feature
data base is stored in an extension to a dummy NDF. The NDF itself has
only the obligatory data array. The data array is one-dimensional with
1 pixel. All the actual information is in an extension with the name
"ECHELLE" and of type "ECH_FTRDB". Its HDS components are:


+ FTR_WAVE(NLINES) <_REAL>
+ FTR_DB(10,10,NLINES) <_REAL>
+ FTR_LEFT(10,10,NLINES) <_BYTE>
+ FTR_RIGHT(10,10,NLINES) <_BYTE>
+ WAVE_INDEX(10,10,NLINES) <_UWORD>
+ QUICK_INDEX(5000) <_INTEGER>
+ QENTRIES(5000) <_REAL>

NLINES is the number of features listed in the input file. The scope
(=10) controls about how many neighbours information is stored in the
data base. The index size is fixed to 5000, which seems sufficient for
NLINES = 3500. The size of the FDB is
(804 * NLINES + 40000) bytes
plus a small overhead for the HDS structure and the nominal NDF. So it
is 10 to 100 times bigger than the original ASCII list. The point
about the FDB is the reduced computing time when auto-identifying
features in an observed arc spectrum.


Usage
~~~~~


::

    
       arcgendb in fdb
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If true, informational messages will be issued.



IN = FILENAME (Read)
````````````````````
The name of the input ASCII list of wavelengths or frequencies. The
list must be strictly monotonically increasing.



FDB = NDF (Read)
````````````````
The name of the output file to hold the feature data base. This is
formally an NDF.



Examples
~~~~~~~~
arcgendb $FIGARO_PROG_S/thar.arc thar_arc
This will convert the Th-Ar list from the Figaro release into a
"feature data base" by the name of "thar_arc.sdf".



References
~~~~~~~~~~
Mills, D., 1992, Automatic ARC wavelength calibration, in P.J.
Grosbol, R.C.E. de Ruijsscher (eds), 4th ESO/ST-ECF Data Analysis
Workshop, Garching, 13 - 14 May 1992, ESO Conference and Workshop
Proceedings No. 41, Garching bei Muenchen, 1992


