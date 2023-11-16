import copy

def minor(matrix,index):
	m=copy.deepcopy(matrix[1:])
	for i in range(len(m)):
		m[i].pop(index)
	return m


def det(matrix):
	size=len(matrix)
	if not matrix or not matrix[0]:
		return 1
	if size==1:
		return matrix[0][0]
	if size==2:
		return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	total=0
	for index in range(size):
		total+=(-1)**index*matrix[0][index]*det(minor(matrix,index))
	return total

