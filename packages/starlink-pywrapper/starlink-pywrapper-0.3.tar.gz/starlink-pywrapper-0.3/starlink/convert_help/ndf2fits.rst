

NDF2FITS
========


Purpose
~~~~~~~
Converts NDFs into FITS files


Description
~~~~~~~~~~~
This application converts one or more NDF datasets into FITS-format
files. NDF2FITS stores any variance and quality information in IMAGE
extensions (`sub-files') within the FITS file; and it uses binary
tables to hold any NDF-extension data present, except for the FITS-
airlock extension, which may be merged into the output FITS file's
headers.
You can select which NDF array components to export to the FITS file,
and choose the data type of the data and variance arrays. You can
control whether or not to propagate extensions and history
information.
The application also accepts NDFs stored as top-level components of an
HDS container file.
Both NDF and FITS use the term extension, and they mean different
things. Thus to avoid confusion in the descriptions below, the term
`sub-file' is used to refer to a FITS IMAGE, TABLE or BINTABLE Header
and Data Unit (HDU).


Usage
~~~~~


::

    
       ndf2fits in out [comp] [bitpix] [origin]
       



ADAM parameters
~~~~~~~~~~~~~~~



ALLOWTAB = _LOGICAL (Read)
``````````````````````````
If TRUE, tables of world co-ordinates may be written using the TAB
algorithm as defined in the FITS-WCS Paper III. Examples where such a
table might be present in the WCS include wavelengths of pre-scrunched
spectra, and the presence of distortions that prevent co-ordinates
being defined by analytical expressions. Since many FITS readers are
yet to support the TAB algorithm, which uses a FITS binary-table
extension to store the co-ordinates, this parameter permits this
facility to be disabled. [TRUE]



AXISORDER = LITERAL (Read)
``````````````````````````
Specifies the order of WCS axes within the output FITS header. It can
be either null (!), "Copy" or a space-separated list of axis symbols
(case insensitive). If it is null, the order is determined
automatically so that the ith WCS axis is the WCS axis that is most
nearly parallel to the ith pixel axis. If it is "Copy", the ith WCS
axis in the FITS header is the ith WCS axis in the NDF's current WCS
Frame. Otherwise, the string must be a space-separated list of axis
symbols that gives the order for the WCS axes. An error is reported if
the list does not contain any of the axis symbols present in the
current WCS Frame, but no error is reported if the list also contains
other symbols. [!]



BITPIX = GROUP (Read)
`````````````````````
The FITS bits-per-pixel (BITPIX) value for each conversion. This
specifies the data type of the output FITS file. Permitted values are:
8 for unsigned byte, 16 for signed word, 32 for integer, 64 for 64-bit
integer, -32 for real, -64 for double precision. There are three other
special values.


+ - BITPIX=0 will cause the output file to have the data type
equivalent to that of the input NDF.
+ - BITPIX=-1 requests that the output file has the data type
corresponding to the value of the BITPIX keyword in the NDF's FITS
extension. If the extension or BITPIX keyword is absent, the output
file takes the data type of the input array.
+ - BITPIX="Native" requests that any scaled arrays in the NDF be
  copied to the scaled data type. Otherwise behaviour reverts to
  BITPIX=-1, which may in turn be effectively BITPIX=0. The case-
  insensitive value may be abbreviated to "n".

BITPIX must be enclosed in double quotes and may be a list of comma-
separated values to be applied to each conversion in turn. An error
results if more values than the number of input NDFs are supplied. If
too few are given, the last value in the list applied to all the
conversions. The given values must be in the file may be used. If more
than one line is required to enter the information at a prompt then
place a "-" at the end of each line where a continuation line is
desired. [0]



CHECKSUM = _LOGICAL (Read)
``````````````````````````
If TRUE, each header and data unit in the FITS file will contain the
integrity-check keywords CHECKSUM and DATASUM immediately before the
END card. [TRUE]



COMP = GROUP (Read)
```````````````````
The list of array components to attempt to transfer to each FITS file.
The acceptable values are "D" for the main data array "V" for
variance, "Q" for quality, or any permutation thereof. The special
value "A" means all components, i.e. COMP="DVQ". Thus COMP="VD"
requests that both the data array and variance are to be converted if
present. During processing at least one, if not all, of the requested
components must be present, otherwise an error is reported and
processing turns to the next input NDF. If the DATA component is in
the list, it will always be processed first into the FITS primary
array. The order of the variance and quality in COMP decides the order
they will appear in the FITS file.
The choice of COMP may affect automatic quality masking. See "Quality
Masking" for the details.
COMP may be a list of comma-separated values to be applied to each
conversion in turn. The list must be enclosed in double quotes. An
error results if more values than the number of input NDFs are
supplied. If too few are given, the last value in the list is applied
to the remainder of the NDFs; thus a single value is applied to all
the conversions. The given values must be in the same order as that of
the input NDFs. Indirection through a text file may be used. If more
than one line is required to enter the information at a prompt then
place a "-" at the end of each line where a continuation line is
desired. ["A"]



CONTAINER = _LOGICAL (Read)
```````````````````````````
If TRUE, the supplied IN files are any multi-NDF HDS container files,
in which the NDFs reside as top-level components. This option is
primarily intended to support the UKIRT format, where the NDFs are
named .In, n >=1, and one named HEADER containing global metadata in
its FITS airlock. The .In NDFs may also contain FITS airlocks, storing
metadata pertinent to that NDF, such as observation times. The
individual NDFs often represent separate integrations nodded along a
slit or spatially. Note that this is not a group, so a single value
applies to all the supplied input files. [FALSE]



DUPLEX = _LOGICAL (Read)
````````````````````````
This qualifies the effect of PROFITS=TRUE. DUPLEX=FALSE means that the
airlock headers only appear with the primary array. DUPLEX=TRUE,
propagates the FITS airlock headers for other array components of the
NDF. [FALSE]



ENCODING = LITERAL (Read)
`````````````````````````
Controls the FITS keywords which will be used to encode the World Co-
ordinate System (WCS) information within the FITS header. The value
supplied should be one of the encodings listed in the "World Co-
ordinate Systems" section below. In addition, the value "Auto" may
also be supplied, in which case a suitable default encoding is chosen
based on the contents of the NDF's FITS extension and WCS component.
["Auto"]



IN = LITERAL (Read)
```````````````````
The names of the NDFs to be converted into FITS format. It may be a
list of NDF names or direction specifications separated by commas and
enclosed in double quotes. NDF names may include wild-cards ("*",
"?"). Indirection may occur through text files (nested up to seven
deep). The indirection character is "^". If extra prompt lines are
required, append the continuation character "-" to the end of the
line. Comments in the indirection file begin with the character "#".



MERGE = _LOGICAL (Read)
```````````````````````
Whether or not to merge the FITS-airlocks' headers of the header NDF
of a UKIRT multi-NDF container file with its sole data NDF into the
primary header and data unit (HDU). This parameter is only used when
CONTAINER is TRUE; and when the container file only has two component
NDFs: one data NDF of arbitrary name, and the other called HEADER that
stores the global headers of the dataset. [TRUE]



NATIVE = _LOGICAL (Read)
````````````````````````
If a TRUE value is given for Parameter NATIVE, then World Co-ordinate
System (WCS) information will be written to the FITS header in the
form of a `native' encoding (see "World Co-ordinate Systems" below).
This will be in addition to the encoding specified using Parameter
ENCODING, and will usually result in two descriptions of the WCS
information being stored in the FITS header (unless the ENCODING
parameter produces a native encoding in which case only one native
encoding is stored in the header). Including a native encoding in the
header will enable other AST-based software (such as FITS2NDF) to
reconstruct the full details of the WCS information. The other non-
native encodings will usually result in some information being lost.
[FALSE]



ORIGIN = LITERAL (Read)
```````````````````````
The origin of the FITS files. This becomes the value of the ORIGIN
keyword in the FITS headers. If a null value is given it defaults to
"Starlink Software". [!]



OUT = LITERAL (Write)
`````````````````````
The names for the output FITS files. These may be enclosed in double
quotes and specified as a list of comma-separated names, or they may
be created automatically on the basis of the input NDF names. To do
this, the string supplied for this parameter should include an
asterisk "*". This character is a token that represents the name of
the corresponding input NDF, but with a file type of ".fit" instead of
".sdf", and with no directory specification. Thus, simply supplying
"*" for this parameter will create a group of output files in the
current directory with the same names as the input NDFs, but with file
type ".fit". You can also specify some simple editing to be performed.
For instance, "new-*|.fit|.fits|" will add the string "new-" to the
start of every file name, and will substitute the string ".fits" for
the original string ".fit".
NDF2FITS will not permit you to overwrite an existing FITS file,
unless you supply an exclamation-mark prefix (suitably escaped if you
are using a UNIX shell).



PROEXTS = _LOGICAL (Read)
`````````````````````````
If TRUE, the NDF extensions (other than the FITS extension) are
propagated to the FITS files as FITS binary-table sub-files, one per
structure of the hierarchy. [FALSE]



PROFITS = _LOGICAL (Read)
`````````````````````````
If TRUE, the contents of the FITS extension of the NDF are merged with
the header information derived from the standard NDF components. See
the Notes for details of the merger. [TRUE]



PROHIS = _LOGICAL (Read)
````````````````````````
If TRUE, any NDF history records are written to the primary FITS
header as HISTORY cards. These follow the mandatory headers and any
merged FITS-extension headers (see Parameter PROFITS). [TRUE]



PROVENANCE = LITERAL (Read)
```````````````````````````
This controls the export of NDF provenance information to the FITS
file. Allowed values are as follows.
"None" -- No provenance is written.
"CADC" -- The CADC headers are written. These record the number and
paths of both the direct parents of the NDF being converted, and its
root ancestors (the ones without parents). It also modifies the
PRODUCT keyword to be unique for each FITS sub-file.
"Generic" -- Encapsulates the entire PROVENANCE structure in FITS
headers in sets of five character-value indexed headers. there is a
set for the current NDF and each parent.
See Section "Provenance" for more details. ["None"]



USEAXIS = _LOGICAL (Read)
`````````````````````````
Whether or not to export AXIS co-ordinates to an alternate world co-
ordinate representation in the FITS headers. Such an alternate may
require a FITS sub-file to store lookup tables of co-ordinates using
the -TAB projection type. The default null value requests no AXIS
information be stored unless the current NDF contains AXIS information
but no WCS. An explicit TRUE or FALSE selection demands the chosen
setting irrespective of how the current NDF stores co-ordinate
information. [!]



Examples
~~~~~~~~
ndf2fits horse logo.fit d
This converts the NDF called horse to the new FITS file called
logo.fit. The data type of the FITS primary data array matches that of
the NDF's data array. The FITS extension in the NDF is merged into the
FITS header of logo.fit.
ndf2fits horse !logo.fit d proexts
This converts the NDF called horse to the FITS file called logo.fit.
An existing logo.fit will be overwritten. The data type of the FITS
primary data array matches that of the NDF's data array. The FITS
extension in the NDF is merged into the FITS header of logo.fit. In
addition any NDF extensions (apart from FITS) are turned into binary
tables. that follow the primary header and data unit.
ndf2fits horse logo.fit noprohis
This converts the NDF called horse to the new FITS file called
logo.fit. The data type of the FITS primary data array matches that of
the NDF's data array. The FITS extension in the NDF is merged into the
FITS header of logo.fit. Should horse contain variance and quality
arrays, these are written in IMAGE sub-files. Any history information
in the NDF is not relayed to the FITS file.
ndf2fits "data/a*z" * comp=v noprofits bitpix=-32
This converts the NDFs with names beginning with "a" and ending in "z"
in the directory called data into FITS files of the same name and with
a file extension called .fit. The variance array becomes the data
array of each new FITS file. The data type of the FITS primary data
array single-precision floating point. Any FITS extension in the NDF
is ignored.
ndf2fits "abc,def" "jvp1.fit,jvp2.fit" comp=d bitpix="16,-64"
This converts the NDFs called abc and def into new FITS files called
jvp1.fit and jvp2.fit respectively. The data type of the FITS primary
data array is signed integer words in jvp1.fit, and double-precision
floating point in jvp2.fit. The FITS extension in each NDF is merged
into the FITS header of the corresponding FITS file.
ndf2fits horse logo.fit d native encoding="fits-wcs"
This is the same as the first example except that the co-ordinate
system information stored in the NDF's WCS component is written to the
FITS file twice; once using the FITS-WCS headers, and once using a
special set of `native' keywords recognised by the AST library (see
SUN/210). The native encoding provides a `loss-free' means of
transferring co-ordinate system information (i.e. no information is
lost; other encodings may cause information to be lost). Only
applications based on the AST library (such as FITS2NDF) are able to
interpret native encodings.
ndf2fits u20040730_00675 merge container accept
This converts the UIST container file u20040730_00675.sdf to new FITS
file u20040730_00675.fit, merging its .I1 and .HEADER structures into
a single NDF before the conversion. The output file has only one
header and data unit.
ndf2fits in=c20011204_00016 out=cgs4_16.fit container
This converts the CGS4 container file c20011204_00016.sdf to the
multiple-extension FITS file cgs4_16.fit. The primary HDU has the
global metadata from the .HEADER's FITS airlock. The four integrations
in I1, I2, I3, and I4 components of the container file are converted
to FITS IMAGE sub-files.
ndf2fits in=huge out=huge.fits comp=d bitpix=n
This converts the NDF called huge to the new FITS file called
huge.fits. The data type of the FITS primary data array matches that
of the NDF's scaled data array. The scale and offset coefficients used
to form the FITS array are also taken from the NDF's scaled array.
ndf2fits in=huge out=huge.fits comp=d bitpix=-1
As the previous example, except that the data type of the FITS primary
data array is that given by the BITPIX keyword in the FITS airlock of
NDF huge and the scaling factors are determined.



Notes
~~~~~
The rules for the conversion are as follows:

+ The NDF main data array becomes the primary data array of the FITS
file if it is in value of Parameter COMP, otherwise the first array
defined by Parameter COMP will become the primary data array. A
conversion from floating point to integer or to a shorter integer type
will cause the output array to be scaled and offset, the values being
recorded in keywords BSCALE and BZERO. There is an offset (keyword
BZERO) applied to signed byte and unsigned word types to make them
unsigned-byte and signed-word values respectively in the FITS array
(this is because FITS does not support these data types).
+ The FITS keyword BLANK records the bad values for integer output
types. Bad values in floating-point output arrays are denoted by IEEE
not-a-number values.
+ The NDF's quality and variance arrays appear in individual FITS
IMAGE sub-files immediately following the primary header and data
unit, unless that component already appears as the primary data array.
The quality array will always be written as an unsigned-byte array in
the FITS file, regardless of the value of the Parameter BITPIX.
+ Here are details of the processing of standard items from the NDF
  into the FITS header, listed by FITS keyword. SIMPLE, EXTEND, PCOUNT,
  GCOUNT --- all take their default values. BITPIX, NAXIS, NAXISn ---
  are derived directly from the NDF data array; however the BITPIX in
  the FITS airlock extension is transferred when Parameter BITPIX is -1.
  CRVALn, CDELTn, CRPIXn, CTYPEn, CUNITn --- are derived from the NDF
  WCS component if possible (see "World Co-ordinate Systems"). If this
  is not possible, and if PROFITS is TRUE, then it copies the headers of
  a valid WCS specified in the NDF's FITS airlock. Should that attempt
  fail, the last resort tries the NDF AXIS component, if it exists. If
  its co-ordinates are non-linear, the AXIS co-ordinates may be exported
  in a -TAB sub-file subject to the value of Parameter USEAXIS. OBJECT,
  LABEL, BUNIT --- the values held in the NDF's TITLE, LABEL, and UNITS
  components respectively are used if they are defined; otherwise any
  values found in the FITS extension are used (provided Parameter
  PROFITS is TRUE). For a variance array, BUNIT is assigned to
  "(<unit>)**2", where <unit> is the DATA unit; the BUNIT header is
  absent for a quality array. DATE --- is created automatically. ORIGIN
  --- inherits any existing ORIGIN card in the NDF FITS extension,
  unless you supply a value through parameter ORIGIN other than the
  default "Starlink Software". EXTNAME --- is the array-component name
  when the EXTNAME appears in the primary header or an IMAGE sub-file.
  In a binary-table derived from an NDF extension, EXTNAME is the path
  of the extension within the NDF, the path separator being the usual
  dot. The path includes the indices to elements of any array structures
  present; the indices are in a comma-separated list within parentheses.

If the component is too long to fit within the header (68 characters),
EXTNAME is set to '@EXTNAMEF'. The full path is then stored in keyword
EXTNAMEF using the HEASARC Long-string CONTINUE convention
(http://fits.gsfc.nasa.gov/registry/continue_keyword.html) EXTVER ---
is only set when EXTNAME (q.v.) cannot accommodate the component name,
and it is assigned the HDU index to provide a unique identifier.
EXTLEVEL --- is the level in the hierarchical structure of the
extension. Thus a top-level extension has value 1, sub-components of
this extension have value 2 and so on. EXTTYPE --- is the data type of
the NDF extension used to create a binary table. EXTSHAPE --- is the
shape of the NDF extension used to create a binary table. It is a
comma-separated list of the dimensions, and is 0 when the extension is
not an array. HDUCLAS1, HDUCLASn --- "NDF" and the array-component
name respectively. LBOUNDn --- is the pixel origin for the nth
dimension when any of the pixel origins is not equal to 1. (This is
not a standard FITS keyword.) XTENSION, BSCALE, BZERO, BLANK and END
--- are not propagated from the NDF's FITS extension. XTENSION will be
set for any sub-file. BSCALE and BZERO will be defined based on the
chosen output data type in comparison with the NDF array's type, but
cards with values 1.0 and 0.0 respectively are written to reserve
places in the header section. These `reservation' cards are for
efficiency and they can always be deleted later. BLANK is set to the
Starlink standard bad value corresponding to the type specified by
BITPIX, but only for integer types and not for the quality array. It
appears regardless of whether or not there are bad values actually
present in the array; this is for the same efficiency reasons as
before. The END card terminates the FITS header. HISTORY headers are
propagated from the FITS airlock when PROFITS is TRUE, and from the
NDF history component when PROHIS is TRUE. DATASUM and CHECKSUM ---
data-integrity keywords are written when Parameter CHECKSUM is TRUE,
replacing any existing values. When Parameter CHECKSUM is FALSE and
PROFITS is TRUE any existing values inherited from the FITS airlock
are removed to prevent storage of invalid checksums relating to
another data file.
See also the sections "Provenance" and "World Co-ordinate Systems" for
details of headers used to describe the PROVENANCE extension and WCS
information respectively.


