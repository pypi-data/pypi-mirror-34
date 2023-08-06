# mtsort
A cross-platform module for sorting files by time.

[![PyPI version](https://badge.fury.io/py/mtsort.svg)](https://badge.fury.io/py/mtsort)
[![GitHub license](https://img.shields.io/github/license/stiftcast/mtsort.svg)](https://github.com/stiftcast/mtsort/blob/master/LICENSE)


Gets last modification time from file(s) and folder(s), 
then moves them to a new directory, sorting them in new
folders.  These folder names are in 'yyyy-mm-dd' format.

Useful for sorting large collections of files, which would be otherwise
tedious to do manually!

Tested and confirmed working on Python 3.6 and above.

## Installation
    pip install mtsort
 
or with the installation script:

    python3 setup.py install

## Examples

**Moving files:**

    >>> import mtsort
    >>> mtsort.mtmove('/home/test/sourcedir', '/home/test/destdir')
    
Results in:

```
    before:                after:
    .                      .
    |-- destdir            |-- destdir
    |-- sourcedir          |   |-- 2016-07-29  
        |-- file1          |   |   |-- file1
        |-- file2          |   |-- 2016-07-30
        |-- file3          |   |   |-- file2
                           |   |-- 2016-07-31
                           |       |-- file3
                           |-- sourcedir
```                           
**Copying files:**

    >>> import mtsort
    >>> mtsort.mtcopy('/home/test/sourcedir', '/home/test/destdir')

Results in:

```
    before:                after:
    .                      .
    |-- destdir            |-- destdir
    |-- sourcedir          |   |-- 2016-07-29  
        |-- file1          |   |   |-- file1
        |-- file2          |   |-- 2016-07-30
        |-- file3          |   |   |-- file2
                           |   |-- 2016-07-31
                           |       |-- file3
                           |-- sourcedir
                               |-- file1
                               |-- file2
                               |-- file3
```


Alternatively, you can simply launch the script on its own, or from the command line to use it:

from terminal:

    $ mtsort

from cmd or Powershell:

    C:\> py -m mtsort
