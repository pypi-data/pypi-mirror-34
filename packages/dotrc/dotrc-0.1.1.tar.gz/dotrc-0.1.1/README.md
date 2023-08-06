dotrc
=====

[![Build Status](https://travis-ci.org/paulholden2/dotrc.svg?branch=master)](https://travis-ci.org/paulholden2/dotrc)

Simple .rc file loading for your Python projects. Looks for config files
passed via --config as well as typical locations based on your app name:

* Files provided via --config option (see below)
* .*app*rc
* ~/.config/*app*

Files are loaded such that files earlier in the above list override settings
in later ones. The content of each file is parsed as YAML, falling back to
JSON if that fails.

## Usage

```python
import dotrc

# Loads .apprc, ~/.config/app, etc.
config = dotrc.load('app')
```

## --config

Additional configuration files may be provided via the --config commandline
option. This parses `sys.argv` directly, so load your configs before doing
anything that might modify it. Files are loaded in order, so options in later files override options set in
earlier ones.

```
$ python app.py --config .extrarc .lastrc
$ python app.py --config=.extrarc
$ python app.py --config=.1rc --config=.2rc
```

A list of files will be populated from the commandline arguments until a
switch or option is detected. You need to be mindful if you for some reason
have config files starting with dashes, so you don't signal the end of your
file list.

```
$ python app.py --config .1rc --config=--.weirdrc
$ python app.py --config=--.1rc --config=--.2rc
$ python app.py --config ./-.1rc ./-.2rc
```
