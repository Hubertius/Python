iban = input("Proszę podaj IBAN: ")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("Wprowadzono niepoprawne znaki.")
elif len(iban) < 15:
    print("Wprowadzony IBAN jest za krótki.")
elif len(iban) > 31:
    print("Wprowadzony IBAN jest za długi")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban_second = ""
    for ch in iban:
        if ch.isdigit():
            iban_second += ch
        else:
            iban_second += str(10 + ord(ch) - ord('A'))
    int_iban = int(iban_second)
    if int_iban % 97 == 1:
        print("Wprowadzony IBAN jest jak najbarziej poprawny.")
    else:
        print("Wprowadzony IBAN nie jest poprawny.")
exit(0)


