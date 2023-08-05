

WCSSHOW
=======


Purpose
~~~~~~~
Examines the internal structure of an AST Object


Description
~~~~~~~~~~~
This application allows you to examine an AST Object stored in a
specified NDF or HDS object, or a catalogue. The structure can be
dumped to a text file, or a Graphical User Interface can be used to
navigate through the structure (see Parameter LOGFILE). A new FrameSet
can also be stored in the WCS component of an NDF (see Parameter
NEWWCS). This allows an NDF WCS component to be dumped to a text file,
edited, and then restored to the NDF.
The GUI main window contains the attribute values of the supplied AST
Object. Only those associated with the Object's class are displayed
initially, but attributes of the Objects parent classes can be
displayed by clicking one of the class button to the top left of the
window.
If the Object contains attributes which are themselves AST Objects
(such as the Frames within a FrameSet), then new windows can be
created to examine these attributes by clicking over the attribute
name.


Usage
~~~~~


::

    
       wcsshow ndf object logfile newwcs full quiet
       



ADAM parameters
~~~~~~~~~~~~~~~



CAT = FILENAME (Read)
`````````````````````
A catalogue containing a positions list such as produced by
applications LISTMAKE, CURSOR, etc. If supplied, the WCS Information
in the catalogue is displayed. If a null (!) is supplied, the WCS
information in the NDF specified by Parameter NDF is displayed. [!]



FULL = _INTEGER (Read)
``````````````````````
This parameter is a three-state flag and takes values of -1, 0 or +1.
It controls the amount of information included in the output generated
by this application. If FULL is zero, then a modest amount of non-
essential but useful information will be included in the output. If
FULL is negative, all non-essential information will be suppressed to
minimise the amount of output, while if it is positive, the output
will include the maximum amount of detailed information about the
Object being examined. [current value]



LOGFILE = FILENAME (Write)
``````````````````````````
The name of the text file in which to store a dump of the specified
AST Object. If a null (!) value is supplied, no log file is created.
If a log file is given, the Tk browser window is not produced. [!]



NDF = NDF (Read or Update)
``````````````````````````
If an NDF is supplied, then its WCS FrameSet is displayed. If a null
(!) value is supplied, then the Parameter OBJECT is used to specify
the AST Object to display. Update access is required to the NDF if a
value is given for Parameter NEWWCS. Otherwise, only read access is
required. Only accessed if a null (!) value is supplied for CAT.



NEWWCS = GROUP (Read)
`````````````````````
A group expression giving a dump of an AST FrameSet which is to be
stored as the WCS component in the NDF given by Parameter NDF. The
existing WCS component is unchanged if a null value is supplied. The
value supplied for this parameter is ignored if a null value is
supplied for Parameter NDF. The Base Frame in the FrameSet is assumed
to be the GRID Frame. If a value is given for this parameter, then the
log file or Tk browser will display the new FrameSet (after being
stored in the NDF and retrieved). [!]



OBJECT = LITERAL (Read)
```````````````````````
The HDS object containing the AST Object to display. Only accessed if
parameters NDF and CAT are null. It must have an HDS type of WCS, must
be scalar, and must contain a single 1-D array component with name
DATA and type _CHAR.



QUIET = _LOGICAL (Read)
```````````````````````
If TRUE, then the structure of the AST Object is not displayed (using
the Tk GUI). Other functions are unaffected. If a null (!) value is
supplied, the value used is TRUE if a non-null value is supplied for
Parameter LOGFILE or Parameter NEWWCS, and FALSE otherwise. [!]



Examples
~~~~~~~~
wcsshow m51
Displays the WCS component of the NDF m51 in a Tk GUI.
wcsshow m51 logfile=m51.ast
Dumps the WCS component of the NDF m51 to text file m51.ast.
wcsshow m51 newwcs=^m51.ast
Reads a FrameSet from the text file m51.ast and stores it in the WCS
component of the NDF m51. For instance, the text file m51.ast could be
an edited version of the text file created in the previous example.
wcsshow object="~/agi_starprog.agi_3800_1.picture(4).more.ast_plot"
Displays the AST Plot stored in the AGI database with X windows
picture number 4.



Copyright
~~~~~~~~~
Copyright (C) 1998-1999, 2004 Central Laboratory of the Research
Councils. Copyright (C) 2006 Particle Physics & Astronomy Research
Council. Copyright (C) 2008 Science and Technology Facilities Council.
All Rights Reserved.


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


