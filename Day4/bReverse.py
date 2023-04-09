# Program for Reversing a list

a = []
n = int(input("Enter number of elements : "))

print("Enter elements of the list")
for i in range(0, n):
	element = int(input())
	a.append(element)

print(a)

def Reverse(a):
	new_a = a[::-1]
	return new_a

    
print(Reverse(a))

