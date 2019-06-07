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
	if len(sys.argv) < 6:
		print globals()['__doc__'] % locals()
		sys.exit(1)
	inp_ture, inp_pred, ScoreThreshold, n_best, top_n= sys.argv[1:6]

	i = 0
	n_best = int(n_best)
	top_n = int(top_n)

	fin_true = open(inp_ture,'r')
	fin_pred = open(inp_pred,'r')

	fout = open(inp_pred+".score", 'w')

	totscore = 0.0
	while 1:
		perscore = 0.0

		linesc = fin_true.readline().strip()
		linesc = re.sub('[_a-zA-Z ]','',linesc)
		linesc = re.sub('[0-9]','',linesc)
		if not linesc:
			break
		linetg = [None] * n_best
		for tgi in range(n_best):
			linetg[tgi] = fin_pred.readline().strip()
			linetg[tgi] = re.sub('[_a-zA-Z ]','',linetg[tgi])
			linetg[tgi] = re.sub('[0-9]','',linetg[tgi])
		# linetg = re.sub('[_a-zA-Z ]','',linetg)
		j = 0

		smalllen = len(linesc) if len(linesc) < len(linetg[0]) else len(linetg[0])
		# print(linesc, smalllen)

		while j < smalllen:
			if linetg[0][j] == linesc[j]:
				perscore += 1.0
			else:
				for tgi in range(1,top_n):
					if (len(linesc) == len(linetg[tgi])):
						if (linetg[tgi][j] == linesc[j]):
							perscore += 1.0
							break
			# if linetg[j] == linesc[j]:
			# 	perscore += 1.0
			j += 1
		#print(i,perscore, smalllen)
		#if smalllen != 0:
		#	perscore /= smalllen
		#else:
		#	perscore = 1.0 
		perscore = perscore / float(smalllen) if smalllen != 0 else 0
		# print(perscore, smalllen)
		#perscore /= smalllen
		if perscore >= float(ScoreThreshold):
			totscore += perscore
		fout.write(str(perscore))
		fout.write("\n")
		i += 1
		if (i % 100 == 0):
			logger.info("Saved " + str(i) + " articles")
	totscore /= i
	logger.info("Total Score = " + str(totscore))
	fin_true.close()
	fin_pred.close()
	fout.close()
	logger.info("Finished Saved " + str(i) + " articles")
