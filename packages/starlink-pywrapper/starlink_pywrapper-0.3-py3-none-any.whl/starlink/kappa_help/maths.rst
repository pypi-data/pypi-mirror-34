

MATHS
=====


Purpose
~~~~~~~
Evaluates mathematical expressions applied to NDF data structures


Description
~~~~~~~~~~~
This application allows arithmetic and mathematical functions to be
applied pixel-by-pixel to a number of NDF data structures and
constants so as to produce a new NDF. The operations to be performed
are specified using a Fortran-like mathematical expression. Up to 26
each input NDF data and variance arrays, 26 parameterised `constants',
and pixel and data co-ordinates along up to 7 dimensions may be
combined in wide variety of ways using this application. The task can
also calculate variance estimates for the result when there is at
least one input NDF array.


Usage
~~~~~


::

    
       maths exp out ia-iz=? va-vz=? fa-fz=? pa-pz=? lbound=? ubound=?
       



ADAM parameters
~~~~~~~~~~~~~~~



EXP = LITERAL (Read)
````````````````````
The mathematical expression to be evaluated for each NDF pixel, e.g.
"(IA-IB+2)*PX". In this expression, input NDFs are denoted by the
variables IA, IB, ... IZ, while constants may either be given
literally or represented by the variables PA, PB, ... PZ. Values for
those NDFs and constants which appear in the expression will be
requested via the application's parameter of the same name.
Fortran-77 syntax is used for specifying the expression, which may
contain the usual intrinsic functions, plus a few extra ones. An
appendix in SUN/61 gives a full description of the syntax used and an
up to date list of the functions available. The expression may be up
to 132 characters long and is case insensitive.



FA-FZ = LITERAL (Read)
``````````````````````
These parameters supply the values of `sub-expressions' used in the
expression EXP. Any of the 26 (FA, FB, ... FZ) may appear; there is no
restriction on order. These parameters should be used when repeated
expressions are present in complex expressions, or to shorten the
value of EXP to fit within the 132-character limit. Sub-expressions
may contain references to other sub-expressions and constants (PA-PZ).
An example of using sub-expressions is: EXP > PA*ASIND(FA/PA)*XA/FA FA
> SQRT(XA*XA+XB*YB) PA > 10.1 where the parameter name is to the left
of > and its value is to the right of the >.



IA-IZ = NDF (Read)
``````````````````
The set of 26 parameters named IA, IB, ... IZ is used to obtain the
input NDF data structure(s) to which the mathematical expression is to
be applied. Only those parameters which actually appear in the
expression are used, and their values are obtained in alphabetical
order. For instance, if the expression were "SQRT(IB+IA)", then the
parameters IA and IB would be used (in this order) to obtain the two
input NDF data structures.



LBOUND( ) = _INTEGER (Read)
```````````````````````````
Lower bounds of new NDF, if LIKE=! and there is no input NDF
referenced in the expression. The number of values required is the
number of pixel co-ordinate axes in the expression.



LIKE = NDF (Read)
`````````````````
An optional template NDF which, if specified, will be used to define
bounds and data type of the new NDF, when the expression does not
contain a reference to an NDF. If a null response (!) is given the
bounds are obtained via parameters LBOUND and UBOUND, and the data
type through parameter TYPE. [!]



OUT = NDF (Write)
`````````````````
Output NDF to contain the result of evaluating the expression at each
pixel.



PA-PZ = _DOUBLE (Read)
``````````````````````
The set of 26 parameters named PA, PB, ... PZ is used to obtain the
numerical values of any parameterised `constants' which appear in the
expression being evaluated. Only those parameters which actually
appear in the expression are used, and their values are obtained in
alphabetical order. For instance, if the expression were
"PT*SIN(IA/PS)", then the parameters PS and PT (in this order) would
be used to obtain numerical values for substitution into the
expression at the appropriate points.
These parameters are particularly useful for supplying the values of
constants when writing procedures, where the constant may be
determined by a command-language variable, or when the constant is
stored in a data structure such as a global parameter. In other cases,
constants should normally be given literally as part of the
expression, as in "IZ**2.77".



QUICK = _LOGICAL (Read)
```````````````````````
Specifies the method by which values for the VARIANCE component of the
output NDF are calculated. The algorithm used to determine these
values involves perturbing each of the input NDF data arrays in turn
by an appropriate amount, and then combining the resulting output
perturbations. If QUICK is set to TRUE, then each input data array
will be perturbed once, in the positive direction only. If QUICK is
set to FALSE, then each will be perturbed twice, in the positive and
negative directions, and the maximum resultant output perturbation
will be used to calculate the output variance. The former approach
(the normal default) executes more quickly, but the latter is likely
to be more accurate in cases where the function being evaluated is
highly non-linear, and/or the errors on the data are large. [TRUE]



TITLE = LITERAL (Read)
``````````````````````
Value for the title of the output NDF. A null value will cause the
title of the (alphabetically) first input NDF to be used instead. [!]



TYPE = LITERAL (Read)
`````````````````````
Data type for the new NDF, if LIKE=! and no input NDFs are referenced
in the expression. It must be one either "_DOUBLE" or "_REAL".



