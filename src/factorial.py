# Bulding a Recursive Function that calculate the factorial of a number

def factorial(number):
    # base case to stop the recursion
    if number <= 1:
        return 1
    

    return number * factorial(number - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))

# Here we break our code surpassing the call back's recursion limit
print(factorial(1000))