

POL2MAP
=======


Purpose
~~~~~~~
Create Q, U and I maps from a group of POL-2 "spin&scan" data files


Description
~~~~~~~~~~~
This script creates maps (Q, U and I) and a vector catalogue from a
set of POL-2 observation. New observations can be added into the map
without the need to re-process previously processed observations. The
output maps are all in units of pW.
Note, with the default configuration this script can take up to an
hour to run for each observation on a typical SCUBA-2-capabale
computer.
Masking of models within makemap (AST, etc) can be based either on the
SNR of the map created as the end of each iteration, or on an external
map, or on a fixed circle centred on the origin - see parameter MASK.
By default, the Q, U, I and PI catalogue values are in units of
mJy/beam (see parameter Jy).


Usage
~~~~~


::

    
       pol2map in iout qout uout [cat] [config] [pixsize] [qudir] [mapdir]
               [mask] [masktype] [ipcor] [ipref] [reuse] [ref] [north] [reffcf]
               [debias] [retain] [maskout1] [maskout2] [msg_filter] [ilevel]
               [glevel] [logfile]
       



ADAM parameters
~~~~~~~~~~~~~~~



BINSIZE = _REAL (Read)
``````````````````````
The bin size in the output vector catalogue, in arcsec. The value
supplied for parameter PIXSIZE is used as the default for BINSIZE. An
error is reported if BINSIZE is smaller than PIXSIZE. []



CAT = LITERAL (Read)
````````````````````
The output FITS vector catalogue. No catalogue is created if null (!)
is supplied. The Q, U and PI values in this catalogue will be in units
of pW or mJy/beam, as selected using parameter JY . The bin size is
specified by parameter BINSIZE. [!]



