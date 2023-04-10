# Program to find second largest element in the list

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

print(a)

b = list(set(a))

b.sort()

print("Second largest number in the list: ", b[-2])