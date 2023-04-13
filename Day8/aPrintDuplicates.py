#  Program for Increamenting Numeric String

a = []
n = int(input("Enter number of elements: "))

print("Enter elements of the list")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(a)

n1 = int(input("Increament of "))

def Increment_Numeric_String(Test_list, n1):
    Result = []
    for ele in Test_list:
        if ele.isDigit():
            Result.append(str(int(ele)+n1))
        else:
            Result.append(ele)
    return Result

print(Increment_Numeric_String(a, n1))

