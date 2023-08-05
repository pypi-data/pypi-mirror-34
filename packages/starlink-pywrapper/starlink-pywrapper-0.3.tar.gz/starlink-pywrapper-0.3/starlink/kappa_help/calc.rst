

CALC
====


Purpose
~~~~~~~
Evaluates a mathematical expression


Description
~~~~~~~~~~~
This task evaluates an arithmetic expression and reports the result.
It main role is to perform floating-point arithmetic in scripts. A
value "Bad" is reported if there was an error during the calculation,
such as a divide by zero.


Usage
~~~~~


::

    
       calc exp [prec] fa-fz=? pa-pz=?
       



ADAM parameters
~~~~~~~~~~~~~~~



EXP = LITERAL (Read)
````````````````````
The mathematical expression to be evaluated, e.g. "-2.5*LOG10(PA)". In
this expression constants may either be given literally or represented
by the variables PA, PB, ... PZ. The expression may contain sub-
expressions represented by the variables FA, FB, ... FZ. Values for
those sub-expressions and constants which appear in the expression
will be requested via the application's parameter of the same name.
FORTRAN 77 syntax is used for specifying the expression, which may
contain the usual intrinsic functions, plus a few extra ones. An
appendix in SUN/61 gives a full description of the syntax used and an
up-to-date list of the functions available. The arithmetic operators
(+,-,/,*,**) follow the normal order of precedence. Using matching
(nested) parentheses will explicitly define the order of expression
evaluation. The expression may be up to 132 characters long.



FA-FZ = LITERAL (Read)
``````````````````````
These parameters supply the values of `sub-expressions' used in the
expression EXP. Any of the 26 may appear; there is no restriction on
order. These parameters should be used when repeated expressions are
present in complex expressions, or to shorten the value of EXP to fit
within the 132-character limit. Sub-expressions may contain references
to other sub-expressions and constants (PA-PZ). An example of using
sub-expressions is: EXP > PA*ASIND(FA/PA)*X/FA FA > SQRT(X*X+Y*Y) PA >
10.1 where the parameter name is to the left of > and its value is to
the right of the >.



PA-PZ = _DOUBLE (Read)
``````````````````````
These parameters supply the values of constants used in the expression
EXP and sub-expressions FA-FZ. Any of the 26 may appear; there is no
restriction on order. Using parameters allows the substitution of
repeated constants using one reference. This is especially convenient
for constants with many significant digits. It also allows easy
modification of parameterised expressions provided the application has
not been used with a different EXP in the interim. The parameter PI
has a default value of 3.14159265359D0. An example of using parameters
is: EXP > SQRT(PX*PX+PY*PY)*EXP(PX-PY) PX > 2.345 PY > -0.987 where
the parameter name is to the left of > and its value is to the right
of the >.



PREC = LITERAL (Read)
`````````````````````
The arithmetic precision with which the transformation functions will
be evaluated when used. This may be either "_REAL" for single
precision, "_DOUBLE" for double precision, or "_INTEGER" for integer
precision. Elastic precisions are used, such that a higher precision
will be used if the input data warrant it. So for example if PREC =
"_REAL", but double-precision data were to be transformed, double-
precision arithmetic would actually be used. The result is reported
using the chosen precision. ["_REAL"]



RESULT = LITERAL (Write)
````````````````````````
The result of the evaluation.



Examples
~~~~~~~~
The syntax in the following examples apply to the shell.

calc "27.3*1.26"
The reports the value of the expression 27.3*1.26, i.e. 34.398.
calc exp="(pa+pb+pc+pd)/4.0" pa=$med1 pb=$med2 pc=$med3 pd=$med4
This reports the average of four values defined by script variables
med1, med2, med3, and med4.
calc "42.6*pi/180"
This reports the value in radians of 42.6 degrees.
calc "(mod(PO,3)+1)/2" prec=_integer po=$count
This reports the value of the expression "(mod($count,3)+1)/2)" where
$count is the value of the shell variable count. The calculation is
performed in integer arithmetic, thus if count equals 2, the result is
1 not 1.5.
calc "sind(pa/fa)*fa" fa="log(abs(pb+pc))" pa=2.0e-4 pb=-1 pc=$x
This evaluates sind(0.0002/log(abs($x-1)))*log(abs($x-1)) where $x is
the value of the shell variable x.
For ICL usage only those expressions containing parentheses need

to be in quotes, though ICL itself provides the arithmetic. So

the above examples would be

calc 27.3*1.26
The reports the value of the expression 27.3*1.26, i.e. 34.398.
calc exp="(pa+pb+pc+pd)/4.0" pa=(med1) pb=(med2) pc=(med3)
pd=(med4) This reports the average of four values defined by ICL
variables med1, med2, med3, and med4.
calc 42.6*pi/180
This reports the value in radians of 42.6 degrees.
calc "(mod(PO,3)+1)/2" prec=_integer po=(count)
This reports the value of the expression "(mod(count,3)+1)/2)" where
(count) is the value of the ICL variable count. The calculation is
performed in integer arithmetic, thus if count equals 2, the result is
1 not 1.5.
calc "sind(pa/fa)*fa" fa="log(abs(pb+pc))" pa=2.0e-4 pb=-1 pc=(x)
This evaluates sind(0.0002/log(abs((x)-1)))*log(abs((x)-1)) where (x)
is the value of the ICL variable x.



Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: MATHS.


Copyright
~~~~~~~~~
Copyright (C) 1995 Central Laboratory of the Research Councils. All
Rights Reserved.


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
On OSF/1 systems an error during the calculation results in a core
dump. On Solaris, undefined values are set to one. These are due to
problems with the TRANSFORM infrastructure.


