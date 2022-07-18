#!/bin/sh
# Command for opening a new PyCharm window, using the command line.
# The command uses the current working directory as the project root directory.

open -na "PyCharm.app" --args "$@"
