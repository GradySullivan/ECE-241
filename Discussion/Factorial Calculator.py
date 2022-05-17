num = int(input("Input x for f(x)!: ")) #input number for factorial

def factorial(n):
    if n > 1:
        return n * factorial(n-1) #recursion
    else:
        return 1

print(factorial(num))