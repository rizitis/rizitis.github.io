#!/bin/bash

TMP=.

probe -l 2> /dev/null | grep -E 'Linux$' | sort | uniq 1> $TMP/SeTplist 2> /dev/null
