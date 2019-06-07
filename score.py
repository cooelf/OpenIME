#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import os.path
import sys

if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))

	# check and process input arguments
	if len(sys.argv) < 4:
		print globals()['__doc__'] % locals()
		sys.exit(1)
	inp1, inp2, outp = sys.argv[1:4]

	i = 1

	fin1 = open(inp1,'r')
	fin2 = open(inp2,'r')
	fout = open(outp, 'w')
	totscore = 0.0
	while 1:
		perscore = 0.0
		if i>1000:
			break
		linesc = fin1.readline().strip()
		linetg = fin2.readline().strip()
		#linech = fin1.readline().strip()
		wordsc = linesc.split()
		wordtg = linetg.split()
		j = 0
		while j < len(wordsc):
			if wordtg[j] == wordsc[j]:
				perscore += 1.0
			j += 1
		perscore /= len(wordsc)
		if(perscore >= 0.0):
			totscore += perscore
		fout.write(str(perscore))
		fout.write("\n")
		i += 1
		if (i % 100 == 0):
			logger.info("Saved " + str(i) + " articles")
	totscore /= i
	logger.info("Total Score = " + str(totscore))
	fin1.close()
	fin2.close()
	fout.close()
	logger.info("Finished Saved " + str(i) + " articles")
