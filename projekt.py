import random
import os
wyniki = []
def znajdz(x):
    for x in range(0,len(list1)):
         for i in range(0,len(list1)):
             ilosc = 0
             if int(list1(x))==int(list1(i)):
                 ilosc+=1
             if ilosc>=2:
                 print(list1(x))
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
