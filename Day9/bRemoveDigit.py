#  Program for Removing Specific Digit from every element 

a = []
n = int(input("Enter number of elements: "))

print("Enter elements of the list")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(a)

n1 = int(input("Digit to be removed:"))


res = []
for ele in a:
	x = str(ele).replace(str(n1), '')
	res.append(int(x))

print("Modified List : " + str(res))