UBOUND( ) = _INTEGER (Read)
```````````````````````````
Upper bounds of new NDF, if LIKE=! and there is no input NDF
referenced in the expression. These must not be smaller than the
corresponding LBOUND. The number of values required is the number of
pixel co-ordinate axes in the expression.



UNITS = _LOGICAL (Read)
```````````````````````
Specifies whether the UNITS component of the (alphabetically) first
input NDF or the template NDF will be propagated to the output NDF. By
default this component is not propagated since, in most cases, the
units of the output data will differ from those of any of the input
data structures. In simple cases, however, the units may be unchanged,
and this parameter then allows the UNITS component to be preserved.
This parameter is ignored if the expression does not contain a token
to at least one input NDF structure and LIKE=!. [FALSE]



VA-VZ = NDF (Read)
``````````````````
The set of 26 parameters named VA, VB, ... VZ is used to obtain the
input NDF variance array(s) to which the mathematical expression is to
be applied. The variance VA corresponds to the data array specified by
parameter IA, and so on. Only those parameters which actually appear
in the expression, and do not have their corresponding data-array
parameter IA-IZ present, have their values obtained in alphabetical
order. For instance, if the expression were "IB+SQRT(VB+VA)", then the
parameters VA and IB would be used (in this order) to obtain the two
input NDF data structures. The first would use just the variance
array, whilst the second would read both data and variance arrays.



VARIANCE = _LOGICAL (Read)
``````````````````````````
Specifies whether values for the VARIANCE component of the output NDF
should be calculated. If this parameter is set to TRUE (the normal
default), then output variance values will be calculated if any of the
input NDFs contain variance information. Any which do not are regarded
as having zero variance. Variance calculations will normally be
omitted only if none of the input NDFs contain variance information.
However, if VARIANCE is set to FALSE, then calculation of output
variance values will be disabled under all circumstances, with a
consequent saving in execution time. This parameter is ignored if the
expression does not contain a token to at least one input NDF
structure. [TRUE]



Examples
~~~~~~~~
maths "ia-1" dat2 ia=dat1
The expression "ia-1" is evaluated to subtract 1 from each pixel of
the input NDF referred to as IA, whose values reside in the data
structure dat1. The result is written to the NDF structure dat2.
maths "(ia-ib)/ic" ia=data ib=back ic=flat out=result units
The expression "(ia-ib)/ic" is evaluated to remove a background from
an image and to divide it by a flat-field. All the images are held in
NDF data structures, the input image being obtained from the data
structure data, the background image from back and the flat-field from
flat. The result is written to the NDF structure result. The data
units are unchanged and are therefore propagated to the output NDF.
maths "-2.5*log10(ii)+25.7" ii=file1 out=file2
The expression "-2.5*log10(ii)+25.7" is evaluated to convert intensity
measurements into magnitudes, including a zero point. Token II
represents the input measurements held in the NDF structure file1. The
result is written to the NDF structure file2. If file1 contains
variance values, then corresponding variance values will also be
calculated for file2.
maths exp="pa*exp(ia+pb)" out=outfile pb=13.7 novariance
The expression "pa*exp(ia+pb)" is evaluated with a value of 13.7 for
the constant PB, and output is written to the NDF structure outfile.
The input NDF structure to be used for token IA and the value of the
other numerical constant PA will be prompted for. NOVARIANCE has been
specified so that output variance values will not be calculated.
maths exp="mod(XA,32)+mod(XB,64)" out=outfile like=comwest
The expression "mod(XA,32)+mod(XB,64)" is evaluated, and output is
written to the NDF structure outfile. The output NDF inherits the
shape, bounds, and other properties (except the variance) of the NDF
called comwest. The data type of outfile is _REAL unless comwest has
type _DOUBLE. XA and XB represent the pixel co-ordinates along the x
and y axes respectively.
maths "xf*xf+0*xa" ord2 lbound=[-20,10] ubound=[20,50]
The expression "xf*xf+0*xa" is evaluated, and output is written to the
NDF structure ord2. The output NDF has data type _REAL, is two-
dimensional with bounds -20:20, 10:50. The XA is needed to indicate
that XF represents pixel co-ordinates along the y axis.
maths "xa/max(1,xb)+sqrt(va)" ord2 va=fuzz title="Fuzz correction"
The expression "xa/max(1,xb)+sqrt(va)" is evaluated, and output is
written to the NDF structure ord2. Token VA represents the input
variance array held in the NDF structure fuzz. The output NDF inherits
the shape, bounds, and other properties of fuzz. The title of ord2 is
"Fuzz correction". The data type of ord2 is _REAL unless fuzz has type
_DOUBLE. XA and XB represent the pixel co-ordinates along the x and y
axes respectively.



