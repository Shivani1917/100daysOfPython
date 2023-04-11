#  Program to find Occurrences of elements.

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

print(a)


x = int(input("Enter the element to be checked: "))

def countOccurance(a, x):
    count = 0
    for i in a:
        if (i == x):
          count = count +1
    return count


print("The occurance of", x , "is", countOccurance(a,x))
