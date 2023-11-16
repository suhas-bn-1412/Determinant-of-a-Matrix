mat=[[2,4,1,1],[4,0,2,3],[0,2,1,0],[2,1,1,3]]
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
		minor=[[value for row,value in enumerate(line) if row != index]for line in matrix[1:]]
		total+=(-1)**index*matrix[0][index]*det(minor)
	return total
print(det(mat))
