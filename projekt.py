import os
#zamiast funkcji len() można uzyć zapytania do uzytkownika o ilość liczb ale funkcja len jest wygodniejsza
wyniki = []
def znajdz(x):
    for x in range(0,len(list1)):
         ilosc = 0 #dodatkowa zmienna pomocnicza do zliczania wystąpień x
         for i in range(0,len(list1)):
             if x==list1[i]: # tutaj musi być x a nie jak wcześniej list[x] by elementy sie nie powtarzały i by szukano powtarzających się elementów tylko z przedziału zawartego w zadaniu
                 ilosc +=1
         if ilosc==2:
             wyniki.append(x) # tutaj jakby dodać brake to znajdzie pierwszy powtarzajacy sie element i zakonczy szukanie dalej
#deklaracja list
list1 = []
wyniki = []
f=open("plik.txt") # otwarcie pliku
for x in f:
    x = x.replace("\n", "")
    list1.append(int(x)) #dodawanie do listy elementów które są oddzielane znakiem /n czyli enterem(są w nowej lini)
znajdz(list1)
zapis = open("wyniki.txt", "w")
zapis.write("Powtarzające się liczby w podanym pliku w którym rozważamy tylko liczby od 1 do n-1, gdzie n jest ilością liczb to: \n")
#zapis wyników do pliku "wyniki"
for i in wyniki:
    zapis.write(str(i)+", ")
zapis.close
#ogólnie całą funkcję znajdź można zstąpić wyrażeniem
#    for x in range(0,len(list1)):
#        if list1.count(x)>=2:
#            print(x)
#            wyniki.append(x) co wydawałoby mi się najlepszym rozwiązaniem