#Run in python 3
a=1
b=1
f=[]
list=input("Numbers:")
list=list.split(',')
list = [ int(x) for x in list ]

for i in range(60):
	c=a+b
	a=b
	b=c
	f.append(c)

if 1 in list:
	print (2)

for j in range(len(list)):
	for i in range(len(f)):
		if (list[j]>f[i] and list[j]<f[i+1]) or list[j]==f[i]:
			print (f[i+1])