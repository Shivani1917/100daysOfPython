#  Program to remove multiple elements

a = []
n = int(input("Enter number of elements: "))

print("Enter elements of the list")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(a)

n1 = int(input("Enter the first element to be removed: "))
n2 = int(input("Enter the second element to be removed: "))

def removeMultipleElements(a, n1, n2):
    a = [i for i in a if i != n1 and i != n2]
    return a

result = removeMultipleElements(a, n1, n2)
if len(result) == len(a):
    print("The elements are not present")
else:
    print("The list after removing multiple elements:", result)
