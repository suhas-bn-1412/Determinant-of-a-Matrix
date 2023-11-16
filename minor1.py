mat=[[2,4,1,1],[0,2,1,0],[2,1,1,3],[4,0,2,3]]
def minor(matrix,index):
	minor=[[value for row,value in enumerate(line) if row != index]for line in matrix[1:]]
	return minor
for index in range(len(mat)):
	print(minor(mat,index))
	
	
