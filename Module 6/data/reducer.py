#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter

import sys

current_word = None
word_details = []
for line in sys.stdin:
	line = line.strip()
	word,doc_id = line.split('\t', 1)
	if word == current_word:
		doc_det = word_details[1]
		if doc_id not in doc_det:
			doc_det.append(doc_id)
		word_details[1] = doc_det
	else:
		if current_word:
			print '%s' % word_details  
		current_word = word
		word_details = []
		doc_details = []
		doc_details.append(doc_id)
		word_details.append(word)
		word_details.append(doc_details)
if current_word:
	print '%s' % word_details  		

	
   
