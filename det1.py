mat=[[1,2,3,4],[2,3,4,5],[9,8,7,6],[3,4,7,8]]
for i in mat[0]:
	n=mat[0].index(i)
	if n%2==1:
		mat[0][n]*=-1
print(mat)
