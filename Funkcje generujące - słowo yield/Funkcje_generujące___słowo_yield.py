# yield - pozwala nam generować dokładnie od momentu, w którym ostatni raz wywołaliśmy next( ... )
#... - kolejne wywołanie obiektu, np. next(a)
def generate_number_with_yield():
    for number in range(400):
        if number % 2 == 0:
            yield number
a = generate_number_with_yield()
for i in range(10):
    print(next(a))
exit(0)

