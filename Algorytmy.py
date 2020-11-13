import random
import os
wyniki = []
def znajdz(x):
    list1.sort()
    for x in range(0,len(list1)):
         if list1.count(x)>=2:
            print(x)
            wyniki.append(x)
list1 = []
wyniki = []
f=open("plik.txt")
for x in f:
    x = x.replace("\n", "")
    list1.append(int(x))
znajdz(list1)
zapis = open("wyniki.txt", "w")
zapis.write("Powtarzające się liczby w podanym pliku w którym rozważamy tylko liczby od 1 do n-1, gdzie n jest ilością liczb to: \n")
for i in wyniki:
    zapis.write(str(i)+", ")
zapis.close
