#!/usr/bin/python

import re

infile='ig_pairs.out'
fh = open(infile)

outfile='ig_pairs_parsed.txt'
handle = open(outfile, 'w')

index = []
identifier = []

mydict = {}

line = fh.readline()

for line in fh:
	regexp=r'(\d+) +>([^/]+)/'
	m=re.search(regexp,line)
	if m:
		group1 = m.group(1)
		group2 = m.group(2)

		index.append(group1)
		identifier.append(group2)
		mydict = {'index':index, 'identifier':identifier}

	else:
		I = line[0:5].strip()
		J = line[6:10].strip()
		ILEN =line[11:15].strip()
		JLEN = line[16:20].strip()
		MATCH = line[21:30].strip()
		NGAPS = line[31:37].strip()
		NALIG = line[38:44].strip()
		NIDENT = line[45:51].strip()
		IDENT = line[52:61].strip()
		NAS = line[62:71].strip()
		NASAL = line[72:81].strip()
		NRANS = line[82:88].strip()
		RMEAN = line[89:98].strip()
		STDEV = line[99:108].strip()
		SCORE = line[109:119].strip()

	
#columns = ['I', 'J','ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STDEV', 'SCORE']
	print >> handle, mydict,I
fh.close()
handle.close()


