
# 1.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale=note_muzicale[::-1]
print(note_muzicale)

 #2
 #de cate ori apare do in lista

print(note_muzicale.count('do'))

#3

prima_lista = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
#prima varianta
lista_finala = prima_lista + lista_2
print(lista_finala)
# a doua varianta
prima_lista.append(lista_2)
print(prima_lista)

# 4
prima_lista = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_finala = prima_lista + lista_2
lista_finala.sort()
print(f' print dupa prima sortare: {lista_finala}')
lista_finala.pop(0)
print(lista_finala)

#5
prima_lista = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_finala = prima_lista + lista_2
lista_finala.sort()
print(f' print dupa prima sortare: {lista_finala}')
if lista_finala == []:
 print(f'lista este goala')
else:
 print(f'Lista nu este goala')

 #6
lista_finala = [0, 1, 2, 3, 4, 5, 6]
lista_finala.clear()
print(lista_finala)

#7
prima_lista = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_finala = prima_lista + lista_2
lista_finala.sort()
print(f' print dupa prima sortare: {lista_finala}')
if lista_finala == []:
 print(f'lista este goala')
else:
 print(f'Lista nu este goala')

 #8
 dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
 print(dict1.keys())

#9
print(f'Ana a luat nota',  dict1['Ana'])
print(f'Gigel a luat nota',  dict1['Gigel'])
print(f'Dorel a luat nota',  dict1['Dorel'])

#10
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f'Dorel a luat nota',  dict1['Dorel'])
dict1.update({'Dorel' : 6})
print(f'Noua nota a lui Dorel este',  dict1['Dorel'])

#11
#il scoatem pr Gigel
dict1.pop('Gigel')
print(dict1)
 # il adaugam pe Ionica care are nota 9
dict1['Ionica']=9
print(dict1)

#12
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# in Set nu pot fi duplicate
print(zile_sapt)

#13
if zile_sapt > weekend:
 print(f'weekend Nu este un subset al variabilei zile_sapt')
else:
 print(f'weekend este un subset al variabilei zile_sapt ')

 #14
i= zile_sapt.difference(weekend)
print(i)

#15
i= zile_sapt.intersection(weekend)
print(i)






