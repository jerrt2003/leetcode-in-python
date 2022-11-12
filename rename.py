#!/usr/bin/python3

import os, sys, re
for f in next(os.walk('.'))[1]:
    if f[0].startswith('Q'):
        _f = re.split(" |\. ", f)
        os.rename(f, "_".join(_f))

