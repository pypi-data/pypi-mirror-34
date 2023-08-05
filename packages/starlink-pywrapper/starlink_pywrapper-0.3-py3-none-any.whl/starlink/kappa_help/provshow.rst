

PROVSHOW
========


Purpose
~~~~~~~
Displays provenance information for an NDF


Description
~~~~~~~~~~~
This application displays details of the NDFs that were used in the
creation of the supplied NDF. This information is read from the
PROVENANCE extension within the NDF, and includes both immediate
parent NDFs and older ancestor NDFs (i.e. the parents of the parents,
etc.).
Each displayed NDF (see parameter SHOW) is described in a block of
lines. The first line holds an integer index for the NDF followed by
the path to that NDF. Note, this path is where the NDF was when the
provenance information was recorded. It is of course possible that the
NDF may subsequently have been moved or deleted.
The remaining lines in the NDF description are as follows:
"Parents" -- A comma-separated list of integers that are the indices
of the immediate parents of the NDF. These are the integers that are
displayed on the first line of each NDF description.
"Date" -- The formatted UTC date and time at which the provenance
information for the NDF was recorded.
"Creator" -- A string identifying the software that created the NDF.
"More" -- A summary of any extra information about the NDF stored with
the provenance information. In general this may be completely
arbitrary and so full details cannot be given on a single line. If the
NDF has no extra information, this item will not be present.
"History" -- This is only displayed if parameter HISTORY is set to a
TRUE value. It contains information copied from the History component
of the ancestor NDF. See Parameter HISTORY.
In addition, a text file can be created containing the paths for the
direct parents of the supplied NDF. See Parameter PARENTS.


Usage
~~~~~


::

    
       provshow ndf [show]
       



ADAM parameters
~~~~~~~~~~~~~~~



DOTFILE = FILENAME (Read)
`````````````````````````
Name of a new text file in which to store a description of the
provenance tree using the "dot" format. This file can be visualised
using third-party tools such as Graphviz, ZGRViewer, OmniGraffle, etc.



HIDE = _LOGICAL (Read)
``````````````````````
If TRUE, then any ancestors which are flagged as "hidden" (for
example, using PROVREM) are excluded from the display. If FALSE, then
all requested ancestors, whether hidden or not, are included in the
display (but hidden ancestors will be highlighted as such). Note,
choosing to exclude hidden ancestors may change the index displayed
for each ancestor. The default is to display hidden ancestors if and
only if history is being displayed (see Parameter HISTORY). []



HISTORY = _LOGICAL (Read)
`````````````````````````
If TRUE, any history records stored with each ancestor are included in
the displayed information. Since the amount of history information
displayed can be large, and thus swamp other information, the default
is not to display history information.
When an existing NDF is used in the creation of a new NDF, the
provenance system will copy selected records from the HISTORY
component of the existing NDF and store them with the provenance
information in the new NDF. The history records copied are those that
describe operations performed on the existing NDF itself. Inherited
history records that describe operations performed on ancestors of the
existing NDF are not copied. [FALSE]



INEXT = LITERAL (Read)
``````````````````````
Determines which ancestor to display next. Only used if parameter SHOW
is set to "Tree". The user is re-prompted for a new value for this
parameter after each NDF is displayed. The new value should be the
integer identifier for one of the parents of the currently displayed
NDF. Alternatively, the string "up" can be supplied, causing the
previously displayed NDF to be displayed again.



NDF = NDF (Read)
````````````````
The NDF data structure.



PARENTS = FILENAME (Read)
`````````````````````````
Name of a new text file in which to put the paths to the direct
parents of the supplied NDF. These are written one per line with no
extra text. If null, no file is created. [!]



SHOW = LITERAL (Read)
`````````````````````
Determines which ancestors are displayed on the screen. It can take
any of the following case-insensitive values (or any abbreviation).


+ "All" -- Display all ancestors, including the supplied NDF itself.
+ "Roots" -- Display only the root ancestors (i.e. ancestors that do
not themselves have any recorded parents). The supplied NDF itself is
not displayed.
+ "Parents" -- Display only the direct parents of the supplied NDF.
The supplied NDF itself is not displayed.
+ "Tree" -- Display the top level NDF and then asks the user which
  parent to display next (see parameter INEXT). The whole family tree
  can be navigated in this way.

["All"]



Examples
~~~~~~~~
provshow m51
This displays information about the NDF m51, and all its recorded
ancestors.
provshow m51 roots
This displays information about the root ancestors of the NDF m51.
provshow m51 parents
This displays information about the direct parents of the NDF m51.



Notes
~~~~~


+ An input NDF is included in the provenance of an output NDF only if
the Data component of the input NDF is mapped for read or update
access by the application. In other words, input NDFs which are
accessed only for their meta-data (e.g. WCS information) are not
included in the output provenance of an application.
+ If a KAPPA application uses one or more input NDFs to create an
output NDF, the output NDF may or may not contain provenance
information depending on two things: 1) whether any of the input NDFs
already contain provenance information, and 2) the value of the
AUTOPROV environment variable. It is usually necessary to set the
AUTOPROV variable to "1" in order to create output NDFs that contain
provenance information. The exception to this if you are supplied with
NDFs from another source that already contain provenance. If such NDFs
are used as inputs to KAPPA applications, then the output NDFs will
contain provenance even if the AUTOPROV variable is unset. However,
setting AUTOPROV to "0" will always prevent provenance information
being stored in the output NDFs.
+ Some other packages, such as CCDPACK, follow the same strategy for
  creating and propagating provenance information.




Related Applications
~~~~~~~~~~~~~~~~~~~~
KAPPA: PROVADD, HISLIST.


Copyright
~~~~~~~~~
Copyright (C) 2008-2009 Science & Technology Facilities Council. All
Rights Reserved.


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


