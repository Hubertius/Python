import math

def is_square(n):   
    if n < 0:
        return False 
    number = math.isqrt(n)
    if number**2 == n:
        return True
    return False

print(is_square(25))