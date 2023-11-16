mat=[[2,4,1,1],[0,2,1,0],[2,1,1,3],[4,0,2,3]]
import copy
def minor1(matrix,index):
	m=copy.deepcopy(matrix[1:])
	for i in range(len(m)):
		m[i].pop(index)
	return m
for index in range(len(mat)):
	print(minor1(mat,index))
