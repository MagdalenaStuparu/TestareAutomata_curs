# # 1.Funcție care să calculeze și să returneze suma a două numere
# def aduna(x,y):
#      return x+y
#
# suma = aduna(15,100)
# print(suma)
#
#
#
# # 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# # def estenrPar(n):
# #     if n%2 == 0:
# #         return True
# #     else:
# #         return False
# #
# # print(estenrPar(1202))
#
# # 3. Funcție care returnează numărul total de caractere din numele tău complet.
# # (nume, prenume, nume_mijlociu)
#
# def calculeaza_lungime(nume, prenume, nume_mijlociu):
#        return len(nume+prenume+nume_mijlociu)
# numar_caractere=calculeaza_lungime('Stuparu', 'Magdalena', 'Maria')
# print(numar_caractere)
#
#
#
# # 4. Funcție care returnează aria dreptunghiului
# def aria_dreptunghi(L,l):
#     return L*l
# a=aria_dreptunghi(4,2)
# print(a)
#
#
# # 5. Funcție care returnează aria cercului
# import math
#
# def arie_cerc(raza):
#     return math.pi*raza*raza
# a=arie_cerc(3)
# print(a)
#
# # 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
# def cauta(x,a):
#      return x in a
# gasit=cauta('r', 'piersica')
# print(gasit)
#
#
# # 7. Funcție fără return, primește un string și printează pe ecran:
# #  Nr de caractere lower case este x
# #  Nr de caractere upper case exte y
#
#
# # def lower_upper():
# #      prop=input('Introduceti stringul: ')
# #      x=('')
# #      y=('')
# #      for i in range (len(prop)):
# #          if prop[i]==prop[i].lower():
# #              x+=prop[i]
# #          else:
# #              y+=prop[i]
# #      print(f'Nr de caractere lower case este {len(x)}')
# #      print(f'Nr de caractere upper case este {len(y)}')
# # lower_upper()
#
#
#
# # 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# # numerele pozitive
#
# def numere_pozitive(lista):
#      lista_pozitive =[ ]
#      for n in lista:
#          if n >0:
#              lista_pozitive.append(n)
#      return lista_pozitive
#
# lista_noua=numere_pozitive([2,5,7,-3,2])
# print(lista_noua)
#
#
# # 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# # Primul număr x este mai mare decat al doilea nr y
# # Al doilea nr y este mai mare decat primul nr x
# # Numerele sunt egale.
# def comparare (x,y):
#      if x>y:
#       print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
#      elif y>x:
#       print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#      else:
#       print('Numerele sunt egale')
#
# comparare(6,3)
# comparare(3,6)
# comparare(7,7)
#
#
# # 10. Funcție care primește un număr și un set de numere.
# # Printeaza ‘am adaugat numărul nou în set’ + returnează True
# # Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# # returnează False
# def adauga(n,sn):
#     if n in sn:
#         print('Nu am adaugat numărul în set.Acesta există deja')
#         return False
#     else:
#         sn.add(n)
#         print('Am adaugat numărul nou în set')
#         return True
#
#
# grup = {3,8,7}
# nr_adaugat = adauga(5,grup)
# print(nr_adaugat)
#

#
# num_list=[10, 20,33, 46, 55]
# print("lista este", num_list)
# for num in num_list:
#     if num% 5==0:
#         print(num)

# n=6
# for i in range(1,11,1):
#     product= i*6
#     print(pro1
#     2
#     3
#     duct)
#
# x = input()
# y = input()
# z = input()
# sum = x + y + z
# if x==y==z:
#     sum=sum*3
# print(sum)
#
# rows=5
# for i in range(0, rows):
#     for j in range(0, i, +1):
#         print("*", end=' ')
#     print("/r")
# for i in range(rows, 0, -1):
#     for j in range(0, i, +1):
#         print("*", end=' ')
#     print("/r")

for i in range(4,0,-2):
    print(i)
