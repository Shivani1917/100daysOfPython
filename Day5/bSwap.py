#  Program to Swap first element with last element in a list

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

print(a)

#function for swapping element
def swapElements(list):
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
    return list

print("The swapped list", swapElements(a))