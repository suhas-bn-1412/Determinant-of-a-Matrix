import copy
def minor(matrix,index):
	m=copy.deepcopy(matrix[1:])
	for i in range(len(m)):
		m[i].pop(index)
	return m

	
	
