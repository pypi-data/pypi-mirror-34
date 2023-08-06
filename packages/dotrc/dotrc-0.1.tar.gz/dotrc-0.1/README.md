dotrc
=====

Simple .rc file loading for your Python projects. Looks for config files
in typical locations based on your app name:

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
