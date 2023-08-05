

FIT1D
=====


Purpose
~~~~~~~
Fit 1-D profiles to a data cube


Description
~~~~~~~~~~~
This command fits 1-D profiles, such as gaussians, along an axis of a
multi-dimensional data cube, that is expected to have spectral
baselines or continua removed. The task creates a (hyper-)cube of the
fitted profiles; this NDF also stores the fitted-profile parameters in
an extension. Note that this is a preliminary release of FIT1D.
The routine can fit complex spectra with multiple components in a data
cube (actually: fit along any axis of a hyper-cube). It is multi-
threaded and capable of fitting a large number of (i.e. order a
million) spectra in a few minutes, depending of course on the number
of cores available. It borrows heavily from the "xgaufit" routine of
the GIPSY package.
The type of profiles that can be fitted and have been tested are
"gaussian", "gausshermite1" (gaussian with asymmetric wings), and
"gausshermite2" (peaky gaussians possibly with asymmetric wings). See
the important "Fitting Functions" topic for more details.
The parameters for each fitted component reside in the SMURF_FIT1D
extension as cube NDFs called COMP_1,..., COMP_N. For a gaussian the
planes in these cubes correspond to: amplitude, position, and fwhm.
Further details are under topic "Fitted Parameters".
A default config file is in $SMURF_DIR/smurf_fit1d.def. A sample file
for user specified values is $SMURF_DIR/smurf_fit1d_uval.def.


Usage
~~~~~


::

    
       fit1d in out rms config [userval] [pardir] [parndf] [parcomp]
       



ADAM parameters
~~~~~~~~~~~~~~~



CONFIG = GROUP (Read)
`````````````````````
Specifies values for the configuration parameters used by the FIT1D.
If the string "def" (case-insensitive) or a null (!) value is
supplied, a set of default configuration parameter values will be used
from $SMURF_DIR/smurf_fit1d.def. See the "Configuration Parameters"
topic for detailed information.



IN = NDF (Read)
```````````````
Baselined input file(s).



OUT = NDF (Write)
`````````````````
Output file(s) with the fitted profiles.



OUTFILES = LITERAL (Write)
``````````````````````````
The name of text file to create, in which to put the names of all the
output NDFs created by this application (one per line). If a null
value is supplied no file is created. [!]



PARCOMP = GROUP (Read)
``````````````````````
Component parameter file(s) to use for initial estimates, fixed
values, or to generate a model with (see "model_only"). Instead of a
comma separated string of filenames a "^list" file can be submitted
with each filename on a separate line. Files will map to components
1..N in the order as specified. See "Fitted Parameters" for more
information on parameter files.
The full specification of a parameter file name consists of three
parts: an optional directory path ("pardir"), an optional container
ndf ("parndf") and plus the base name for the file ("parcomp"):
"pardir"/"parndf".MORE.SMURF_FIT1D."parcomp" For convenience "pardir"
and "parndf" can be specified through their respective parameters, but
full name(s) can also be specified through "parcomp". In case "pardir"
is specified, FIT1D will append a "/". Similarly, if "parndf" is given
the string ".MORE.SMURF_FIT1D." will be appended. Note that leaving
"parndf" blank will result in a conventional "pardir"/"filename" path.
In case "parndf" is specified, but "parcomp" is not, all components in
the container file will be read. Note that COMP_0 will be skipped
since it hold diagnostics information about the fit.
To escape special characters (",", ".", "@", etc) in the string you
may need to use a set of single+double quotes. A null value means no
component parameter files will be used. [!]



PARDIR = LITERAL (Read)
```````````````````````
Directory with component parameter files or the parameter NDF. For
details see help on PARCOMP. To escape special characters (",", ".",
"@", etc) in the string you may need to use a set of single+double
quotes. A null value results in use of the current directory. [!]



