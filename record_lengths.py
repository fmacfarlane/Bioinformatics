# this script was used to find the 3 longest gene sequences in the NC_002695.1.fasta file
from Bio import SeqIO
# this imports the correct programmes in Biopython
filename = "NC_002695.1.fasta"
# this assigns the filename as the fasta file we are investigating

for record in SeqIO.parse(filename, "fasta"):
	if len(record) >6315: 
		print("Record " + record.id + ", length " + str(len(record.seq)))
# This for loop finds records with length longer than 6315 bp long and prints them along with their record id.
# This script does find the 3 longest genes, however trial and error to find the length they must be longer than, ie. the fourth longest gene.
