#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	line = line.strip("[")
	line = line.strip("]")
	line = line.replace("\"","")
	data = line.split(", ", 1)
	print '%s\t%s' % (data[0], 1)
