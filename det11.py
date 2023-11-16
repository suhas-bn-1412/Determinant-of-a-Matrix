mat=[[2,4,1,1],[0,2,1,0],[4,0,2,3],[2,1,1,3]]
import copy
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
		#arr=[[value for row,value in enumerate(line) if row != index]for line in matrix[1:]]
		m=copy.deepcopy(matrix)
		for j in m[0]:		
			m1=copy.deepcopy(m[1:])
			for k in range(len(m1)):
				m1[k].remove(m1[k][m[0].index(j)])
		total+=(-1)**index*matrix[0][index]*det(m1)
	return total
print(det(mat))
