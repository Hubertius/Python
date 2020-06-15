file_liczby_1 = open("Liczby1.txt","r")
file_liczby_2 = open("Liczby2.txt","r")
file_porownanie = open("Porownanie.txt","w+")
list_1 = file_liczby_1.readlines()
length_1 = len(list_1)
list_2 = file_liczby_2.readlines()
length_2 = len(list_2)
length = 0
if length_1 > length_2:
    length = length_2
else:
    length = length_1
for i in range (0,length):
    if list_1[i] == list_2[i]:
        file_porownanie.write(list_1[i])
file_porownanie.seek(0)
n = file_porownanie.tell()
#print(n)
file_porownanie.seek(n,0)
file_porownanie.write('0')
file_porownanie.seek(0,0)
print(file_porownanie.read())
exit(0)


