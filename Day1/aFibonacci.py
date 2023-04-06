# Program to display the Fibonacci sequence up to n-th term

#number of terms 
n= int(input("Enter number of terms:"))

n1 = 0
n2 = 1
count = 0

if n <= 0:
    print("This term is not acceptable")
elif n == 1:
    print("The fibonacci series", n1)
else:
      print("The fibonacci series")
      while count < n:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1