PARNDF = LITERAL (Read)
```````````````````````
NDF resulting from a previous execution of FIT1D and containing
component parameter files as part of its meta-data to use in the
current fit. The components are stored as
"parndf".MORE.SMURF_FIT1D.COMP_#. For further details see help on
PARCOMP. To escape special characters (",", ".", "@", etc) in the
string you may need to use a set of single+double quotes. [!]



RMS = _DOUBLE (Read)
````````````````````
RMS in input NDF(s) in data units.



USERVAL = GROUP (Read)
``````````````````````
Input keymap file with user-supplied fixed values or initial estimates
for the fit and a flag whether parameters are to be kept fixed in the
fit. The sample/default keymap file is
$SMURF_DIR/smurf_fit1d_uval.def. Entries are of the form:
"comp"#."fid" = value, "comp"#.par = value, or "fix"#.par = [0,1] with
'par' being a parameter relevant for the function being fitted. '#'
(1..n) indicates the component profile being described. Fix indicates
a parameter to be kept fixed or fitted.
If specified "comp"#.fid will override the default function selected
in the config file. Parameter names are described in the help item
"Fitting Functions" comp.fid comp.par Gauss: 1 a, b, c Gausshermite1:
2 a, b, c, h3 Gausshermite2: 3 a, b, c, h4 Voigt: 4 a, b, c, l
The "fix"#.par parameter can have a value of: 1 = fix parameter at
given value, do not fit -or- 0 = use as initial estimate, but fit. As
for comp, the '#' (1..n) indicates the component.
A null value for USERVAL means that no user-supplied estimates or
fixed values are to be used. [!]



Examples
~~~~~~~~
fit1d in=orion out=orion_gauh2 rms=0.22
Fits using the settings as defined in the default Configuration file
"$SMURF_DIR/smurf_fit1d.def": fitting a single gausshermite2 to each
profile along the highest dimension of the file "orion.sdf". The input
file is expected to be baselined and the zerolevel of the profile to
be 0. The fitted profiles are stored in the file "orion_gauh2.sdf"
with a component parameter file with the gauss-hermite parameters a,
b, c, h3, h4 as "orion_gauh2.more.smurf_fit1d.comp_1" (plus ...comp_0
for the diagnostics component).
fit1d in=orion out=orion_gauss rms=0.22 \
config='"^$SMURF_DIR/smurf_fit1d.def,function=gauss"' Same as above,
but fit a single gaussian instead. Alternatively, use
config='"^myfits1d.def"' having the following lines:
^$SMURF_DIR/smurf_fit1d.def function = gaussian
fit1d in=orion out=orion_gauh2 rms=0.22 parndf=orion_gauss
As in the first example fit a gausshermite2, but use the output from
the gaussian fit of the second example for initial estimates. This can
help or do harm: while the "internal" initial estimate from Fit1d may
be in-accurate, in the first example a fit with a gausshermite2 will
be attempted regardless. By contrast, the gaussian fit to a non-
gaussian profile in example 2 may have been so poor that is was
rejected: in that case current gausshermite2 fit will skip the profile
because there won't be any initial estimates.
fit1d in=orion out=orion_gauh2 rms=0.22 userval='"^myvalues.def"' \
config='"^$SMURF_DIR/smurf_fit1d.def,function=gauss,ncomp=3"' Fit
three gaussian components to each profile using initial estimates and
fixed values as defined in the file "myvalues.def" (template:"
$SMURF_DIR/smurf_fit1d_uval'def"), e.g.: comp1.b = -5.2 fix1.b = 1
comp1.c = 6 comp2.b = 20.4 fix2.b = 1 comp2.c = 4 comp3.b = 35.3 That
is: provide a user-defined fixed value for the position (parameter
"b") of components 1 and 2, and an initial estimate for component 3.
Also provide user-defined initial estimates for the FWHM (parameter
"c") of components 1 and 2. Leave it to fit1d to find initial
estimates for all other parameters.



Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~
A default configuration file can be found at
$SMURF_DIR/smurf_fit1d.def. ABSH3MIN, ABSH3MAX = REAL Min and Max
allowable value for the H3 (~skew) parameter in a Gausshermite# fit.
If RETRY=1 has been set, a pure gaussian fit (H3=0) will be attempted
in case the initial fit of H3 is out of bounds. Set to <undef> if no
limit desired. [0.01, 0.5] ABSH4MIN, ABSH4MAX = REAL Min and Max
allowable value for the H4 (~peakiness) parameter in a Gausshermite4
fit. If RETRY=1 has been set, a gausshermite1 fit (H4=0) will be
attempted in case the initial fit of H4 is out of bounds. Set to
<undef> if no limit desired. [0.01, 0.35] AXIS = INTEGER Axis to fit
along (starting at 1). A value of 0 translates as fit along highest
dimension i.e. Vlsr in a Ra, Dec, Vlsr cube. [0] CLIP(2) = REAL Values
in the input profiles outside the specified clip-range [min,max] will
be not be used in the fit. ESTIMATE_ONLY = LOGICAL Set to 1: The
output cube will have the results from the initial estimates routine
instead of the the fit. Good initial estimates are critical for the
fit and checking and/or fixing initial estimates may help solve
problems. [0] FUNCTION = STRING Function to fit. Currently implemented
are "gaussian", "gausshermite1", "gausshermite2", "voigt". See topic
"Fitting Functions" for details. If your aim is to capture a much
emission as possible e.g. in order to create a 2-D image from a 3-D
cube, gausshermite2 profiles are recommmended. ["gausshermite2"]
MAXLORZ = REAL Maximum value for the FHWM of the Lorentzian component
("L") in a Voigt fit in terms of ==PIXELS==(!). If RETRY=1 has been
set, a pure gaussian fit (L=0) will be attempted in case the initial
fit of H3 is out of bounds. [<undef>] MINAMP = REAL Minimum value for
the Amplitude-like parameter to accept as a genuine fit in terms of
the RMS(!). Based on this alone at 3-sigma ~5% of the profiles
selected for fitting can be expected to be noise spikes. This value
drops to ~2% for 5-sigma. All assuming gaussian statistics of course.
[3] MINWIDTH = REAL Minimum value for the FHWM (~2.35*Dispersion) to
accept as a genuine fit in terms of ==PIXELS==(!). [1.88] MODEL_ONLY =
LOGICAL Set to 1: Bypass both the initial estimates and fitting
routine and generate profiles directly from the supplied input
parameter cube(s) and/or user supplied fixed values. Not supplying all
parameters will generate an error. [0] NCOMP = INTEGER Maximum number
of 'component' functions to fit to each profile, e.g. a multi-
component spectrum of maximum three gaussians. [Note: The complete fit
of the gaussians is done concurrently, not iteratively starting e.g.
with the strongest component]. The routine will try to find and fit
ncomp functions along each profile, but may settle for less. [3]
POS_ONLY = LOGICAL FIT1D expected profiles to have been baselined i.e.
fitted profiles typically should not have a negative values. However,
Gausshermite profiles naturally give rise to undesired negative
features e.g. in fitting skewed profiles. This parameter simply causes
the routine to set values in the output profiles to zero whereever
they are negative. This generally gives better matching profiles, but
of course means the fits are not pur gausshermites anymore. Make sure
to set this parameter to NO of your profiles have genuine negative
features e.g. as in p-cygni profiles. [YES] RANGE(2) = REAL Coordinate
range along axis to find and fit profiles. The format is (x1, x2)
including the (). For example, Vlsr -20 35 is "(-20,35)". Default is
to use the full extent of the axis: [<undef>] RETRY = LOGICAL Whenever
the lorentzian ("L") or hermite parameters ("H3", "H4") are out of the
routine re-tries the fit with the out-of-bounds parameter(s) fixed at
0. This means that in effect the fit cascades to a simpler function:
gausshermite2 -> gausshermite1 -> gaussian; voigt -> gaussian. The
result is that there are valid fits for more profiles, but the
function actually fitted may vary with position. Setting the retry
value to 0 prevents this from happening and may cause the fit to fail
or be (very) poor. [YES] SORT = STRING Sort the resulting fits: "amp":
sort by decreasing fitted value of the amp-like parameter "width":
sort by decreasing fitted fwhm of the width-like parameter "position":
sort by increasing position along the profile axis "distance": sort by
increasing fitted distance from the centre pixel in the profile.
Sorting can be helpful, but be cautioned that it can also complicate
things: if there are two components one at -10 km/s and one at 10 km/s
sorting by amplitude or width can result in the parameter file for
component 1 to be a mix of the -10 and 10 km/s features depending on
which one was relatively stronger or wider. Similarly, sorting by
position can result in low-amplitude fits of noise spikes to be mixed
with stronger components. For more precise control try to run the
routine iteratively with e.g. a different restricted velocity range to
try pick out the different components. Default is to sort by
amplitude. ["amp"] SORT_ESTIMATE = LOGICAL Sort initial estimates also
with the sorting selected in 'sort'. Estimates can be very inaccurate
plus are not checked against any boundary limits until after the fit.
Thus this option may not be very helpful.


Fitting Functions
~~~~~~~~~~~~~~~~~
The function menu provides the choice of four functions for which you
can fit the parameters to the data in your profiles.
1) A standard GAUSSIAN. Parameters are a = maximum, b = centre, and c
= FWHM.
NOTE that if one of h3 and h4 in a gauss-hermite function is non-zero,
the mean of the distribution is not the position of the maximum
(Reference; Marel, P. van der, Franx, M., A new method for the
identification of non-gaussian line profiles in elliptical galaxies.
A.J., 407 525-539, 1993 April 20):
2) GAUSS-HERMITE1 polynomial (h3). Parameters are a (amplitude), b
(position),c (width), and h3 as mentioned these are *NOT* the same as
maximum, centre, and fwhm of the distribution as for a gaussian:
maximum ~= [determine value and position of max from fitted profiles
using e.g. collapse] centre ~= b + h3*sqrt(3) FWHM ~= abs( c*(1-3h3^2)
) ~= c skewness ~= 4*sqrt(3)*h3
3) GAUSS-HERMITE2 polynomial (h3, h4). Same as previous, but an extra
parameter h4 is included: maximum ~= [determine value and position of
max from fitted profiles using e.g. collapse] centre ~= b + h3*sqrt(3)
FWHM ~= abs( c*(1+h4*sqrt(6)) ) skewness ~= 4*sqrt(3)*h3 kurtosis ~=
8*sqrt(6)*h4
4) VOIGT function. Parameters are a (area), b (centre), c (doppler
FWHM), l (lorenztian FWHM), and v (area factor) with relations:
maximum ~= [determine value of max from fitted profiles using e.g.
collapse] centre ~= b doppler fwhm ~= c lorentzian fwhm ~= l amp = v
(OUTPUT ONLY!) amplitude calculated from a (area) using the standard
amp2area function for a voigt (based on the Faddeeva complex error
function): amp = area / amp2area


Fitted Parameters
~~~~~~~~~~~~~~~~~
The fitted parameters are stored in the file header as
FILE.MORE.SMURF_FIT1D.COMP_0 to COMP_N, with N depending on how many
components are being fitted. These are regular data cubes that can be
inspected with e.g. Gaia or extracted using NDFCOPY. The 'planes' in
the cubes are:
COMP_0 diagnostics info, planes: 1 = number of components found 2 =
fit error: (see below)
COMP_1..N fitted profiles, planes: (gaussian) (gausshermite) (voigt) 1
= amplitude 'a' area 2 = position 'b' position 3 = fwhm 'c' doppler
fwhm 'd' 4 = - 'h3' lorentzian fwhm 'l' 5 = - 'h4' amp2area 'v' last:
function id 1 = gaussian; 2 = gausshermite1 (h3); 3 = gausshermite2
(h3,h4), 4 = voigt
FIT ERRORS: >0 Number of iterations needed to achieve convergence
according to TOL.

+ 1 Too many free parameters, maximum is 32.
+ 2 No free parameters.
+ 3 Not enough degrees of freedom.
+ 4 Maximum number of iterations too small to obtain a solution which
satisfies TOL.
+ 5 Diagonal of matrix contains elements which are zero.
+ 6 Determinant of the coefficient matrix is zero.
+ 7 Square root of negative number. <-10 All fitted components
  rejected due to minamp, minwidth, maxlorz, or range constraints.




Copyright
~~~~~~~~~
Copyright (C) 2006 Particle Physics and Astronomy Research Council.
Copyright (C) 2008-2012 Science and Technology Facilities Council.
Copyright (C) 2013 University of British Columbia. All Rights
Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 3 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307,
USA.


