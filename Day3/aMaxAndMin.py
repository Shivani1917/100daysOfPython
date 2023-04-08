# Program to display the  number in the list is minimum and maximum

list = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	list.append(element)

print(list)

print("Maximum element in the list: ", max(list))
print("Minimum element in the list: ", min(list))
