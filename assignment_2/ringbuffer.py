#!usr/bin/python
# set the infile variable to be the signal.txt file
infile='signal.txt'
#read in our search sequences
dataset=open(infile)
data=[]
for line in dataset.readlines():
	line=line.strip()
	for number in line.split():
		data.append(float(number))
dataset.close()
# this reads all of the entries in the signal.txt file as floating numbers and puts them in the array data
buffersize=60
# this sets the buffer size, trial and error found that 60 was a suitable buffer size
buffer=[]
# creates the buffer array
buffertotal=0
position=0
result=[]
# The above commands fill the buffer
while len(buffer)<buffersize:
	buffer.append(data[position])
	buffertotal=buffertotal+data[position]
	position=position+1
	result.append(float(buffertotal)/buffersize)
# This calculates the moving average and moves on one step, and then calculates the running average.

for v in range(position, len(data)):
	buffertotal=buffertotal-buffer[v%buffersize]
	buffer[v%buffersize]=data[v]
	buffertotal=buffertotal+buffer[v%buffersize]
	result.append(float(buffertotal)/buffersize)
# This works through the rest of the data.
print result
# this loop creates the buffer and runs it, organising the data and printing the result
smooth=open('smoothed.txt', 'w')
# we open a new text file to hold the buffer results
for r in result:
	smooth.write("%s\n" % r)
smooth.close()
# this send the data from the buffer into a text file which can then be plotted in R

