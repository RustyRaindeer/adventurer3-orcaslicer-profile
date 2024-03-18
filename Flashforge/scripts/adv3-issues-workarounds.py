#!/usr/bin/python
import sys
import re
import os

sourceFile=sys.argv[1]
destFile = sourceFile
tempLine = ""

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()
f.close()

with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]

        if oline[:4] == "M104":
            # First, remove any trailing comment
            oline = re.sub(" *;.*$", "", oline)

            # add T0, if neither T0 nor T1 found on the line
            if None == re.search(" T[01]", oline):
                oline = re.sub(" *$", " T0", oline, 1)

            of.write(oline)

        elif oline[:7] == "M106 S0":
            of.write("M107\n")

        else:
            of.write(oline)

of.close()
