# Program for Cumulative Sum of list

a = []
n = int(input("Enter number of elements: "))

print("Enter elements of the list")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(a)

def cumulativeSum(a):
    sum = 0
    ele = []
    for i in range(len(a)):
        sum += a[i]
        i += i
        ele.append(sum)
    return ele

print("The cumulative sum of list: ", cumulativeSum(a))
