

POLCONCAT
=========


Purpose
~~~~~~~
Concatenate two or more vector catalogues


Description
~~~~~~~~~~~
This application creates a new vector catalogue by concatenating the
vectors from a list of two or more input catalogues. The output
catalogue inherits the WCS and reference diection of the first input
catalogue.


Usage
~~~~~


::

    
       polconcat in out
       



ADAM parameters
~~~~~~~~~~~~~~~



IN = LITERAL (Write)
````````````````````
A group of two or more input vector catalogues.



OUT = LITERAL (Write)
`````````````````````
The output catalogue.



Notes
~~~~~


+ All input catalogues must contain WCS information (i.e. they must
have been created using polpack).
+ This command does not currently support concatenating catalogues
that contain circular polarisation values.
+ All input catalogues must use the same units for I, Q and U.
+ If the first input catalogue contains variance columns, then all
  input catalogues must contain variance columns. If the first input
  catalogue does not contains variance columns, then none of the input
  catalogues must contain variance columns.




Copyright
~~~~~~~~~
Copyright (C) 2017 East Asian Observatory. All Rights Reserved.


Licence
~~~~~~~
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either Version 2 of the License, or (at
your option) any later version.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


