def persistence(n):
    if len(str(n)) == 1:
        return 0
    count = 0
    while True:
        multiply = 1
        for i in str(n):
            multiply *= int(i)
        count += 1
        if multiply <= 9:
            return count
        n = multiply

print(persistence(27))