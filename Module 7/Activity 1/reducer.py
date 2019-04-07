#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter


import sys

orders = []
line_items = []
items_ids = []
result = []
for line in sys.stdin:
	line = line.strip()
	if line[0] == 'o':
		data = line.split(", ", 9)	
		orders.append(data)
	else:
		data = line.split(", ", 16)
		line_items.append(data)
		items_ids.append(data[1])
for order in orders:
	if order[1] in items_ids:
		first_index = items_ids.index(order[1])
		last_index = len(items_ids) - 1 - items_ids[::-1].index(order[1])
		rem = last_index - first_index + 1
		i = 0
		while rem > 0:
			index = first_index + i
			test = order + line_items[index]
			i = i + 1
			rem = rem - 1
			print '%s' % test
			
	
	
	

		
	


		
		
	 

		
