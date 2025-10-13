def factorial(n):
    
    if n < 0:
        return 
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

a1 = int(input("Enter your number:- "))
print("The factorial of {} is {}".format(a1, factorial(a1)))