CONFIG = LITERAL (Read)
```````````````````````
Extra parameter values to include in the MAKEMAP configuration used to
create both the I maps and the Q/U maps.
In general, it is important that the I, Q and U maps are all created
using the same configuration so that they can be compared directly.
However, if it is necessary to use a different configuration for I and
Q/U maps, the differences may be specified using the ADAM parameters
"ICONFIG" and "QUCONFIG". The ADAM parameter "CONFIG" specifies the
configuration parameters that are always used, whether an I map or a
Q/U map is being created. In all cases the configuration parameters
specified by "CONFIG" are applied first, followed by the configuration
parameters specified by "ICONFIG" (if creating an I map) or "QUCONFIG"
(if creating a Q or U map). Thus values supplied in "ICONFIG" or
"QUCONFIG" over-ride values for the same parameters specified in
"CONFIG".
The configurations specified by CONFIG, ICONFIG and QUCONFIG are
applied on top of the following set of default parameters:

+ -- ^$STARLINK_DIR/share/smurf/.dimmconfig_pol2.lis numiter = -200
  modelorder=(com,gai,pca,ext,flt,ast,noi)

maptol = 0.05 maptol_mask = <undef> maptol_mean = 0 maptol_box = 60
maptol_hits = 1
ast.mapspike_freeze = 5 pca.pcathresh = -150 pca.zero_niter = 0.5
com.zero_niter = 0.5 flt.zero_niter = 0.5 com.freeze_flags = 30

+ -- Additional parameters are also set, depending on the value of
parameter MASK. If MASK is set to "AUTO", the following parameters are
added to the above default config:
+ -- ast.skip = 10 ast.zero_snr = 3 ast.zero_snrlo = 2 ast.zero_freeze
  = 0.2

pca.pcathresh = -50 pca.zero_snr = 5 pca.zero_snrlo = 3
pca.zero_freeze = -1
com.zero_snr = 5 com.zero_snrlo = 3 com.zero_freeze = -1
flt.zero_snr = 5 flt.zero_snrlo = 3 flt.zero_freeze = -1

+ -- If MASK is set to "CIRCLE", the following parameters are added to
the above default config:
+ -- ast.zero_circle = 0.0083 (degrees, i.e. 30 arc-seconds)
pca.zero_circle = 0.0038 com.zero_circle = 0.0083 flt.zero_circle =
0.0083
+ -- The default value for pca.pcathresh indicated above will be
  changed if it is too high to allow convergence of the I maps within
  the number of iterations allowed by numiter (this change only occurs
  if parameter SKYLOOP is FALSE).

If MASK is set to the name of an NDF, this script creates fixed masks
from the NDF, and the following parameters are added to the above
default config:

+ -- ast.zero_mask = ref pca.zero_mask = mask2 com.zero_mask = mask2
flt.zero_mask = mask2
+ -- The above "ref" mask consists of clumps of pixel with SNR greater
  than 3, extended down to an SNR level of 2. The "mask2" mask consists
  of clumps of pixel with SNR greater than 5, extended down to an SNR
  level of 3. However, the above SNR levels are raised if necessary to
  ensure that the source occupies no more than 20% of the pixels within
  the "ref" mask, and 10% of the pixels within the "mask2" mask.

The same configuration is used for all three Stokes parameters - I, Q
and U with the exception that "com.noflag=1" is added to the
configuration when creating maps for Q and U.
If a configuration is supplied using parameter CONFIG, values supplied
for any of the above parameters will over-write the values specified
above. In addition, the following mandatory values are always appended
to the end of the used configuration:

+ -- flagslow = 0.01 downsampscale = 0 noi.usevar=1
+ -- If null (!) or "def" is supplied, the above set of default
  configuration parameters are used without change. ["def"]





DEBIAS = LOGICAL (Given)
````````````````````````
TRUE if a correction for statistical bias is to be made to percentage
polarization and polarized intensity in the output vector catalogue
specified by parameter CAT. [FALSE]



FCF = _REAL (Read)
``````````````````
The FCF value that is used to convert I, Q and U values from pW to
Jy/Beam. If a null (!) value is supplied a default value is used that
depends on the waveband in use - 725.0 for 850 um and 962.0 for 450
um. [!]



GLEVEL = LITERAL (Read)
```````````````````````
Controls the level of information to write to a text log file. Allowed
values are as for "ILEVEL". The log file to create is specified via
parameter "LOGFILE. In adition, the glevel value can be changed by
assigning a new integer value (one of starutil.NONE,
starutil.CRITICAL, starutil.PROGRESS, starutil.ATASK or
starutil.DEBUG) to the module variable starutil.glevel. ["ATASK"]



ICONFIG = LITERAL (Read)
````````````````````````
Extra parameter values to include in the MAKEMAP configuration used to
create I maps. The values specified by "ICONFIG" are applied after
those specified by "CONFIG". [!]



ILEVEL = LITERAL (Read)
```````````````````````
Controls the level of information displayed on the screen by the
script. It can take any of the following values (note, these values
are purposefully different to the SUN/104 values to avoid confusion in
their effects):


+ "NONE": No screen output is created
+ "CRITICAL": Only critical messages are displayed such as warnings.
+ "PROGRESS": Extra messages indicating script progress are also
displayed.
+ "ATASK": Extra messages are also displayed describing each atask
invocation. Lines starting with ">>>" indicate the command name and
parameter values, and subsequent lines hold the screen output
generated by the command.
+ "DEBUG": Extra messages are also displayed containing unspecified
  debugging information.

In adition, the glevel value can be changed by assigning a new integer
value (one of starutil.NONE, starutil.CRITICAL, starutil.PROGRESS,
starutil.ATASK or starutil.DEBUG) to the module variable
starutil.glevel. ["PROGRESS"]



IN = NDF (Read)
```````````````
A group of input files. Each specified file must be one of the
following types:


