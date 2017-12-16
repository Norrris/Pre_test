#Run in python 3
#Initialize 2 list(listA is the set,list B is the testing list) and split the list by ,
a=input("list A\n")
a=a.split(',')
b=input("list B\n")
b=b.split(',')
check=0

# If there are same element,check+1
for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==b[j]:
			check+=1

# If ckheck is larger or equal to length of the subset list, it means it is the subset of list A,else it is not.
if check>=len(b):
	print("true")

if check<len(b):
	print("False")
