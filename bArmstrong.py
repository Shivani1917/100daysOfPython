# Program to display the  number is Armstrong or not

number = int(input("Write a number: "))


def find_armstrong(num):
    if num in range(1,10):
        return True

    original = num
    count = len(str(num))
    sum = 0

    while num > 0:
       digit = num % 10
       sum += digit ** count
       num = num // 10
    
    if sum == original:
       return True
    else:
        return False

if find_armstrong(number):
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number")

    