+ a raw POL-2 data file. Any supplied raw POL-2 data files will be
converted into time-series Q,U and I files using SMURF:CALCQU and
placed in the directory specified by parameter QUDIR. These will then
be converted into maps using SMURF:MAKEMAP, and placed in the
directory specified by parameter MAPDIR.
+ a time-series file holding Stokes Q, U or I values. Any supplied
time-series files will be converted into individual maps (one for each
file) using SMURF:MAKEMAP, and placed in the directory specified by
parameter MAPDIR. These maps are created only for the required Stokes
parameters - as indicated by parameters IOUT, QOUT and UOUT.
+ a two-dimensional map holding Stokes Q, U or I values. Any maps must
  be in units of pW. The final output I map is created by coadding any
  supplied I maps with the I maps created by this script. These coadded
  maps are created only for the required Stokes parameters - as
  indiciated by parameters IOUT, QOUT and UOUT.

Any combination of the above types can be supplied. Note, if parameter
REUSE is TRUE, then any required output files that already exist in
the directory specified by parameter MAPDIR are re-used rather than
being re-created from the corresponding input data.



IOUT = NDF (Write)
``````````````````
The output NDF in which to return the total intensity (I) map
including all supplied observations. This will be in units of pW.
Supply null (!) if the I map is not to be retained on exit. In this
case, the I map will only be created if it is needed to create the
output vector catalogue (see parameter CAT) and will be deleted on
exit.



IPCOR = _LOGICAL (Read)
```````````````````````
If TRUE, then IP correction is used when creating Q and U maps, based
on the values in the total intensity map specified by parameter IPREF.
If FALSE, then no IP correction is performed. The default is TRUE if
any Q or U output maps are being created, and FALSE otherwise. []



IPREF = NDF (Read)
``````````````````
The total intensity map to be used for IP correction. Only accessed if
parameter IPCOR is set TRUE. If null (!) is supplied for IPREF, the
map supplied for parameter REF is used. The map must be in units of
pW. If the same value is supplied for both IOUT and IPREF, the output
I map will be used for IP correction. [!]



JY = _LOGICAL (Read)
````````````````````
If TRUE, the I, Q and U values in the output catalogue will be in
units of mJy/beam. Otherwise they will be in units of pW. Note, the Q,
U and I maps are always in units of pW. The same FCF value is used to
convert all three Stokes parameters from pW to mJy/beam, derived from
the value supplied for parameter FCF. [TRUE]



LOGFILE = LITERAL (Read)
````````````````````````
The name of the log file to create if GLEVEL is not NONE. The default
is "<command>.log", where <command> is the name of the executing
script (minus any trailing ".py" suffix), and will be created in the
current directory. Any file with the same name is over-written. The
script can change the logfile if necessary by assign the new log file
path to the module variable "starutil.logfile". Any old log file will
be closed befopre the new one is opened. []



MAPDIR = LITERAL (Read)
```````````````````````
The name of a directory in which to put the Q, U an I maps made from
each individual observation supplied via "IN", before coadding them.
If null is supplied, the new maps are placed in the same temporary
directory as all the other intermediate files and so will be deleted
when the script exists (unless parameter RETAIN is set TRUE). Note,
these maps are always in units of pW. Each one will contain FITS
headers specifying the pointing corrections needed to align the map
with the reference map. [!]



MAPVAR = _LOGICAL (Read)
````````````````````````
Determines how the variance information in the final I, Q and U
coadded maps (parameters IOUT, QOUT and UOUT) are derived.
If MAPVAR is FALSE, the variances in the coadded maps are calculated
by propagating the variance information from the individual
observation maps. These variances are determined by makemap and are
based on the spread of bolometer I, Q or U values that fall in each
pixel of the individual observation map.
If MAPVAR is TRUE, the variances in the coadded maps are determined
from the spread of input values (i.e. the pixel values from the
individual observation maps) that fall in each pixel of the coadd.
The two methods produce similar variance estimates in the background
regions, but MAPDIR=TRUE usually creates much higher on-source errors
than MAPDIR=FALSE. Only use MAPDIR=TRUE if you have enough input
observations to make the variance between the individual observation
maps statistically meaningful. [FALSE]



