

EVALFIT
=======


Purpose
~~~~~~~
Evaluate fit results


Description
~~~~~~~~~~~
This routine turns components in the result structure of the Specdre
Extension into a fake data set representing those results. Such a data
set is necessary to perform arithmetic operations between the result
(otherwise expressed only as a set of parameters) and the original
data.
The routine takes as input a base NDF (a section is not acceptable).
The output is a copy of the input, except for the main NDF data and
variance components. These are re-calculated from certain components
in the result structure of the Specdre Extension. Thus the output
contains the fit results both in the result structure and in the main
NDF. The main NDF can then be compared pixel by pixel with the
original data.
If the input main NDF has a variance component, the output variances
will be set to zero.
This routine recognises result components created by FITCHEBY,
FITGAUSS, FITPOLY, or FITTRI. Unrecognised components are ignored,
i.e. not added into the data. A warning to that effect is given. If a
component in any particular position has bad values as parameters,
then that component is ignored on that position. No warning to this
effect is given.
A component is accepted as 7th order series of Chebyshev polynomials
if the component type is 'Chebyshev series' and it has 11 parameters.
These are assumed to be order, xmin, xmax, coeff0, ... coeff7.
A component is accepted as 7th order polynomial if the component type
is 'polynomial' and it has 9 parameters. These are assumed to be
order, coeff0, ... coeff7.
A component is accepted as Gauss or triangle if the component type is
'Gauss' or 'triangle' and it has 4 parameters. The first three are
assumed to be centre, peak, FWHM.
The string comparison to check the component type is case-insensitive.


Usage
~~~~~


::

    
       evalfit in out comp=?
       



ADAM parameters
~~~~~~~~~~~~~~~



INFO = _LOGICAL (Read)
``````````````````````
If false, this routine will issue only error messages and no
informational message. [YES]



DIALOG = _CHAR (Read)
`````````````````````
If 'T', the routine can evaluate several sets of components. After a
set of components has been evaluated, the user will be asked whether
she wants to specify another set. ['T']



IN = NDF (Read)
```````````````
The input NDF. This must be a base NDF. If you need only a section of
an NDF, you use SUBSET first to create the section permanently.



OUT = NDF (Read)
````````````````
The output NDF.



COMP = _INTEGER (Read)
``````````````````````
The numbers of up to 6 components to be added into the output data
component. If you are not sure which component is which, you should
inspect the result structure of the data first with EDITEXT.



REPLY = _LOGICAL (Read)
```````````````````````
Set true to work on another set of components. This parameter is
relevant only if DIALOG is true. [NO]



Examples
~~~~~~~~
evalfit in out comp=[2,5,1,2] accept
This will take the input NDF IN and create an equally shaped NDF
called OUT. The specified components stored in IN's (and OUT's)
Specdre Extension are evaluated and added up to make up the main data
in OUT. Note that component no. 2 is added twice.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.