Notes
~~~~~


+ The alphabetically first input NDF is regarded as the primary input
dataset. NDF components whose values are not changed by this
application will be propagated from this NDF to the output. The same
propagation rules apply to the LIKE template NDF, except that the
output NDF does have inherit any variance information.
+ There are additional tokens which can appear in the expression.

The set of 7 tokens named CA, CB, ... CG is used to obtain the data
co-ordinates from the primary input NDF data structure. Any of the 7
parameters may appear in the expression. The order defines which axis
is which, so for example, "2*CF+CB*CB" means the first-axis data co-
ordinates squared, plus twice the co-ordinates along the second axis.
There must be at least one input NDF in the expression to use the CA-
CG tokens, and it must have dimensionality of at least the number of
CA-CG tokens given.
The set of 7 tokens named XA, XB, ... XG is used to obtain the pixel
co-ordinates from the primary input NDF data structure. Any of the 7
parameters may appear in the expression. The order defines which axis
is which, so for example, "SQRT(XE)+XC" means the first-axis pixel co-
ordinates plus the square root of the co-ordinates along the second
axis. Here no input NDF need be supplied. In this case the
dimensionality of the output NDF is equal to the number of XA-XG
tokens in the expression. However, if there is at least one NDF in the
expression, there should not be more XA-XG tokens than the
dimensionality of the output NDF (given as the intersection of the
bounds of the input NDFs).

+ If illegal arithmetic operations (e.g. division by zero, or square
root of a negative number) are attempted, then a bad pixel will be
generated as a result. (However, the infrastructure software that
detects this currently does not work on OSF/1 systems, and therefore
MATHS will crash in this circumstance.)
+ All arithmetic performed by this application is floating point.
  Single-precision will normally be used, but double-precision will be
  employed if any of the input NDF arrays has a numeric type of _DOUBLE.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: CREFRAME, SETAXIS, and numerous arithmetic tasks; Figaro:
numerous arithmetic tasks.


Calculating Variance
~~~~~~~~~~~~~~~~~~~~
The algorithm used to calculate output variance values is general-
purpose and will give correct results for any reasonably well-behaved
mathematical expression. However, this application as a whole, and the
variance calculations in particular, are likely to be less efficient
than a more specialised application written knowing the form of the
mathematical expression in advance. For simple operations (addition,
subtraction, etc.) the use of other applications (ADD, SUB, etc.) is
therefore recommended, particularly if variance calculations are
required.
The main value of the variance-estimation algorithm used here arises
when the expression to be evaluated is too complicated, or too
infrequently used, to justify the work of deriving a direct formula
for the variance. It is also of value when the data errors are
especially large, so that the linear approximation normally used in
error analysis breaks down.
There is no variance processing when there are no tokens for input NDF
structures.


Timing
~~~~~~
If variance calculations are not being performed, then the time taken
is approximately proportional to the number of NDF pixels being
processed. The execution time also increases with the complexity of
the expression being evaluated, depending in the usual way on the
nature of any arithmetic operations and intrinsic functions used. If
certain parts of the expression will often give rise to illegal
operations (resulting in bad pixels), then execution time may be
minimised by placing these operations near the beginning of the
expression, so that later parts may not need to be evaluated.
If output variance values are being calculated and the QUICK parameter
is set to TRUE, then the execution time will be multiplied by an
approximate factor (N+1), where N is the number of input NDFs which
contain a VARIANCE component. If QUICK is set to FALSE, then the
execution time will be multiplied by an approximate factor (2N+1).


Copyright
~~~~~~~~~
Copyright (C) 1989-1990 Science & Engineering Research Council.
Copyright (C) 1995, 1998-1999, 2002, 2004 Central Laboratory of the
Research Councils. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street,Fifth Floor, Boston, MA
02110-1301, USA


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ This routine correctly processes the AXIS, DATA, QUALITY, VARIANCE,
LABEL, TITLE, UNITS, WCS and HISTORY components of the input NDFs.
HISTORY and extensions are propagated from both the primary NDF and
template NDF.
+ Processing of bad pixels and automatic quality masking are
supported.
+ All non-complex numeric data types can be handled.
+ NDFs with any number of dimensions can be processed. The NDFs
  supplied as input need not all be the same shape.