MASK = LITERAL (Read)
`````````````````````
Specifies the type of masking to be used within makemap (the same type
of masking is used to create all three maps - I, Q and U):


+ "AUTO": makemap uses automatically generated masks based on the SNR
map at the end of each iteration. The SNR levels used are specified by
the "xxx.ZERO_SNR" and "xxx.ZERO_SNRLO" configuration parameters (see
parameter CONFIG).
+ "CIRCLE": makemap uses a fixed circular mask of radius 60 arc-
seconds centred on the expected source position.
+ Any other value is assumed to be a group of one or two NDFs that
  specify the "external" AST and PCA masks to be used. The way in which
  these NDFs are used depends on the value of parameter MASKTYPE. These
  NDFs must be aligned in pixel coordinates with the reference map
  (parameter REF).

["AUTO"]



MASKOUT1 = LITERAL (Write)
``````````````````````````
If a non-null value is supplied for MASKOUT, it specifies the NDF in
which to store the AST mask created from the NDF specified by
parameter MASK. Only used if an NDF is supplied for parameter MASK.
[!]



MASKOUT2 = LITERAL (Write)
``````````````````````````
If a non-null value is supplied for MASKOUT, it specifies the NDF in
which to store the PCA mask created from the NDF specified by
parameter MASK. Only used if an NDF is supplied for parameter MASK.
[!]



MASKTYPE = LITERAL (Read)
`````````````````````````
Specifies the way in which NDFs supplied for parameter MASK are to be
used. This parameter can be set to either of the following values:


+ "Signal": A single NDF should be supplied for parameter MASK holding
the astronomical signal level at each pixel within the astronomical
field being mapped. It can be in any units, but must have a Variance
component. The AST and PCA masks are created from this map by finding
all clumps of contiguous pixels above a fixed SNR limit, and then
extending these clumps down to a lower SNR limit. For the AST model,
the upper and lower SNR limits are of 3.0 and 2.0. For the PCA mask,
the limits are 5.0 and 3.0. The AST and PCA masks created in this way
can be saved using parameters MASKOUT1 and MASKOUT2.
+ "Mask": A pair of NDFs should be supplied for parameter MASK, each
  holding a mask in which background pixels have bad values and source
  pixels have good values. The first supplied NDF is used directly as
  the AST mask, and the second is used as the PCA mask.

["Signal"]



MSG_FILTER = LITERAL (Read)
```````````````````````````
Controls the default level of information reported by Starlink atasks
invoked within the executing script. This default can be over-ridden
by including a value for the msg_filter parameter within the command
string passed to the "invoke" function. The accepted values are the
list defined in SUN/104 ("None", "Quiet", "Normal", "Verbose", etc).
["Normal"]



MULTIOBJECT = _LOGICAL (Read)
`````````````````````````````
Indicates if it is acceptable for the list of input files to include
data for multiple objects. If FALSE, an error is reported if data for
more than one object is specified by parameter IN. Otherwise, no error
is reported if multiple objects are found. [FALSE]



NEWMAPS = LITERAL (Read)
````````````````````````
The name of a text file to create, in which to put the paths of all
the new maps written to the directory specified by parameter MAPDIR
(one per line). If a null (!) value is supplied no file is created.
[!]



