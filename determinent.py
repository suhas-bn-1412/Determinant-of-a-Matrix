def solve(matrix,mul):
	width = len(matrix)
	if width==1:
		return mul*matrix[0][0]
	else:
		sign=-1
		total=0
	for i in range(width):
		m=[]
		for j in range(1,width):
			buff=[]
			for k in range(width):
				if k !=i:
					buff.append(matrix[j][k])
					print(buff)
				m.append(buff)
				print(m)
			sign*=-1
			print(total)
			total+=mul*solve(m,sign*matrix[0][i])
		return total
print(solve([[0,1,2],[3,4,5],[1,2,4]],1))
