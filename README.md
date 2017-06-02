# LHCFillScheme

Returns the bunch pattern for a given LHC fill for use in offline analyses.

* [Usage](#usage)
  * [Getting bunch patterns](#getting-bunch-patterns)
  * [Using bunch patterns](#using-bunch-patterns)
    * [C++](#c)
    * [Python](#python)

## Usage

### Getting bunch patterns

This is done through the main script, `lhcFillScheme.py`, which downloads a LHC fill scheme file and processes it, returning a txt file with the bunch pattern.

```
usage: lhcFillScheme.py [-h] [-i INDIR] [-o OUTDIR] fills

Downloads and analyzes a fill scheme

positional arguments:
  fills                 Fill scheme number(s). Accepts comma-separated list, e.g. 5501,5502,etc

optional arguments:
  -h, --help            show this help message and exit
  -i INDIR, --indir INDIR
                        Directory to save the fill schemes to (default: fillschemes/)
  -o OUTDIR, --outdir OUTDIR
                        Directory to save the analyzed output to (default: bunchpatterns/)
```

### Using bunch patterns

Included are definitions for a `Fill` class that can be used to read in the bunchpattern files for both C++ and python. Each instance of `Fill` contains a set of vectors that holds the bunch crossing numbers for each type of bunch crossing:

```
All BXs      = all colliding bunch crossings
Isolated BXs = all isolated bunch crossings
First BXs    = the first bunch crossing of a train
Last BXs     = the last bunch crossing of a train
Middle BXs   = the bunch crossings in a train that are neither the first nor the last bunch crossing
Empty BXs    = all non-colliding bunch crossings
```

#### C++

The C++ `Fill` class files are `src/Fill.cpp` and `inc/Fill.hpp`.

```
#include "src/Fill.cpp"

// Instantiate
Fill fill5717("bunchpatterns/bunchpattern5717.txt");

// Member variables
fill5717.allBXs
fill5717.isoBXs
fill5717.firstBXs
fill5717.lastBXs
fill5717.middleBXs
fill5717.emptyBXs
```

#### Python
The python `Fill` class file is `python/Fill.py`

```
from python.Fill import Fill

# Instantiate
fill5717 = Fill("bunchpatterns/bunchpattern5717.txt")

# Member variables
fill5717.allBXs
fill5717.isoBXs
fill5717.firstBXs
fill5717.lastBXs
fill5717.middleBXs
fill5717.emptyBXs
```