NORMALISE = _LOGICAL (Read)
```````````````````````````
If TRUE, scale corrections for individual observations found in any
pre-existing auto-masked maps (e.g. made on a previous run of this
script) are applied when creating new maps. If False, no scale
corrections are applied. Scale correction factors are created and
stored at the same time as the pointing corrections. The correction
factor for a single observation is found by comparing the data values
in the map made from the single observation with those in the mean of
the maps made from all observation. The factor found in this way is
stored in the FITS extension of the map made from the observation
(header "CHUNKFAC"). [FALSE]



NORTH = LITERAL (Read)
``````````````````````
Specifies the celestial coordinate system to use as the reference
direction in any newly created Q and U time series files. For instance
if NORTH="AZEL", then they use the elevation axis as the reference
direction, and if "ICRS" is supplied, they use the ICRS Declination
axis. If "TRACKING" is supplied, they use north in the tracking system
- what ever that may be. ["TRACKING"]



OBSWEIGHT = _LOGICAL (Write)
````````````````````````````
This parameter affects how maps from separate observations are
weighted when they are combined together to form a coadd. If it is
FALSE, each pixel in each map is weighted simply using the reciprocal
of the Variance value stored in the map. If it is TRUE, an extra
factor is included in the pixel weights that is constant for all
pixels in a map but varies from observation to observation. In other
words, each observation is assigned a weight, which is used to factor
the pixel weights derived from the Variance values. The purpose of
this per-observation weight is to down-weight observations that are
very different to the other observations and which would therefore
contribute to a high Variance if parameter MAPVAR is set TRUE. These
weights are proportional to 1/(RMS*RMS), where "RMS" is the RMS
residual between an individual observation map and the coadd of all
observation maps, after they have been aligned spatially to take
account of any pointing error in the individual observation. [FALSE]



PIXSIZE = _REAL (Read)
``````````````````````
Pixel dimensions in the output I, Q and U maps, in arcsec. The default
is 4 arc-sec for both 450 and 850 um data. The bin size for the output
catalogue can be specified separately - see parameter BINSIZE and CAT.
[4]



QOUT = NDF (Write)
``````````````````
The output NDF in which to return the Q map including all supplied
observations. This will be in units of pW. Supply null (!) if no Q map
is required.



QUCONFIG = LITERAL (Read)
`````````````````````````
Extra parameter values to include in the MAKEMAP configuration used to
create Q and U maps. The values specified by "QUCONFIG" are applied
after those specified by "CONFIG". [!]



QUDIR = LITTERAL (Read)
```````````````````````
The name of a directory in which to put the Q, U and I time series
generated by SMURF:CALCQU, prior to generating maps from them. If null
(!) is supplied, they are placed in the same temporary directory as
all the other intermediate files and so will be deleted when the
script exists (unless parameter RETAIN is set TRUE). [!]



REF = NDF (Read)
````````````````
An optional map defining the pixel grid for the output maps, and which
is used to determine pointing corrections. If null (!) is supplied,
then the map (if any) specified by parameter MASK is used. See also
parameter REFFCF. [!]



REFFCF = _REAL (Read)
`````````````````````
The FCF that should be used to convert the supplied REF map to pW.
This parameter is only used if the supplied REF map is not already in
units of pW. The default is the FCF value stored in the FITS extension
of the map, or the standard FCF for the band concerned (450 or 840) if
there is no FCF value in the FITS header. Specify a new value on the
pol2map command line if the default value described above is
inappropriate. []



REUSE = _LOGICAL (Read)
```````````````````````
If TRUE, then any output maps or time-treams that already exist (for
instance, created by a previous run of this script) are re-used rather
than being re-created from the corresponding input files. If FALSE,
any previously created output maps or time-streams are ignored and new
ones are created from the corresponding input files. [TRUE]



RETAIN = _LOGICAL (Read)
````````````````````````
Should the temporary directory containing the intermediate files
created by this script be retained? If not, it will be deleted before
the script exits. If retained, a message will be displayed at the end
specifying the path to the directory. [FALSE]



SKYLOOP = _LOGICAL (Read)
`````````````````````````
Should the skyloop script be used in place of makemap to create the
maps from the I, Q and U time-series data? Note, when using skyloop it
is not possible to add in new observations to an existing collection
of I, Q and U maps - all observations must be processed together.
Therefore the value supplied for parameter REUSE will be ignored and a
value of FALSE assumed if the MAPDIR directory is missing maps for any
of the supplied observations. [FALSE]



UOUT = NDF (Write)
``````````````````
The output NDF in which to return the U map including all supplied
observations. This will be in units of pW. Supply null (!) if no U map
is required.



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


