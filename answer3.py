#Run in python 3
a=1
b=1
f=[]
# Append a list to store input and change input to be integer
list=input("Numbers:")
list=list.split(',')
list = [ int(x) for x in list ]

#prepare a list to store the first 60 fibonacci numbers
for i in range(60):
	c=a+b
	a=b
	b=c
	f.append(c)

# If input list include 1 then print 2
if 1 in list:
	print (2)
 
 #Check input in list>2,check if the number is within the boundary of f[i] and f[i+1],if yes,then print out f[i+1]
for j in range(len(list)):
	for i in range(len(f)):
		if (list[j]>f[i] and list[j]<f[i+1]) or list[j]==f[i]:
			print (f[i+1])