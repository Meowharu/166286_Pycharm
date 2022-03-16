import math
# kwadraty liczb od 0 do 9
# a=[]
# for x in range(0,10):
#     a.append(x**2)
# print(a)
# a2=[x**2 for x in range(0,10)]
# print(a2)

# b=[]
# for x in range(0,6):
#     b.append(3**x)
# print(b)
# b2=[3**x for x in range(0,6)]
# print(b2)

# c=[]
# for x in a:
#     if x%2!=0:
#         c.append(x)
# print(c)
# c2=[x for x in a if x%2!=0]
# print(c2)

# lista=[]
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a,b))
# print(lista)
# lista2=[(a,b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# slownik={"PZU":"Państwowy zakład ubezpieczeń",
#                "ZUS":"Zakład ubezpieczeń społecznych",
#                      "PKO":"Państwowa kasa oszczędności" }
# print(slownik)
# slownik_odwrocony={}
# for key, value in slownik.items():
#     slownik_odwrocony[value]=key
# print(slownik_odwrocony)
# slownik2={value:key for key, value in slownik.items()}
# print(slownik2)

# def row_kwadratowe(a, b, c):
#     delta=b**2-4*a*c
#     if delta<0:
#         print('brak rozwiązań')
#         return -1
#     elif delta==0:
#         print('jedno rozwiązanie')
#         x=(-b)/(2*a)
#         return x
#     else:
#         print('dwa rozwiązania')
#         x1=((-b)-math.sqrt(delta))/(2*a)
#         x2=((-b)+math.sqrt(delta))/(2*a)
#         return x1, x2
# print(row_kwadratowe(6, 1, 3))
# print(row_kwadratowe(1, 2, 1))
# print(row_kwadratowe(1, 4, 1))

# def parzyste(a):
#     if a%2==0:
#         print('liczba parzysta')
#         return 1
#     else:
#         print('liczba nieparzysta')
#         return 0
# print(parzyste(10))
# print(parzyste(9))

# def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
#     return math.sqrt((x2-x1)**2+(y2-y1)**2)
# # argumenty domyslne
# print(dlugosc_odcinka())
# # argumenty pozycyjne
# print(dlugosc_odcinka(1, 2, 3, 4))
# print(dlugosc_odcinka(2, 2, y2=2, x2=1))
# # argumenty nie w kolejnosci
# print(dlugosc_odcinka(y2=3, y1=2, x1=8, x2=2))
# # reszta argumentow wartosci domyslne
# print(dlugosc_odcinka(x2=2, y2=3))

# def ciag(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         suma=0
#         for i in liczby:
#             suma+=i
#         return suma
# print(ciag())
# print(ciag(1,2,3,4,5,6,7))

def co_lubie(** rzeczy):
    for cos in rzeczy:
        print('to jest')
        print(cos)
        print('co lubie')
        print(rzeczy[cos])
co_lubie(sloczycze='czekolada', gry=['lol','cs'])