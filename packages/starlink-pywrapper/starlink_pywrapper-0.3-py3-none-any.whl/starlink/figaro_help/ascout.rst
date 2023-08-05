

ASCOUT
======


Purpose
~~~~~~~
Write an NDF to an ASCII table


Description
~~~~~~~~~~~
This routine takes an NDF (section) and writes it to an ASCII table.
The first part of the output file is a header giving textual
information and a head for the table. These lines start with a blank
carriage return control character followed by an exclamation mark as
the first printed character. The table itself has to the left all the
axis values and optionally the pixel widths, and to the right the data
value and its error if known. The spectroscopic axis is written with
higher precision (12 significant digits instead of 7) if its storage
type is _DOUBLE. The total number of table columns can be 8 at most.
All pixel widths are written if and only if requested, regardless of
whether there is explicit information in the input file. Each width
occupies the column to the right of the corresponding centre value.


Usage
~~~~~


::

    
       ascout in out
       



ADAM parameters
~~~~~~~~~~~~~~~



WIDTH = _LOGICAL (Read)
```````````````````````
True if pixel widths are to be written, too. [NO]



BAD = _REAL (Read)
``````````````````
The alternative bad value. Where the data or variance array has bad
values, BAD is written to the ASCII table.



IN = NDF (Read)
```````````````
The input NDF.



OUT = FILENAME (Read)
`````````````````````
The ASCII output file.



Examples
~~~~~~~~
ascout in(1.5:2.5) out
This expects a 1-D data set in IN and will write to the ASCII file OUT
the information for axis values between 1.5 and 2.5. Should IN be more
than 1-D, the first hyper-row would be used.
ascout in(1.5:2.5,10:15) out
This will accept a 2-D data set in IN and write to OUT the information
for 1st axis coordinate values between 1.5 and 2.5 and for 2nd axis
pixel number between 10 and 15. Note that integers in the section
specification are interpreted as pixel numbers.



Notes
~~~~~
This routine recognises the Specdre Extension v. 0.7.


