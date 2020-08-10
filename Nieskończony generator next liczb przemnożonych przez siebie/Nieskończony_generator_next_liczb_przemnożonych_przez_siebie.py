"""
Nieskończony generator kolejnych liczb przemnożonych przez siebie (1,4,9,16,25,36 itd)
Skorzystaj z funkcji generując 20 elementów, po czym wróć do momentu zakończenia i wygeneruj następnie 30 liczb. Zapisz wygenerowane elementy w tej samej liście
"""
def generate_subside_numbers():
    i = 1
    while True:
        x = i
        x **= 2
        i += 1
        yield x
a = generate_subside_numbers()
list = []
for i in range(20):
    list.append(next(a))
print(list)
for i in range(30):
    list.append(next(a))
print(list)
exit(0)

