#!usr/bin/python

infile='signal.txt'
#read in our search sequences
dataset=open(infile)
data=[]
for line in dataset.readlines():
	line=line.strip()
	for number in line.split():
		data.append(float(number))
dataset.close()
buffersize=60
buffer=[]
buffertotal=0
position=0
result=[]
while len(buffer)<buffersize:
	buffer.append(data[position])
	buffertotal=buffertotal+data[position]
	position=position+1
	result.append(float(buffertotal)/buffersize)
for v in range(position, len(data)):
	buffertotal=buffertotal-buffer[v%buffersize]
	buffer[v%buffersize]=data[v]
	buffertotal=buffertotal+buffer[v%buffersize]
	result.append(float(buffertotal)/buffersize)
print result

smooth=open('smoothed.txt', 'w')
for r in result:
	smooth.write("%s\n" % r)
smooth.close()


