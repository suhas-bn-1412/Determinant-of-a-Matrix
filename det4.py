u=[[1,2],[3,1]]
import copy
def det(n):
	if len(n)==1:
		return n[0][-1]
	else:
		m=copy.deepcopy(n)
		m1=m[0]
		for i in m1:
			if m1.index(i)%2!=0:
				i*=-1
			m2=copy.deepcopy(n.remove(n[0]))
			for k in m2:
				m3=copy.deepcopy(m2.remove(k[k.index(i)]))
			return i*det(m3)
print(det(u))
