

SETEXT
======


Purpose
~~~~~~~
Manipulates the contents of a specified NDF extension


Description
~~~~~~~~~~~
This task enables the contents of a specified NDF extension to be
edited. It can create a new extension or delete an existing one, can
create new scalar components within an extension, or modify or display
the values of existing scalar components within the extension. The
task operates on only one extension at a time, and must be closed down
and restarted to work on a new extension.
The task may operate in one of two modes, according to the LOOP
parameter. When LOOP=FALSE only a single option is executed at a time,
making the task suitable for use from an ICL procedure. When LOOP=TRUE
several options may be executed at once, making it easier to modify
several extension components interactively in one go.


Usage
~~~~~


::

    
       setext ndf xname option cname { ok
                                     { ctype=? shape=? ok
                                     { newname=?
                                     { xtype=?
                                   option
       



ADAM parameters
~~~~~~~~~~~~~~~



CNAME = LITERAL (Read)
``````````````````````
The name of component (residing within the extension) to be examined
or modified. It is only accessed when OPTION="Erase", "Get", "Put", or
"Rename".



CTYPE = LITERAL (Read)
``````````````````````
The type of component (residing within the extension) to be created.
Allowed values are "LITERAL", "_LOGICAL", "_DOUBLE", "_REAL",
"_INTEGER", "_CHAR", "_BYTE", "_UBYTE", "_UWORD", "_WORD". The length
of the character type may be defined by appending the length, for
example, "_CHAR*32" is a 32-character component. "LITERAL" and "_CHAR"
generate 80-character components. CTYPE is only accessed when
OPTION="Put".



CVALUE = LITERAL (Read)
```````````````````````
The value(s) for the component. Each value is converted to the
appropriate data type for the component. CVALUE is only accessed when
OPTION="Put". Note that for an array of values the list must be
enclosed in brackets, even in response to a prompt. For convenience,
if LOOP=TRUE, you are prompted for each string.



LOOP = _LOGICAL (Read)
``````````````````````
LOOP=FALSE requests that only one operation be performed. This allows
batch and non-interactive processing or use in procedures. LOOP=TRUE
makes SETEXT operate in a looping mode that allows several
modifications and/or examinations to be made to the NDF for one
activation. Setting OPTION to "Exit" will end the looping. [TRUE]



NDF = NDF (Update)
``````````````````
The NDF to modify or examine.



NEWNAME = LITERAL (Read)
````````````````````````
The new name of a renamed extension component. It is only accessed
when OPTION="Rename".



OK = _LOGICAL (Read)
````````````````````
This parameter is used to seek confirmation before a component is
erased or overwritten. A TRUE value permits the operation. A FALSE
value leaves the existing component unchanged. This parameter is
ignored when LOOP=FALSE.



OPTION = LITERAL (Read)
```````````````````````
The operation to perform on the extension or a component therein. The
recognised options are:


+ "Delete" -- Delete an existing NDF extension, and exit the task
(when LOOP=TRUE).
+ "Erase" -- Erase a component within an NDF extension
+ "Exit" -- Exit from the task (when LOOP=TRUE)
+ "Get" -- Display the value of a component within an NDF extension.
The component must exist.
+ "Put" -- Change the value of a component within an NDF extension or
create a new component.
+ "Rename" -- Renames a component. The component must exist.
+ "Select" -- Selects another extension. If the extension does not
  exist a new one is created. This option is not allowed when
  LOOP=FALSE.

The suggested default is the current value, except for the first
option where there is no default.



SHAPE( ) = _INTEGER (Read)
``````````````````````````
The shape of the component. Thus 3,2 would be a 2-dimensional object
with three elements along each of two lines. 0 creates a scalar. The
suggested default is the shape of the object if it already exists,
otherwise it is the current value. It is only accessed when
OPTION="Put".



XNAME = LITERAL (Given)
```````````````````````
The name of the extension to modify.



XTYPE = LITERAL (Given)
```````````````````````
The type of the extension to create. The suggested default is the
current value or "EXT" when there is no current value.



Examples
~~~~~~~~
setext hh50 fits delete noloop
This deletes the FITS extension in the NDF called hh50.
setext myndf select xtype=mytype noloop
This creates the extension MYEXT of data type MYTYPE in the NDF called
myndf.
setext xname=ccdpack ndf=abc erase cname=filter noloop
This deletes the FILTER component of the CCDPACK extension in the NDF
called abc.
setext abc ccdpack put cname=filter cvalue=B ctype=_char noloop
This assigns the character value "B" to the FILTER component of the
CCDPACK extension a the NDF called abc.
setext virgo plate put cname=pitch shape=2 cvalue=[32,16]

ctype=_byte noloop
This sets the byte 2-element vector of component PITCH of the PLATE
extension in the NDF called virgo. The first element of PITCH is set
to 32 and the second to 16.
setext virgo plate rename cname=filter newname=waveband noloop
This renames the FILTER component of the PLATE extension in the NDF
called virgo to WAVEBAND.



Notes
~~~~~


+ The "PUT" option allows the creation of extension components with
any of the primitive data types.
+ The task creates the extension automatically if it does not exist
  and only allows one extension to be modified at a time.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: FITSIMP, FITSLIST, NDFTRACE; CCDPACK: CCDEDIT; Figaro:
FITSKEYS; HDSTRACE; IRAS90: IRASTRACE, PREPARE.


Copyright
~~~~~~~~~
Copyright (C) 1993 Science & Engineering Research Council. Copyright
(C) 1995, 1999-2000, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2010 Science & Technology Facilities Council. All Rights
Reserved.


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