+ Extension information may be transferred to the FITS file when
  PROEXTS is TRUE. The whole hierarchy of extensions is propagated in
  order. This includes substructures, and arrays of extensions and
  substructures. However, at present, any extension structure containing
  only substructures is not propagated itself (as zero-column tables are
  not permitted), although its substructures may be converted.

Each extension or substructure creates a one-row binary table, where
the columns of the table correspond to the primitive (non-structure)
components. The name of each column is the component name. The column
order is the same as the component order. The shapes of multi-
dimensional arrays are recorded using the TDIMn keyword, where n is
the column number. The HEASARCH convention for specifying the width of
character arrays (keyword TFORMn='rAw', where r is the total number of
characters in the column and w is the width of an element) is used.
The EXTNAME, EXTTYPE, EXTSHAPE and EXTLEVEL keywords (see above) are
written to the binary-table header.
There are additional rules if a multi-NDF container file is being
converted (see Parameter CONTAINER). This excludes the case where
there are but two NDFs---one data and the other just headers---that
have already been merged (see Parameter MERGE):

+ For multiple NDFs a header-only HDU may be created followed by an
IMAGE sub-file containing the data array (or whichever other array is
first specified by COMP).
+ BITPIX for the header HDU is set to an arbitrary 8.
+ Additional keywords are written for each IMAGE sub-file HDSNAME ---
  is the NDF name for a component NDF in a multi-NDF container file, for
  example "I2". HDSTYPE --- is set to "NDF" for a component NDF in a
  multi-NDF container file.




