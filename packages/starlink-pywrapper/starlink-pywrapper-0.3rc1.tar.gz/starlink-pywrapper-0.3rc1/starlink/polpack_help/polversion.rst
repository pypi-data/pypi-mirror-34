

POLVERSION
==========


Purpose
~~~~~~~
Checks the package version number


Description
~~~~~~~~~~~
This application will display the installed package version number, or
compare the version number of the installed package against a
specified version number, reporting whether the installed package is
older, or younger, or equal to the specified version.


Usage
~~~~~


::

    
       polversion [compare]
       



ADAM parameters
~~~~~~~~~~~~~~~



COMPARE = LITERAL (Read)
````````````````````````
A string specifying the version number to be compared to the version
of the installed package. If a null (!) value is supplied, the version
string of the installed package is displayed, but no comparison takes
place. If a non-null value is supplied, the version of the installed
package is not displayed.
The supplied string should be in the format "V<ddd>.<ddd>-<ddd>, where
"<ddd>" represents a set of digits. The leading "V" can be omitted, as
can any number of trailing fields (missing trailing fields default to
zero). [!]



RESULT = INTEGER (Write)
````````````````````````
If a value is given for the COMPARE parameter, then RESULT is set to
one of the following values:


+ 1 -- The installed package is older than the version number
specified by the COMPARE parameter.
+ 0 -- The version of the installed package is equal to the version
specified by the COMPARE parameter.
+ -1 -- The installed package is younger than the version number
  specified by the COMPARE parameter.

The same value is also written to standard output.



Examples
~~~~~~~~
polversion
Displays the version number of the installed package.
polversion compare="V2.0"
Compares the version of the installed package with the version "V2.0",
and sets the RESULT parameter appropriately. For instance, if the
installed package was "V1.0-6" then RESULT would be set to -1. If the
installed package was "V2.0", RESULT would be set to 0. If the
installed package was "V2.0-6" RESULT would be set to +1.



Notes
~~~~~


+ The package version number is obtained from the "version" file in
  the directory containing the package's installed executable files.
  This file is created when the package is installed using the "mk
  install" command. An error will be reported if this file cannot be
  found.




