from tkinter import *
from tkinter import messagebox
top=Tk()
top.title("Flames Application")
top.geometry('430x250')
c=Canvas(top,width=400,height=200,bg="yellow")
c.pack(side='top', fill='both', expand='yes')
fn1=StringVar()
sn1=StringVar()
Label(top,text="FLAMES",bg="yellow",font=("Times",20)).place(x=140,y=10)
l1=Label(top,text="Male's Name:",font=4,bg="red",fg="white")
l1.place(x=30,y=65)
f=Entry(top,bd=8,font=3,textvariable=fn1,bg="red",fg="white")
f.place(x=170,y=60)
l2=Label(top,text="Female's Name:",font=4,bg="green",fg="white")
l2.place(x=20,y=130)
s=Entry(top,bd=8,font=3,textvariable=sn1,bg="green",fg="white")
s.place(x=170,y=125)


def fun():
	fn=fn1.get()
	sn=sn1.get()
	n1=len(fn)
	n2=len(sn)
	i=0
	c1=[]
	c2=[]
	while(i<26):
		c1.append(0)
		c2.append(0)
		i+=1
	i=0
	while(i<n1):
		if(fn[i]=='A' or fn[i]=='a'):
			c1[0]+=1
		elif(fn[i]=='B' or fn[i]=='b'):
			c1[1]+=1
		elif(fn[i]=='C' or fn[i]=='c'):
			c1[2]+=1
		elif(fn[i]=='D' or fn[i]=='d'):
			c1[3]+=1
		elif(fn[i]=='E' or fn[i]=='e'):
			c1[4]+=1
		elif(fn[i]=='F' or fn[i]=='f'):
			c1[5]+=1
		elif(fn[i]=='G' or fn[i]=='g'):
			c1[6]+=1
		elif(fn[i]=='H' or fn[i]=='h'):
			c1[7]+=1
		elif(fn[i]=='I' or fn[i]=='i'):
			c1[8]+=1
		elif(fn[i]=='J' or fn[i]=='j'):
			c1[9]+=1
		elif(fn[i]=='K' or fn[i]=='k'):
			c1[10]+=1
		elif(fn[i]=='L' or fn[i]=='l'):
			c1[11]+=1
		elif(fn[i]=='M' or fn[i]=='m'):
			c1[12]+=1
		elif(fn[i]=='N' or fn[i]=='n'):
			c1[13]+=1
		elif(fn[i]=='O' or fn[i]=='o'):
			c1[14]+=1
		elif(fn[i]=='P' or fn[i]=='p'):
			c1[15]+=1
		elif(fn[i]=='Q' or fn[i]=='q'):
			c1[16]+=1
		elif(fn[i]=='R' or fn[i]=='r'):
			c1[17]+=1
		elif(fn[i]=='S' or fn[i]=='s'):
			c1[18]+=1
		elif(fn[i]=='T' or fn[i]=='t'):
			c1[19]+=1
		elif(fn[i]=='U' or fn[i]=='u'):
			c1[20]+=1
		elif(fn[i]=='V' or fn[i]=='v'):
			c1[21]+=1
		elif(fn[i]=='W' or fn[i]=='w'):
			c1[22]+=1
		elif(fn[i]=='X' or fn[i]=='x'):
			c1[23]+=1
		elif(fn[i]=='Y' or fn[i]=='y'):
			c1[24]+=1
		elif(fn[i]=='Z' or fn[i]=='z'):
			c1[25]+=1
		elif(fn[i]=='A' or fn[i]=='a'):
			c1[26]+=1
		i+=1


	i=0
	while(i<n2):
		if(sn[i]=='A' or sn[i]=='a'):
			c2[0]+=1
		elif(sn[i]=='B' or sn[i]=='b'):
			c2[1]+=1
		elif(sn[i]=='C' or sn[i]=='c'):
			c2[2]+=1
		elif(sn[i]=='D' or sn[i]=='d'):
			c2[3]+=1
		elif(sn[i]=='E' or sn[i]=='e'):
			c2[4]+=1
		elif(sn[i]=='F' or sn[i]=='f'):
			c2[5]+=1
		elif(sn[i]=='G' or sn[i]=='g'):
			c2[6]+=1
		elif(sn[i]=='H' or sn[i]=='h'):
			c2[7]+=1
		elif(sn[i]=='I' or sn[i]=='i'):
			c2[8]+=1
		elif(sn[i]=='J' or sn[i]=='j'):
			c2[9]+=1
		elif(sn[i]=='K' or sn[i]=='k'):
			c2[10]+=1
		elif(sn[i]=='L' or sn[i]=='l'):
			c2[11]+=1
		elif(sn[i]=='M' or sn[i]=='m'):
			c2[12]+=1
		elif(sn[i]=='N' or sn[i]=='n'):
			c2[13]+=1
		elif(sn[i]=='O' or sn[i]=='o'):
			c2[14]+=1
		elif(sn[i]=='P' or sn[i]=='p'):
			c2[15]+=1
		elif(sn[i]=='Q' or sn[i]=='q'):
			c2[16]+=1
		elif(sn[i]=='R' or sn[i]=='r'):
			c2[17]+=1
		elif(sn[i]=='S' or sn[i]=='s'):
			c2[18]+=1
		elif(sn[i]=='T' or sn[i]=='t'):
			c2[19]+=1
		elif(sn[i]=='U' or sn[i]=='u'):
			c2[20]+=1
		elif(sn[i]=='V' or sn[i]=='v'):
			c2[21]+=1
		elif(sn[i]=='W' or sn[i]=='w'):
			c2[22]+=1
		elif(sn[i]=='X' or sn[i]=='x'):
			c2[23]+=1
		elif(sn[i]=='Y' or sn[i]=='y'):
			c2[24]+=1
		elif(sn[i]=='Z' or sn[i]=='z'):
			c2[25]+=1
		elif(sn[i]=='A' or sn[i]=='a'):
			c2[26]+=1
		i+=1

	i=0
	while(i<26):
		if(c1[i]==c2[i]):
			c1[i]=0
			c2[i]=0
		elif(c1[i]>c2[i]):
			c1[i]=c1[i]-c2[i]
			c2[i]=0
		elif(c2[i]>c1[i]):
			c2[i]=c2[i]-c1[i]
			c1[i]=0
		i+=1

	i=0
	count=0
	while(i<26):
		count+=c1[i]
		count+=c2[i]
		i+=1

	fl=[1,1,1,1,1,1]
	i=-1
	x=-1
	tp=count-1
	while(1):
		i+=1
		if(fl[i]==1):
			x+=1
		if(i==5 and x<tp):
			i=-1
		if(x==tp):
			fl[i]=0
			if(fl==[1,0,0,0,0,0] or fl==[0,1,0,0,0,0] or fl==[0,0,1,0,0,0] or fl==[0,0,0,1,0,0] or fl==[0,0,0,0,1,0] or fl==[0,0,0,0,0,1]):
				break
			elif(i==5):
				x=-1
				i=-1
			else:
				x=-1

	if(fl==[1,0,0,0,0,0]):
		print(fn+" and "+sn+" are Friends")
		messagebox.showinfo("Flames Result",fn+" and "+sn+" are Friends")
	elif(fl==[0,1,0,0,0,0]):
		print(fn+" and "+sn+" are Lovers")
		messagebox.showinfo("Flames Result",fn+" and "+sn+" are Lovers")
	elif(fl==[0,0,1,0,0,0]):
		print(fn+" and "+sn+" are just having Attraction")
		messagebox.showinfo("Flames Result",fn+" and "+sn+" are just having Attraction")
	elif(fl==[0,0,0,1,0,0]):
		print(fn+" and "+sn+" will Marry")
		messagebox.showinfo("Flames Result",fn+" and "+sn+" will Marry")
	elif(fl==[0,0,0,0,1,0]):
		print(fn+" and "+sn+" are Enemies")
		messagebox.showinfo("Flames Result",fn+" and "+sn+" are Enemies")
	elif(fl==[0,0,0,0,0,1]):
		print(fn+" and "+sn+" are Brother and Sister")
		messagebox.showinfo("Flames Result",fn+" and "+sn+" are Brother and Sister")





b=Button(top,text="Match It!",font=8,bg="blue",fg="white",command=fun)
b.place(x=150,y=180)


top.mainloop()