World Co-ordinate Systems
~~~~~~~~~~~~~~~~~~~~~~~~~
Any co-ordinate system information stored in the WCS component of the
NDF is written to the FITS header using one of the following encoding
systems (the encodings used are determined by parameters ENCODING and
NATIVE):
"FITS-IRAF" --- This uses keywords CRVALi CRPIXi, CDi_j, and the
system commonly used by IRAF. It is described in the document "World
Coordinate Systems Representations Within the FITS Format" by R.J.
Hanisch and D.G. Wells, 1988, available by ftp from fits.cv.nrao.edu
/fits/documents/wcs/wcs88.ps.Z.
"FITS-WCS" --- This is the FITS standard WCS encoding scheme described
in the paper "Representation of celestial coordinates in FITS"
(http://www.atnf.csiro.au/people/mcalabre/WCS/). It is very similar to
"FITS-IRAF" but supports a wider range of projections and co-ordinate
systems.
"FITS-WCS(CD)" --- This is the same as "FITS-WCS" except that the
scaling and rotation of the data array is described by a CD matrix
instead of a PC matrix with associated CDELT values.
"FITS-PC" --- This uses keywords CRVALi, CDELTi, CRPIXi, PCiiijjj,
etc., as described in a previous (now superseded) draft of the above
FITS world co-ordinate system paper by E.W.Greisen and M.Calabretta.
"FITS-AIPS" --- This uses conventions described in the document "Non-
linear Coordinate Systems in AIPS" by Eric W. Greisen (revised 9th
September, 1994), available by ftp from fits.cv.nrao.edu
/fits/documents/wcs/aips27.ps.Z. It is currently employed by the AIPS
data-analysis facility (amongst others), so its use will facilitate
data exchange with AIPS. This encoding uses CROTAi and CDELTi keywords
to describe axis rotation and scaling.
"FITS-AIPS++" --- This is an extension to FITS-AIPS which allows the
use of a wider range of celestial projections, as used by the AIPS++
project.
"FITS-CLASS" --- This uses the conventions of the CLASS project. CLASS
is a software package for reducing single-dish radio and sub-mm
spectroscopic data. It supports double sideband spectra. See
http://www.iram.fr/IRAMFR/GILDAS/doc/html/class-html/class.html.
"DSS" --- This is the system used by the Digital Sky Survey, and uses
keywords AMDXn, AMDYn, PLTRAH, etc.
"NATIVE" --- This is the native system used by the AST library (see
SUN/210) and provides a loss-free method for transferring WCS
information between AST-based application. It allows more complicated
WCS information to be stored and retrieved than any of the other
encodings.
Values for FITS keywords generated by the above encodings will always
be used in preference to any corresponding keywords found in the FITS
extension (even if PROFITS is TRUE). If this is not what is required,
the WCS component of the NDF should be erased using the KAPPA command
ERASE before running NDF2FITS. Note, if PROFITS is TRUE, then any WCS-
related keywords in the FITS extension which are not replaced by
keywords derived from the WCS component may appear in the output FITS
file. If this causes a problem, then PROFITS should be set to FALSE or
the offending keywords removed using KAPPA FITSEDIT, for example.


