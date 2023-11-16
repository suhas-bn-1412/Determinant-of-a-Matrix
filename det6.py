matrix=[[1,2,3,4],[3,4,5,6],[2,6,7,9],[4,7,8,6]]
import copy
m=copy.deepcopy(matrix)
for i in m[0]:
	print(i)
	m1=copy.deepcopy(m[1:])
	ind=m[0].index(i)
	for k in copy.deepcopy(m1):
		k.remove(k[ind])
		print(k)
	print(m1)
