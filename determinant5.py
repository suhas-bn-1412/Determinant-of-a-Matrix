order=int(input('enter the order of your matrix:'))
input_matrix=[]
for i in range(1,order+1):
	print('enter your',i,'th row')
	k=input().split(',')
	for j in range(len(k)):
		k[j]=int(k[j])
	input_matrix.append(k)
print("your matrix is:",input_matrix)
def square(matrix):
	for i in matrix:
		if len(i)!=len(matrix):
			return False
		else:
			return True
if square(input_matrix):
	print("your matrix is square matrix:")
else:
	print("your matrix is not a square matrix")
