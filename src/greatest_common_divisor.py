# Bulding a Recursive Function that calculate the greatest commom divisor between two numbers

def gcd(x, y):
    if y == 0:
        return x
    elif x > y:
        j = x % y
        return gcd(y, j)
    else:
        return None
    
print(gcd(125, 35))