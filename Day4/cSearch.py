# Program for Searching elements in a list

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

print(a)

number = int(input("Enter number to be searched : "))

if a.index(number) == True:
	print("The number is present in the list")