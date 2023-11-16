order=int(input('enter the order of your matrix:'))
input_matrix=[]
for i in range(1,order+1):
	print('enter your',i,'th row')
	k=input().split(',')
	for j in range(len(k)):
		k[j]=int(k[j])
	input_matrix.append(k)
print("your matrix is:",input_matrix)
def determinant(matrix):
	import copy
	def det(matrix):
		result=0
		if len(matrix)!=1:
			m=copy.deepcopy(matrix)
			for i in range(len(m[0])):
				if i%2==1:
					m[0][i]=m[0][i]*-1
			for i in m[0]:
				m1=copy.deepcopy(m[1:])
				ind=m[0].index(i)
				for k in m1:
					k.remove(k[ind])
				result =result +i*det(m1)
		if len(matrix)==1: 
			return(matrix[0][0])
		return result
print("determinant of your matrix is",determinant(input_matrix))

