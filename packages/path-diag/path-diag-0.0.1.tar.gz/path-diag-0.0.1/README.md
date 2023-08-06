# Path-diag

A utility for validating paths in environment variables and modifying them safely.

## Prerequisites

* Python 3

## Installation

You can install `path-diag` via `pip`:
```
pip3 install path-diag
```

## Usage

### Diagnose environment variable problems

Check if `$PATH` contains any invalid paths:
```
$ pathdiag
```

`$PATH` is the default variable to check.

You can specify another variable. For example:

```
$ pathdiag --var PYTHONPATH
```

You can also specify an increased verbosity which will also print the paths that are successfully checked:
```
$ pathdiag -v
✓ /usr/local/bin
✓ /usr/bin
✓ /bin
✓ /usr/sbin
✓ /sbin
```

### Safely append/prepend paths to environment variables

You can use the bash functions in order to take advantage of this features by adding the following line on top of your `.bashrc`/`.zshrc` file:
```
source /usr/local/bin/path-diag-functions.sh
```

Then you can use the `safe_append`/`safe_prepend` functions. For example:
```
safe_append "/usr/local/Cellar/node/7.4.0/bin"
safe_prepend "/usr/local/opt/python/libexec/bin"
```

This will add `/usr/local/Cellar/node/7.4.0/bin` at the end of `$PATH` if this path passes the validation checks, and will also add `/usr/local/opt/python/libexec/bin` at the beginning of `$PATH`, again if no errors are identified.

## Contributing

All contributions are welcomed. Make sure your code passes `flake8` checks and that is auto-formatted using [black](https://github.com/ambv/black)
