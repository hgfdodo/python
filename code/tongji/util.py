def lines(file):
	for line in file:
		yield line
	yield '\n'

def get_block(filename):
	f=open(filename,'r')
	blocks=[]
	for line in lines(f.read()):
		if line.strip()[-1:]==':':
			#blocks.append(line)
			pass
		else:
			blocks.append(line)
	return blocks
