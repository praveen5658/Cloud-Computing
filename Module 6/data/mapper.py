#!/usr/bin/env python
"mapper.py"

import sys

for line in sys.stdin:
	line = line.strip("[")
	line = line.strip("]")
	data = line.split(",", 1)
	unique = [];
	words = data[1].split()
	for word in words:
		if word not in unique:
			unique.append(word)
	for uniqueword in unique:
		print '%s\t%s' % (uniqueword, data[0].replace("\"",""))
