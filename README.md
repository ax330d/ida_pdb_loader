
# IDA PDB Loader (IPL)

## What is this

This is a simple IDA plugin to load PDB symbols. The problem is that
sometimes IDA crashes for me when trying to load symbols, so I came up
with this quick and dirty alternative.


## Requirements & installation

This plugin relies on Python pdbparse module
(https://github.com/moyix/pdbparse), and I have it included in plugin,
because I had to do minor modifications to code.

pdbparse also relies on other Python module named construct
(https://pypi.python.org/pypi/construct). I have included construct in
plugin. pdbparse is using old API (version 2.0.0 is known to support
it).


## How it works

Load plugin (Alt+F7), pick PDB file and wait. It will take a while if PDB
file is big.  


## Other things to know

Tested only on IDA 6.9 x32. Sometimes fails to find symbols for certain
functions. Currently only renames functions.
