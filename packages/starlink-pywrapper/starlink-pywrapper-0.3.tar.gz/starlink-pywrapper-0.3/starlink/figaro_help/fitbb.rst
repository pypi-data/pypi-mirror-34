

FITBB
=====


Purpose
~~~~~~~
Fit diluted Planck curves to a spectrum


Description
~~~~~~~~~~~
This routine fits up to six diluted Planck curves to a one-dimensional
data set. This can be specified as an NDF section. The data set must
extend along the spectroscopic axis. The fit is done on a double
logarithmic representation of the data. The axis data must be the
common logarithm of frequency in Hertz. The data themselves must be
the common logarithm of intensity or flux density in arbitrary units.
A diluted Planck component is defined as 3 f_j Theta_j alpha_j nu 10 =
10 (nu/Hz) (2h/c^2) ------------------- exp(hnu/kT_j) - 1
This assumes that the optical depth is small and the emissivity is
proportional to the frequency to the power of alpha. 10^Theta is the
hypothetical optical depth at frequency 1 Hz.
If the optical depth is large, a single simple Planck function should
be fitted, i.e. only one component with alpha = 0. In this case
10^Theta is the conversion factor from the Planck function in Jy/sr to
the (linear) data values. If for example the data are the common
logarithm of the calibrated flux density of a source in Jy, then Theta
is the logarithm of the solid angle (in sr) subtended by the source.
The fit is performed in double logarithmic representation, i.e. the
fitted function is
f = lg[ sum_j 10^f_j ]
The choice of Theta, alpha and lg(T) as fit parameters is intuitive,
but makes the fit routine ill-behaved. Very often alpha cannot be
fitted at all and must be fixed. Theta and alpha usually anti-
correlate completely. Even with fixed alpha do Theta and lg(T) anti-
correlate strongly.
Furthermore, Theta is difficult to guess. From any initial guess of
Theta one can improve by using Theta plus the average deviation of the
data from the guessed spectrum.
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
+ the components' guessed scaling constants Theta,
+ emissivity exponents alpha and
+ common logarithms of colour temperatures in Kelvin. Finally,
+ fit flags for each of the parameters are needed.

The fit flags specify whether any parameter is fixed, fitted, or kept
at a constant offset to another fitted parameter.
The masked data and parameter guesses are then fed into the fit
routine. Single or multiple fits are made. Fit parameters may be free,
fixed, or tied to the corresponding parameter of another component
fitted at the same time. They are tied by fixing the offset, Up to six
components can be fitted simultaneously.
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
Extension. The component types are 'Planck'. The numbers of parameters
allocated to each component are 3, the three guessed and fitted
parameters. The parameter types are in order of appearance: 'Theta',
'alpha', 'lg(T)'.


Usage
~~~~~


::

    
       fitbb in device=? mask1=? mask2=?
          ncomp=? theta=? alpha=? lgtemp=? sf=? af=? tf=?
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
The number of Planck curves to be fitted. Must be between 1 and 6. [1]



THETA( 6 ) = _REAL (Read)
`````````````````````````
Guess scaling constant for each diluted Planck component.



ALPHA( 6 ) = _REAL (Read)
`````````````````````````
Guess emissivity exponent for each diluted Planck component.



LGTEMP( 6 ) = _REAL (Read)
``````````````````````````
Guess common logarithm of colour temperature in Kelvin for each
diluted Planck component.



SF( 6 ) = _INTEGER (Read)
`````````````````````````
For each component I, a value SF(I)=0 indicates that THETA(I) holds a
guess which is free to be fitted. A positive value SF(I)=I indicates
that THETA(I) is fixed. A positive value SF(I)=J<I indicates that
THETA(I) has to keep a fixed offset from THETA(J).



AF( 6 ) = _INTEGER (Read)
`````````````````````````
For each component I, a value AF(I)=0 indicates that ALPHA(I) holds a
guess which is free to be fitted. A positive value AF(I)=I indicates
that ALPHA(I) is fixed. A positive value AF(I)=J<I indicates that
ALPHA(I) has to keep a fixed offset to ALPHA(J).



TF( 6 ) = _INTEGER (Read)
`````````````````````````
For each component I, a value TF(I)=0 indicates that LGTEMP(I) holds a
guess which is free to be fitted. A positive value TF(I)=I indicates
that LGTEMP(I) is fixed. A positive value TF(I)=J<I indicates that
LGTEMP(I) has to keep a fixed ratio to LGTEMP(J).



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
fitbb in device=xw mask1=10.5 mask2=14.5
ncomp=1 theta=0.5 alpha=0 lgtemp=3.5 sf=0 af=1 tf=0 comp=1
logfil=planck This fits a Planck curve to the range of frequencies
between about 30 GHz and 3E14 Hz. The temperature is guessed to be
3000 K. The fit result is reported to the text file PLANCK and stored
as component number 1 in the input file's Specdre Extension. Since
DIALOG is not turned off, the user will be prompted for improvements
of the mask and guess, and will be asked whether the final fit result
is to be accepted (stored in the Extension and written to PLANCK.DAT).
The XWINDOWS graphics device will display the spectrum before masking,
guessing, and fitting. Independent of the DIALOG switch, a plot is
produced after fitting.



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


