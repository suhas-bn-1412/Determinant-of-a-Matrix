mat=[[1,2,3,4],[2,3,4,5],[9,8,7,6],[3,4,7,6]]
import copy
result=0
def det(matrix):
	global result
	if len(matrix)>=2:
		m=copy.deepcopy(matrix)
		for i in range(len(m[0])):
			if i%2==1:
				m[0][i]=m[0][i]*-1
		for i in m[0]:
			ind=m[0].index(i)
			m1=copy.deepcopy(m[1:])
			for k in m1:
				k.remove(k[ind])
			result =result +i*det(m1)
	if len(matrix)==2: 
		return(matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1])
	return result
print(det(mat))