Provenance
~~~~~~~~~~
The following PROVENANCE headers are written if parameter PROVENANCE
is set to "Generic". PRVPn --- is the path of the <nth> NDF. PRVIn ---
is a comma-seapated list of the identifiers of the direct parents for
<nth> ancestor. PRVDn --- is the creation date of <nth> ancestor in
ISO order. PRVCn --- is the software used to create the <nth>
ancestor. PRVMn --- lists the contents of the MORE structure of <nth>
parent. All have value '<unknown>' if the information could not be
found, except for the PRVMn header, which is omitted if there is no
MORE information to record. The index n used in each keyword's name is
the provenance identifier for the NDF, and starts at 0 for the NDF
being converted to FITS.
The following PROVENANCE headers are written if parameter PROVENANCE
is set to "CADC". PRVCNT --- is the number of immediate parents. PRVm
--- is name of the mth immediate parent. OBSCNT --- is the number of
root ancestor OBSm headers. OBSm --- is mth root ancestor identifier
from its MORE.OBSIDSS component. FILEID --- is the name of the output
FITS file, omitting any file extension.
PRODUCT is modified or added to each sub-file's header to be the
primary header's value of PRODUCT with a '_<extnam>' suffix, where
<extnam> is the extension name in lowercase.
When PROFITS is TRUE any existing provenance keywords in the FITS
airlock are not copied to the FITS file.


