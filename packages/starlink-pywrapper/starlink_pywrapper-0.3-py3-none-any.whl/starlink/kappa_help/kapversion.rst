

KAPVERSION
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

    
       kapversion [compare]
       



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
kapversion
Displays the version number of the installed package.
kapversion compare="V0.14-1"
Compares the version of the installed package with the version
"V0.14-1", and sets the RESULT parameter appropriately. For instance,
if the installed package was "V0.13-6" then RESULT would be set to -1.
If the installed package was "V0.14-1", RESULT would be set to 0. If
the installed package was "V0.14-5" RESULT would be set to +1.



Notes
~~~~~


+ The package version number is obtained from the "version" file in
  the directory containing the package's installed executable files.
  This file is created when the package is installed using the "mk
  install" command. An error will be reported if this file cannot be
  found.




Copyright
~~~~~~~~~
Copyright (C) 1999 Central Laboratory of the Research Councils. All
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


