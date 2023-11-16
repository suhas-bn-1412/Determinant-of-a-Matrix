mat=[[1,2,3,4],[3,4,5,6],[2,4,6,9],[6,3,4,2]]
import copy
def det(matrix):
	l=[]
	if len(matrix)>=2:
		m=copy.deepcopy(matrix)
		for i in range(len(m[0])):
			if i%2==1:
				m[0][i]*=-1
		for j in m[0]:
			m1=copy.deepcopy(matrix[1:])
			for k in m1:
				k.remove(k[m[0].index(j)])
			l.append((j,m1))
		return sum(map(lambda x:x[0]*det(x[1]),l))
	if len(matrix)==2:
		return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

	
det(mat)
		
		
