#Run in python 3
a=input("list A\n")
a=a.split(',')
b=input("list B\n")
b=b.split(',')
check=0

for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==b[j]:
			check+=1
		else:
			check+=0


if check>=len(b):
	print("true")

if check<len(b):
	print("False")
