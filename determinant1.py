m=int(input('enter the order of your matrix:'))
input_matrix=[]
for i in range(1,m+1):
	print('enter your',i,'th row')
	k=input().split(',')
	for j in range(len(k)):
		k[j]=int(k[j])
	input_matrix.append(k)
print(input_matrix) 
