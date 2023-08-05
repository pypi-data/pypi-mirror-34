

CREOBJ
======


Purpose
~~~~~~~
Create an HDS object


Description
~~~~~~~~~~~
This routine creates an HDS object, primitive or structure, scalar or
array. In theory it is possible to build up a complete NDF or Figaro
DST data file. This is not recommended because the risk of creating an
illegal hierarchy of HDS structures - i.e. one not accepted by KAPPA,
Figaro, etc. - is very high. This routine is intended only for minor
repairs to such files, or in emergencies to create a very simple,
minimal, data file.


Usage
~~~~~


::

    
       creobj type dims object
       



ADAM parameters
~~~~~~~~~~~~~~~



TYPE = _CHAR (Read)
```````````````````
The HDS type of the object to be created. Figaro users note that this
is something like '_REAL', '_DOUBLE', '_INTEGER', '_WORD' etc.
Anything which is not such a primitive HDS type will cause a structure
to be created. The type specified here will then be used as that
structure's type. ['_REAL']



DIMS( 7 ) = _INTEGER (Read)
```````````````````````````
The dimensions of the object to be created, i.e. the size of the array
along each axis. The number of positive integers specified indicates
the dimensionality of the object created. To create a scalar object
enter zero, a single zero will do. [0]



OBJECT = HDSOBJECT (Read)
`````````````````````````
The object to be created. Specify beginning with directory and file
name in the syntax of the operating system, followed by the dot-
separated structure hierarchy. Elements of structure arrays are
specified in ordinary brackets (). An array element cannot be created.



Examples
~~~~~~~~
creobj type=NDF dims=0 object=file
This will create an empty HDS file. The top level structure is of type
"NDF", which has little consequence.
creobj type=ARRAY dims=0 object=file.DATA_ARRAY
This will create the scalar structure DATA_ARRAY in the top level
structure of the file "file". The structure type is "ARRAY", which has
special meaning in the Starlink Data Format.
creobj type=_REAL dims=[20,30] object=file.DATA_ARRAY.DATA
This will create a two-dimensional array of _REAL numbers called DATA
and situated in file.DATA_ARRAY. The size of the new array is 20 by 30
numbers.
creobj type=AXIS dims=2 object=file.AXIS
This will create a one-dimensional array of AXIS structures called
AXIS and situated underneath the top level of "file".



