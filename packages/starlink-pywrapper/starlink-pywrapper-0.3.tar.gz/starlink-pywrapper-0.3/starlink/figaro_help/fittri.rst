

FITTRI
======


Purpose
~~~~~~~
Fit triangular profiles to a spectrum


Description
~~~~~~~~~~~
This routine fits up to six triangular profiles at a time to a one-
dimensional data set. This can be specified as an NDF section. The
data set must extend along the spectroscopic axis.
After accessing the data and the (optional) plot device, the data will
be subjected to a mask that consists of up to six abscissa intervals.
These may or may not overlap and need not lie within the range of
existing data. The masking will remove data which are bad, have bad
variance or have zero variance. The masking will also provide weights
for the fit. If the given data have no variances attached, or if the
variances are to be ignored, all weights will be equal.
After the data have been masked, guessed values for the fit are
required. These are

+ the number of components to be fitted,
+ the value of any underlying constant continuum (this must be an
a-priori known constant),
+ the components' guessed centre positions,
+ peak heights and
+ full widths at half maxima. Finally,
+ fit flags for each of the triangle parameters are needed.

The fit flags specify whether any parameter is fixed, fitted, or kept
at a constant ratio or offset to another fitted parameter.
The masked data and parameter guesses are then fed into the fit
routine. Single or multiple triangle fits are made to line features.
Triangle fit parameters may be free, fixed, or tied to the
corresponding parameter of another triangle component fitted at the
same time. Peak and width are tied by fixing the ratios, the centre is
tied by fixing the offset. Up to six triangle components can be fitted
simultaneously.
The fit is done by minimising chi-squared (or rms if variances are
unavailable or are chosen to be ignored). The covariances between fit
parameters - and among these the uncertainties of parameters - are
estimated from the curvature of psi-squared. psi-squared is usually
the same as chi-squared. If, however, the given data are not
independent measurements, a slightly modified function psi-squared
should be used, because the curvature of chi-squared gives an
overoptimistic estimate of the fit parameter uncertainty. In that
function the variances of the given measurements are substituted by
the sums over each row of the covariance matrix of the given data. If
the data have been resampled with a Specdre routine, that routine will
have stored the necessary additional information in the Specdre
Extension, and this routine will automatically use that information to
assess the fit parameter uncertainties. A full account of the psi-
squared function is given in Meyerdierks, 1992a/b. But note that these
covariance row sums are ignored if the main variance is ignored or
unavailable.
If the fit is successful, then the result is reported to the standard
output device and plotted on the graphics device. The final plot
viewport is saved in the AGI data base and can be used by further
applications.
The result is stored in the Specdre Extension of the input NDF.
Optionally, the complete description (input NDF name, mask used,
result, etc.) is written (appended) to an ASCII log file.
Optionally, the application can interact with the user. In that case,
a plot is provided before masking, before guessing and before fitting.
After masking, guessing and fitting, a screen report and a plot are
provided and the user can improve the parameters. Finally, the result
can be accepted or rejected, that is, the user can decide whether to
store the result in the Specdre Extension or not.
The screen plot consists of two viewports. The lower one shows the
data values (full-drawn bin-style) overlaid with the guess or fit
(dashed line-style). The upper box shows the residuals (cross marks)
and error bars. The axis scales are arranged such that all masked data
can be displayed. The upper box displays a zero-line for reference,
which also indicates the mask.
The Extension provides space to store fit results for each non-
spectroscopic coordinate. Say, if you have a 2-D image each row being
a spectrum, then you can store results for each row. The whole set of
results can be filled successively by fitting one row at a time and
always using the same component number to store the results for that
row. (See also the example.)
The components fitted by this routine are specified as follows: The
line names and laboratory frequencies are the default values and are
not checked against any existing information in the input's Specdre
Extension. The component types are 'triangle'. The numbers of
parameters allocated to each component are 4, the three guessed and
fitted parameters and the line integral. The parameter types are in
order of appearance: 'centre', 'peak', 'FWHM', 'integral'.


Usage
~~~~~


::

    
       fittri in device=? mask1=? mask2=?
          ncomp=? cont=? centre=? peak=? fwhm=? cf=? pf=? wf=?
          comp=? logfil=?
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, this routine will issue only error messages and no
informational message. [YES]



VARUSE = _LOGICAL (Read)
````````````````````````
If false, input variances are ignored. [YES]



DIALOG = _CHAR (Read)
`````````````````````
If 'T', the routine offers in general more options for interaction.
The mask or guess can be improved after inspections of a plot. Also,
the routine can resolve uncertainties about where to store results by
consulting the user. ['T']



IN = NDF (Read)
```````````````
The input NDF. This must be a one-dimensional (section of an) NDF. You
can specify e.g. an image column as IN(5,) or part of an image row as
IN(2.2:3.3,10). Update access is necessary to store the fit result in
the NDF's Specdre Extension.



REPAIR = _LOGICAL (Read)
````````````````````````
If DIALOG is true, REPAIR can be set true in order to change the
spectroscopic number axis in the Specdre Extension. [NO]



DEVICE = DEVICE (Read)
``````````````````````
The name of the plot device. Enter the null value (!) to disable
plotting. [!]