Quality Masking
~~~~~~~~~~~~~~~


+ NDF automatic quality masking is a facility whereby any bad quality
  information (flagged by the bad-bits mask) present can be incorporated
  in the data or variance as bad values. NDF2FITS uses this facility in
  exported data variance information provided the quality array is not
  transferred. Thus if a QUALITY component is present in the input NDF,
  the data and any variance arrays will not be masked whenever Parameter
  COMP's value is 'A' or contains 'Q'.




Special Formats
~~~~~~~~~~~~~~~
In the general case, NDF extensions (excluding the FITS extension) may
be converted to one-row binary tables in the FITS file when Parameter
PROEXTS is TRUE. This preserves the information, but it may not be
accessible to the recipient's FITS reader. Therefore, in some cases it
is desirable to understand the meanings of certain NDF extensions, and
create standard FITS products for compatibility.
At present only one product is supported, but others may be added as
required.
o AAO 2dF
Standard processing is used except for the 2dF FIBRES extension and
its constituent structures. The NDF may be restored from the created
FITS file using FITS2NDF. The FIBRES extension converts to the second
binary table in the FITS file (the NDF_CLASS extension appears in the
first).
To propagate the OBJECT substructure, NDF2FITS creates a binary table
of constant width (224 bytes) with one row per fibre. The total number
of rows is obtained from component NUM_FIBRES. If a possible OBJECT
component is missing from the NDF, a null column is written for that
component. The columns inherit the data types of the OBJECT
structure's components. Column meanings and units are assigned based
upon information in the reference given below.
The FIELD structure components are converted into additional keywords
of the same name in the binary-table header, with the exception that
components with names longer than 8 characters have abbreviated
keywords: UNALLOCxxx become UNAL-xxx (xxx=OBJ, GUI, or SKY), CONFIGMJD
becomes CONFMJD, and xSWITCHOFF become xSWTCHOF (x=X or Y). If any
FIELD component is missing it is ignored.
Keywords for the extension level, name, and type appear in the binary-
table header.
o JCMT SMURF
Standard processing is used except for the SMURF-type extension. This
contains NDFs such as EXP_TIME and TSYS. Each such NDF is treated like
the main NDF except that it is assumed that these extension NDFs have
no extensions of their own. FITS airlock information and HISTORY are
inherited from the parent NDF. Also the sub-file keywords are written:
EXTNAME gives the path to the NDF, EXTLEVEL records the extension
hierarchy level, and EXTTYPE is set to "NDF". Any non-NDF components
of the SMURF extension are written to a binary table in the normal
fashion.


References
~~~~~~~~~~
Bailey, J.A. 1997, 2dF Software Report 14, Version 0.5. NASA Office of
Standards and Technology, 1994, "A User's Guide for the Flexible Image
Transport System (FITS)", Version 3.1. NASA Office of Standards and
Technology, 1995, "Definition of the Flexible Image Transport System
(FITS)", Version 1.1.


Related Applications
~~~~~~~~~~~~~~~~~~~~
CONVERT: FITS2NDF; KAPPA: FITSDIN, FITSIN.


Copyright
~~~~~~~~~
Copyright (C) 1994 Science & Engineering Research Council. Copyright
(C) 1996-2000, 2004 Central Laboratory of the Research Councils.
Copyright (C) 2006 Particle Physics & Astronomy Research Council.
Copyright (C) 2007-2011, 2013 Science & Technology Facilities Council.
All Rights Reserved.


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


Implementation Status
~~~~~~~~~~~~~~~~~~~~~


+ All NDF data types are supported.




