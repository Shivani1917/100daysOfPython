# Program to know the list is monotonic or not

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

def monotonic(a):
    return (all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or all(a[i] >= a[i + 1] for i in range(len(a) - 1)))

print((monotonic(a)))