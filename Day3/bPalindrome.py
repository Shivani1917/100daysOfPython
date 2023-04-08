# Program to display the  number Palindrome or not

number = int(input("Enter a number: "))
rev = 0
original = number

while number >0:
    digit = number % 10
    rev = rev * 10 + digit
    number = number // 10

if rev == original:
    print("The number", rev ," is Palindrome")
else:
    print("The number", rev ,"is not Palindrome")