# factorial number

def factorial(num):
    l = list(range(num + 1))
    return sum(l)

print(factorial(3))

print(factorial(5))

# using deferent 

def fac(num):
    l = list(range(num + 1))
    if num < 1:
        return 1
    else: 
        num = num * fac(num - 1)
        return num 

print(fac(3));