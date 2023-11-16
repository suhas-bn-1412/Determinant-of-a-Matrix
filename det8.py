order=int(input('enter the order of your matrix:'))
input_matrix=[]
for i in range(1,order+1):
	print('enter your',i,'th row')
	k=input().split(',')
	for j in range(len(k)):
		k[j]=int(k[j])
	input_matrix.append(k)
print("your matrix is:",input_matrix)
a=0
import copy
def determinant(matrix):
	global a
	result=a
	if len(matrix)>=2:
		m=copy.deepcopy(matrix)
		for i in range(len(m[0])):
			if i%2==1:
				m[0][i]*=-1
		for j in m[0]:		
			m1=copy.deepcopy(m[1:])
			for k in range(len(m1)):
				m1[k].remove(m1[k][m[0].index(j)])
			result=result+j*determinant(m1)
			a=result
	if len(matrix)==2:
		return matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
	return result
print("Determinant of your matrix is:",determinant(input_matrix))
