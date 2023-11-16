mat=[[1,2,3,4],[2,3,4,5],[9,8,7,6],[3,4,7,8]]
import copy
result=0
def reduce_(matrix):
	result=0
	if len(matrix)>=2:
		for i in matrix[0]:
			m1=copy.deepcopy(matrix[1:])
			m=copy.deepcopy(matrix[:])
			ind=matrix[0].index(i)
			for k in m1:
				k.remove(k[ind])
			print(i,m1)
			result=result+reduce_(m1)
	if len(matrix)==2:
		return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
print(reduce_(mat))
