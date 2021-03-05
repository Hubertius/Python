def readint(prompt, min, max):
    try:
        value = int(input("Your input: "))
        assert value >= min and value <= max
    except AssertionError:
        print("Błąd: podana liczba jest spoza dozwolonego zakresu (min..max)")
        exit(1)
    except:
        print("Błąd: wprowadzono nieprawidłową liczbę")
        exit(1)
    return value


v = readint("Podaj liczbe od -10 do 10: ", -10, 10)

print("Liczba to:", v)
