#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import os.path
import sys
import re

if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))

	# check and process input arguments
	if len(sys.argv) < 3:
		print globals()['__doc__'] % locals()
		sys.exit(1)
	inp1, inp2, ScoreThreshold= sys.argv[1:4]

	i = 1


	fin1 = open(inp1,'r')
	fin2 = open(inp2,'r')

	fout = open(inp2+".score", 'w')

	totscore = 0.0
	while 1:
		perscore = 0.0

		linesc = fin1.readline().strip()
		if not linesc:
			break
		linetg = fin2.readline().strip()
		linesc = re.sub('[_a-zA-Z ]','',linesc)
		linetg = re.sub('[_a-zA-Z ]','',linetg)
		j = 0

		smalllen = len(linesc) if len(linesc) < len(linetg) else len(linetg)

		while j < smalllen:
			if linetg[j] == linesc[j]:
				perscore += 1.0
			j += 1
		perscore /= smalllen
		if perscore >= float(ScoreThreshold):
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
