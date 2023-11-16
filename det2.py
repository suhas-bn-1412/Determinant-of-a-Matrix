mat=[[1,2,3,4],[2,3,4,5],[9,8,7,6],[3,4,7,8]]
import copy
def det(matrix):
	result=0
	if len(matrix)!=1:
		m=copy.deepcopy(matrix)
		for i in m[0]:
			if m[0].index(i)%2==1:
				i=i*-1
		for i in m[0]:
			m1=copy.deepcopy(matrix[1:])
			ind=matrix[0].index(i)
			for k in copy.deepcopy(m1):
				k.remove(k[ind])
			result=result+i*int(det(copy.deepcopy(m1)))
	if len(matrix)==1:
		return(matrix[0][0])
print(det(mat))

