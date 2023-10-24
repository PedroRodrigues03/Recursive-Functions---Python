# Bulding a Recursive Function that calculate the fibonacci sequence 

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


for i in range(11):
    result = fibonacci(i)
    print(f'Fibonacci({i}) = {result}')