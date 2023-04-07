# Program to display the  number is Fibonacci or not

num = int(input("Write a number: "))

import math

def isPerfectSquare(number):
    s = int(math.sqrt(number))
    return s*s == number

def isFibonacciNumber(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

if isFibonacciNumber(num) == True:
    print("This is a fibonacci number")
else:
    print("This is not a fibonacci number")