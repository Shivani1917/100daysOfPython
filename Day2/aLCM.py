# Program to display the  of two numbers

number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2ndnumber: "))

def findLCM(num1,num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1,smaller + 1):
        if ((num1%i==0) and (num2%i==0)):
           hcf = i
           lcm = (num1 * num2)/hcf 

    return lcm

print(findLCM(number1,number2))
