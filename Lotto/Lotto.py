"""
Napisz funkcję, która zasymuluje jak działa Lotto.
Wybierasz 6 unikalnych liczb z 49
"""
import random
def choose_values(how_many, max_range):
    print(random.sample(range(max_range + 1),how_many))
choose_values(6,49)
exit(0)
