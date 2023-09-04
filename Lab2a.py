n=int(input("Enter the value of n")) 
der fibonacci(n) 
    if n<2:
       return 1
    return fibonacci(n-1) + fibonacci(n-2) 
print(0, end='') 
for i in range (n-1):
      print(fibonacci (i), end='')
