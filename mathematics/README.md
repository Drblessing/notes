# Mathematics

The language of the universe, and the foundation of all sciences. God's purest tongue.

## Overview

To install primesieve

```
export CPPFLAGS="-I/opt/homebrew/include"
export LDFLAGS="-L/opt/homebrew/lib"
```

or

```
export CPPFLAGS="-I$(brew --prefix primesieve)/include"
export LDFLAGS="-L$(brew --prefix primesieve)/lib"
export CPLUS_INCLUDE_PATH="$(brew --prefix primesieve)/include${CPLUS_INCLUDE_PATH:+:$CPLUS_INCLUDE_PATH}"
export LIBRARY_PATH="$(brew --prefix primesieve)/lib${LIBRARY_PATH:+:$LIBRARY_PATH}"
python -m pip install numpy
python -m pip install --no-cache-dir --force-reinstall --no-binary=:all: primesieve
```
