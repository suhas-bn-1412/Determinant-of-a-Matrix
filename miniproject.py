from tkinter import *

c=0
a=[]
o=0
frame=0

import copy

def minor(matrix,index):
	m=copy.deepcopy(matrix[1:])
	for i in range(len(m)):
		m[i].pop(index)
	return m


def det(matrix):
	size=len(matrix)
	if not matrix or not matrix[0]:
		return 1
	if size==1:
		return matrix[0][0]
	if size==2:
		return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	total=0
	for index in range(size):
		total+=(-1)**index*matrix[0][index]*det(minor(matrix,index))
	return total


def showgrid():
	global order,a,o,c,frame
	if not order.get():
			output_1.insert(END,'NO ORDER GIVEN!')
	else:
		o=int(order.get())
		if not c==0:
			frame.destroy()
			frame=Frame(window)
			frame.grid(row=2,column=1,columnspan=10)
		else:
			frame=Frame(window)
			frame.grid(row=2,column=1,columnspan=10)
			c=1
		for i in range(o):
			a.append([])
			for j in range(o):
				a[i].append(0)
				a[i][j]=Entry(frame,width=4)
				a[i][j].grid(row=i+3,column=j+3)	
		button1=Button(frame,text="submit",width=10,command=getvalue)
		button1.grid(row=13,column=13)

	
def getvalue():
	global a,o
	b=[]
	for i in range(o):
		b.append([])
		for j in range(o):
			b[i].append(0)
			if a[i][j].get():
				b[i][j]=int(a[i][j].get())
			else:
				b[i][j]=0
	output_1.insert(END,"The determinant of your matrix is:%d\n"%det(b))
	



window=Tk()
window.title("Determinant of matrix")


window.minsize(width=500,height=400)
window.maxsize(width=800,height=600)

order=Entry(window,width=4)
order.grid(row=0,column=1)

Label(window,text="Enter the order of matrix:").grid(row=0,column=0)

button=Button(window,text="click here to proceed",width=20,command=showgrid)
button.grid(row=1,column=1)

output_1=Text(window, width=50, height =10)
output_1.grid(row=10,column=0,columnspan=3)


window.mainloop()


