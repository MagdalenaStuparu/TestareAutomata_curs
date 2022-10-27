# 1.

# 2.
'''
x = int(input('Introduceti valoarea lui x '))
if int(x) >= 0:
    print('x este numar natural')
else:
    print('x este numar impar')
'''

# 3.
'''
x = int(input('Introduceti valoarea lui x '))
if int(x) < 0:
    print('x este numar negativ')
elif int(x) > 0:
    print('x este numar pozitiv')
else:
    print('x este numar neutru')
'''

# 4.
'''
x = int(input('Introduceti valoarea lui x '))
if int(x) > -2 and int(x) < 13:
    print('x este intre -2 si 13')
else:
    print('x nu este intre -2 si 13')
'''

# 5.
'''
x = int(input('x este '))
y = int(input('y este '))
diferenta = x-y
if int(diferenta) < 5:
    print('Diferenta dintre x si y este mai mica decat 5')
else:
    print('Diferenta dintre x si y nu este mai mica decat 5')
'''

# 6.
# x = int(input('Introduceti valoarea lui x '))
# if not int(x) < 5 and not int(x) >27:
#     print('X este intre 5 si 27')
# else:
#     print('X nu este intre 5 si 27')


# 7.
'''
x = int(input('Introduceti valoarea lui x '))
y = int(input('Introduceti valoarea lui y '))
if x == y:
    print('Numerele sunt egale')
elif x < y:
    print(f'{y} este mai mare decat {x}')
else:
    print('X este mai mare decat y')
'''

# 8.
# xy = int(input('Introduceti cat este latura XY '))
# yz = int(input('Introduceti cat este latura YZ '))
# xz = int(input('Introduceti cat este latura XZ '))
# if xy == yz and xy != xz and yz != xz:
#     print('Triunghiul este isoscel')
# elif xy == xz and xy != yz and yz != xz:
#     print(' Triunghiul este isoscel')
# elif yz == xz and xy != xz and xy != xz:
#     print('Triunghiul este isoscel')
# elif xy == yz == xz:
#     print('Triunghiul este echilateral')
# else:
#     print('Triunghiul este oarecare')

# 9.
'''
litera = str(input('Introduceti o litera: '))
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print('Litera este o vocala')
else:
    print('Litera este o consoana')
'''


# 10.
note_initiale = list(map(int, input('Introduceti notele: ').split()))
print(f'Notele in sistem romanesc: {note_initiale}')

for i in range(len(note_initiale)):

 if note_initiale[i] < 0 or note_initiale[i] > 10:
    print('Nota introdusa nu este corecta: ')
note_initiale[i] = int(input('Reintroduceti nota: '))

for i in range(len(note_initiale)):
if note_initiale[i] <= 4:
    note_initiale[i] = 'F'
elif 4 < note_initiale[i] <= 6:
    note_initiale[i] = 'E'
elif 6 < note_initiale[i] <= 7:
    note_initiale[i] = 'D'
elif 7 < note_initiale[i] <= 8:
    note_initiale[i] = 'C'
elif 8 < note_initiale[i] <= 9:
    note_initiale[i] = 'B'
else:
    note_initiale[i] = 'A'
print(f'Notele in sistem european: {note_initiale}')


