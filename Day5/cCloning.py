#  Program for Cloning/Copying the list

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

print(a)

# function to clone a list

def cloneList(a):
    b = list(set(a))
    return b

print("The clonned list:", cloneList(a))