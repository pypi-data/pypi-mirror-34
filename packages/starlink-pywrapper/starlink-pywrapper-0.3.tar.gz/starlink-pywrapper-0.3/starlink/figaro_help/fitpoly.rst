

FITPOLY
=======


Purpose
~~~~~~~
Fit a polynomial to a spectrum


Description
~~~~~~~~~~~
This routine fits a polynomial to a one-dimensional data set. This can
be specified as an NDF section. The data set must extend along the
spectroscopic axis.
After accessing the data and the (optional) plot device, the data will
be subjected to a mask that consists of up to six abscissa intervals.
These may or may not overlap and need not lie within the range of
existing data. The masking will remove data which are bad, have bad
variance or have zero variance. The masking will also provide weights
for the fit. If the given data have no variances attached, or if the
variances are to be ignored, all weights will be equal.
The masked data are then fed into the fit routine. The highest
polynomial order possible is 7. The fit weights data points according
to their errors. The coefficients reported are those of an ordinary
polynomial. Let (x,y) be the measurements, y(x) be the polynomial of
order n fitting the measurements, c_i (i = 1, ..., n+1) be the fitted
coefficients. Then y(x) can be calculated as
y(x) = c_1 + c_2 x + c_3 x**2 + ... + c_{n+1} x**n
If the fit is successful, then the result is reported to the screen
and plotted on the graphics device. The final plot viewport is saved
in the AGI data base and can be used by further applications.
The result is stored in the Specdre Extension of the input NDF.
Optionally, the complete description (input NDF name, mask used,
result, etc.) is written (appended) to an ASCII log file.
Optionally, the application can interact with the user. In that case,
a plot is provided before masking and before specifying the polynomial
order. After masking and fitting, a screen report and a plot
(optional) are provided and the user can improve the parameters.
Finally, the result can be accepted or rejected, that is the user can
decide whether to store the result in the Specdre Extension or not.
The screen plot consists of two viewports. The lower one shows the
data values (full-drawn bin-style) overlaid with the fit (dashed line-
style). The upper box shows the residuals (cross marks) and error
bars. The axis scales are arranged such that all masked data can be
displayed. The upper box displays a zero-line for reference, which
also indicates the mask.
The Extension provides space to store fit results for each non-
spectroscopic coordinate. Say, if you have a 2-D image each row being
a spectrum, then you can store results for each row. The whole set of
results can be filled successively by fitting one row at a time and
always using the same component number to store the results for that
row. (See also the example.)
The component fitted by this routine is specified as follows: The line
name and laboratory frequency are the default values and are not
checked against any existing information in the input's Specdre
Extension. The component type is 'polynomial'. The number of
parameters allocated to the component is 9. The parameter types are in
order of appearance: 'order', 'coeff0', ... 'coeff7'. Unused
coefficient are stored as zero.


Usage
~~~~~


::

    
       fitpoly in device=? mask1=? mask2=? order=? comp=? logfil=?
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, the routine will issue only error messages and no
informational messages. [YES]



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



ORDER = _INTEGER (Read)
```````````````````````
The polynomial order of the fit. Must be between 0 and 7. [1]



REMASK = _LOGICAL (Read)
````````````````````````
Reply YES to have another chance for improving the mask. [NO]



REGUESS = _LOGICAL (Read)
`````````````````````````
Reply YES to have another chance for improving the guess and fit. [NO]



FITGOOD = _LOGICAL (Read)
`````````````````````````
Reply YES to store the result in the Specdre Extension. [YES]



COMP = _INTEGER (Read and Write)
````````````````````````````````
The results are stored in the Specdre Extension of the data. This
parameter specifies which existing component is being fitted. It
should be between zero and the number of components that are currently
stored in the Extension. Give zero for a hitherto unknown component.
If COMP is given as zero or if it specifies a component unfit to store
the results of this routine, then a new component will be created in
the result storage structure. In any case this routine will report
which component was actually used and it will deposit the updated
value in the parameter system. [1]



FITCOEFFS( ) = _REAL (Write)
````````````````````````````
The coefficients of the fitted polynomial. The number of coefficients
returned depends on the order of the fitted polynomial. No more than
eight coefficients will be returned.



LOGFIL = FILENAME (Read)
````````````````````````
The file name of the log file. Enter the null value (!) to disable
logging. The log file is opened for append. [!]



Examples
~~~~~~~~
fitpoly in device=! mask1=2.2 mask2=3.3 order=3 comp=1 logfil=!
IN is a 1-D NDF. A 3rd order fit is made to the abscissa range between
2.2 and 3.3. The result is stored in component number 1 of the result
structure in the Specdre Extension of IN. The plot device and ASCII
log file are de-selected.
fitpoly in(,15) device=xw mask1=[2.0,2.3,3.4] mask2=[2.1,3.2,4.0]
order=2 comp=0 logfil=myfil Here IN is 2-D and the 15th row is
selected as the 1-D input for the fit. The mask consists of three
intervals [2.0;2.1] U [2.3;3.2] U [3.4,4.0]. The fit is a parabola.
Space for a new component is created for storage in the Specdre
Extension. The plot device is xwindows.
fitpoly in(,20) device=xw mask1=[2.0,2.3,3.4] mask2=[2.1,3.2,4.0]
order=4 comp=2 logfil=myfil In a follow-up from the previous example,
now the 20th row is fitted with 4th order. If in the previous run the
routine told us that it had used component number 2, then COMP=2 is
what we want to use to store a similar fit for a different row. The
first time round, the description of component 2 was created, saying
that it is a polynomial with order of 7 or less etc. And the fit
result for the 15th row was stored in an array that has space for all
rows in the input file. So the second time round, FITPOLY checks
whether component 2 is suitable, whether it is a polynomial with
maximum order 7. It then stores the new result for the 20th row in the
place reserved for this row. Gradually all rows can be fitted and
their results stored in the Extension. Possibly this could be
automated by writing a looping ICL procedure or shell script. In the
end the corresponding results for all rows are stored in one data
structure, and could for example be converted into a plot of the n-th
parameter value versus row number.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.
This routine works in situ and modifies the input file.


