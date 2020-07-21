"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
"""
import random
list_1 = []
list_2 = []
for i in range(1,101):
    n = random.randint(1,51)
    list_1.append(n)
for i in range(1,151):
    n = random.randint(1,71)
    list_2.append(n)
list_end = []
size = 1
if len(list_1) > len(list_2):
    size = len(list_2)
else:
    size = len(list_1)
for i in range(0,size):
    for j in range(0,size):
       if list_2[j] == list_1[i]:
           list_end.append(list_1[i])
final_list = list(dict.fromkeys(list_end))
print(final_list)
# Final list is ready without repeats.