# Bulding a Recursive Function that calculate the leats commom multiple between two numbers

from greatest_common_divisor import gcd

def lcm(x, y):
    return (abs(x * y)) / gcd(x, y)

print(lcm(125, 35))