MASK1( 6 ) = _REAL (Read)
`````````````````````````
Lower bounds of mask intervals. The mask is the part(s) of the
spectrum that is (are) fitted and plotted. The mask is put together
from up to six intervals:
mask = [MASK1(1);MASK2(1)] U [MASK1(2);MASK1(2)] U ... U
[MASK1(MSKUSE);MASK2(MSKUSE)].
The elements of the MASK parameters are not checked for monotony. Thus
intervals may be empty or overlapping. The number of intervals to be
used is derived from the number of lower/upper bounds entered. Either
MASK1 or MASK2 should be entered with not more numbers than mask
intervals required.



MASK2( 6 ) = _REAL (Read)
`````````````````````````
Upper bounds of mask intervals. See MASK1.



NCOMP = _INTEGER (Read)
```````````````````````
The number of triangle profiles to be fitted. Must be between 1 and 6.
[1]



CONT = _REAL (Read)
```````````````````
This value indicates the level of the continuum. Any constant value
for CONT is acceptable. [0]



CENTRE( 6 ) = _REAL (Read)
``````````````````````````
Guess centre position for each triangle component.



PEAK( 6 ) = _REAL (Read)
````````````````````````
Guess peak height for each triangle component.



FWHM( 6 ) = _REAL (Read)
````````````````````````
Guess full width at half maximum for each triangle component.



CF( 6 ) = _INTEGER (Read)
`````````````````````````
For each triangle component I, a value CF(I)=0 indicates that
CENTRE(I) holds a guess which is free to be fitted. A positive value
CF(I)=I indicates that CENTRE(I) is fixed. A positive value CF(I)=J<I
indicates that CENTRE(I) has to keep a fixed offset from CENTRE(J).



PF( 6 ) = _INTEGER (Read)
`````````````````````````
For each triangle component I, a value PF(I)=0 indicates that PEAK(I)
holds a guess which is free to be fitted. A positive value PF(I)=I
indicates that PEAK(I) is fixed. A positive value PF(I)=J<I indicates
that PEAK(I) has to keep a fixed ratio to PEAK(J).



WF( 6 ) = _INTEGER (Read)
`````````````````````````
For each triangle component I, a value WF(I)=0 indicates that FWHM(I)
holds a guess which is free to be fitted. A positive value WF(I)=I
indicates that FWHM(I) is fixed. A positive value WF(I)=J<I indicates
that FWHM(I) has to keep a fixed ratio to FWHM(J).



REMASK = _LOGICAL (Read)
````````````````````````
Reply YES to have another chance for improving the mask. [NO]



REGUESS = _LOGICAL (Read)
`````````````````````````
Reply YES to have another chance for improving the guess and fit. [NO]



FITGOOD = _LOGICAL (Read)
`````````````````````````
Reply YES to store the result in the Specdre Extension. [YES]



COMP = _INTEGER (Read)
``````````````````````
The results are stored in the Specdre Extension of the data. This
parameter specifies which existing components are being fitted. You
should give NCOMP values, which should all be different and which
should be between zero and the number of components that are currently
stored in the Extension. Give a zero for a hitherto unknown component.
If a COMP element is given as zero or if it specifies a component
unfit to store the results of this routine, then a new component will
be created in the result storage structure. In any case this routine
will report which components were actually used and it will deposit
the updated values in the parameter system. [1,2,3,4,5,6]



LOGFIL = FILENAME (Read)
````````````````````````
The file name of the log file. Enter the null value (!) to disable
logging. The log file is opened for append. [!]



Examples
~~~~~~~~
fittri in device=xw mask1=-1.5 mask2=2.5
ncomp=1 cont=1.0 centre=0.5 peak=-0.5 fwhm=1.5 cf=0 pf=0 wf=0 comp=1
logfil=line This fits a single triangular profile to the x range
[-1.5,2.5]. The continuum is assumed to be constant at 1.0. The
triangle is guessed to be centred at 0.5 with width 1.5. It is guessed
to be an absorption line with an amplitude of -0.5. All triangle
parameters are free to be fitted. The fit result is reported to the
text file LINE and stored as component number 1 in the input file's
Specdre Extension. Since DIALOG is not turned off, the user will be
prompted for improvements of the mask and guess, and will be asked
whether the final fit result is to be accepted (stored in the
Extension and written to LINE.DAT). The XWINDOWS graphics device will
display the spectrum before masking, guessing, and fitting.
Independent of the DIALOG switch, a plot is produced after fitting.
fittri in(,5) device=! mask1=-1.5 mask2=2.5
ncomp=1 cont=0.0 centre=0.5 peak=13.0 fwhm=1.5 cf=0 pf=0 wf=1 comp=0
logfil=! dialog=f This fits a single triangular profile to the x range
[-1.5,2.5] of the 5th row in the 2-D image IN. The baseline is assumed
to be constant at 0.0. The triangle is guessed to be centred at 0.5
with width 1.5. It is guessed to be an emission line with an amplitude
of 13. Centre position and peak height are free to be fitted, but the
width is fixed to 1.5. User interaction (DIALOG) and plotting (DEVICE)
are de-selected. There is also no log file where to the results are
written. If INFO were also switched off, no report whatsoever would be
made. However, the results are stored as a new component (COMP=0) in
the Specdre Extension of the input file.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.
This routine works in situ and modifies the input file.


References
~~~~~~~~~~
Meyerdierks, H., 1992a, Covariance in resampling and model fitting,
Starlink, Spectroscopy Special Interest Group
Meyerdierks, H., 1992b, Fitting resampled spectra, in P.J. Grosbol,
R.C.E. de Ruijsscher (eds), 4th ESO/ST-ECF Data Analysis Workshop,
Garching, 13 - 14 May 1992, ESO Conference and Workshop Proceedings
No. 41, Garching bei Muenchen, 1992


