
from Bio import SeqIO
filename = "NC_002695.1.fasta"

for record in SeqIO.parse(filename, "fasta"):
	if len(record) >6315: 
		print("Record " + record.id + ", length " + str(len(record.seq)))
