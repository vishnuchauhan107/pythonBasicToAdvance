def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1);
num = 5
print("Factorial of", num, "is",fact(num) )
# Factorial of 5 is 120
