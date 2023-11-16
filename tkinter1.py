from tkinter import *
from det9 import *

a=[]
o=0
def showgrid():
	global order,a,o
	o=int(order.get())
	frame=Frame(window)
	frame.grid(row=2,column=1,columnspan=10)
		
	for i in range(o):
		a.append([])
		for j in range(o):
			a[i].append(0)
			a[i][j]=Entry(frame,width=4)
			a[i][j].grid(row=i+3,column=j+3)
	
	button1=Button(frame,text="submit",width=20,command=getvalue)
	button1.grid(row=10,column=10)		
def getvalue():
	global a,o
	b=[]
	for i in range(o):
		b.append([])
		for j in range(o):
			b[i].append(0)
			#b[i][j]=int(a[i][j].get())
			if a[i][j].get():
				b[i][j]=int(a[i][j].get())
			else:
				b[i][j]=0
	output_1.insert(END,"The determinant of your matrix is:%d\n"%det(b))




window=Tk()
window.title("Determinant of matrix")

window.minsize(width=400,height=400)
window.maxsize(width=600,height=600)

order=Entry(window,width=4)
order.grid(row=0,column=1)

button=Button(window,text="click here to proceed",width=20,command=showgrid)
button.grid(row=1,column=1)

output_1=Text(window, width=50, height =10)
output_1.grid(row=10,column=0,columnspan=3)

Label(window,text="Enter the order of matrix:").grid(row=0,column=0)
	
window.mainloop()

