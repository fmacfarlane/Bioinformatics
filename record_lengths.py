# this script was used to find the 3 longest gene sequences in the NC_002695.1.fasta file
from Bio import SeqIO
# this imports the correct programmes in Biopython
filename = "NC_002695.1.fasta"
outputfile = "longest_genes.fasta"
output_handle = open(outputfile, 'w')
# this assigns the filenames and opens a file for the result to be written in to.
records = list(SeqIO.parse(filename, 'fasta'))
# this puts all of the record into a list
records.sort(cmp = lambda x,y: cmp(len(y),len(x)))
# this sorts the list by length
SeqIO.write(records[0:3], output_handle, 'fasta')
# this writes the top 3 ,longest 3 , results into the outputfile
output_handle.close()
# we then close the outputfile.
