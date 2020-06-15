table = [3,4,3,5,6,3]
len = 6
count = 0
for i in range(0,3):
    j = (len - 1) - i
    temp = table[i]
    table[i] = table[j]
    table[j] = temp
for i in range(0,6):
    if table[i] == 3:
        count += 1
print("Tablica: ",table)
print("Tyle wystapilo trojek: ",count)
exit(0)
