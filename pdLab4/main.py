import math
import random

# Zad 1

# liczby = [random.randint(0,31) * 2 for x in range(0,21)]
# plik = open("packet/text.txt", "w+")
# plik.write(str(liczby))
# znaki = plik.read(10)

# Zad 2

# plik = open("packet/text.txt", "r")
# znaki = plik.read(100)
# linia = plik.readline(100)
# print(znaki)


# Zad 3

# with open("packet/text.txt", "w+") as plik:
#     for linia in plik:
#         print(linia,end="")

# Zad 4

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jednego):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jednego = cena_jednego

#     def wyswietl_produkt(self):
#         print("Nazwa: %(a)s Ilość: %(b)s Jednostka pomiaru: %(c)s Cena: %(d)s zl" % {'a' : self.nazwa_produktu, 'b' : self.ilosc, 'c' : self.jednostka_miary, 'd' : self.cena_jednego})

#     def ile_produktu(self):
#         print("%(a)s%(b)s" % {'a' : self.ilosc, 'b' : self.jednostka_miary})

#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jednego

# mandarynki = NaZakupy(nazwa_produktu="mandarynki", ilosc=8, jednostka_miary="kg", cena_jednego=0.8)
# print(mandarynki.wyswietl_produkt())
# print(mandarynki.ile_produktu())
# print(mandarynki.ile_kosztuje())

# Zad 5

# class Ciagi:
#     def __init__(self, a1, r, n, ile):
#         self.a1 = a1
#         self.r = r
#         self.n = n
#         self.ile = ile

#     def wyswietl_dane(self):
#         print('a1 = %(a)d' % {'a' : self.a1})
#         print('r = %(b)d' % {'b' : self.r})
#         print('n = %(c)d' % {'c' : self.n})
#         print('ile = %(d)d' % {'d' : self.ile})

#     def pobierz_element(self):
#         self.ile = int(input("Podaj element ciągu: "))

#     def pobierz_parametry(self):
#         self.a1 = int(input("Pierwsza liczba ciagu: "))
#         self.r = int(input("Różnica liczb w ciągu: "))
#         self.n = int(input("Liczba elementów ciągu: "))

#     def suma(self):
#         return ((self.a1 + ((self.a1 + (self.n - 1)) * self.r)) / 2) * self.n

#     def policz_elementy(self):
#         an = self.a1
#         for x in range(self.ile):
#             k = an + self.r
#             an = k
#             print(k)

# ciag = Ciagi(a1 = 1, r = 4, n = 10, ile = 0)
# print(ciag.suma())
# print(ciag.wyswietl_dane())

# print(ciag.policz_elementy())
# print(ciag.pobierz_parametry())

# print(ciag.suma())
# print(ciag.policz_elementy())
# print(ciag.wyswietl_dane())

# Zad 6

class Robaczek:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def w(self, move):
        self.y += move
        text = ('Robaczek moves %(a)d steps up' % {'a': move})
        return text
    def a(self, move):
        self.x -= move
        text = ('Robaczek moves %(a)d steps left' % {'a': move})
        return text

    def s(self, move):
        self.y -= move
        text = ('Robaczek moves %(a)d steps down' % {'a': move})
        return text

    def d(self, move):
        self.x += move
        text = ('Robaczek moves %(a)d steps right' % {'a' : move})
        return text

    def xy(self):
        return (self.x, self.y)

    def target(self):


play = Robaczek(0, 0)
print(play.xy())

print(play.w(7))
print(play.d(7))
print(play.xy())

print(play.w(7))
print(play.a(7))
print(play.xy())

print(play.s(14))
print(play.xy())