# Program to display the Factorial of n-th term

n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Take positive value or 0")
elif 0 <= n <= 1:
    print("The factorial of ", n, " is ", fact)
else:
    print("The factorial for ", n , " is ")    
    while n >= 1:
        fact = fact * n
        n -= 1    
print(fact)     
  

       
